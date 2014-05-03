# Industry Standard Architecture

Die **Industry Standard Architecture** ist aus dem Erweiterungsbus des IBM-PC hervorgegangen und hat die Entwicklung des (IBM-kompatiblen) PCs maßgeblich beeinflusst. Anfangs ein 8 Bit breiter Bus (PC/XT) wurde er später auf 16 Bit (PC/AT) erweitert und rückwirkend in **ISA-Bus** umbenannt. Obwohl heutzutage nicht mehr in der ursprünglichen Form verbaut, findet er in der Industrie noch vereinzelt Verwendung.

## Geschichtliches

Der IBM-PC war als offenes System gedacht. Durch die Erweiterungsmöglichkeiten konnte man bestehende Systeme stückweise aufrüsten und war nicht an ein bestimmtes System gebunden. Durch die weite Verbreitung von ISA-Geräten fand er seinen Weg auch in IBM-fremde Systeme (z.B. manche Amigas).

## Gegenwart

Seit etwa 2005 wird der ISA-Slot nicht mehr in Desktop-PCs verbaut. Allerdings sind [PIC](https://github.com/lowlevel-eu/wiki/wiki/Programmable-Interrupt-Controller "PIC"), [PIT](https://github.com/lowlevel-eu/wiki/wiki/Programmable-Interval-Timer "PIT"), [Tastatur](https://github.com/lowlevel-eu/wiki/wiki/Keyboard-Controller "KBC") und [Floppy](https://github.com/lowlevel-eu/wiki/wiki/Floppy-Disk-Controller "Floppy") allesamt ISA-Geräte, sodass ISA auch heute noch eine wichtige Rolle spielt. Davon ist der [PIC](https://github.com/lowlevel-eu/wiki/wiki/Programmable-Interrupt-Controller "PIC") im Chipsatz integriert und der [PIT](https://github.com/lowlevel-eu/wiki/wiki/Programmable-Interval-Timer "PIT"), [Tastatur](https://github.com/lowlevel-eu/wiki/wiki/Keyboard-Controller "KBC") und [Floppy](https://github.com/lowlevel-eu/wiki/wiki/Floppy-Disk-Controller "Floppy") in einem zusätzlichen Super-I/O-Chip enthalten welcher über [LPC](http://www.intel.com/design/chipsets/industry/lpc.htm) (der Nachfolger des ISA mit sehr wenigen Pins) an den Chipsatz angebunden ist.

Seitdem die CPUs aber den Speicher selber direkt anbinden, verbreiten sich in den PCs zunehmend Single-Chip-Chipsätze (die im wesentlichen die Aufgaben der früheren South-Bridge beinhalten) und üblicherweise auch [PIT](https://github.com/lowlevel-eu/wiki/wiki/Programmable-Interval-Timer "PIT") und [Tastatur](https://github.com/lowlevel-eu/wiki/wiki/Keyboard-Controller "KBC") enthalten (Floppy ist damit komplett weggefallen, womit oft auch der [ISA-DMA-Controller](https://github.com/lowlevel-eu/wiki/wiki/Direct-Memory-Access#isa-dma-controller "DMA") verschwunden ist), so dass der LPC eigentlich nur noch für das BIOS-Flash und das optionale TPM benutzt wird.

## Plug-and-Play

Die Plug-and-Play-Spezifikation ist dafür gedacht gewesen, den ISA-Bus mit den gleichen Funktionialitäten des PCI-Busses auszustatten. Dazu gehören relozierbare I/O-Ports und geographische Addressierung. Die Relozierung übernimmt dabei das BIOS, weshalb das BIOS auch PnP-fähig sein muss.

Bei der geographischen Addressierung wird jedem Peripheriegerät eine *Card Select Number* zugewiesen. Diese wird mit der 64-Bit breiten Seriennummer, die jedes PnP-Gerät hat, verknüpft. Dieser Vorgang wird vom ebenfalls vom BIOS übernommen und wird direkt beim Hochfahren des Rechners durchgeführt.

**TODO**: [ISA Plug and Play Specification V1.0a](http://www.osdever.net/documents/PNP-ISA-v1.0a.pdf)

## Extended Industry Standard Architecture

**EISA** stellt eine zu ISA kompatible 32-Bit-Erweiterung dar. EISA unterstützt den Zugriff durch mehrere CPUs und beherrst Burst-Zugriffe. Im Heimbereich erreichte es keine nennenswerte Bedeutung und spielt für die Entwicklung von Betriebssystemen keine Rolle mehr.

## Links

- [Wikipedia: Industry Standard Architecture](http://de.wikipedia.org/wiki/Industry_Standard_Architecture)
- [Wikipedia: Extended ISA](http://de.wikipedia.org/wiki/Extended_ISA)
- [Low Pin Count Interface Specification (LPC)](http://www.intel.com/design/chipsets/industry/lpc.htm)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/11197/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1709/index.html)

<!-- MediaWiki page 1709; revision 11197; parent 11194; 2014-05-03T23:50:35Z -->
