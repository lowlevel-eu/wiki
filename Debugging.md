# Debugging

Als **Debugging** wird die Fehlersuche in Programmen bezeichnet. Debugging ist v.a. in der Betriebssystementwicklung oft ein langer und mühsamer Prozess aber meist nicht vermeidbar.

## JMP \$ / HLT

Das ist die primitivste Methode der Fehlersuche und sie wird meist nur am Anfang bei der [Kernelentwicklung](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel") benötigt, solange Exceptions noch nicht (korrekt) gehandhabt werden. Dabei versucht man den genauen Ort zu finden an dem ein Fehler auftritt, indem man versucht die Ausführung möglichst kurz vor der vermuteten Stelle anzuhalten, um sich so der gesuchten Instruktion langsam anzunähern.

## print(f)/cout

Diese Methode ist schon etwas praktischer als die letzte. Debug-Ausgaben werden eigentlich in jedem Stadium der Entwicklung immer wieder gebraucht. Man platziert an den relevanten Stellen im Code [Textausgaben](https://github.com/lowlevel-eu/wiki/wiki/Textausgabe "Textausgabe") um beispielsweise zu sehen, welche Funktion aufgerufen wurde oder wie oft eine Schleife durchläuft usw.

## RS232

Ähnlich wie bei der print(f)/cout - Methode kann man auch Daten/ASCII-Strings über die [serielle Schnittstelle](https://github.com/lowlevel-eu/wiki/wiki/Serielle-Schnittstelle "Serielle Schnittstelle") verschicken. Das hat den Vorteil, dass man mehr als nur 25 oder 50 Zeilen zeitgleich betrachten kann. Bei bochs werden die an die serielle Schnittstelle gegebenen Daten in eine Textdatei gegeben, diese kann später ggf. auch von weiteren Tools (z.B. grep) weiterverarbeitet werden. Zudem ist ein [rs232](https://github.com/lowlevel-eu/wiki/wiki/Serielle-Schnittstelle "Rs232")-Treiber sowohl im RM als auch im PM relativ einfach zu schreiben. Interrupts müssen hierfür nicht verarbeitet werden können.

## bochs / qemu

Falls man mit Fehlern wie Pagefaults, GPFs oder anderen Exceptions kämpft, ist es wichtig, dass man die Registerinhalte vor der Exception kennt. Um an diese zu kommen sind Debug-Funktionen in den Emulatoren ein wertvolles Werkzeug. Bei bochs kann dazu der integrierte Debugger benutzt werden. qemu stellt keinen eigenen Debugger zur Verfügung, ermöglicht aber eine Verbindung mit einem externen (siehe GNU Project Debugger und QEMU). Oft braucht man aber in Verbindung mit qemu gar keine komplexen Debug-Funktionen, wenn man nur an die Adresse rankommen muss, wo eine Exception auftritt. Denn qemu bietet den -d Parameter um verschiedene Dinge zu loggen. Meist benötigt man ein -d int um alle Interrupts aufzuzeichnen. Dabei muss man aber ein wenig aufpassen, da qemu bei einem Triplefault keinen Reset ausführt, das heißt er schreibt dann lauter GPFs in die Logdatei und diese wird dabei extrem groß. Man sollte qemu also möglichst schnell schließen, wenn ein Triplefault aufgetreten ist.

## Exception-Meldungen

Wenn der Kernel schon ein wenig weiter ausgebaut ist, und [Exceptions](https://github.com/lowlevel-eu/wiki/wiki/Ausgabe-2#exceptions "Ausgabe 2") abfängt, können diese Meldungen so ausgebaut werden, dass sie alle nötigen Informationen ausgeben. Um die Registerinhalte auszugeben empfiehlt es sich, diese in der [ISR](https://github.com/lowlevel-eu/wiki/wiki/Interrupt-Service-Routine "ISR") für die Exceptions auf den Stack zu legen, und dem Exception-Handler einen Zeiger auf das zuletzt gepushte Register zu übergeben. Dabei sollte man darauf, dass nichts anderes zwischen dem Interrupt-Stack-Frame und den Registern liegt, da der Handler sonst nicht mehr wirklich an eip und esp aus dem Interrupt-Stack-Frame ran kommen kann. Der Exception-Handler kann dann eine nette Meldung mit allen nötigen Informationen ausgeben.

## objdump

Sobald man die Adresse hat, muss man daraus irgendwie auf die Codestelle schließen können. Dabei kann das GNU-Tool objdump eine große Hilfe sein. Dies ist aber nur möglich, wenn man ein Binärformat wie ELF benutzt, bei flachen Binaries fehlen dem Tool nötige Informationen. objdump kann dabei mit dem Parameter -d Assembler-Code mit Adresse vor jeder Instruktion generieren. Wenn man den Code mit Debug-Infos (bei gcc mit dem Parameter -g) kompiliert und linkt kann objdump mit dem Parameter -S sogar den zugehörigen Quelltext der ursprünglichen Sprache anzeigen. Dieses Feature macht aber scheinbar in den aktuellen Versionen vorallem bei großen Dateien noch Probleme. Dabei wird der Quellcode am Anfang oft noch angezeigt, dann aber irgendwann wird nur noch der Assembler-Code angezeigt. Das kann man am besten umgehen, indem man den Abstand der gesuchten Speicherstelle zum Funktionsanfang berechnet, und danach nur den Dump der entsprechenden Objektdateien ansieht.

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/2695/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1544/index.html)

<!-- MediaWiki page 1544; revision 2695; parent 2455; 2008-03-22T16:38:25Z -->
