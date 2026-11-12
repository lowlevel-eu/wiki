# Floppy Disk Controller

Diese Seite oder Abschnitt ist zwar komplett, es wird aber folgende Verbesserungen gewünscht:  

- Nach Rechtschreibfehlern suchen
- Nach inhaltlichen Fehlern suchen (vor allem bei Bitmasken verschreibt man sich leicht!)
- Verlinkungen innerhalb des Artikels einbauen.
- Beispielcode

Hilf Lowlevel, den Artikel zu verbessern.

Der Floppy Disk Controller (FDC) ist ein Chip, der ein bis vier Disketten-Laufwerke ansteuern kann.

## Eigenschaften und Besonderheiten

- Der FDC sendet [IRQ](Programmable-Interrupt-Controller.md#irq-tabelle "IRQ") 6, wenn z.B. eine Lese- oder Schreiboperation beendet ist
- Der FDC kann über [DMA](Direct-Memory-Access.md "DMA") Daten direkt aus dem Speicher auf Diskette schreiben und anders herum. Dafür wird DMA Channel 2 verwendet
- Der FDC ist recht schlecht standardisiert, da verschiedene Hersteller unterschiedliche Funktionalitäten hinzugefügt haben.
- Bei allen Operationen, für die der Schreib-/Lesekopf bewegt werden muss, sollte eine Wartezeit eingehalten werden, bis die nächste Operation folgt, da insbesondere Disketten sehr hohe Zugriffszeiten besitzen. Bei Fehlen dieser Wartezeiten funktioniert der Treiber oft nur in Emulatoren, versagt aber auf echter Hardware!
- Der FDC kann nur Sektorangaben in [CHS](Cylinder-Head-Sector.md "CHS") verarbeiten
- Der FDC kann theoretisch bis zu vier Diskettenlaufwerke ansteuern, allerdings findet man heute wohl kein System mehr, welches mehr als zwei besitzt.
- **Diskettenlaufwerke sind sehr fehleranfällig! Deshalb muss ein Befehl oftmals mehrmals gesendet werden, bevor er funktioniert. Großzügige Timeouts sind Pflicht in jedem Treiber für Diskettenlaufwerke.**

## Verhalten in Emulatoren und echter Hardware

- [Bochs](Bochs.md "Bochs") unterstützt nur die Übertragung der Daten via [DMA](Direct-Memory-Access.md "DMA"). Allerdings ist dies auch die sinnvollste Variante.
- [Microsoft Virtual PC](Microsoft-Virtual-PC.md "Microsoft Virtual PC") hat Probleme mit DMA, wenn das Auto Bit gesetzt ist. Damit der Code funktioniert, muss der DMA Transfer jedes Mal durch die CPU reinitialisiert werden.

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

| **Bit** | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| ---------- | ----- | ----- | ------ | ------ | ------ | ------ | ------ | ------ |
| **Name** | MRQ | DIO | NDMA | BUSY | ACTD | ACTC | ACTB | ACTA |

MRQ  
*Status*

0: DR nicht bereit

1: DR bereit

DIO  
*Daten I/O*

0: CPU -\> FDC (Daten schreiben)

1: FDC -\> CPU (Daten lesen)

NDMA  
*DMA-Modus*

0: DMA-Modus aktiviert

1: DMA-Modus deaktiviert

BUSY  
*BUSY (Befehl wird ausgeführt)*

0: nicht busy

1: busy

ACTD-ACTA  
Laufwerk D-A ist im Positionierungsmodus

#### DOR

| **Bit** | 7 | 6 | 5 | 4 | 3 | 2 | 1 &#150; 0 |
| ---------- | ------ | ------ | ------ | ------ | ----- | ------- | ------------ |
| **Name** | MOTD | MOTC | MOTB | MOTA | DMA | RESET | DRIVE |

MOTD-A  
*Motorsteuerung*

0: Motor ausschalten

1: Motor anschalten

DMA  
*DMA und IRQ*

0: deaktiviert

1: aktiviert

RESET  
*Controller Reset*

0: Reset ausführen (!!!)

1: Controller aktiviert (Reset ausgeführt)

DRIVE  
*Laufwerk auswählen*

00: Drive 0

01: Drive 1

10: Drive 2

11: Drive 3

#### DR

In das Data-Register werden die Befehle geschrieben, die jeweils aus mehreren Bytes bestehen. Nach manchen Befehlen werden die Status-Register im DR zurückgegeben.

##### ST0

| **Bit** | 7 &#150; 6 | 5 | 4 | 3 | 2 | 1 &#150; 0 |
| ---------- | ------------ | ----- | ----- | ----- | ----- | ------------ |
| **Name** | IC | SE | UC | NR | HD | US |

IC  
*Interrupt Code*

00: Der Befehl wurde ohne Fehler ausgeführt

01: Der Befehl wurde gestartet, aber nicht richtig beendet

10: invalid Command

11: Controller war nicht bereit (Polling)

SE  
*seek end*

Der Controller hat einen Befehl mit implizitem Seek, Calibrate oder Seek erfolgreich ausgeführt

UC  
*unit check*

Gesetzt bei Fehler

NR  
*drive not ready*

HD  
*Aktiver Head*

0: Head 0

1: Head 1

US  
*Aktives Laufwerk*

00: A

01: B

10: C

11: D

##### ST1

| **Bit** | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| ---------- | ----- | ----- | ----- | ----- | ----- | ------ | ----- | ----- |
| **Name** | EN | 0 | DE | TO | 0 | NDAT | NW | NID |

EN  
*end of cylinder*

Gesetzt, wenn die geforderte Sektoranzahl die Anzahl der Sektoren auf einer Spur überschreitet

DE  
*data error*

Gesetzt bei einem Fehler im ID *address field* oder im *data field*

TO  
*time-out*

Gesetzt, wenn der FDC keine Signale von CPU oder DMA empfängt

NDAT  
*no data*

Gesetzt, wenn bei einem *read sektor*-Befehl der Sektor nicht gefunden wurde oder wenn der FDC nach einem *read ID*-Befehl die ID nicht lesen konnte

NW  
*not writeable*

Gesetzt, wenn die Floppy schreibgeschützt ist

NID  
*no address mark*

Gesetzt, wenn die *ID Address Mark* nicht gefunden wurde

##### ST2

| **Bit** | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| ---------- | ----- | ------ | ------ | ------ | ----- | ------ | ------ | ------ |
| **Name** | 0 | DADM | CRCE | WCYL | SEQ | SERR | BCYL | NDAM |

DADM  
*deleted address mark*

Bei einem *read Sector*-Befehl: Eine gelöschte *Data Address Mark* wurde gefunden

Bei einem *read deleted sector*-Befehl: Eine gesetzte *Data Address Mark* wurde gefunden

CRCE  
*CRC error in data field*

WCYL  
*wrong cylinder*

SEQ  
*seek equal*

SERR  
*seek error*

BCYL  
*bad cylinder*

NDAM  
*not data address mark DAM*

##### ST3

| **Bit** | 7 | 6 | 5 | 4 | 3 | 2 | 1 &#150; 0 |
| ---------- | ------ | ------ | ----- | ------ | ------ | ------ | ------------ |
| **Name** | ESIG | WPDR | RDY | TRKO | DSDR | HDDR | DS |

ESIG  
*error*

Gesetzt nach einem Fehler

WPDR  
*write protection*

Gesetzt, wenn die Floppy schreibgeschützt ist

RDY  
*ready*

Gesetzt, wenn das Laufwerk ready ist

TRKO  
*track 0*

Der Head ist über Track 0 (?)

DSDR  
*double sided drive*

Gesetzt, wenn die Floppy doppelseitig ist

HDDR  
*Head*

0: Head 0

1: Head 1

DS  
*drive select*

00: A

01: B

10: C

11: D

#### CCR

Im CCR sind nur die Funktionen der ersten zwei Bits definiert (Bit 0 und Bit 1):

00 500 Kbps

10 250 Kbps

01 300 Kbps

11 1 Mbps

## Befehle

### Senden von Befehlen

Das Senden von Befehlen erfolgt in drei Phasen:

- Command-Phase: Der Befehl wird von der CPU an den FDC gesendet. Dafür werden die Daten, wie weiter unten beschrieben, in das Datenregister geschrieben. Vorher sollte getestet werden, ob dieses wirklich leer ist.
- Execution-Phase: Der Befehl wird vom FDC ausgeführt. Dabei sollte im Treiber eine Wartezeit eingehalten werden, da Diskettenlaufwerke sehr langsam sind. Bei einigen Befehlen wird die Execution-Phase zusätzlich durch das Senden eines IRQs beendet.
- Result-Phase: Bei einigen Befehlen liefert der FDC Daten zurück, z.B. ob der Befehl erfolgreich ausgeführt wurde. Diese müssen alle gelesen werden, damit erneut Befehle gesendet werden können.

### Allgemeine Parameter

| Abkürzung | Beschreibung | Empfohlener Wert für 3,5" |
| ------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------- |
| MT | Multitrack, Befehl wird auf beiden Seiten der Diskette ausgeführt |  |
| DTL | Datenlänge | 0xFF |
| N | Sektorengröße, wobei 0=128Byte, 1=256Byte, 2=512Byte, ... | 2 |
| Gap3 | Abstand zwischen Sektoren | 27 |
| MFM | High Density (HD) Mode | 1 |
| SK | Skip Mode, als gelöscht markierte Daten werden automatisch übersprungen | 1 |
| Drive, Cylinder, Head, Sektor | Positionsangabe für einen bestimmten Sektor einer Diskette. Siehe [CHS](Cylinder-Head-Sector.md "CHS") |  |
| Trackgröße | Anzahl der Sektoren, die auf einem Track („Ring“) liegen | 18 (pro Track und Seite) |

### Technische Laufwerksdaten einstellen (3h)

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

- Die benötigten Daten sollten vom BIOS abgefragt werden (siehe unten).
- Im DOR kann eingestellt werden, ob DMA/IRQ oder keins von beiden verwendet wird. Hier wird dann noch einmal explizit zwischen DMA (Bit gelöscht) und kein DMA (Bit gesetzt) entschieden.

### Laufwerk kalibrieren (7h)

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
<td>1</td>
<td>1
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

Result Phase: *keine*

  
Anmerkungen:

- Nach der Kalibrierung wird ein IRQ6 gesendet
- Es kann passieren, dass der Befehl nicht funktioniert. Deshalb sollte mit "Interrupt Status überprüfen" (8h) überprüft werden, ob Bit 4 in St0 gelöscht ist.
- Bei Disketten mit mehr als 80 Tracks muss dieser Befehl in jedem Fall mehrmals gesendet werden.

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

  

### Interrupt Status überprüfen (8h)

Command Phase:

| Bit: | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| ------ | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| \#1: | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 |

Result Phase:

|  |  |
| ------ | -------------------- |
| \#1: | ST0 |
| \#2: | Aktueller Zylinder |

Anmerkungen:

- Dieser Befehl sollte immer gesendet werden, wenn der FDC einen IRQ 6 gesendet hat.
- Er muss außerdem viermal (!) nach einem Reset des FDCs gesendet werden.
- Die Zylindernummer ist oftmals falsch und sollte ignoriert werden.

  

### Schreib- /Lesekopf positionieren (fh)

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
<td>1</td>
<td>1</td>
<td>1</td>
<td>1
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
</td></tr></tbody></table>

Result Phase: *Keine*

  
Anmerkungen:

- Es kann passieren, dass der Befehl nicht funktioniert. Deshalb muss mit "Interrupt Status überprüfen" (8h) überprüft werden, ob Bit 5 in St0 gesetzt ist.
- Nach Beendigung wird ein IRQ 6 gesendet.

### Sektor schreiben (5h)

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
<td>MT</td>
<td>MFM</td>
<td>SK</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1
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
<td colspan="8">Letzter zu schreibender Sektor (im aktuellen Cylinder)
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
| \#6: | Sektor |
| \#7: | Sektorgröße N |

Anmerkungen:

- Nach dem Schreibvorgang wird ein IRQ 6 gesendet.

### Sektor lesen (6h)

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
<td>MT</td>
<td>MFM</td>
<td>SK</td>
<td>0</td>
<td>0</td>
<td>1</td>
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
<td colspan="8">Letzter zu lesender Sektor (im aktuellen Cylinder)
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
| \#6: | Sektor |
| \#7: | Sektorgröße N |

Anmerkungen:

- Nach dem Lesevorgang wird ein IRQ 6 gesendet.

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
<td colspan="8">0
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
| \#6: | Sektor |
| \#7: | Sektorgröße N |

Anmerkungen:

- Dieser Befehl ließt alle Sektoren eines Tracks hintereinander ein
- Der Befehl funktioniert nur für eine Seite der Diskette, für beide Seiten muss der Befehl mehrmals gesendet werden
- Es ist immer schneller einen gesamten Track zu lesen anstatt einzeln jeden Sektor des Tracks.

### Andere

Der FDC kennt noch weitere Befehle, auf die hier nicht weiter eingegangen wird. Diese sind:

- Gelöschten Sektor lesen / schreiben
- Track formatieren
- Sektor ID einlesen

Darüber hinaus gibt es noch erweiterte Befehle. Man kann sich aber nicht darauf verlassen, dass der eingebaute FDC diese unterstützt:

- Register Zusammenfassung
- Controller Version lesen
- Bestätigen
- Relatives Positionieren des Schreib-/Lesekopfes

## Beispielcode

### Erkennen von Diskettenlaufwerken

Zum Erkennen von den an den Computer angeschlossenen Diskettenlaufwerken gibt es zwei Möglichkeiten:

- Im Real Mode das BIOS fragen (in 0x13, ah=8), siehe dazu [Interrupt 13h](Interrupt-13h.md "Interrupt 13h")
- Im [CMOS](CMOS.md "CMOS") nachschauen (Offset 0x10), hier sind allerdings keine technischen Daten abfragbar, sondern nur der Typ des Laufwerks

### Daten/Befehle schreiben

Bevor man Daten bzw. Befehle ins Datenregister schreiben darf, muss man im MSR testen, ob das DIO-Bit gelöscht und das MRQ-Bit gesetzt ist. Erst dann ist das Datenregister leer und bereit Daten zu empfangen. \<c\>

1.  define NO_ERROR 0
2.  define ERROR_TIMEOUT 1

uint8_t error = NO_ERROR;

void send_cmd(uint8_t cmd) {

     send_data(cmd);

}

void send_data(uint8_t data) {

     for (uint8_t timeout = 0; timeout < 200; timeout++)
     {
       if ( (inb(MSR) & (MSR_MASK_DATAREG | MSR_MASK_DIO2CPU)) == MSR_MASK_DATAREG)
       {
         outb(CMD, cmd);
         error = NO_ERROR;
         return;
       }
       sleep(5);  //5ms warten vor dem nächsten Versuch
     }
     error = ERROR_TIMEOUT;
     return;

} \</c\>

### Daten lesen

Ähnlich wie beim Senden von Daten müssen beim Lesen das MRQ-Bit und DIO-Bit gesetzt sein.

\<c\> uint8_t read_data() {

     for(uint8_t timeout = 0; timeout < 200; timeout++)
     {
       if( (inb(MSR) & (MSR_MASK_DATAREG | MSR_MASK_DIO2CPU)) == (MSR_MASK_DATAREG | MSR_MASK_DIO2CPU))
       {
         error = NO_ERROR;
         return inb(DATA);
       }
       sleep(5);
     }
     error = ERROR_TIMEOUT;
     return 0;

} \</c\>

### Motor starten/anhalten

\<c\> void start_motor(uint8_t n) {

     if (!drive_states[n].motor_on)
     {
       outb(DOR, n | (0x01<<(n+4)) | DOR_MASK_NRESET | DOR_MASK_DMA);
     }

}

void stop_motor(uint8_t n) {

     if (drive_states[n].motor_on)
     {
       outb(DOR, n | DOR_MASK_NRESET | DOR_MASK_DMA);
     }

} \</c\>

### Laufwerk kallibrieren

\<c\> void calibrate_drive(uint8_t drive) { ...TODO \</c\>

### Schreib-/Lesekopf postionieren

\<c\> bool seek_head(uint8_t cyl, uint8_t head, uint8_t sector) { ...TODO \</c\>

### Reset

\<c\> void reset() {

     outb(DOR, 0);
     sleep(10);
     outb(DOR, DOR_MASK_NRESET | DOR_MASK_DMA);
     wait_irq();
     for(int i = 0; i < 4; i++)
     {
       check_interrupt_status();
     }
     outb(CCR, 0);

     /* TODO: zusätzlich sollten jetzt noch die Laufwerke kallibriert werden */

} \</c\>

### Sektoren lesen/schreiben

Die folgende Funktion nutzt Code aus dem [DMA](Direct-Memory-Access.md "DMA") Artikel: \<c\>

1.  define CMD_WRITE_SECTOR (0x05 \| 0x40)
2.  define CMD_READ_SECTOR (0x06 \| 0x40)

bool transfer_sector(uint8_t drive, uint8_t cylinder, uint8_t head, uint8_t sector, bool write, void\* buffer) {

     select_drive(drive);   //TODO
     start_motor(drive);    //TODO
     seek_head(drive);      //TODO

     dma_begin_transfer(buffer, write);
     for (int i = 0; i<5; i++)
     {
       send_command(wrie ? CMD_WRIE_SECTOR : CMD_READ_SECTOR);
       send_data(drive | head<<2);
       send_data(cylinder);
       send_data(head);
       send_data(sector);
       send_data(2);
       send_data(sector); // Letzter zu transferierender Sektor
       send_data(27);
       send_data(0xFF);
       wait_irq();
       read_data();  //st0
       read_data();  //st1
       read_data();  //st2
       read_data();  //cylinder
       read_data();  //head
       read_data();  //sector
       read_data();  //Sektorgröße
       if ( inb(MSR) & 0xC0)
       {
         check_interrupt_status();
         return true;
       }
     }
     /* fünf Fehlversuche */
     return false;

} \</c\>

## Siehe auch

[Interrupt 13h](Interrupt-13h.md "Interrupt 13h") - Disketten- und Festplattenzugriff

## Weblinks

- [82077AA CHMOS Single-Chip Floppy Disk Controller Datasheet](assets/82077AA_FloppyControllerDatasheet.pdf "82077AA FloppyControllerDatasheet.pdf")
- <http://www.isdaman.com/alsos/hardware/fdc/floppy.htm>

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/10497/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1443/index.html)

<!-- MediaWiki page 1443; revision 10497; parent 10466; 2012-03-10T12:48:56Z -->
