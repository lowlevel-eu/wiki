# Bochs

| Allgemeines |  |
| ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| Name: | Bochs |
| Entwickler: | The Bochs Project |
| Akt. Version: | 2.6 (02.09.2012) |
| Lizenz: | LGPL |
| Betriebssystem(e): | [Linux](Linux.md "Linux"), [Windows](Windows.md "Windows") und andere |
| Virtualisiertes System |  |
| Plattform: | [x86](X86.md "X86"), [x86-64](X86-64.md "X64") |
| SMP: | bis zu 8 Prozessoren |
| Mechanismus: | vollständige Emulation |
| Homepage |  |

<http://bochs.sourceforge.net/>

Bochs ist ein portabler [x86](X86.md "X86")- und [x86-64](X86-64.md "X86-64")-[Emulator](https://lowlevel-eu.github.io/wiki/pages/1938/index.html "Emulator"), der in [C++](C%2B%2B.md "C++") geschrieben ist. Da Bochs ein „reiner“ Emulator ist, wird abgesehen von Tastatur, [Maus](Maus.md "Maus"), Grafikkarte, Festplatten, etc. auch der bzw. die Prozessoren vollständig emuliert und nicht Maschinencode teilweise auf dem Hostsystem ausgeführt. Das führt zum einen dazu, dass Bochs um Größenordnungen langsamer ist als beispielsweise [QEMU](QEMU.md "QEMU") oder [VMWare](VMware.md "VMWare"), andererseits sind die [Debuggingmöglichkeiten](Bochs-Debugger.md "Bochs Debugger") von Bochs (im Bereich OSDev) um einiges besser.

## Emulierte Hardware

Bochs kann, abhängig davon mit welchen Parametern der Emulator kompiliert wurde, folgende Hardware emulieren:

- einen (oder mehrere) 386-, 486-, Pentium-, Pentium-Pro- oder AMD64-Prozessor(en)
- Standardgeräte: [PIT](Programmable-Interval-Timer.md "PIT"), [PIC](Programmable-Interrupt-Controller.md "PIC"), [CMOS](CMOS.md "CMOS"), [APIC](Advanced-Programmable-Interrupt-Controller.md "APIC"), [I/O-APIC](Advanced-Programmable-Interrupt-Controller.md "APIC"), [DMA](Direct-Memory-Access.md "DMA")-Controller, serielle und parallele Schnittstelle
- [Netzwerkkarten](Kategorie-Netzwerkkarte.md "Kategorie:Netzwerkkarte"): NE2000, Intel 82540EM (e1000)
- PS/2-Maus und -Tastatur
- CD-ROM-Laufwerk
- Festplatte
- [Diskettenlaufwerk](Floppy-Disk-Controller.md "Floppy Disk Controller")
- [Soundkarte](Kategorie-Soundkarte.md "Kategorie:Soundkarte"): Soundblaster 16, ES1370
- eingeschränkte Unterstützung für eine [Cirrus CLGD 5446](Cirrus-Logic.md "Cirrus Logic") PCI-VGA-Karte
- eingeschränkte Unterstützung von [USB](Universal-Serial-Bus.md "USB")

## Siehe auch

- [Debugging](Debugging.md "Debugging")

## Links

- [Bochs Homepage](http://bochs.sourceforge.net/)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/10897/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1538/index.html)

<!-- MediaWiki page 1538; revision 10897; parent 10896; 2012-09-30T23:57:21Z -->
