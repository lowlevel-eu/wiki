# Open Host Controller Interface

Diese Seite oder Abschnitt ist zwar komplett, es wird aber folgende Verbesserungen gewünscht:  

- Die Liste der Register vervollständigen (Spezifikation: Seite 137ff)
- Isochronous Transfers (Spezifikation: Seite 39ff und 48ff)
- Alignment der verschiedenen Datenstrukturen!
- Vielleicht noch ein paar nette Flowcharts, wie man Transfers durchführt?

Hilf Lowlevel, den Artikel zu verbessern.

  
Das OHCI ist neben dem UHCI ein Interface für USB-1.x- und Firewire-Hostcontroller (HC). Zum Verständnis dieses Artikels ist die Kenntnis des [USB](https://github.com/lowlevel-eu/wiki/wiki/Universal-Serial-Bus "USB")-Protoklls Vorraussetzung.

## Kommunikation mit dem HC

Die Kommunikation mit dem HC erfolgt über zwei Wege, zum einen über in den Arbeitsspeicher eingeblendete Register, zum anderen über einen gemeinsamen Speicherbereich im Arbeitsspeicher. Dieser Speicherbereich enthält zum einen die sogenannte Host Controller Communications Area (HCCA) und zum anderen verkettete Listen, die die Abfolge der zu erledigenden Transfers enthalten. **Hinweis:** Bei allen Angaben von Speicheradressen sind die *physikalischen* Adressen zu übergeben!

### Register

Die Register sind in den Arbeitsspeicher eingeblendet. Ihre Adresse ist allerdings nicht fix. Da der HC aber in der Regel über einen PCI-Bus an die CPU angeschlossen ist, kann man von diesem die Adresse abrufen. Dafür durchläuft man die einzelnen Konfigurations-Adressräume nach einem Gerät mit der Class 0x0C (Serielle Buscontroller) und der Subclass 0x03. Das DWord an Offset 0x10 ist die Adresse der Register. Die angesprochenen Register sind alle 32 Bit breit (Offset in Klammern)

#### Status-Register

- **HcRevision** (0x00)

<table>
<tbody><tr>
<th>Bit</th>
<th>31</th>
<th>30</th>
<th>29</th>
<th>28</th>
<th>27</th>
<th>26</th>
<th>25</th>
<th>24</th>
<th>23</th>
<th>22</th>
<th>21</th>
<th>20</th>
<th>19</th>
<th>18</th>
<th>17</th>
<th>16</th>
<th>15</th>
<th>14</th>
<th>13</th>
<th>12</th>
<th>11</th>
<th>10</th>
<th>9</th>
<th>8</th>
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
<td>Bedeutung</td>
<td colspan="24"><i>reserviert</i></td>
<td colspan="8">REV
</td></tr></tbody></table>

**REV**: Version der OHCI-Spezifikation in [BCD](https://github.com/lowlevel-eu/wiki/wiki/Binary-Coded-Decimal "BCD"). Hier sollte 0x10 stehen.

- **HcControl** (0x04)

<table>
<tbody><tr>
<th>Bit</th>
<th>31</th>
<th>30</th>
<th>29</th>
<th>28</th>
<th>27</th>
<th>26</th>
<th>25</th>
<th>24</th>
<th>23</th>
<th>22</th>
<th>21</th>
<th>20</th>
<th>19</th>
<th>18</th>
<th>17</th>
<th>16</th>
<th>15</th>
<th>14</th>
<th>13</th>
<th>12</th>
<th>11</th>
<th>10</th>
<th>9</th>
<th>8</th>
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
<td>Bedeutung</td>
<td colspan="21"><i>reserviert</i></td>
<td>RWE</td>
<td>RWC</td>
<td>IR</td>
<td colspan="2">HCFS</td>
<td>BLE</td>
<td>CLE</td>
<td>IE</td>
<td>PLE</td>
<td colspan="2">CBSR
</td></tr></tbody></table>

**CBSR** (ControlBulkServiceRatio): In einem Frame werden sowohl Transfers für Bulk-Endpunkte als auch für Control-Endpunkte durchgeführt. Hier wird spezifiziert, wie viele Control-Endpunkte auf einen Bulk-Endpunkt kommen: 00b = 1:1, 01b = 2:1, 10b = 3:1, 11b = 4:1

**PLE** (PeriodicListEnable): Ist dieses Bit gesetzt, dann arbeitet der HC die Liste mit periodischen Transfers ab (-\> HcPeriodCurrentED)

**IE** (IsochronousEnable): Ist dieses Bit gesetzt, dann führt der HC auch Isochronous Transfers in der Liste der periodischen Transfers aus

**CLE** (ControlListEnable): Ist dieses Bit gesetzt, dann arbeitet der HC die Liste mit Control Transfers ab (-\>HcControlCurrentED)

**BLE** (BulkListEnable): Ist dieses Bit gesetzt, dann arbeitet der HC die Liste mit Bulk Transfers ab (-\>HcBulkCurrentED)

**HCFS** (HostControllerFunctionalState): Der Zustand, in den der HC den USB setzen soll: 00b=USB_RESET, 01b=USB_RESUME, 10b=USB_OPERATIONAL, 11b=USB_SUSPEND

**IR** (InterruptRouting): Ist dieses Bit gesetzt, dann werden alle Interrupts vom [SMI](https://github.com/lowlevel-eu/wiki/wiki/SMI "SMI") behandelt. Ist es gelöscht, werden Interrupts vom Betriebssystem behandelt.

**RWC** (RemoteWakeupConnected): Ist dieses Bit gesetzt, dann unterstützt der HC Remote Wakeup. Dieses Bit sollte nur gelesen werden.

- **HcCommandStatus** (0x08)

<table>
<tbody><tr>
<th>Bit</th>
<th>31</th>
<th>30</th>
<th>29</th>
<th>28</th>
<th>27</th>
<th>26</th>
<th>25</th>
<th>24</th>
<th>23</th>
<th>22</th>
<th>21</th>
<th>20</th>
<th>19</th>
<th>18</th>
<th>17</th>
<th>16</th>
<th>15</th>
<th>14</th>
<th>13</th>
<th>12</th>
<th>11</th>
<th>10</th>
<th>9</th>
<th>8</th>
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
<td>Bedeutung</td>
<td colspan="14"><i>reserviert</i></td>
<td colspan="2">SOC</td>
<td colspan="12"><i>reserviert</i></td>
<td>OCR</td>
<td>BLF</td>
<td>CLF</td>
<td>HCR
</td></tr></tbody></table>

**HCR** (HostControllerReset): Beim Setzen dieses Bits führt der HC einen Reset durch. Nach Beendigung, die nicht länger als 10µs andauern darf, löscht der HC dieses Bit.

**CLF** (ControlListFilled): Immer wenn ein neuer TD in die Liste der Control-Transfers eingefügt wird, muss dieses Bit gesetzt werden. Andernfalls arbeitet der HC die Liste nicht weiter ab.

**BLF** (BulkListFilled): Immer wenn ein neuer TD in die Liste der Bulk-Transfers eingefügt wird, muss dieses Bit gesetzt werden. Andernfalls arbeitet der HC die Liste nicht weiter ab.

**OCR** (OwnershipChangeRequest): Aus Kompatibilitätsgründen wird der HC vom [BIOS](https://github.com/lowlevel-eu/wiki/wiki/Basic-Input-Output-System "BIOS") so initialisiert, dass er vom [SMI](https://github.com/lowlevel-eu/wiki/wiki/SMI "SMI") gesteuert wird. Wenn das Betriebssystem nun die Steuerung des HC übernehmen will, dann setzt es dieses Bit. Wenn der HC die Kontrolle vom SMI auf das Betriebssystem übergeben hat, löscht er dieses Bit wieder.

**SOC** (SchedulingOverrunCount): Wird bei Fehlern inkrementiert.

- **HcInterruptStatus** (0x0C)

<table>
<tbody><tr>
<th>Bit</th>
<th>31</th>
<th>30</th>
<th>29</th>
<th>28</th>
<th>27</th>
<th>26</th>
<th>25</th>
<th>24</th>
<th>23</th>
<th>22</th>
<th>21</th>
<th>20</th>
<th>19</th>
<th>18</th>
<th>17</th>
<th>16</th>
<th>15</th>
<th>14</th>
<th>13</th>
<th>12</th>
<th>11</th>
<th>10</th>
<th>9</th>
<th>8</th>
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
<td>Bedeutung</td>
<td>0</td>
<td>OC</td>
<td colspan="23"><i>reserviert</i></td>
<td>RHSC</td>
<td>FNO</td>
<td>UE</td>
<td>RD</td>
<td>SF</td>
<td>WDH</td>
<td>SO
</td></tr></tbody></table>

**SO** (SchedulingOverrun): Wird gesetzt, wenn ein Fehler auftritt.

**WDH** (WritebackDoneHead): Ist dieses Bit gelöscht, dann übernimmt der HC den Wert von HcDoneHead in HccaDoneHead.

**SF** (StartofFrame): Wird vom HC beim Anfang eines neuen Frames gesetzt.

**RD** (ResumeDetected): Wird vom HC gesetzt, wenn ein Gerät den Zustand USBResume verlangt.

**UE** (UnrecoverableError): Wenn der HC dieses Bit setzt, dann ist ein nicht behebbarer Fehler aufgetreten, der nur noch durch einen Reset des HCs aufgelöst werden kann.

**FNO** (FrameNumberOverflow): Wenn Bit 15 von HcFmNumber seinen Wert ändert, wird dieses Bit vom HC gesetzt.

**RHSC** (RootHubStatusChange): Wird vom HC gesetzt, wenn HcRhStatus oder HcRhPortStatus\[\] seinen Wert ändert.

**OC** (OwnershipChange): Wird gesetzt, wenn ein OwnerchipChange durchgeführt wurde (-\>HcConnandStatus, OCR)

- **HcInterruptEnable** (0x10) und **HcInterruptDisable** (0x14)

Diese Register dienen dem Aktivieren bzw. Deaktiviern von Interrupts beim Ändern von Bits durch den HC in HcInterruptStauts. Das Schreiben einer 1 in eines der Register setzt das entsprechende Bit im Register und löscht es im anderen. Das Schreiben einer 0 ändert nichts.

<table>
<tbody><tr>
<th>Bit</th>
<th>31</th>
<th>30</th>
<th>29</th>
<th>28</th>
<th>27</th>
<th>26</th>
<th>25</th>
<th>24</th>
<th>23</th>
<th>22</th>
<th>21</th>
<th>20</th>
<th>19</th>
<th>18</th>
<th>17</th>
<th>16</th>
<th>15</th>
<th>14</th>
<th>13</th>
<th>12</th>
<th>11</th>
<th>10</th>
<th>9</th>
<th>8</th>
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
<td>Bedeutung</td>
<td>MIE/MID</td>
<td>OC</td>
<td colspan="23"><i>reserviert</i></td>
<td>RHSC</td>
<td>FNO</td>
<td>UE</td>
<td>RD</td>
<td>SF</td>
<td>WDH</td>
<td>SO
</td></tr></tbody></table>

**MIE/MID** (MasterInterruptEnable/MasterInterruptDisable): Aktiviert/Deaktiviert alle Interrupts.

------------------------------------------------------------------------

#### Zeiger-Register

- **HcHCCA** (0x18)

Enthält die Adresse der HCCA, die an einer 256 Byte Grenze ausgerichtet sein muss.

- **HcPeriodCurrentED** (0x1C)

Zeiger auf den aktuellen ED der periodischen Transfers

- **HcControlHeadED** (0x20) und **HcControlCurrentED** (0x24)

Zeiger auf den ersten bzw. aktuellen ED der Transfers in der Liste der Control-Transfers

- **HcBulkHeadED** (0x28) und **HcBulkCurrentED** (0x2C)

Zeiger auf den ersten bzw. aktuellen ED der Transfers in der Liste der Bulk-Transfers

- **HcDoneHead** (0x30)

Wenn der HC einen TD abgearbeitet hat, dann hängt er ihn an die Done-Liste an und schreibt dessen Adresse in der Liste in dieses Reigster. Wenn das WDH-Bit in HcInterruptStatus gelöscht ist, dann schreibt der HC diesen Wert in HccaDoneHead und setzt das WDH-Bit. Daher sollte das Betriebssystem diesen Wert nur aus HccaDoneHead lesen und dann das WDH-Bit löschen.

------------------------------------------------------------------------

#### Frame Register

- **HcFmInterval** (0x34)

<table>
<tbody><tr>
<th>Bit</th>
<th>31</th>
<th>30</th>
<th>29</th>
<th>28</th>
<th>27</th>
<th>26</th>
<th>25</th>
<th>24</th>
<th>23</th>
<th>22</th>
<th>21</th>
<th>20</th>
<th>19</th>
<th>18</th>
<th>17</th>
<th>16</th>
<th>15</th>
<th>14</th>
<th>13</th>
<th>12</th>
<th>11</th>
<th>10</th>
<th>9</th>
<th>8</th>
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
<td>Bedeutung</td>
<td>FIT</td>
<td colspan="16">FSMPS</td>
<td colspan="2"><i>reserviert</i></td>
<td colspan="14">FI
</td></tr></tbody></table>

**FIT** (FrameIntervalToggle): Muss gesetzt werden, wenn in FI ein neuer Wert geschrieben wird.

**FSMPS** (FSLargestDataPacket): Maximale Anzahl von Bits, die in einem Packet gesendet werden können.

**FI** (FrameInterval): Länge eines Frames in Bits (Standart ist 11,999).

- **HcFmRemaining** (0x38)

<table>
<tbody><tr>
<th>Bit</th>
<th>31</th>
<th>30</th>
<th>29</th>
<th>28</th>
<th>27</th>
<th>26</th>
<th>25</th>
<th>24</th>
<th>23</th>
<th>22</th>
<th>21</th>
<th>20</th>
<th>19</th>
<th>18</th>
<th>17</th>
<th>16</th>
<th>15</th>
<th>14</th>
<th>13</th>
<th>12</th>
<th>11</th>
<th>10</th>
<th>9</th>
<th>8</th>
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
<td>Bedeutung</td>
<td>FRT</td>
<td colspan="17"><i>reserviert</i></td>
<td colspan="14">FR
</td></tr></tbody></table>

**FR** (FrameRemaining): Anzahl der Bits, die in diesem Frame noch übertragen werden.

**FRT** (FrameRemainingToggle): Dient dem HC zur Synchronisation zwischen FrameRemaining und FrameInterval.

- **HcFmNumber** (0x3C)

<table>
<tbody><tr>
<th>Bit</th>
<th>31</th>
<th>30</th>
<th>29</th>
<th>28</th>
<th>27</th>
<th>26</th>
<th>25</th>
<th>24</th>
<th>23</th>
<th>22</th>
<th>21</th>
<th>20</th>
<th>19</th>
<th>18</th>
<th>17</th>
<th>16</th>
<th>15</th>
<th>14</th>
<th>13</th>
<th>12</th>
<th>11</th>
<th>10</th>
<th>9</th>
<th>8</th>
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
<td>Bedeutung</td>
<td colspan="16"><i>reserviert</i></td>
<td colspan="16">FN
</td></tr></tbody></table>

**FN** (FrameNumber): Wird bei jedem neuen Frame inkrementiert und in HccaFrameNumber geschrieben. Nach dem Wert 0xFFFF gibt es einen Wraparound zum Wert 0x00.

- **HcPeriodicStart** (0x40)

<table>
<tbody><tr>
<th>Bit</th>
<th>31</th>
<th>30</th>
<th>29</th>
<th>28</th>
<th>27</th>
<th>26</th>
<th>25</th>
<th>24</th>
<th>23</th>
<th>22</th>
<th>21</th>
<th>20</th>
<th>19</th>
<th>18</th>
<th>17</th>
<th>16</th>
<th>15</th>
<th>14</th>
<th>13</th>
<th>12</th>
<th>11</th>
<th>10</th>
<th>9</th>
<th>8</th>
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
<td>Bedeutung</td>
<td colspan="18"><i>reserviert</i></td>
<td colspan="14">PS
</td></tr></tbody></table>

**PS** (PeriodicStart): Anzahl der Bits, die in einem Frame übertragen werden müssen, bis der HC Periodische Transfers ausführt.

- **HcLSThreshold** (0x44)

<table>
<tbody><tr>
<th>Bit</th>
<th>31</th>
<th>30</th>
<th>29</th>
<th>28</th>
<th>27</th>
<th>26</th>
<th>25</th>
<th>24</th>
<th>23</th>
<th>22</th>
<th>21</th>
<th>20</th>
<th>19</th>
<th>18</th>
<th>17</th>
<th>16</th>
<th>15</th>
<th>14</th>
<th>13</th>
<th>12</th>
<th>11</th>
<th>10</th>
<th>9</th>
<th>8</th>
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
<td>Bedeutung</td>
<td colspan="20"><i>reserviert</i></td>
<td colspan="12">LST
</td></tr></tbody></table>

**LST** (LSThreshold): Anzahl der Bits, die in einem Frame mindestens noch übertragen werden, damit der HC noch einen LowSpeed-Transfer durchführt. Dieser Wert darf nur gelesen werden!

------------------------------------------------------------------------

#### Root-Hub-Register

- **HcRhDescriptorA** (0x48)

//TODO

- **HcRhDescriptorB** (0x4C)

//TODO

- **HcRhStatus** (0x50)

//TODO

- **HcRhPortStatus**\[1\] (0x54)

//TODO

### Host Controller Communications Area (HCCA)

| Offset | Größe | Feld | Lesen | Schreiben | Beschreibung |
| -------- | ------- | --------------------- | ------- | ----------- | -------------------------------------------------------------------- |
| 0x00 | 128 | HccaInterrruptTable | x | \- | 32 Zeiger auf Interrupt Transfers |
| 0x80 | 2 | HccaFrameNumber | \- | x | Laufende Frame Nummer für periodische Transfers |
| 0x82 | 2 | HccaPad1 | \- | x | Der HC setzt dieses Feld auf Null, wenn er HccaFrameNumber ändert. |
| 0x84 | 4 | HccaDoneHead | \- | x | Zeiger auf den ersten TD in der Done-Liste |
| 0x88 | 116 | *reserviert* | x | x |  |

## Transfers

### Arten

Das OHCI teilt die vier Transferarten in zwei Gruppen ein: periodische und nicht-periodische.

- Control Transfer: Nicht-periodischer Transfer mit geringen Datenmengen zur Konfguration von USB-Geräten
- Bulk Transfer: Nicht-periodischer Transfer mit hohen Datenmengen, die verlustfrei zwischen USB-Gerät und HC transferiert werden
- Interrupt Transfer: Periodischer Transfer mit gernigen Datenmengen, die in regelmäßigen Abständen beim USB-Gerät abgefragt werden
- Isochronous Transfers: Periodischer Transfer zur (meist verlustbehafteten) Übertragung von großen Datenmengen

### Einteilung der Frames

Der HC teilt die einzelnen Frames in drei Abschnitte ein, in denen er die unterschiedlichen Transferlisten abarbeitet. Die Länge dieser Abschnitte wird über die Register HcPeriodicStart und das Feld ControlBulkServiceRatio (CBSR) in HcControl beeinflusst:

- Vorm ersten Abschnitt sendet der HC ein StartOfFrame-Signal (SOF).
- Im ersten Abschnitt werden die nicht periodischen Transfers abgearbeitet. Wieviele Bulk- und Control-Transfers dies sind, wird mit dem CBSR-Feld beeinflusst.
- Wenn mehr Bits gesendet wurden, als in HcPeriodicStart vorgegeben sind, dann beginnt Abschnitt 2, in dem die periodischen Transfers abgearbeitet werden.
- Im dritten Abschnitt werden die verbleibenden Bits im Frame wieder mit nicht-periodischen Transfers gefüllt.

### Organisation von Transfers

#### Organisation von nicht-periodischen Transfers

Die Organisation der Datentransfers erfolgt über zwei Datenstrukturen, die über einfach verkettete Listen miteinander verknüpft sind. Die Datenstrukturen sind zum einen der Endpoint Descriptor (ED) und zum anderen der Transfer Descriptor (TD). Die EDs beschreiben genau einen Endpunkt einer Funktion (d.h. eines USB-Geräts). Die TDs beschreiben einen Transfer, der einem Endpunkt zugeordnet wird. Die EDs sind in einfach verketteten Listen organisiert. Von diesen Listen gibt es zwei für die nicht-periodischen, d.h. Bulk und Control Transfers. Die Zeiger auf die Anfänge dieser Listen sind in den Registern HcBulkHeadED sowie HcControlHeadED gespeichert. Jeder ED enthält wiederum einen Zeiger auf den Kopf einer verketteten Liste von TDs, die für diesen Endpunkt ausgeführt werden sollen, zB:

    HcBulkHeadED
     |
     V
     ED --> ED --> ED --> ED --> ED --> ED
     |       |            |      |
     V       V            V      V
     TD      TD           TD     TD
             |                   |
             V                   V
             TD                  TD
                                 |
                                 V
                                 TD

Es ist dabei Aufgabe des USB-Treibers diese Listen im Arbeitsspeicher anzulegen, wobei beide Deskriptoren an 16 Byte Grenzen im Arbeitsspeicher ausgerichtet sein müssen. Außerdem muss der Treiber die Felder *HcBulkHeadED*, *HcControlHeadED* sowie die Bits *CLE/BLE* im Feld *HcControl* sowie *CLF/BLF* in *HcCommandStatus* entsprechend zu setzen. Es ist dann Aufgabe des HCs die Listen abzuarbeiten und die Felder *HcBulkCurrentED* und HcControlCurrentED zu setzen. Außerdem entfernt er die TDs und fügt sie in die sogenannte Done-Liste ein, auf die *HcDoneHead* zeigt.

##### Aufbau EndpointDescriptor

<table>
<tbody><tr>
<th>Bit</th>
<th>31</th>
<th>30</th>
<th>29</th>
<th>28</th>
<th>27</th>
<th>26</th>
<th>25</th>
<th>24</th>
<th>23</th>
<th>22</th>
<th>21</th>
<th>20</th>
<th>19</th>
<th>18</th>
<th>17</th>
<th>16</th>
<th>15</th>
<th>14</th>
<th>13</th>
<th>12</th>
<th>11</th>
<th>10</th>
<th>9</th>
<th>8</th>
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
<td>DWORD 1</td>
<td colspan="6"><i>??</i></td>
<td colspan="11">MPS</td>
<td>F</td>
<td>K</td>
<td>S</td>
<td colspan="2">D</td>
<td colspan="4">EN</td>
<td colspan="7">FA
</td></tr>
<tr>
<td>DWORD 2</td>
<td colspan="28">TD Queue Tail Pointer (TailP)</td>
<td colspan="4"><i>??</i>
</td></tr>
<tr>
<td>DWORD 3</td>
<td colspan="28">TD Queue Head Pointer (HeadP)</td>
<td colspan="2">0</td>
<td>C</td>
<td>H
</td></tr>
<tr>
<td>DWORD 4</td>
<td colspan="28">Next Endpoint Descriptor (NextED)</td>
<td colspan="4"><i>??</i>
</td></tr></tbody></table>

//TODO: Beschreibung der Felder

##### Aufbau TransferDescriptor

<table>
<tbody><tr>
<th>Bit</th>
<th>31</th>
<th>30</th>
<th>29</th>
<th>28</th>
<th>27</th>
<th>26</th>
<th>25</th>
<th>24</th>
<th>23</th>
<th>22</th>
<th>21</th>
<th>20</th>
<th>19</th>
<th>18</th>
<th>17</th>
<th>16</th>
<th>15</th>
<th>14</th>
<th>13</th>
<th>12</th>
<th>11</th>
<th>10</th>
<th>9</th>
<th>8</th>
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
<td>DWORD 1</td>
<td colspan="4">CC</td>
<td colspan="2">EC</td>
<td colspan="2">T</td>
<td colspan="3">DI</td>
<td colspan="2">DP</td>
<td>R</td>
<td colspan="18"><i>??</i>
</td></tr>
<tr>
<td>DWORD 2</td>
<td colspan="32">Current Buffer Pointer (CBP)
</td></tr>
<tr>
<td>DWORD 3</td>
<td colspan="28">Next TD (NextTD)</td>
<td colspan="4">0
</td></tr>
<tr>
<td>DWORD 4</td>
<td colspan="32">Buffer End (BE)
</td></tr></tbody></table>

//TODO: Beschreibung der Felder

#### Organisation von Interrupt Transfers

Die Organisation von Interrupt Transfers funktioniert über 32 Interrupt-Transfer-Listen, die verkettete Listen von Interrupt EDs sind. Die Zeiger auf diese Listen liegen in der HCCA an Offset 0x00. In jedem Frame wird eine Interrupt-Transfer-Liste abgearbeitet. Dafür verwendet der HC den Zeiger aus der HccaInterrruptTable, dessen Index den unteren 5 Bits aus HccaFrameNumber besteht. Ein ED kann in mehreren Interrupt-Transfer-Listen auftachen, wodurch er entsprechend öfter abgearbeitet wird.

#### Organisation von Isochronous Transfers

//TODO

## Initialisierung des HCs

### Finden eines OHCI kompatiblen Host Controller

Bei PCs sind die Host Controller über den PCI-Bus mit der CPU verbunden. Man muss also die Konfigurationsadressräume nach einem Geräte mit dem Classcode 0x0C und der Subclass 0x03 durchsuchen. Weitere Informationen dazu im Artikel zum [PCI](https://github.com/lowlevel-eu/wiki/wiki/Peripheral-Component-Interconnect "PCI"). Das DWord an Offset 0x10 im Konfigurationsadressraum enthält die Basisadresse der Register. Bei diesen sollte man nun zuerst das *HcRevision* Feld überprüfen, welches den Wert 0x10 enthalten muss. Andernfalls ist der HC mit dieser Spezifikation möglicherweise nicht kompatibel.

### Kontrolle über den Host Controller übernehmen

Nun muss der [SMI](https://github.com/lowlevel-eu/wiki/wiki/SMI "SMI") deaktiviert werden, der momentan die Steuerung des HCs übernimmt. Dafür muss nur das OCR-Bit in HcCommandStatus gesetzt werden. Wenn der SMI erfolgreich deaktiviert wurde, setzt der HC das IR-Bit in HcControl. Sollte sich die CPU im [Real Mode](https://github.com/lowlevel-eu/wiki/wiki/Real-Mode "Real Mode") befinden, dann ist möglicherweise der [BIOS](https://github.com/lowlevel-eu/wiki/wiki/Basic-Input-Output-System "BIOS") USB-Treiber aktiv, der ebenfalls deaktiviert werden muss.

### Host Controller zurücksetzen

Vor dem Zurücksetzen muss der Wert des Registers *HcFmInterval* gesichert werden. Dann wird das HCR Bit in *HcCommandStatus* gesetz, um den HC zurückzusetzen. Der HC darf nicht länger als 10µs für den Reset benötigen, diese Zeit sollte der Treiber warten.

### Host Controller einrichten

1.  Die HCCA anlegen, ihre Adresse in HcHCCA eintragen
2.  CLE/BLE/IE/PLE in *HcControl' löschen, andernfalls müssen die entsprechenden Listen angelegt werden!*
3.  Speicher für die Done-Liste reservieren und deren physikalische Adresse in HcDoneHead eintragen
4.  *HcPeriodicStart* auf 90% vom ursprünglichen Wert von *HcFmInterval* setzen
5.  In *HcInterruptEnable* gewünschte Interrupts aktivieren
6.  HCFS in *HcControl* auf 10b (USB_OPERATIONAL) setzen
7.  Innerhalb von 1ms beginnt der HC nun SOF-Tokens zu senden, womit er auch mit Transfers beginnt.

## Weblinks

- [Open Host Controller Interface Specification V1.0a](http://h18000.www1.hp.com/productinfo/development/openhci.html)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/11241/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1575/index.html)

<!-- MediaWiki page 1575; revision 11241; parent 10089; 2014-12-29T18:28:27Z -->
