# Exception

Diese Seite oder Abschnitt ist zwar komplett, es wird aber folgende Verbesserungen gewünscht:  

- Einige Exceptions ausführlicher beschreiben
- Mehr praktische Hinweise

Hilf Lowlevel, den Artikel zu verbessern.

  
Als Exception (engl. Ausnahme) bezeichnet man einen Fehler, der während des Ausführens eines Programmes auftritt. Es entsteht also eine Ausnahmesituation, in der die Programmausführung nicht wie geplant fortgesetzt werden kann. Eine der bekanntesten Exception ist die 'Divide by Zero'-Exception, die auftritt, wenn man versucht durch Null zu teilen. Auf der x86-Architektur löst eine Exception, die nicht abgefangen wird, zunächst einen Double Fault aus, der selbst wieder eine Exception ist. Wird auch der Double Fault nicht abgefangen, führt dies zum Triple Fault und ein CPU-Reset wird durchgeführt.

## Abfangen von Exceptions

Die Exceptions sind im Grunde wie [Interrupts](https://github.com/lowlevel-eu/wiki/wiki/Interrupt "Interrupt"). Sie werden aber nicht von der Software über die "int x"-Instruktion ausgelöst, sondern von der CPU selbst, wenn diese auf Fehler in der Codeausführung stößt. Die Exceptions werden den Interrupts 0 bis 31 zugeordnet. D.h., um Exceptions abzufangen, muss man die entsprechenden Interrupts abfangen und behandeln.

### Behandeln von Exceptions

Wie bei allen Interrupts legt die CPU die Werte der Register CS, EIP, EFLAGS, SS und ESP auf dem [Stack](https://github.com/lowlevel-eu/wiki/wiki/Stack "Stack") ab, bevor sie die in die [Interrupt-Behandlungs-Routine](https://github.com/lowlevel-eu/wiki/wiki/Interrupt-Service-Routine "ISR") springt. Bei manchen Exceptions legt die CPU zusätzlich noch einen Fehlercode auf den Stack, der zusätzliche Informationen zum Fehler enthält. Wie dieser Fehlercode zu interpretieren ist, wird unten bei den Exceptions beschrieben. Zu beachten ist außerdem, dass das CS:EIP Registerpaar bei Exceptions des Typs Fault immer auf die Instruktion zeigen, die den Fehler verursachte, bei den anderen Exceptions muss dies nicht der Fall sein.

## Arten von Exceptions

Man teilt Exceptions in drei Arten ein:

- **Traps** (Fallen): Unterbrechen ein Programm nach einer bestimmten Instruktion oder nach einer Instruktion an einer bestimmten Stelle.
- **Faults** (Fehler): Unterbrechen ein Programm, wenn eine Instruktion nicht ausgeführt werden kann. Der Kernel kann den Fehler aber ggf. beheben und dann das Programm fortfahren. Manche Fehler sind sogar planmäßig vom Kernel eingesetzt, so z.B der Page Fault.
- **Aborts** (Abbrüche): Sind nicht behebbare Fehler.

## Liste der Exceptions

| Vektor | Bezeichnung | Typ | Fehlercode |
| ----------- | ---------------------------------------------------------------------------------------------------------------------------- | ------------ | ------------ |
| 0x00 | \#DE - [Divide by Zero](https://github.com/lowlevel-eu/wiki/wiki/Exception#divide-by-zero "Exception") | Fault | nein |
| 0x01 | \#DB - [Debug](https://github.com/lowlevel-eu/wiki/wiki/Exception#debug "Exception") | Fault/Trap | nein |
| 0x02 | \#NMI - [Non Maskable Interrupt](https://github.com/lowlevel-eu/wiki/wiki/Non-Maskable-Interrupt "Non Maskable Interrupt") | \- | nein |
| 0x03 | \#BP - [Breakpoint](https://github.com/lowlevel-eu/wiki/wiki/Exception#breakpoint "Exception") | Trap | nein |
| 0x04 | \#OF - [Overflow](https://github.com/lowlevel-eu/wiki/wiki/Exception#overflow "Exception") | Trap | nein |
| 0x05 | \#BR - [Bound Range](https://github.com/lowlevel-eu/wiki/wiki/Exception#bound-range "Exception") | Fault | nein |
| 0x06 | \#UD - [Invalid Opcode](https://github.com/lowlevel-eu/wiki/wiki/Exception#invalid-opcode "Exception") | Fault | nein |
| 0x07 | \#NM - [Device Not Available](https://github.com/lowlevel-eu/wiki/wiki/Exception#device-not-available "Exception") | Fault | nein |
| 0x08 | \#DF - [Double Fault](https://github.com/lowlevel-eu/wiki/wiki/Exception#double-fault "Exception") | Abort | ja |
| 0x09 | [Coprocessor Segment Overrun](https://github.com/lowlevel-eu/wiki/wiki/Exception#coprocessor-segment-overrun "Exception") | \- | nein |
| 0x0a | \#TS - [Invalid TSS](https://github.com/lowlevel-eu/wiki/wiki/Exception#invalid-tss "Exception") | Fault | ja |
| 0x0b | \#NP - [Segment not Present](https://github.com/lowlevel-eu/wiki/wiki/Exception#segment-not-present "Exception") | Fault | ja |
| 0x0c | \#SS - [Stack Fault](https://github.com/lowlevel-eu/wiki/wiki/Exception#stack-fault "Exception") | Fault | ja |
| 0x0d | \#GP - [General Protection](https://github.com/lowlevel-eu/wiki/wiki/Exception#general-protection "Exception") | Fault | ja |
| 0x0e | \#PF - [Page Fault](https://github.com/lowlevel-eu/wiki/wiki/Exception#page-fault "Exception") | Fault | ja |
| 0x0f | *Reserviert* | \- | \- |
| 0x10 | \#MF - [x87 Floating Point](https://github.com/lowlevel-eu/wiki/wiki/Exception#x87-floating-point "Exception") | Fault | nein |
| 0x11 | \#AC - [Alignment Check](https://github.com/lowlevel-eu/wiki/wiki/Exception#alignment-check "Exception") | Fault | ja |
| 0x12 | \#MC - [Machine Check](https://github.com/lowlevel-eu/wiki/wiki/Exception#machine-check "Exception") | Abort | nein |
| 0x13 | \#XF - [SIMD Floating Point](https://github.com/lowlevel-eu/wiki/wiki/Exception#simd-floating-point "Exception") | Fault | nein |
| 0x14-0x1f | *Reserviert* | \- | \- |

## Nähere Erläuterung

### Divide By Zero

Tritt bei den DIV und IDIV Instruktionen auf, wenn der Teiler Null ist.

### Debug

Wird durch die [Debug Register](https://github.com/lowlevel-eu/wiki/wiki/Debug-Register "Debug Register") gesteuert.

### Non Maskable Interrupt

Das ist nicht wirklich eine Exception sondern eine Art externer Interrupt der aber nicht durch das IE-Flag gesperrt werden kann. Genauere Infos: [Non Maskable Interrupt](https://github.com/lowlevel-eu/wiki/wiki/Non-Maskable-Interrupt "Non Maskable Interrupt").

### Breakpoint

Diese Exception wird durch die "int 3"-Instruktion ausgelöst und kann zu Debugging-Zwecken genutzt werden. Die "int 3"-Instruktion besitzt einen speziellen Opcode und ist nur ein Byte groß. Das CS:EIP Registerpaar auf dem Stack zeigt auf die Instruktion **nach** der "int 3"-Instruktion.

### Overflow

Die Overflow-Exception wird durch die "into"-Instruktion ausgelöst. Die CPU überprüft das Overflow-Flag und löst dann diese Exception aus, wenn es gesetzt ist.

### Bound Range

Diese Exceptions wird durch die "bound"-Instruktion ausgelöst, die Arrays auf Grenzen überprüft.

### Invalid Opcode

Wird ausgelöst, wenn die CPU auf einen ungültigen Opcode oder einen gültigen Opcode mit ungültigen Parametern stößt.

### Device Not Available

Wird ausgelöst, wenn eine FPU-Instruktion ausgeführt werden soll, obwohl an den Computer keine FPU angeschlossen ist. Dieser Fehler ist bei neueren Computern eher nicht mehr relevant.

### Double Fault

Wenn eine Exception eintritt während die CPU versucht, den Handler für eine andere Exception aufzurufen, dann bezeichnet man dies als Double Fault. Dieser ist im Grunde der letzte Schritt vorm Triple Fault (Systemabsturz) und kann nicht in irgendeiner Art behoben werden.

### Coprocessor Segment Overrun

???

### Invalid TSS

Die Exception wird ausgelöst, wenn die CPU beim Taskswitch auf ein ungültiges TSS trifft. Sie übergibt auf dem Stack einen Errorcode:

| Bits | Bedeutung |
| ------- | -------------------------------------------------------------- |
| 0 | Gesetzt: Die Exception hat ihren Ursprung außerhalb der CPU |
| 1,2 | 0: GDT, 1 und 3: IDT, 2: LDT |
| 3-15 | Index in der GDT, IDT oder LDT, je nach Wert von Bit 1 und 2 |
| 16-31 | reserviert |

### Segment not Present

Diese Exception wird ausgelöst, wenn die CPU ein Segmentregister (DS, ES, FS, GS, CS) mit einem ungültigen Wert füllt. Ungültige Werte meint hierbei einen Deskriptor, der als nicht aktiv oder in irgendeiner anderen Form ungültig ist. Beim Laden des SS Register tritt ein Stack Fault auf.

### Stack Fault

Der Stack Fault tritt auf, wenn der Stack seine maximale Größe erreicht hat oder das SS-Register mit einem ungültigen Wert geladen wird.

### General Protection

Der General Protection Fault tritt bei jeder Art von Rechteverletzung auf, die nicht von einer anderen Exception abgefangen wird. Als Error-Code wird die Segmentnummer übergeben, bei der die Exception auftrat.

### Page Fault

Der Page Fault wird ausgelöst, wenn ein Programm...

- auf eine Page zugreift, die nicht aktiv ist (Present-Bit gelöscht).
- Daten in eine Page schreibt, die als nur lesbar markiert ist.
- auf eine Page zugreift, dessen Reserved-Bit gesetzt ist.
- in Ring 3 (Usermode) läuft und auf eine Page zugreift, die nur für den Kernel (Ring 0) zugänglich ist.

Die CPU übergibt zusätzlich noch einen Errorcode auf dem Stack:

| Bit | Bedeutung |
| ----- | -------------------------------------------------------------------------------------------------- |
| 0 | Wenn gelöscht, dann wurde der Fault durch eine nicht aktive Page ausgelöst |
| 1 | Wenn gesetzt, dann wurde der Fault durch einen Schreibzugriff ausgelöst |
| 2 | Wenn gestzt, dann hatte das Programm nur Usermode-Rechte |
| 3 | Wenn gesetzt, dann hatte das Reserved-Feld den Wert 1 |
| 4 | Wenn gesetzt, dann wurde der Fault durch einen Zugriff auf Code ausgelöst, andernfalls auf Daten |

Außerdem übergibt die CPU im [CR2](https://github.com/lowlevel-eu/wiki/wiki/Control-Register "Control Register") die Adresse, auf die zugegriffen wurde.

#### Planmäßiger Einsatz des Page Faults

Der Page Fault ist oftmals nicht auf einen wirklichen Fehler zurückzuführen, sondern wird planmäßig eingesetzt.

Wenn bei aktiviertem [Paging](https://github.com/lowlevel-eu/wiki/wiki/Paging "Paging") eine Speicherseite nicht zugegriffen werden kann, kann das beispielsweise daran liegen, dass diese Seite auf die Festplatte ausgelagert worden ist. In diesem Fall lädt der Kernel die Seite wieder in den Speicher und springt zurück in das Programm. Diese Methode bezeichnet man als [Swapping](https://github.com/lowlevel-eu/wiki/wiki/Swapping "Swapping").

Eine weitere Anwendungsmöglichkeit ist Copy on Write. Es kommt zum Einsatz, wenn ganze Pages kopiert werden - z.B. bei unixoiden Systemen bei fork(), dem Klonen von Prozessen. Dabei werden alle zu kopierenden Seiten zunächst nicht wirklich kopiert, sondern sowohl im alten als auch neuen Prozess als schreibgeschützt markiert. Erst bei Bedarf, also wenn sich die Originalpage und Kopie zum ersten Mal unterscheiden, wird wirklich kopiert: Beim ersten Schreibzugriff auf eine solche Seite wird ein Page Fault abgefangen (der ausgelöst wird, weil der Bereich schreibgeschützt ist) und eine zweite Page für die Kopie alloziert.

### x87 Floating Point

???

### Alignment Check

Wenn auf nicht ausgerichtete Daten zugegriffen wird und das AM Bit in CR0 sowie das AC in den EFLAGS sind gesetzt, dann wird diese Exception ausgelöst. In der Regel trifft man nicht auf diese Exception, weil Alignment Checks standartmäßig ausgeschaltet sind.

### Machine Check

???

### SIMD Floating Point

Wenn das Exception Mask Bit in MXCSR gelöscht ist und das CR4.OSXMMEXCPT Bit gesetzt ist, so löst eine 128-Bit Floating Point Exception diese Exception aus. Ist das Exception Mask Bit gesetzt, so wird keine Exception ausgelöst. Ist CR4.OSXMMEXCPT gelöscht, so wird statt der SIMD Floating Point Exception eine [Invalid Opcode Exception](https://github.com/lowlevel-eu/wiki/wiki/Exception#invalid-opcode "Exception") ausgelöst.

## Weblinks

<http://www.logix.cz/michal/doc/i386/chp09-08.htm> (Englisch)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/9731/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1824/index.html)

<!-- MediaWiki page 1824; revision 9731; parent 9377; 2011-05-02T15:52:35Z -->
