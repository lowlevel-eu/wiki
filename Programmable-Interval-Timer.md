# Programmable Interval Timer

Der **Programmable Interval Timer** (= **PIT**) erzeugt ein Signal mit der Frequenz von 1193180Hz. Dieses Signal zählt 3 Register herunter, welche jeweils eine Aktion auslösen sobald sie 0 erreichen:

- Zählregister 1: das auslösen des [IRQ](https://github.com/lowlevel-eu/wiki/wiki/Programmable-Interrupt-Controller#irq-tabelle "IRQ") 0 (Dient Betriebssystemen zur Zeitmessung und wird oft für Multitasking genutzt)  
- Zählregister 2: dient in alten XT-PCs, zusammen mit dem DMA-Kanal 0, der Speicherauffrischung  
- Zählregister 3: Signal für den [Systemlautsprecher](https://github.com/lowlevel-eu/wiki/wiki/Systemlautsprecher "Systemlautsprecher") (also die Tonfrequenz)  

Die Frequenz für das Auslösen errechnet sich aus der Grundfrequenz und dem Wert im Register der heruntergezählt wird (Teiler).  

1193180 Hz / Teiler = Auslöse-Frequenz  

Der Teiler ist ein 16-Bit groß, kann also Werte von 0 bis 65535 aufnehmen. Der Wert 0 wird jedoch als 65536 interpretiert, weshalb sich ein möglicher Teilerwert von 1 bis 65536 ergibt.  

Der Minimal- und Maximalwert des Teilers bestimmt die möglichen Auslöse-Frequenzen:  

Max: 1193180 Hz / 1 = 1193180 Hz  
Min: 1193180 Hz / 65536 = ~18.206 Hz  

## Links

- [Intel 8253 Chip auf Wikipedia](http://en.wikipedia.org/wiki/Intel_8253)  
- [Intel 8254 Chip auf Wikipedia](http://en.wikipedia.org/wiki/Intel_8254)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/2737/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1432/index.html)

<!-- MediaWiki page 1432; revision 2737; parent 2470; 2008-03-22T17:20:36Z -->
