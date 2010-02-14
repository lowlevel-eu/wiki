# Nuke

| Nuke |  |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|  |  |
| Entwickler: | [SHyx0rmZ](https://lowlevel-eu.github.io/wiki/pages/1785/index.html "Benutzer:SHyx0rmZ") |
| Akt. Version: | kernel4-0.0.1 |
| [Lizenz](https://github.com/lowlevel-eu/wiki/wiki/Lizenzen "Lizenzen"): | [AVOL](http://avol.asxsoft.de) |
| OS-Eigenschaften |  |
| Plattform: | [x64](https://github.com/lowlevel-eu/wiki/wiki/X86-64 "X64") |
| [Kernelart](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel"): | Exokernel |
| [Sprache](https://lowlevel-eu.github.io/wiki/pages/1648/index.html "Kategorie:Programmiersprache"): | [Assembler](https://github.com/lowlevel-eu/wiki/wiki/Assembler "Assembler"),[C](https://github.com/lowlevel-eu/wiki/wiki/C "C"),[C++](https://github.com/lowlevel-eu/wiki/wiki/C%2B%2B "C++") |
| API: | *noch nicht vorhanden* |
| Binärformat: | *noch nicht vorhanden* (Vermutlich ELF?) |
| [IPC-Methode](https://github.com/lowlevel-eu/wiki/wiki/Interprozesskommunikation "IPC"): | *noch nicht vorhanden* |
| Homepage |  |

<http://nuke.asxsoft.de>

  
Nuke ist mein Hobby OS, welches im Long Mode läuft. Hauptziel von Nuke ist es, dem Benutzer eine schnelle Arbeit am Computer zu gewährleisten.

## Screenshot

[<img src="https://raw.githubusercontent.com/wiki/lowlevel-eu/wiki/assets/cd20ff76126c74c40341.png" width="720" height="400" alt="Nuke-0.4.png" />](https://raw.githubusercontent.com/wiki/lowlevel-eu/wiki/assets/cd20ff76126c74c40341.png)

## Aktuelle Features

- Textausgabe (mit Farbe)
- Vorhanden Arbeitsspeicher anzeigen

## Geplante Features

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

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/7077/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1750/index.html)

<!-- MediaWiki page 1750; revision 7077; parent 7075; 2010-02-14T23:48:34Z -->
