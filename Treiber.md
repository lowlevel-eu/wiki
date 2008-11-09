# Treiber

Treiber sind unterhalb der [HAL](https://github.com/lowlevel-eu/wiki/wiki/Hardware-Abstraction-Layer "HAL"). Sie sollen Zugriff zu der Hardware halten. Sie werden bei ein Hybrid- und Mikrokernel geladen, während sie bei ein Monolithischen Kernel schon in [Kernel](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel") enthalten sind.

## Treiber beim Mikrokernel

Beim Mikrokernel sind jegliche Treiber im User-Mode ausgelagert. Diese können abstürzen, ohne den Kernel mitzureißen. Hier ist es wichtig, den Artikel [Interprozesskommunikation](https://github.com/lowlevel-eu/wiki/wiki/Interprozesskommunikation "Interprozesskommunikation") zu lesen. Zudem sollte darauf aufbauend eine Treiberschnittstelle vorhaden sein. Als (vereinfachtes) Diagramm würde ein Betriebsystem mit [Mikrokernel](https://github.com/lowlevel-eu/wiki/wiki/Kernel#mikrokernel "Mikrokernel") so aussehen. **Achtung, kein [Exokernel](https://github.com/lowlevel-eu/wiki/wiki/Kernel#exokernel "Exokernel")**  
![Diagramm.png](http://be59.be.funpic.de/Lowlevel/Diagramm.png)

## Makrokernel

Hier sind sie direkt im [Kernel](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel") einkompiliert. Ist ein Treiber fehlerhaft, stürzt immer dann der ganze [Kernel](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel") ab. Als (vereinfachtes) Diagramm würde ein Betriebsystem mit Makrokernel so aussehen.  
![Diagramm2.png](http://be59.be.funpic.de/Lowlevel/Diagramm2.png)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/3507/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1669/index.html)

<!-- MediaWiki page 1669; revision 3507; parent 3506; 2008-11-09T13:43:12Z -->
