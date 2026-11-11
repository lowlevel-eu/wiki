# Debug Register

Die **Debug Register** ermöglichen es eine Debug [Exception](Exception "Exception") *\#DB* (Int 1) auszulösen, wenn bestimmte Ereignisse eintreten. Die Register *DR0* bis *DR3* enthalten dabei jeweils die [lineare Adresse](Paging "Lineare Adresse") eines Breakpoints. Dies kann ein Befehl, ein Datenbereich oder ein [I/O-Port](I-O-Ports "I/O-Ports") sein. Zu jedem dieser Register gehören mehrere Flags im Register *DR7*, die die Art des Breakpoints festlegen. Die CPU setzt beim Auslösen einer Debug Exception im Register *DR6* bestimmte Flags, die anzeigen welche Breakpoints erreicht wurden.

## Verwendung

Um einen Breakpoint zu setzen, lädt man eines der Register *DR0* bis *DR3* mit der Adresse und setzt die entsprechenden Flags in *DR7*. Beim Erreichen des Breakpoints wird der Interrupt 1 (*\#DB*) ausgelöst. Bei der Behandlung sollte man das DR6 Register auswerten, und danach auf 0 setzen, da die CPU möglicherweise nicht automatisch alle Flags vor der nächsten Exception zurücksetzt. Um zu verhindern, dass dieser Breakpoint bei der Rückkehr aus der ISR direkt wieder ausgelöst wird, sollte das Resume Flag (*RF*) im [EFLAGS](EFLAGS "EFLAGS")-Register (auf dem Stack) gesetzt werden.

Das Kapitel zu den Debug Registern im System Programming Guide der Intel Manuals sollte vor der Implementierung von Debugfunktionen gelesen werden. Im Folgenden ein grober Überblick über die wichtigsten Flags der Register *DR6* und *DR7*.

### DR7

DR7 legt fest, wann welcher Breakpoint ausgelöst werden soll.

| 31-30 | 29-28 | 27-26 | 25-24 | 23-22 | 21-20 | 19-18 | 17-16 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| LEN3 | R/W3 | LEN2 | R/W2 | LEN1 | R/W1 | LEN0 | R/W0 | 0 | 0 | GD | 0 | 0 | 1 | GE | LE | G3 | L3 | G2 | L2 | G1 | L1 | G0 | L0 |

- G0 und L0 aktivieren den Breakpoint in DR0. Der Unterschied zwischen G0 und L0 ist, dass L0 bei einem Task-Switch wieder gelöscht wird.
- Die beiden Bits in R/W0 bestimmen, wann ein Breakpoint an der Adresse in DR0 ausgelöst wird:
  - 00 - Ausführung einer Instruktion an dieser Adresse
  - 01 - Schreiben von Daten an dieser Adresse
  - 10 - I/O an dieser Adresse (verfügbar ab Pentium, bei gesetztem DE-Bit in [CR4](Control-Register "Control Register"))
  - 11 - Lesen oder Schreiben an dieser Adresse
- Die beiden Bits in LEN0 geben die Länge des vom Breakpoints überdeckten Bereichs an:
  - 00 - 1 Byte
  - 01 - 2 Bytes
  - 10 - 8 Bytes (bei bestimmten Prozessoren, siehe Intel Manual)
  - 11 - 4 Bytes

Breakpoints auf Instruktionen müssen immer mit der Länge 1 Byte (LEN0 = 00) erstellt werden. Breakpoints mit der Länge 2 Bytes bzw. 4 Bytes müssen auf 2- bzw. 4-Byte-Grenzen ausgerichtet sein (d.h. das untere bzw. die beiden unteren Bits der Adresse müssen 0 sein.)

- Die Felder G1-3, L1-3, R/W1-3 und LEN1-3 funktionieren analog für DR1-3.
- Wenn GD gesetzt ist, wird *\#DB* ausgelöst, wenn auf die Debug Register zugegriffen wird
- GE und LE sollten immer gesetzt sein, wenn man bei Breakpoints auf Datenzugriffen die genaue Instruktion herausbekommen will

### DR6

DR6 zeigt an, welche Bedingung einen Breakpoint ausgelöst hat.

| 31-16 | 15 | 14 | 13 | 12 | 11-4 | 3 | 2 | 1 | 0 |
| ------- | ----- | ----- | ----- | ----- | ------ | ----- | ----- | ----- | ----- |
| 1 | BT | BS | BD | 0 | 1 | B3 | B2 | B1 | B0 |

- B0-B3 zeigen an welcher der Breakpoints erreicht wurde (es können mehrere gleichzeitig gesetzt sein)
- BD ist gesetzt, wenn der Zugriff auf ein Debug Register die Exception ausgelöst hat
- BS ist gesetzt, wenn die Exception durch einen Single Step ausgelöst wurde
- BT ist gesetzt, wenn bei einem Task-Switch das T-Bit im [TSS](Task-State-Segment "TSS") gesetzt war

## Vergleich mit der Breakpoint-Instruktion

Die Breakpoint-Instruktion (*INT3*) ermöglicht das Setzen von Breakpoints im Code durch das Einfügen des direkten Aufrufs der Breakpoint Exception *\#BP* (Int 3). Beide Arten Breakpoints zu setzen ergänzen sich, da sie unterschiedliche Vor- und Nachteile mit sich bringen:

### Vorteile der Debug Register

- Breakpoints beim Daten- und I/O-Port-Zugriff
- Unterscheidung zwischen Lese- und Schreibzugriff
- Keine Manipulation des Codes notwendig

### Vorteile der Breakpoint-Instruktion

- Beliebig viele Breakpoints möglich
- Kann bereits im Compiler/Assembler gesetzt werden

## Unterstützung in Emulatoren

Beim Testen der Debug Funktionen sollte man beachten, dass vor allem ältere Emulatoren diese eventuell noch nicht unterstützen. Zum Beispiel sind sie in [Bochs](Bochs "Bochs") 2.4.1 nur teilweise implementiert. In [QEMU](QEMU "QEMU") ab Version 0.10 und [VirtualBox](VirtualBox "VirtualBox") scheinen sie hingegen zu funktionieren.

## Siehe auch

- Intel Manuals - Volume 3: System Programming Guide

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/7416/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1928/index.html)

<!-- MediaWiki page 1928; revision 7416; parent 5771; 2010-03-22T22:50:46Z -->
