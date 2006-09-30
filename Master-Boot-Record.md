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

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/1507/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1431/index.html)

<!-- MediaWiki page 1431; revision 1507; parent 0; 2006-09-30T16:46:26Z -->
