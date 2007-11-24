# BIOS Data Area

In der BIOS Data Area werden wichtige Informationen über Hardware und andere Systemkomponenten gespeichert.

## BIOS Data Area 1

Der erste BIOS-Speicher beginnt im Segment 0x0040, also ab der Adresse 0x0400.

| Offset | Größe (Bytes) | Beschreibung |
| -------- | --------------- | ------------------------------------------ |
| 0x00 | 2 | IO-Port von COM1 |
| 0x02 | 2 | IO-Port von COM2 |
| 0x04 | 2 | IO-Port von COM3 |
| 0x06 | 2 | IO-Port von COM4 |
| 0x08 | 2 | IO-Port von LP1 |
| 0x0A | 2 | IO-Port von LP2 |
| 0x0C | 2 | IO-Port von LP3 |
| 0x0E | 2 | IO-Port von LP4 |
| 0x10 | 2 | Equipment word |
| 0x12 | 1 | Manufacturing test data |
| 0x13 | 2 | Speichergröße (in kB) |
| 0x15 | 2 | Manufacturing test data |
| 0x17 | 2 | Keyboard-Status-Flag |
| 0x19 | 1 | Alt+Numpad-Data |
| 0x1A | 2 | Keyboard buffer head |
| 0x1C | 2 | Keyboard buffer tail |
| 0x1E | 32 | Keyboard buffer |
| 0x3E | 11 | Disk-Kontroller-Informationen |
| 0x49 | 30 | Grafik-Adapter-Informationen |
| 0x67 | 5 | Unbekannt |
| 0x6C | 4 | Zähler |
| 0x70 | 1 | Zähler 24h Überlauf |
| 0x71 | 1 | Keyboard-Control-Flag |
| 0x72 | 2 | Soft-Reset-Flag |
| 0x74 | 4 | Disk-Kontroller-Informationen |
| 0x78 | 4 | LP-Timout-Werte |
| 0x7C | 4 | COM-Timout-Werte |
| 0x80 | 2 | Start des PS/2-Keyboard-Buffers |
| 0x82 | 2 | Ende des PS/2-Keyboard-Buffers |
| 0x84 | 7 | Grafik-Controller-Informationen |
| 0x8B | 13 | Disk-Controller-Informationen |
| 0x96 | 2 | Keyboard-Status-Flag |
| 0x98 | 4 | Zeiger auf Benutzer-Flag |
| 0x9C | 4 | Benutzer-Warte-Zähler |
| 0xA0 | 1 | Benutzer-Warte-Flag |
| 0xA1 | 7 | Reseviert für Netzwerk-Adapter |
| 0xA8 | 4 | Grafik-Adapter-Informationen |
| 0xAC | 68 | Reserviert |
| 0xF0 | 16 | Inter-Application-Kommunikations-Bereich |

## BIOS Data Area 2

Die 2. BIOS Data Area befindet sich im Sektor 0xFFFF also an der Adresse 0xFFFF0.

| Offset | Größe (Bytes) | Beschreibung |
| -------- | --------------- | -------------------------------------------- |
| 0x00 | 5 | Farjump-Instruktion zum Ausführen des POST |
| 0x05 | 8 | ROM-BIOS-Datum als String |
| 0x0C | 2 | Unbenutzt |
| 0x0E | 1 | IBM-Computer-Typ-Code |

## Weblinks

- <http://www.geocities.com/riskyfriends/x86/os/bios.html>

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/2260/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1564/index.html)

<!-- MediaWiki page 1564; revision 2260; parent 0; 2007-11-24T16:07:41Z -->
