# LF OS/LFX

# Spezifikation des LFX Dateiformates

| Adresse | Wert | Beschreibung |
| ------------- | ------- | ------------------------------------------------------------------------------------------- |
| 0x00 - 0x02 | "LFX" | Magic number - Erkennungsmerkmal für LFX Dateien |
| 0x03 | 1 | Major Version - Versionsnummer |
| 0x04 | 0 | Minor Version - Versionsnummer |
| 0x05 | \- | Typ des Programms (0 = Programm, 1 = Treiber, 2 = Shared Library) |
| 0x06 | \- | Prozessorarchitektur (0 = 386, rest undefiniert) |
| 0x07 - 0x0F | \- | Reserviert - für spätere Verwendung |
| 0x10 - 0x13 | \- | Ladeadresse - wohin im Speicher? |
| 0x14 - 0x1F | \- | Reserviert - für spätere Verwendung |
| 0x20 - 0x3F | \- | Name des Programms - nullterminiert |
| 0x40 - 0x8F | \- | Beschreibung des Programms - nullterminiert |
| 0x90 | \- | Major Version des Programms |
| 0x91 | \- | Minor Version des Programms |
| 0x92 | \- | Buildnummer des Programms |
| 0x93 | \- | Revision des Programms |
| 0x94 | \- | Bei Treibern: Bussystem des unterstützen Gerätes (0 = PCI, 1 = USB, ...) sonst reserviert |
| 0x95 - 0x98 | \- | Bei Treibern: Einsprungpunktes der GetDeviceID(); Funktion sonst reserviert |
| 0x99 - 0xFF | \- | Reserviert |
| ab 0x100 | \- | Programm im Maschinencode |

------------------------------------------------------------------------

Das LFX Format ermöglicht es, Informationen zu einem Programm, wie etwa Name, Beschreibung und natürlich die Ladeadresse, in einer Datei abzuspeichern.

Das Betriebssystem hat schon vor Programmstart die Möglichkeit, einie Informationen über das Programm zu erhalten.

Beispielsweise steht an der Adresse 0x05 der Typ des Programms, damit kann zwischen normalen Programmen und Treibern unterschieden werden.

Der Header ist nur 256 Byte groß, also geht kaum Platz verloren.

------------------------------------------------------------------------

Auf meiner Internetseite <http://littlefox.web-fuxx.de> werde ich demnächst eine Beispielimplementation in C++ veröffentlichen, fertig ist sie schon.

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/8562/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2315/index.html)

<!-- MediaWiki page 2315; revision 8562; parent 0; 2010-10-09T10:32:08Z -->
