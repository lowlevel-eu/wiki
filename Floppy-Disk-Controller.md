# Floppy Disk Controller

Der Floppy Disk Controller ist ein Chip, der ein bis vier Floppy-Laufwerke ansteuern kann.

## Eigenschaften

- DMA-Channel: 2
- IRQ: 6

# Register

## Übersicht

| Name | Port | Beschreibung | lesen/schreiben |
| ------ | ------- | -------------------------------- | ----------------- |
| SRA | 0x3F0 | Status Register A | lesen |
| SRB | 0x3F1 | Status Register B | lesen |
| DOR | 0x3F2 | Digital Output Register | schreiben |
| TDR | 0x3F3 | Tape Drive Register | lesen/schreiben |
| MSR | 0x3F4 | Main Status Register | lesen |
| DRSR | 0x3F4 | Data Rate Select Register | schreiben |
| DR | 0x3F5 | Data Register | lesen/schreiben |
| DIR | 0x3F7 | Digital Input Register | lesen |
| CCR | 0x3F7 | Configuration Control Register | schreiben |

## Aufbau

Wenn nichts dasteht, gilt das Flag bei gesetztem Bit.

### MSR

|  |  |  |  |  |  |  |  |  |
| ---------- | ----- | ----- | ------ | ------ | ------ | ------ | ------ | ------ |
| **Bit** | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| **Name** | MRQ | DIO | NDMA | BUSY | ACTD | ACTC | ACTB | ACTA |

MRQ  
Status

0: DR nicht bereit

1: DR bereit

DIO  
Daten I/O

0: CPU -\> FDC (Daten schreiben)

1: FDC -\> CPU (Daten lesen)

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
| ---------- | ------ | ------ | ------ | ------ | ----- | ------- | ------------ |
| **Bit** | 7 | 6 | 5 | 4 | 3 | 2 | 1 &#150; 0 |
| **Name** | MOTD | MOTC | MOTB | MOTA | DMA | RESET | DRIVE |

MOTD-A  
Motorsteuerung

0: Motor ausschalten

1: Motor anschalten

DMA  
DMA und IRQ

0: deaktiviert

1: aktiviert

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

In das Data-Register werden die Befehle geschrieben, die jeweils aus mehreren Bytes bestehen. Nach manchen Befehlen werden die Status-Register im DR zurückgegeben.

#### ST0

|  |  |  |  |  |  |  |
| ---------- | ------------ | ----- | ----- | ----- | ----- | ------------ |
| **Bit** | 7 &#150; 6 | 5 | 4 | 3 | 2 | 1 &#150; 0 |
| **Name** | IC | SE | UC | NR | HD | US |

IC  
Interrupt Code

00: der Befehl wurde ohne Fehler ausgeführt

01: der Befehl wurde gestartet, aber nicht richtig beendet

10: invalid Command

11: Controller war nicht bereit (Polling)

SE  
Seek end

der Controller hat einen Befehl mit inplizitem Seek erfolgreich ausgeführt

UC  
unit check

gesetzt bei Fehler

NR  
drive not ready

HD  
aktiver head

0: Head 0

1: Head 1

US  
aktives Laufwerk

00: A

01: B

10: C

11: D

#### ST1

|  |  |  |  |  |  |  |  |  |
| ---------- | ----- | ----- | ----- | ----- | ----- | ------ | ----- | ----- |
| **Bit** | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| **Name** | EN | 0 | DE | TO | 0 | NDAT | NW | NID |

EN  
End of Cylinder

gesetzt wenn die geforderte Sektoranzahl die Anzahl der Sektoren auf einer Spur überschreitet

DE  
Data Error

gesetzt bei einem Fehler im ID Addressfield oder im Datafield

TO  
Time-out

gesetzt wenn der FDC keine Signale von CPU oder DMA empfängt

NDAT  
No Data

gesetzt wenn bei einem read sektor Befehl der Sektor nicht gefunden wurde

oder wenn der FDC nach einem read ID Befehl die ID nicht lesen konnte

NW  
Not Writeable

gesetzt wenn die Floppy schreibgeschützt ist

NID  
Ao Address Mark

gesetzt wenn die ID Address mark nicht gefunden wurde

#### ST2

|  |  |  |  |  |  |  |  |  |
| ---------- | ----- | ------ | ------ | ------ | ----- | ------ | ------ | ------ |
| **Bit** | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| **Name** | 0 | DADM | CRCE | WCYL | SEQ | SERR | BCYL | NDAM |

DADM  
Deleted Address Mark

Bei einem read Sector Befehl:

eine gelöschte Data Address Mark wurde gefunden

Bei einem read deleted Sector Befehl:

eine gesetzte Data Address Mark wurde gefunden

CRCE  
CRC error in data field

WCYL  
wrong cylinder

SEQ  
seek equal

SERR  
seek error

BCYL  
bad cylinder

NDAM  
not data address mark DAM

#### ST3

|  |  |  |  |  |  |  |  |
| ---------- | ------ | ------ | ----- | ------ | ------ | ------ | ------------ |
| **Bit** | 7 | 6 | 5 | 4 | 3 | 2 | 1 &#150; 0 |
| **Name** | ESIG | WPDR | RDY | TRKO | DSDR | HDDR | DS |

ESIG  
Error

gesetzt nach einem Fehler

WPDR  
Write Protection

gesetzt wenn die Disc schreibgeschützt ist

RDY  
Ready

gesetzt wenn die Drive ready ist

TRKO  
Track 0

der Head ist über Track 0 (?)

DSDR  
Double sided drive

gesetzt wenn die Floppy doppelseitig ist

HDDR  
Head

0: Head 0

1: Head 1

DS  
Drive select

00: A

01: B

10: C

11: D

# Befehle

# Infos

## Data Address Mark

# Siehe auch

[Interrupt 13h](https://github.com/lowlevel-eu/wiki/wiki/Interrupt-13h "Interrupt 13h") - Disketten- und Festplattenzugriff

# Weblinks

- [82077AA CHMOS Single-Chip Floppy Disk Controller Datasheet](http://lowlevel.brainsware.org/wiki/images/82077AA_FloppyControllerDatasheet.pdf)
- <http://www.isdaman.com/alsos/hardware/fdc/floppy.htm>

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/4628/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1443/index.html)

<!-- MediaWiki page 1443; revision 4628; parent 4627; 2009-07-12T18:31:02Z -->
