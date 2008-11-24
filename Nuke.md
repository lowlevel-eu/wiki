# Nuke

| Nuke |  |
| ----------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
|  |  |
| Entwickler: | [SHyx0rmZ](https://lowlevel-eu.github.io/wiki/pages/1785/index.html "Benutzer:SHyx0rmZ") |
| Akt. Version: | 00002 |
| [Lizenz](https://github.com/lowlevel-eu/wiki/wiki/Lizenzen "Lizenzen"): | *AVOL* |
| OS-Eigenschaften |  |
| Plattform: | x86 (x64 geplant) |
| [Kernelart](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel"): | Exokernel |
| [Sprache](https://lowlevel-eu.github.io/wiki/pages/1648/index.html "Kategorie:Programmiersprache"): | [Assembler](https://github.com/lowlevel-eu/wiki/wiki/Assembler "Assembler") |
| API: | *noch nicht vorhanden* |
| Binärformat: | *noch nicht vorhanden* (RAW?) |
| [IPC-Methode](https://github.com/lowlevel-eu/wiki/wiki/Interprozesskommunikation "IPC"): | *noch nicht vorhanden* |
| Homepage |  |

<http://nuke.asxsoft.de>

  
Nuke ist mein Hobby OS, welches im Protected Mode läuft. Hauptziel von Nuke ist es, dem Benutzer eine schnelle Arbeit am Computer zu gewährleisten.

## Entwickler

- [SHyx0rmZ](https://lowlevel-eu.github.io/wiki/pages/1785/index.html "Benutzer:SHyx0rmZ")

## Aktuelle Features

- Textausgabe
- Register Debugging
- 320x200x8 VGA

## Historie

Die Versionsnummer besteht aus 5 Hex-Ziffern. Sie kann im Bootsektor an Adresse 0x127 - 0x12B ausgelesen werden. *Kursiver Text* zeigt noch nicht implementierte Features an.

  
Ver 00002

- GDT wird geladen // Muss noch angepasst werden
- *IDT*
- *Exception Handling & IRQs*
- Protected Mode
- *FAT12*
- *NukeFS*

Ver 00001

- Werte der Register auslesbar
- VGA
- Kernel wird von Floppy gelesen

Ver 00000

- Bootloader gibt *Hallo Welt* aus und rebootet nach Tastendruck

## TODO

- Tastatur-Layout anpassen
- Dateisystem-Entwurf fertigstellen
- Festplatte beschreiben/lesen
- AMD Processor Optimization Module

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/3552/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1750/index.html)

<!-- MediaWiki page 1750; revision 3552; parent 3551; 2008-11-24T20:51:22Z -->
