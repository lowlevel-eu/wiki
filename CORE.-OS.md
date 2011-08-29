# CORE.\\OS

**Achtung!**

**Die Homepage befindet sich in Arbeit, leider verzögert mein Privatleben die Fertigstellung drastisch! :(**  
**Trotzdem werde ich wenigstens versuchen regelmäßig den Artikel zu füllen und fertigzustellen.**  
**PS: CORE.\OS wird wahrscheinlich erst veröffentlicht, wenn es aus der Betaphase draußen ist! (Ich hab ja nicht mal die GUI richtig fertig...)**

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
| [IPC-Methode](https://github.com/lowlevel-eu/wiki/wiki/Interprozesskommunikation "IPC"): | Channels, RPC, XML-RPC |
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
  - Interprozesskommunikation
- Treiber:
  - Tastaturtreiber (PS/2 Tastaturen)
  - Diskettenlaufwerkstreiber
  - ATA/ATAPI Laufwerkstreiber (IDE-Festplatten und IDE-CD-ROM Laufwerke)
  - Dateisystemtreiber:
    - ext-Dateisystemtreiber (ext2, ext3)
    - FAT-Dateisystemtreiber (FAT12/FAT16/FAT32)
- Eigene Programme:
  - *coreTERMINAL* (Shell)
  - *coreTXT* (Texteditor)
- Andere:
  - CORE.\BOOT (Bootloader)

**Folgende Features sind noch nicht implementiert bzw. befinden sich noch in der Entwicklung:**

- Symmetrisches Multiprocessing
- Treiber:
  - Dateisystemtreiber:
    - *CORE.\FS*-Dateisytemtreiber (Da noch zu unausgereift.)
    - CDFS-Dateisystemtreiber (ISO9660, Joliet)
- Eigene Programme:
  - *corePACKAGE* (Paketmanager)
  - *coreSTUDIO* (Integrierte Entwicklungsumgebung mit *coreSCRIPT*)
  - *coreWEB* (Webbrowser)
- Andere:
  - *CORE.\WAVE* (Graphische Benutzeroberfläche)

**Über folgende Features wird nachgedacht:**

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

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/10097/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2365/index.html)

<!-- MediaWiki page 2365; revision 10097; parent 10096; 2011-08-29T21:38:22Z -->
