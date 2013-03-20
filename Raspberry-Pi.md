# Raspberry Pi

|  |  |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------- |
| [<img src="https://raw.githubusercontent.com/wiki/lowlevel-eu/wiki/assets/55d56d04146e1a63bca3.png" width="280" height="187" alt="Raspberrypi.png" />](https://raw.githubusercontent.com/wiki/lowlevel-eu/wiki/assets/8bb335421ee989c2c7b7.png) |  |
|  |  |
| Entwickler: | Raspberry Pi Foundation |
| CPU: | ARM1176JZF-S |
| GPU: | Broadcom VideoCore IV |
| Hardware: | Ethernet, Kartenleser, 256-512MB RAM, USB, HDMI |
| Homepage |  |

Der Raspberry Pi ist ein kreditkartengroßer Computer, der von der [Raspberry Pi Foundation](http://www.raspberrypi.org/) entwickelt wurde und wird. Er basiert auf einem [ARM](https://github.com/lowlevel-eu/wiki/wiki/ARM "ARM")-Prozessor und bietet, je nach Modell, zusätzlich [USB](https://github.com/lowlevel-eu/wiki/wiki/Universal-Serial-Bus "USB"), [Ethernet](https://github.com/lowlevel-eu/wiki/wiki/Ethernet "Ethernet"), SD-Slots uvm.

Des Weiteren ist der Raspberry Pi zudem sehr günstig (B-Variante ohne MwSt. 35 US-\$), was ihn für Interessierte noch attraktiver macht.

## Bedeutung für OS-Entwickler

Der Raspberry Pi ist eine sehr interessante Plattform für [OS](https://github.com/lowlevel-eu/wiki/wiki/Betriebssystem "OS")-Entwickler:

Normale PCs sind heute aus sehr vielen verschiedenen Bauteilen zusammengesetzt - so gibt es jährlich neue Grafikkartenserien und Prozessoren, und es gibt unzählige weitere Bauteile, die ein PC-Nutzer verbauen kann. Es ist für Hobby-OS-Entwickler unmöglich, für all jene Geräte Treiber zu schreiben.

Der Raspberry Pi dagegen ist eine Plattform, den es "nur" in 2 Ausführungen gibt - einer A-Variante und einer erweiterten B-Variante. Natürlich gibt es auch hier immer wieder kleinere Veränderungen, was die Bestückung betrifft, jedoch kann man diese Änderungen leicht nachvollziehen und sein OS einfach nachrüsten, sodass man (fast) die gesamte Hardware unterstützen kann (abgesehen von eigenen Erweiterungen).

## Technik

Der Raspberry Pi ist 85,60 mm × 53,98 mm × 17 mm groß. Er besitzt als CPU einen ARM1176JZF-S mit 700 MHz und sogar eine eigene GPU, nämlich den Broadcom VideoCore IV. Beide Ausführungen verfügen außerdem über einen HDMI- sowie einen Composite Video-Ausgang. Ton wird entweder über HDMI oder separat über Klinke (3,5 mm) ausgegeben.

Eine Festplatte ist nicht verbaut, dafür gibt es einen Kartenleser für SDHC-, SDXC-, MMC- und SDIO-Karten. Es existieren noch einige GPIO-Ports für eigene Erweiterungen (s.u.). Mit Strom wird der Rechner wahlweise über Batterien oder einen MicroUSB-Port versorgt.

### Unterschiede zwischen den Modellen A und B

Während die A-Variante mit 256 MB auskommen muss, wurden der B-Variante in der aktuellen Version 512 MB spendiert. Über USB-Anschlüsse verfügen beide Modelle, jedoch hat die B-Variante einen Hub integriert, der einen weiteren USB-Anschluss zulässt (der auch verbaut wurde). Die B-Variante besitzt zudem einen Ethernet-Controller, benötigt dafür aber insgesamt auch 3,5 Watt im Gegensatz zu 2,5W beim A-Modell.

## Eigene Erweiterungen

Der Raspberry Pi verfügt über eine Schnittstelle, mit der man eigene Hardware anbauen kann (z.B. eine Platine mit Temperatursensoren). Elektrotechnisch interessierte können somit also - anders als bei handelsüblichen PCs - eigene Bauteile entwerfen, für die man dann sogar die Unterstützung im eigenen Betriebssystem einbauen kann.

  

## Weblinks

- [elinux Raspberry Pi osdev](http://elinux.org/RaspberryPi_Osdev)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/11060/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2637/index.html)

<!-- MediaWiki page 2637; revision 11060; parent 11052; 2013-03-20T15:24:41Z -->
