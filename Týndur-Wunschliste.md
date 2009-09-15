# Týndur/Wunschliste

Hier bitte alle Wünsche für týndur (nach Möglichkeit sortiert nach Zielgebiet) eintragen.

## Kernel

- Umstellung auf kernel2
- Syscall damit Prozess für jeden abgestorbenen Prozess einen RPC erhält (Wichtig u.a. um bei unsauber beendeten Programmen aufräumen zu können - alternativ folgt irgendwann ein OOM)
- Mehr Dokumentation in kernel2, auf tyndur wird oft als Beispiel verwiesen und eines seiner ursprünglichen Ziele ist auch, daß es dabei hilfreich sein soll. In den Code könnte man oft fast eine Art Tutorial als Kommentar einbetten.
- LostIOv2 als neues, kernelbasiertes virtuelles Dateisystem soll das bisherige LostIO, das im Userspace läuft, ablösen und sowohl eine sauberere Schnittstelle bereitstellen als auch die Performance verbessern
- Portierung auf amd64
- FPU-Unterstützung

## Allgemeines

- Entfernen der COM1-Ausgabe aus putc, stattdessen wäre ein komplettes Modul für serielle Ausgänge (inkl. Eingabe, nicht nur Ausgabe) wünschenswert.
- Mehr Hardwareunterstützung
- Shared Libraries
- POSIX-kompatible Shell
- libc:
  - xscanf
  - fork/exec

## Module

- Tastaturtreiber
  - Ladbare Tastaturbelegungen
  - Deadkeys
- Framebufferkonsole für mehr als 80x25

## Anwendungen

- kedit
  - Suchen
  - Markieren, Kopieren/Ausschneiden, Einfügen
    - Idealerweise über eine systemweite Zwischenablage, so dass man von einer kedit-Instanz in eine andere kopieren kann
  - build-Integration
  - vim-Befehlsmodus
  - Syntaxhighlighting für mehr Sprachen
- lpt
  - Upgrades
  - aptitude-ähnliche TUI
- Setup (Installation & Konfiguration)
- FTP-Client
- Mail-Client
- git-Client

## LostIO

- Berechtigungen setzen und abfragen
- ioctl/fcntl um kompatibler zu bestehenden Systemen und Anwendungen zu werden (und um alternativ weitere Files im vfs einzusparen)
- Dokumentation/SDK

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/5913/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1513/index.html)

<!-- MediaWiki page 1513; revision 5913; parent 5901; 2009-09-15T14:53:00Z -->
