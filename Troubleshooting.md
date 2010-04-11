# Troubleshooting

In diesem Artikel sollen möglichst viele der - für die Betriebssystemprogrammierung oder für bestimmte Wikiartikel relevanten - Fehlermeldungen des Compilers/Linkers erklärt werden und ein Weg zum Beheben der Fehler aufgezeigt werden. Es sollen hier allerdings keine Probleme zur Sprache kommen, die sich durch einen Blick in "*\<Programmiersprache\> für Dummies*" lösen lassen.

## undefined reference to \`funktionsname'

Diese Fehlermeldung wird vom Linker ausgegeben, wenn er kein Symbol mit dem Namen *funktionsname* findet. Dies kann vorkommen, wenn

- du vergessen hast die Objektdatei mit der Definition der Funktion *funktionsname* zu kompilieren und mit zu linken
- du vergessen hast in der Sourcecodedatei diese Funktion zu definieren
- du aus Versehen die Funktion als *static* deklariert hast
- du [C++](https://github.com/lowlevel-eu/wiki/wiki/C%2B%2B "C++") verwendest und *funktionsname* in einer C++-Quellcodedatei definiert wird und von einer C/Assembler-Quellcodedatei verwendet wird, eine Lösung findet sich [hier](https://github.com/lowlevel-eu/wiki/wiki/C%2B%2B "C++")
- du Archive (.a Dateien) verwendest und die Reihenfolge der Kommandozeilenparameter von ld nicht richtig ist oder du vergessen hast *--start-group* und *--end-group* anzugeben, siehe hierfür auch das [ld Manual](http://sourceware.org/binutils/docs/ld/Options.html)

Falls nichts davon zutrifft, könntest du die Objektdatei, die die deiner Meinung nach entsprechende Funktion enthalten soll, disassemblieren und schauen ob ein entsprechender Symbolname auftaucht.

## C++-spezifisch

### expected primary-expression before ‘.’ token

→ Hauptartikel: [C++](https://github.com/lowlevel-eu/wiki/wiki/C%2B%2B "C++")

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/7548/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2227/index.html)

<!-- MediaWiki page 2227; revision 7548; parent 0; 2010-04-11T14:04:15Z -->
