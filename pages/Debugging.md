# Debugging

Als Debugging wird die Fehlersuche in Programmen bezeichnet. Debugging ist oft ein langer und mühsamer Prozess aber meist nicht vermeidbar.

## JMP \$ / CLI-HLT

Das ist die primitivste Methode der Fehlersuche und sie wird meist nur am Anfang der Kernelentwicklung benötigt, solange Exceptions noch nicht (korrekt) gehandhabt werden. Dabei wird die Stelle, an der der Fehler auftritt, durch das Platzieren von Endlosschleifen oder CLI-HLT eingegrenzt.

## print(f)/cout

Diese Methode ist schon etwas praktischer als die vorangegangene. Debug-Ausgaben werden eigentlich in jedem Stadium der Entwicklung immer wieder gebraucht. Man platziert an den relevanten Stellen im Code [Textausgaben](Textausgabe.md "Textausgabe"), um beispielsweise zu sehen, welche Funktion aufgerufen wurde oder wie oft eine Schleife durchlaufen wird.

## Serielle Schnittstelle

Ähnlich wie bei der print(f)/cout-Methode kann man auch Daten/ASCII-Strings über die [serielle Schnittstelle](Serielle-Schnittstelle.md "Serielle Schnittstelle") verschicken. Das hat den Vorteil, dass man mehr als nur 25 oder 50 Zeilen zeitgleich betrachten kann.

Bei [bochs](Bochs.md "Bochs") werden die auf der seriellen Schnittstelle ausgegebenen Daten in eine Textdatei geschrieben, [QEMU](QEMU.md "QEMU") kann man mit einem Schalter veranlassen, die serielle Schnittstelle auf stdout oder in eine Datei umzuleiten. Diese kann später ggf. auch von weiteren Tools (z. B. grep) weiterverarbeitet werden.

Zudem ist ein Treiber für die serielle Schnittstelle sowohl im [Real Mode](Real-Mode.md "Real Mode") als auch im [Protected Mode](Protected-Mode.md "Protected Mode") relativ einfach zu schreiben. [Interrupts](Interrupt.md "Interrupt") müssen hierfür nicht verarbeitet werden können.

## bochs / QEMU / VirtualBox

Falls man mit Fehlern wie Pagefaults, GPFs oder anderen Exceptions kämpft, ist es wichtig, die Registerinhalte vor der Exception zu kennen. Um an diese zu kommen, sind Debug-Funktionen in den Emulatoren ein wertvolles Werkzeug.

Bei [bochs](Bochs-Debugger.md "Bochs Debugger") und [VirtualBox](VirtualBox.md "VirtualBox") kann dazu der integrierte Debugger benutzt werden. Diese beiden Emulatoren bieten weiterhin ein Log in der Konsole (Bochs) bzw. über die Debug-Funktionen (VirtualBox), dass unter Umständen wichtige Informationen über fehlerhafte Harwareansteuerung liefert.

QEMU stellt keinen eigenen Debugger zur Verfügung, ermöglicht aber eine Verbindung mit einem externen, wie z. B. dem GNU Debugger. Dies ist mit der Option „-s“ möglich, dazu sollte man „-S“ verwenden, da das emulierte OS sonst sofort startet. Verwendet wird TCP-Port 1234. Um den GDB anzuhängen, startet man GDB mit dem Kernel-Binary, also z. B. „*gdb bin/kernel.bin*“. Darauf gibt man auf der GDB-Kommandozeile „*target remote :1234*“ ein, um GDB mit QEMU zu verbinden. Ein „*cont*“ führt die Ausführung fort. Breakpoints können mit „*break datei:zeile*“ gesetzt werden, können aber auch auf Funktionen („*break \_foo*“) gesetzt werden.

Oft braucht man aber in Verbindung mit QEMU gar keine komplexen Debug-Funktionen, wenn man nur an die Adresse kommen muss, an der eine Exception auftritt, es den „-d“-Schalter anbietet, um verschiedene Dinge zu loggen. Meist benötigt man ein „-d int“, um alle Interrupts aufzuzeichnen.

## Exception-Meldungen

Wenn der Kernel schon ein wenig weiter ausgebaut ist und [Exceptions](Exception.md "Exception") abfängt, können die generierten Meldungen so ausgebaut werden, dass sie alle nötigen Informationen ausgeben. Um die Registerinhalte auszugeben, empfiehlt es sich, diese in der [ISR](Interrupt-Service-Routine.md "ISR") für die Exceptions auf den Stack zu legen, und dem Exception-Handler einen Pointer auf das zuletzt gepushte Register zu übergeben. Der Exception-Handler kann dann eine nette Meldung mit allen nötigen Informationen ausgeben.

Es können auch Breakpoints gesetzt werden: \<c\>asm("int \$3");\</c\>

## objdump

Sobald die Adresse bekannt ist, muss man daraus auf die Codestelle schließen können. Dabei kann das GNU-Tool [objdump](Objdump.md "Objdump") eine große Hilfe sein. Dies ist aber nur möglich, wenn man ein Binärformat wie [ELF](Executable-and-Linking-Format.md "ELF") benutzt, bei flachen Binaries fehlen dem Tool nötige Informationen (um einfach nur zu disassemblieren, kann man dann z. B. ndisasm, also den Disassembler von nasm, verwenden). objdump kann dabei mit dem Parameter -d Assemblercode mit Adresse vor jeder Instruktion generieren.

### Debuginformationen

Wenn man den Code mit Debuginformationen (bei gcc mit dem Parameter -g) kompiliert und linkt, kann objdump mit dem Parameter -S sogar den zugehörigen Quelltext der ursprünglichen Sprache anzeigen. Dieses Feature macht aber anscheinend in den aktuellen Versionen vor allem bei großen Dateien noch Probleme. Dabei wird der Source am Anfang oft noch angezeigt, dann aber irgendwann wird nur noch der Assembler-Code angezeigt. Das kann man am besten umgehen, indem man den Abstand der gesuchten Speicherstelle zum Funktionsanfang berechnet, und danach nur den Dump der entsprechenden Objektdateien ansieht.

### Optimierungen

Ein weiteres Problem sind beim Debuggen oft die Compileroptimierungen. Sind diese aktiviert, ist der Code oft wesentlich schwieriger zu verstehen, und ein objdump mit den Debuginformationen wird erst recht unverständlich. Es kann aber natürlich auch sein, dass Probleme erst durch das Aktivieren der Optimierungen auftauchen.

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/11256/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1544/index.html)

<!-- MediaWiki page 1544; revision 11256; parent 9438; 2015-01-18T17:22:46Z -->
