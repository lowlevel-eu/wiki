# Hardware Abstraction Layer

Die **HAL** (**H**ardware **A**bstraction **L**ayer) bezeichnet eine Softwareschicht, die zwischen der Hardware und dem [Betriebssystemkernel](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel") liegt. Sie hat die Aufgabe, hardwarespezifische Funktionen auszulagern, um eine spätere Portierbarkeit zu erleichtern, da im besten Fall nur die HAL angepasst werden muss. Auch [Microsoft Windows](https://github.com/lowlevel-eu/wiki/wiki/Windows "Windows") hat eine eigene HAL, die als Datei hal.dll vorliegt.

## Aufgaben

Die HAL beinhaltet somit folgende Aufgaben:

- Port-Zugriffe
- Interrupts
- GDT,IDT,...
- Exceptions
- ...

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/2464/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1480/index.html)

<!-- MediaWiki page 1480; revision 2464; parent 1746; 2007-12-21T15:31:42Z -->
