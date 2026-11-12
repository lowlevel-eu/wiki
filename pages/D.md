# D

| Allgemeines |  |
| -------------------------------- | ------------------------------- |
| Name: | D |
| Inlineassembler: | Ja (Intel-Syntax) |
| Compiler: | dmd (Digital Mars), gdc (GNU) |
| Spracheneigenschaften |  |
| Plattformen: | Alle |
| Beispielkernel in der Sprache: | s.u. |
| Homepage |  |

<http://www.digitalmars.com/d>

D ist eine prozedurale sowie objekorientierte Programmiersprache und wird seit 1999 von Walter Bright entwickelt. Primäres Ziel der Entwicklung war dabei die Produktivität von Scriptsprachen wie Python mit der Abstraktion von [C++](C%2B%2B.md "C++") und der Nähe zum System von [C](C.md "C") zu vereinen.

## D als Sprache für ein Betriebssystem

D kann primär als objektorientiertes C (ähnlich C++) gesehen werden. Mit D lässt sich genauso wie in C sehr systemnah programmieren, es sind Sprachmittel wie Pointer vorhanden und man kann per Inline-[Assembler](Assembler.md "Assembler") (Intel-Syntax) Assembler-Routinen einbauen. Einzig muss (z.B. für den [Kernel](Kernel.md "Kernel")) ein kleines Runtime implementiert werden, welcher Funktionen zum Überprüfen von Werten während der Laufzeit zur Verfügung stellt (mehr dazu weiter unten). Um Sprachmittel wie Konstruktoren und Destruktoren einzusetzen, bedarf es ebenfalls Laufzeitunterstützung.

## Kernel in D

### Konstruktoren/Destruktoren

Wer in D seinen Kernel programmiert, möchte vielleicht den Vorteil der Objektorientierung nicht missen. Dazu muss allerdings, wie in C++ auch, Code geschrieben werden, welcher die Konstruktoren/Destruktoren aufruft.

Für die Konstruktoren: \<asm\> static_ctors_loop:

      mov ebx, start_ctors
      jmp .test

.body:

      call [ebx]
      add ebx,4

.test:

      cmp ebx, end_ctors
      jb .body

\</asm\>

start_ctors ist dabei im [Linkerscript](Linker.md "Linkerscript") angegeben.

Für die Destruktoren: \<asm\> static_dtors_loop:

      mov ebx, start_dtors
      jmp .test

.body:

      call [ebx]
      add ebx,4

.test:

      cmp ebx, end_dtors
      jb .body

\</asm\>

end_dtors ist hier auch im Linkerscript angegeben.

Das passende Linkerscript dazu:

#### link.ld

    OUTPUT_FORMAT(elf32-i386)
    ENTRY (start)

    SECTIONS{
        . = 0x00100000;

        .text :{
            code = .; _code = .; __code = .;
            *(.text)
            *(.rodata)
        }

        .rodata ALIGN (0x1000) : {
            *(.rodata)
        }

        .data ALIGN (0x1000) : {
            data = .; _data = .; __data = .;
            *(.data)
            start_ctors = .; *(.ctors)   end_ctors = .;
            start_dtors = .; *(.dtors)   end_dtors = .;
        }
        

        .bss :{
            sbss = .;
            bss = .; _bss = .; __bss = .;
            *(COMMON)
            *(.bss)
            ebss = .;
        }
        end = .; _end = .; __end = .;
    }

### Runtime

Wer in D einen Kernel schreibt wird bei der Benutzung von Arrays beim Linken schnell folgenden Fehler zu sehen bekommen:

`undefined reference to _d_array_bounds`

\_d_array_bounds ist dabei nicht anderes, als eine Funktion im D-Runtime, welche überprüft, ob Array-Grenzen eingehalten werden. Um diesen Fehler vorzubeugen, sollte also zumindest eine Stub-Funktion erstellt werden:

\<c\> extern(C) void \_d_array_bounds(char \*filename, uint line) {} \</c\>

Zu Debugging-Zwecken kann hier natürlich auch eine echte Überprüfung gemacht werden.

Wer allerdings keine Runtime-Überprüfung im Kernel braucht, der kann den Compiler auch so aufrufen:

    $ gdc -no-bounds-check

  

Neu hinzugekommen zu dem Schluesselwort

    synchronized

sind neu zu erstellende Stubs:

\<c\> extern (C) void \_d_criticalenter() {} extern (C) void \_d_criticalexit() {} extern (C) void \_Dmodule_ref() {} \</c\>

### Der eigentliche Kernel

Nichts weltbewegendes, wir geben ein einfaches 'D' auf dem Bildschirm aus:

\<c\> module kernel.main;

extern(C) void main(uint magic, uint addr) {

       int ypos = 0; 
       int xpos = 0;
       const uint COLUMNS = 80; 
       const uint LINES = 24;

       ubyte* vidmem = cast(ubyte*)0x000B8000; 

       for (int i = 0; i < COLUMNS * LINES * 2; i++) { 
           synchronized *(vidmem + i) = 0;
       }

       synchronized *(vidmem + (xpos + ypos * COLUMNS) * 2) = 'D' & 0xFF; 
       synchronized *(vidmem + (xpos + ypos * COLUMNS) * 2 + 1) = 0x07; 

       for (;;) { 
       }

} \</c\>

Man beachte das 'module kernel.main', wobei kernel der Name des Verzeichnisses ist, wo sich die Datei befindet.

### start.asm

Und hier der Start-Code mit Multiboot-Signatur und dem Konstruktor/Destruktor-Code von oben:

\<asm\> global start extern main extern start_ctors, end_ctors, start_dtors, end_dtors

MODULEALIGN equ 1\<\<0 MEMINFO equ 1\<\<1 FLAGS equ MODULEALIGN \| MEMINFO MAGIC equ 0x1BADB002 CHECKSUM equ -(MAGIC + FLAGS)

section .text

align 4 MultiBootHeader:

          dd MAGIC
          dd FLAGS
          dd CHECKSUM

STACKSIZE equ 0x4000

static_ctors_loop:

      mov ebx, start_ctors
      jmp .test

.body:

      call [ebx]
      add ebx,4

.test:

      cmp ebx, end_ctors
      jb .body

start:

          mov esp, STACKSIZE+stack

          push eax
          push ebx

          call main

static_dtors_loop:

      mov ebx, start_dtors
      jmp .test

.body:

      call [ebx]
      add ebx,4

.test:

      cmp ebx, end_dtors
      jb .body

cpuhalt:

          hlt
          jmp cpuhalt

section .bss align 32

stack:

         resb      STACKSIZE

\</asm\>

### Erstellung

Erstellt wird das Ganze per

    $ nasm -f elf -o ./obj/start.o ./src/kernel/start.asm

und

    $ gdc -nostdlib -g -c -o ./obj/kernel.main.o ./src/kernel/kernel.main.d

gelinkt wird's so:

    $ ld -T link.d -o dkernel ./obj/start.o ./obj/kernel.main.o

  

## D-Compiler

- [gdc](http://bitbucket.org/goshawk/gdc/wiki/Home) für die [GNU Compiler Collection](GNU-Compiler-Collection.md "GNU Compiler Collection")
- [dmd](http://dlang.org/download.html) Digital-Mars-D-Compiler

## Weblinks

- [Offizielle Website der Sprache D](http://dlang.org/index.html)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/11188/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1863/index.html)

<!-- MediaWiki page 1863; revision 11188; parent 11187; 2014-03-05T11:17:10Z -->
