# I/O Ports

Als I/O Ports werden die Schnittstellen zwischen CPU und Peripheriegeräten bezeichnet. Die Kommunikation erfolgt über spezielle Maschinenbefehle, wie zum Beispiel *in* und *out*. Jedem Gerät wird dabei ein Bereich des I/O-Adressraums zugeordnet, und Lese- bzw. Schreibzugriffe werden an das Gerät weitergeleitet. In diesem Wiki werden als C-Funktionen *outb*, *outw* und entsprechende andere Varianten von in und out vorausgesetzt. Wie man diese Funktionen in C mit Hilfe von Inline-Assembler implementieren kann wird im Artikel [Inline-Assembler mit GCC](Inline-Assembler-mit-GCC.md "Inline-Assembler mit GCC") für den [GCC](GNU-Compiler-Collection.md "GCC") teilweise erklärt.

Ergänzend zur Port I/O existiert Memory Mapped I/O, bei dem die Geräte in den Adressraum des physischen Speichers eingeblendet werden. Das Gerät kann somit über normale Befehle zum Speicherzugriff angesteuert werden.

## Liste

Dies ist eine kleine Liste der Standard-I/O-Portbereiche eines [x86](X86.md "X86")/[x86-64](X86-64.md "X86-64")-Systems. Diese Liste ist nicht vollständig, da beispielsweise bei Geräten, die über den [PCI](Peripheral-Component-Interconnect.md "PCI")-Bus angeschlossen sind, die I/O Ports und die physischen Speicherbereiche nicht fix sind, sondern ausgelesen und konfiguriert werden können. Hier sind also vorwiegend Geräte aufgelistet, die aus der Zeit des [ISA](Industry-Standard-Architecture.md "ISA")/[EISA](Industry-Standard-Architecture.md#extended-industry-standard-architecture "EISA")-Busses stammen, als die I/O-Portbereiche für viele Geräte standardisiert wurden, da es im Allgemeinen keine Möglichkeit gab, diese Bereiche zur Laufzeit auszulesen bzw. zu konfigurieren.

| Beginn | Ende | Gerät |
| -------- | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0x000 | 0x01F | [DMA Controller](Direct-Memory-Access.md "Direct Memory Access") (8237A-5) |
| 0x020 | 0x021 | [Programmable Interrupt Controller](Programmable-Interrupt-Controller.md "Programmable Interrupt Controller") (PIC) |
| 0x040 | 0x043 | [Programmable Interval Timer](Programmable-Interval-Timer.md "Programmable Interval Timer") (PIT) |
| 0x060 | 0x060 | [Tastaturcontroller](Keyboard-Controller.md "Keyboard Controller") |
| 0x064 | 0x064 | [Tastaturcontroller](Keyboard-Controller.md "Keyboard Controller") |
| 0x070 | 0x071 | [CMOS](CMOS.md "CMOS") |
| 0x080 | 0x083 | [DMA Controller](Direct-Memory-Access.md "Direct Memory Access") (8237A-5) |
| 0x0A0 | 0x0AF | [PIC](Programmable-Interrupt-Controller.md "PIC") |
| 0x0C0 | 0x0CF | [DMA Controller](Direct-Memory-Access.md "Direct Memory Access") (8237A-5) |
| 0x0F0 | 0x0FF | [Nummerischer Koprozessor](Mathematischer-Koprozessor.md "Floating point unit") (FPU) |
| 0x170 | 0x177 | 2\. [Festplatten Controller](AT-Attachment.md "ATA") |
| 0x1F0 | 0x1F7 | 1\. [Festplatten Controller](AT-Attachment.md "ATA") |
| 0x278 | 0x27F | 2\. Parallel Port (3. mit MDA) |
| 0x2C0 | 0x2DF | 2\. EGA |
| 0x2E8 | 0x2EF | 4\. [RS232](Serielle-Schnittstelle.md "Serielle Schnittstelle") (COM-Port) |
| 0x2F8 | 0x2FF | 2\. [RS232](Serielle-Schnittstelle.md "Serielle Schnittstelle") (COM-Port) |
| 0x370 | 0x375 | 2\. [Diskettenlaufwerk Controller](Floppy-Disk-Controller.md "Floppy Disk Controller") |
| 0x376 | 0x377 | 2\. [Festplatten Controller](AT-Attachment.md "ATA") |
| 0x378 | 0x37F | 1\. Parallel Port |
| 0x3B0 | 0x3DF | [Video Graphics Array](Video-Graphics-Array.md "Video Graphics Array") (VGA) |
| 0x3C0 | 0x3CF | 1\. EGA |
| 0x3D0 | 0x3DF | CGA und EGA/[VGA](Video-Graphics-Array.md "Video Graphics Array") |
| 0x3E8 | 0x3EF | 3\. [RS232](Serielle-Schnittstelle.md "Serielle Schnittstelle") (COM-Port) |
| 0x3F0 | 0x3F5 | 1\. [Diskettenlaufwerk Controller](Floppy-Disk-Controller.md "Floppy Disk Controller") |
| 0x3F6 | 0x3F7 | 1\. [Festplatten Controller](AT-Attachment.md "ATA") |
| 0x3F8 | 0x3FF | 1\. [RS232](Serielle-Schnittstelle.md "Serielle Schnittstelle") (COM-Port) |
| 0xCF8 | 0xCFB | [PCI](Peripheral-Component-Interconnect.md "PCI") Configuration Address |
| 0xCFC | 0xCFF | [PCI](Peripheral-Component-Interconnect.md "PCI") Configuration Data |

## Links

- *Ralf Brown's Interrupt List* (RBIL) ist nicht nur eine Liste aller erdenklichen Software-Interrupts, sondern bietet auch eine sehr große (!) Liste mit Port-Nummern und entsprechenden Beschreibungen. Die Liste ist ist in 3 Dateien aufgeteilt (PORTS.A, PORTS.B und PORTS.C). Diese Dateien findet man in folgendem Zip-Archiv: [inter61d.zip](http://www.cs.cmu.edu/~ralf/interrupt-list/inter61d.zip)

<!-- -->

- [Eine Liste der Universität Magdeburg](http://mudlist.eorbit.net/~adam/pickey/ports.html) (Letzte Aktualisierung 26.03.1995) Zwar veraltet, aber dafür recht übersichtlich.

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/10912/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1543/index.html)

<!-- MediaWiki page 1543; revision 10912; parent 9897; 2012-11-01T11:42:44Z -->
