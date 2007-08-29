# Debugging

Als Debugging wird die Fehlersuche in Programmen bezeichnet. Debugging ist oft ein langer und mühsamer Prozess aber meist nicht vermeidbar.

# JMP \$ / HLT

Das ist die primitivste Methode der Fehlersuche und sie wird meist nur am Anfang bei der Kernelentwicklung benötigt, solange Exceptions noch nicht (korrekt) gehandhabt werden. Dabei versucht man den genauen Ort zu finden an dem ein Fehler auftritt, indem man versucht die Ausführung möglichst kurz vor der vermuteten Stelle anzuhalten um so immer Näher an die gesuchte Instruktion ran zu kommen.

# print(f)/cout

Diese Methode ist schon etwas praktischer als die letzte. Debug-Ausgaben werden eigentlich in jedem Stadium der Entwicklung immer wieder gebraucht. Man platziert an den relevanten Stellen im Code Text-Ausgaben um beispielsweise zu sehen, welche Funktion aufgerufen wurde oder wie oft eine Schleife durchläuft usw.

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/2082/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1544/index.html)

<!-- MediaWiki page 1544; revision 2082; parent 0; 2007-08-29T10:10:38Z -->
