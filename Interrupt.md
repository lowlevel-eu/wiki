# Interrupt

Ein Interrupt ist ein Ereignis, welches die Arbeit der CPU unterbricht, um eine andere Routine auszuführen. Die CPU kann durch verschiedene Ursachen unterbrochen werden:

- ein Peripheriegerät fordert die Behandlung eines Interrupts ([IRQ](https://github.com/lowlevel-eu/wiki/wiki/Programmable-Interrupt-Controller#irq-tabelle "IRQ"))
- im Programmfluss wird mit der Instruktion *int \<n\>* ein Software-Interrupt ausgelöst
- im Programm tritt eine [Exception](https://github.com/lowlevel-eu/wiki/wiki/Exception "Exception") auf

## Arten von Interrupts

Es wird zwischen synchronen und asynchronen Unterbrechungen unterschieden. Als asynchrone Unterbrechungen werden Interrupts bezeichnet, die nicht vorhersagbar und nicht reproduzierbar sind. Sie treten bei wiederholter Ausführung des Programms nicht wieder oder nicht an der selben Stelle auf. Synchrone Interrupts werden hingegen ausgelöst, wenn die CPU genau definierte Bedingungen vorfindet, während sie eine Instruktion ausführt. Sie sind somit reproduzierbar und vorhersagbar.

### Synchrone Interrupts

Synchrone Interrupts werden bei der Intel Architektur in 3 Klassen aufgeteilt:

- Traps: Breakpoints, Overflow (INTO)
- Exceptions: z.B. Division durch 0, Page Faults
- Aborts: Double Fault

### Asynchrone Interrupts

Asynchrone Interrupts treten bei Ereignissen auf, die nicht vom Programm gezielt hervorgerufen wurden. Darunter fallen [IRQs](https://github.com/lowlevel-eu/wiki/wiki/Programmable-Interrupt-Controller#irq-tabelle "IRQ"), die von Peripheriegeräten ausgelöst werden, und z.B. (aus Sicht eines Programms) Page Faults in Folge einer Auslagerung von Seiten aus dem RAM auf die Festplatte durch das Betriebssystem.

## Interrupt-Behandlung

Wenn ein Interrupt ausgelöst wird, sichert die CPU die Register [EFLAGS](https://github.com/lowlevel-eu/wiki/wiki/EFLAGS "EFLAGS"), CS und EIP auf dem Stack. Danach wird eine Behandlungsroutine angesprungen, die in der [IDT](https://github.com/lowlevel-eu/wiki/wiki/Interrupt-Descriptor-Table "IDT") (Protected Mode) bzw. in der [IVT](https://github.com/lowlevel-eu/wiki/wiki/Interrupt-Vector-Table "IVT") (Real Mode) angegeben ist. Diese kehrt nach ihrer Ausführung im Allgemeinen mit dem Befehl *iret* zur Stelle, an der unterbrochen wurde, zurück.

In Interrupt-Behandlungsroutinen sollte je nach Art des Interrupts reagiert werden:

- In IRQs muss in der Regel das entsprechende Gerät ausgelesen werden. Außerdem muss der Erhalt der IRQs beim [PIC](https://github.com/lowlevel-eu/wiki/wiki/Programmable-Interrupt-Controller "PIC") quittiert werden.
- Bei Software Interrupts sollte z.B. eine Systemfunktion im Kernel ausgeführt werden
- Exceptions müssen entweder gelöst werden, oder zum Abbruch des Programms führen

## Sperrung der Interrupts

Interrupts können mit Hilfe der Instruktionen *sti* und *cli* ein- bzw. ausgeschaltet werden. Dabei wird das [Interrupt Flag](https://github.com/lowlevel-eu/wiki/wiki/EFLAGS#if---interrupt-enable-flag-bit-9 "EFLAGS") im Register EFLAGS gesetzt bzw. zurückgesetzt. Der Aufruf von Software-Interrupts, sowie Non-Maskable Interrupts können damit nicht unterbunden werden.

## Siehe auch

- [Programmable Interrupt Controller](https://github.com/lowlevel-eu/wiki/wiki/Programmable-Interrupt-Controller "Programmable Interrupt Controller")
- [Interrupt Vector Table](https://github.com/lowlevel-eu/wiki/wiki/Interrupt-Vector-Table "Interrupt Vector Table")
- [Interprocessor Interrupt](https://github.com/lowlevel-eu/wiki/wiki/Interprocessor-Interrupt "Interprocessor Interrupt")
- [Non Maskable Interrupt](https://github.com/lowlevel-eu/wiki/wiki/Non-Maskable-Interrupt "Non Maskable Interrupt")
- [Interrupt 13h](https://github.com/lowlevel-eu/wiki/wiki/Interrupt-13h "Interrupt 13h")
- [Message Signaled Interrupt](https://github.com/lowlevel-eu/wiki/wiki/Message-Signaled-Interrupt "Message Signaled Interrupt")
- Intel Manuals Volume 1A - Chapter 6 und Volume 3A - Chapter 5

## Links

[Liste von BIOS-Interrupts](http://www.cs.cmu.edu/afs/cs/user/ralf/pub/WWW/files.html)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/9570/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1596/index.html)

<!-- MediaWiki page 1596; revision 9570; parent 4801; 2011-02-19T14:05:38Z -->
