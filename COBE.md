# COBE

| COBE |  |
| ----------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
|  |  |
| Entwickler: | [Christian Hülsemeyer](https://lowlevel-eu.github.io/wiki/pages/2299/index.html "Benutzer:ChiSaw") |
| Akt. Version: | 0.1 Alpha |
| [Lizenz](https://github.com/lowlevel-eu/wiki/wiki/Lizenzen "Lizenzen"): | BSD |
| OS-Eigenschaften |  |
| Plattform: | [x86](https://github.com/lowlevel-eu/wiki/wiki/X86 "X86") |
| [Kernelart](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel"): | [Monolith](https://github.com/lowlevel-eu/wiki/wiki/Kernel#monolithischer-kernel "Monolithischer Kernel") |
| [Sprache](https://lowlevel-eu.github.io/wiki/pages/1648/index.html "Kategorie:Programmiersprache"): | [C](https://github.com/lowlevel-eu/wiki/wiki/C "C") [Assembler](https://github.com/lowlevel-eu/wiki/wiki/Assembler "Assembler") |
| API: | Noch keine vorhanden |
| Binärformat: | [ELF](https://github.com/lowlevel-eu/wiki/wiki/Executable-and-Linking-Format "ELF") |
| [IPC-Methode](https://github.com/lowlevel-eu/wiki/wiki/Interprozesskommunikation "IPC"): | Noch keine |
| Homepage |  |

<http://cobe.sourceforge.net>

  
COBE (Computer Betriebsystem) ist ein System mit Ziel eines monolithischen [Kernels](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel"). Derzeit ist das System in den Sprachen [C](https://github.com/lowlevel-eu/wiki/wiki/C "C") und [Assembler](https://github.com/lowlevel-eu/wiki/wiki/Assembler "Assembler") geschrieben. Entwickelt wird es von Christian Hülsemeyer.

## Aufbau

COBE besteht aus folgenden Elementen:

- [Bootloader](https://github.com/lowlevel-eu/wiki/wiki/Bootloader "Bootloader"): Ein eigens geschriebener Bootloader, welcher zuerst den Sektor des Kernelloaders lädt und danach die Sektoren des eigentlichen Kernels. Der Bootloader springt danach in den Kernelloader.
- Kernelloader: Der Kernelloader ist dafür da, in den Protected Mode zu springen, die [GDT](https://github.com/lowlevel-eu/wiki/wiki/Global-Descriptor-Table "GDT") Tabelle zu erstellen und danach den eigentlichen Kernel zu laden.

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
- Shell
- CMOS implementieren
- Multitasking
- FDC
- Paging
- Speicherverwaltung
- ELF-Programme

## Geplant

**COBE 0.2:**

noch in Planung

## Sourcecode

COBE steht unter der BSD-Lizenz, der Sourcecode ist [hier herunterladbar](http://cobe.svn.sourceforge.net/viewvc/cobe/?view=tar).

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/8803/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2298/index.html)

<!-- MediaWiki page 2298; revision 8803; parent 8802; 2010-11-02T09:07:07Z -->
