# Microsoft Portable Executable and Common Object File Format

Diese Seite ist ein Artikel, welcher **mehr** haben könnte..  

Wenn du mehr darüber weißt oder recherchieren willst, bist **du** aufgerufen, dies zu tun. Wenn du dir in einer Sache nicht sicher bist, dann stell es auf die Diskussionsseite.

## Aufbau

### EXE Header

Dieser Header ist der Basisheader jeder Datei im EXE-Format (auch DLL und andere abgeleitete Dateien), worauf sich der PE/COFF-Header aufbaut. Da aber die Informationen für solche Dateien nicht mehr im EXE-Header abgelegt werden, könnte man theoretisch den EXE-Header weglassen. Leider ist dem aber nicht so, weil dieser die Offsetadresse zu unserem PE/COFF-Header enthält.

Die folgende Tabelle zeigt, was noch vom EXE-Header benötigt wird:

| Offset | Größe | Beschreibung |
| -------- | ---------- | ------------------------------------------------------------ |
| 0x00 | 2 Bytes | EXE-Datei Signatur ("MZ") |
| 0x02 | 6 Bytes | *Unbedeutend* |
| 0x08 | 2 Bytes | Größe des EXE-Header in 16-Byte-Paragraphen (Wert: 0x0004) |
| 0x0A | 50 Bytes | *Unbedeutend* |
| 0x3C | 4 Bytes | Dateioffset des PE/COFF-Header |

### MS-DOS-Stub

Dieser liegt an offset 0x4F und dient nur noch dazu, um unter DOS nur die Meldung "This programm cannot be run in DOS mode" auszugeben.

### PE Kennzeichnung

Dem DOS Stub folgt die eigentliche PE Datei. Sie beginnt mit der Signatur, die 4 Byte Lang ist und den Wert 0x00004550 enthält, was dem Wort "PE", gefolgt von zwei Nullbytes entspricht.

### COFF Dateiheader

Hier ist der Common Object File Format Header:

| Offset | Größe | Beschreibung |
| -------- | --------- | --------------------------------------------------------------------------------------------- |
| 0x00 | 2 Bytes | Hier wird beschrieben, für welche Plattform diese aufführbare Datei geeignet ist |
| 0x02 | 2 Bytes | Die Anzahl der Sektoren |
| 0x04 | 4 Bytes | Die ersten 32 Bits der Sekundenanzahl vom 1. Januar 1970 00:00 bis zur Erstellung der Datei |
| 0x08 | 4 Bytes | In der Objektdatei der Offset zur Symboltabelle. Sollte in der Executable 0 sein. |
| 0x0B | 4 Bytes | Die Anzahl der Eintragungen von der Symboltabelle |
| 0x0F | 2 Bytes | Größe des "optionalen" Headers in der Executable. Sollte in einer Objektdatei 0 sein. |
| 0x12 | 2 Bytes | Flags für Eigenschaften der Datei |

#### Plattformtypen für den COFF-Header

In dieser Tabelle werden die Werte für die Plattformentypen des COFF-Headers erläutert.

