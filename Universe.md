# Universe

| Universe |  |
| ----------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
|  |  |
| Entwickler: | Tdotu |
| Akt. Version: | 0.8 (in Entwicklung) |
| [Lizenz](https://github.com/lowlevel-eu/wiki/wiki/Lizenzen "Lizenzen"): | Closed-Source |
| OS-Eigenschaften |  |
| Plattform: | [x86](https://github.com/lowlevel-eu/wiki/wiki/X86 "X86") |
| [Kernelart](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel"): | Hybrid |
| [Sprache](https://lowlevel-eu.github.io/wiki/pages/1648/index.html "Kategorie:Programmiersprache"): | Assembler/C/C++ |
| API: | nativ |
| Binärformat: | UEF,[ELF](https://github.com/lowlevel-eu/wiki/wiki/Executable-and-Linking-Format "ELF") |
| [IPC-Methode](https://github.com/lowlevel-eu/wiki/wiki/Interprozesskommunikation "IPC"): | [Shared Memory](https://github.com/lowlevel-eu/wiki/wiki/Interprozesskommunikation#shared-memory "Shared Memory") |
| Homepage |  |

in Arbeit

  

  
Universe ist als benutzerfreundliches universelles Desktop-Betriebssystem geplant. Es soll später möglich sein auf Universe Linux und eventuell Windows Applikationen auszuführen. Dieses Ziel liegt jedoch noch in weiter Ferne. Aktuell handelt es sich um einen einfachen Hybrid-Kernel mit einem kleinen Treibersatz. Es wird seit 2009 entwickelt. Der Großteil der Universe-Versionen wurden für den [Real Mode](https://github.com/lowlevel-eu/wiki/wiki/Real-Mode "Real Mode") entwickelt erst ab Version 0.7 läuft das System im [Protected Mode](https://github.com/lowlevel-eu/wiki/wiki/Protected-Mode "Protected Mode").

## Ziele der Version 0.8

Teile dieser Ziele sind bereits umgesetzt, jedoch dauert die Fertigstellung der anderen Funktionen noch an.

- Graphische Benutzeroberfläche (GUI)
- Verbesserung der Speicherverwaltung ([Paging](https://github.com/lowlevel-eu/wiki/wiki/Paging "Paging"))
- verbessertes [Shared Memory](https://github.com/lowlevel-eu/wiki/wiki/Interprozesskommunikation#shared-memory "Shared Memory") IPC System
- Implememtierung von Linux [ELF](https://github.com/lowlevel-eu/wiki/wiki/Executable-and-Linking-Format "ELF") Dateien
- Implememtierung des [Common Driver Interface](https://github.com/lowlevel-eu/wiki/wiki/Common-Driver-Interface "Common Driver Interface")
- Treiber:
  - [Floppy](https://github.com/lowlevel-eu/wiki/wiki/Floppy-Disk-Controller "Floppy")
  - [Maus](https://github.com/lowlevel-eu/wiki/wiki/Maus "Maus")
  - [VESA](https://github.com/lowlevel-eu/wiki/wiki/Video-Electronics-Standards-Association "VESA")
  - [FAT](https://github.com/lowlevel-eu/wiki/wiki/File-Allocation-Table "FAT")

## Versionen

Bisher fertiggestellte Versionen:

| Version | Änderungen/Fähigkeiten |
| --------- | ---------------------------------------------------------------------------------------------------------- |
| 0.1 | Einfaches bootbares „Hello world!“ Programm mit eigenem Bootloader(nur ASM) |
| 0.2 | Textbasiertes Logo (nur ASM) |
| 0.3 | Erster Versuch mit C-Kernel(C/ASM) |
| 0.4 | Neustart- und Herunterfahrfunktionen (C/ASM) |
| 0.5 | Funktionsmenü (nur ASM) |
| 0.6 | Graphischer Editor mit Druckfunktion + Lade und Startfunktion für binäre Programme (nur ASM) |
| 0.7 | Erste Versuche mit dem Protected Mode und Vesa (Version wegen hoher Fehlerquote als gescheitert erklärt) |

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/10352/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2498/index.html)

<!-- MediaWiki page 2498; revision 10352; parent 0; 2011-12-07T14:04:29Z -->
