# LightOS

| lightOS |  |
| ----------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
|  |  |
| Entwickler: | [bluecode](https://lowlevel-eu.github.io/wiki/pages/1489/index.html "Benutzer:Bluecode") |
| Akt. Version: | 0.2pre2 |
| [Lizenz](https://github.com/lowlevel-eu/wiki/wiki/Lizenzen "Lizenzen"): | GNU GPL |
| OS-Eigenschaften |  |
| Plattform: | i386, x86_64 |
| [Kernelart](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel"): | Microkernel |
| [Sprache](https://lowlevel-eu.github.io/wiki/pages/1648/index.html "Kategorie:Programmiersprache"): | [C++](https://github.com/lowlevel-eu/wiki/wiki/C%2B%2B "C++") & teilweise [C](https://github.com/lowlevel-eu/wiki/wiki/C "C") |
| API: | Nativ & teilweise [POSIX](https://github.com/lowlevel-eu/wiki/wiki/POSIX "POSIX") |
| Binärformat: | [ELF](https://github.com/lowlevel-eu/wiki/wiki/Executable-and-Linking-Format "ELF") |
| [IPC-Methode](https://github.com/lowlevel-eu/wiki/wiki/Interprozesskommunikation "IPC"): | Message passing & shared-memory |
| Homepage |  |

<http://repo.or.cz/w/lightOS.git>

  
lightOS ist ein weiteres Betriebssystem für x86 und x86-64. Es basiert auf einem Microkernel. ~~Das Projekt wurde zugunsten von [Pedigree](https://github.com/lowlevel-eu/wiki/wiki/Pedigree "Pedigree") eingestellt~~. Das Projekt wird seit Anfang 2009 wieder weiterentwickelt.

## Entwickler

- [bluecode](https://lowlevel-eu.github.io/wiki/pages/1489/index.html "Benutzer:Bluecode")

## Features

Im Moment sind die folgenden Features implementiert:

- Microkernel
- x86 und x86-64
- Multitasking/-threading
- Shared libraries
- [IPC](https://github.com/lowlevel-eu/wiki/wiki/Interprozesskommunikation "IPC"): Messages, Shared-Memory
- [SMP](https://github.com/lowlevel-eu/wiki/wiki/Symmetrisches-Multiprozessorsystem "SMP")-kompatibles System wird erkannt und alle Prozessoren gestartet
- Netzwerkkartentreiber:
  - [AMD PCnet](https://github.com/lowlevel-eu/wiki/wiki/AMD-PCnet "AMD PCnet")
  - [Realtek RTL8139](https://github.com/lowlevel-eu/wiki/wiki/RTL8139 "RTL8139")
- TCP/IP Stack: Ethernet, ARP, IP (teilweise), UDP, DNS, DHCP
- kleine Shell
- Portierte Anwendungen:
  - yasm 0.6.1
  - nano 2.0.6
  - nasm 0.99.02
  - binutils 2.18
- Portierte Bibliotheken:
  - zlib 1.2.3
  - libbzip2 1.0.4
  - freetype 2.3.5
  - libpng 1.2.20

## Ziele

Das Hauptziel ist es, einen möglichst performanten [Mikrokernel](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel") mit Unterstützung für [SMP](https://github.com/lowlevel-eu/wiki/wiki/Symmetrisches-Multiprozessorsystem "SMP")- und evtl. auch [NUMA](https://github.com/lowlevel-eu/wiki/wiki/Non-Uniform-Memory-Architecture "NUMA")-Systemen zu entwickeln. Außerdem soll die [IPC](https://github.com/lowlevel-eu/wiki/wiki/Interprozesskommunikation "IPC") so gestaltet werden, dass Prozesse, welche auf verschiedenen Computer laufen, ohne zusätzlichen Aufwand miteinander kommunizieren können.

# Links

- [Projektseite](http://repo.or.cz/w/lightOS.git)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/4285/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1454/index.html)

<!-- MediaWiki page 1454; revision 4285; parent 4207; 2009-04-13T08:44:31Z -->
