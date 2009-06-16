# C-Kernel mit GRUB

In diesem Tutorial werde ich beschreiben wie man einen in [C](https://github.com/lowlevel-eu/wiki/wiki/C "C") programmierten [Kernel](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel") mithilfe von [GRUB](https://github.com/lowlevel-eu/wiki/wiki/Grand-Unified-Bootloader "GRUB") bootet.

## Hinweis für Windowsianer

Ich werde hier beschreiben, wie ich es unter [Linux](https://github.com/lowlevel-eu/wiki/wiki/Linux "Linux") mache. Unter [Windows](https://github.com/lowlevel-eu/wiki/wiki/Windows "Windows") geht es auch, aber du musst sicherstellen, dass du ELF als Binärformat benutzt - das heißt, du solltest dir erst entweder den Artikel [Crosscompiler für Windows](https://github.com/lowlevel-eu/wiki/wiki/Crosscompiler-f%C3%BCr-Windows "Crosscompiler für Windows") (Verwenden von Jidders Crosscompiler) oder [Cross-Compiler](https://github.com/lowlevel-eu/wiki/wiki/Cross-Compiler "Cross-Compiler") (Erstellen eines eigenen Crosscompilers) durchlesen und eine entsprechende Entwicklungsumgebung aufsetzen.

## Kernel

Der eigentliche Kernel soll ja in C programmiert sein. Ein Teil des Kernels muss aber immernoch in [Assembler](https://github.com/lowlevel-eu/wiki/wiki/Assembler "Assembler") sein.

### Kernel - C

Als erstes kannst du dir einen kleinen Test-Kernel ausdenken, oder einfach den hier benutzen: \<c\> int main() {

     // Pointer zum Videospeicher
     char *video = (char*)0xB8000;
     // String zum Ausgeben
     char *hello = "Hello World";

     // Zuerst den Speicher leeren
     for(video+=4000; video !=(char*)0xB8000 ;video--)
        *video=0;

     // String ausgeben
     while (*hello) {
       *video = *hello;
       video++;
       *video = 0x07;
       video++;
       hello++;
     }

     // jetzt wo wir schon im Kernel drin sind, wollen wir auch nicht mehr raus ;)
     while (1);
     return 0;

} \</c\>

### Kernel - Assembler

Dieser Code macht eigentlich nichts anderes als in die main-Funktion unseres C-Kernels zu springen. \<asm\> global loader ; loader für Linker sichtbar machen extern main  ; main-Funktion des C-Kernels

FLAGS equ 0 MAGIC equ 0x1BADB002  ; Magicnumber - Erkennungsmerkmal für GRUB CHECKSUM equ -(MAGIC + FLAGS) ; Checksum

section .text align 4 MultiBootHeader:

     dd MAGIC       ; Magic number
     dd FLAGS       ; Flags
     dd CHECKSUM    ; Checksum

loader:

     mov esp,0x200000 ; Stack an die 2MB-Grenze platzieren
     push eax         ; Multiboot Magicnumber auf den Stack legen
     push ebx         ; Adresse der Multiboot-Structure auf den Stack legen
     call main        ; main-Funktion des C-Kernels aufrufen

     cli ; falls der Kernel bis hier her kommt, CPU anhalten
     hlt

\</asm\> Der Code sollte eigentlich gut verständlich sein, trotzdem ist noch was zu klären:

- Die Flags können geändert werden, am besten schaut man sich die [Multiboot](https://github.com/lowlevel-eu/wiki/wiki/Multiboot "Multiboot")-Spezifikation an.
- Den Stack kann man natürlich an eine beliebige Stelle setzen, aber an der 2MB-Grenze wird er uns nicht stören.
- Es wird die Adresse der Multiboot-Structure nicht umsonst an den C-Kernel übergeben. Am besten liest man so ziemlich am Anfang des Kernels die Informationen aus ihr. In der Multiboot-Structure steht z.B wie viel Speicher der Rechner hat, oder welche Module von GRUB mitgeladen wurden.

## Zusammenbauen

Nun müssen wir den Kernel "zusammenbauen". Dafür müssen wir den Assembler-Code assemblieren, den C-Code kompilieren und am Ende beides linken.

### Assemblieren

Dies geschieht ganz einfach mit diesem Befehl:

    $ nasm -f elf -o kernel_asm.o kernel.asm

Damit wird eine [ELF](https://github.com/lowlevel-eu/wiki/wiki/Executable-and-Linking-Format "ELF")-Datei erzeugt, die wir später noch linken können.

### Kompilieren

Der C-Kernel wird mit diesem Befehl kompiliert:

    $ gcc -m32 -ffreestanding -o kernel_c.o -c kernel.c -Wall -Werror -nostdinc

Damit erstellen wir eine Objektdatei, mit der wir nachher noch linken können. Es ist wichtig, dass keine Includes und damit auch keine Funktionen aus der Standardbibliothek des Hostsystems benutzt werden. Diese müssen erst selbst implementiert werden. Eine genau Beschreibung der einzelnen Kommandozeilenparameter findet sich im [GCC Handbuch (englisch)](http://gcc.gnu.org/onlinedocs/gcc/Invoking-GCC.html#Invoking-GCC). An dieser Stelle nur so viel:

- -m32 weißt gcc an den Code für den 32Bit Protected-Mode (im Gegensatz zu -m64) zu erstellen
- -ffreestanding weißt gcc an nicht davon auszugehen, dass eine Standardbibliothek zur Verfügung steht
- -nostdinc weißt gcc an keine Header aus der Standardbibliothek des Hostsystems bereitzustellen

### Linken

Meiner Meinung nach ist dies der schwierigste Teil des "Zusammenbauens". Beim Linken wird unser Assembler-Kernel und unser C-Kernel miteinander verbunden und es wird z.B dem Assembler-Kernel auch gesagt wo die main-Funktion des C-Kernels liegt. Wir brauchen erstmal eine Konfigurationsdatei/[Linkerscript](https://github.com/lowlevel-eu/wiki/wiki/Linker "Linkerscript") für *ld*:

    ENTRY (loader)

    SECTIONS
    {
      . = 0x00100000;
        
      .text :
      {
        *(.text)
      }
        
      .rodata ALIGN (0x1000) :
      {
        *(.rodata)
      }

      .data ALIGN (0x1000): 
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

Mehr Informationen was genau dieses Linkerscript genau macht und warum es notwendig bzw. sinnvoll ist findet ihr im Artikel [Linkerscript](https://github.com/lowlevel-eu/wiki/wiki/Linker "Linkerscript"). An dieser Stelle nur so viel:

Mit "ENTRY(loader)" wird ld mitgeteilt, dass der Kernel bei der Funktion loader (siehe Assemblerteil des Kernels) beginnt. Dies wird in einem Datenfeld in der ELF-Header der "kernel.bin" festgehalten und von GRUB benötigt um zur richtigen Adresse zu springen.

Der Rest des Linkerscripts gibt an wo die Sektionen, das sind die Bereiche welche man in Assembler mittels des ".section .text" beispielsweise direkt angeben kann, aus den ELF-Objektdateien (kernel_asm.o und kernel_c.o) in der ELF-Binärdatei "kernel.bin" bzw. nach dem Laden im Speicher landen. Das ". = 0x00100000;" gibt an, dass die "kernel.bin" an Adresse 1MB gelinkt wird, d.h. sich nach dem Laden durch GRUB an Adresse 1MB und folgende im (physischen) Speicher befindet.

TODO: Rest

## GRUB-Image erstellen

Wir müssen jetzt natürlich noch ein Disketten-Image erstellen und dann GRUB und unseren Kernel draufladen.

### Floppy-Image erstellen

Wir erstellen uns erstmal ein Floppy-Image und formatieren es mit [ext2](https://github.com/lowlevel-eu/wiki/wiki/Ext2 "Ext2"). Es können auch andere [Dateisystem](https://github.com/lowlevel-eu/wiki/wiki/Dateisystem "Dateisystem") benutzt werden, z.B [FAT](https://github.com/lowlevel-eu/wiki/wiki/File-Allocation-Table "FAT"), man muss nur drauf achten, dass GRUB dieses Dateisystem unterstützt.

Mit *dd* erzeugen wir ein 1,44MB großes Floppy-Image:

    $ dd if=/dev/zero of=floppy.img bs=1024 count=1440

Dann formatieren wir es mit ext2:

    $ /sbin/mke2fs -F floppy.img

### Dateien auf die Diskette kopieren

Jetzt mounten wir schnell das Image (ein Verzeichnis namens *floppy* wird benötigt)

    $ mount -o loop floppy.img floppy/

und kopieren unseren Kernel drauf

    $ cp kernel.bin floppy/

[GRUB](https://github.com/lowlevel-eu/wiki/wiki/Grand-Unified-Bootloader "GRUB") muss auch noch drauf. Hierzu legen wir einen Ordner namens *grub* auf der Diskette an und kopieren *stage1* und *stage2* aus */boot/grub* auf die Diskette.

    $ mkdir floppy/grub
    $ cp /boot/grub/stage1 floppy/grub
    $ cp /boot/grub/stage2 floppy/grub

Wir brauchen natürlich noch eine GRUB-Konfigurationsdatei. Diese sollte folgendermaßen aussehen:

    default 0
    timeout 10

    title Mein super tolles OS
    kernel /kernel.bin
    root (fd0)

Die Konfigurationsdatei wird als *floppy/grub/menu.lst* gespeichert.

Jetzt können wir das Floppy-Image schon wieder unmounten

    $ umount floppy/

aber GRUB muss noch in den Bootsektor

    $ /usr/sbin/grub

Und dann folgendes eingeben:

    device (fd0) floppy.img
    root (fd0)
    setup (fd0)
    quit

Fertig ist unser GRUB-Image! Man kann es jetzt noch mit

    $ dd if=floppy.img of=/dev/fd0

auf eine Floppydisk kopieren und damit booten. Wenn alles klappt seht ihr "Hello World" auf dem Bildschirm.

## Vorschläge

- Auf Dauer wird es anstregend die ganzen Befehl einzutippen. Am einfachsten ist es eine [Makefile](https://github.com/lowlevel-eu/wiki/wiki/Makefile "Makefile") zu benutzen.
- Um nicht immer neustarten zu müssen, kann man einen Emulator wie Qemu oder [Bochs](https://github.com/lowlevel-eu/wiki/wiki/Bochs "Bochs") nehmen. Dann muss man das Image auch erst gar nicht auf Diskette kopieren.
- Mit *color light-blue/black light-cyan/blue* in menu.lst kann man dem Bootloader Farbe verpassen.

## Nachwort

Bei Fehlern in Text oder Code bitte an das Lowlevel-Team wenden.

## Siehe auch

- [C-Kernel starten](https://github.com/lowlevel-eu/wiki/wiki/C-Kernel-starten "C-Kernel starten")
- [GRUB-Image erstellen](https://github.com/lowlevel-eu/wiki/wiki/GRUB-Image-erstellen "GRUB-Image erstellen")
- [Multiboot](https://github.com/lowlevel-eu/wiki/wiki/Multiboot "Multiboot")
- [GRUB](https://github.com/lowlevel-eu/wiki/wiki/Grand-Unified-Bootloader "GRUB")
- GRUB auf CD

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/4442/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1604/index.html)

<!-- MediaWiki page 1604; revision 4442; parent 4438; 2009-06-16T09:54:21Z -->
