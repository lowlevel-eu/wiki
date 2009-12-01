# C\+\+-Kernel mit GRUB

Die Programmierung eines [Kernels](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel") in [C++](https://github.com/lowlevel-eu/wiki/wiki/C%2B%2B "C++") unterscheidet sich in einigen Punkten von der mit [C](https://github.com/lowlevel-eu/wiki/wiki/C "C"). Einen ausführlicheren Überblick zu den relevanten Unterschieden zu C gibt der Artikel [C++](https://github.com/lowlevel-eu/wiki/wiki/C%2B%2B "C++"). Dieses Tutorial arbeitet genau wie [C-Kernel mit GRUB](https://github.com/lowlevel-eu/wiki/wiki/C-Kernel-mit-GRUB "C-Kernel mit GRUB") mit dem Bootloader [GRUB](https://github.com/lowlevel-eu/wiki/wiki/Grand-Unified-Bootloader "GRUB").

## Kernel

Wir werden mit [GCC](https://github.com/lowlevel-eu/wiki/wiki/GNU-Compiler-Collection "GCC") und [NASM](https://github.com/lowlevel-eu/wiki/wiki/Netwide-Assembler "NASM") arbeiten. Es kann auch Windows verwendet werden, allerdings ist dazu etwas Vorarbeit in Bezug auf die Tools von Nöten, siehe dazu [C-Kernel mit GRUB](https://github.com/lowlevel-eu/wiki/wiki/C-Kernel-mit-GRUB#hinweis-f%C3%BCr-windowsianer "C-Kernel mit GRUB").

### Kernel.cpp

Da wir ja schon mit C++ arbeiten, wäre auch etwas OOP angebracht. Deshalb erstellen wir ein Klasse namens Video, die wir in einen Header stecken. Dadurch ist unsere kernel.cpp sehr übersichtlich: \<cpp\>

1.  include "Video.h" // Einbinden unseres Header

void main() { screen.color(0x7000); // Vordergrund schwarz, Hintergrund hellgrau screen.clear(); // Bildschirm leeren screen \<\< "Willkommen im C++-TestKernel!"; // Textausgabe } \</cpp\>

### Video.h

Der Header ist dann doch etwas umfangreicher:

\<cpp\>

1.  ifndef VIDEO_H
2.  define VIDEO_H

class Video { public: Video(); // Konstruktor ~Video(); // Destruktor void clear(); // Leeren des Bildschirms, die Größe beträgt 80x25 Zeichen Video& operator \<\< (const char\* s); // Textausgabe void put(char c); // Ausgabe eines einzelnen Zeichens void color(int color); // Setzen der FG/BG-Farben private: unsigned short\* videomem; // Zeiger auf den Videospeicher unsigned int off; // Y-Position der Textausgabe, je volle Zeile +80 unsigned int pos; // X-Position der Textausgabe, ab Zeilenanfang unsigned int screen_color; // FB/BG-Farbe };

extern Video screen; // Globale Instanz der Video-Klasse, Definition in Video.cpp

1.  endif

\</cpp\>

### Video.cpp

Die Implementierung der in Video.h definierten Memberfunktionen kommt in eine eigene Quellcodedatei:

\<cpp\>

1.  include "Video.h"

Video screen;

Video::Video(){ screen_color = 0x0700; // Setzen der Farbe auf Hellgrau auf Schwarz pos = 0; // Setzen der Textausgabe auf off = 0; // links oben. videomem = (unsigned short\*) 0xb8000; // Startadresse des Videospeichers }

Video::~Video(){ }

void Video::clear(){ for(int i = 0;i \< (80\*25);i++) { videomem\[i\] = (unsigned char)' ' \| screen_color; // Füllen des Bildschirms mit Leerzeichen } pos = 0; // Zurücksetzen der Textausgabe nach links oben off = 0; }

Video& Video::operator \<\< (const char\* s){ while (\*s != '\0'){ put(\*s++); // Für jedes einzelne Zeichen wird put() aufgerufen } return \*this; }

void Video::put(char c){ if(pos \>= 80){ // Wenn die Textausgabe den rechten... pos = 0; off += 80; } if(off \>= (80\*25)){ // ...oder den unteren Bildschirmrand erreicht, gibt es einen clear(); // Umbruch bzw. es wird aufgeräumt. } videomem\[off + pos\] = (unsigned char)c \| screen_color; // Setzen des Zeichens und der Farbe in den Videospeicher pos++; }

void Video::color(int color){ screen_color = color; } \</cpp\>

### Startup.cpp

Um die Konstruktoren bzw. die Destruktoren von globalen/statischen Objekten aufzurufen (siehe auch [C++](https://github.com/lowlevel-eu/wiki/wiki/C%2B%2B#globalestatische-objekte "C++")), wird die Funktion initialiseConstructors aus [C++](https://github.com/lowlevel-eu/wiki/wiki/C%2B%2B#konstruktoren "C++") benötigt. Diese wird später mit in den Kernel gelinkt und in der asmKernel.asm aufgerufen. Die Destruktoraufrufe von globalen/statischen Objekten werden absichtlich nicht aufgerufen, da es innerhalb des Kernels der Erfahrung von [bluecode](https://lowlevel-eu.github.io/wiki/pages/1489/index.html "Benutzer:Bluecode") nach keinen Sinn macht bei (globalen/statischen!) Objekten den Destruktor zu verwenden. Falls man dies dennoch möchte kann man im Artikel [C++](https://github.com/lowlevel-eu/wiki/wiki/C%2B%2B "C++") einer der beiden relevanten Abschnitte implementieren.

### asmKernel.asm

Auch bei C++ kommen wir nicht um ein wenig Assembler herum:

\<asm\>

global loader ; Unser Einsprungspunkt extern main ; main() aus Kernel.cpp extern initialiseConstructors ; aus Startup.cpp

FLAGS equ 0 MAGIC equ 0x1BADB002 ; Magicnumber - Erkennungsmerkmal für GRUB CHECKSUM equ -(MAGIC + FLAGS) ; Checksum

section .text align 4 MultiBootHeader:

     dd MAGIC                    ; Magic number
     dd FLAGS                       ; Flags
     dd CHECKSUM                    ; Checksum

loader:

     mov esp,0x200000                ; Stack an die 2MB-Grenze platzieren
     push eax                       ; Multiboot-Magicnumber auf den Stack legen
     push ebx                       ; Adresse der Multiboot-Structure auf den Stack legen
     call initialiseConstructors        ; Konstruktoren aufrufen
     call main                      ; main aufrufen

stop:

     jmp stop                    ; Endlosschleife nach Beendigung unseres Kernels

\</asm\>

## Kompilieren und Linken

Die asmKernel.asm:

    nasm -f elf -o asmKernel.o asmKernel.asm

Video.cpp:

    gcc -m32 -fno-use-cxa-atexit -nostdlib -fno-builtin -fno-rtti -ffreestanding -fno-exceptions -fno-leading-underscore -c -o Video.o Video.cpp

Kernel.cpp:

    gcc -m32 -fno-use-cxa-atexit -nostdlib -fno-builtin -fno-rtti -ffreestanding -fno-exceptions -fno-leading-underscore -c -o Kernel.o Kernel.cpp

Startup.cpp:

    gcc -m32 -fno-use-cxa-atexit -nostdlib -fno-builtin -fno-rtti -ffreestanding -fno-exceptions -fno-leading-underscore -c -o Startup.o Startup.cpp

  
Nun zu einer der wichtigsten Stellen, dem Linkvorgang: Wir müssen asmKernel.o, Startup.o, Video.o und Kernel.o zu einer kernel.bin linken, die dann von GRUB geladen werden kann.

Unser Linkerscript (link.txt)

    ENTRY(loader)
    OUTPUT_FORMAT(elf32-i386)
    OUTPUT_ARCH(i386:i386)

    SECTIONS
    {
      .text  0x0100000 :
      {
        *(.text)
        *(.rodata)
      }

      .data  :
      {
        start_ctors = .;
        *(.ctors)
        end_ctors = .;

        start_dtors = .;
        *(.dtors)
        end_dtors = .;

        *(.data)
      }

      .bss  :
      {
        *(.bss)
      }

      /DISCARD/ : { *(.dtors) }
    }

Wir teilen dem Linker mit, dass wir die Labels start_ctors, end_ctors, start_dtors und end_dtors in der Datei Startup.cpp haben und er diese beim Linken berücksichtigen soll. Außerdem wird die Liste der Destruktoren aus der aus dem Kernel entfernt, da sie wie oben erklärt nicht verwendet werden. Nur noch ein kurzer Aufruf von LD, und wir haben unseren fertigen Kernel:

    ld -T link.txt -o kernel.bin asmKernel.o Startup.o Video.o Kernel.o

Wie der Kernel nun mitsamt GRUB auf einer Diskette landet, kann im Artikel [C-Kernel mit GRUB](https://github.com/lowlevel-eu/wiki/wiki/C-Kernel-mit-GRUB "C-Kernel mit GRUB") nachgelesen werden. Hier verfährt man einfach analog.

## Siehe auch

- [C-Kernel mit GRUB](https://github.com/lowlevel-eu/wiki/wiki/C-Kernel-mit-GRUB "C-Kernel mit GRUB")
- [GRUB](https://github.com/lowlevel-eu/wiki/wiki/Grand-Unified-Bootloader "GRUB")
- [C++](https://github.com/lowlevel-eu/wiki/wiki/C%2B%2B "C++")
- [Multiboot](https://github.com/lowlevel-eu/wiki/wiki/Multiboot "Multiboot")
- [Linkerscript](https://github.com/lowlevel-eu/wiki/wiki/Linker "Linkerscript")

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/6433/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2124/index.html)

<!-- MediaWiki page 2124; revision 6433; parent 6425; 2009-12-01T14:32:48Z -->
