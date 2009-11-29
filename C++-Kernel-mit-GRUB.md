# C\+\+-Kernel mit GRUB

Die Programmierung eines [Kernels](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel") in [C++](https://github.com/lowlevel-eu/wiki/wiki/C%2B%2B "C++") unterscheidet sich in einigen Punkten von der mit [C](https://github.com/lowlevel-eu/wiki/wiki/C "C"). Da wären zum Beispiel der Aufruf der Constructoren, bzw. der Destructoren, die vor bzw. nach dem eigentlichen Kernel aufgerufen werden. Unser Kernel wird mittels [GRUB](https://github.com/lowlevel-eu/wiki/wiki/Grand-Unified-Bootloader "GRUB") geladen.

  

## Kernel

Wir werden mit [GCC](https://github.com/lowlevel-eu/wiki/wiki/GNU-Compiler-Collection "GCC") und [NASM](https://github.com/lowlevel-eu/wiki/wiki/Netwide-Assembler "NASM") arbeiten. Ich verwende den Cross-Compiler von Jidder, es sollte aber keinen Unterschied zu einem "normalen" GCC unter Linux geben.

### Kernel.cpp

Da wir ja schon mit C++ arbeiten, wäre auch etwas OOP angebracht. Deshalb erstellen wir ein Klasse namens Video, die wir in einen Header stecken. Dadurch ist unsere kernel.cpp sehr übersichtlich: \<cpp\>

1.  include "MyOS.h" //einbinden unseres Header

void main(void){ Video screen; //erzeugen von screen screen.color(0x7000); //Vordergrund Schwarz, Hintergrund Dunkelgrau screen.clear(); //Bildschirm leeren screen.write((char \*)"Wilkommen im C++-TestKernel!"); //Textausgabe } \</cpp\>

### MyOS.h

Der Header ist dann doch etwas Umfangreicher:

\<cpp\>

1.  ifndef MyOS_H
2.  define MyOS_H

class Video { public: Video(); //Konstruktor ~Video(); //Destruktor void clear(); //Leeren des Bildschirms, die Gräße liegt bei 80x25 Zeichen void write(char \*cp); //Textausgabe void put(char c); //Ausgabe eines einzelnen Zeichens void color(int color); //Setzen der FG/BG Farben private: unsigned short \*videomem; //Zeiger auf den Videospeicher unsigned int off; //Y-Position der Textausgabe, je volle Zeile +80 unsigned int pos; //X-Position der Textausgabe, ab Zeilenanfang unsigned int screen_color; //FB/BG Farbe }; Video::Video(){ screen_color = 0x0700; //Setzen der Farbe auf Dunkelgrau auf Schwarz pos=0; //Setzen der Textausgabe auf off=0; //Linksoben. videomem = (unsigned short\*) 0xb8000; //Startadresse des Videospeichers } Video::~Video(){} void Video::clear(){ for(int i=0;i\<(80\*25);i++) { videomem\[i\] = (unsigned char)' ' \|screen_color; //Füllen des Bildschirms mit Leerzeichen } pos = 0; //Zurücksetzen der Textausgabe nach Linksoben off = 0; // } void Video::write(char \*cp){ char \*str = cp, \*ch; for(ch = str; \*ch; ch++){ put(\*ch); //Für jedes einzelne Zeichen wird put() aufgerufen } } void Video::put(char c){ if(pos \>= 80){ //Wenn die Textausgabe den rechten pos = 0; off += 80; } if(off\>=(80\*25)){ //oder den unteren Bildschirmrand erreicht, gibt es einen clear(); //Umbruch bzw. es wird aufgeräumt. } videomem\[off + pos\] = (unsigned char)c\|screen_color; // Setzen des Zeichens und der Farbe in den Videospeicher pos++; } void Video::color(int color){ screen_color = color; //eigentlcih selbsterklärend }

1.  endif

\</cpp\>

### cKernel.c

Um den Constructor bzw. den Destructor aufzurufen, verlinken wir später diese zwei Funktionen mit:

\<c\> void \_cmain() { extern void (\*\_\_CTOR_LIST\_\_)(); void (\*\*constructor)() = &\_\_CTOR_LIST\_\_; int total = \*(int \*) constructor; constructor++; while(total){ (\*constructor)(); total--; constructor++; } }

void \_catexit() { extern void (\*\_\_DTOR_LIST\_\_)(); void (\*\*deconstructor)() = &\_\_DTOR_LIST\_\_; deconstructor++; int total = \*(int \*) deconstructor; while(total) { (\*deconstructor)(); total--; deconstructor++; } } \</c\>

### asmKernel.asm

Auch bei C++ kommen wir nicht um ein wenig Assembler herum:

\<asm\>

global loader ; Unser Einsprungspunkt extern main ; main() aus Kernel.cpp extern \_cmain ; \_cmain() aus cKernel.c extern \_catexit ; \_catexit() aus cKernel.c

FLAGS equ 0 MAGIC equ 0x1BADB002 ; Magicnumber - Erkennungsmerkmal für GRUB CHECKSUM equ -(MAGIC + FLAGS) ; Checksum

section .text align 4 MultiBootHeader:

     dd MAGIC                    ; Magic number
     dd FLAGS                       ; Flags
     dd CHECKSUM                    ; Checksum

loader:

     mov esp,0x200000                ; Stack an die 2MB-Grenze platzieren
     push eax                       ; Multiboot Magicnumber auf den Stack legen
     push ebx                       ; Adresse der Multiboot-Structure auf den Stack legen
     call _cmain                    ; main-Funktion des C++-Kernels aufrufen
     call main                      ; cmain-Funktion des C-Kernels aufrufen
     call _catexit                  ; atexit-Funktion des C-Kernels aufrufen
     jmp stop
     

stop: ; endlos Schleife nach Beendung unseres Kernels

    jmp stop

\</asm\>

## Kompilieren und Linken

Die asmKernel.asm:

    nasm -f elf -o asmKernel.o asmKernel.asm

Kernel.cpp:

    gcc -nostdlib -fno-builtin -fno-rtti -ffreestanding -fno-exceptions -c -Os -o  Kernel.o Kernel.cpp

cKernel.cpp:

    gcc -m32 -ffreestanding -fno-leading-underscore -c -o cKernel.o cKernel.c -Wall -Werror -nostdinc

Nun zu einem der wichtigsten Stellen: das Linken. Wir müssen die asmKernel.o, die Kernel.o und die cKernel.o zu einer Kernel.bin linken, die dann von GRUB geladen werden kann.

Unser Linkerscript, wir speichern es in link.txt:

    ENTRY(loader)
    OUTPUT_FORMAT(elf32-i386)
    OUTPUT_ARCH(i386:i386)

    SECTIONS
    {
      .text  0x0100000 : {
        code = .; _code = .; __code = .;
        *(.text)
        . = ALIGN(1);
      }
      .data  : {
        __CTOR_LIST__ = .; LONG((__CTOR_END__ - __CTOR_LIST__) / 4 - 2) *(.ctors) LONG(0) __CTOR_END__ = .;
        __DTOR_LIST__ = .; LONG((__DTOR_END__ - __DTOR_LIST__) / 4 - 2) *(.dtors) LONG(0) __DTOR_END__ = .;

        data = .; _data = .; __data = .;
        *(.data)
        . = ALIGN(1);
      }
      .bss  :
      {
        bss = .; _bss = .; __bss = .;
        *(.bss)
        . = ALIGN(1);
      }
      end = .; _end = .; __end = .;
    }

Wir sagen dem Linker zusätzlich zu einem Script für eine C-Kernel, dass wir die Labels \_\_CTOR_LIST\_\_, \_\_CTOR_END, \_\_DTOR_LIST\_\_ und \_\_DTOR_END\_\_ haben. Nur noch ein kurzer Aufruf von LD, und wir haben unseren fertigen Kernel in der Hand, äh Maus ^^.

    ld -T link.txt -o kernel.bin asmKernel.o cKernel.o Kernel.o

Und fertig ist unser Kernel! Unsere Kernel.bin kann die Kernel.bin auf dem Disketten-Image aus [C-Kernel mit GRUB](https://github.com/lowlevel-eu/wiki/wiki/C-Kernel-mit-GRUB "C-Kernel mit GRUB") ohne weiteres ersetzen, und schon Startet unsser C++-Kernel!

## Anmerkungen

Es kann unter umständen nötig sein \_\_CTOR_LIST\_\_ etc. durch \_CTOR_LIST\_\_ zu ersetzen, also das \_ weglassen. Ich vermute, dass das von der GCC Version abhängig ist.

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/6395/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2124/index.html)

<!-- MediaWiki page 2124; revision 6395; parent 0; 2009-11-29T00:48:31Z -->
