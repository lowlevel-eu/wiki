# Hardware Abstraction Layer

Die **HAL** (Hardware Abstraction Layer) bezeichnet eine Softwareschicht, die zwischen der Hardware dem [Betriebssystemkernel](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel") liegt. Sie hat die Aufgabe, hardwarespezifische Funktionen auszulagern, um eine spätere Portierbarkeit zu erleichtern, da im besten Fall nur die HAL angepasst werden muss. Auch Microsoft Windows hat eine eigene HAL, die als Datei hall.dll vorliegt.

## Aufgaben

Die HAL beinhaltet somit folgende Aufgaben:

- Port-Zugriffe
- Interrupts
- GDT,IDT,...
- Exceptions
- ...

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/1743/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1480/index.html)

<!-- MediaWiki page 1480; revision 1743; parent 0; 2007-01-18T21:35:12Z -->
