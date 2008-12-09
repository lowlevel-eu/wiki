# Microsoft Portable Executable and Common Object File Format

## Grober Aufbau

### MS-DOS Header

Diese Header ist ein Kompabilitätsheader, womit im MS-DOS ausgedrückt werden kann, dass das Programm darunter nicht läuft.  
Für lowlevel kann dieser Bereich getrost ausgelassen werden, weil

- Programme eines Nicht-Windowssystem brauchen nicht unter MS-DOS zu laufen
- Fast niemand hat noch MS-DOS

### PE Kennzeichnung

An der Stelle 0x3c kommt das Kennzeichnen des PE-Formates. Dieser ist 4-Byte groß und sieht so aus: "PE\0\0". (Zwei Nullbytes am Ende) Das ist wiederum ein Kennzeichen von Windows und sollte verändert(nicht weggelassen) werden.

### COFF Dateiheader

Hier ist der Common Object File Format Header:

| Offset | Größe | Beschreibung |
| -------- | --------- | ------------------------------------------------------------------------------------------------------ |
| 0x00h | 2 Bytes | Hier wird beschrieben, für welche Plattform diese aufführbare Datei geeignet ist. |
| 0x02h | 2 Bytes | Die Anzahl der Sections. |
| 0x04h | 4 Bytes | Die ersten 32-Bytes von der Sekundenanzahl ab 1.Januar 1970 00:00, wann die Datei hergestellt wurde. |
| 0x08h | 4 Bytes | Die Dateioffset dieser COFF-Datei. Wenn Null, dann ist garkeine vorhanden. |
| 0x0Bh | 4 Bytes | Die Anzahl der Eintragungen von der Symboltabelle.(?) |
| 0x0Fh | 2 Bytes | Größe des optimalen Headers der ausführbaren Datei. **Achtung, ist nicht für die Objektdatei** |
| 0x12h | 2 Bytes | Flags für Eigenschaften der Datei. |

## Weitergehende Informationen

### Plattformtypen für den COFF-Header

In dieser Tabelle werden die Werte für die Plattformentypen des COFF-Headers erläutert.

| Wert | Plattform |
| --------- | ---------------------------------------------------------------------------------- |
| 0x00h | Nicht bekannt oder auf jeder Plattform lauffähig. |
| 0x1D3h | Matsushita AM33 |
| 0x8664h | [x64](https://github.com/lowlevel-eu/wiki/wiki/X86-64 "X64") |
| 0x1C0h | ARM little endian |
| 0xEBCh | EFI Bytecode |
| 0x14Ch | [x86](https://github.com/lowlevel-eu/wiki/wiki/X86 "X86") kompatible Prozessoren |
| 0x200h | Intel Itanium Prozessorfamilie |
| 0x9041h | Mitsubishi M32R little endian |
| 0x266h | MIPS16 |
| 0x366h | MIPS mit FPU |
| 0x466h | MIPS16 mit FPU |
| 0x1f0h | Power PC little endian |
| 0xf1h | Power PC mit Floating Point Support |
| 0x166h | MIPS little endian |
| 0x1A2h | Hitachi SH3 |
| 0x1A3h | Hitachi SH3 DSP |
| 0x1A6h | Hitachi SH4 |
| 0x1A8h | Hitachi SH5 |
| 0x1C2h | Thumb |
| 0x169h | MIPS little endian WCE v2 |

### Flags des COFF-Headers

| Bit | Funktion |
| ----- | ----------------------------------------------------------------------------------------- |
| 1 | Nur für Windows wichtig. |
| 2 | Muss Eins sein. Wenn nicht, dann hat der Linker ein Fehler. |
| 3 | Obsulot. Sollte Null sein. |
| 4 | Obsulot. Sollte Null sein. |
| 5 | Obsulot. Sollte Null sein. |
| 6 | Das Programm kann mit mehr als 2GB was anfangen. In naher Zukunft wird es obsulot sein. |
| 7 | Reserviert. |
| 8 | Obsulot. Sollte Null sein. |

Wird noch erweitert.

## Links

- [Microsoft Portable Executable and Common Object File Format Specification](http://www.microsoft.com/whdc/system/platform/firmware/PECOFF.mspx)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/3641/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1644/index.html)

<!-- MediaWiki page 1644; revision 3641; parent 3640; 2008-12-09T16:38:04Z -->
