# MZ EXE

Das MZ EXE Format wurde von Microsoft entwickelt und löste das .COM Format ab. Es wurde hauptsächlich unter DOS verwendet, allerdings steht der MZ EXE Header noch bei vielen Formaten von ausführbaren Dateien aus Kompabilitätsgründen. Der Vorteil dieses Formats gegenüber dem COM Format war die Tatsache, dass die Datei größer als 64KB groß sein konnte, also mehrere Segmente belegen durfte.

Die Buchstaben MZ sind dabei angeblich die Initialen von Mark Zbikowski, einem Mitarbeiter von Microsoft.

## Datengrößen

Im Real Mode bzw. unter DOS benannte man bestimmte Datengrößen anders als heutzutage gebräuchlich:

- Paragraph: 16 Bytes
- Page: 512 Bytes
- Segment: 4096 Bytes

## Aufbau

Im Header eines MZ EXE Programms befinden sich nur 16Bit Werte, weil die Programme im Real Mode liefen / laufen:

| Offset | Name | Beschreibung |
| -------- | --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| 0x00 | Signatur | Identifiziert die Datei als MZ EXE, wenn hier der Wert 0x4D5A ("MZ") steht |
| 0x02 | Größe der letzten Page | *siehe unten* |
| 0x04 | Anzahl Pages | *siehe unten* |
| 0x06 | Anzahl von Einträge in der Relocation Table | *siehe unten* |
| 0x08 | Code Offset | Offset des eigentlichen Codes (in Paragraphen) |
| 0x0A | Benötigter Speicher (min) | Größe des Speichers, der mindestens zusätzlich zum Code noch alloziert werden muss, damit das Programm läuft (in Paragraphen) |
| 0x0C | Benötigter Speicher (max) | Größe des Speichers, der höchstens zusätzlich zum Code noch alloziert werden muss, damit das Programm läuft (in Paragraphen) |
| 0x0E | SS | Wert, der zu Programmstart ins SS Register geladen werden soll |
| 0x10 | SP | Wert, der zu Programmstart ins SP Register geladen werden soll |
| 0x12 | Checksumme | Sorgt dafür, dass, wenn man alle Werte des Headers addiert, man Null erhält. Dieses Feld wurde aber oft vernachlässigt |
| 0x14 | IP | Wert, der zu Programmstart ins IP Register geladen werden soll |
| 0x16 | CS | Wert, der zu Programmstart ins CS Register geladen werden soll |
| 0x18 | Offset der Relocationtable | Offset der Relocationtable in der Datei. Wenn hier 0x40 steht, dann ist die Datei möglicherweise keine MZ EXE |
| 0x1A | ??? | ??? |

## Die Relocationtable

Eine MZ EXE konnte von DOS an jede beliebige Stelle im Speicher geladen werden. Dadurch waren allerdings die Segmentadressen im Code nicht mehr richtig. In der Relocationtable stehen die Adressen derjenigen Segmentwerte, die angepasst werden müssen. Jeder Eintrag besteht aus zwei 16Bit Werten, von denen der eine der Wert das Segment, der zweite der Offset innerhalb des Codes sind. Diese beiden Werte zeigen somit auf den 16 Bit Wert im Code, auf den die Segmentadresse adiert werden muss, an die die MZ EXE geladen wurde.

## Programm ausführen

- Code an den Anfang des gewünschten Startsegments kopieren:
  - Offset des Codes in der Datei: Dem Header entnehmen (0x08)
  - Länge des Codes: Anzahl Pages \* 16 + Größe der letzten Page
- Relocationtable abarbeiten:
  - Offset und Anzahl der Einträge: Dem Header entnehmen (0x06, 0x18)
    - Die Adresse des Startsegments auf die 16 Bit Werte addieren, auf die die Einträge in der Relocationtable zeigen
- Zusätzlichen Speicher für das Programm allozieren
- SS, SP mit den gewünschten Werten laden
- einen Sprung nach CS+Startsegment:IP ausführen

## Siehe auch

- [Microsoft Disk Operating System](https://github.com/lowlevel-eu/wiki/wiki/Microsoft-Disk-Operating-System "Microsoft Disk Operating System")

## Weblinks

- <http://www.tavi.co.uk/phobos/exeformat.html>
- <http://www.delorie.com/djgpp/doc/exe/>

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/9239/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2375/index.html)

<!-- MediaWiki page 2375; revision 9239; parent 0; 2011-01-03T15:33:47Z -->
