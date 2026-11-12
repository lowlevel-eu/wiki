# Objective-C

Diese Seite ist ein Artikel, welcher **mehr** haben könnte..  

Wenn du mehr darüber weißt oder recherchieren willst, bist **du** aufgerufen, dies zu tun. Wenn du dir in einer Sache nicht sicher bist, dann stell es auf die Diskussionsseite.

| Allgemeines |  |
| -------------------------------- | --------------------------------------------------------------------------- |
| Name: | Objective-C |
| Inlineassembler: | Nein |
| Compiler: | gobjc, Cocoa |
| Spracheneigenschaften |  |
| Plattformen: | Mac OS X, [Linux](Linux.md "Linux") |
| Beispielkernel in der Sprache: | Siehe unten |
| Homepage |  |

[Apple's Developer-Center](http://developer.apple.com/mac/library/documentation/cocoa/Conceptual/ObjectiveC/index.html)

**Objective-C** ist eine imperative und objektorientierte Programmiersprache, welche in den 80er-Jahren von Brad Cox und Tom Love als Basis für NextStep, einem Betriebssystem auf Basis von 4.3BSD und dem Mach2-Kernel, entwickelt wurde.

  

## Spracheigenschaften

Primär hat Objective-C als Grundlage [C](C.md "C"), welches es um objektorientierte Eigenschaften und Syntax erweitert. Die Syntax ist dabei stark an Smalltalk angelehnt und hebt sich bewusst von den C-Sprachelementen ab. Objective-C implementiert dabei bekannte Elemente der Objektorientierung wie:

- Klassen
- Methoden
- Instanzen
- Delegierte

## Objective-C als Sprache für ein Betriebssystem

Objective-C eignet sich genauso wie C für die Entwicklung von Betriebssystemen bzw. Kerneln, verfügt allerdings nicht, anders als C, über einen Inline-[Assembler](Assembler.md "Assembler"), weshalb etwaige Assembler-Arbeiten extern erledigt werden müssen. Um die objektorientierten Eigenschaften von Objective-C zu nutzen bedarf es allerdings einiger Vorarbeiten (TODO ;-).

  

## Kernel in Objective-C

Hier ein Objective-C-Kernel ohne Objektorientierung:

### init.m

\<c\> int init(int argc, const char \*argv\[\]) {

       // Pointer zum Videospeicher
       char *video = (char*)0xB8000;

       // String zum Ausgeben
       char *hello = "Hello World";

       // Zuerst den Speicher leeren
       for(video+=4000; video !=(char*)0xB8000 ;video--)
           *video=0;

       // String ausgeben
       while (*hello) 
       {
           *video = *hello;
           video++;
        *video = 0x07;
        video++;
        hello++;
       }

       while (1);
       return 0;

} \</c\>

Findige Leser des Wikis haben wahrscheinlich gemerkt: Das ist der gleiche Kernel wie im Artikel zu [C](C.md "C"); Objective-C hat als Basis C und somit ist (fast) jedes C-Programm auch ein gültiges Objective-C-Programm. Einzig wird aus

    #include <stdio.h>

folgendes:

    #import <stdio.h>

### start.S

Hier die Assembler-Startdatei samt [Multiboot](Multiboot.md "Multiboot")-Header, welche von [GRUB](Grand-Unified-Bootloader.md "GRUB") aufgerufen wird und durch welche wir in den Objective-C-Kernel springen: \<asm\> .section .text

.extern init

.global \_start

\_start: mov \$\_kernel_stack, %esp push 0 push 0

mov %esp, %ebp

       push %ebx
       call init

       jmp .

.section multiboot

1.  define MB_MAGIC 0x1BADB002
2.  define MB_FLAGS 0x0
3.  define MB_CHECKSUM -(MB_MAGIC + MB_FLAGS)

.align 4 .int MB_MAGIC .int MB_FLAGS .int MB_CHECKSUM

// 16 KB Stack werden hier reserviert .section .bss .space 16384 \_kernel_stack: \</asm\>

### link.ld

Dazu noch das [Linker](Linker.md "Linker")-Script:

` ENTRY(_start) `

`SECTIONS { `

       . = 0x100000;

       kernel_start = .;

       .text : {
           *(multiboot)
           *(.text)
       }
       .data ALIGN(4096) : {
           *(.data)
       }
       .rodata ALIGN(4096) : {
           *(.rodata)
       }
       .bss ALIGN(4096) : {
           *(.bss)
       }

       . = ALIGN(4096);
       kernel_end = .;

`} `

### Kernel erstellen

Gebaut wird der Kernel nun wie folgt:

    $ gcc -g -c -m32 -Wall -fno-stack-protector -fno-builtin -nostdlib -nodefaultlibs -c start.S
    $ gcc -g -c -m32 -Wall -fno-stack-protector -fno-builtin -nostdlib -nodefaultlibs -c init.m
    $ ld -melf_i386 -Tlink.ld start.o init.o -o objckernel

Dieser kann dann mit [qemu](QEMU.md "QEMU") direkt aufgerufen werden (ab Version 0.11.0):

    $ qemu -kernel objkernel

## Compiler

- [GCC](http://gcc.gnu.org/) - Unterstützung auch für Objective-C (gobjc)

  

## Weblinks

- [Apple's Developer-Center](http://developer.apple.com/mac/library/documentation/cocoa/Conceptual/ObjectiveC/index.html)
- [Kleines Tutorial über die Spracheigenschaften](http://www.otierney.net/objective-c.html)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/6347/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2115/index.html)

<!-- MediaWiki page 2115; revision 6347; parent 6346; 2009-11-18T05:35:57Z -->
