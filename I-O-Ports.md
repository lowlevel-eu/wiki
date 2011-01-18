# I/O Ports

Als I/O Ports werden die Schnittstellen zwischen CPU und Peripheriegeräten bezeichnet. Die Kommunikation erfolgt über spezielle Maschinenbefehle, wie zum Beispiel *in* und *out*. Jedem Gerät wird dabei ein Bereich des I/O-Adressraums zugeordnet, und Lese- bzw. Schreibzugriffe werden an das Gerät weitergeleitet. In diesem Wiki werden als C-Funktionen *outb*, *outw* und entsprechende andere Varianten von in und out vorausgesetzt. Wie man diese Funktionen in C mit Hilfe von Inline-Assembler implementieren kann wird im Artikel [Inline-Assembler mit GCC](https://github.com/lowlevel-eu/wiki/wiki/Inline-Assembler-mit-GCC "Inline-Assembler mit GCC") für den [GCC](https://github.com/lowlevel-eu/wiki/wiki/GNU-Compiler-Collection "GCC") teilweise erklärt.

Ergänzend zur Port I/O existiert Memory Mapped I/O, bei dem die Geräte in den Adressraum des physischen Speichers eingeblendet werden. Das Gerät kann somit über normale Befehle zum Speicherzugriff angesteuert werden.

## Liste

Dies ist eine kleine Liste der Standard-I/O-Portbereiche eines [x86](https://github.com/lowlevel-eu/wiki/wiki/X86 "X86")/[x86-64](https://github.com/lowlevel-eu/wiki/wiki/X86-64 "X86-64")-Systems. Diese Liste ist nicht vollständig, da beispielsweise bei Geräten, die über den [PCI](https://github.com/lowlevel-eu/wiki/wiki/Peripheral-Component-Interconnect "PCI")-Bus angeschlossen sind, die I/O Ports und die physischen Speicherbereiche nicht fix sind, sondern ausgelesen und konfiguriert werden können. Hier sind also Geräte aufgelistet, die aus der Zeit des [ISA](https://github.com/lowlevel-eu/wiki/wiki/Industry-Standard-Architecture "ISA")/[EISA](https://github.com/lowlevel-eu/wiki/wiki/Industry-Standard-Architecture#extended-industry-standard-architecture "EISA")-Busses stammen, als die I/O-Portbereiche für viele Geräte standardisiert wurden, da es im Allgemeinen keine Möglichkeit gab, diese Bereiche zur Laufzeit auszulesen bzw. zu konfigurieren.

| Begin | Ende | Gerät |
| ------- | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0x000 | 0x01F | [DMA Controller](https://github.com/lowlevel-eu/wiki/wiki/Direct-Memory-Access "Direct Memory Access") (8237A-5) |
| 0x020 | 0x021 | [Programmable Interrupt Controller](https://github.com/lowlevel-eu/wiki/wiki/Programmable-Interrupt-Controller "Programmable Interrupt Controller") (PIC) |
| 0x040 | 0x043 | [Programmable Interval Timer](https://github.com/lowlevel-eu/wiki/wiki/Programmable-Interval-Timer "Programmable Interval Timer") (PIT) |
| 0x060 | 0x060 | [Tastaturcontroller](https://github.com/lowlevel-eu/wiki/wiki/Keyboard-Controller "Keyboard Controller") |
| 0x064 | 0x064 | [Tastaturcontroller](https://github.com/lowlevel-eu/wiki/wiki/Keyboard-Controller "Keyboard Controller") |
| 0x070 | 0x071 | [CMOS](https://github.com/lowlevel-eu/wiki/wiki/CMOS "CMOS") |
| 0x080 | 0x083 | [DMA Controller](https://github.com/lowlevel-eu/wiki/wiki/Direct-Memory-Access "Direct Memory Access") (8237A-5) |
| 0x0A0 | 0x0AF | [PIC](https://github.com/lowlevel-eu/wiki/wiki/Programmable-Interrupt-Controller "PIC") |
| 0x0C0 | 0x0CF | [DMA Controller](https://github.com/lowlevel-eu/wiki/wiki/Direct-Memory-Access "Direct Memory Access") (8237A-5) |
| 0x0F0 | 0x0FF | [Nummerischer Koprozessor](https://github.com/lowlevel-eu/wiki/wiki/Mathematischer-Koprozessor "Floating point unit") (FPU) |
| 0x170 | 0x177 | 2\. [Festplatten Controller](https://github.com/lowlevel-eu/wiki/wiki/AT-Attachment "ATA") |
| 0x1F0 | 0x1F7 | 1\. [Festplatten Controller](https://github.com/lowlevel-eu/wiki/wiki/AT-Attachment "ATA") |
| 0x278 | 0x27F | 2\. Parallel Port (3. mit MDA) |
| 0x2C0 | 0x2DF | 2\. EGA |
| 0x2E8 | 0x2EF | 4\. [rs232](https://github.com/lowlevel-eu/wiki/wiki/Serielle-Schnittstelle "Rs232") (COM-Port) |
| 0x2F8 | 0x2FF | 2\. [rs232](https://github.com/lowlevel-eu/wiki/wiki/Serielle-Schnittstelle "Rs232") (COM-Port) |
| 0x370 | 0x375 | 2\. [Diskettenlaufwerk Controller](https://github.com/lowlevel-eu/wiki/wiki/Floppy-Disk-Controller "Floppy Disk Controller") |
| 0x376 | 0x377 | 2\. [Festplatten Controller](https://github.com/lowlevel-eu/wiki/wiki/AT-Attachment "ATA") |
| 0x378 | 0x37F | 1\. Parallel Port |
| 0x3B0 | 0x3DF | [Video Graphics Array](https://github.com/lowlevel-eu/wiki/wiki/Video-Graphics-Array "Video Graphics Array") (VGA) |
| 0x3C0 | 0x3CF | 1\. EGA |
| 0x3D0 | 0x3DF | CGA und EGA/[VGA](https://github.com/lowlevel-eu/wiki/wiki/Video-Graphics-Array "Video Graphics Array") |
| 0x3E8 | 0x3EF | 3\. [rs232](https://github.com/lowlevel-eu/wiki/wiki/Serielle-Schnittstelle "Rs232") (COM-Port) |
| 0x3F0 | 0x3F5 | 1\. [Diskettenlaufwerk Controller](https://github.com/lowlevel-eu/wiki/wiki/Floppy-Disk-Controller "Floppy Disk Controller") |
| 0x3F6 | 0x3F7 | 1\. [Festplatten Controller](https://github.com/lowlevel-eu/wiki/wiki/AT-Attachment "ATA") |
| 0x3F8 | 0x3FF | 1\. [rs232](https://github.com/lowlevel-eu/wiki/wiki/Serielle-Schnittstelle "Rs232") (COM-Port) |
| 0xCF8 | 0xCF8 | [PCI](https://github.com/lowlevel-eu/wiki/wiki/Peripheral-Component-Interconnect "PCI") |
| 0xCFC | 0xCFC | [PCI](https://github.com/lowlevel-eu/wiki/wiki/Peripheral-Component-Interconnect "PCI") |

## Links

- *Ralf Brown's Interrupt List* (RBIL) ist nicht nur eine Liste aller erdenklichen Software-Interrupts, sondern bietet auch eine sehr große (!) Liste mit Port-Nummern und entsprechenden Beschreibungen. Die Liste ist ist in 3 Dateien aufgeteilt (PORTS.A, PORTS.B und PORTS.C). Diese Dateien findet man in folgendem Zip-Archiv: [inter61d.zip](http://www.cs.cmu.edu/~ralf/interrupt-list/inter61d.zip)

<!-- -->

- [Eine Liste der Universität Magdeburg](http://mudlist.eorbit.net/~adam/pickey/ports.html) (Letzte Aktualisierung 26.03.1995) Zwar veraltet, aber dafür recht übersichtlich.

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/9348/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1543/index.html)

<!-- MediaWiki page 1543; revision 9348; parent 7362; 2011-01-18T16:34:13Z -->
