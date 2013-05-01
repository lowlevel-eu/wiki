# BIOS Data Area

In der **BIOS Data Area** (**BDA**) speichert das [BIOS](https://github.com/lowlevel-eu/wiki/wiki/Basic-Input-Output-System "BIOS") Informationen über Hardware und andere Systemkomponenten.

  

## Aufbau der BIOS Data Area

Die BDA befindet sich im Segment 0x0040, d.h. an der physikalischen Adresse 0x0400. Die für ein im [Protected Mode](https://github.com/lowlevel-eu/wiki/wiki/Protected-Mode "Protected Mode") bzw. [Long Mode](https://github.com/lowlevel-eu/wiki/wiki/Long-Mode "Long Mode") laufendes Betriebssystem interessanten Teile sind fett hervorgehoben, um Anfängern unnötige Arbeit zu ersparen. Alle anderen Informationen sind fehlerbehaftet, veraltet oder können anderweitig sinnvoller erfasst werden. Die folgende Tabelle zeigt den Aufbau dieses Segments:

  

| Offset | Größe (Bytes) | Beschreibung |
| -------- | --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0x00 | 2 | **Basisadresse des I/O-Ports von [COM1](https://github.com/lowlevel-eu/wiki/wiki/Serielle-Schnittstelle "Serielle Schnittstelle")** |
| 0x02 | 2 | **Basisadresse des I/O-Ports von COM2** |
| 0x04 | 2 | **Basisadresse des I/O-Ports von COM3** |
| 0x06 | 2 | **Basisadresse des I/O-Ports von COM4** |
| 0x08 | 2 | Basisadresse des I/O-Ports von [LPT1](https://github.com/lowlevel-eu/wiki/wiki/Parallele-Schnittstelle "Parallele Schnittstelle") |
| 0x0A | 2 | Basisadresse des I/O-Ports von LPT2 |
| 0x0C | 2 | Basisadresse des I/O-Ports von LPT3 |
| 0x0E | 2 | Basisadresse des I/O-Ports von LPT4 oder<br>**Segment der [EBDA](https://github.com/lowlevel-eu/wiki/wiki/Extended-BIOS-Data-Area "EBDA") (bei PS/2)** |
| 0x10 | 2 | **[Equipment Word](#equipment-word)** |
| 0x12 | 1 | POST Status |
| 0x13 | 2 | Größe des konventionellen Speichers (in kB) |
| 0x15 | 2 | POST System Flag |
| 0x17 | 2 | [Tastatur-Status-Flags](#tastatur-status-flags) |
| 0x19 | 1 | Alt+Numpad-Data |
| 0x1A | 2 | Zeiger auf nächsten Buchstaben im Tastatur-Ringpuffer |
| 0x1C | 2 | Zeiger auf letzten Buchstaben im Tastatur-Ringpuffer |
| 0x1E | 32 | Tastatur-Ringpuffer |
| 0x3E | 11 | [Disk-Kontroller-Informationen](#disk-kontroller-informationen) |
| 0x49 | 30 | [Grafik-Adapter-Informationen](#grafik-adapter-informationen) |
| 0x67 | 4 | Sprungadresse (Far Pointer) nach einem CPU-Reset (prä-AT: inkl. 0x6B diverse Informationen zum Kassettenlaufwerk) |
| 0x6B | 1 | In AT und neuer ungenutzt. Siehe 0x67. |
| 0x6C | 4 | Zähler für Interrupt 0x1A |
| 0x70 | 1 | Zähler 24h Überlauf |
| 0x71 | 1 | Keyboard-Control-Break-Flag |
| 0x72 | 2 | Soft-Reset-Flag |
| 0x74 | 4 | Disk-Kontroller-Informationen |
| 0x78 | 4 | LPT-Timeout-Werte |
| 0x7C | 4 | COM-Timeout-Werte |
| 0x80 | 2 | Start des PS/2-Keyboard-Buffers |
| 0x82 | 2 | Ende des PS/2-Keyboard-Buffers |
| 0x84 | 7 | Grafik-Controller-Informationen |
| 0x8B | 11 | Disk-Controller-Informationen |
| 0x96 | 2 | Keyboard-Status-Flag |
| 0x98 | 4 | Zeiger auf Benutzer-Flag |
| 0x9C | 4 | Benutzer-Warte-Zähler |
| 0xA0 | 1 | Benutzer-Warte-Flag |
| 0xA1 | 7 | Reseviert für Netzwerk-Adapter |
| 0xA8 | 4 | Grafik-Adapter-Informationen |
| 0xAC | 68 | Reserviert |
| 0xF0 | 16 | Inter-Application-Kommunikations-Bereich |

  

### Equipment Word

| Bits | Beschreibung |
| ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| 15-14 | Anzahl der vorhandenen LPT-Ports |
| 13 | 01b = internes Modem vorhanden |
| 12 | 01b = Joystick vorhanden |
| 11-9 | **Anzahl der vorhandenen [COM-Ports](https://github.com/lowlevel-eu/wiki/wiki/Serielle-Schnittstelle "Serielle Schnittstelle") 0-4** |
| 8 | [DMA](https://github.com/lowlevel-eu/wiki/wiki/Direct-Memory-Access "Direct Memory Access")-Controller vorhanden (PC-junior) |
| 7-6 | 00b = 1 Floppylaufwerk vorhanden<br>01b = 2 Floppylaufwerke vorhanden |
| 5-4 | **00b = EGA oder älter<br>01b = Farbe 40x25<br>10b = Farbe 80x25<br>11b = Monochrom 80x25** |
| 3 | Reserviert |
| 2 | Ob eine PS/2-Maus vorhanden ist |
| 1 | Ob ein [mathematischer Koprozessor](https://github.com/lowlevel-eu/wiki/wiki/Mathematischer-Koprozessor "Mathematischer Koprozessor") vorhanden ist |
| 0 | Ob ein Bootfloppy-Laufwerk vorhanden ist |

  

### Tastatur-Status-Flags

Hier werden die Tastatur-Flags gespeichert welche vom Interrupt 0x16 verwendet werden.  
Byte 1 (0x17):

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

  

Byte 2 (0x18):

| Bits | Beschreibung |
| ------ | -------------------------------------------------------------- |
| 7 | 0 = Einfügen nicht gedrückt<br>1 = Einfügen gedrückt |
| 6 | 0 = CapsLock nicht gedrückt<br>1 = CapsLock gedrückt |
| 5 | 0 = NumLock nicht gedrückt<br>1 = NumLock gedrückt |
| 4 | 0 = ScrollLock nicht gedrückt<br>1 = ScrollLock gedrückt |
| 3 | 0 = Pause-Taste inaktiv<br>1 = Pause-Taste aktiv |
| 2 | 0 = SysReg-Key (?) nicht gedrückt<br>1 = SysReg-Key gedrückt |
| 1 | 0 = Linkes Alt nicht gedrückt<br>1 = Linkes Alt gedrückt |
| 0 | 0 = Rechtes Alt nicht gedrückt<br>1 = Rechtes Alt gedrückt |

  

### Disk-Kontroller-Informationen

Byte 1 (0x3E): Floppy-Kalibrations-Status

| Bits | Beschreibung |
| ------ | ---------------------------------------------- |
| 7-4 | Reserviert |
| 3 | Ob Floppy-Laufwerk 4 kalibriert ist (PC, XT) |
| 2 | Ob Floppy-Laufwerk 3 kalibriert ist (PC, XT) |
| 1 | Ob Floppy-Laufwerk 2 kalibriert ist |
| 0 | Ob Floppy-Laufwerk 1 kalibriert ist |

  
Byte 2 (0x3F): Floppy-Motor-Status

| Bits | Beschreibung |
| ------ | ------------------------------------------------------------------------------------------------ |
| 7 | 0b = Read- oder Verify-Operation<br>1b Write- oder Format-Operation |
| 6 | Unbenutzt |
| 5-4 | 00b = Laufwerk 1<br>01b = Laufwerk 2<br>10b = Laufwerk 3 (PC, XT)<br>11b = Laufwerk 4 (PC, XT) |
| 3 | Ob der Motor des Laufwerks 1 eingeschaltet ist |
| 2 | Ob der Motor des Laufwerks 2 eingeschaltet ist |
| 1 | Ob der Motor des Laufwerks 3 eingeschaltet ist |
| 0 | Ob der Motor des Laufwerks 4 eingeschaltet ist |

  
Byte 3 (0x40): Floppy-Motor-Timeout

  
Byte 4 (0x41): Floppy-Laufwerk-Status

| Bit | Beschreibung |
| ----- | ------------------------------------------- |
| 7 | Ob Laufwerk bereit ist |
| 6 | Ob ein Seek-Fehler aufgetreten ist |
| 5 | Ob Floppy-Controller-Test erfolgreich war |
| 4-0 | Error-Code |

Error-Codes

| Binär | Hexadezimal | Beschreibung |
| -------- | ------------- | ------------------------------ |
| 00000b | 0x00 | Kein Fehler |
| 00001b | 0x01 | Ungültige Funktion |
| 00010b | 0x02 | Adresszeichen nicht gefunden |
| 00011b | 0x03 | Schreibschutzfehler |
| 00100b | 0x04 | Sektor nicht gefunden |
| 00110b | 0x06 | Disketten-Changelink aktiv |
| 01000b | 0x08 | DMA-Überlauf |
| 01001b | 0x09 | DMA-Boundary-Fehler |
| 01100b | 0x0C | Unbekannter Medientyp |
| 10000b | 0x10 | CRC-Fehler während Lesen |

  

Byte 5 (0x42): Festplatten- und Floppystatus

| Bits | Beschreibung |
| ------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 7-6 | Interrupt-Code<br>00b = Befehl normal abgeschlossen<br>01b = Befehl unnormal beendet<br>10b = Unnormales Beenden, Readline aktiv oder Diskette verändert<br>11b = Seek-Befehl nicht abgeschlossen |
| 5 | Ob Seek abgeschlossen wurde |
| 4 | Drive-Fault |
| 3 | Ob das Laufwerk bereit ist |
| 2 | Kopf-Status |
| 1-0 | 00b = Laufwerk 1<br>01b = Laufwerk 2<br>10b = Laufwerk 3<br>11b = Laufwerk 4 |

  

Byte 6 (0x43): Floppy Statusregister 1

| Bits | Beschreibung |
| ------ | ------------------------------------------------------------------ |
| 7 | Versuchter Zugriff jenseits des letzten Zylinders |
| 6 | Unbenutzt |
| 5 | CRC-Fehler während Lesen |
| 4 | DMA-Überlauf |
| 3 | Unbenutzt |
| 2 | Sektor nicht gefunden oder lesen der Disketten-ID fehlgeschlagen |
| 1 | Medium schreibgeschützt |
| 0 | fehlendes Adresszeichen |

  

Byte 7 (0x44): Floppy Statusregister 2

| Bits | Beschreibung |
| ------ | -------------------------------------------- |
| 7 | Unbenutzt |
| 6 | gelöschtes Daten-Adresszeichen |
| 5 | CRC-Fehler festgestellt |
| 4 | Falsche Zylinder |
| 3 | Gleichheitsbedingungen während Verify |
| 2 | Sektor nicht gefunden während Verify |
| 1 | Ungültiger Zylinder |
| 0 | Adresszeichen nicht gefunden während Lesen |

  

Byte 8 (0x45): Floppy Zylindernummer

  

Byte 9 (0x46): Floppy Kopfnummer

  

Byte 10 (0x47): Floppy Sektornummer

  

Byte 11 (0x48): Anzahl geschriebener Bytes

  

### Grafik-Adapter-Informationen

| Offset | Größe (Bytes) | Beschreibung |
| -------- | --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0x49 | 1 | Aktueller Videomodus ([\[1\]](http://www.ctyme.com/intr/rb-0069.htm#table10)) |
| 0x4A | 2 | Anzahl Spalten |
| 0x4C | 2 | Größe einer Bildschirmseite im [Regenerate Buffer](https://github.com/lowlevel-eu/wiki/wiki/Color-Graphics-Adapter#regen-buffer "Color Graphics Adapter") |
| 0x4E | 2 | Adresse der aktuellen Seite im Regenerate Buffer |
| 0x50 | 16 | Cursorpositionen für die Seiten 0-7, abwechselnd Spalte und Zeile |
| 0x60 | 2 | Cursortyp |
| 0x62 | 1 | Aktuelle Bildschirmseite |
| 0x63 | 2 | I/O-Basisadresse des Grafikadapters |
| 0x65 | 1 | Inhalt des Mode Select Registers |
| 0x66 | 1 | Inhalt des CGA Palette Registers |

## Weblinks

- <http://www.bioscentral.com/misc/bda.htm>
- <http://www.cs.cmu.edu/~ralf/files.html> (Part C -\> memory.lst)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/11108/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1564/index.html)

<!-- MediaWiki page 1564; revision 11108; parent 10579; 2013-05-01T12:30:41Z -->
