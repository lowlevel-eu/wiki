# Exokernel

Der Exokernel ist eine Unterart des [Mikrokernels](https://github.com/lowlevel-eu/wiki/wiki/Kernel#mikrokernel "Mikrokernel"). Bestimmende Eigenschaft dieser [Kernelart](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel") ist die optionale [HAL](https://github.com/lowlevel-eu/wiki/wiki/Hardware-Abstraction-Layer "HAL"), d. h. der Anwendungsprogrammierer kann entscheiden, ob er direkt auf die [Hardware](https://lowlevel-eu.github.io/wiki/pages/1953/index.html "Hardware") zugreift oder diese abstrahiert.

## Motivation für den Exokernel

Eine [HAL](https://github.com/lowlevel-eu/wiki/wiki/Hardware-Abstraction-Layer "HAL") kann unmöglich alle Anforderung einer Anwendung erfüllen. Trotzdem wird bei jedem traditionellen [Betriebssystem](https://github.com/lowlevel-eu/wiki/wiki/Betriebssystem "Betriebssystem") versucht, alle Anforderungen zu erfüllen. Die [HAL](https://github.com/lowlevel-eu/wiki/wiki/Hardware-Abstraction-Layer "HAL") wird dadurch aufgebläht und unperfom. Die Idee des Exokernel ist, dass die Abstraktion der [Hardware](https://lowlevel-eu.github.io/wiki/pages/1953/index.html "Hardware") nicht auf [Kernelebene](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel"), sondern auf Anwendungsebene passiert.

## Besonderheiten eines Exokernels

Wie erwähnt, ist die HAL nicht zwingend, sondern optional. Ein Programm kann entscheiden, ob sie denn Hardwarezugriff braucht. Bei den meisten Programmen wird dies nicht nötig sein. Bei rechenintisiven oder systemveränderen Programmen wird dies jedoch nötig. Folgendes Diagramm veranschaulich dies. ![exokernel.png](http://be59.be.funpic.de/Lowlevel/exokernel.png)

## Vorteile

- Bessere Flexibilität: Ein Entwickler kann seine Anwendung besser optimieren.

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/4169/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1678/index.html)

<!-- MediaWiki page 1678; revision 4169; parent 4166; 2009-03-21T11:30:05Z -->
