# Interrupt

Ein Interrupt ist ein Ereignis, welches die Arbeit der CPU unterbricht, um eine andere Routine auszuführen. Die CPU kann durch verschiedene Ursachen unterbrochen werden:

- ein Peripheriegerät fordert die Behandlung eines Interrupts ([IRQ](Programmable-Interrupt-Controller.md#irq-tabelle "IRQ"))
- im Programmfluss wird mit der Instruktion *int \<n\>* ein Software-Interrupt ausgelöst
- im Programm tritt eine [Exception](Exception.md "Exception") auf

## Arten von Interrupts

Es wird zwischen synchronen und asynchronen Unterbrechungen unterschieden. Als asynchrone Unterbrechungen werden Interrupts bezeichnet, die nicht vorhersagbar und nicht reproduzierbar sind. Sie treten bei wiederholter Ausführung des Programms nicht wieder oder nicht an der selben Stelle auf. Synchrone Interrupts werden hingegen ausgelöst, wenn die CPU genau definierte Bedingungen vorfindet, während sie eine Instruktion ausführt. Sie sind somit reproduzierbar und vorhersagbar.

### Synchrone Interrupts

Synchrone Interrupts werden bei der Intel Architektur in 3 Klassen aufgeteilt:

- Traps: Breakpoints, Overflow (INTO)
- Exceptions: z.B. Division durch 0, Page Faults
- Aborts: Double Fault

### Asynchrone Interrupts

Asynchrone Interrupts treten bei Ereignissen auf, die nicht vom Programm gezielt hervorgerufen wurden. Darunter fallen [IRQs](Programmable-Interrupt-Controller.md#irq-tabelle "IRQ"), die von Peripheriegeräten ausgelöst werden, und z.B. (aus Sicht eines Programms) Page Faults in Folge einer Auslagerung von Seiten aus dem RAM auf die Festplatte durch das Betriebssystem.

## Interrupt-Behandlung

Wenn ein Interrupt ausgelöst wird, sichert die CPU die Register [EFLAGS](EFLAGS.md "EFLAGS"), CS und EIP auf dem Stack. Danach wird eine Behandlungsroutine angesprungen, die in der [IDT](Interrupt-Descriptor-Table.md "IDT") (Protected Mode) bzw. in der [IVT](Interrupt-Vector-Table.md "IVT") (Real Mode) angegeben ist. Diese kehrt nach ihrer Ausführung im Allgemeinen mit dem Befehl *iret* zur Stelle, an der unterbrochen wurde, zurück.

In Interrupt-Behandlungsroutinen sollte je nach Art des Interrupts reagiert werden:

- In IRQs muss in der Regel das entsprechende Gerät ausgelesen werden. Außerdem muss der Erhalt der IRQs beim [PIC](Programmable-Interrupt-Controller.md "PIC") quittiert werden.
- Bei Software Interrupts sollte z.B. eine Systemfunktion im Kernel ausgeführt werden
- Exceptions müssen entweder gelöst werden, oder zum Abbruch des Programms führen

## Sperrung der Interrupts

Interrupts können mit Hilfe der Instruktionen *sti* und *cli* ein- bzw. ausgeschaltet werden. Dabei wird das [Interrupt Flag](EFLAGS.md#if---interrupt-enable-flag-bit-9 "EFLAGS") im Register EFLAGS gesetzt bzw. zurückgesetzt. Der Aufruf von Software-Interrupts, sowie Non-Maskable Interrupts können damit nicht unterbunden werden.

## Siehe auch

- [Programmable Interrupt Controller](Programmable-Interrupt-Controller.md "Programmable Interrupt Controller")
- [Interrupt Vector Table](Interrupt-Vector-Table.md "Interrupt Vector Table")
- [Interprocessor Interrupt](Interprocessor-Interrupt.md "Interprocessor Interrupt")
- [Non Maskable Interrupt](Non-Maskable-Interrupt.md "Non Maskable Interrupt")
- [Interrupt 13h](Interrupt-13h.md "Interrupt 13h")
- [Message Signaled Interrupt](Message-Signaled-Interrupt.md "Message Signaled Interrupt")
- Intel Manuals Volume 1A - Chapter 6 und Volume 3A - Chapter 5

## Links

- [Liste von BIOS-Interrupts](http://www.cs.cmu.edu/afs/cs/user/ralf/pub/WWW/files.html)
- [Tabelle zu BIOS-Interrupts](http://www.ctyme.com/intr/int.htm)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/10008/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1596/index.html)

<!-- MediaWiki page 1596; revision 10008; parent 9601; 2011-07-28T21:21:23Z -->
