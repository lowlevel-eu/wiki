# Týndur/Wunschliste

Hier bitte alle Wünsche für týndur (nach Möglichkeit sortiert nach Zielgebiet) eintragen.

## Kernel

- Syscall damit Prozess für jeden abgestorbenen Prozess einen RPC erhält (Wichtig u.a. um bei unsauber beendeten Programmen aufräumen zu können - alternativ folgt irgendwann ein OOM)
- Mehr Dokumentation in kernel2, auf týndur wird oft als Beispiel verwiesen und eines seiner ursprünglichen Ziele ist auch, dass es dabei hilfreich sein soll. In den Code könnte man oft fast eine Art Tutorial als Kommentar einbetten.

<!-- -->

- Idee: Eine Art "Code-Walkthrough". Das habe ich mal bei einem Open-Source-Spiel gesehen ([Unknown Horizons](http://www.unknown-horizons.org) falls es wen interessiert), da werden im Code halt Kommentarmarken platziert, die einen neuen Programmierer in logisch sinnvoller Reihenfolge durch den Kern-Code führen, um den Einstieg zu erleichtern. Ist wohl schwer zu warten, aber das ist ja eh nur eine Wunschliste.

<!-- -->

- LostIOv2 als neues, kernelbasiertes virtuelles Dateisystem soll das bisherige LostIO, das im Userspace läuft, ablösen und sowohl eine sauberere Schnittstelle bereitstellen als auch die Performance verbessern
- Portierung auf amd64
- FPU-Unterstützung
- Multithreading (mit oder ohne SMP)

## Allgemeines

- Shared Libraries
- POSIX-kompatible Shell
- libc:
  - fork/exec
- Buildsystem überarbeiten (oder für Neulinge erklären)
- servmgr in init integrieren
- Automagisch Treiber für installierte PCI-Geräte laden

## Module

- Tastaturtreiber
  - Deadkeys
- Framebufferkonsole für mehr als 80x25

  

## Treiber

### Block

- AHCI

### Netzwerk

- nVidia MCP67 \[10de:054c\]
- Atheros AR8132 PCI-E Fast Ethernet Controller \[1969:1062\]
- Realtek PCIe Gigabit Ethernet Family Controller \[10EC:8168\]
- Broadcom Corporation NetLink BCM57785 Gigabit Ethernet PCIe \[14e4:16b5\]

## Anwendungen

- help
  - Kommando um von den Hilfsunterseiten wieder zurück zur Einleitung zu springen (Hilfe neu Starten)
- kedit
  - Suchen
  - Markieren, Kopieren/Ausschneiden, Einfügen
    - Idealerweise über eine systemweite Zwischenablage, so dass man von einer kedit-Instanz in eine andere kopieren kann
  - build-Integration
  - vim-Befehlsmodus
- lpt
  - Upgrades
  - aptitude-ähnliche TUI
  - Liste von Bereits installierter Software
  - Liste von vorhandener aber noch nicht instalierter Software
- Setup (Installation)
- Mail-Client
- git-Client
- kirc
  - Irgendwie sinnvoll ein /ns identify erlauben
    - Geht das nicht mit */msg NickServ identify passwort*? --[Sfan](https://lowlevel-eu.github.io/wiki/pages/2378/index.html "Benutzer:Sfan") 18:18, 3. Apr. 2011 (CEST)
  - Hochscrollen
- fbc (FreeBasic Compiler)
  - (infos hier <http://www.freebasic.net/> )

## LostIO

- Berechtigungen setzen und abfragen
- ioctl/fcntl um kompatibler zu bestehenden Systemen und Anwendungen zu werden (und um alternativ weitere Files im vfs einzusparen)
- Dokumentation/SDK

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/10795/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1513/index.html)

<!-- MediaWiki page 1513; revision 10795; parent 10622; 2012-09-11T08:37:10Z -->
