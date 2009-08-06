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

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/5089/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1932/index.html)

<!-- MediaWiki page 1932; revision 5089; parent 0; 2009-08-06T08:34:12Z -->
