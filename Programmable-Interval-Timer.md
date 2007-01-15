# Programmable Interval Timer

Der Programmable Interval Timer, manchmal auch falsch als Programmable Interrupt Timer bezeichnet, erzeugt ein Signal mit der Frequenz von 1193180Hz. Dieses Signal zählt 3 Register herunter, welche jeweils eine Aktion auslösen sobald sie null erreichen.  

Zählregister 1: das auslösend des IRQ0 (Dient Betriebsystemen zur Zeitmessung und wird oft für Multitasking genutzt)  
Zählregister 2: dient in alten XT-PCs, zusammen mit dem DMA-Kanal 0, der Speicherauffrischung  
Zählregister 3: Signal für den PC-Lautsprecher (also die Tonfrequenz)  

Die Frequenz für das Auslösen errechnet sich aus der Grundfrequenz und dem Wert im Register der heruntergezählt wird (Teiler).  

1193180 Hz / Teiler = Auslöse-Frequenz  

Der Teiler ist eine word groß. Kann also Werte von 0 bis 65535 aufnehmen. Der Wert 0 wird jedoch als 65536 angesehen, weshalb sich ein möglcher Teilerwert von 1 bis 65536 ergibt.  

Der Minimal- und Maximalwert des Teiler bestimmt die möglichen Auslöse-Frequentzen:  

Max: 1193180 Hz / 1 = 1193180 Hz  
Min: 1193180 Hz / 65536 = ~18.206 Hz  

  
**Links**

[Intel 8253 Chip auf Wikipedia](http://en.wikipedia.org/wiki/Intel_8253)  
[Intel 8254 Chip auf Wikipedia](http://en.wikipedia.org/wiki/Intel_8254)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/1677/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1432/index.html)

<!-- MediaWiki page 1432; revision 1677; parent 1599; 2007-01-15T22:47:51Z -->
