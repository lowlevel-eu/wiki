# Page Size Extension

Die Page Size Extension von x86-Prozessoren wurde mit dem Pentium-Prozessor eingeführt. Es ermöglicht [Paging](https://github.com/lowlevel-eu/wiki/wiki/Paging "Paging") mit sogenannten *large pages*, also [Pages](https://github.com/lowlevel-eu/wiki/wiki/Paging#funktionsweise "Paging"), die statt 4KB einen 4MB großen Speicherbereich repräsentieren.

## Vorteile

- Es wird deutlich weniger Speicherplatz durch Pagetables verbraucht. (Im günstigsten Fall 4MB weniger)
- Der [Translation Lookaside Buffer](https://github.com/lowlevel-eu/wiki/wiki/Paging#translation-lookaside-buffer "Translation Lookaside Buffer") kann besser arbeiten.
- 4MB und 4KB große Pages können auch gleichzeitig verwendet werden.

## Funktionsweise

### Unterschied zum 4KB-Paging

Beim "normalen" Paging zeigt jeder der 1024 Einträge im [Page Directory](https://github.com/lowlevel-eu/wiki/wiki/Paging "Paging") auf eine 4KB große [Page Table](https://github.com/lowlevel-eu/wiki/wiki/Paging "Paging"), deren 1024 Einträge wiederrum einen 4 MB großen Bereich definieren. Somit sind insgesamt 4 MB Speicherplatz durch Page Tables belegt.

Wenn PSE aktiviert ist, dann wird Bit 7 (S-Bit) in den Einträgen des Page Directory gültig. Ist dieses Bit nicht gesetzt, dann zeigt der Eintrag auf eine Page Table mit 4KB-Pages (so wie beim "normalen" Paging), andernfalls zeigt der Eintrag direkt auf eine 4MB-Page. Falls man also nur 4MB-Pages verwendet (alle S-Bits sind gesetzt), bedeutet das, dass man keine Page Tables mehr benötigt, weil das Page Directory alle Pages direkt definiert.

### Aktivieren der Page Size Extension

- ein Page Directory mit 1024 Einträge anlegen
  - ist das S-Bit gesetzt, dann zeigt der Eintrag direkt auf eine 4MB-Page
  - ist das S-Bit nicht gesetzt, muss eine Page Table angelegt werden, auf die der Eintrag zeigt
- in das [Control Register](https://github.com/lowlevel-eu/wiki/wiki/Control-Register "Control Register") cr3 die Adresse des Page Directory laden
- PSE aktivieren, indem Bit 4 im Control Register cr4 gesetzt wird
- Paging aktivieren, indem Bit 31 im Control Register cr0 gesetzt wird

## Siehe auch

- [Paging](https://github.com/lowlevel-eu/wiki/wiki/Paging "Paging")

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/6927/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1999/index.html)

<!-- MediaWiki page 1999; revision 6927; parent 6925; 2010-01-17T21:10:10Z -->
