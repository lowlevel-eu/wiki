# Bochs

| Allgemeines |  |
| ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| Name: | Bochs |
| Entwickler: | The Bochs Project |
| Akt. Version: | 2.5.1 (06.01.2012) |
| Lizenz: | LGPL |
| Betriebssystem(e): | [Linux](https://github.com/lowlevel-eu/wiki/wiki/Linux "Linux"), [Windows](https://github.com/lowlevel-eu/wiki/wiki/Windows "Windows") und andere |
| Virtualisiertes System |  |
| Plattform: | [x86](https://github.com/lowlevel-eu/wiki/wiki/X86 "X86"), [x86-64](https://github.com/lowlevel-eu/wiki/wiki/X86-64 "X64") |
| SMP: | bis zu 8 Prozessoren |
| Mechanismus: | vollständige Emulation |
| Homepage |  |

<http://bochs.sourceforge.net/>

Bochs ist ein portabler [x86](https://github.com/lowlevel-eu/wiki/wiki/X86 "X86")- und [x86-64](https://github.com/lowlevel-eu/wiki/wiki/X86-64 "X86-64")-[Emulator](https://lowlevel-eu.github.io/wiki/pages/1938/index.html "Emulator"), der in [C++](https://github.com/lowlevel-eu/wiki/wiki/C%2B%2B "C++") geschrieben ist. Da Bochs ein „reiner“ Emulator ist, wird abgesehen von Tastatur, [Maus](https://github.com/lowlevel-eu/wiki/wiki/Maus "Maus"), Grafikkarte, Festplatten, etc. auch der bzw. die Prozessoren vollständig emuliert und nicht Maschinencode teilweise auf dem Hostsystem ausgeführt. Das führt zum einen dazu, dass Bochs um Größenordnungen langsamer ist als beispielsweise [QEMU](https://github.com/lowlevel-eu/wiki/wiki/QEMU "QEMU") oder [VMWare](https://github.com/lowlevel-eu/wiki/wiki/VMware "VMWare"), andererseits sind die [Debuggingmöglichkeiten](https://github.com/lowlevel-eu/wiki/wiki/Bochs-Debugger "Bochs Debugger") von Bochs (im Bereich OSDev) um einiges besser.

## Emulierte Hardware

Bochs kann, abhängig davon mit welchen Parametern der Emulator kompiliert wurde, folgende Hardware emulieren:

- einen (oder mehrere) 386-, 486-, Pentium-, Pentium-Pro- oder AMD64-Prozessor(en)
- Standardgeräte: [PIT](https://github.com/lowlevel-eu/wiki/wiki/Programmable-Interval-Timer "PIT"), [PIC](https://github.com/lowlevel-eu/wiki/wiki/Programmable-Interrupt-Controller "PIC"), [CMOS](https://github.com/lowlevel-eu/wiki/wiki/CMOS "CMOS"), [APIC](https://github.com/lowlevel-eu/wiki/wiki/Advanced-Programmable-Interrupt-Controller "APIC"), [I/O-APIC](https://github.com/lowlevel-eu/wiki/wiki/Advanced-Programmable-Interrupt-Controller "APIC"), [DMA](https://github.com/lowlevel-eu/wiki/wiki/Direct-Memory-Access "DMA")-Controller, serielle und parallele Schnittstelle
- NE2000-[Netzwerkkarte](https://lowlevel-eu.github.io/wiki/pages/1826/index.html "Kategorie:Netzwerkkarte")
- PS/2-Maus und -Tastatur
- CD-ROM-Laufwerk
- Festplatte
- [Diskettenlaufwerk](https://github.com/lowlevel-eu/wiki/wiki/Floppy-Disk-Controller "Floppy Disk Controller")
- [Soundblaster 16](https://lowlevel-eu.github.io/wiki/pages/1827/index.html "Kategorie:Soundkarte")
- eingeschränkte Unterstützung für eine [Cirrus CLGD 5446](https://github.com/lowlevel-eu/wiki/wiki/Cirrus-Logic "Cirrus Logic") PCI-VGA-Karte
- eingeschränkte Unterstützung von [USB](https://github.com/lowlevel-eu/wiki/wiki/Universal-Serial-Bus "USB")

## Siehe auch

- [Debugging](https://github.com/lowlevel-eu/wiki/wiki/Debugging "Debugging")

## Links

- [Bochs Homepage](http://bochs.sourceforge.net/)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/10671/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1538/index.html)

<!-- MediaWiki page 1538; revision 10671; parent 10665; 2012-08-11T20:46:52Z -->
