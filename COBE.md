# COBE

| COBE |  |
| ----------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
|  |  |
| Entwickler: | [Christian Hülsemeyer](https://lowlevel-eu.github.io/wiki/pages/2299/index.html "Benutzer:ChiSaw") |
| Akt. Version: | 0.1 Alpha |
| [Lizenz](Lizenzen "Lizenzen"): | [BSD](Lizenzen#bsd-lizenz "Lizenz") |
| OS-Eigenschaften |  |
| Plattform: | [x86](X86 "X86") |
| [Kernelart](Kernel "Kernel"): | [Microkernel](Kernel#mikrokernel "Microkernel") |
| [Sprache](https://lowlevel-eu.github.io/wiki/pages/1648/index.html "Kategorie:Programmiersprache"): | [C](C "C"), [Assembler](Assembler "Assembler") |
| API: | Noch keine vorhanden |
| Binärformat: | [ELF](Executable-and-Linking-Format "ELF") |
| [IPC-Methode](Interprozesskommunikation "IPC"): | Noch keine |
| Homepage |  |

<http://chisaw.de/?page_id=17>

  
COBE (Computer Betriebsystem) ist ein System mit Ziel eines [Microkernels](Kernel "Kernel"). Derzeit ist das System in den Sprachen [C](C "C") und [Assembler](Assembler "Assembler") geschrieben. Entwickelt wird es von Christian Hülsemeyer. Das Image des ersten Releases ist auf der Projektseite zu finden.

## Aufbau

COBE besteht aus folgenden Elementen:

- COBE besteht aus dem Kernel, da das System nun GRUB als Bootloader benutzt.
- Eine [Shell](Shell "Shell") sorgt für die Kommunikation zum Benutzer. Derzeit werden an relevanten Befehlen nur folgende überstützt: *help*, *cd*, *dir*, *mkdir*, *del*, *rechne*

## Kernel

Der Kernel von COBE verfolgt den Ansatz eines Mikrokernels. Dabei ist derzeit das System-nötigste im Kernel enthalten. Der Kernel von COBE beinhaltet System-Calls, welche über den Interrupt 0x30 erreichbar sind, eine genaue Dokumentation der System-Calls ist in Kürze auf der Projekt-Seite verfügbar.

## Versionen

**COBE 0.1 Alpha unstable:**

- Grundinitialisierung von COBE
- [GRUB](Grand-Unified-Bootloader "GRUB")
- Bootscreen (derzeit ausgeschaltet)
- [GDT](Global-Descriptor-Table "GDT")
- [IDT](Interrupt-Descriptor-Table "IDT"), ISR
- [PIC](Programmable-Interrupt-Controller "PIC") Remap
- [Keyboard-Treiber](Keyboard-Controller "KBC")
- Shell
- [CMOS](CMOS "CMOS")
- [Multitasking](Multitasking "Multitasking")
- [FDC](Floppy-Disk-Controller "FDC")
- [FAT12](File-Allocation-Table "FAT")
- [DMA](Direct-Memory-Access "DMA")
- [Paging](Paging "Paging")
- Speicherverwaltung
- System-Calls

## Geplant

**COBE 0.2:**

- [FAT32](File-Allocation-Table "FAT")
- [ATA](AT-Attachment "ATA")
- Dateistream
- C Library
- GUI-Demo
- mehr Syscalls

## Sourcecode

COBE steht unter der BSD-Lizenz, der Sourcecode ist [hier herunterladbar](http://cobe.svn.sourceforge.net/viewvc/cobe/?view=tar). Eine Dokumentation dieses Sourcecodes ist hier [einsehbar](http://chisaw.de/docs/kernel_doc/index.html)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/11258/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2298/index.html)

<!-- MediaWiki page 2298; revision 11258; parent 10355; 2015-01-30T09:32:15Z -->
