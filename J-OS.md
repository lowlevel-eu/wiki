# J-OS

**Löschhinweis:**

Dieser Artikel wurde zum Löschen vorgeschlagen.

Wird nicht mehr weiterentwickelt. ---[DerHartmut](https://lowlevel-eu.github.io/wiki/pages/1865/index.html "Benutzer:Hartmut") 10:36, 11. Feb. 2011 (CET)

| J-OS |  |
| ----------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
|  |  |
| Entwickler: | [jonebohne](https://lowlevel-eu.github.io/wiki/pages/2138/index.html "Benutzer:Jonebohne") |
| Akt. Version: | Noch keine (siehe unten) |
| [Lizenz](https://github.com/lowlevel-eu/wiki/wiki/Lizenzen "Lizenzen"): | [by-nc-sa 3.0](http://creativecommons.org/licenses/by-nc-sa/3.0/de/) |
| OS-Eigenschaften |  |
| Plattform: | [x86](https://github.com/lowlevel-eu/wiki/wiki/X86 "X86") |
| [Kernelart](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel"): | [Makrokernel](https://github.com/lowlevel-eu/wiki/wiki/Kernel#makrokernel "Makrokernel") |
| [Sprache](https://lowlevel-eu.github.io/wiki/pages/1648/index.html "Kategorie:Programmiersprache"): | [C](https://github.com/lowlevel-eu/wiki/wiki/C "C") |
| API: | [Syscall](https://github.com/lowlevel-eu/wiki/wiki/Syscall "Syscall")-Interface (geplant) |
| Binärformat: | (noch keins) |
| [IPC-Methode](https://github.com/lowlevel-eu/wiki/wiki/Interprozesskommunikation "IPC"): | Keine |
| Homepage |  |

Noch keine (siehe unten)

  
***J-OS wird nicht mehr weiterentwickelt. Stattdessen entwickle ich momentan an meinem neues OS: ExpOS. Grund: J-OS war nicht nur untestbar sondern auch unübersichtlich und bestand aus zusammengewürfeltem Nudelsalat-Code :-).***

J-OS ist ein (sehr) kleines [Betriebssystem](https://github.com/lowlevel-eu/wiki/wiki/Betriebssystem "Betriebssystem") von mir, welches ich hier etwas genauer beschreibe.

J-OS ist fast komplett in [C](https://github.com/lowlevel-eu/wiki/wiki/C "C") geschrieben (teilweise [Assembler](https://github.com/lowlevel-eu/wiki/wiki/Assembler "Assembler")) und bootet mit dem [GRUB](https://github.com/lowlevel-eu/wiki/wiki/Grand-Unified-Bootloader "GRUB")-Loader. Es läuft vollständig im [Protected Mode](https://github.com/lowlevel-eu/wiki/wiki/Protected-Mode "Protected Mode"). Geplant ist eine API, [Treiber](https://github.com/lowlevel-eu/wiki/wiki/Treiber "Treiber") für Festplatten/Disketten/CD-Laufwerke, Netzwerkkarten und vieles mehr.

## Changelog

#### Version 0.0.1 (wird geschrieben)

In der Version 0.0.1 werden (vorraussichtlich) folgende Features implementiert sein:

- Einrichtung einer [IDT](https://github.com/lowlevel-eu/wiki/wiki/Interrupt-Descriptor-Table "IDT") und einer [GDT](https://github.com/lowlevel-eu/wiki/wiki/Global-Descriptor-Table "GDT")
- Behandlung von [Exceptions](https://github.com/lowlevel-eu/wiki/wiki/Exception "Exception") und [ISRs](https://github.com/lowlevel-eu/wiki/wiki/Interrupt-Service-Routine "ISR")
- [Syscall](https://github.com/lowlevel-eu/wiki/wiki/Syscall "Syscall")-Interface
- [Multitasking](https://github.com/lowlevel-eu/wiki/wiki/Multitasking "Multitasking") in Ring 3
- [Paging](https://github.com/lowlevel-eu/wiki/wiki/Paging "Paging")
- Eine kleine [Shell](https://github.com/lowlevel-eu/wiki/wiki/Shell "Shell") (momentan eher eine *sehr* kleine Shell)
- [Debugging](https://github.com/lowlevel-eu/wiki/wiki/Debugging "Debugging") über den [COM](https://github.com/lowlevel-eu/wiki/wiki/Serielle-Schnittstelle "COM")-Port
- stdlibc (momentan nur teilweise)
- [Tastatur](https://github.com/lowlevel-eu/wiki/wiki/Tastatur "Tastatur")-[Treiber](https://github.com/lowlevel-eu/wiki/wiki/Treiber "Treiber")
- Treiber für [PCI](https://github.com/lowlevel-eu/wiki/wiki/Peripheral-Component-Interconnect "PCI") und evtl. Netzwerkkarten
- Vielleicht auch mehr

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/9521/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1828/index.html)

<!-- MediaWiki page 1828; revision 9521; parent 8033; 2011-02-11T09:36:14Z -->
