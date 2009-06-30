# Floppy Disk Controller

Der Floppy Disk Controller ist ein Chip, der ein bis vier FLoppy-Laufwerke ansteuern kann.

## Eigenschaften

- DMA-Channel: 2
- IRQ: 6

## Register

### Übersicht

| Name | Port | Beschreibung | lesen/schreiben |
| ------ | ------- | ------------------------- | ----------------- |
| MSR | 0x3F4 | Main Status Register | lesen |
| DR | 0x3F5 | Data Register | lesen/schreiben |
| DOR | 0x3F2 | Digital Output Register | schreiben |

### Aufbau

#### MSR

#### DR

#### DOR

wird fortgesetzt!

## Siehe auch

[Interrupt 13h](https://github.com/lowlevel-eu/wiki/wiki/Interrupt-13h "Interrupt 13h") - Disketten- und Festplattenzugriff

## Weblinks

- [82077AA CHMOS Single-Chip Floppy Disk Controller Datasheet](http://lowlevel.brainsware.org/wiki/images/82077AA_FloppyControllerDatasheet.pdf)
- <http://www.isdaman.com/alsos/hardware/fdc/floppy.htm>

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/4521/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1443/index.html)

<!-- MediaWiki page 1443; revision 4521; parent 4520; 2009-06-30T10:53:54Z -->
