# Debugging

Als Debugging wird die Fehlersuche in Programmen bezeichnet. Debugging ist oft ein langer und mühsamer Prozess aber meist nicht vermeidbar.

# JMP \$ / HLT

Das ist die primitivste Methode der Fehlersuche und sie wird meist nur am Anfang bei der Kernelentwicklung benötigt, solange Exceptions noch nicht (korrekt) gehandhabt werden. Dabei wird die Stelle, an der der Fehler auftritt, durch das Platzieren von Endlosschleifen oder HLTs eingegrenzt.

# print(f)/cout

Diese Methode ist schon etwas praktischer als die Letzte. Debug-Ausgaben werden eigentlich in jedem Stadium der Entwicklung immer wieder gebraucht. Man platziert an den relevanten Stellen im Code [Text-Ausgaben](https://github.com/lowlevel-eu/wiki/wiki/Textausgabe "Textausgabe") um beispielsweise zu sehen, welche Funktion aufgerufen wurde oder wie oft eine Schleife durchläuft usw.

# RS232

Ähnlich wie bei der print(f)/cout - Methode kann man auch Daten/ASCII-Strings über die [serielle Schnittstelle](https://github.com/lowlevel-eu/wiki/wiki/Serielle-Schnittstelle "Serielle Schnittstelle") verschicken. Das hat den Vorteil, dass man mehr als nur 25 oder 50 Zeilen zeitgleich betrachten kann. Bei bochs werden die auf der seriellen Schnittstelle ausgegebenen Daten in eine Textdatei geschrieben. Diese kann später ggf. auch von weiteren Tools (z.B. grep) weiterverarbeitet werden. Zudem ist ein Treiber für die [serielle Schnittstelle](https://github.com/lowlevel-eu/wiki/wiki/Serielle-Schnittstelle "Serielle Schnittstelle") sowohl im [Real Mode](https://github.com/lowlevel-eu/wiki/wiki/Real-Mode "Real Mode") als auch im [Protected Mode](https://github.com/lowlevel-eu/wiki/wiki/Protected-Mode "Protected Mode") relativ einfach zu schreiben. [Interrupts](https://github.com/lowlevel-eu/wiki/wiki/Interrupt "Interrupt") müssen hierfür nicht verarbeitet werden können.

# bochs / qemu

Falls man mit Fehlern wie Pagefaults, GPFs oder anderen Exceptions kämpft, ist es wichtig, die Registerinhalte vor der Exception zu kennen. Um an diese zu kommen sind Debug-Funktionen in den Emulatoren ein wertvolles Werkzeug.

Bei [bochs](https://github.com/lowlevel-eu/wiki/wiki/Bochs "Bochs") kann dazu der integrierte Debugger benutzt werden.

qemu stellt keinen eigenen Debugger zur Verfügung, ermöglicht aber eine Verbindung mit einem Externen(siehe GNU Project Debugger und QEMU). Oft braucht man aber in Verbindung mit qemu gar keine komplexen Debug-Funktionen, wenn man nur an die Adresse kommen muss, an der eine Exception auftritt. Denn qemu bietet den -d Parameter um verschiedene Dinge zu loggen. Meist benötigt man ein -d int um alle Interrupts aufzuzeichnen. Dabei muss man aber ein wenig aufpassen, da ältere Versionen von Qemu bei einem Tripplefault keinen Reset auslösen. Das heisst er schreibt dann lauter GPFs in die Logdatei und diese wird dabei SEHR gross. Man sollte den qemu also möglichst schnell schliessen, sobald ein Triplefault aufgetreten ist.

# Exception-Meldungen

Wenn der Kernel schon ein wenig weiter ausgebaut ist, und [Exceptions](https://github.com/lowlevel-eu/wiki/wiki/Ausgabe-2#exceptions "Ausgabe 2") abfängt, können diese Meldungen so ausgebaut werden, dass sie alle nötigen Informationen ausgeben. Um die Registerinhalte auszugeben empfiehlt es sich, diese in der [ISR](https://github.com/lowlevel-eu/wiki/wiki/Interrupt-Service-Routine "ISR") für die Exceptions auf den Stack zu legen, und dem Exception-Handler einen Pointer auf das zuletzt gepushte Register zu übergeben. Der Exception-Handler kann dann eine nette Meldung mit allen nötigen Informationen ausgeben.

# objdump

Sobald die Adresse bekannt ist, muss man daraus auf die Codestelle schliessen können. Dabei kann das GNU-Tool [objdump](https://github.com/lowlevel-eu/wiki/wiki/Objdump "Objdump") eine grosse Hilfe sein. Dies ist aber nur möglich, wenn man ein Binärformat wie [ELF](https://github.com/lowlevel-eu/wiki/wiki/Executable-and-Linking-Format "ELF") benutzt, bei flachen Binaries fehlen dem Tool nötige Informationen. objdump kann dabei mit dem Parameter -d Assembler-Code mit Adresse vor jeder Instruktion generieren.

## Debuginformationen

Wenn man den Code mit Debug-Infos (bei gcc mit dem Parameter -g) kompiliert und linkt kann objdump mit dem Parameter -S sogar den zugehörigen Quelltext der ursprünglichen Sprache anzeigen. Dieses Feature macht aber anscheinend in den aktuellen Versionen vorallem bei grossen Dateien noch Probleme. Dabei wird der Source am Anfang oft noch angezeigt, dann aber irgendwann wird nur noch der Assembler-Code angezeigt. Das kann man am besten umgehen, indem man den Abstand der gesuchten Speicherstelle zum Funktionsanfang berechnet, und danach nur den Dump der entsprechenden Objektdateien ansieht.

## Optimierungen

Ein weiteres Problem sind beim Debuggen oft die Compileroptimierungen. Sind diese aktiviert, ist der Code oft wesentlich schwieriger zu verstehen, und ein objdump mit den Debuginformationen wird erst recht unverständlich. Es kann aber natürlich auch sein, dass Probleme erst durch das Aktivieren der Optimierungen auftauchen.

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/3210/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1544/index.html)

<!-- MediaWiki page 1544; revision 3210; parent 3209; 2008-08-16T09:20:21Z -->
