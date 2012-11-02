# Basic Input Output System

Diese Seite ist ein Artikel, welcher **mehr** haben könnte..  

Wenn du mehr darüber weißt oder recherchieren willst, bist **du** aufgerufen, dies zu tun. Wenn du dir in einer Sache nicht sicher bist, dann stell es auf die Diskussionsseite.

Das **BIOS** (**B**asic **I**nput/**O**utput **S**ystem) ist die Firmware eines x86-PCs. Es wird meistens auf einem Flash-Speicher auf dem Motherboard gespeichert. Die Einstellungen des BIOS werden im [CMOS](https://github.com/lowlevel-eu/wiki/wiki/CMOS "CMOS") gespeichert. Im Realmode werden vom BIOS außerdem Funktionen für das Ansprechen der Hardware bereitgestellt.

  

## Aufgaben des BIOS

Das BIOS ist das „Ur-Programm“ eines x86-Rechners (im Nachfolgendem nur noch „PC“ genannt). Es sitzt in einem beschreibbaren Flash-Speicher und wird direkt beim Starten des PCs ausgeführt. Es unternimmt nun den sogenannten [POST](https://github.com/lowlevel-eu/wiki/wiki/Power-On-Self-Test "POST"), den **P**ower-**O**n **S**elf-**T**est, welcher den verfügbaren Arbeitsspeicher hochzählt und verschiedene Laufwerke anspricht sowie ihre Daten ausliest.

Nach dem POST versucht es von einer Liste von Laufwerken einen Bootloader zu laden. Dieser wird an Adresse 0x7C00 geladen und dann ausgeführt; Ab da hat das Betriebssystem die volle Kontrolle über den PC.

Allerdings ist das BIOS (zumindest im [Real Mode](https://github.com/lowlevel-eu/wiki/wiki/Real-Mode "Real Mode")) noch immer aktiv: Es stellt eine Menge an Interrupts zur Kommunikation mit den verschiedenen Peripheriegeräten bereit.

## Weblinks

- [<img src="https://raw.githubusercontent.com/wiki/lowlevel-eu/wiki/assets/38adc39e49df427364bd.png" title="englisch" width="20" height="12" alt="englisch" /> BIOS Central](http://bioscentral.com/)
- [<img src="https://raw.githubusercontent.com/wiki/lowlevel-eu/wiki/assets/38adc39e49df427364bd.png" title="englisch" width="20" height="12" alt="englisch" /> Die Interruptliste von Ralph Brown](http://ctyme.com/intr/int.htm)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/10924/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1616/index.html)

<!-- MediaWiki page 1616; revision 10924; parent 10913; 2012-11-02T08:31:04Z -->
