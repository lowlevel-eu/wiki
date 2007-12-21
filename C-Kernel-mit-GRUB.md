# C-Kernel mit GRUB

## Vorwort

In diesem Tutorial werde ich beschreiben wie man einen in C programmierten Kernel mithilfe von Grub bootet.

Ich werde hier beschreiben, wie ich es unter Linux mache, unter Windows wird es sicher auch gehen (nur etwas anders).

## Kernel

Der eigentlich Kernel soll ja in C programmiert sein. Ein Teil des Kernels muss aber immernoch in Assembler sein.

### Kernel - C

Als erstes kannst du dir einen kleinen Test-Kernel ausdenken, oder einfach den hier benutzen: \<c\> int main() {

     // Pointer zum Videospeicher
     char *video = (char*)0xB8000;
     // String zum Ausgeben
     char *hello = "Hello World";

     // String ausgeben
     while (*hello) {
       *video = 0x07;
       video++;
       *video = *hello;
       hello++;
     }

     // jetzt wo wir schon im Kernel drin sind, wollen wir auch nicht mehr raus ;)
     while (true);
     return 0;

} \</c\>

### Kernel - Assembler

Dieser Code macht eigentlich nichts anderes als in die main-Funktion unseres C-Kernels zu springen. \<asm\> global loader ; loader für Linker sichtbar machen extern main  ; main-Funktion des C-Kernels

FLAGS equ 0 MAGIC equ 0x1BADB002  ; Magicnumber - Erkennungsmerkmal für Grub CHECKSUM equ -(MAGIC + FLAGS) ; Checksum

section .text align 4 align 4 MultiBootHeader:

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
- Es wird die Adresse der [Multiboot](https://github.com/lowlevel-eu/wiki/wiki/Multiboot "Multiboot")-Structure nicht umsonst an den C-Kernel übergeben. Am besten liest man so ziemlich am Anfang des Kernels die Informationen aus ihr. In der [Multiboot](https://github.com/lowlevel-eu/wiki/wiki/Multiboot "Multiboot")-Structure steht z.B wie viel Speicher der Rechner hat, oder welche Module von Grub mitgeladen wurden.

## Zusammenbauen

Nun müssen wir den Kernel "zusammenbauen". Dafür müssen wir den Assembler-Code assemblieren, den C-Code kompilieren und am Ende beides linken.

### Assemblieren

Dies geschiet ganz einfach mit diesem Befehl:

    $ nasm -f elf -o kernel_asm.o kernel.asm

Damit wird eine Elf-Datei erzeugt, die wir später noch linken können.

### Kompilieren

Der C-Kernel wir mit diesem Befehl kompiliert:

    $ gcc -ffreestanding -o kernel_c.o -c kernel.c -Wall -Werror -nostdlib -nostartfiles -nodefaultlibs

Damit erstellen wir eine Objektdatei, mit der wir nachher noch linken können. Es ist wichtig, dass keine Standardbibliotheken benutzt werden.

### Linken

Meiner Meinung nach ist dies der schwierigste Teil des "Zusammenbauens". Beim Linken wird unser Assembler-Kernel und unser C-Kernel miteinander verbunden und es wir z.B dem Assembler-Kernel auch gesagt wo die main-Funktion des C-Kernels liegt. Wir brauchen erstmal eine Konfigurationsdatei für *ld*:

    ENTRY (loader)

    SECTIONS{
        . = 0x00100000;

        .text :{
            *(.text)
        }

        .rodata ALIGN (0x1000) : {
            *(.rodata)
        }

        .data ALIGN (0x1000) : {
            *(.data)
        }

        .bss : {
            _sbss = .;
            *(COMMON)
            *(.bss)
            _ebss = .;
        }
    }

Ich bin mir nicht 100%ig sicher ob dies die optimalste Linkerfile ist, aber sie funktioniert ;)

Nun wird gelinkt:

    $ ld -T <LD-Konfigurationsdatei> -o kernel.bin kernel_asm.o kernel_c.o

Wenn man später mehr Dateien hat, können diese natürlich auch dazugelinkt werden. Man sollte den fertigen Kernel jetzt in einer Datei namens *kernel.bin* haben.

## Grub-Image erstellen

Wir müssen jetzt natürlich noch ein Disketten-Image erstellen und dann Grub und unseren Kernel draufladen.

### Floppy-Image erstellen

Wir erstellen uns erstmal ein Floppy-Image und formatieren es mit ext2. Es können auch andere Dateisysteme benutzt werden, z.B FAT, man muss nur drauf achten, dass Grub dieses Dateisystem unterstützt.

Mit *dd* erzeugen wir ein 1,44MB großes Floppy-Image:

    $ dd if=/dev/zero of=floppy.img bs=1024 count=1440

Dann formatieren wir es mit ext2:

    $ /sbin/mke2fs -F floppy.img

### Dateien auf die Diskette kopieren

Jetzt mounten wir schnell das Image (ein Verzeichnis namens *floppy* wird benötigt)

    $ mount -o loop floppy.img floppy/

und kopieren unseren Kernel drauf

    $ cp kernel.bin floppy/

Grub muss auch noch drauf. Hierzu legen wir einen Ordner namens *grub* auf der Diskette an und kopieren *stage1* und *stage2* aus */boot/grub* auf die Diskette.

    $ mkdir floppy/grub
    $ cp /boot/grub/stage1 floppy/grub
    $ cp /boot/grub/stage2 floppy/grub

Wir brauchen natürlich noch eine Grub-Konfigurationsdatei. Diese sollte folgendermaßen aussehen:

    default 0
    timeout 10

    title Mein super tolles OS
    kernel /kernel.bin

Die Konfigurationsdatei wird als *floppy/grub/menu.lst* gespeichert.

Jetzt können wir das Floppy-Image schon wieder unmounten

    $ umount floppy/

aber Grub muss noch in den Bootsektor

    $ /usr/sbin/grub

Und dann folgendes eingeben:

    device (fd0) floppy.img
    root (fd0)
    setup (fd0)
    quit

Fertig ist unser Grub-Image! Man kann es jetzt noch mit

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
- Grub

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/2458/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1604/index.html)

<!-- MediaWiki page 1604; revision 2458; parent 0; 2007-12-21T13:32:29Z -->
