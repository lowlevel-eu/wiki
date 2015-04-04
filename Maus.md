# Maus

Die Maus ist das wichtigste Eingabegerät bei einer [GUI](https://github.com/lowlevel-eu/wiki/wiki/Graphical-User-Interface "GUI"). Populär wurden sie als Eingabegerät des Apple Macintosh. Ursprünglich wurden Mäuse über die [Serielle Schnittstelle](https://github.com/lowlevel-eu/wiki/wiki/Serielle-Schnittstelle "Serielle Schnittstelle") angebunden; IBM führte schließlich mit dem [PS/2-Maus](https://github.com/lowlevel-eu/wiki/wiki/PS-2-Maus "PS/2-Maus")-Anschluss eine neue Anschlusstechnik mit einem neuen Protokoll ein. Heutzutage werden Mäuse meist per [USB](https://github.com/lowlevel-eu/wiki/wiki/Universal-Serial-Bus "USB") mit dem Rechner verbunden.

## Serielle Schnittstelle

Diese Seite ist ein Artikel, welcher **mehr** haben könnte..  

Wenn du mehr darüber weißt oder recherchieren willst, bist **du** aufgerufen, dies zu tun. Wenn du dir in einer Sache nicht sicher bist, dann stell es auf die Diskussionsseite.

## PS/2

Siehe Artikel [PS/2-Maus](https://github.com/lowlevel-eu/wiki/wiki/PS-2-Maus "PS/2-Maus").

## USB

Mäuse (und Tastaturen) für USB werden von der Spezifikation "Device Class Definition for Human Interface Devices (HID)" definiert. Version 1.11 der Spezifikation ermöglicht zwar umfassende gerätespezifische Funktionen, definiert allerdings auch ein sog. "Boot Interface" für Mäuse und Tastaturen; ein festgelegtes Protokoll für die Kommunikation mit Mäusen und Tastaturen, damit bereits das BIOS mit diesen kommunizieren kann, ohne dass ein umfangreicher Treiber notwendig wäre.

Die Kommunikation mit der Maus läuft über den vom Gerät bereitgestellten Interrupt-Endpoint. Über diesen können Pakete von 3 oder mehr Bytes empfangen werden; die ersten drei Bytes sind dabei wie folgt standardisiert:

| Byte | Beschreibung |
| ------ | -------------------------------------------------------------------------------- |
| 0 | Button-Status. Bit 0: Linke Taste; Bit 1: Rechte Taste; Bit 2: Mittlere Taste. |
| 1 | X-Verschiebung (von links nach rechts) |
| 2 | Y-Verschiebung (von oben nach unten) |
| 3-N | Gerätespezifisch |

## Weblinks

- [http://www.usb.org/developers/hidpage/ (USB-HID-Spezifikation und dazugehörende Dokumente)](http://www.usb.org/developers/hidpage/)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/11265/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1670/index.html)

<!-- MediaWiki page 1670; revision 11265; parent 11198; 2015-04-04T11:45:09Z -->
