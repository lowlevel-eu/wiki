# Page Size Extension

Die Page Size Extension von x86-Prozessoren wurde mit dem Pentium-Prozessor eingeführt. Es ermöglicht [Paging](Paging "Paging") mit sogenannten *large pages*, also [Pages](Paging#funktionsweise "Paging"), die statt 4KB einen 4MB großen Speicherbereich repräsentieren.

## Vorteile

- Es wird deutlich weniger Speicherplatz durch Pagetables verbraucht. (Im günstigsten Fall 4MB weniger)
- 4MB und 4KB große Pages können auch gleichzeitig verwendet werden.
- Der [Translation Lookaside Buffer](Paging#translation-lookaside-buffer "Translation Lookaside Buffer") wird besser ausgenutzt (es gibt üblicherweise zwei separate TLBs für 4k- und 4M-Pages; mit 4k-Pages bleibt letzterer ungenutzt).

## Funktionsweise

### Unterschied zum 4KB-Paging

Beim "normalen" Paging zeigt jeder der 1024 Einträge im [Page Directory](Paging "Paging") auf eine 4KB große [Page Table](Paging "Paging"), deren 1024 Einträge wiederrum einen 4 MB großen Bereich definieren. Somit sind insgesamt 4 MB Speicherplatz durch Page Tables belegt.

Wenn PSE aktiviert ist, dann wird Bit 7 (S-Bit) in den Einträgen des Page Directory gültig. Ist dieses Bit nicht gesetzt, dann zeigt der Eintrag auf eine Page Table mit 4KB-Pages (so wie beim "normalen" Paging), andernfalls zeigt der Eintrag direkt auf eine 4MB-Page. Falls man also nur 4MB-Pages verwendet (alle S-Bits sind gesetzt), bedeutet das, dass man keine Page Tables mehr benötigt, weil das Page Directory alle Pages direkt definiert.

### Aktivieren der Page Size Extension

- ein Page Directory mit 1024 Einträge anlegen
  - ist das S-Bit gesetzt, dann zeigt der Eintrag direkt auf eine 4MB-Page
  - ist das S-Bit nicht gesetzt, muss eine Page Table angelegt werden, auf die der Eintrag zeigt
- in das [Control Register](Control-Register "Control Register") cr3 die Adresse des Page Directory laden
- PSE aktivieren, indem Bit 4 im Control Register cr4 gesetzt wird
- Paging aktivieren, indem Bit 31 im Control Register cr0 gesetzt wird

## Siehe auch

- [Paging](Paging "Paging")

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/6930/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1999/index.html)

<!-- MediaWiki page 1999; revision 6930; parent 6927; 2010-01-18T11:04:27Z -->
