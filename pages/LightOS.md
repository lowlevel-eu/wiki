# LightOS

| lightOS |  |
| ----------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
|  |  |
| Entwickler: | [bluecode](https://lowlevel-eu.github.io/wiki/pages/1489/index.html "Benutzer:Bluecode") |
| Akt. Version: | 0.2pre2 |
| [Lizenz](Lizenzen.md "Lizenzen"): | GNU GPL |
| OS-Eigenschaften |  |
| Plattform: | [x86](X86.md "X86"), [x86_64](X86-64.md "X64") |
| [Kernelart](Kernel.md "Kernel"): | Microkernel |
| [Sprache](Kategorie-Programmiersprache.md "Kategorie:Programmiersprache"): | [C++](C%2B%2B.md "C++") & teilweise [C](C.md "C") |
| API: | Nativ & teilweise [POSIX](POSIX.md "POSIX") |
| Binärformat: | [ELF](Executable-and-Linking-Format.md "ELF") |
| [IPC-Methode](Interprozesskommunikation.md "IPC"): | Message passing & shared-memory |
| Homepage |  |

<http://repo.or.cz/w/lightOS.git>

  
lightOS ist ein weiteres Betriebssystem für x86 und x86-64. Es basiert auf einem Microkernel. ~~Das Projekt wurde zugunsten von [Pedigree](Pedigree.md "Pedigree") eingestellt~~. Das Projekt wird seit Anfang 2009 wieder weiterentwickelt.

## Entwickler

- [bluecode](https://lowlevel-eu.github.io/wiki/pages/1489/index.html "Benutzer:Bluecode")

## Features

Im Moment sind die folgenden Features implementiert:

- Microkernel
- x86 und x86-64
- Multitasking/-threading
- Shared libraries
- [IPC](Interprozesskommunikation.md "IPC"): Messages, Shared-Memory
- [SMP](Symmetrisches-Multiprozessorsystem.md "SMP")-kompatibles System wird erkannt und alle Prozessoren gestartet
- Netzwerkkartentreiber:
  - [AMD PCnet](AMD-PCnet.md "AMD PCnet")
  - [Realtek RTL8139](RTL8139.md "RTL8139")
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

Das Hauptziel ist es, einen möglichst performanten [Mikrokernel](Kernel.md "Kernel") mit Unterstützung für [SMP](Symmetrisches-Multiprozessorsystem.md "SMP")- und evtl. auch [NUMA](Non-Uniform-Memory-Architecture.md "NUMA")-Systemen zu entwickeln. Außerdem soll die [IPC](Interprozesskommunikation.md "IPC") so gestaltet werden, dass Prozesse, welche auf verschiedenen Computer laufen, ohne zusätzlichen Aufwand miteinander kommunizieren können.

# Links

- [Projektseite](http://repo.or.cz/w/lightOS.git)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/5574/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1454/index.html)

<!-- MediaWiki page 1454; revision 5574; parent 5303; 2009-08-11T16:32:34Z -->
