# BIOS Data Area

In der **BIOS Data Area** (Abkürzung: **BDA**) werden wichtige Informationen über Hardware und andere Systemkomponenten gespeichert.

## Aufbau der BIOS Data Area

Die BDA befindet sich im Segment 0x0040, d.h. an der physikalischen Adresse 0x0400. Die folgende Tabelle zeigt den Aufbau dieses Segments:

| Offset | Größe (Bytes) | Beschreibung |
| -------- | --------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| 0x00 | 2 | I/O-Port von [COM1](https://github.com/lowlevel-eu/wiki/wiki/Serielle-Schnittstelle "Serielle Schnittstelle") |
| 0x02 | 2 | I/O-Port von [COM2](https://github.com/lowlevel-eu/wiki/wiki/Serielle-Schnittstelle "Serielle Schnittstelle") |
| 0x04 | 2 | I/O-Port von [COM3](https://github.com/lowlevel-eu/wiki/wiki/Serielle-Schnittstelle "Serielle Schnittstelle") |
| 0x06 | 2 | I/O-Port von [COM4](https://github.com/lowlevel-eu/wiki/wiki/Serielle-Schnittstelle "Serielle Schnittstelle") |
| 0x08 | 2 | I/O-Port von LP1 |
| 0x0A | 2 | I/O-Port von LP2 |
| 0x0C | 2 | I/O-Port von LP3 |
| 0x0E | 2 | I/O-Port von LP4 oder<br>Segment der [EBDA](https://github.com/lowlevel-eu/wiki/wiki/Extended-BIOS-Data-Area "EBDA") (bei PS/2) |
| 0x10 | 2 | [Equipment word](#equipment-word) |
| 0x12 | 1 | Manufacturing test data |
| 0x13 | 2 | Speichergröße (in kB) |
| 0x15 | 2 | Manufacturing test data |
| 0x17 | 2 | [Tastatur-Status-Flags](#tastatur-status-flags) |
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

  

### Equipment word

| Bits | Beschreibung |
| ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| 15-14 | 00b = 1 Parallelport vorhanden<br>01b = 2 Parallelports vorhanden<br>03b = 3 Parallelports vorhanden |
| 13 | 01b = internes Modem vorhanden |
| 12 | 01b = Joystick vorhanden |
| 11-9 | Anzahl der vorhandenen [COM-Ports](https://github.com/lowlevel-eu/wiki/wiki/Serielle-Schnittstelle "Serielle Schnittstelle") 0-4 |
| 8 | [DMA](https://github.com/lowlevel-eu/wiki/wiki/Direct-Memory-Access "Direct Memory Access")-Controller vorhanden (PC-junior) |
| 7-6 | 00b = 1 Floppylaufwerk vorhanden<br>01b = 2 Floppylaufwerke vorhanden |
| 5-4 | 00b = EGA oder älter<br>01b = Farbe 40x25<br>10b = Farbe 80x25<br>11b = Monochrom 80x25 |
| 3 | Reserviert |
| 2 | Ob eine PS/2-Maus vorhanden ist |
| 1 | Ob ein [mathematischer Koprozessor](https://github.com/lowlevel-eu/wiki/wiki/Mathematischer-Koprozessor "Mathematischer Koprozessor") vorhanden ist |
| 0 | Ob ein Bootfloppy-Laufwerk vorhanden ist |

  

### Tastatur-Status-Flags

Hier werden die Tastatur-Flags gespeichert welche vom Interrupt 0x16 verwendet werden.  

| Bits | Beschreibung |
| ------ | --------------------------------------------------------- |
| 7 | 0 = Einfügen ausgeschaltet<br>1 = Einfügen angeschaltet |
| 6 | 0 = CapsLock aus<br>1 = CapsLock an |
| 5 | 0 = NumLock aus<br>1 = NumLock an |
| 4 | 0 = ScrollLock aus<br>1 = ScrollLock an |
| 3 | 0 = Alt nicht gedrückt<br>1 = Alt gedrückt |
| 2 | 0 = Strg nicht gedrückt<br>1 = Strg gedrückt |
| 1 | 0 = LShift nicht gedrückt<br>1 = LShift gedrückt |
| 0 | 0 = RShift nicht gedrückt<br>1 = RShift gedrückt |

  

## Weblinks

- <http://bioscentral.com/misc/bda.htm>
- <http://www.geocities.com/riskyfriends/x86/os/bios.html>

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/2443/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1564/index.html)

<!-- MediaWiki page 1564; revision 2443; parent 2442; 2007-12-20T11:20:50Z -->
