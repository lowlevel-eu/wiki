# Fortran

| Allgemeines |  |
| -------------------------------- | ------------- |
| Name: | Fortran |
| Inlineassembler: | Nein |
| Compiler: | g77 |
| Spracheneigenschaften |  |
| Plattformen: | Alle |
| Beispielkernel in der Sprache: | Siehe Unten |
| Homepage |  |

  
Fortran ist eine prozedurale und objektorientierte [Programmiersprache](https://lowlevel-eu.github.io/wiki/pages/1648/index.html "Kategorie:Programmiersprache"), die auf einem Vorschlag von John W. Backus aus dem Jahre 1953 zurückgeht und als erste tatsächlich umgesetzte Hochsprache im Jahre 1957 von eben diesem entwickelt wurde. Fortran wird vor allem für numerische Berechnungen genutzt.

## Testkernel in Fortran

**Hinweis:** Ich habe das mit gfortran getestet. Mit anderen Compilern funktioniert das vermutlich nicht so.

### hello.f

    c       Einsprungspunkt
            subroutine hello ()
                    call clear()
                    call print_str('Hello World aus fortran!', 24)
            end subroutine hello

    c       Schreibt einen String auf den Bildschrim
    c         str:  Der String
    c         l:    Laenge des Strings in Zeichen
            subroutine print_str (str, l)
                    character str(*)
                    integer l
                    integer i

                    do 10 i = 1, l
                            call print_char(str(i))
     10             continue
            end subroutine print_str

    c       Schreibt ein Zeichen auf den Bildschirm
    c         c:    Das Zeichen
            subroutine print_char (c)
                    character c
                    integer,save :: vmempos = 1

                    call write_vmem(c, vmempos)
                    vmempos = vmempos + 2
            end subroutine print_char

    c       Leert den Bildschirm
            subroutine clear ()
                    integer i

                    do 10 i = 1, 2000, 2
                            call write_vmem(' ', i)
     10             continue
            end subroutine clear

    c       Schreibt ein Zeichen in den Videospeicher
    c         c:    Das Zeichen
    c         pos:  Die Position (Achtung beginnt bei 1!)
            subroutine write_vmem (c, pos)
                    integer pos
                    character c
                    character vmem(2000)
                    pointer (ipt, vmem)

    c               Entspricht 0xB8000 in Hex
                    ipt = 753664
                    vmem(pos) = c
            end subroutine write_vmem

### header.S

    .globl _start
    _start:
        movl $0x200000, %esp
        .extern hello
        call hello
        hlt

    .align 4
    multiboot_header:
        .int 0x1BADB002
        .int 0x0
        .int (-0x1BADB002)

Hinweis: Unter Windows ist es vonnöten

    .extern _hello
    call _hello

zu schreiben.

### build.sh

    gfortran -fcray-pointer -fno-underscoring -fno-second-underscore -c \
        -m32 -g -o hello.o hello.f
    as -32 -o header.o header.S
    ld -melf_i386 -Ttext=0x100000 -o fortran.krn hello.o header.o

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/10583/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1745/index.html)

<!-- MediaWiki page 1745; revision 10583; parent 10582; 2012-04-23T15:19:11Z -->
