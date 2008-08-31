# Exokernel

Der Exokernel ist eine Unterart des [Mikrokernels](https://github.com/lowlevel-eu/wiki/wiki/Kernel#mikrokernel "Mikrokernel"). Bestimmende Eigenschaft dieser [Kernelart](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel") ist die optionale [HAL](https://github.com/lowlevel-eu/wiki/wiki/Hardware-Abstraction-Layer "HAL"), d. h. der Anwendungsprogrammierer kann entscheiden, ob er direkt auf die Hardware zugreift oder diese abstrahiert.

## Motivation für den Exokernel

Eine HAL kann unmöglich alle Anforderung einer Anwendung erfüllen. Trotzdem wird bei jedem traeitionellen Betriebsystem versucht, alle Anforderungen zu erfüllen. Die HAL wird dadurch aufgebläht und unperfom. Die Idee des Exokernel ist, dass die Abstraktion der Hardware nicht auf Kernelebene, sondern auf Anwendungsebene passiert.

## Vorteile

- Bessere Flexibilität: Ein Entwickler kann seine Anwendung besser optimieren.

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/3270/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1678/index.html)

<!-- MediaWiki page 1678; revision 3270; parent 3242; 2008-08-31T12:33:56Z -->
