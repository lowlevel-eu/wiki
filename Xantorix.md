# Xantorix

| Xantorix |  |
| ----------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
|  |  |
| Entwickler: | Homix |
| Akt. Version: | 0.1.2 |
| [Lizenz](https://github.com/lowlevel-eu/wiki/wiki/Lizenzen "Lizenzen"): | Closed Source |
| OS-Eigenschaften |  |
| Plattform: | [x86](https://github.com/lowlevel-eu/wiki/wiki/X86 "X86"), [x86_64](https://github.com/lowlevel-eu/wiki/wiki/X86-64 "X64") |
| [Kernelart](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel"): | [Monolithischer Kernel](https://github.com/lowlevel-eu/wiki/wiki/Kernel#monolithischer-kernel "Monolithischer Kernel") |
| [Sprache](https://lowlevel-eu.github.io/wiki/pages/1648/index.html "Kategorie:Programmiersprache"): | [Pascal](https://github.com/lowlevel-eu/wiki/wiki/Pascal "Pascal") |
| API: | XixAPI |
| Binärformat: | [PE](https://github.com/lowlevel-eu/wiki/wiki/Microsoft-Portable-Executable-and-Common-Object-File-Format "PE") |
| [IPC-Methode](https://github.com/lowlevel-eu/wiki/wiki/Interprozesskommunikation "IPC"): | \- |
| Homepage |  |

[www.xantorix.de](http://www.xantorix.de)

  
**Xantorix** (früher *HomixOS*) ist ein kleines [Betriebssystem](https://github.com/lowlevel-eu/wiki/wiki/Betriebssystem "Betriebssystem"), das vollständig in [Assembler](https://github.com/lowlevel-eu/wiki/wiki/Assembler "Assembler") ([Bootloader](https://github.com/lowlevel-eu/wiki/wiki/Bootloader "Bootloader")) und [Pascal](https://github.com/lowlevel-eu/wiki/wiki/Pascal "Pascal") ([Kernel](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel"), Anwendungen) programmiert wird. Das Betriebssystem ist modular aufgebaut, daher ist es möglich einfach und bequem verschiedene Module oder Treiber zur Laufzeit hinzuzufügen oder zu entfernen. Der Kernel unterstützt alle modernen Technologien wie Protected-Mode, [Multitasking](https://github.com/lowlevel-eu/wiki/wiki/Multitasking "Multitasking") und [Paging](https://github.com/lowlevel-eu/wiki/wiki/Paging "Paging"). Das Betriebssystem steht derzeit noch am Anfang der Entwicklung und ist daher noch nicht für die dauerhafte Verwendung geeignet. Neben der 32-Bit Variante existiert seit neuestem auch eine noch nicht ausführlich getestete 64-Bit Version.

Den Verlauf und Fortschritt der Entwicklung und die Roadmap kann man auf der offiziellen Webseite betrachten. Dort findet man auch Screenshots aktueller Versionen.

## Features

Einen Überblick über die bereits integrierten, der sich in Entwicklung befindlichen oder erst geplanten Features finden sie auf der [offiziellen Webseite](http://www.xantorix.de/features.php).

## Versionen

Überblick der verschiedenen Versionen seit Umbenennung:

    20.12.2008 : Xantorix 0.1.2

Die Veränderungen bei den verschiedenen Versionen:

**Xantorix 0.1.2:**

- Multiboot-kompatibler Kernel
- 32-Bit ProtectedMode Kernel
- 64-Bit LongMode Kernel
- Multitasking (Prozesse und Threads)
- moderne Speicherverwaltung (Paging)
- Benutzerverwaltung
- Exception-Handling
- Diskettenlaufwerkstreiber
- FAT-Dateisystemtreiber
- Tastaturtreiber
- PE-Unterstützung
- Shell
- Texteditor

## Roadmap

Folgende Versionen sind geplant:

    Ende Dezember 2009   : Xantorix 0.2.0

Die Features der kommenden Versionen:

**Xantorix 0.2.0:**

- erweiterte Benutzerverwaltung
- Paketverwaltung (Xantorix Package Manager)
- neue virtuelle Speicherverwaltung
- System-Datenbank für Systemeinstellungen (Sysdb)
- Unterstützung für mehrere Sprachen (Deutsch, Englisch)
- VM86-Mode Unterstützung (für 32-Bit Version)
- ATA Treiber für Festplatten (PIO, LBA28/LBA48)
- ATAPI Treiber für CD/DVD Laufwerke (PIO)
- CDFS Dateisystemtreiber (ISO9660, Rockridge, Joliet)
- Erweiterter FAT Dateisystemtreiber (FAT32 Unterstützung)
- VDisk: Virtuelle Laufwerke (Diskette, CD/DVD, Festplatte, Ramdisk)
- Verbesserte Shell mit deutlich mehr Befehlen

## Offizielle Webseite

[Xantorix Projekt-Webseite](http://www.xantorix.de/)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/6468/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1453/index.html)

<!-- MediaWiki page 1453; revision 6468; parent 6467; 2009-12-04T22:58:11Z -->
