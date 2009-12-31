# Xantorix

| Xantorix |  |
| ----------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
|  |  |
| Entwickler: | Homix |
| Akt. Version: | 0.2.0 |
| [Lizenz](https://github.com/lowlevel-eu/wiki/wiki/Lizenzen "Lizenzen"): | Closed Source, Freeware |
| OS-Eigenschaften |  |
| Plattform: | [x86](https://github.com/lowlevel-eu/wiki/wiki/X86 "X86") (, [x86_64](https://github.com/lowlevel-eu/wiki/wiki/X86-64 "X64")) |
| [Kernelart](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel"): | [Monolithischer Kernel](https://github.com/lowlevel-eu/wiki/wiki/Kernel#monolithischer-kernel "Monolithischer Kernel") |
| [Sprache](https://lowlevel-eu.github.io/wiki/pages/1648/index.html "Kategorie:Programmiersprache"): | [Pascal](https://github.com/lowlevel-eu/wiki/wiki/Pascal "Pascal") |
| API: | XixAPI |
| Binärformat: | [PE](https://github.com/lowlevel-eu/wiki/wiki/Microsoft-Portable-Executable-and-Common-Object-File-Format "PE") |
| [IPC-Methode](https://github.com/lowlevel-eu/wiki/wiki/Interprozesskommunikation "IPC"): | \- |
| Homepage |  |

[www.xantorix.de](http://www.xantorix.de)

**Xantorix** ist ein kleines [Betriebssystem](https://github.com/lowlevel-eu/wiki/wiki/Betriebssystem "Betriebssystem"), welches vollständig in [Assembler](https://github.com/lowlevel-eu/wiki/wiki/Assembler "Assembler") ([Bootloader](https://github.com/lowlevel-eu/wiki/wiki/Bootloader "Bootloader")) und [Pascal](https://github.com/lowlevel-eu/wiki/wiki/Pascal "Pascal") ([Kernel](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel"), Anwendungen) programmiert wird. Der Kernel läuft ab einem Intel Pentium oder kompatiblen x86-Prozessor und unterstützt moderne Technologien wie [Protected Mode](https://github.com/lowlevel-eu/wiki/wiki/Protected-Mode "Protected Mode"), [Multitasking](https://github.com/lowlevel-eu/wiki/wiki/Multitasking "Multitasking") und [Paging](https://github.com/lowlevel-eu/wiki/wiki/Paging "Paging"). Außerdem ist eine kleine Benutzerverwaltung und eine Systemdatenbank zur Speicherung von System- und Treiberinformationen vorhanden. Treiber stehen derzeit für Disketten- und IDE-ATA/ATAPI Laufwerke (Festplatten und CD/DVD-ROM Laufwerke) zur Verfügung. Die bisher unterstützten Dateisysteme sind [FAT](https://github.com/lowlevel-eu/wiki/wiki/File-Allocation-Table "FAT") und CDFS ([ISO9660](https://github.com/lowlevel-eu/wiki/wiki/ISO9660 "ISO9660") mit RockRidge und Joliet Erweiterung). Das Betriebssystem steht derzeit noch am Anfang der Entwicklung und ist daher noch nicht für die dauerhafte Verwendung geeignet. Neben der 32-Bit-Variante existiert bei einigen Versionen auch eine 64-Bit-Version, die aufgrund der bis jetzt wenigen Vorteile nicht regelmäßig erscheint.

Den Verlauf und Fortschritt der Entwicklung sowie die Roadmap kann man auf der offiziellen Webseite betrachten. Dort findet man auch Screenshots aktueller Versionen.

## Features

Einen Überblick über die bereits integrierten, der sich in Entwicklung befindlichen oder erst geplanten Features findet man auf der [offiziellen Webseite](http://www.xantorix.de/features.php).

## Versionen

Überblick der verschiedenen Versionen seit Umbenennung:

    29.12.2009 : Xantorix 0.2.0
    20.12.2008 : Xantorix 0.1.2

Die Veränderungen bei den verschiedenen Versionen:

**Xantorix 0.2.0:**

- Booten von Diskette, Festplatte und CD/DVD-ROM (Live-CD)
- erweiterte Benutzerverwaltung
- System-Datenbank (Sysdb)
- Neue Konsole mit Scrolling-Funktion
- Verbesserte virtuelle Speicherverwaltung
- System- und Suchpfade
- ATA Treiber für Festplatten (PIO, LBA28/LBA48)
- ATAPI Treiber für CD/DVD Laufwerke (PIO)
- CDFS Dateisystemtreiber (ISO9660, Rockridge, Joliet)
- Auto-Mount für wechselbare Datenträger
- Verbesserte Shell mit deutlich mehr Befehlen

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

    Februar 2010    : Xantorix 0.2.1
    2. Quartal 2010 : Xantorix 0.2.2

Die Features der kommenden Versionen:

**Xantorix 0.2.1:**

- Verbesserte Laufwerks- und Dateiverwaltung
- Caching für Dateien
- DMA-Transfermodus für ATA/ATAPI Laufwerke
- Schreibzugriff auf ATA-Festplatten
- Partitionseditor

**Xantorix 0.2.2:**

- PAE Unterstützung für \>4GB Arbeitsspeicher
- Ext2 Dateisystemtreiber (read-only)
- VM86-Modus (16-Bit Emulation)
- Virtuelle Laufwerke

## Offizielle Webseite

[Xantorix Projekt-Webseite](http://www.xantorix.de/)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/6673/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1453/index.html)

<!-- MediaWiki page 1453; revision 6673; parent 6667; 2009-12-31T23:42:34Z -->
