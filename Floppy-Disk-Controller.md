# Floppy Disk Controller

Diese Seite ist ein Artikel, welcher **mehr** haben könnte..  

Wenn du mehr darüber weißt oder recherchieren willst, bist **du** aufgerufen, dies zu tun. Wenn du dir in einer Sache nicht sicher bist, dann stell es auf die Diskussionsseite.

Der Floppy Disk Controller (FDC) ist ein Chip, der ein bis vier Disketten-Laufwerke ansteuern kann.

## Eigenschaften und Besonderheiten

- Der FDC sendet [IRQ](https://github.com/lowlevel-eu/wiki/wiki/Programmable-Interrupt-Controller#irq-tabelle "IRQ") 6, wenn z.B. eine Lese- oder Schreiboperation beendet ist
- Der FDC kann über [DMA](https://github.com/lowlevel-eu/wiki/wiki/Direct-Memory-Access "DMA") Daten direkt aus dem Speicher auf Diskette schreiben und anders herum. Dafür wird DMA Channel 2 verwendet
- Der FDC ist recht schlecht standardisiert, da verschiedene Hersteller unterschiedliche Funktionalitäten hinzugefügt haben.
- Bei allen Operationen, für die der Schreib-/Lesekopf bewegt werden muss, sollte eine Wartezeit eingehalten werden, bis die nächste Operation folgt, da insbesondere Disketten sehr langsame Zugriffszeiten besitzen. Bei Fehlen dieser Wartezeiten funktioniert der Treiber oft nur in Emulatoren, versagt aber auf echter Hardware!
- Der FDC kann nur Sektorangaben in [CHS](https://github.com/lowlevel-eu/wiki/wiki/Cylinder-Head-Sector "CHS") verarbeiten

## Register

### Übersicht

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

### Aufbau

Wenn nichts dasteht, gilt das Flag bei gesetztem Bit.

#### MSR

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

#### DOR

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
Laufwerk auswählen

00: Drive 0

01: Drive 1

10: Drive 2

11: Drive 3

#### DR

In das Data-Register werden die Befehle geschrieben, die jeweils aus mehreren Bytes bestehen. Nach manchen Befehlen werden die Status-Register im DR zurückgegeben.

##### ST0

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

##### ST1

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
No Address Mark

gesetzt wenn die ID Address Mark nicht gefunden wurde

##### ST2

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

##### ST3

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

### CCR

Im CCR sind nur die Funktionen der ersten zwei Bits definiert (Bit 0 und Bit 1):

00 500 Kbps

10 250 Kbps

01 300 Kbps

11 1 Mbps

## Befehle

### Senden von Befehlen

Das Senden von Befehlen erfolgt in drei Phasen:

- Command-Phase: Der Befehl wird von der CPU an den FDC gesendet. Dafür werden die Daten wie weiter unten beschrieben in das Datenregister geschrieben. Vorher sollte getestet werden, ob dieses wirklich leer ist.
- Execution-Phase: Der Befehl wird vom FDC ausgeführt. Dabei sollte im Treiber eine Wartezeit eingehalten werden, da Diskettenlaufwerke sehr langsam sind. Bei einigen Befehlen wird die Execution-Phase zusätzlich durch das Senden eines IRQs beendet.
- Result-Phase: Bei einigen Befehlen liefert der FDC Daten zurück, z.B. ob der Befehl erfolgreich ausgeführt wurde. Diese müssen gelesen werden, damit erneut Befehle gesendet werden können.

### Allgemeine Parameter

| Abkürzung | Beschreibung | Empfohlener Wert für 3,5" |
| ------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------- |
| MT | Multitrack, Befehl wird auf beiden Seiten der Diskette ausgeführt |  |
| DTL | Datenlänge | 0xFF |
| N | Sekorengröße, wobei 0=128Byte, 1=256Byte, 2=512Byte, ... | 2 |
| Gap3 | Abstand zwischen Sektoren | 27 |
| MFM | High Density (HD) Mode | 1 |
| SK | Skip Mode, als gelöscht markierte Daten werden automatisch übersprungen | ??? |
| Drive, Cylinder, Head, Sektor | Positionsangabe für einen bestimmten Sektor einer Diskette. Siehe [CHS](https://github.com/lowlevel-eu/wiki/wiki/Cylinder-Head-Sector "CHS") |  |
| Trackgrößße | Anzahl der Sektoren, die auf einem Track ("Ring") liegen | ??? |

### Kompletten Track lesen (2h)

Command Phase:

<table>
<tbody><tr>
<th>Bit:</th>
<th>7</th>
<th>6</th>
<th>5</th>
<th>4</th>
<th>3</th>
<th>2</th>
<th>1</th>
<th>0
</th></tr>
<tr>
<td>#1:</td>
<td>0</td>
<td>MFM</td>
<td>SK</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0
</td></tr>
<tr>
<td>#2:</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>Head</td>
<td colspan="2">Drive
</td></tr>
<tr>
<td>#3:</td>
<td colspan="8">Cylinder
</td></tr>
<tr>
<td>#4:</td>
<td colspan="8">Head
</td></tr>
<tr>
<td>#5:</td>
<td colspan="8">Sektor
</td></tr>
<tr>
<td>#6:</td>
<td colspan="8">Sektorgröße N
</td></tr>
<tr>
<td>#7:</td>
<td colspan="8">Track-Größe
</td></tr>
<tr>
<td>#8:</td>
<td colspan="8">GAP3
</td></tr>
<tr>
<td>#9:</td>
<td colspan="8">DTL
</td></tr></tbody></table>

Result Phase:

|  |  |
| ------ | --------------- |
| \#1: | ST0 |
| \#2: | ST1 |
| \#3: | ST2 |
| \#4: | Cylinder |
| \#5: | Head |
| \#6: | 0 |
| \#7: | Sektorgröße N |

Anmerkungen:

- Dieser Befehl ließt alle Sektoren eines Tracks hintereinander ein
- Der Befehl funktioniert nur für eine Seite der Diskette, für beide Seiten muss der Befehl mehrmals gesendet werden

### Diskettendaten einstellen (3h)

Command Phase:

<table>
<tbody><tr>
<th>Bit:</th>
<th>7</th>
<th>6</th>
<th>5</th>
<th>4</th>
<th>3</th>
<th>2</th>
<th>1</th>
<th>0
</th></tr>
<tr>
<td>#1:</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1
</td></tr>
<tr>
<td>#2:</td>
<td colspan="4">Step Rate</td>
<td colspan="4">Head Unload Time
</td></tr>
<tr>
<td>#3</td>
<td colspan="7">Head Load Time</td>
<td>Kein DMA
</td></tr></tbody></table>

Result Phase: *keine*

Anmerkungen:

- Die benötigten Daten sollten vom BIOS abgefragt werden (siehe unten)
- Im MSR kann eingestellt werden, ob DMA/IRQ oder keins von beidem, hier wird dann noch einmal explizit zwischen DMA (Bit gelöscht) und kein DMA (Bit gesetzt) entschieden.

### Laufwerksstatus überprüfen (4h)

Command Phase:

<table>
<tbody><tr>
<th>Bit:</th>
<th>7</th>
<th>6</th>
<th>5</th>
<th>4</th>
<th>3</th>
<th>2</th>
<th>1</th>
<th>0
</th></tr>
<tr>
<td>#1:</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0
</td></tr>
<tr>
<td>#2:</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>Head</td>
<td colspan="2">Drive
</td></tr></tbody></table>

Result Phase:

ST3

  

### write sector

### calibrate drive

### check interrupt status

### write deleted sector

### read sector ID

### read deleted sector

### format track

### seek head

## Beispielcode

### Erkennen von Diskettenlaufwerken

int 13, ah=8 oder CMOS

### Daten/Befehle schreiben

### Daten lesen

### Initialisierung

### Auf Diskette schreiben

### Von Diskette lesen

## Siehe auch

[Interrupt 13h](https://github.com/lowlevel-eu/wiki/wiki/Interrupt-13h "Interrupt 13h") - Disketten- und Festplattenzugriff

## Weblinks

- [82077AA CHMOS Single-Chip Floppy Disk Controller Datasheet](https://raw.githubusercontent.com/wiki/lowlevel-eu/wiki/assets/3c350f238581550e0dd8.pdf "82077AA FloppyControllerDatasheet.pdf")
- <http://www.isdaman.com/alsos/hardware/fdc/floppy.htm>

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/7739/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1443/index.html)

<!-- MediaWiki page 1443; revision 7739; parent 7737; 2010-06-10T16:31:52Z -->
