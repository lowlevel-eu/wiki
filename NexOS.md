# NexOS

| Nexos |  |
| ----------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
|  |  |
| Entwickler: | [Christian Kranz](https://lowlevel-eu.github.io/wiki/pages/1744/index.html "Benutzer:Chris12") |
| Akt. Version: | 0.0.0.1 |
| [Lizenz](https://github.com/lowlevel-eu/wiki/wiki/Lizenzen "Lizenzen"): | BSD |
| OS-Eigenschaften |  |
| Plattform: | [x86](https://github.com/lowlevel-eu/wiki/wiki/X86 "X86") |
| [Kernelart](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel"): | Monolithischer Kernel |
| [Sprache](https://lowlevel-eu.github.io/wiki/pages/1648/index.html "Kategorie:Programmiersprache"): | [Assembler](https://github.com/lowlevel-eu/wiki/wiki/Assembler "Assembler"), NPL (NexOS Programming Language; für Programme) |
| API: | Int 0xFF |
| Binärformat: | RAW |
| [IPC-Methode](https://github.com/lowlevel-eu/wiki/wiki/Interprozesskommunikation "IPC"): |  |
| Homepage |  |

NexOS wird momentan für die 6116 CPU neu geschrieben. Da die Plattform aber noch nicht ganz fertiggestellt wurde und somit das Programmieren noch nicht begonnen hat, wird im folgendem NexOS für die x86 Plattform vorgestellt.

## Entwickler

- [chris12](https://lowlevel-eu.github.io/wiki/pages/1744/index.html "Benutzer:Chris12")

## Aktuelle Features

- Bootloader für Disketten mit NexFS
- kleine API
- 80x50 oder 80x25 Textmodus
- NexCommand mit Deutschem Tastatur-Layout inklusive ä, ö, ü (einige zeichen sind NexCommand spezifisch und unter anderen OS' auf dieser Taste enthalten bzw. einige Sonderzeichen stimmen nicht mit der Tastatur überein z.B. anstatt "´" ist das Funktionszeichen vorhanden)
- Dateisystem NexFS 0.1
- Dateinamen können Groß- und Kleinbuchstaben enthalten (Programmnamen sollten groß sein, da NexCmd nur Großbuchstaben Befehle hat, es sei denn man benutzt 'START' (Noch nicht implementiert))
- 8.3 Dateinamen
- Diskettennamen (8 Zeichen)
- Programme können ausgeführt werden

## Aktuelle Arbeiten

- NexFS 0.2
- FS-API verfollständigen
- Kernel V0.0.0.2

## API

| INT 0xFF, AL = | Beschreibung | Eingabe | Ausgabe |
| ---------------- | ----------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| 01h | Stringausgabe | SI = String | Inhalt von String auf dem Bildschirm |
| 02h | Version | \- | AX = Version (1234 = 1.2.3.4) |
| 03h | Ausgabe der Version auf dem Bildschirm | \- | Version auf dem Bildschirm |
| 04h | Programm beenden | \- | \- |
| 05h | lädt Daten an eine Stelle in den RAM | CX = Anzahl der Bytes<br>SI = Zeiger auf die Daten<br>DI = Segmen im RAM<br>BX = Offset im RAM<br> | \- |
| 06h | lädt die Dateitabelle des aktuellen Verzeichnisses von der Diskette | \- | \- |
| 07h | prüft ob eine Datei existiert | SI = Dateiname | AX = 01h (kein Fehler)<br>AX = 00h (Datei nicht gefunden)<br> |
| 08h | lädt eine Datei | SI = Dateiname<br>BX = Segment in das geladen werden soll; einige Segmente sind gesperrt<br> | AX = 02h (Segment gesperrt) AX = 01h (kein Fehler)<br>AX = 00h (Datei nicht gefunden)<br> |
| 09h | Verzeichnis wechsel | SI = Verzeichnis<br>(8-Zeichen-Name.DIR für Verzeichnisse und '..' für das übergeordnete)<br> | AX = 01h (kein Fehler)<br>AX = 00h (Datei nicht gefunden)<br> |
| 0Ah | Datei/Verzeichnis löschen | SI = Dateiname<br> | AX = 02h (Datei gesperrt) AX = 01h (kein Fehler)<br>AX = 00h (Datei nicht gefunden)<br> |
| 0Bh | gibt die max. Anzahl an Einträgen des aktuellen Verzeichnisses zurück | \- | AX = max. Anzahl an Einträgen des aktuellen Verzeichnisses |

  

## Befehlsliste der Konsole

    CD DIR       - Wecheslt in das Verzeichnis DIR
    CLS          - löscht den Bildschirminhalt
    CPU          - zeigt Informationen über ihre CPU (via CPUID; im Moment nur die Vendor-ID)
    DEL FILE     - Löscht die Datei oder das Verzeichnis FILE
    DIR          - listet die Dateien im Verzeichnis auf
    DUMP         - zeigt den Inhalt der CPU Register
    ECHO STRING  - zeigt 'STRING' auf dem Bildschirm an
    HELP         - zeigt die Hilfe
    LIST         - listet die Befehle auf
    REBOOT       - startet den Computer neu
    SHUTDOWN     - fährt NexOS herunter
    SWITCH       - wechselt den Textmodus
    VER          - zeigt die Versionen der Systemkomponenten

## History

Aktuelle Version zum Download: [Hier](http://chris122.ch.funpic.de/NexOS/img/NexOS.img)

### Ver 0.0.0.2 Ori

- Working in progress

**!Bis zum Erscheinen werden hier und auf der Website keine Informationen über Version 0.0.0.2 zur Verfügung gestellt!**

### Ver 0.0.0.1 Midway

- Neuer Kernel (Ver 0.0.0.1)
- Bootloader für Disketten mit NexFS 0.1
- NexCommand
- NexFS 0.1
- ausführen von Programmen via NexFS 0.1

### Ver 0.0.0.0

- Kompletter Neustart des Projekts (Mittwoch, Februar 04 2009)

## TODO

- erstellen/verändern von Dateien und formatieren von Disketten in NexFS einbauen
- Dateisystem: NexFS 0.2, (Fat12)
- Editor überarbeiten
- Kernel V0.0.0.2
- Passwortchanger / Passwort-Programm wieder einbauen
- Homepage fertigstellen

## Known Bugs

### NexOS Kernel

- keine Bugs bekannt

### NexCommand

- Backspace springt von der x-ten Zeile nicht in die vorige

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/9832/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1884/index.html)

<!-- MediaWiki page 1884; revision 9832; parent 9831; 2011-06-10T09:09:01Z -->
