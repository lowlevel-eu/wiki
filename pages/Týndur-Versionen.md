# Týndur/Versionen

## Version 0.1.x - Codename Morgoth

### Version 0.1.0

Die erste Version des Community-OS. Der Feature-Freeze für die Version war am 09.04.2007, das Release erfolgte am 03.05.2007. Features waren:

- Speicher & Prozessverwaltung
- einfache Interprozesskommunikation
- Treiber für [DMA](Direct-Memory-Access "DMA"), [Diskettenlaufwerke](Floppy-Disk-Controller "FDC") und [Tastaturen](Keyboard-Controller "KBC")
- Einfache Textkonsolen
- Unterstützung für das [FAT12](File-Allocation-Table "File Allocation Table")-Dateisystem ([LostIO](T%C3%BDndur-LostIO "LostIO")-Treiber)
- eine einfache Shell

  

### Version 0.1.1

Diese Version enthält Überarbeitungen und Bugfixes für Features der 0.1.0-Version. Neuerungen:

- Experimentelle Netzwerkunterstützung
- Texteditor
- Optimierte RPC-Funktionen
- Puffer in LostIO
- Kernelseitige Kontrolle der IO-Ports
- Geschwindigkeit des Diskettentreibers stark verbessert

  

## Version 0.2.x - Codename Gothmog

### Version 0.2.0

Das Release im Jahr 2008 (genauer: am 24.12.2008), und außerdem erste Version unter dem neuen Namen týndur. Offizielle Features:

- Treiber für ata und ext2
- Paketverwaltung lpt
- Pakete wie binutils, fpc (FreePascal), gcc und nano
- Netzwerkunterstützung mit Treiber für [RTL8139](RTL8139 "RTL8139") und sis900
- Tab-Completion und andere neue Möglichkeiten zum editieren der Kommandozeile in der Shell
- Editor kedit verbessert; neu ist unter anderem das Syntax-Highlighting für C (einschalten mit F8)
- Virtuelle Terminals (umschaltbar via Alt+Fx, Standardmäßig gibt es 4 Terminals)

Außerdem hat sich unter der Haube viel getan, die meisten Treiber basieren jetzt auf der vom Betriebssystem unabhängigen Schnittstelle [CDI](Common-Driver-Interface "CDI").

  

### Version 0.2.1

Release am 05.07.2009

- lpt-Pakete: lynx ist als Browser neu dazugekommen, die e2fstools erlauben das Anlegen neuer Dateisysteme und Free Pascal wurde auf 2.3.1 aktualisiert. Außerdem sind dropbear als SSH-Client und der Subversion-Client portiert worden.
- Ein neues Hilfesystem wurde integriert, das den alten help-Befehl ersetzt (nur auf dem Festplattenimage)
- CD-ROM-Unterstützung
- UTF-8-Unterstützung (und damit endlich auch Umlaute in Shell, Editor und IRC-Client)
- Neues Tool build, das einen Quellcode-Verzeichnisbaum baut (braucht einen installierten Compiler)
- Ein Haufen Fehlerkorrekturen

### Version 0.2.2

Release am 25.12.2009

- Unterstützung für TCP-Server
- Konfigurierbare Tastaturbelegung und einige mehrsprachige Anwendungen
- setup als menügeführtes Konfigurationstool
- FTP-Client
- Neue lbuilds: svn, maumau, fasm, nasm, ctris
- Ein Haufen kleinerer Erweiterungen und Bugfixes

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/10631/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2237/index.html)

<!-- MediaWiki page 2237; revision 10631; parent 7746; 2012-07-02T08:21:28Z -->
