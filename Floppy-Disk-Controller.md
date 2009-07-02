# Floppy Disk Controller

Der Floppy Disk Controller ist ein Chip, der ein bis vier FLoppy-Laufwerke ansteuern kann.

## Eigenschaften

- DMA-Channel: 2
- IRQ: 6

# Register

## Übersicht

| Name | Port | Beschreibung | lesen/schreiben |
| ------ | ------- | ------------------------- | ----------------- |
| MSR | 0x3F4 | Main Status Register | lesen |
| DR | 0x3F5 | Data Register | lesen/schreiben |
| DOR | 0x3F2 | Digital Output Register | schreiben |

## Aufbau

### MSR

|  |  |  |  |  |  |  |  |  |
| ------ | ----- | ----- | ------ | ------ | ------ | ------ | ------ | ------ |
| Bit | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| Name | MRQ | DIO | NDMA | BUSY | ACTD | ACTC | ACTB | ACTA |

MRQ

DIO

NDMA

### DR

|  |  |  |  |  |  |  |
| ------ | ----- | ----- | ----- | ----- | ----- | ----- |
| Bit | 7-6 | 5 | 4 | 3 | 2 | 1-0 |
| Name | IC | SE | UC | NR | HD | US |

### DOR

|  |  |  |  |  |  |  |  |
| ------ | ------ | ------ | ------ | ------ | ----- | ------- | ------- |
| Bit | 7 | 6 | 5 | 4 | 3 | 2 | 1-0 |
| Name | MOTD | MOTC | MOTB | MOTA | DMA | RESET | DRIVE |

wird fortgesetzt!

## Siehe auch

[Interrupt 13h](https://github.com/lowlevel-eu/wiki/wiki/Interrupt-13h "Interrupt 13h") - Disketten- und Festplattenzugriff

## Weblinks

- [82077AA CHMOS Single-Chip Floppy Disk Controller Datasheet](http://lowlevel.brainsware.org/wiki/images/82077AA_FloppyControllerDatasheet.pdf)
- <http://www.isdaman.com/alsos/hardware/fdc/floppy.htm>

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/4527/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1443/index.html)

<!-- MediaWiki page 1443; revision 4527; parent 4521; 2009-07-02T06:23:26Z -->