| Wert | Plattform |
| -------- | ---------------------------------------------------------------------------------- |
| 0x0000 | Nicht bekannt oder auf jeder Plattform lauffähig. |
| 0x01D3 | Matsushita AM33 |
| 0x8664 | [x64](https://github.com/lowlevel-eu/wiki/wiki/X86-64 "X64") |
| 0x01C0 | ARM little endian |
| 0x0EBC | EFI Bytecode |
| 0x014C | [x86](https://github.com/lowlevel-eu/wiki/wiki/X86 "X86") kompatible Prozessoren |
| 0x0200 | Intel Itanium Prozessorfamilie |
| 0x9041 | Mitsubishi M32R little endian |
| 0x0266 | MIPS16 |
| 0x0366 | MIPS mit FPU |
| 0x0466 | MIPS16 mit FPU |
| 0x01f0 | Power PC little endian |
| 0x00f1 | Power PC mit Floating Point Support |
| 0x0166 | MIPS little endian |
| 0x01A2 | Hitachi SH3 |
| 0x01A3 | Hitachi SH3 DSP |
| 0x01A6 | Hitachi SH4 |
| 0x01A8 | Hitachi SH5 |
| 0x01C2 | ARM Thumb |
| 0x0169 | MIPS little endian WCE v2 |

#### Flags des COFF-Headers

| Bit | Funktion |
| ----- | ----------------------------------------------------------------------------------------------- |
| 1 | Nur für Windows wichtig |
| 2 | Muss Eins sein. Wenn nicht, dann hat der Linker einen Fehler |
| 3 | Obsolet. Sollte Null sein |
| 4 | Obsolet. Sollte Null sein |
| 5 | Obsolet. Sollte Null sein |
| 6 | Das Programm kann mit mehr als 2GB umgehen. In naher Zukunft wird dieser Eintrag obsolet sein |
| 7 | Reserviert |
| 8 | Obsolet. Sollte Null sein |
| 9 | Plattform basiert auf 32-Bit-Ausdrücken |
| 10 | Debuginformationen wurden entfernt |
| 11 | Diese Datei stammt aus dem Internet oder von einem Wechselmedium |
| 12 | Diese Datei ist eine Systemdatei und kein Anwendungsprogramm |
| 13 | Diese Datei ist eine DLL |
| 14 | Diese Datei sollte auf einem Einprozessor-System laufen |
| 15 | Obsolet. Sollte Null sein |

  

#### Informationen zum "optionalen" Header

Keiner weiß warum der Optionale Header so heißt, wie er heißt denn jede ausführbare PE Datei hat ein "optionalen" Header. Der optionale Header wird in drei Abschnitte unterteilt (Zu PE32 und PE32+ siehe unten):

| Offset PE32/PE32+ | Größe | Beschreibung |
| ------------------- | ---------- | ------------------------------------------------------------------------------- |
| 0 | 28/24 | Zeigt allgemeine Informationen an |
| 28/24 | 68/88 | Windows-spezifische Informationen |
| 96/112 | Variabel | Sind Adressen oder Teile von Tabellen, die für das Betriebsystem wichtig sind |

Der erste Abschnitt wird wiederum in folgendermaßen unterteilt:

| Offset | Größe | Beschreibung |
| -------- | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0x00 | 2 Bytes | Hier wird angegeben, ob es sich um PE32(0x10B) oder PE32+(0x20B) handelt. Bei PE32+ wird ein 64-Bit-Namensraum verwendet. Unter Windows gibt es trotzdem eine Beschränkung auf 2 GiB. Möglich ist es auch, die Datei als ROM Image( 0x107) zu kennzeichen, aber es geht nicht hervor, was die Unterschiede sind. |
| 0x02 | 1 Byte | Hauptversion des Linkers |
| 0x03 | 1 Byte | Nebenversion des Linkers |
| 0x04 | 4 Bytes | Hier soll die Größe des Quellcodes hin |
| 0x08 | 4 Bytes | Die Summe aller initialisierten Datensektionen |
| 0x0C | 4 Bytes | Die Summe aller nicht initialisierten Datensektionen (BSS) |
| 0x10 | 4 Bytes | Die Adresse des Entry Points (Einsprungpunktes) bezogen auf den Anfang der Datei. Im Fall einer Anwengung ist dies die Position des ersten Befehls, bei Gerätetreibern die Adresse der Initialisierungsfunktion. Für DLL-Dateien ist der Entrypoint optional; sollte keiner erwünscht sein, muss dieser Wert 0 sein. |
| 0x14 | 4 Bytes | Die Adresse, die relativ zum ersten Sektor der ausführbaren Datei steht |
| 0x18 | 4 Bytes | Die Adresse, die relativ zum ersten Sektor der ausführbaren Datei steht. (Nur bei PE32 nötig). |

  
Den Windows spezifischen Teil wird hier nicht erklärt, weil dies für lowlevel nicht wichtig ist. Der geneigte Leser kann die Spezifikation ab Seite 12 durchlesen.  
Im dritten Teil können Strings oder Tabellen angegeben werden, damit sie das Betriebsystem verwenden kann. Es können beliebig viele Resourcen angegeben werden. Jede Resourcenangabe besteht aus zwei Feldern, die jede beide 4-Byte groß sind:

- Die Adresse der Tabelle relativ zum ersten Sektor der ausführbaren Datei zum Zeitpunkt des Laden der Tabelle
- Ihre Größe in Bytes

### Sektorentabelle

Die Sektorentabelle kommt immer nach dem optimalen Header. Die Headergröße wird im COFF-Header festgelegt. Ebenfalls wird die Größe der Tabelle im COFF-Header festgelegt. Jeder Sektor besteht aus folgenden Abschnitten:

| Offset | Größe | Beschreibung |
| -------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0x00 | 8 | Ist ein 8-Byte-String auf UTF-8 Basis. Wenn genau 8-Bytes verwendet wird, dann ist kein Nullbyte nötig. Bei Objektdateien darf dieser länger sein, bei ausführbaren Dateien ist dies verboten.<br> |
| 0x08 | 4 | Die endgültige Größe eines Sektors, wenn es geladen wird. Bei Objektdateien ist dieser Abschnitt voller Nullen. |
| 0x0C | 4 | Für ausführbare Dateien die Adresse des ersten Bytes der Sektion relativ zum Image Basis(?). Bei Objektdateien ist die Adresse des ersten angelegten Bytes, bevor die Verlagerung abgeschlossen ist.<br> |
| 0x10 | 4 | Dies Feld ist gerundet. Entweder die Größe des Sektors(Objektdateien) oder die Größe des initialisierten Daten auf der Festplatte(Bei Imagedateien) Ist dieser Teil kleiner als das Offset 8, dann sind der Rest der Sektorentabelle Nullen. Wenn diese Sektion nur uninitialisierte Daten enthält, dann ist dieser Teil Null. |
| 0x14 | 4 | Der Dateipointer zur ersten Sektion innerhalb des COFF-Headers. Für Objektdateien sollte dieser Teil an einer 4-Byte-Grenze ausgerichtet sein. Enthält die Sektion nur uninitialisierte Daten, dann ist dieser Teil Null. |
| 0x18 | 4 | *nicht verwendet (PointerToRelocations)*<sup>1</sup> |
| 0x1C | 4 | *nicht verwendet (PointerToLinenumbers)*<sup>1</sup> |
| 0x20 | 2 | *nicht verwendet (PointerToLinenumbers)*<sup>1</sup> |
| 0x22 | 2 | *nicht verwendet (PointerToLinenumbers)*<sup>1</sup> |
| 0x24 | 4 | Eigenschaften der Sektion |

<sup>1</sup> Die Felder 0x18 bis 0x23 stammen aus Coff und haben in PE keine Bedeutung. Sie sind auf 0 zu setzten.

#### Eigenschaften für Sektionen

Es gibt folgende Eigneschaftflags von 0 bis 31:

| Nummber | Sektionstyp |
| --------- | -------------------------------------- |
| 5 | Code Sektion |
| 6 | Initialisierte Daten Section (.data) |
| 7 | Unnitialisierte Daten Section (.bss) |
| 26 | Sektion, kann nicht gecached werden. |
| 27 | nicht pagebare Sektion |
| 28 | gemeinsame Sektion |
| 29 | Ausführbare Sektion |
| 30 | Lesbare Sektion |
| 31 | Schreibbare Sektion |

## Weblinks

- [Microsoft Portable Executable and Common Object File Format Specification](http://www.microsoft.com/whdc/system/platform/firmware/PECOFF.mspx)
- [\[1\]](http://www.csn.ul.ie/~caolan/publink/winresdump/winresdump/doc/pefile.html)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/10373/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1644/index.html)

<!-- MediaWiki page 1644; revision 10373; parent 10369; 2011-12-19T19:36:40Z -->
