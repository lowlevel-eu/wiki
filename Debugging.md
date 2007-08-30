# Debugging

Als Debugging wird die Fehlersuche in Programmen bezeichnet. Debugging ist oft ein langer und mühsamer Prozess aber meist nicht vermeidbar.

# JMP \$ / HLT

Das ist die primitivste Methode der Fehlersuche und sie wird meist nur am Anfang bei der Kernelentwicklung benötigt, solange Exceptions noch nicht (korrekt) gehandhabt werden. Dabei versucht man den genauen Ort zu finden an dem ein Fehler auftritt, indem man versucht die Ausführung möglichst kurz vor der vermuteten Stelle anzuhalten um so immer Näher an die gesuchte Instruktion ran zu kommen.

# print(f)/cout

Diese Methode ist schon etwas praktischer als die letzte. Debug-Ausgaben werden eigentlich in jedem Stadium der Entwicklung immer wieder gebraucht. Man platziert an den relevanten Stellen im Code Text-Ausgaben um beispielsweise zu sehen, welche Funktion aufgerufen wurde oder wie oft eine Schleife durchläuft usw.

# bochs / qemu

Falls man mit Fehlern wie Pagefaults, GPFs oder anderen Exceptions kämpft, ist es wichtig, dass man die Registerinhalte vor der Exception kennt. Um an diese zu kommen sind Debug-Funktionen in den Emulatoren ein wertvolles Werkzeug. Bei bochs kann dazu der integrierte Debugger benutzt werden. qemu stellt keinen eigenen Debugger zur Verfügung, ermöglicht aber eine Verbindung mit. Oft braucht man aber in Verbindung mit qemu gar keine komplexen Debug-Funktionen, wenn man nur an die Adresse rankommen muss, wo eine Exception auftritt. Denn qemu bietet den -d Parameter um verschiedene Dinge zu loggen. Meist benötigt man ein -d int um alle Interrupts aufzuzeichnen. Dabei muss man aber ein wenig aufpassen, da qemu keinen Reset ausführt bei einem Triplefault, das heisst er schreibt dann lauter GPFs in die LOG und diese wird dabei SEHR gross. Man sollte den qemu also möglichst schnell schliessen, sobald ein Triplefault aufgetreten ist.

# Exception-Meldungen

Wenn der Kernel schon ein wenig weiter ausgebaut ist, und Exceptions abfängt, können diese Meldungen so ausgebaut werden, damit sie alle nötigen Informationen ausgeben. Um die Registerinhalte auszugeben empfiehlt es sich, diese in der ISR für die Exceptions auf den Stack zu legen, und dem Exception-Handler einen Pointer auf das zuletzt gepushte Register zu übergeben. Dabei sollte man darauf, dass nichts anderes zwischen dem Interrupt-Stack-Frame und den Registern liegt, da der Handler sonst nicht mehr wirklich an eip und esp aus dem Interrupt-Stack-Frame ran kommen kann. Der Exception-Handler kann dann eine nette Meldung mit allen nötigen Infos ausgeben.

# objdump

Sobald man die Adresse hat, muss man daraus irgendwie auf die Codestelle schliessen können. Dabei kann das GNU-Tool objdump eine grosse Hilfe sein. Dies ist aber nur möglich, wenn man ein Binärformat wie ELF benutzt, bei flachen Binaries fehlen dem Tool nötige Informationen. objdump kann dabei mit dem Parameter -d Assembler-Code mit Adresse vor jeder Instruktion generieren. Wenn man den Code mit Debug-Infos (bei gcc mit dem Parameter -g) kompiliert und linkt kann objdump mit dem Parameter -S sogar den zugehörigen Quelltext der ursprünglichen Sprache anzeigen. Dieses Feature macht aber scheinbar in den aktuellen Versionen vorallem bei grossen Dateien noch Probleme. Dabei wird der Source am Anfang oft noch angezeigt, dann aber irgendwann wird nur noch der Assembler-Code angezeigt. Das kann man am besten umgehen, indem man den Abstand der gesuchten Speicherstelle zum Funktionsanfang berechnet, und danach nur den Dump der entsprechenden Objektdateien ansieht.

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/2084/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1544/index.html)

<!-- MediaWiki page 1544; revision 2084; parent 2083; 2007-08-30T10:04:49Z -->
