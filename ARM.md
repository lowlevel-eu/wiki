# ARM

**ARM** (**A**corn **R**isc **M**achine) sind 32-Bit-Prozessoren nach dem [RISC](https://github.com/lowlevel-eu/wiki/wiki/Reduced-Instruction-Set-Computing "RISC")-Prinzip.

## Eigenschaften

Als ARM wird primär das Design des Prozessors bzw. der Prozessor-Architektur bezeichnet. Jedoch bezeichnet man Prozessoren, die nach ARM gebaut wurden als „ARM-Prozessoren“. ARM-Prozessoren zeichnen sich durch einen reduzierten und effizienten Befehlssatz und einen geringen Stromverbrauch aus.

## Einsatzgebiete

ARM-Prozessoren sind zwar vor allem bei PC-Anwendern nicht in aller Munde, stecken aber in erstaunlich vielen Geräten: In fast jedem Router ist ein ARM-Prozessor zu finden, der Apple iPod läuft mit einem ARM-Prozessor und der Game Boy Advance von Nintendo ermöglicht mobiles Spielen mit eben diesen ARM-Prozessoren (im Nintendo DS stecken sogar zwei dieser Sorte, einen für DS-Programme und einen für die GBA-Kompatibilität).

## Programmierung

Die „Lowlevel-Programmierung“ eines ARM-Prozessors mit Assembler unterscheidet sich signifikant von der eines x86-Prozessors. Ein ARM-Prozessor kennt drei Kategorien an Befehlen:

- Befehle zum Zugriff auf den Speicher
- Arithmetische oder logische Befehle auf Werte in Registern
- Befehle zum Ändern des Programmflusses (Sprünge, Subroutinen)

Anders als die x86-Architektur verfügt der ARM über einen Drei-Register-Befehlssatz, welcher es bei arithmetischen und logischen Befehlen ermöglicht, einen Ziel- sowie zwei Quellregister anzugeben:

\<asm\>

    add r0, r1, r2   ; r0 := r1 + r2

\</asm\>

Zusätzlich kann der zweite Quelloperand noch um einen bestimmten Wert rotiert oder geshiftet werden, der entweder fest angegeben oder einem weiteren Register entnommen wird. Somit können an einem arithmetisch-logischen Befehl bis zu vier Register beteiligt sein (z. B. entspricht ein „orr r0,r1,r2,lsl r3“ einem „r0 := r1 \| (r2 \<\< r3)“).

### Register

Es stehen 15 Allzweckregister zur Verfügung (ähnlich \*ax-Register der x86-Prozessoren): r0 bis r14. das Register r13 wird allerdings standardmäßig als Stackpointer genutzt und das Registger r14 als „Link-Register“, in welchem die Rücksprungadresse bei Prozeduraufrufen gespeichert wird. Das Register r15 dient als „Programmzähler“. Daneben gibt es ein Register namens CPSR (Current Program Status Register), in welchem Flags sowie Informationen wie das aktuelle Privileglevel stehen.

Die Register r13, r14 und das Statusregister werden „gespiegelt“, sodass man sich bei einer Exception und der dazugehörigen Behandlung nicht um die Sicherung des Stackpointers und des Instruction-Pointers kümmern muss.

#### CPSR

Das CPSR besteht aus drei Teilen. Die Bits 24 bis 31 sind Flags, die bei arithmetisch-logischen Befehlen dem Ergebnis entsprechend gesetzt oder gelöscht werden. Die Bits 16 bis 23 werden von SIMD-Befehlen als Flags genutzt, 0 bis 15 sind Kontrollbits, die den aktuellen Prozessormodus wiederspiegeln.

| Bit | Inhalt |
| --------- | ------------------------------------------------------------------------------------------ |
| 31 | N-Flag (Negative, negatives Ergebnis) |
| 30 | Z-Flag (Zero, Ergebnis 0) |
| 29 | C-Flag (Carry, vorzeichenloser Überlauf bei Addition, kein Überlauf bei Subtraktion) |
| 28 | V-Flag (Overflow, vorzeichenbehafteter Überlauf) |
| 27 | Q-Flag (Saturation/Overflow, wird bei Saturationsarithmetik verwendet) |
| 25 – 26 | Reserviert |
| 24 | J-Flag (Jazelle, Kontrollbit, s. u.) |
| 20 – 23 | Reserviert |
| 16 – 19 | GE (Greater than or Equal, werden bei SIMD verwendet) |
| 10 – 15 | Reserviert |
| 9 | E (Endianness, wird zum Einstellen der von der CPU verwendeten Daten-Endianness genutzt) |
| 8 | A (Imprecise Abort, deaktiviert solche) |
| 7 | I (IRQ disable, deaktiviert IRQs) |
| 6 | F (FIQ disable, deaktiviert FIQs) |
| 5 | T (Thumb, Kontrollbit, s. u.) |
| 0 – 4 | M (Mode, Nummer des aktuellen Prozessormodus, s. u.) |

Die J- und T-Bits sind Kontrollbits, die den aktuellen Opcodemodus des Prozessors angeben. ARM-Prozessoren unterstützen (bis zu) drei verschiedene Modi, den normalen ARM-Modus, den Thumbmodus mit kleineren Opcodes (s. u.) und den Jazelle-Modus, in dem JVM-Bytecode direkt ausgeführt werden kann. Das J-Bit steht für Jazelle, das T-Bit für Thumb. Manuell sollten sie niemals verändert werden.

M gibt den aktuellen Prozessormodus an. Folgende Werte sind definiert:

| Wert | Modus |
| ------ | ----------------------- |
| 0x10 | User |
| 0x11 | FIQ |
| 0x12 | IRQ |
| 0x13 | Abort |
| 0x17 | Supervisor |
| 0x1B | Undefined Instruction |
| 0x1F | System |

Was diese Modi bedeuten, wird im Abschnitt [Prozessor-Modi](https://github.com/lowlevel-eu/wiki/wiki/ARM#prozessor-modi "ARM") behandelt.

### Thumbmodus

Im normalen ARM-Modus belegt jeder Opcode ein Word Speicher, also vier Bytes. Dadurch ist ARM-Code häufig deutlich größer als vergleichbarer x86-Code. Um dieses Problem zu lösen, unterstützen viele ARM-Prozessoren einen zweiten Befehlssatz, der Thumb genannt wird. Ein Thumbopcode belegt nur zwei Byte Speicher. Dadurch stehen weniger Befehle zur Verfügung (die weggefallenen Befehle werden jedoch sowieso nur relativ selten verwendet) und mit normalen Instruktionen können auch nur noch acht der 16 Register (r0 bis r15) angesprochen werden. Auch gibt es jetzt keine arithmetisch-logischen Befehle mehr, die drei oder mehr Operanden verarbeiten können. Trotz dieser Einschränkungen wird der Thumbmodus häufig eingesetzt, da er eine deutliche Reduzierung der Codegröße ermöglicht. Zu beachten ist jedoch, dass Thumbcode im Allgemeinen langsamer als vergleichbarer ARM-Code verarbeitet wird, da aufgrund der genannten Einschränkungen mehr Thumbbefehle nötig sind, um die gleiche Wirkung zu erreichen.

## Prozessor-Modi

Bei ARM-Prozessoren gibt es sieben verschiedene Ausführungsmodi. Sechs davon sind Systemmodi, einer ist ein Usermodus, in dem bestimmte Instruktionen nicht erlaubt sind und Zugriff auf dem System zugehörige Pages verboten ist.

Wie beschrieben gibt es in jedem Modus ein eigenes r13 und r14 („Schattenregister“), die beim Moduswechsel automatisch umgeschaltet werden. Im sog. FIQ-Modus (s. u.) sind auch die Register r8 bis r12 zusätzlich vorhanden. Der System- und der Usermodus teilen sich r13 und r14.

Normalerweise wird der Prozessormodus gewechselt, wenn eine Exception aufgetreten ist (s. u.). Hier ist die Nutzung von Schattenregistern sehr vorteilhaft, da so z. B. automatisch ein bestimmter Stack (mit r13) ausgewählt wird. System- und Usermodus sind die einzigen Modi, die nicht durch eine Exception aktiviert werden können. Sie verwenden die gleichen Register, nur dass der Systemmodus eben ein privilegierter Modus ist. Aktiviert werden sie, indem das CPSR entsprechend geladen wird.

### Exceptions

Eine Exception ist jegliche Unterbrechnung des normalen Programmflusses, sei es aufgrund eines IRQs oder wegen eines Ausführungsfehlers. Tritt eine Exception auf, so schaltet der Prozessor in den zugehörigen Prozessormodus, wechselt in den ARM-Opcode-Modus, lädt r15 nach r14 und das alte CPSR nach SPSR (Saved PSR) und lädt einen exceptionspezifischen Wert nach r15. Folgende Exceptions gibt es:

| Name | CPU-Modus | r15-Offset | r14-Offset |
| ----------------------- | ----------------------------- | ------------ | ------------ |
| Reset | Supervisor (SVC) | 0x0000 | — |
| Undefined Instruction | Undefined Instruction (UND) | 0x0004 | +4 |
| Software Interrupt | Supervisor (SVC) | 0x0008 | +4 |
| Prefetch Abort | Abort (ABT) | 0x000C | +4 |
| Data Abort | Abort (ABT) | 0x0010 | +8 |
| IRQ | IRQ | 0x0018 | +8 |
| FIQ | FIQ | 0x001C | +8 |

Bei allen Exceptions werden IRQs deaktiviert, bei FIQ oder Reset zusätzlich noch FIQs. Der nach r15 geladene Wert ist der hier angegebene Wert, zu dem noch eine Basisadresse addiert wird. Normalerweise ist diese 0x00000000, kann jedoch auch als 0xFFFF0000 festgelegt werden („High vector“). Der Wert „r14-Offset“ gibt an, wie weit der in r14 stehende Wert von der Adresse des Befehls entfernt ist, an dem die Exception aufgetreten ist (angenommen, dass der Prozessor sich im ARM-Modus befand). Bei allen Exceptions mit +4 weiß die CPU zum Zeitpunkt der Aufnahme des Befehls in die Pipeline bereits, dass eine Exception auftreten wird, bei allen mit +8 wird dies erst bei der Ausführung bemerkt.

#### Reset

Ein Reset wird ausgelöst, indem eine entsprechende Leitung an der CPU aktiviert wird. Der Prozessor beginnt die Ausführung an der Adresse 0x00000000 im Supervisor- und ARM-Modus, mit deaktivierten IRQs und FIQs.

#### Undefined Instruction

Wird ein unbekannter Opcode erkannt oder wird ein Opcode im aktuellen Modus nicht unterstützt (privilegierte Befehle im Usermodus), dann wird diese Exception ausgelöst. Entweder wird das aktuelle Programm unterbrochen oder die Instruktion wird emuliert. Dies wird bei Gleitkommaberechnungen gezielt ausgenutzt: Zwar unterstützt z. B. der gcc mithilfe der libgcc auch Gleitkommaberechnungen ohne FPU, jedoch wird dies nur selten genutzt. Normalerweise wird FPU-Code generiert, selbst wenn bekannt ist, dass die Ziel-CPU keine FPU besitzt, da die allermeisten ARM-Betriebssysteme FPU-Befehle im UND-Handler emulieren. Dadurch kann der gleiche Code sowohl auf FPU-losen als auch auf Systemen mit FPU ausgeführt werden und erreicht dennoch auf letzteren die maximale Geschwindigkeit.

#### Software Interrupt

Diese Exception wird durch den SWI-Befehl (oder auch SVC-Befehl genannt) ausgelöst. Im Normalfall wird der SWI für Systemaufrufe genutzt.

#### Prefetch/Data Abort

Entsprechen dem Pagefault von x86. Sie werden ausgelöst, wenn beim Zugriff auf virtuellen Speicher ein Fehler aufgetreten ist (Speicher nicht gemappt oder nicht genügend Zugriffsrechte). Die Prefetch-Abort-Exception wird ausgelöst, wenn beim Laden eines Befehls ein Fehler aufgetreten ist, die Data-Abort-Exception bei Fehlern während der Ausführung.

Sogenannte Imprecise Aborts entstehen, wenn unabhängig vom eigentlichen Code auf virtuellen Speicher zugegriffen wird und dieser Zugriff einen Fehler auslöst. Es kann sein, dass die CPU sich dann in einem Modus befindet, in dem sie dann nicht sofort einen Abort auslösen kann, daher wird er zurückgestellt und erst später ausgelöst.

#### IRQ

Wird, wie der Name schon sagt, bei IRQs ausgelöst.

#### FIQ

Zusätzlich zu IRQs unterstützen ARMs auch FIQs (Fast IRQs). Sie werden ähnlich wie IRQs ausgelöst und behandelt, jedoch unterscheiden sich CPU-Modus und Priorität: Beim Auftreten einer IRQ-Exceptions werden IRQs deaktiviert (indem das IRQ-Disable-Bit im CPSR gesetzt wird), FIQs jedoch nicht. Dadurch können FIQs jederzeit IRQ-behandelnde Routinen unterbrechen. Weiterhin sind im FIQ-Modus auch die Register r8 bis r12 Schattenregister, sodass nur die Register r0 bis r7 bei Bedarf gesichert werden müssen. Beschränkt man sich auf die Verwendung von r8 bis r14, muss man überhaupt kein Register im Speicher sichern, sodass u. U. eine schnellere Abarbeitung des Interrupts möglich ist.

#### Rückkehr von einer Exception

Um von einer Exception zurückzukehren, müssen gleichzeitig r14 nach r15 und das SPSR ins CPSR geladen werden. Dies geschieht häufig mit einem arithmetisch-logischen Befehl, der r15 als Zielregister hat und bei dem das sogenannte S-Bit gesetzt ist. Normalerweise besagt dieses Bit, ob die Flags verändert werden sollen, ist jedoch r15 das Zielregister, dann bedeutet es, dass SPSR nach CPSR geladen werden soll. Je nach Exception muss ein anderer Befehl verwendet werden, da die verschiedenen Exceptions in unterschiedlicher Entfernung zum auslösenden Opcode stehen. Bei Undefined Opcode und SWI kann „movs r15,r14“ verwendet werden, um den Befehl zu überspringen. Bei Prefetch Abort muss „subs r15,r14,#4“ verwendet werden, um den Befehl noch einmal auszuführen, bei Data Abort ist es „subs r15,r14,#8“. Bei IRQ und FIQ lautet der Befehl „subs r15,r14,#4“, hierdurch wird die Ausführung fortgesetzt.

## Siehe auch

- [Cross-Compiler unter Linux für ARM](https://github.com/lowlevel-eu/wiki/wiki/ARM-Cross-Compiler "ARM Cross-Compiler")
- [RISC](https://github.com/lowlevel-eu/wiki/wiki/Reduced-Instruction-Set-Computing "RISC")
- [ARM-OS-Dev für Einsteiger](https://github.com/lowlevel-eu/wiki/wiki/ARM-OS-Dev-f%C3%BCr-Einsteiger "ARM-OS-Dev für Einsteiger")

## Weblinks

- [Offizielle ARM-Seite](http://infocenter.arm.com/help/index.jsp?noscript=1) – Spezifikationen und weitere Informationen
- [Erstellen einer „nackten“ ARM-Umgebung](http://www.embedded.com/columns/technicalinsights/200900043)
- [ARMv5 Architecture Reference](https://silver.arm.com/download/download.tm?pv=1073121) – (Anmeldung bei <http://www.arm.com> erforderlich)
- [ARMv7 Architecture Reference](https://silver.arm.com/download/download.tm?pv=1111932) – (Anmeldung erforderlich)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/10012/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2101/index.html)

<!-- MediaWiki page 2101; revision 10012; parent 9996; 2011-07-29T17:30:42Z -->
