# Industry Standard Architecture

Die **Industry Standard Architecture** ist ein damaliger Standard, der maßgeblich die Entwicklung des (IBM-)PCs beeinflusst hat. Aus ihm hervorgegangen ist unter anderem der 8-Bit breite PC-Bus, welcher später auf 16-Bit erweitert wurde und von nun an unter der Bezeichnung **ISA-Bus** vermarktet wurde. Heutzutage ist dieser Bus zumindest bei privaten PCs nicht mehr im Einsatz, er wird seit circa 2001 nicht mehr verbaut. In der Industrie ist dieser Bus aber noch vereinzelt im Einsatz.

  

## Geschichtliches

Es wurde schon früh nach einem Standard in der Industrie gesucht sowie nach einer Möglichkeit, bestehende Systeme einfach und effektiv aufzurüsten, ohne dafür alte Systeme durch Neue zu ersetzen.

  

## Gegenwart

Seit etwa 2005 wird der ISA-Slot nicht mehr in Desktop-PCs verbaut. Allerdings sind [PIC](https://github.com/lowlevel-eu/wiki/wiki/Programmable-Interrupt-Controller "PIC"), [PIT](https://github.com/lowlevel-eu/wiki/wiki/Programmable-Interval-Timer "PIT"), [Tastatur](https://github.com/lowlevel-eu/wiki/wiki/Keyboard-Controller "KBC") und [Floppy](https://github.com/lowlevel-eu/wiki/wiki/Floppy-Disk-Controller "Floppy") allesamt ISA-Geräte, sodass ISA auch heute noch eine wichtige Rolle spielt. Davon ist der [PIC](https://github.com/lowlevel-eu/wiki/wiki/Programmable-Interrupt-Controller "PIC") im Chipsatz integriert und der [PIT](https://github.com/lowlevel-eu/wiki/wiki/Programmable-Interval-Timer "PIT"), [Tastatur](https://github.com/lowlevel-eu/wiki/wiki/Keyboard-Controller "KBC") und [Floppy](https://github.com/lowlevel-eu/wiki/wiki/Floppy-Disk-Controller "Floppy") in einem zusätzlichen Super-I/O-Chip enthalten welcher über [LPC](http://www.intel.com/design/chipsets/industry/lpc.htm) (der Nachfolger des ISA mit sehr wenigen Pins) an den Chipsatz angebunden ist. Seit dem die CPUs aber den Speicher selber direkt anbinden verbreiten sich in den PCs zunehmend Single-Chip-Chipsätze (die im wesentlichen die Aufgaben der früheren South-Bridge beinhalten) und üblicherweise auch [PIT](https://github.com/lowlevel-eu/wiki/wiki/Programmable-Interval-Timer "PIT") und [Tastatur](https://github.com/lowlevel-eu/wiki/wiki/Keyboard-Controller "KBC") enthalten (Floppy ist damit komplett weggefallen, womit oft auch der [ISA-DMA-Controller](https://github.com/lowlevel-eu/wiki/wiki/Direct-Memory-Access#isa-dma-controller "DMA") verschwunden ist) so das der LPC eigentlich nur noch für das BIOS-Flash und das optionale TPM benutzt wird.

## Plug-and-Play

Die Plug-and-Play-Spezifikation ist dafür gedacht gewesen, den ISA-Bus mit den gleichen Funktionialitäten des PCI-Busses auszustatten. Dazu gehören relozierbare I/O-Ports und geographische Addressierung. Die Relozierung übernimmt dabei das BIOS, weshalb das BIOS auch PnP-fähig sein muss.

Bei der geographischen Addressierung wird jedem Peripheriegerät eine *Card Select Number* zugewiesen. Diese wird mit der 64-Bit breiten Seriennummer, die jedes PnP-Gerät hat, verknüpft. Dieser Vorgang wird vom ebenfalls vom BIOS übernommen und wird direkt beim Hochfahren des Rechners durchgeführt.

  
**TODO**: [ISA Plug and Play Specification V1.0a](http://www.osdever.net/documents/PNP-ISA-v1.0a.pdf)

## Links

- [Wikipedia: Industry Standard Architecture](http://de.wikipedia.org/wiki/Industry_Standard_Architecture)
- [Low Pin Count Interface Specification (LPC)](http://www.intel.com/design/chipsets/industry/lpc.htm)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/10295/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1709/index.html)

<!-- MediaWiki page 1709; revision 10295; parent 9880; 2011-11-22T21:47:30Z -->
