# Týndur/Wunschliste

Hier bitte alle Wünsche für týndur (nach Möglichkeit sortiert nach Zielgebiet) eintragen.

## Kernel

- Umstellung auf kernel2
- Syscall damit Prozess für jeden abgestorbenen Prozess einen RPC erhält (Wichtig u.a. um bei unsauber beendeten Programmen aufräumen zu können - alternativ folgt irgendwann ein OOM)
- Mehr Dokumentation in kernel2, auf týndur wird oft als Beispiel verwiesen und eines seiner ursprünglichen Ziele ist auch, dass es dabei hilfreich sein soll. In den Code könnte man oft fast eine Art Tutorial als Kommentar einbetten.

<!-- -->

- Idee: Eine Art "Code-Walkthrough". Das habe ich mal bei einem Open-Source-Spiel gesehen ([Unknown Horizons](http://www.unknown-horizons.org) falls es wen interessiert), da werden im Code halt Kommentarmarken platziert, die einen neuen Programmierer in logisch sinnvoller Reihenfolge durch den Kern-Code führen, um den Einstieg zu erleichtern. Ist wohl schwer zu warten, aber das ist ja eh nur eine Wunschliste.

<!-- -->

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

- help
  - Kommando um von den Hilfsunterseiten wieder zurück zur Einleitung zu springen (Hilfe neu Starten)
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
  - Liste von Bereits instalierter Software
  - Liste von vorhandener aber noch nicht instalierter Software
- Setup (Installation & Konfiguration)
- FTP-Client
- Mail-Client
- git-Client
- kirc
  - Unterstuetzung fuer mehrere Channels
  - Irgendwie sinnvoll ein /ns identify erlauben
  - Hochscrollen
- fbc (FreeBasic Compiler)
  - (infos hier <http://www.freebasic.net/> )

## LostIO

- Berechtigungen setzen und abfragen
- ioctl/fcntl um kompatibler zu bestehenden Systemen und Anwendungen zu werden (und um alternativ weitere Files im vfs einzusparen)
- Dokumentation/SDK

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/8850/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1513/index.html)

<!-- MediaWiki page 1513; revision 8850; parent 8849; 2010-11-08T19:58:20Z -->
