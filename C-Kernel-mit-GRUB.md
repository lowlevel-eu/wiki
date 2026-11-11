# C-Kernel mit GRUB

In diesem Tutorial werde ich beschreiben, wie man einen in [C](C "C") programmierten [Kernel](Kernel "Kernel") mithilfe von [GRUB](Grand-Unified-Bootloader "GRUB") bootet.

## Hinweis für Windowsianer

Ich werde hier beschreiben, wie ich es unter [Linux](Linux "Linux") mache. Unter [Windows](Windows "Windows") geht es auch, aber du musst sicherstellen, dass du ELF als Binärformat benutzt – das heißt, du solltest dir erst entweder den Artikel [Crosscompiler für Windows](Crosscompiler-f%C3%BCr-Windows "Crosscompiler für Windows") (Verwenden von Jidders Crosscompiler) oder [Cross-Compiler](Cross-Compiler "Cross-Compiler") (Erstellen eines eigenen Crosscompilers) durchlesen und eine entsprechende Entwicklungsumgebung aufsetzen.

## Kernel

Der eigentliche Kernel soll ja in C programmiert sein. Ein Teil des Kernels muss aber immernoch in [Assembler](Assembler "Assembler") sein.

### Kernel - C

Als erstes kannst du dir einen kleinen Test-Kernel ausdenken, oder einfach den hier benutzen:

``` c
int main() {
  // Pointer zum Videospeicher
  char *video = (char*)0xB8000;
  // String zum Ausgeben
  char *hello = "Hello World";

  // Zuerst den Speicher leeren
  for(video+=4000; video !=(char*)0xB8000 ;video--)
     *video=0;

  // String ausgeben
  while (*hello) {
    *video = *hello;
    video++;
    *video = 0x07;
    video++;
    hello++;
  }

  // jetzt wo wir schon im Kernel drin sind, wollen wir auch nicht mehr raus ;)
  while (1);
  return 0;
}
```

### Kernel - Assembler

Dieser Code macht eigentlich nichts anderes als in die main-Funktion unseres C-Kernels zu springen.

``` asm
global loader ; loader für Linker sichtbar machen
extern main   ; main-Funktion des C-Kernels

FLAGS    equ 0
MAGIC    equ 0x1BADB002       ; Magicnumber - Erkennungsmerkmal für GRUB
CHECKSUM equ -(MAGIC + FLAGS) ; Checksum

section .text
align 4
MultiBootHeader:
  dd MAGIC       ; Magic number
  dd FLAGS       ; Flags
  dd CHECKSUM    ; Checksum

loader:
  mov esp,0x200000 ; Stack an die 2MB-Grenze platzieren
  push eax         ; Multiboot Magicnumber auf den Stack legen
  push ebx         ; Adresse der Multiboot-Structure auf den Stack legen
  call main        ; main-Funktion des C-Kernels aufrufen

  cli ; falls der Kernel bis hier her kommt, CPU anhalten
  hlt
```

Der Code sollte eigentlich gut verständlich sein, trotzdem ist noch was zu klären:

- Die Flags können geändert werden, am besten schaut man sich die [Multiboot](Multiboot "Multiboot")-Spezifikation an.
- Den Stack kann man natürlich an eine beliebige Stelle setzen, aber an der 2MB-Grenze wird er uns nicht stören.
- Es wird die Adresse der Multiboot-Structure nicht umsonst an den C-Kernel übergeben. Am besten liest man so ziemlich am Anfang des Kernels die Informationen aus ihr. In der Multiboot-Structure steht z. B. wie viel Speicher der Rechner hat oder welche Module von GRUB mitgeladen wurden.

## Zusammenbauen

Nun müssen wir den Kernel „zusammenbauen“. Dafür müssen wir den Assembler-Code assemblieren, den C-Code kompilieren und am Ende beides linken.

### Assemblieren

Dies geschieht ganz einfach mit diesem Befehl:

    $ nasm -f elf -o kernel_asm.o kernel.asm

Damit wird eine [ELF](Executable-and-Linking-Format "ELF")-Datei erzeugt, die wir später noch linken können.

### Kompilieren

Der C-Kernel wird mit diesem Befehl kompiliert:

    $ gcc -m32 -ffreestanding -o kernel_c.o -c kernel.c -Wall -Werror -nostdinc

