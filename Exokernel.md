# Exokernel

Der Exokernel ist eine Unterart des [Mikrokernel](https://github.com/lowlevel-eu/wiki/wiki/Kernel#mikrokernel "Mikrokernel"). Bestimmene Eigenschaft dieser [Kernelart](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel") ist die optimale [HAL](https://github.com/lowlevel-eu/wiki/wiki/Hardware-Abstraction-Layer "HAL"), d. h. der Anwendungsprogrammierer kann entscheiden, ob er direkt auf die Hardware zugreift oder diese abstratiert. == Motivation für ein Exokernel Eine HAL kann unmöglich alle Anforderung einer Anwendung erfüllen. Trotzdem wird bei jeden trafitionelen Betriebsystem versucht, alle Anforderungen zu erfüllen. Die HAL wird dadurch aufgebläht und unperfom. Die Idee des Exokernel ist, dass die Abstraktion der HArdware nicht auf Kernelebene, sondern Anwendungsebene passiert.

## Vorteile

- Bessere Flexibilität: Ein Entwickler kann seine Anwendung besser optimieren.

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/3241/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1678/index.html)

<!-- MediaWiki page 1678; revision 3241; parent 3240; 2008-08-25T17:57:28Z -->
