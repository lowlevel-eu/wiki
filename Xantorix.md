# Xantorix

| Xantorix |  |
| ----------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
|  |  |
| Entwickler: | Homix |
| Akt. Version: | 0.2.0 |
| [Lizenz](https://github.com/lowlevel-eu/wiki/wiki/Lizenzen "Lizenzen"): | Closed Source, Freeware |
| OS-Eigenschaften |  |
| Plattform: | [x86](https://github.com/lowlevel-eu/wiki/wiki/X86 "X86") |
| [Kernelart](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel"): | [Monolithischer Kernel](https://github.com/lowlevel-eu/wiki/wiki/Kernel#monolithischer-kernel "Monolithischer Kernel") |
| [Sprache](https://lowlevel-eu.github.io/wiki/pages/1648/index.html "Kategorie:Programmiersprache"): | [Pascal](https://github.com/lowlevel-eu/wiki/wiki/Pascal "Pascal") |
| API: | XixAPI |
| Binärformat: | [PE](https://github.com/lowlevel-eu/wiki/wiki/Microsoft-Portable-Executable-and-Common-Object-File-Format "PE") |
| [IPC-Methode](https://github.com/lowlevel-eu/wiki/wiki/Interprozesskommunikation "IPC"): | \- |
| Homepage |  |

[www.xantorix.de](http://www.xantorix.de)

  
**Xantorix** ist ein kleines 32-Bit Hobby-[Betriebssystem](https://github.com/lowlevel-eu/wiki/wiki/Betriebssystem "Betriebssystem") für Computer mit x86-Architektur. Ziel ist es, ein schnelles, stabiles und speichersparendes System zu erschaffen, das für den Benutzer möglichst einfach zu bedienen ist. Der [Kernel](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel") des Betriebssystems sowie auch die meisten [Treiber](https://github.com/lowlevel-eu/wiki/wiki/Treiber "Treiber"), Bibliotheken und Programme sind bis auf einige wenige Ausnahmen komplett selbst geschrieben. Xantorix ist derzeit hauptsächlich in [Pascal](https://github.com/lowlevel-eu/wiki/wiki/Pascal "Pascal") (mit Hilfe des FreePascal Compilers) programmiert.  
Aktuell wird an der Version 0.4.0 gearbeitet, die eine grafische Benutzeroberfläche und Netzwerkunterstützung beinhalten soll. Zu Demonstrations- und Testzwecken soll davor eine Zwischenversion 0.3.0 erscheinen, um den Entwicklungsstand zu zeigen. Gegen Ende des Jahres mit der Version 0.4.0 wird auch angedacht, das Projekt komplett oder zumindest größtenteils unter einer OpenSource-Lizenz zur Verfügung zu stellen.

## Versionen

Überblick der verschiedenen Versionen seit Umbenennung:

    29.12.2009 : Xantorix 0.2.0
    20.12.2008 : Xantorix 0.1.2

Anmerkung: Da die Entwicklung der neuen Versionen voranschreitet und die bisherigen Releases schon ein wenig zurückliegen, sind diese Versionen nicht mehr als "aktuell" anzusehen.

## Roadmap

Folgende Versionen sind geplant:

    September 2011 : Xantorix 0.3.0
    Dezember 2011  : Xantorix 0.4.0

**Xantorix 0.3.0:**  
Die Version 0.3.0 stellt nur einen Zwischenschritt in der Entwicklung zur Version 0.4.0 dar und hat das Hauptziel, die Kernelfunktionen und Treiber stabil laufen zu lassen und einige der 0.4.0-Features teilweise und/oder als Beta-Module nachladen zu können. Da der Zeitpunkt des Releases fest ist, können die unten angegebenen Features nur als Schätzung angegeben werden.  

- Neue Dateisystemverwaltung
- verbesserte Benutzerrechte
- Multiprocessor Unterstützung ([SMP](https://github.com/lowlevel-eu/wiki/wiki/Symmetrisches-Multiprozessorsystem "SMP"))
- [IDE](https://github.com/lowlevel-eu/wiki/wiki/AT-Attachment "IDE") und AHCI (S-ATA) Treiber für ATA/ATAPI Laufwerke
- CDFS, FAT (lesend und schreibend), [ext2](https://github.com/lowlevel-eu/wiki/wiki/Ext2 "Ext2") (nur lesend)
- Einfacher Grafikmodus ohne richtigen Desktop
- Speicherverwaltung mit [PAE](https://github.com/lowlevel-eu/wiki/wiki/Physical-Address-Extension "PAE") und PSE
- Erste Netzwerkimplementierung mit DNS, IPv4, TCP und UDP
- Netzwerkkartentreiber: [RTL8139](https://github.com/lowlevel-eu/wiki/wiki/RTL8139 "RTL8139"), [PCnet](https://github.com/lowlevel-eu/wiki/wiki/AMD-PCnet "PCnet") (PCI)

**Xantorix 0.4.0:**

- Xantorix GUI mit Desktop und grafischen Anwendungen
- Stabiles Netzwerk mit DNS, IPv4, TCP, UDP, DHCP
- Netzwerkkartentreiber: [RTL8169](https://github.com/lowlevel-eu/wiki/wiki/RTL8169 "RTL8169"), e1000
- Evtl. eine einfache [CDI](https://github.com/lowlevel-eu/wiki/wiki/Common-Driver-Interface "CDI") Implementierung
- Zusätzliches ausführbares Binärformat: [ELF](https://github.com/lowlevel-eu/wiki/wiki/Executable-and-Linking-Format "ELF")
- ext2/3/4 (lesend und schreibend)
- Programme: u.a. einfacher Internet Browser, E-Mail Client, portierter Compiler

## Offizielle Webseite

[Xantorix Projekt-Webseite](http://www.xantorix.de/)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/10069/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1453/index.html)

<!-- MediaWiki page 1453; revision 10069; parent 9744; 2011-08-20T20:47:49Z -->
