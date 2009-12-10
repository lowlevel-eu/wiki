# Infortus

| Inforatus (InfoOS) |  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| [<img src="https://raw.githubusercontent.com/wiki/lowlevel-eu/wiki/assets/62bf341e1dffc350b6ff.png" width="256" height="256" alt="Infortus.png" />](https://raw.githubusercontent.com/wiki/lowlevel-eu/wiki/assets/62bf341e1dffc350b6ff.png) |  |
| Entwickler: | Sebi2020 |
| Akt. Version: | 0.0.01 |
| [Lizenz](https://github.com/lowlevel-eu/wiki/wiki/Lizenzen "Lizenzen"): | [Creative Commons](http://creativecommons.org/licenses/by-nc-nd/3.0/de/) |
| OS-Eigenschaften |  |
| Plattform: | [x86](https://github.com/lowlevel-eu/wiki/wiki/X86 "X86") |
| [Kernelart](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel"): | [Makrokernel](https://github.com/lowlevel-eu/wiki/wiki/Kernel#makrokernel "Makrokernel") |
| [Sprache](https://lowlevel-eu.github.io/wiki/pages/1648/index.html "Kategorie:Programmiersprache"): | [C](https://github.com/lowlevel-eu/wiki/wiki/C "C") [Assembler](https://github.com/lowlevel-eu/wiki/wiki/Assembler "Assembler") |
| API: | \- |
| Binärformat: | [elf32](https://github.com/lowlevel-eu/wiki/wiki/Executable-and-Linking-Format "ELF32") |
| [IPC-Methode](https://github.com/lowlevel-eu/wiki/wiki/Interprozesskommunikation "IPC"): | \- |
| Homepage |  |

Keine

Infortus ist mein Betriebssystem (abgeleitet von [Informatikonline.net](http://www.Informatikonline.net)). Es baut auf einen [Makrokernel](https://github.com/lowlevel-eu/wiki/wiki/Kernel#makrokernel "Makrokernel") auf und ist weitgehend in C geschrieben. Spezielle Aufgaben sind in Assembly ausgelagert worden (unter anderem bestimmte Treiber.). Es ist für x86 Systeme (also 32Bit) ausgelegt. Es arbeitet mit dem [Elf](https://github.com/lowlevel-eu/wiki/wiki/Executable-and-Linking-Format "ELF32") Datei-Format.

## Planung

Erstes Minor Release (0.1.0) 2010 - 2011

Bis dahin Hoffe ich Keyboard-Treiber und eventuell einen CD-Treiber mit [ISO9660](https://github.com/lowlevel-eu/wiki/wiki/ISO9660 "ISO9660")-Unterstützung Implementiert zu haben.

## Phase

- **Implementierung des Keyboard-Treibers**
- Implementierung des CD-Treibers
- Implementierung von ISO9660

## Screenshots

Hier sehen sie Screenshots von Infortus (Codename: InfoOS)

Grub:  
![InfoOS1.png](http://www.informatikonline.net/images/extern/InfoOS1.png)

  
Kernel  
![InfoOS2.png](http://www.informatikonline.net/images/extern/InfoOS2.png)

## Bugs

Bisher ist beim Testen in KVM herausgekommen (taljeth hat es getestet), dass ein Triple Fault ausgelöst wurde. Im Moment weiß ich leider noch nicht woran es liegt und wäre für Hilfe dankbar. (Siehe Download)

Erfolgreich getestet:  
**Emulatoren/Virtualisierung:** Vmware, Bochs  
**Computer:**  

- Fujitsu Siemens Amilo Reihe, Intel Celeron M CPU, 448 MB RAM,
- Medion, 2,6 GHz Intel Quad Core CPU, 2GB RAM
- Medion, 1,6 GHz Intel Pentium 4 CPU, 256 MB RAM

Falls mir jemand Helfen möchte, und mir sagen kann, woran dieser Fehler liegt, kann er mir gerne eine PM im Forum an Sebi2020 schicken, oder einen Eintrag auf der Diskussionsseite von Infortus schreiben.

## Download

Dies ist der Downloadlink zu einer Zip-Datei, die ein CD ISO-Image enthält:  
Aktuelle Version 0.00.001:  
<http://dev.informatikonline.net/download.php?file=1>

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/6511/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2117/index.html)

<!-- MediaWiki page 2117; revision 6511; parent 6501; 2009-12-10T21:16:17Z -->
