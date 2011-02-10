# NightOS

| StefanOS |  |
| ----------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
|  |  |
| Entwickler: | [sfan](https://lowlevel-eu.github.io/wiki/pages/2378/index.html "Benutzer:Sfan") |
| Akt. Version: | 0.1 |
| [Lizenz](https://github.com/lowlevel-eu/wiki/wiki/Lizenzen "Lizenzen"): | [by-nc-sa 2.0](http://creativecommons.org/licenses/by-nc-sa/2.0/de/) |
| OS-Eigenschaften |  |
| Plattform: | [x86](https://github.com/lowlevel-eu/wiki/wiki/X86 "X86") |
| [Kernelart](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel"): | Monolithischer [Kernel](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel") |
| [Sprache](https://lowlevel-eu.github.io/wiki/pages/1648/index.html "Kategorie:Programmiersprache"): | [C](https://github.com/lowlevel-eu/wiki/wiki/C "C") [Assembler](https://github.com/lowlevel-eu/wiki/wiki/Assembler "Assembler") |
| API: | \- |
| Binärformat: | .bin und [ELF](https://github.com/lowlevel-eu/wiki/wiki/Executable-and-Linking-Format "ELF") |
| [IPC-Methode](https://github.com/lowlevel-eu/wiki/wiki/Interprozesskommunikation "IPC"): | \- |
| Homepage |  |

[Website](http://sfan.funpic.de/StefanOS.html)  
[Quellcode](http://sfan.funpic.de/StefanOS_source)  
[Image](http://sfan.funpic.de/StefanOS_source/StefanOS.img)

StefanOS hat die Aufgabe einen PC schnell und einfach zu benutzen. Das OS wird dafür (voraussichtlich) einen Dateisystemtreiber für [FAT](https://github.com/lowlevel-eu/wiki/wiki/File-Allocation-Table "FAT") im Kernel haben. Die Shell wird als .elf oder .bin Datei von GRUB geladen.

## Features

### 0.1

- [GDT](https://github.com/lowlevel-eu/wiki/wiki/Global-Descriptor-Table "GDT")/[IDT](https://github.com/lowlevel-eu/wiki/wiki/Interrupt-Descriptor-Table "IDT") wird geladen

### 0.1.1 (voraussichtlich)

- [GDT](https://github.com/lowlevel-eu/wiki/wiki/Global-Descriptor-Table "GDT")/[IDT](https://github.com/lowlevel-eu/wiki/wiki/Interrupt-Descriptor-Table "IDT") wird geladen
- Multitasking
- Tastaturtreiber
- kleine Shell
- Loader für Binaries
  - [ELF](https://github.com/lowlevel-eu/wiki/wiki/Executable-and-Linking-Format "ELF")
  - flache Binärdateien (.bin)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/9512/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2359/index.html)

<!-- MediaWiki page 2359; revision 9512; parent 9499; 2011-02-10T16:48:17Z -->
