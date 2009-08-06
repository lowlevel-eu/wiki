# Nuke

| Nuke |  |
| ----------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
|  |  |
| Entwickler: | [SHyx0rmZ](https://lowlevel-eu.github.io/wiki/pages/1785/index.html "Benutzer:SHyx0rmZ") |
| Akt. Version: | 00003 |
| [Lizenz](https://github.com/lowlevel-eu/wiki/wiki/Lizenzen "Lizenzen"): | [AVOL](http://avol.asxsoft.de) |
| OS-Eigenschaften |  |
| Plattform: | [x64](https://github.com/lowlevel-eu/wiki/wiki/X86-64 "X64") |
| [Kernelart](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel"): | Exokernel |
| [Sprache](https://lowlevel-eu.github.io/wiki/pages/1648/index.html "Kategorie:Programmiersprache"): | [Assembler](https://github.com/lowlevel-eu/wiki/wiki/Assembler "Assembler") |
| API: | *noch nicht vorhanden* |
| Binärformat: | *noch nicht vorhanden* (RAW?) |
| [IPC-Methode](https://github.com/lowlevel-eu/wiki/wiki/Interprozesskommunikation "IPC"): | *noch nicht vorhanden* |
| Homepage |  |

<http://nuke.asxsoft.de>

  
Nuke ist mein Hobby OS, welches im Long Mode läuft. Hauptziel von Nuke ist es, dem Benutzer eine schnelle Arbeit am Computer zu gewährleisten.

## Entwickler

- [SHyx0rmZ](https://lowlevel-eu.github.io/wiki/pages/1785/index.html "Benutzer:SHyx0rmZ")

## Aktuelle Features

- Textausgabe (mit Farbe)
- Registerinhalte ausgeben
- 640x480x4 VGA
- Vorhanden Arbeitsspeicher anzeigen

## Geplante Features

- *NukeFS*
- *AVOP* (Interpreter-Sprache)
- *HAL-Lib*
- *angepasstes Tastatur-Layout*
- *Festplatte beschreiben/lesen* (RAW)
- *AMD Processor Optimization Module*

## Historie

Die Versionsnummer besteht aus 5 Hex-Ziffern. Sie kann im Bootsektor an Adresse 0x127 - 0x12B ausgelesen werden. (Nur für andere OS wichtig :D)

  
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

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/5288/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1750/index.html)

<!-- MediaWiki page 1750; revision 5288; parent 4614; 2009-08-06T15:31:04Z -->
