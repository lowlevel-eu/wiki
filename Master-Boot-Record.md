# Master Boot Record

Der MBR (Master Boot Record) ist der Erste Sector einer Festplatte

    LBA -> 0x00000000
    CHS -> Cilinder: 0, Head: 0, Sector: 1

## Aufgabe

Die Aufgabe des MBR ist es, die Partitionen zu definieren, den [Boot Record](https://github.com/lowlevel-eu/wiki/wiki/Bootsektor "Boot Record") einer bootbaren Pation zu laden und zu starten.

## Aufbau

|  |  |
| --------------- | ------------------------------------ |
| Offset |  |
| 0x0000-0x01BD | Code zum laden der einer Partition |
| 0x01BE-0x01FD | Paritions Tabelle |
| 0x01FE-0x01FF | Bootsignatur 0xAA55 |

## Partitions Tabelle

Die Partitions Tabelle besteht aus 4 Einträgen á 16Byte in folgendem Format:

|  |  |  |
| ------------ | ----- | --------------------------------------------------------------------------------- |
| **Offset** |  |  |
| 0x0 | DB | Bootflag<br>• 0x00 nicht bootbar<br>• 0x80 bootbare Partition<br> |
| 0x1 | DB | Kopf an dem die Partiton anfängt |
| 0x2 | DB | • Bit 0-5 -\> Anfangs Sector<br>• Bit 6-7 -\> Bit 8-9 des Anfangs-Zylinders<br> |
| 0x3 | DB | Bit 0-7 des Anfangs-Zylinders |
| 0x4 | DB | Gibt den Partitions Typ an |
| 0x5 | DB | Kopf an dem die Partition endet |
| 0x6 | DB | • Bit 0-5 -\> Anfangs Sector<br>• Bit 6-7 -\> Bit 8-9 des Anfangs-Zylinders<br> |
| 0x7 | DB | Bit 0-7 des Anfangs-Zylinders |
| 0x8 | DD | LBA(Logical Block Addressing) Nummer des Ersten Sektors |
| 0xC | DD | Länge der Partition in Sektoren |

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/1589/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1431/index.html)

<!-- MediaWiki page 1431; revision 1589; parent 1510; 2007-01-06T16:27:59Z -->
