# I/O Ports

Dies ist eine Liste der Standard I/O Portbereiche.

Diese Liste ist nicht vollständig!!!

## Liste

|  |  |  |
| ------- | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Begin | Ende | Gerät |
| 0x000 | 0x01F | [DMA Kontroller](https://github.com/lowlevel-eu/wiki/wiki/Direct-Memory-Access "Direct Memory Access") (8237A-5) |
| 0x020 | 0x021 | [Programmable Interrupt Controller](https://github.com/lowlevel-eu/wiki/wiki/Programmable-Interrupt-Controller "Programmable Interrupt Controller") (PIC) |
| 0x040 | 0x043 | [Programmable Interrupt Controller](https://github.com/lowlevel-eu/wiki/wiki/Programmable-Interrupt-Controller "Programmable Interrupt Controller") (PIC) |
| 0x060 | 0x063 | [Tastaturcontroller](https://github.com/lowlevel-eu/wiki/wiki/Keyboard-Controller "Keyboard Controller") |
| 0x070 | 0x071 | [CMOS](https://github.com/lowlevel-eu/wiki/wiki/CMOS "CMOS") |
| 0x080 | 0x083 | [DMA Kontroller](https://github.com/lowlevel-eu/wiki/wiki/Direct-Memory-Access "Direct Memory Access") (8237A-5) |
| 0x0A0 | 0x0AF | [PIC](https://github.com/lowlevel-eu/wiki/wiki/Programmable-Interrupt-Controller "PIC") |
| 0x0C0 | 0x0CF | [DMA Kontroller](https://github.com/lowlevel-eu/wiki/wiki/Direct-Memory-Access "Direct Memory Access") (8237A-5) |
| 0x0F0 | 0x0FF | [Nummerischer Koprozessor](https://github.com/lowlevel-eu/wiki/wiki/Mathematischer-Koprozessor "Floating point unit") (FPU) |
| 0x170 | 0x177 | 2\. [Festplatten Kontroller](https://github.com/lowlevel-eu/wiki/wiki/AT-Attachment "ATA") |
| 0x1F0 | 0x1F7 | 1\. [Festplatten Kontroller](https://github.com/lowlevel-eu/wiki/wiki/AT-Attachment "ATA") |
| 0x278 | 0x27F | 2\. Parallel Port (3. mit MDA) |
| 0x2C0 | 0x2DF | 2\. EGA |
| 0x2F8 | 0x2FF | 2\. [rs232](https://github.com/lowlevel-eu/wiki/wiki/Serielle-Schnittstelle "Rs232") (Comport) |
| 0x370 | 0x375 | 2\. [Diskettenlaufwerk Kontroller](https://github.com/lowlevel-eu/wiki/wiki/Floppy-Disk-Controller "Floppy Disk Controller") |
| 0x376 | 0x377 | 2\. [Festplatten Kontroller](https://github.com/lowlevel-eu/wiki/wiki/AT-Attachment "ATA") |
| 0x3B0 | 0x3DF | [Video Graphics Array](https://github.com/lowlevel-eu/wiki/wiki/Video-Graphics-Array "Video Graphics Array") (VGA) |
| 0x3C0 | 0x3CF | 1\. EGA |
| 0x3D0 | 0x3DF | CGA and EGA/VGA |
| 0x3F0 | 0x3F5 | 1\. [Diskettenlaufwerk Kontroller](https://github.com/lowlevel-eu/wiki/wiki/Floppy-Disk-Controller "Floppy Disk Controller") |
| 0x3F6 | 0x3F7 | 1\. [Festplattencontroller](https://github.com/lowlevel-eu/wiki/wiki/AT-Attachment "ATA") |
| 0x3F8 | 0x3FF | 1\. [rs232](https://github.com/lowlevel-eu/wiki/wiki/Serielle-Schnittstelle "Rs232") (Comport) |
| 0xCF8 | 0xCF8 | [PCI](https://github.com/lowlevel-eu/wiki/wiki/Peripheral-Component-Interconnect "PCI") |
| 0xCFC | 0xCFC | [PCI](https://github.com/lowlevel-eu/wiki/wiki/Peripheral-Component-Interconnect "PCI") |

## Links

- Ralf Brown's Interrupt List (RBIL) ist nicht nur eine Liste aller erdenklichen Software Interrupts, sondern bietet auch eine sehr große(!) Liste mit Port-Nummern und entsprechenden Beschreibungen. Die Liste ist ist in 3 Dateien aufgeteilt (PORTS.A, PORTS.B und PORTS.C). Diese Dateien findet man in folgendem Zip-Archiv: [inter61d.zip](http://www.cs.cmu.edu/~ralf/interrupt-list/inter61d.zip)

<!-- -->

- [Eine Liste der Universität Magdeburg](http://mudlist.eorbit.net/~adam/pickey/ports.html) (Letzte Aktualisierung 26.03.1995) Zwar veraltet, aber dafür recht übersichtlich.

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/2203/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1543/index.html)

<!-- MediaWiki page 1543; revision 2203; parent 2198; 2007-10-27T17:41:22Z -->
