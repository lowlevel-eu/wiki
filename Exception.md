# Exception

Diese Seite ist ein Artikel, welcher **mehr** haben könnte..  

Wenn du mehr darüber weißt oder recherchieren willst, bist **du** aufgerufen, dies zu tun. Wenn du dir in einer Sache nicht sicher bist, dann stell es auf die Diskussionsseite.

Als Exception (engl. Ausnahme) bezeichnet man einen Fehler, der während des Ausführens eines Programmes auftritt. Es entsteht also eine Ausnahmesituation, in der die Programmausführung nicht wie geplant fortgesetzt werden kann. Eine der bekanntesten Exception ist die 'Divide by Zero'-Exception, die auftritt, wenn man versucht durch Null zu teilen. Auf der x86-Architektur löst eine Exception, die nicht abgefangen wird, zunächst einen Double Fault aus, der selbst wieder eine Exception ist. Wird auch der Double Fault nicht abgefangen, führt dies zum Triple Fault und ein CPU-Reset wird durchgeführt.

## Abfangen von Exceptions

Die Exceptions sind im Grunde wie [Interrupts](https://github.com/lowlevel-eu/wiki/wiki/Interrupt "Interrupt"). Sie werden aber nichht von der Software über die "int x"-Instruktion ausgelöst, sondern von der CPU selbst, wenn diese auf Fehler in der Codeausführung stößt. Die Exceptions werden den Interrupts 0 bis 31 zugeordent. D.h., um Exceptions abzufangen, muss man die entsprechenden Interrupts abfangen und behandeln.

### Behandeln von Exceptions

Wie bei allen Interrupts legt die CPU die Werte der Register CS, EIP, EFLAGS, SS und ESP auf dem [Stack](https://github.com/lowlevel-eu/wiki/wiki/Stack "Stack") ab, bevor sie die in die [Interrupt-Behandlungs-Routine](https://github.com/lowlevel-eu/wiki/wiki/Interrupt-Service-Routine "ISR") springt. Bei manchen Exceptions legt die CPU zusätzlich noch einen Fehlercode auf den Stack, der zusätzliche Informationen zum Fehler enthält. Wie dieser Fehlercode zu interpretieren ist, wird unten bei den Excpetions beschrieben. Zu beachten ist außerdem, dass das CS:EIP Registerpaar bei Exceptions des Typs Fault immer auf die Instruktion zeigen, die den Fehler verursachte, bei den anderen Exceptions muss dies nicht der Fall sein.

## Arten von Exceptions

Man teilt Exceptions in drei Arten ein:

- **Traps** (Fallen): Unterbrechen ein Programm nach einer bestimmten Instruktion oder nach einer Instruktion an einer bestimmten Stelle.
- **Faults** (Fehler): Unterbrechen ein Programm, wenn eine Instruktion nicht ausgeführt werden kann. Der Kernel kann den Fehler aber ggf. beheben und dann das Programm fortfahren. Manche Fehler sind sogar planmäßig vom Kernel eingesetzt, so z.B der Page Fault.
- **Aborts** (Abbrüche): Sind nicht behebbare Fehler.

## Liste der Exceptions

| Vektor | Bezeichnung | Typ | Fehlercode |
| ----------- | ------------------------------------------------------------------------------ | ------------ | ------------ |
| 0x00 | \#DE - Divide by Zero | Fault | nein |
| 0x01 | \#DB - Debug | Fault/Trap | nein |
| 0x02 | [NMI](https://github.com/lowlevel-eu/wiki/wiki/Non-Maskable-Interrupt "NMI") | \- | nein |
| 0x03 | \#BP - Breakpoint | Trap | nein |
| 0x04 | \#OF - Overflow | Trap | nein |
| 0x05 | \#BR - Bound Range | Fault | nein |
| 0x06 | \#UD - Invalid Opcode | Fault | nein |
| 0x07 | \#NM - Device Not Available | Fault | nein |
| 0x08 | \#DF - Double Fault |  |  |
| 0x09 | Coprocessor Segment Overrun |  |  |
| 0x0a | \#TS - Invalid TSS |  |  |
| 0x0b | \#NP - Segment not Present |  |  |
| 0x0c | \#SS - Stack |  |  |
| 0x0d | \#GP - General Protection |  |  |
| 0x0e | \#PF - Page Fault |  |  |
| 0x0f | *Reserviert* |  |  |
| 0x10 | \#MF - x87 Floating Point |  |  |
| 0x11 | \#AC - Alignment Check |  |  |
| 0x12 | \#MC - Machine Check |  |  |
| 0x13 | \#XF - SIMD Floating Point |  |  |
| 0x14-0x1f | *Reserviert* |  |  |

## Nähere Erläuterung

### Divide By Zero

Tritt bei den DIV und IDIV Instruktionen auf, wenn der Teiler Null ist.

### Debug

Wird durch die [Debug Register](https://github.com/lowlevel-eu/wiki/wiki/Debug-Register "Debug Register") gesteuert.

### Breakpoint

Diese Exception wird durch die "int 3"-Instruktion ausgelöst und kann zu Debugging-Zwecken genutzt werden. Die "int 3"-Instruktion besitzt einen speziellen Opcode und ist nur ein Byte groß. Das CS:EIP Registerpaar auf dem Stack zeigt auf die Instruktion **nach** der "int 3"-Instruktion.

### Overflow

Die Overflow-Exception wird durch die "into"-Instruktion ausgelöst. Die CPU überprüft das Overflow-Flag und löst dann diese Exception aus, wen es gesetzt ist.

### Bound Range

Diese Exceptions wird durch die "bound"-Instruktion ausgelöst, die Arrays auf Grenzen überprüft.

### Invalid Opcode

Wird ausgelöst, wenn die CPU auf einen ungültigen Opcode oder einen gültigen Opcode mit ungültigen Parametern stößt.

### Device Not Available

Wird ausgelöst, wenn ein FPU-Instruktion ausgeführt werden soll, obwohl an den Computer keine FPU angeschlossen ist. Dieser Fehler ist bei neueren Computern eher nicht mehr relevant.

//TODO: die restlichen Exceptions beschreiben //TODO: Exceptions mit der Tabelle oben verlinken

## Weblinks

<http://www.logix.cz/michal/doc/i386/chp09-08.htm> (Englisch)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/9187/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1824/index.html)

<!-- MediaWiki page 1824; revision 9187; parent 8032; 2010-12-30T16:34:08Z -->
