# FreeBASIC

| Allgemeines |  |
| -------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| Name: | FreeBasic |
| Inlineassembler: | Ja (Intel-Syntax) |
| Compiler: | FBC (arbeitet mit [GCC](GNU-Compiler-Collection.md "GCC") zusammen) |
| Spracheneigenschaften |  |
| Plattformen: | [Windows](Windows.md "Windows"), [Linux](Linux.md "Linux"), u.a. |
| Beispielkernel in der Sprache: | s.u. |
| Homepage |  |

[www.freebasic.net](http://www.freebasic.net/)

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

## Anfang einer kleinen RTLib

Möchte man FB-Funktionen wie IN oder OUT benutzen, muss erstmal eine Runtime-Lib her, die die Funktionen zur Verfügung stellt. Die ist normalerweise in C geschrieben, aber das geht (zumindest für einfache Dinge) auch in FREEBASIC. Hier Beispiele für IN und OUT:

\<freebasic\> SUB fb_Out CDECL ALIAS "fb_Out" (port as USHORT, value as UBYTE)

       ASM
           movw dx, [port]
           movb al, [value]
           outb dx, al
       END ASM

END SUB

FUNCTION fb_In CDECL ALIAS "fb_In" (port as USHORT) AS UBYTE

       DIM value AS UBYTE

       ASM
          movw dx, [port]
          inb al, dx
          mov [value], al
       END ASM

       RETURN value

END FUNCTION \</freebasic\>

Diese werden in die Datei rtlib.bas gepackt, danach wie oben angegeben kompiliert. Zum Linken muss jetzt der folgende Befehl benutzt werden:

    ld -Ttext=0x100000 kernel.o rtlib.o -melf_i386 -o basic.krn

## Weblinks

- <http://www.freebasic.net> - Offizielle englischsprachige Website der FreeBASIC-Entwickler
- <http://www.freebasic-portal.de> - deutschsprachiges Portal zu FreeBASIC mit Tutorials und Code-Beispielen

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/9833/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1624/index.html)

<!-- MediaWiki page 1624; revision 9833; parent 6163; 2011-06-11T20:42:50Z -->
