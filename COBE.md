# COBE

| COBE |  |
| ----------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
|  |  |
| Entwickler: | [Christian Hülsemeyer](https://lowlevel-eu.github.io/wiki/pages/2299/index.html "Benutzer:ChiSaw") |
| Akt. Version: | 0.1 Alpha |
| [Lizenz](https://github.com/lowlevel-eu/wiki/wiki/Lizenzen "Lizenzen"): | BSD |
| OS-Eigenschaften |  |
| Plattform: | [x86](https://github.com/lowlevel-eu/wiki/wiki/X86 "X86") |
| [Kernelart](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel"): | [Microkernel](https://github.com/lowlevel-eu/wiki/wiki/Kernel#mikrokernel "Microkernel") |
| [Sprache](https://lowlevel-eu.github.io/wiki/pages/1648/index.html "Kategorie:Programmiersprache"): | [C](https://github.com/lowlevel-eu/wiki/wiki/C "C") [Assembler](https://github.com/lowlevel-eu/wiki/wiki/Assembler "Assembler") |
| API: | Noch keine vorhanden |
| Binärformat: | [ELF](https://github.com/lowlevel-eu/wiki/wiki/Executable-and-Linking-Format "ELF") |
| [IPC-Methode](https://github.com/lowlevel-eu/wiki/wiki/Interprozesskommunikation "IPC"): | Noch keine |
| Homepage |  |

<http://cobe.sourceforge.net>

  
COBE (Computer Betriebsystem) ist ein System mit Ziel eines [Microkernels](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel"). Derzeit ist das System in den Sprachen [C](https://github.com/lowlevel-eu/wiki/wiki/C "C") und [Assembler](https://github.com/lowlevel-eu/wiki/wiki/Assembler "Assembler") geschrieben. Entwickelt wird es von Christian Hülsemeyer.

## Aufbau

COBE besteht aus folgenden Elementen:

- COBE besteht mittlerweile nur noch aus dem Kernel, da das System nun GRUB als Bootloader benutzt.

## Kernel

Der Kernel wird auf monolithischer Basis aufgebaut werden. Derzeit ist der Kernel in einem noch recht instabilem Zustand, jedoch ist zu erwarten, dass der Kernel bereits in der Version 0.2 wesentlich stabiler laufen wird. Die GDT ist bei COBE nicht im Kernel enthalten, sondern in dem Kernelloader, dafür ist aber bereits die [IDT](https://github.com/lowlevel-eu/wiki/wiki/Interrupt-Descriptor-Table "IDT"), [ISR](https://github.com/lowlevel-eu/wiki/wiki/Interrupt-Service-Routine "ISR"), und ein Remap der [PIC](https://github.com/lowlevel-eu/wiki/wiki/Programmable-Interrupt-Controller "PIC") im Kernel enthalten.

## Versionen

**COBE 0.1 Alpha:**

- Grundinitialisierung von COBE
- eigener Bootloader
- Bootscreen
- GDT
- IDT, ISR
- PIC Remap
- Keyboard-Treiber
- Mini-Shell im Kernel
- stabiler Kernel
- [Shell](https://github.com/lowlevel-eu/wiki/wiki/Shell "Shell")
- [CMOS](https://github.com/lowlevel-eu/wiki/wiki/CMOS "CMOS") implementieren
- [Multitasking](https://github.com/lowlevel-eu/wiki/wiki/Multitasking "Multitasking")
- [FDC](https://github.com/lowlevel-eu/wiki/wiki/Floppy-Disk-Controller "FDC")
- [Paging](https://github.com/lowlevel-eu/wiki/wiki/Paging "Paging")
- Speicherverwaltung
- ELF-Programme

## Geplant

**COBE 0.2:**

noch in Planung

## Sourcecode

COBE steht unter der BSD-Lizenz, der Sourcecode ist [hier herunterladbar](http://cobe.svn.sourceforge.net/viewvc/cobe/?view=tar).

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/8818/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2298/index.html)

<!-- MediaWiki page 2298; revision 8818; parent 8807; 2010-11-03T13:04:34Z -->
