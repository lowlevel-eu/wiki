# Speicherbereiche

Es gibt unter der 1MB-Grenze einige reservierte Speicherbereiche, die von BIOS benutzt werden oder z.B zur Ansteuerung von Videospeicher dienen.

## Speicherbereiche als Grafik

![id90g15_t.png](http://cgi.zdnet.de/glossar/i/small/id90g15_t.png)

## Speicherbereiche als Tabelle

| Name | Adresse | Größe |
| -------------------------------------------------------------------------------------------------------------------- | ---------- | ------- |
| [Interrupt Vector Table](https://github.com/lowlevel-eu/wiki/wiki/Interrupt-Vector-Table "Interrupt Vector Table") | 0x000000 | 1kB |
| [BIOS Data Area](https://github.com/lowlevel-eu/wiki/wiki/BIOS-Data-Area "BIOS Data Area") | 0x000400 | 256B |
| Base Memory | 0x000500 | 639kB |
| [VGA](https://github.com/lowlevel-eu/wiki/wiki/Video-Graphics-Array "VGA") RAM | 0x0A0000 | 64kB |
| Video ROM | 0x0C0000 | 32kB |
| [BIOS](https://github.com/lowlevel-eu/wiki/wiki/Basic-Input-Output-System "BIOS"), ROM, UMA | 0x0C8000 | 32kB |
| ROM, UMA oder Page Frame | 0x0D0000 | 64kB |
| UMA oder Page Frame | 0x0E0000 | 64kB |
| Motherboard [BIOS](https://github.com/lowlevel-eu/wiki/wiki/Basic-Input-Output-System "BIOS") | 0x0F0000 | 64kB |
| Extended Memory | 0x100000 | ... |

## Weblinks

- <http://www.zdnet.de/glossar/0,39029897,70012320p-39001793q,00.htm>
- <http://bugclub.org/eric/memory/reserved.html>

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/2259/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1563/index.html)

<!-- MediaWiki page 1563; revision 2259; parent 0; 2007-11-24T15:45:33Z -->
