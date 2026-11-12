# J-OS

**Löschhinweis:**

Dieser Artikel wurde zum Löschen vorgeschlagen.

Wird nicht mehr weiterentwickelt. ---[DerHartmut](https://lowlevel-eu.github.io/wiki/pages/1865/index.html "Benutzer:Hartmut") 10:36, 11. Feb. 2011 (CET)

| J-OS |  |
| ----------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
|  |  |
| Entwickler: | [jonebohne](https://lowlevel-eu.github.io/wiki/pages/2138/index.html "Benutzer:Jonebohne") |
| Akt. Version: | Noch keine (siehe unten) |
| [Lizenz](Lizenzen.md "Lizenzen"): | [by-nc-sa 3.0](http://creativecommons.org/licenses/by-nc-sa/3.0/de/) |
| OS-Eigenschaften |  |
| Plattform: | [x86](X86.md "X86") |
| [Kernelart](Kernel.md "Kernel"): | [Makrokernel](Kernel.md#makrokernel "Makrokernel") |
| [Sprache](Kategorie-Programmiersprache.md "Kategorie:Programmiersprache"): | [C](C.md "C") |
| API: | [Syscall](Syscall.md "Syscall")-Interface (geplant) |
| Binärformat: | (noch keins) |
| [IPC-Methode](Interprozesskommunikation.md "IPC"): | Keine |
| Homepage |  |

Noch keine (siehe unten)

  
***J-OS wird nicht mehr weiterentwickelt. Stattdessen entwickle ich momentan an meinem neues OS: ExpOS. Grund: J-OS war nicht nur untestbar sondern auch unübersichtlich und bestand aus zusammengewürfeltem Nudelsalat-Code :-).***

J-OS ist ein (sehr) kleines [Betriebssystem](Betriebssystem.md "Betriebssystem") von mir, welches ich hier etwas genauer beschreibe.

J-OS ist fast komplett in [C](C.md "C") geschrieben (teilweise [Assembler](Assembler.md "Assembler")) und bootet mit dem [GRUB](Grand-Unified-Bootloader.md "GRUB")-Loader. Es läuft vollständig im [Protected Mode](Protected-Mode.md "Protected Mode"). Geplant ist eine API, [Treiber](Treiber.md "Treiber") für Festplatten/Disketten/CD-Laufwerke, Netzwerkkarten und vieles mehr.

## Changelog

#### Version 0.0.1 (wird geschrieben)

In der Version 0.0.1 werden (vorraussichtlich) folgende Features implementiert sein:

- Einrichtung einer [IDT](Interrupt-Descriptor-Table.md "IDT") und einer [GDT](Global-Descriptor-Table.md "GDT")
- Behandlung von [Exceptions](Exception.md "Exception") und [ISRs](Interrupt-Service-Routine.md "ISR")
- [Syscall](Syscall.md "Syscall")-Interface
- [Multitasking](Multitasking.md "Multitasking") in Ring 3
- [Paging](Paging.md "Paging")
- Eine kleine [Shell](Shell.md "Shell") (momentan eher eine *sehr* kleine Shell)
- [Debugging](Debugging.md "Debugging") über den [COM](Serielle-Schnittstelle.md "COM")-Port
- stdlibc (momentan nur teilweise)
- [Tastatur](Tastatur.md "Tastatur")-[Treiber](Treiber.md "Treiber")
- Treiber für [PCI](Peripheral-Component-Interconnect.md "PCI") und evtl. Netzwerkkarten
- Vielleicht auch mehr

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/9521/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1828/index.html)

<!-- MediaWiki page 1828; revision 9521; parent 8033; 2011-02-11T09:36:14Z -->
