# Sonstige Informationen

Ich weiß momentan nicht so ganz wo ich es einordnen soll, aber bei [BIOS Data Area](BIOS-Data-Area "BIOS Data Area") hat es meines Erachtens nichts verloren. Deswegen hab ich es mal einfach hier hineinkopiert.--[Bluecode](https://lowlevel-eu.github.io/wiki/pages/1489/index.html "Benutzer:Bluecode") 19:15, 26. Nov. 2007 (CET)

## BIOS Data Area 2

Die 2. BIOS Data Area befindet sich im Sektor 0xFFFF also an der Adresse 0xFFFF0.

| Offset | Größe (Bytes) | Beschreibung |
| -------- | --------------- | -------------------------------------------- |
| 0x00 | 5 | Farjump-Instruktion zum Ausführen des POST |
| 0x05 | 8 | ROM-BIOS-Datum als String |
| 0x0C | 2 | Unbenutzt |
| 0x0E | 1 | IBM-Computer-Typ-Code |

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/6100/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1573/index.html)

<!-- MediaWiki page 1573; revision 6100; parent 4871; 2009-10-19T12:21:43Z -->
