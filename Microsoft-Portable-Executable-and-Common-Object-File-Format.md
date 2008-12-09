# Microsoft Portable Executable and Common Object File Format

## Grober Aufbau

### MS-DOS Header

Dieser Header ist ein Kompatibilitätsheader, der unter MS-DOS ausgeführt wird und meist eine Fehlermeldung anzeigt, die besagt, dass das Programm Windows benötigt.  
Für Lowlevel-Zwecke kann dieser Bereich getrost ausgelassen werden, weil

- Programme eines Nicht-Windowssystem brauchen keine MS-DOS-Kompatibilität
- Fast niemand verwendet noch MS-DOS

### PE Kennzeichnung

An der Stelle 0x3c kommt das Kennzeichnen des PE-Formates. Dieser ist 4-Byte groß und sieht so aus: "PE\0\0". (Zwei Nullbytes am Ende) Das ist wiederum ein Kennzeichen von Windows und sollte verändert (nicht weggelassen) werden.

### COFF Dateiheader

Hier ist der Common Object File Format Header:

| Offset | Größe | Beschreibung |
| -------- | --------- | ----------------------------------------------------------------------------------------------- |
| 0x00h | 2 Bytes | Hier wird beschrieben, für welche Plattform diese aufführbare Datei geeignet ist |
| 0x02h | 2 Bytes | Die Anzahl der Sections |
| 0x04h | 4 Bytes | Die ersten 32bits von der Sekundenanzahl von 1.Januar 1970 00:00 bis zur Erstellung der Datei |
| 0x08h | 4 Bytes | Die Dateioffset dieser COFF-Datei. Wenn Null, dann ist gar keine vorhanden |
| 0x0Bh | 4 Bytes | Die Anzahl der Eintragungen von der Symboltabelle (?) |
| 0x0Fh | 2 Bytes | Größe des optimalen Headers der ausführbaren Datei **Achtung, ist nicht für die Objektdatei** |
| 0x12h | 2 Bytes | Flags für Eigenschaften der Datei |

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
| ----- | ----------------------------------------------------------------------------------------------- |
| 1 | Nur für Windows wichtig |
| 2 | Muss Eins sein. Wenn nicht, dann hat der Linker einen Fehler |
| 3 | Obsolet. Sollte Null sein |
| 4 | Obsolet. Sollte Null sein |
| 5 | Obsolet. Sollte Null sein |
| 6 | Das Programm kann mit mehr als 2GB umgehen. In naher Zukunft wird dieser Eintrag obsulet sein |
| 7 | Reserviert |
| 8 | Obsolet. Sollte Null sein |
| 9 | Plattform basiert auf 32-Bit-Ausdrücken |
| 10 | Debuginformationen wurden entfernt |
| 11 | Diese Datei stammt aus dem Internet oder von einem Wechselmedium |
| 12 | Diese Datei ist eine Systemdatei und kein Anwendungsprogramm |
| 13 | Diese Datei ist eine DLL |
| 14 | Diese Datei sollte auf einem Einprozessor-System laufen |
| 15 | Obsolet. Sollte Null sein |

### Informationen zum optimalen Header

Jede ausführbare Datei hat ein optimalen Header. Hier wird er (für Windows) benötigt. In Objektdateien wird dieser normalerweise nicht verwendet, außer seine Größe zu erhöhen. Der optimale Header wird in drei Abschnitte unterteilt (Zu PE32 und PE32+ siehe unten):

| Offset PE32/PE32+ | Größe | Beschreibung |
| ------------------- | ---------- | ------------------------------------------------------------------------------- |
| 0 | 28/24 | Zeigt allgemeine Informationen an |
| 28/24 | 68/88 | Windows-spezifische Informationen |
| 96/112 | Variabel | Sind Adressen oder Teile von Tabellen, die für das Betriebsystem wichtig sind |

Der erste Abschnitt wird wiederum in folgendermaßen unterteilt:

| Offset | Größe | Beschreibung |  |  |  |
| -------- | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----- | --------- | ------------------------------------------------------------------------- |
| 0 | 2 Bytes | Hier wird angegeben, ob es sich um PE32(0x10Bh) oder PE32+(0x20Bh) handelt. Bei PE32+ wird ein 64-Bit-Namensraum verwendet. Unter Windows gibt es trotzdem eine Beschränkung auf 2 GiB. Möglich ist es auch, die Datei als ROM Image( 0x107h) zu kennzeichen, aber es geht nicht hervor, was die Unterschiede sind. |  |  |  |
| 2 | 1 Byte | Hauptversion des Linkers |  |  |  |
| 3 | 1 Byte | Nebenversion des Linkers |  |  |  |
| 4 | 4 Bytes | Hier soll die Größe des Quellcodes hin |  |  |  |
| 8 | 4 Bytes | Die Summe aller initialisierten Datensektionen |  |  |  |
| 12 | 4 Bytes | Die Summe aller nicht initialisierten Datensektionen (BSS) |  |  |  |
| 16 | 4 Bytes | Die Adresse des Entry Points (Einsprungpunktes) bezogen auf den Anfang der Datei. Im Fall einer Anwengung ist dies die Position des ersten Befehls, bei Gerätetreibern die Adresse der Initialisierungsfunktion. Für DLL-Dateien ist der Entrypoint optional; sollte keiner erwünscht sein, muss dieser Wert 0 sein. | 20 | 4 Bytes | Die Adresse, die relativ zum ersten Sektor der ausführbaren Datei steht |

## Links

- [Microsoft Portable Executable and Common Object File Format Specification](http://www.microsoft.com/whdc/system/platform/firmware/PECOFF.mspx)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/3645/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1644/index.html)

<!-- MediaWiki page 1644; revision 3645; parent 3644; 2008-12-09T17:31:54Z -->
