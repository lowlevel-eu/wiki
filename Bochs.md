# Bochs

| Allgemeines |  |
| ------------------------ | ---------------------------- |
| Name: | Bochs |
| Entwickler: | The Bochs Project |
| Akt. Version: | 2.4<br>(Stand 03.05.2009) |
| Lizenz: | LGPL |
| Betriebssystem(e): | Linux, Windows, und andere |
| Virtualisiertes System |  |
| Plattform: | x86, x86-64 |
| SMP: | bis zu 8 Prozessoren |
| Mechanismus: | vollständige Emulation |
| Homepage |  |

<http://bochs.sourceforge.net/>

Bochs ist ein portabler [x86](https://github.com/lowlevel-eu/wiki/wiki/X86 "X86")- und [x86-64](https://github.com/lowlevel-eu/wiki/wiki/X86-64 "X86-64")-[Emulator](https://lowlevel-eu.github.io/wiki/pages/1938/index.html "Emulator"), der in C++ geschrieben ist. Da Bochs ein "reiner" Emulator ist, wird abgesehen von Tastatur, Maus, Grafikkarte, Festplatten, etc. auch der bzw. die Prozessoren vollständig emuliert und nicht Maschinencode teilweise auf dem Hostsystem ausgeführt. Das führt zum einen dazu, dass Bochs um Größenordnungen langsamer ist als beispielsweise Qemu oder [VMWare](https://github.com/lowlevel-eu/wiki/wiki/VMware "VMWare"), andererseits sind die [Debuggingmöglichkeiten](https://github.com/lowlevel-eu/wiki/wiki/Debugging "Debugging") von Bochs (im Bereich OSDev) um einiges besser.

## Emulierte Hardware

Bochs kann, abhängig davon mit welchen Parametern der Emulator kompiliert wurde, folgende Hardware emulieren:

- einen (oder mehrere) 386, 486, Pentium, Pentium Pro oder AMD64 Prozessor(en)
- Standardgeräte: [PIT](https://github.com/lowlevel-eu/wiki/wiki/Programmable-Interval-Timer "PIT"), [PIC](https://github.com/lowlevel-eu/wiki/wiki/Programmable-Interrupt-Controller "PIC"), [CMOS](https://github.com/lowlevel-eu/wiki/wiki/CMOS "CMOS"), [APIC](https://github.com/lowlevel-eu/wiki/wiki/Advanced-Programmable-Interrupt-Controller "APIC"), [I/O-APIC](https://github.com/lowlevel-eu/wiki/wiki/Advanced-Programmable-Interrupt-Controller "APIC"), [DMA](https://github.com/lowlevel-eu/wiki/wiki/Direct-Memory-Access "DMA")-Controller, serielle und parallele Schnittstelle
- NE2000 Netzwerkkarte
- PS/2 Maus und Tastatur
- CD-ROM Laufwerk
- Festplatte
- Diskettenlaufwerk
- Soundblaster 16
- eingeschränkte Unterstützung für eine Cirrus CLGD 5446 PCI VGA-Karte
- eingeschränkte Unterstützung von [USB](https://github.com/lowlevel-eu/wiki/wiki/Universal-Serial-Bus "USB")

## Siehe auch

- [Debugging](https://github.com/lowlevel-eu/wiki/wiki/Debugging "Debugging")

## Links

- [Bochs Homepage](http://bochs.sourceforge.net/)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/4354/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1538/index.html)

<!-- MediaWiki page 1538; revision 4354; parent 3818; 2009-05-03T20:39:41Z -->
