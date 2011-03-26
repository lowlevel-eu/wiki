# Infortus

| Infortus (InfoOS) |  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| [<img src="https://raw.githubusercontent.com/wiki/lowlevel-eu/wiki/assets/62bf341e1dffc350b6ff.png" width="256" height="256" alt="Infortus.png" />](https://raw.githubusercontent.com/wiki/lowlevel-eu/wiki/assets/62bf341e1dffc350b6ff.png) |  |
| Entwickler: | Sebi2020 |
| Akt. Version: | 0.0.07 prealpha |
| [Lizenz](https://github.com/lowlevel-eu/wiki/wiki/Lizenzen "Lizenzen"): | [GPL](https://github.com/lowlevel-eu/wiki/wiki/Lizenzen "GPL") |
| OS-Eigenschaften |  |
| Plattform: | [x86](https://github.com/lowlevel-eu/wiki/wiki/X86 "X86") |
| [Kernelart](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel"): | [Makrokernel](https://github.com/lowlevel-eu/wiki/wiki/Kernel#makrokernel "Makrokernel") |
| [Sprache](https://lowlevel-eu.github.io/wiki/pages/1648/index.html "Kategorie:Programmiersprache"): | [C](https://github.com/lowlevel-eu/wiki/wiki/C "C") [Assembler](https://github.com/lowlevel-eu/wiki/wiki/Assembler "Assembler") |
| API: | \- |
| Binärformat: | [elf32](https://github.com/lowlevel-eu/wiki/wiki/Executable-and-Linking-Format "ELF32") |
| [IPC-Methode](https://github.com/lowlevel-eu/wiki/wiki/Interprozesskommunikation "IPC"): | \- |
| Homepage |  |

<http://infortus-os.sourceforge.net/>

Infortus ist mein Betriebssystem (abgeleitet von [Informatikonline.net](http://www.Informatikonline.net)). Es baut auf einen [Makrokernel](https://github.com/lowlevel-eu/wiki/wiki/Kernel#makrokernel "Makrokernel") auf und ist weitgehend in C geschrieben. Spezielle Aufgaben sind in Assembly ausgelagert worden (unter anderem bestimmte Treiber.). Es ist für x86 Systeme (also 32Bit) ausgelegt. Es arbeitet mit dem [Elf](https://github.com/lowlevel-eu/wiki/wiki/Executable-and-Linking-Format "ELF32") Datei-Format.

## Planung

Erstes Minor Release (0.1.0) 2010 - 2011

Bis dahin Hoffe ich Keyboard-Treiber und eventuell einen CD-Treiber mit [ISO9660](https://github.com/lowlevel-eu/wiki/wiki/ISO9660 "ISO9660")-Unterstützung Implementiert zu haben.

## Phase

- GDT, IDT, PIC etc...
  - GDT
  - IDT
  - Interrupts
  - Timer
  - rudimentäres Multitasking
  - Verbesserung des Multitasking/Neuschreiben
  - Rudimentäre Speicherverwaltung
  - **Paging**
- Modul & ELF-Loader
- Implementierung des Keyboard-Treibers
- Implementierung des CD-Treibers
- Implementierung von ISO9660

## Screenshots

Hier sehen sie Screenshots von Infortus (Codename: InfoOS)  
**Version: 0.00.01:**  
Grub:  
![InfoOS1.png](http://www.informatikonline.net/images/extern/InfoOS1.png)

  
Kernel  
![InfoOS2.png](http://www.informatikonline.net/images/extern/InfoOS2.png)

  
**Version 0.00.03 (preview)**  
Phase 1:  
![InfoOS3.png](http://www.informatikonline.net/images/extern/InfoOS3.png)

Phase 2:  
![InfoOS4.png](http://www.informatikonline.net/images/extern/InfoOS4.png)

## Tests

Erfolgreich getestet Version 0.00.02:  
**Emulatoren/Virtualisierung:** Vmware, Bochs, Sun Virtual Box  
**Computer:**  

- Fujitsu Siemens Amilo Reihe, Intel Celeron M CPU, 448 MB RAM,
- Medion, 2,6 GHz Intel Quad Core CPU, 2GB RAM
- Medion, 1,6 GHz Intel Pentium 4 CPU, 256 MB RAM

## Download

Dies ist der Downloadlink zu einer Zip-Datei, die ein CD ISO-Image enthält:  
Aktuelle Version 0.00.07-prealpha:  
<http://sourceforge.net/projects/infortus-os/files/binary/prelapha-0-00-07/Infortus-x86-LiveCD%200-00-07%20prealpha.gz/download>

Die Sourcefiles findet man unter:  
<http://sourceforge.net/projects/infortus-os/files/source/prealpha-0-00-07/src-prealpha-0-00-07.zip/download>

## Bekannte Bugs

Beim Springen nach Phase 2 hängt das System manchmal. (festgestellt unter VBox)

## Links

- [Homepage](http://infortus-os.sourceforge.net)
- [Infortus Seite bei Ohloh.net](http://www.ohloh.net/p/infortus-os)
- [Bugtracker](http://sourceforge.net/tracker/?group_id=293332&atid=1239537)
- [Sourcecode](http://infortus-os.svn.sourceforge.net/viewvc/infortus-os/)
- [Datenblatt Kernel](http://infortus-os.sourceforge.net/downloads/datasheet-core.pdf)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/9632/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2117/index.html)

<!-- MediaWiki page 2117; revision 9632; parent 9631; 2011-03-26T16:02:24Z -->
