# CORE.\\OS

| CORE.\OS |  |
| ----------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|  |  |
| Entwickler: | [MtheD](https://lowlevel-eu.github.io/wiki/pages/2347/index.html "Benutzer:MtheD") |
| Akt. Version: | 1.4.2 Beta (Codename: "Nitro") |
| [Lizenz](https://github.com/lowlevel-eu/wiki/wiki/Lizenzen "Lizenzen"): | CORE.\LICENCE |
| OS-Eigenschaften |  |
| Plattform: | [x86](https://github.com/lowlevel-eu/wiki/wiki/X86 "X86"), [x64](https://github.com/lowlevel-eu/wiki/wiki/X86-64 "X64"), [ARM](https://github.com/lowlevel-eu/wiki/wiki/ARM "ARM") |
| [Kernelart](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel"): | Makrokernel |
| [Sprache](https://lowlevel-eu.github.io/wiki/pages/1648/index.html "Kategorie:Programmiersprache"): | [C++](https://github.com/lowlevel-eu/wiki/wiki/C%2B%2B "C++"), [Assembler](https://github.com/lowlevel-eu/wiki/wiki/Assembler "Assembler") |
| API: | CORE.\API |
| Binärformat: | [ELF](https://github.com/lowlevel-eu/wiki/wiki/Executable-and-Linking-Format "ELF"), EXE |
| [IPC-Methode](https://github.com/lowlevel-eu/wiki/wiki/Interprozesskommunikation "IPC"): | Channels, RPC |
| Homepage |  |

In Arbeit.

  
CORE.\OS ist ein [Betriebssystem](https://github.com/lowlevel-eu/wiki/wiki/Betriebssystem "Betriebssystem"), welches seit 2009 von [MtheD](https://lowlevel-eu.github.io/wiki/pages/2347/index.html "Benutzer:MtheD") entwickelt wird. Es befindet sich zur Zeit in einem frühen Stadium. Die Hauptziele von CORE.\OS sind, eine brauchbare Umgebung für Entwickler und Normalanwender bereitzustellen.

  

## Hintergrundstory

## Konzepte/Bedienung

## Features

**Folgende Features sind bereits implementiert:**

- *CORE.\KERNEL* (Kernel)
  - Präemptives Multitasking
  - Protected Mode
  - Paging
  - Physische Speicherverwaltung
- Treiber:
  - Tastaturtreiber (PS/2 Tastaturen)
  - Diskettenlaufwerkstreiber
  - Dateisystemtreiber:
    - ext-Dateisystemtreiber (ext2, ext3)
- Eigene Programme:
  - *coreTERMINAL* (Shell)
  - *coreTXT* (Texteditor)
- Andere:
  - CORE.\BOOT (Bootloader)

**Folgende Features sind noch nicht implementiert bzw. befinden sich noch in der Planung:**

- - Interprozesskommunikation
  - Symmetrisches Multiprocessing
- Treiber:
  - ATA/ATAPI Laufwerkstreiber (IDE-Festplatten und IDE-CD-ROM Laufwerke)
  - Dateisystemtreiber:
    - *CORE.\FS*-Dateisytemtreiber (Da noch zu unausgereift.)
    - FAT-Dateisystemtreiber (FAT12/FAT16/FAT32)
    - CDFS-Dateisystemtreiber (ISO9660, Joliet)
- Eigene Programme:
  - *corePACKAGE* (Paketmanager)
  - *coreSTUDIO* (Integrierte Entwicklungsumgebung mit *CORE.\SCRPT*)
  - *coreWEB* (Webbrowser)
- Andere:
  - *CORE.\WAVE* (Graphische Benutzeroberfläche)

**Über folgende Features wird nachgedacht, sie zu implementieren:**

- CDI-Integration

**Weiteres folgt...**

  

## Entwicklungsumgebung

- Hardware:
  - Intel® Core™ i7-980X: Extreme Edition @ 3,33 GHz
  - 8GB DDR3-SDRAM
  - nVidia GeForce GTX 580
  - 128GB SSD & 2TB HDD
- Software:
  - Microsoft® Windows® 7: Ultimate (64Bit)
  - Microsoft® VisualStudio™: Ultimate
  - Microsoft® Windows-Debugger x86/x64
  - FASM
  - Notepad++
  - Microsoft® VirtualPC 2007:SP1
  - Bochs
  - VMware® Workstation 7

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/10092/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2365/index.html)

<!-- MediaWiki page 2365; revision 10092; parent 10091; 2011-08-29T20:53:34Z -->
