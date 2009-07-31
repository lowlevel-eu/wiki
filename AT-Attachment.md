# AT Attachment

## Erkennen der angeschlossenen Geräte

Eine der größten Hürden zu Beginn beim Schreiben eines ATA-Treibers ist das Erkennen der angeschlossenen Geräte. Hierzu gibt es keinen von der Spezifikation vorgeschriebenen Weg. Viele Methoden funktionieren zwar in einigen Emulatoren aber auf echter Hardware nicht und umgekehrt.

Beim Schreiben des ATA-Treibers für týndur habe ich lange nach einer Methode gesucht, die überall funktioniert und lange Wartezeiten beim Erkennen der Geräte vermeidet. Mittlerweile glaube ich, eine passende Methode gefunden zu haben, die in Qemu und [VMWare](https://github.com/lowlevel-eu/wiki/wiki/VMware "VMWare") und auf sämtlichen meinen bisher getesteten Maschinen funktioniert (4 Rechner von P1 bis zum P4).

### HOB-Bit löschen

Im OSDev-Forum bin ich darauf gestoßen, dass man vor dem Suchen nach Geräten zuerst das HOB-Bit in den Kontrollregistern der beiden Geräte löschen sollte, da noch nicht klar ist, ob sie LBA48 unterstützen oder nicht. Ob es wirklich notwendig ist weiß ich nicht, aber schaden kann es ja nicht.

### Floating Bus

Angefangen wird mit einem kleinen Test auf eine Erscheinung, die als *floating bus* bezeichnet wird. Damit kann festgestellt werden, ob der Bus sicher leer ist. Das Ganze hängt damit zusammen, dass der ATA-Bus mit sogenannten Pullup-Widerständen auf einem hohen Pegel gehalten wird, wenn die einzelnen Leitungen nicht von den Geräten gegen Masse gezogen werden. Beim Auslesen der Register äußert sich das dann durch lauter gesetzte Bits. Am einfachsten lässt sich das durch das Auslesen des Statusregisters erledigen. Zuerst wählt man den Master aus, liest danach den Wert des Statusregisters ein und vergleicht ihn danach mit 0xFF (ist ein ungültiger Status-Wert).

### Responsive Device

Der nächste Schritt dient dazu, herauszufinden, ob auf dem Bus ein Gerät vorhanden ist, das auf Anfragen reagiert. Der Test kann einfach durchgeführt werden, indem man ein Gerät auswählt, danach beliebige Werte in die LBA-Register schreibt, und diese wieder ausliest. Wenn ein antwortendes Gerät vorhanden ist, kann man die gleichen Werte wieder einlesen, wenn das nicht der Fall ist, müssen auf dem Bus keine weiteren Prüfungen vorgenommen werden. Sicherheitshalber sollte hier zweimal geprüft werden, einmal mit Master und einmal mit Slave. Dies macht zwar eigentlich keinen Sinn, aber in VMWare reagiert der Master nicht (wie es in der Spezifikation vorgeschrieben ist), falls nur der Slave angesprochen wird, und soviel Zeit braucht das ganze ja nicht.

### IDENTIFY DEVICE - Kommando

Falls keine der vorherigen Prüfungen fehlgeschlagen ist, müsste jetzt mindestens ein Gerät am Bus vorhanden sein. Das wird jetzt sichergestellt und genauer ermittelt, welche Geräte wirklich vorhanden sind. Dies wird mit dem IDENTIFY DEVICE Befehl gemacht. Beim Senden dieses Befehls ist es sehr wichtig, dass man die ATA-Spezifikation genau befolgt, und sich an die dort erwähnten Protokolle hält. Wenn das korrekt gemacht wird, geht das Erkennen ohne ewig lange Timeouts und co. von statten. Falls das Identifizieren eines Gerätes fehlschlägt, heißt das noch nicht, dass kein Gerät vorhanden ist. Denn es könnte auch sein, dass es sich um ein Gerät mit PACKET Interface handelt. Diese Geräte lassen sich mit dem IDENTIFY PACKET DEVICE identifizieren.

## Register

| Beschreibung | 1\. Kanal | 2\. Kanal | 3\. Kanal | 4\. Kanal |
| ------------------------- | ----------- | ----------- | ----------- | ----------- |
| Datenregister | 0x1F0 | 0x170 | 0x1E8 | 0x168 |
| Fehlerregister | 0x1F1 | 0x171 | 0x1E9 | 0x169 |
| Sektoranzahl | 0x1F2 | 0x172 | 0x1EA | 0x16A |
| LBA niedrig | 0x1F3 | 0x173 | 0x1EB | 0x16B |
| LBA mittel | 0x1F4 | 0x174 | 0x1EC | 0x16C |
| LBA hoch | 0x1F5 | 0x175 | 0x1ED | 0x16D |
| Geräteauswahl | 0x1F6 | 0x176 | 0x1EE | 0x16E |
| Status/Kommandoregister | 0x1F7 | 0x177 | 0x1EF | 0x16F |
| Status2/Steuerregister | 0x3F6 | 0x376 | 0x3EE | 0x36E |

### Datenregister

Das Datenregister dient zur Übermittlung der Lese/Schreib-Words(!).

### Fehlerregister

### Sektoranzahl

### LBA niedrig

### LBA mittel

### LBA hoch

### Geräteauswahl

| 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| ----- | ----- | ----- | ----- | ----- | ------ | ------ | ----- |
| r | r | r | r | r | SRST | nIEN | 0 |

- r: reserviert
- SRST: Software Reset
- nIEN: ???
- 0: Immer 0

### Status/Kommandoregister

### Status2/Steuerregister

## Fehlerquellen

Hier ein paar Hinweise auf Fehler, die nicht sofort offensichtlich sind.

### Gerätesignaturen

In der ATA-Spezifikation wird beschrieben, unter welchen Umständen ein Gerät seine Signatur in die Register schreiben sollte. Doch hier ist Vorsicht geboten. Denn die Signatur wird von längst nicht allen Emulatoren und auch nicht von allen Geräten korrekt gesetzt.

### NIEN-Bit

Beim Testen auf einem älteren Gerät (Pentium), musste ich feststellen, dass das NIEN-Bit dort nicht wirkt. Trotz gesetztem NIEN-Bit hat der Controller frisch fröhlich IRQs losgeschickt. Hier sollte also sichergestellt werden, dass der IRQ verarbeitet wird, ohne dass etwas Unerwünschtes passiert.

## Weblinks

- [Working-Drafts der aktuellen Spezifikationen zu ATA(PI)](http://t13.org/Documents/UploadedDocuments/project/d1321r3-ATA-ATAPI-5.pdf)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/4934/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1522/index.html)

<!-- MediaWiki page 1522; revision 4934; parent 4775; 2009-07-31T19:05:24Z -->
