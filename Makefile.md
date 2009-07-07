# Makefile

Ein **Makefile** ist eine Konfigurationsdatei für das Unix-Programm *make*. Eine der bekanntesten Implementierungen ist das freie GNU Make.

Die Aufgabe von *make* ist es im Grunde genommen, dem Programmierer zu ermöglichen, ein Programm zu kompilieren, ohne alle Compilerbefehle von Hand eingeben zu müssen. In Projekten, die mit Makefiles ausgestattet ist, muss man normalerweise nur in das Verzeichnis wechseln und den Befehl *make* eingeben, wodurch das Projekt gebaut wird. Im Gegensatz zu einem Shellscript, das genau die selbe Aufgabe erledigen könnte, prüft *make* jedoch, welche Dateien verändert wurden, und welche Komponenten darum neu gebaut werden müssen. Dadurch wird bei mehrfacher Kompilierung (z.B in der Entwicklung) viel Zeit gespart, weil nicht immer das ganze Programm neu kompiliert werden muss. Je größer das Projekt ist, desto mehr macht sich dieser Effekt deutlich.

Um *make* diese Checks zu ermöglichen definiert der Programmierer in seinem Projekt Targets und Abhängigkeiten zwischen diesen. Diese sind im einfachsten Falle Dateien (z.B. Source-, Header- und Objektdateien), können aber auch abstrakte Objekte wie Module sein. Das Target definiert dann einen Befehl, mit dem die Target-Datei eben aus den Abhängigkeiten erstellt wird.

Dies ist jedoch nur die Grundidee von *make*. Für weitergehende Informationen empfiehlt sich die Lektüre der vielen im Internet verfügbaren Tutorials sowie natürlich die GNU Make Dokumentation.

## Links

- [Wikipedia zu make](http://de.wikipedia.org/wiki/Make)
- [GNU Make Dokumentation](http://www.gnu.org/software/make/manual/html_node/index.html) (englisch)
- [Ein Tutorial zu Makefiles](http://www.ijon.de/comp/tutorials/makefile.html)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/4584/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1436/index.html)

<!-- MediaWiki page 1436; revision 4584; parent 3517; 2009-07-07T18:53:53Z -->
