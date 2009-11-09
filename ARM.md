# ARM

Diese Seite ist ein Artikel, welcher **mehr** haben könnte..  

Wenn du mehr darüber weißt oder recherchieren willst, bist **du** aufgerufen, dies zu tun. Wenn du dir in einer Sache nicht sicher bist, dann stell es auf die Diskussionsseite.

**ARM** (**A**corn **R**isc **M**achine) sind 32-Bit-Prozessoren nach dem [RISC](https://github.com/lowlevel-eu/wiki/wiki/Reduced-Instruction-Set-Computing "RISC")-Prinzip.

## Eigenschaften

Als ARM wird primär das Design des Prozessors bzw. der Prozessor-Architektur bezeichnet. Jedoch bezeichnet man Prozessoren, die nach ARM gebaut wurden als "ARM-Prozessoren". ARM-Prozessoren zeichnen sich durch einen reduzierten und effizienten Befehlssatz und einem geringen Stromverbrauch aus.

  

## Einsatzgebiete

ARM-Prozessoren sind zwar vor allem bei PC-Anwendern nicht in aller Munde, stecken aber in erstaunlich vielen Geräten: In fast jedem Router ist ein ARm-Prozessor zu finden, der Apple iPod läuft mit einem ARM-Prozessor und die GameBoys von Nintendo ermöglichen mobiles Spielen mit eben diesen ARM-Prozessoren (im Nintendo DS stecken sogar zwei dieser Sorte).

## Programmierung

Die "Lowlevel-Programmierung" eines ARM-Prozessors mit Assembler unterscheidet sich stark in der eines x86-Prozessors. Ein ARM-Prozessor kennt drei Kategorien an Befehlen:

- Befehle zum Zugriff auf den Speicher
- Arithmetische oder logische Befehle auf Werte in Registern
- Befehle zum Ändern des Programmflusses (Sprünge, Subroutinen)

Anders als die x86-Architektur verfügt der ARM über ein Drei-Register-Behfelssatz, welcher ermöglicht, einen Ziel- sowie zwei Quellregister anzugeben:

\<asm\>

    add r0, r1, r2   ; r0 := r1 + r2

\</asm\>

  

### Register

Es stehen einem 15 Allzweckregister zur Verfügung (ähnlich \*ax-Register der x86-Prozessoren): r0 bis r14. das Register r13 wird allerdings standardmäßig als Stackpointer genutzt und das Registger r14 als "Link-Register", in welchem die Rücksprungaddresse bei Prozeduraufrufen gespeichert wird. Das Register r15 dient als "Programmzähler". Daneben gibt es ein Register namens CPSR (Current Program Status Register), in welchem der Informationen wie der aktuelle Programm-Status gespeichert werden.

Die Register r13, r14 und das Statusregister werden "gespiegelt", sodass bei einer Exception und der dazugehörigen Behandlung sich nicht um die Sicherung des Stackpointers und des Instruction-Pointers gekümmert werden muss.

  

## Prozessor-Modi

Bei ARM-Prozessoren gibt es keinen Real-Mode und Protected-Mode. Auch das Konzept der Ringe fällt weg, stattdessen wird selbiges als Prozessor-Modus implementiert. Hier die Modi des ARM-Prozessors:

- Supervisor-Mode (SVC): Entspricht dem Ring-0 bei x86-Prozessoren, hier läuft das Betriebssystem
- User Mode: Entspricht dem Ring-3 bei x86-Prozessoren. hier laufen normale User-Programme
- Interrupt-Mode (IRQ): Wird ein Interrupt ausgelöst oder eine Exception geworfen wird der Prozessor in diesen Modus umgeschaltet
- Undefined Instruction Exception (UND): Wird ein unbekannter Befehl ausgeführt, wird der Prozessor in diesen Modus geschaltet und bei Bedarf der Befehl emuliert werden
- Memory Abort (ABT): Kann eine Datenanforderung nicht verarbeitet werden, wird der Prozessor in diesen Modus geschaltet
- Fast Interrupt-Mode (FIQ): Wird durch einen sogenannten "Fast-Interrupt-Request" ausgelöst, findet meist bei Echtzeit-Betriebssystemen Verwendung

In jedem Modus hat der gerade auführende Code andere Privilegien, sofern er nicht schon im Supervisor-Mode arbeitet.

  

## Siehe auch

- [Cross-Compiler unter Linux für ARM](https://github.com/lowlevel-eu/wiki/wiki/ARM-Cross-Compiler "ARM Cross-Compiler")
- [RISC](https://github.com/lowlevel-eu/wiki/wiki/Reduced-Instruction-Set-Computing "RISC")

  

## Weblinks

- [Offizielle ARM-Seite](http://infocenter.arm.com/help/index.jsp?noscript=1) - Spezifikationen und weitere Informationen
- [Erstellen einer "nackten" ARM-Umgebung](http://www.embedded.com/columns/technicalinsights/200900043)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/6210/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2101/index.html)

<!-- MediaWiki page 2101; revision 6210; parent 6209; 2009-11-09T01:46:01Z -->
