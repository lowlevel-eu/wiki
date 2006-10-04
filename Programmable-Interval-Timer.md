# Programmable Interval Timer

Der Programmable Interval Timer, manchmal auch falsch als Programmable Interrupt Timer bezeichnet, erzeugt ein Signal mit der Frequenz von ~1193181Hz. Diese Signal zählet 3 Register herunter, welche jedes Mal eine Aktion auslösen sobald sie null erreichen.

Zählregister 1: das auslösend des IRQ0 (Dient dem Betriebsystem zur Zeitmessung) Zählregister 2: dient in alten XT-PCs, zusammen mit dem DMA-Kanal 0, der Speicherauffrischung Zählregister 3: Signal für den PC-Lautsprecher (also die Tonfrequenz)

Die Frequenz für das Auslösen errechnet sich aus der Grundfrequenz (1193181Hz) und dem Teiler (word). Wobei der Teilerwert 0 für die Zahl 65536 steht. Also 1193181/0 würde wie 1193181/65536 gerechnet werden.

1193181 Hz / Teiler = Frequenz

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/1513/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1432/index.html)

<!-- MediaWiki page 1432; revision 1513; parent 0; 2006-10-04T15:55:57Z -->
