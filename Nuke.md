# Nuke

| Nuke |  |
| ----------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
|  |  |
| Entwickler: | [SHyx0rmZ](https://lowlevel-eu.github.io/wiki/pages/1785/index.html "Benutzer:SHyx0rmZ") |
| Akt. Version: | 00002 |
| [Lizenz](https://github.com/lowlevel-eu/wiki/wiki/Lizenzen "Lizenzen"): | [AVOL](http://avol.asxsoft.com) |
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
- 640x480x4 VGA

## Historie

Die Versionsnummer besteht aus 5 Hex-Ziffern. Sie kann im Bootsektor an Adresse 0x127 - 0x12B ausgelesen werden. *Kursiver Text* zeigt noch nicht implementierte Features an.

  
Ver 00002

- GDT wird geladen
- *IDT*
- *Exception Handling & IRQs* //Schreitet voran
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

- Long Mode
- Tastatur-Layout anpassen
- Dateisystem-Entwurf fertigstellen
- Festplatte beschreiben/lesen
- AMD Processor Optimization Module

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/3720/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1750/index.html)

<!-- MediaWiki page 1750; revision 3720; parent 3552; 2008-12-23T20:57:21Z -->
