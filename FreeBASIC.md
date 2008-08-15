# FreeBASIC

Ob man BASIC für einen Kernel benutzen kann, ist in erster Linie eine akademische Frage. Der typische BASIC-Programmierer hat nicht die Kenntnisse, ein OS zu schreiben, und die Fortgeschritteneren wollen mit BASIC in aller Regel nichts zu tun haben.

Der Vollständigkeit halber: Es geht. Ich habe dazu FreeBASIC als Compiler benutzt.

## Testkernel in BASIC

\<freebasic\>DIM video AS BYTE POINTER DIM hello AS BYTE POINTER

video = CAST(BYTE POINTER, &Hb8000)

hello = strptr("Hello world")

WHILE \*hello \<\> 0

       *video = *hello
       hello = hello + 1
       video = video + 2

WEND

DO : LOOP

CONST mb_magic = &H1BADB002 CONST mb_flags = 3

ASM .global \_start \_start:

       call fb_ctor__kernel
       jmp $

fb_RtInit:

       ret

mb_header:

       .align 4
       .int mb_magic
       .int mb_flags
       .int -mb_magic-mb_flags

END ASM\</freebasic\>

Gebaut wird das ganze mit den folgenden Befehlen:

    fbc -c kernel.bas
    ld -Ttext=0x100000 kernel.o -melf_i386 -o basic.krn

## Weblinks

- <http://www.freebasic.net> - Offizielle englischsprachige Website der FreeBASIC-Entwickler
- <http://www.freebasic-portal.de> - deutschsprachiges Portal zu FreeBASIC mit Tutorials und Code-Beispielen

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/3208/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1624/index.html)

<!-- MediaWiki page 1624; revision 3208; parent 3207; 2008-08-15T23:36:06Z -->
