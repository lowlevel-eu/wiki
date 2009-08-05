# Hardware Abstraction Layer

Die **HAL** (**H**ardware **A**bstraction **L**ayer) bezeichnet eine Softwareschicht, die zwischen der Hardware und dem [Betriebssystemkernel](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel") liegt. Sie hat die Aufgabe, hardwarespezifische Funktionen auszulagern, um eine spätere Portierung zu erleichtern, da im besten Fall nur die HAL angepasst werden muss. Die verbreitesten Betriebsysteme haben eine HAL.

## Aufgaben

Die HAL beinhaltet somit folgende Aufgaben:

- [I/O Port](https://github.com/lowlevel-eu/wiki/wiki/I-O-Ports "I/O Ports")-Zugriffe
- [Interrupts](https://github.com/lowlevel-eu/wiki/wiki/Interrupt "Interrupt") (IRQs), [Interrupt Service Routines](https://github.com/lowlevel-eu/wiki/wiki/Interrupt-Service-Routine "Interrupt Service Routine") (ISRs)
- [GDT](https://github.com/lowlevel-eu/wiki/wiki/Global-Descriptor-Table "GDT"), [IDT](https://github.com/lowlevel-eu/wiki/wiki/Interrupt-Descriptor-Table "IDT"), [IRQ](https://github.com/lowlevel-eu/wiki/wiki/Programmable-Interrupt-Controller#irq-tabelle "IRQ"), [PIC](https://github.com/lowlevel-eu/wiki/wiki/Programmable-Interrupt-Controller "PIC"), ...
- [Syscalls](https://github.com/lowlevel-eu/wiki/wiki/Syscall "Syscall")
- [Paging](https://github.com/lowlevel-eu/wiki/wiki/Paging "Paging")
- ...

## Implentierung einer HAL

Die Implentierung einer HAL ist im Protected Mode einfach:

- Die [GDT](https://github.com/lowlevel-eu/wiki/wiki/Global-Descriptor-Table "GDT") mit ihr Rechteverwaltung.
- ...

## [Exokernel](https://github.com/lowlevel-eu/wiki/wiki/Kernel#exokernel "Exokernel")

Eine besondere Rolle hat der [Exokernel](https://github.com/lowlevel-eu/wiki/wiki/Kernel#exokernel "Exokernel"). Dieser hat normalerweise keine HAL.

## Ältere Betriebsysteme

[MS-DOS](https://github.com/lowlevel-eu/wiki/wiki/Microsoft-Disk-Operating-System "MS-DOS") hatte keine HAL, zumindest wenn es nicht mit Windows aufgerüstet worden war.

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/5077/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1480/index.html)

<!-- MediaWiki page 1480; revision 5077; parent 5074; 2009-08-05T19:26:46Z -->
