# Treiber

Treiber sind unterhalb der [HAL](https://github.com/lowlevel-eu/wiki/wiki/Hardware-Abstraction-Layer "HAL"). Sie sollen Zugriff zu der Hardware halten. Sie werden bei ein Hybrid- und Mikrokernel geladen, während sie bei ein Monolithischen Kernel schon in Kernel enthalten sind.

## Treiber beim Mikrokernel

Hier ist es wichtig, den Artikel [Interprozesskommunikation](https://github.com/lowlevel-eu/wiki/wiki/Interprozesskommunikation "Interprozesskommunikation") zu lesen. Zudem sollte darauf aufbauend eine Treiberschnittstelle vorhaden sein. Als (vereinfachtes) Diagramm würde ein Betriebsystem mit Mikrokernel so aussehen. **Achtung, kein Exokernel**  
![Diagramm.png](http://be59.be.funpic.de/Lowlevel/Diagramm.png)

## Makrokernel

Hier sind sie direkt im Kernel einkompiliert. Ist ein Treiber fehlerhaft, stürzt immer dann der ganze Kernel ab. Als (vereinfachtes) Diagramm würde ein Betriebsystem mit Makrokernel so aussehen.  
![Diagramm2.png](http://be59.be.funpic.de/Lowlevel/Diagramm2.png)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/3505/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1669/index.html)

<!-- MediaWiki page 1669; revision 3505; parent 3504; 2008-11-09T13:25:56Z -->
