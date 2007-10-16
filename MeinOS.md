# MeinOS

meinOS ist ein [Microkernel](https://github.com/lowlevel-eu/wiki/wiki/Ausgabe-2#der-microkernel "Ausgabe 2")-Betriebssystem für x86-Systeme. Es wird von [jgraef](https://lowlevel-eu.github.io/wiki/pages/1550/index.html "Benutzer:Jgraef") entwickelt.

## Entwicklung

meinOS ist noch in einer sehr frühen Entwicklungsphase, es wird aber schon fast komplettes Memorymanagement, Taskmanagement und IPC unterstützt. Da meinOS ein [Microkernel](https://github.com/lowlevel-eu/wiki/wiki/Ausgabe-2#der-microkernel "Ausgabe 2") ist und noch keine Programme für es entwickelt wurden, gibt es auch noch überhaupt keine Treiber.

## Komplett

- Memorymanagement (Speicherzuweisungs-Routinen nicht komplett)
- Taskmanagement (Routine zum erzeugen eines neuen Tasks und Dispatcher nicht komplett)
- IPC (Jeder Prozess hat für jeden Anderen 1 Byte Buffer; asynchrones IPC; Zuteilung über Ports)
- (Kernel-)Timer (100Hz) - zeitversetztes Aufrufen von Funktionen (z.B für Beep)
- (Kernel-)Textausgabe - die meisten Steuerzeichen werden unterstützt.

## Planung

- Init-Task (Initialisierung aller Treiber und des login-Programms)
- Filesystem
- devfd (FS-Treiber für /dev)
- Console-Treiber (Keyboard und Textdisplay)
- Floppy-Treiber
- FAT12-Treiber
- eventuell pipefs (Für Named Pipes ohne "richtiges" FS, dass Named Pipes unterstützt)

Wie man sieht, ist noch eine Menge zu tun.

## Links

- [meinOS-Website](http://wonsheimlan.wo.funpic.de/meinos/)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/2178/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1551/index.html)

<!-- MediaWiki page 1551; revision 2178; parent 0; 2007-10-16T17:14:15Z -->