Damit erstellen wir eine Objektdatei, mit der wir nachher noch linken können. Es ist wichtig, dass keine Includes und damit auch keine Funktionen aus der Standardbibliothek des Hostsystems benutzt werden. Diese müssen erst selbst implementiert werden. Eine genau Beschreibung der einzelnen Kommandozeilenparameter findet sich im [GCC Handbuch (englisch)](http://gcc.gnu.org/onlinedocs/gcc/Invoking-GCC.html#Invoking-GCC). An dieser Stelle nur so viel:

- -m32 weist gcc an, den Code für den 32-Bit-Protected-Mode (im Gegensatz zu -m64) zu erstellen
- -ffreestanding weißt gcc an nicht davon auszugehen, dass eine Standardbibliothek zur Verfügung steht
- -nostdinc weißt gcc an keine Header aus der Standardbibliothek des Hostsystems bereitzustellen

### Linken

Meiner Meinung nach ist dies der schwierigste Teil des „Zusammenbauens“. Beim Linken wird unser Assembler-Kernel und unser C-Kernel miteinander verbunden und es wird z. B. dem Assembler-Kernel auch gesagt wo die main-Funktion des C-Kernels liegt. Wir brauchen erstmal eine Konfigurationsdatei/[Linkerscript](Linker "Linkerscript") für *ld*:

    ENTRY (loader)
    OUTPUT_FORMAT(elf32-i386)
    OUTPUT_ARCH(i386:i386)

    SECTIONS
    {
      . = 0x00100000;
        
      .text :
      {
        *(.text)
      }
        
      .rodata :
      {
        *(.rodata)
      }

      .data : 
      {
        *(.data)
      }

      .bss :
      {
        _sbss = .;
        *(COMMON)
        *(.bss)
        _ebss = .;
      }
    }

Nun wird gelinkt:

    $ ld -T <LD-Konfigurationsdatei> -o kernel.bin kernel_asm.o kernel_c.o

Wenn man später mehr Dateien hat, können diese natürlich auch dazugelinkt werden. Man sollte den fertigen Kernel jetzt in einer Datei namens *kernel.bin* haben.

Mehr Informationen darüber, was genau dieses Linkerscript genau macht und warum es notwendig bzw. sinnvoll ist, findet ihr im Artikel [Linkerscript](Linker "Linkerscript"). An dieser Stelle nur so viel:

Mit „ENTRY(loader)“ wird ld mitgeteilt, dass der Kernel bei der Funktion loader (siehe [Assemblerteil des Kernels](C-Kernel-mit-GRUB#kernel---assembler "C-Kernel mit GRUB")) beginnt. Dies wird in einem Datenfeld in der ELF-Header der „kernel.bin“ festgehalten und von GRUB benötigt um zur richtigen Adresse zu springen.

Der Rest des Linkerscripts gibt an wo die Sektionen, das sind die Bereiche, welche man in Assembler mittels des „.section .text“ beispielsweise direkt angeben kann, aus den ELF-Objektdateien (kernel_asm.o und kernel_c.o) in der ELF-Binärdatei „kernel.bin“ bzw. nach dem Laden im Speicher landen. Das „. = 0x00100000;“ gibt an, dass die „kernel.bin“ an die Adresse 1 MB gelinkt wird, d. h. sich nach dem Laden durch GRUB an die Adresse 1 MB und folgende im (physischen) Speicher befindet. 1 MB ist als Adresse gewählt, da GRUB keine Dateien unter diese Adresse lädt, der Grund dafür ist, dass der Speicherbereich zwischen 0 und 1 MB durch das BIOS, den Bootloader selbst und verschiedene Hardware belegt ist. Siehe dazu auch den Artikel über [Speicherbereiche](Speicherbereiche "Speicherbereiche").

## GRUB-Image erstellen

*siehe: [GRUB legacy](Grand-Unified-Bootloader#grub-legacy "GRUB")*

Fertig ist unser GRUB-Image! Man kann es jetzt noch mit

    $ dd if=floppy.img of=/dev/fd0

auf eine Floppydisk kopieren und damit booten. Wenn alles klappt, seht ihr „Hello World“ auf dem Bildschirm.

## Vorschläge

- Auf Dauer wird es anstregend, die ganzen Befehle einzutippen. Am einfachsten ist es eine [Makefile](Makefile "Makefile") zu benutzen.
- Um nicht immer neustarten zu müssen, kann man einen Emulator wie [QEMU](QEMU "QEMU") oder [Bochs](Bochs "Bochs") nehmen. Dann muss man das Image auch erst gar nicht auf Diskette kopieren.
- Mit *color light-blue/black light-cyan/blue* in menu.lst kann man dem Bootloader Farbe verpassen.

## Nachwort

Bei Fehlern in Text oder Code bitte an das Lowlevel-Team wenden.

## Siehe auch

- [C-Kernel starten](C-Kernel-starten "C-Kernel starten")
- [Multiboot](Multiboot "Multiboot")
- [GRUB](Grand-Unified-Bootloader "GRUB")
- [C++-Kernel mit GRUB](C%2B%2B-Kernel-mit-GRUB "C++-Kernel mit GRUB")

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/11528/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1604/index.html)

<!-- MediaWiki page 1604; revision 11528; parent 8463; 2020-12-05T22:52:57Z -->
