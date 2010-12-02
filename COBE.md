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

Der Kernel von COBE verfolgt den Ansatz eines Mikrokernels. Dabei ist derzeit das System-nötigste im Kernel enthalten. Der Kernel von COBE beinhaltet System-Calls, welche über den Interrupt 0x30 erreichbar sind, eine genaue Dokumentation der System-Calls ist in Kürze auf der Projekt-Seite verfügbar.

## Versionen

**COBE 0.1 Alpha:**

- Grundinitialisierung von COBE
- GRUB
- Bootscreen
- GDT
- IDT, ISR
- PIC Remap
- Keyboard-Treiber
- stabiler Kernel
- [Shell](https://github.com/lowlevel-eu/wiki/wiki/Shell "Shell")
- [CMOS](https://github.com/lowlevel-eu/wiki/wiki/CMOS "CMOS")
- [Multitasking](https://github.com/lowlevel-eu/wiki/wiki/Multitasking "Multitasking")
- [FDC](https://github.com/lowlevel-eu/wiki/wiki/Floppy-Disk-Controller "FDC")
- [Paging](https://github.com/lowlevel-eu/wiki/wiki/Paging "Paging")
- Speicherverwaltung
- ELF-Programme
- System-Calls

## Geplant

**COBE 0.2:**

noch in Planung

## Sourcecode

COBE steht unter der BSD-Lizenz, der Sourcecode ist [hier herunterladbar](http://cobe.svn.sourceforge.net/viewvc/cobe/?view=tar).

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/9035/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2298/index.html)

<!-- MediaWiki page 2298; revision 9035; parent 9034; 2010-12-02T17:05:43Z -->
