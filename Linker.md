# Linker

Diese Seite ist ein Artikel, welcher **mehr** haben könnte..  

Wenn du mehr darüber weißt oder recherchieren willst, bist **du** aufgerufen, dies zu tun. Wenn du dir in einer Sache nicht sicher bist, dann stell es auf die Diskussionsseite.

Ein **Linker** ist ein Programm, welches Objektdateien "zusammenkopiert" und mit anderen nötigen Dateien verbindet.

  

## Funktionsweise

Beispiel: Wir haben ein simples "Hallo-Welt"-Programm in C, welches Gebrauch von der Funktion printf() macht. Diese ist bekanntlich Teil der libc, also der Standardbibliothek von C. Beim Kompillieren wird das C-Programm in Maschinencode übersetzt.

Das erreicht man mit dem [gcc](https://github.com/lowlevel-eu/wiki/wiki/GNU-Compiler-Collection "Gcc") so:

` gcc -c -o hello.o hello.c `

Nun wurde eine Objektdatei erstellt. Diese enthält sogenannte Referenzen auch Objekte, Funktionen usw.. Wenn wir uns also die erzeugte Datei per objdump -t anschauen, bekommen wir die Symboltabelle:

` hello.o: file format elf32-i386 `

`SYMBOL TABLE: 00000000 l df *ABS* 00000000 hello.c 00000000 l d .text 00000000 .text 00000000 l d .data 00000000 .data 00000000 l d .bss 00000000 .bss 00000000 l d .rodata 00000000 .rodata 00000000 l d .note.GNU-stack 00000000 .note.GNU-stack 00000000 l d .comment 00000000 .comment 00000000 g F .text 0000002b main 00000000 *UND* 00000000 puts `

Hier sehen wir die Referenzen, die noch nicht in der Datei enthalten sind: puts z.B..

Erst durch das Zusammenlinken mit anderen Objektdateien (hier: die der libc) wird der nötige Code in die Datei eingelinkt und die Datei ausführbar gemacht:

  

## Linkerdatei

Eine Linkerdatei definiert, wo welche Sektionen des Codes liegen.

Hier ein Beispiel aus dem Betriebssystem Qultics:

` OUTPUT_FORMAT(elf32-i386) OUTPUT_ARCH(i386:i386) ENTRY(start) phys = 0x00100000; SECTIONS { kernel_start = phys; `

     .text phys : AT(phys) {
       code = .;
       *(.text)
       *(.rodata)
       . = ALIGN(4096);
     }
     .data : AT(phys + (data - code))
     {
       data = .;
       *(.data)
       . = ALIGN(4096);
     }
     .bss : AT(phys + (bss - code))
     {
       bss = .;
       *(.bss)
       . = ALIGN(4096);
     }
     end = .;

     kernel_end = end;
     kernel_size = kernel_end - kernel_start;

`} `

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/10003/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1932/index.html)

<!-- MediaWiki page 1932; revision 10003; parent 8259; 2011-07-28T21:15:47Z -->
