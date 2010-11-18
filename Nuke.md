# Nuke

| [GPLv3](https://github.com/lowlevel-eu/wiki/wiki/Lizenzen "GPL") |  |
| ----------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
|  |  |
| Entwickler: | [SHyx0rmZ](https://lowlevel-eu.github.io/wiki/pages/1785/index.html "Benutzer:SHyx0rmZ") |
| Akt. Version: | kernel5-0.0.1 |
| [Lizenz](https://github.com/lowlevel-eu/wiki/wiki/Lizenzen "Lizenzen"): | [AVOL](http://avol.asxsoft.de) |
| OS-Eigenschaften |  |
| Plattform: | [x64](https://github.com/lowlevel-eu/wiki/wiki/X86-64 "X64") |
| [Kernelart](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel"): | Exokernel |
| [Sprache](https://lowlevel-eu.github.io/wiki/pages/1648/index.html "Kategorie:Programmiersprache"): | [Assembler](https://github.com/lowlevel-eu/wiki/wiki/Assembler "Assembler"),[C](https://github.com/lowlevel-eu/wiki/wiki/C "C") |
| API: | *noch nicht vorhanden* |
| Binärformat: | [ELF](https://github.com/lowlevel-eu/wiki/wiki/Executable-and-Linking-Format "ELF") |
| [IPC-Methode](https://github.com/lowlevel-eu/wiki/wiki/Interprozesskommunikation "IPC"): | *noch nicht vorhanden* |
| Homepage |  |

zur Zeit keine

  
Nuke ist mein Hobby OS, welches ursprünglich mal nur im Long Mode laufen sollte. Jetzt gibt es Nuke aber auch für Leute ohne Long Mode CPU. Hauptziel von Nuke was es, dem Benutzer eine schnelle Arbeit am Computer zu gewährleisten. Nuke soll es nun einigermaßen schaffen, einen Exokernel umzusetzen. Inwieweit mir dies gelingt weiß ich allerdings selbst noch nicht abzuschätzen ^^

## Screenshot

[<img src="https://raw.githubusercontent.com/wiki/lowlevel-eu/wiki/assets/cd20ff76126c74c40341.png" width="720" height="400" alt="Nuke-0.4.png" />](https://raw.githubusercontent.com/wiki/lowlevel-eu/wiki/assets/cd20ff76126c74c40341.png) Dieser Screenshot zeigt noch kernel4, welcher nicht mehr in der Entwicklung befindlich ist

## Aktuelle Features

- SMP (zumindest fast fertig ^^)
- PMM
- Syscalls

## Die Zukunft

Genauere Pläne stehen noch nicht fest. Sicher ist aber, dass Nuke eine libPosix bekommen wird und auch einmal Linuxprogramme unterstützen soll. Zudem ist angedacht, [CDI](https://github.com/lowlevel-eu/wiki/wiki/Common-Driver-Interface "CDI") zu implementieren.

## Ehemals Geplante Features

- *NukeFS*
- *Initial Ramdisk*
- *AVOP* (Interpreter-Sprache)
- *HAL-Lib*
- *angepasstes Tastatur-Layout*
- *Festplatte beschreiben/lesen* (RAW)
- *AMD Processor Optimization Module*

## Historie

kernel4-0.0.1

- Paging
- Rudimentäres MM
- delete/delete\[\] und new/new\[\] (Funktioniert, solang Objekt kleinergleich Pagegröße)
- IRQ0-Handler alloziert zu Demonstrationszwecken Speicher

kernel4-0.0.0

- Neuester Rewrite, dazwischen liegen noch ein paar Versionen, kernel3 gab's sogar auch mal (glaub ich zumindest)
- Alles so weit wie möglich in C++0x
- Zielsetzung: Nuke endlich mal benutzbar bekommen und Neueinsteigern Resourcen bieten (Kommentare, UML-Diagramme, ...)

Ver **00004**

- Rudimentäre Speicherverwaltung
- Rudimentäres Paging
- Multitasking

Ver **00003**

- IDT & GDT für Long Mode
- Exceptions & IRQs werden durch einen Stub-Handler abgefangen
- Long Mode
- Arbeitsspeicher wird erkannt

  
Ver **00002**

- GDT wird geladen
- Protected Mode

  
Ver **00001**

- Werte der Register auslesbar
- VGA
- Kernel wird von Floppy gelesen

  
Ver **00000**

- Bootloader gibt *Hallo Welt* aus und rebootet nach Tastendruck

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/8908/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1750/index.html)

<!-- MediaWiki page 1750; revision 8908; parent 7077; 2010-11-18T15:21:57Z -->
