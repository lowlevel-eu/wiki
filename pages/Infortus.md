# Infortus

| Infortus (InfoOS) |  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| [<img src="assets/Infortus.png" width="256" height="256" alt="Infortus.png" />](assets/Infortus.png) |  |
| Entwickler: | Sebi2020 |
| Akt. Version: | 0.0.09 prealpha |
| [Lizenz](Lizenzen "Lizenzen"): | [GPL](Lizenzen "GPL") |
| OS-Eigenschaften |  |
| Plattform: | [x86](X86 "X86") |
| [Kernelart](Kernel "Kernel"): | [Makrokernel](Kernel#makrokernel "Makrokernel") |
| [Sprache](Kategorie-Programmiersprache "Kategorie:Programmiersprache"): | [C](C "C") [Assembler](Assembler "Assembler") |
| API: | \- |
| Binärformat: |  |
| [IPC-Methode](Interprozesskommunikation "IPC"): | \- |
| Homepage |  |

<http://infortus-os.sourceforge.net/>

Infortus ist mein Betriebssystem (abgeleitet von [Informatikonline.net](http://www.Informatikonline.net)). Es baut auf einen [Makrokernel](Kernel#makrokernel "Makrokernel") auf und ist weitgehend in C geschrieben. Spezielle Aufgaben sind in Assembly ausgelagert worden (unter anderem bestimmte Treiber.). Es ist für x86 Systeme (also 32Bit) ausgelegt. Es arbeitet mit dem [Elf](Executable-and-Linking-Format "ELF32") Datei-Format.

## Planung

Erstes Minor Release (0.1.0) 2010 - 2011

Bis dahin Hoffe ich Keyboard-Treiber und eventuell einen CD-Treiber mit [ISO9660](ISO9660 "ISO9660")-Unterstützung Implementiert zu haben.

## Phase

- GDT, IDT, PIC etc...
  - GDT
  - IDT
  - Interrupts
  - Timer
  - rudimentäres Multitasking
  - Verbesserung des Multitasking/Neuschreiben
  - Rudimentäre Speicherverwaltung
  - *Paging*
- **Modul & ELF-Loader**
- Implementierung des Keyboard-Treibers
- Implementierung des CD-Treibers
- Implementierung von ISO9660

## Tests

Erfolgreich getestet Version 0.00.08:  
**Emulatoren/Virtualisierung:** Vmware, Bochs, Oracle Virtual Box, qemu  
**Computer:**  

- Fujitsu Siemens Amilo Reihe, Intel Celeron M CPU, 448 MB RAM,
- Medion, 2,6 GHz Intel Quad Core CPU, 2GB RAM
- Medion, 1,6 GHz Intel Pentium 4 CPU, 256 MB RAM
- Dell, 2,4 GHz Intel Core i5 CPU, 4GB RAM

## Download

Dies ist der Downloadlink zu einer Zip-Datei, die ein CD ISO-Image enthält:  
Aktuelle Version 0.00.09-prealpha:  
<http://sourceforge.net/projects/infortus-os/>

Die Sourcefiles findet man unter:  
<http://infortus-os.svn.sourceforge.net/viewvc/infortus-os/>

## Links

- [Infortus Seite bei Ohloh.net](http://www.ohloh.net/p/infortus-os)
- [Bugtracker](http://sourceforge.net/tracker/?group_id=293332&atid=1239537)
- [Datenblatt Kernel](http://infortus-os.sourceforge.net/downloads/datasheet-core.pdf)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/9884/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2117/index.html)

<!-- MediaWiki page 2117; revision 9884; parent 9632; 2011-06-26T23:06:18Z -->
