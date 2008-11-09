# Treiber

Treiber sind unterhalb der [HAL](https://github.com/lowlevel-eu/wiki/wiki/Hardware-Abstraction-Layer "HAL"). Sie sollen Zugriff zu der Hardware halten. Sie werden bei ein Hybrid- und Mikrokernel geladen, während sie bei ein Monolithischen Kernel schon in Kernel enthalten sind.

## Treiber beim Mikrokernel

Hier ist es wichtig, den Artikel [Interprozesskommunikation](https://github.com/lowlevel-eu/wiki/wiki/Interprozesskommunikation "Interprozesskommunikation") zu lesen. Zudem sollte darauf aufbauend eine Treiberschnittstelle vorhaden sein.

## Makrokernel

Hier sind sie direkt im Kernel einkompiliert. Ist ein Treiber fehlerhaft, stürzt immer dann der ganze Kernel ab.

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/3504/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1669/index.html)

<!-- MediaWiki page 1669; revision 3504; parent 3014; 2008-11-09T13:00:53Z -->
