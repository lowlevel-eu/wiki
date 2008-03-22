# Hardware Abstraction Layer

Die **HAL** (**H**ardware **A**bstraction **L**ayer) bezeichnet eine Softwareschicht, die zwischen der Hardware und dem [Betriebssystemkernel](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel") liegt. Sie hat die Aufgabe, hardwarespezifische Funktionen auszulagern, um eine spätere Portierung zu erleichtern, da im besten Fall nur die HAL angepasst werden muss. Auch [Microsoft Windows](https://github.com/lowlevel-eu/wiki/wiki/Windows "Windows") hat eine eigene HAL, die als Datei hal.dll vorliegt.

## Aufgaben

Die HAL beinhaltet somit folgende Aufgaben:

- [I/O Port](https://github.com/lowlevel-eu/wiki/wiki/I-O-Ports "I/O Ports")-Zugriffe
- [Interrupts](https://github.com/lowlevel-eu/wiki/wiki/Interrupt "Interrupt")
- [GDT](https://github.com/lowlevel-eu/wiki/wiki/Global-Descriptor-Table "GDT"), [IDT](https://github.com/lowlevel-eu/wiki/wiki/Interrupt-Descriptor-Table "IDT"), ...
- [Syscalls](https://github.com/lowlevel-eu/wiki/wiki/Syscall "Syscall")
- ...

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/2651/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1480/index.html)

<!-- MediaWiki page 1480; revision 2651; parent 2468; 2008-03-22T11:03:46Z -->
