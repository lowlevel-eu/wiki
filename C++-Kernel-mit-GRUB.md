# C\+\+-Kernel mit GRUB

Die Programmierung eines [Kernels](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel") in [C++](https://github.com/lowlevel-eu/wiki/wiki/C%2B%2B "C++") unterscheidet sich in einigen Punkten von der mit [C](https://github.com/lowlevel-eu/wiki/wiki/C "C"). Einen ausführlicheren Überblick zu den relevanten Unterschieden zu C gibt der Artikel [C++](https://github.com/lowlevel-eu/wiki/wiki/C%2B%2B "C++"). Dieses Tutorial arbeitet genau wie [C-Kernel mit GRUB](https://github.com/lowlevel-eu/wiki/wiki/C-Kernel-mit-GRUB "C-Kernel mit GRUB") mit dem Bootloader [GRUB](https://github.com/lowlevel-eu/wiki/wiki/Grand-Unified-Bootloader "GRUB").

  

## Kernel

Wir werden mit [GCC](https://github.com/lowlevel-eu/wiki/wiki/GNU-Compiler-Collection "GCC") und [NASM](https://github.com/lowlevel-eu/wiki/wiki/Netwide-Assembler "NASM") arbeiten. Diese Programme können auch unter Windows (nach-)installiert werden, was allerdings einiges an Vorarbeit benötigt; siehe dazu [C-Kernel mit GRUB](https://github.com/lowlevel-eu/wiki/wiki/C-Kernel-mit-GRUB#hinweis-f%C3%BCr-windowsianer "C-Kernel mit GRUB").

### Kernel.cpp

Da wir ja schon mit C++ arbeiten, wäre auch etwas OOP angebracht. Deshalb erstellen wir ein Klasse namens Video, die wir in einen Header stecken. Dadurch ist unsere kernel.cpp sehr übersichtlich: \<cpp\> // Einbinden unseres Header

1.  include "Video.h"
2.  include "Multiboot.h"

extern "C" void kernelMain(const Multiboot& multiboot_structur,

                              uint32_t multiboot_magic);

void kernelMain(const Multiboot& multiboot_structur,

                   uint32_t multiboot_magic)

{

     if (multiboot_magic != MULTIBOOT_MAGIC)
     {
       // Fehler!
       screen << background(color::red) << color::white << "Fehler: Nicht von einem multibootfaehigem Bootloader geladen!";
       return;
     }

     // Textausgabe
     screen << background(color::light_gray) << color::blue << "Willkommen im C++-TestKernel!";

} \</cpp\>

### types.h

Ein paar Typendefinitionen:

\<cpp\>

1.  ifndef TYPES_H
2.  define TYPES_H

/\* Garantiert, dass ein Typ nicht gepaddet wird und somit exakt die Größe seiner Member hat \*/

1.  define PACKED \_\_attribute\_\_((packed))

typedef unsigned char uint8_t; typedef unsigned short uint16_t; typedef unsigned int uint32_t;

1.  endif

\</cpp\>

### Video.h

Der Header ist dann doch etwas umfangreicher:

\<cpp\>

1.  ifndef VIDEO_H
2.  define VIDEO_H

<!-- -->

1.  include "types.h"

namespace color {

     enum type
     {
       black         = 0x00,
       blue          = 0x01,
       green         = 0x02,
       cyan          = 0x03,
       red           = 0x04,
       magenta       = 0x05,
       brown         = 0x06,
       light_gray    = 0x07,
       dark_gray     = 0x08,
       light_blue    = 0x09,
       light_green   = 0x0A,
       light_cyan    = 0x0B,
       light_red     = 0x0C,
       light_magenta = 0x0D,
       yellow        = 0x0E,
       white         = 0x0F
     };

}

struct background {

     inline background(color::type color)
       : m_color(color){}

     color::type m_color;

};

class Video {

     public:
       // Konstruktor
       Video();

       // Destruktor
       ~Video();

       // Leeren des Bildschirms, die Größe beträgt 80x25 Zeichen
       void clear();

       // Textausgabe
       Video& operator << (const char* s);

       // Vordergrundfarbe setzen
       Video& operator << (color::type color);

       // Hintergrundfarbe setzen
       Video& operator << (const background& color);

       // Ausgabe eines einzelnen Zeichens
       void put(char c);

     private:
       // Zeiger auf den Videospeicher
       uint16_t* m_videomem;

       // Y-Position der Textausgabe, je volle Zeile +80
       unsigned int m_off;

       // X-Position der Textausgabe, ab Zeilenanfang
       unsigned int m_pos;

       // FB/BG-Farbe
       uint16_t m_color;

};

// Globale Instanz der Video-Klasse, Definition in Video.cpp extern Video screen;

1.  endif

\</cpp\>

### Video.cpp

Die Implementierung der in Video.h definierten Memberfunktionen kommt in eine eigene Quellcodedatei:

\<cpp\>

1.  include "Video.h"

Video screen;

Video::Video()

     : m_videomem((uint16_t*) 0xb8000), m_off(0), m_pos(0), m_color(0x0700)

{

     //Bildschirm leeren
     clear();

}

Video::~Video(){ }

void Video::clear(){

     // Füllen des Bildschirms mit Leerzeichen
     for(int i = 0;i < (80*25);i++)
       m_videomem[i] = (unsigned char)' ' | m_color;

     // Zurücksetzen der Textausgabe nach links oben
     m_pos = 0;
     m_off = 0;                         

}

Video& Video::operator \<\< (const char\* s){

     // Für jedes einzelne Zeichen wird put() aufgerufen
     while (*s != '\0')
       put(*s++);

     return *this;

}

Video& Video::operator \<\< (color::type color){

     m_color = (static_cast<uint16_t>(color) << 8) | (m_color & 0xF000);
     return *this;

}

Video& Video::operator \<\< (const background& color){

     m_color = (static_cast<uint16_t>(color.m_color) << 12) | (m_color & 0x0F00);
     return *this;

}

void Video::put(char c){

     // Wenn die Textausgabe den rechten...
     if(m_pos >= 80){
       m_pos = 0;
       m_off += 80;
     }

     // ...oder den unteren Bildschirmrand erreicht, gibt es
     // einen Umbruch bzw. es wird aufgeräumt.
     if(m_off >= (80*25))
       clear();

     // Setzen des Zeichens und der Farbe in den Videospeicher
     m_videomem[m_off + m_pos] = (uint16_t)c | m_color;
     m_pos++;

} \</cpp\>

### Multiboot.h

Eine Header um die von [GRUB](https://github.com/lowlevel-eu/wiki/wiki/Grand-Unified-Bootloader "GRUB") an das Betriebssystem übergebene Multibootstruktur zu verwenden (siehe auch [Multiboot](https://github.com/lowlevel-eu/wiki/wiki/Multiboot "Multiboot")):

\<cpp\>

1.  ifndef MULTIBOOT_H
2.  define MULTIBOOT_H

<!-- -->

1.  include "types.h"

<!-- -->

1.  define MULTIBOOT_MAGIC 0x2BADB002

struct Multiboot {

     uint32_t flags;
     uint32_t mem_lower;
     uint32_t mem_upper;
     uint32_t bootdevce;
     uint32_t cmdline;
     uint32_t module_count;
     uint32_t module_address;
     /* etc... */

} PACKED;

1.  endif

\</cpp\>

### Startup.cpp

Um die Konstruktoren bzw. die Destruktoren von globalen/statischen Objekten aufzurufen (siehe auch [C++](https://github.com/lowlevel-eu/wiki/wiki/C%2B%2B#globalestatische-objekte "C++")), wird die Funktion initialiseConstructors aus [C++](https://github.com/lowlevel-eu/wiki/wiki/C%2B%2B#konstruktoren "C++") benötigt. Diese wird später mit in den Kernel gelinkt und in der asmKernel.asm aufgerufen. Die Destruktoraufrufe von globalen/statischen Objekten werden absichtlich nicht aufgerufen, da es innerhalb des Kernels der Erfahrung von [bluecode](https://lowlevel-eu.github.io/wiki/pages/1489/index.html "Benutzer:Bluecode") nach keinen Sinn macht bei (globalen/statischen!) Objekten den Destruktor zu verwenden. Falls man dies dennoch möchte kann man im Artikel [C++](https://github.com/lowlevel-eu/wiki/wiki/C%2B%2B "C++") einer der beiden relevanten Abschnitte implementieren.

### asmKernel.asm

Auch bei C++ kommen wir nicht um ein wenig Assembler herum:

\<asm\>

global loader ; Unser Einsprungspunkt extern kernelMain ; kernelMain() aus Kernel.cpp extern initialiseConstructors ; aus Startup.cpp

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
     call kernelMain                    ; kernelMain aufrufen

stop:

     jmp stop                    ; Endlosschleife nach Beendigung unseres Kernels

\</asm\>

## Kompilieren und Linken

Die asmKernel.asm:

    nasm -f elf -o asmKernel.o asmKernel.asm

Video.cpp:

    gcc -m32 -fno-use-cxa-atexit -nostdlib -fno-builtin -fno-rtti -fno-exceptions -fno-leading-underscore -Wall -Wextra -pedantic-errors -c -o Video.o Video.cpp

Kernel.cpp:

    gcc -m32 -fno-use-cxa-atexit -nostdlib -fno-builtin -fno-rtti -fno-exceptions -fno-leading-underscore -Wall -Wextra -pedantic-errors -c -o Kernel.o Kernel.cpp

Startup.cpp:

    gcc -m32 -fno-use-cxa-atexit -nostdlib -fno-builtin -fno-rtti -fno-exceptions -fno-leading-underscore -Wall -Wextra -pedantic-errors -c -o Startup.o Startup.cpp

  
Nun zu einer der wichtigsten Stellen, dem Linkvorgang: Wir müssen asmKernel.o, Startup.o, Video.o und Kernel.o zu einer kernel.bin linken, die dann von GRUB geladen werden kann.

Unser Linkerscript (link.txt)

    ENTRY(loader)
    OUTPUT_FORMAT(elf32-i386)
    OUTPUT_ARCH(i386:i386)

    SECTIONS
    {
      . = 0x0100000;

      .text :
      {
        *(.text*)
        *(.rodata)
      }

      .data  :
      {
        start_ctors = .;
        *(.ctors)
        end_ctors = .;

        *(.data)
      }

      .bss  :
      {
        *(.bss)
      }

      /DISCARD/ : { *(.dtors) *(.comment) }
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

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/11074/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2124/index.html)

<!-- MediaWiki page 2124; revision 11074; parent 9441; 2013-03-22T17:43:35Z -->
