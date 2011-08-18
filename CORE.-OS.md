# CORE.\\OS

| CORE.\OS |  |
| ----------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|  |  |
| Entwickler: | [MtheD](https://lowlevel-eu.github.io/wiki/pages/2347/index.html "Benutzer:MtheD") |
| Akt. Version: | 1.3 Beta (Sonderversion: 1.3.A3) |
| [Lizenz](https://github.com/lowlevel-eu/wiki/wiki/Lizenzen "Lizenzen"): | CORE.\LICENCE |
| OS-Eigenschaften |  |
| Plattform: | [x86](https://github.com/lowlevel-eu/wiki/wiki/X86 "X86"), [x64](https://github.com/lowlevel-eu/wiki/wiki/X86-64 "X64"), [ARM](https://github.com/lowlevel-eu/wiki/wiki/ARM "ARM") |
| [Kernelart](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel"): | Makrokernel |
| [Sprache](https://lowlevel-eu.github.io/wiki/pages/1648/index.html "Kategorie:Programmiersprache"): | [C++](https://github.com/lowlevel-eu/wiki/wiki/C%2B%2B "C++"), [Assembler](https://github.com/lowlevel-eu/wiki/wiki/Assembler "Assembler"), *CORE.\SCRPT* |
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

- *CORE.\KRNL* (Kernel)
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
  - *cTRMNL* (Shell)
  - *cTXT* (TextEditor)
- Andere:
  - CORE.\BOOT (Bootloader)

**Folgende Features sind noch nicht implementiert bzw. befinden sich noch in der Planung:**

- *CORE.\KRNL* (Kernel)
  - Interprozesskommunikation
  - Symmetrisches Multiprocessing
- Treiber:
  - ATA/ATAPI Laufwerkstreiber (IDE-Festplatten und IDE-CD-ROM Laufwerke)
  - Dateisystemtreiber:
    - *CORE.\FS*-Dateisytemtreiber (Da noch zu unausgereift.)
    - FAT-Dateisystemtreiber (FAT12/FAT16/FAT32)
    - CDFS-Dateisystemtreiber (ISO9660, Joliet)
- Eigene Programme:
  - *cPCKG* (Paketmanager)
  - *cSTUDIO* (Integrierte Entwicklungsumgebung mit *CORE.\SCRPT*)
  - *cWEB* (Webbrowser)
- Andere:
  - *CORE.\WAVE* (Graphische Benutzeroberfläche)

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

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/10065/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2365/index.html)

<!-- MediaWiki page 2365; revision 10065; parent 10052; 2011-08-18T20:13:58Z -->
