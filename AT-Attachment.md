# AT Attachment

## Erkennen der angeschlossenen Geräte

Eine der größten Hürden zu Beginn beim Schreiben eines ATA-Treibers ist das Erkennen der angeschlossenen Geräte. Hierzu gibt es keinen von der Spezifikation vorgeschriebenen Weg. Viele Methoden funktionieren zwar in einigen Emulatoren aber auf echter Hardware nicht und umgekehrt.

Beim Schreiben des ATA-Treibers für LOST habe ich lange nach einer Methode gesucht, die überall funktioniert und lange Wartezeiten beim Erkennen der Geräte vermeidet. Mittlerweile glaube ich, eine passende Methode gefunden zu haben, die in qemu und vmware, und auf sämtlichen meinen bisher getesteten Maschinen funktioniert (4 Rechner von P1 bis zum P4).

### HOB-Bit löschen

Im OSdev-Forum bin ich darauf gestossen, dass man vor dem Suchen nach Geräten zuerst das HOB-Bit in den Kontrollregistern der beiden Geräte löschen sollte, da noch nicht klar ist, ob sie LBA48 unterstützen oder nicht. Ob es wirklich notwendig ist, weiß ich nicht, aber schaden kann es ja nicht.

### Floating Bus

Angefangen wird mit einem kleinen Test auf eine Erscheinung, die als "floating bus" bezeichnet wird. Damit kann festgestellt werden, ob der Bus sicher leer ist. Das Ganze hängt damit zusammen, dass der ATA-Bus, mit sogenannten Pullup-Widerständen auf einem Hohen Pegel gehalten wird, wenn die einzelnen Leitungen nicht von den Geräten gegen Masse gezogen werden. Beim auslesen der Register äußert sich das dann durch lauter gesetzte Bits. Am einfachsten lässt sich das durch das auslesen des Stausregisters erledigen. Zuerst wählt man den Master aus, liest danach den Wert des Statusregisters ein und vergleicht ihn danach mit 0xFF (ist ein ungültiger Status-Wert).

### Responsive Device

Der nächste Schritt dient dazu, herauszufinden ob auf dem Bus ein Gerät vorhanden ist, dass auf Anfragen reagiert. Der Test kann einfach durchgeführt werden, indem man ein Gerät auswählt, danach beliebige Werte in die LBA-Register schreibt, und diese wieder ausliest. Wenn ein antwortendes Gerät vorhanden ist, kann man die gleichen Werte wieder einlesen, wenn das nicht der Fall ist, müssen auf dem Bus keine weiteren Prüfungen vorgenommen werden. Sicherheitshalber sollte hier 2x geprüft werden, einmal mit Master und einmal mit Slave. Dies macht zwar eigentlich keinen Sinn, aber in vmware reagiert der Master nicht (wie es in der Spezifikation vorgeschrieben ist), falls nur der Slave angesprochen wird, und soviel Zeit braucht das ganze ja nicht.

### IDENTIFY DEVICE - Kommando

Falls keine der vorherigen Prüfungen fehlgeschlagen ist, müsste jetzt mindestens ein Gerät am Bus vorhanden sein. Das wird jetzt sichergestellt und genauer ermittelt, welche Geräte wirklich vorhanden sind. Dies wird mit dem IDENTIFY DEVICE Befehl gemacht. Beim Senden dieses Befehls ist es sehr wichtig, dass man die ATA-Spezifikation genau befolgt, und sich an die dort erwähnten Protokolle hält. Wenn das korrekt gemacht wird, geht das Erkennen ohne ewig lange Timeouts und co. von statten. Falls das Identifizieren eines Gerätes fehlschlägt, heißt das noch nicht, dass kein Gerät vorhanden ist. Denn es könnte auch sein, dass es sich um ein Gerät mit PACKET Interface handelt. Diese Geräte lassen sich mit dem IDENTIFY PACKET DEVICE identifizieren.

  

## Fehlerquellen

Hier ein paar Hinweise auf Fehler die nicht sofort offensichtlich sind.

### Gerätesignaturen

In der ATA-Spezifikation wird beschrieben, unter welchen Umständen ein Gerät seine Signatur in die Register schreiben sollte. Doch hier ist Vorsicht geboten. Denn die Signatur wird von längst nicht allen Emulatoren und auch nicht von allen Geräten korrekt gesetzt.

### NIEN-Bit

Beim Testen auf einem älteren Gerät (Pentium), musste ich feststellen, dass das NIEN-Bit dort nicht wirkt. Trotz gesetztem NIEN-Bit hat der Controller frisch fröhlich IRQs losgeschickt. Hier sollte also sichergestellt werden, dass der IRQ verarbeitet wird, ohne dass etwas Unerwünschtes passiert.

## Spezifikationen

Working-Drafts der aktuellen Spezifikationen zu ATA(PI) können hier bezogen werden: [Technical Committee T13](http://www.t13.org/)

[Direkt-Link](http://t13.org/Documents/UploadedDocuments/project/d1321r3-ATA-ATAPI-5.pdf)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/3474/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1522/index.html)

<!-- MediaWiki page 1522; revision 3474; parent 3473; 2008-11-05T13:56:36Z -->
