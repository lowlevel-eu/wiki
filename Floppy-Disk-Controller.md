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

Wenn nichts dasteht, gilt das Flag bei gesetztem Bit.

### MSR

|  |  |  |  |  |  |  |  |  |
| ------ | ----- | ----- | ------ | ------ | ------ | ------ | ------ | ------ |
| Bit | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| Name | MRQ | DIO | NDMA | BUSY | ACTD | ACTC | ACTB | ACTA |

MRQ  
Status

0: DR nicht bereit

1: DR bereit

DIO  
Daten I/O

0: CPU -\> FDC

1: FDC -\> CPU

NDMA  
DMA-Modus

0: DMA-Modus aktiviert

1: DMA-Modus deaktiviert

BUSY  
BUSY (Befehl wird ausgeführt)

0: nicht busy

1: busy

ACTD-ACTA  
Laufwerk D-A ist im Positionierungs-Modus

### DOR

|  |  |  |  |  |  |  |  |
| ------ | ------ | ------ | ------ | ------ | ----- | ------- | ------- |
| Bit | 7 | 6 | 5 | 4 | 3 | 2 | 1-0 |
| Name | MOTD | MOTC | MOTB | MOTA | DMA | RESET | DRIVE |

MOTD-A  
Motorsteuerung

0: Motor ausschalten

1: Motor anschalten

DMA  
DMA und IRQ-Channel

0: aus

1: an

RESET  
Controller Reset

0: Reset ausführen (!!!)

1: Controller aktiviert (Reset ausgeführt)

DRIVE  
Laufwärk auswählen

00: Drive 0

01: Drive 1

10: Drive 2

11: Drive 3

### DR

Nach manchen Befehlen werden die Status-Register im DR zurückgegeben.

#### ST0

|  |  |  |  |  |  |  |
| ------ | ----- | ----- | ----- | ----- | ----- | ----- |
| Bit | 7-6 | 5 | 4 | 3 | 2 | 1-0 |
| Name | IC | SE | UC | NR | HD | US |

#### ST1

#### ST2

#### ST3

wird fortgesetzt!

## Siehe auch

[Interrupt 13h](https://github.com/lowlevel-eu/wiki/wiki/Interrupt-13h "Interrupt 13h") - Disketten- und Festplattenzugriff

## Weblinks

- [82077AA CHMOS Single-Chip Floppy Disk Controller Datasheet](http://lowlevel.brainsware.org/wiki/images/82077AA_FloppyControllerDatasheet.pdf)
- <http://www.isdaman.com/alsos/hardware/fdc/floppy.htm>

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/4530/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1443/index.html)

<!-- MediaWiki page 1443; revision 4530; parent 4529; 2009-07-03T08:22:16Z -->
