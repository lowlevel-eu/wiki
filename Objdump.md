# Objdump

**objdump** ist ein mächtiges Werkzeug aus den binutils für Unix. Es ermöglicht, (Objekt)-Code zu disassemblieren und verschiedenste Informationen zu einer Objektdatei zu erhalten.

  

## objdump in der OS-Entwicklung

In der OS-Entwicklung ist objdump ein unentbehrliches Werkzeug. Mit objdump lassen sich z.B. schnell und einfach Symbolnamen anzeigen.

  

## Crashkurs

Um die Symboltabelle einer Objektdatei zu bekommen, gibt man

` objdump -t DATEI `

ein. Die Ausgabe sieht dann z.B. so aus bei einem einfachen "Hallo-Welt"-Programm in C:

` hello.o: file format elf32-i386 `

`SYMBOL TABLE: 00000000 l df *ABS* 00000000 hello.c 00000000 l d .text 00000000 .text 00000000 l d .data 00000000 .data 00000000 l d .bss 00000000 .bss 00000000 l d .rodata 00000000 .rodata 00000000 l d .note.GNU-stack 00000000 .note.GNU-stack 00000000 l d .comment 00000000 .comment 00000000 g F .text 0000002b main 00000000 *UND* 00000000 puts `

Um die dynamische Symboltabelle zu bekommen, nutzt man

` objdump -T DATEI `

Per

` objdump -d DATEI `

lässt sich eine Datei (bzw. der ausführbare Teil) disassemblieren und auf der Kommandozeile ausgeben. Alternativ lässt sich die Ausgabe natürlich auch Umleiten:

` objdump -d DATEI > output.< `

Um eine Datei komplett zu disassemblieren, nutzt man

` objdump -D DATEI `

Mit dem Schalter -S versucht objdump, originalen Sourcecode herauszufinden und diesen mit dem disassemblierten Code zu vermischen. Der Schalter -l gibt zusätzlich Zeilennummern aus dem ursprünglichen Sourcecode aus (wenn dies möglich ist). Mit "-M intel-mnemonic" wird der Assemblercode nicht in der AT&T-Syntax, sondern in der Intelsyntax ausgegeben.

  

## Weblinks

- [objdump in den binutils](http://sourceware.org/binutils/docs-2.19/binutils/objdump.html)
- [Manpage](http://linux.die.net/man/1/objdump)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/5498/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1998/index.html)

<!-- MediaWiki page 1998; revision 5498; parent 5365; 2009-08-08T20:05:59Z -->
