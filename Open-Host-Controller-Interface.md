# Open Host Controller Interface

Diese Seite ist ein Artikel, welcher **mehr** haben könnte..  

Wenn du mehr darüber weißt oder recherchieren willst, bist **du** aufgerufen, dies zu tun. Wenn du dir in einer Sache nicht sicher bist, dann stell es auf die Diskussionsseite.

Diese Seite oder Abschnitt ist zwar komplett, es wird aber folgende Verbesserungen gewünscht:  

- Die Liste der Register vervollständigen (Spezifikation: Seite 125ff)
- Abschnitt über die HCCA vervollständigen (Spezifikation: Seite 48ff)
- Periodische Transfers (Spezifikation: Seite 39ff und 48ff)
- Initialisierung des HCs

Hilf Lowlevel, den Artikel zu verbessern.

Das OHCI ist neben dem UHCI ein Interface für USB-1.x- und Firewire-Hostcontroller (HC). Zum Verständnis dieses Artikels ist die Kenntnis des [USB](https://github.com/lowlevel-eu/wiki/wiki/Universal-Serial-Bus "USB")-Protoklls Vorraussetzung.

## Kommunikation mit dem HC

Die Kommunikation mit dem HC erfolgt über zwei Wege, zum einen über in den Arbeitsspeicher eingeblendete Reigster, zum anderen über einen gemeinsamen Speicherbereich im Arbeitsspeicher. Dieser Speicherberiech enthält zum einen die sogenannte Host Controller Communications Area (HCCA) und zum anderen verkettete Listen, die die Abfolge der zu erledigenden Transfers enthalten.

### Register

Die Register sind in den Arbeitsspeicher eingeblendet. Ihre Adresse ist allerdings nicht fix. Da der HC aber in der Regel über einen PCI-Bus an die CPU angeschlossen ist, kann man von diesem die Adresse abrufen. Dafür durchläuft man die einzelnen Konfigurations-Adressräume nach einem Gerät mit der Class 0x0C (Serielle Buscontroller) und der Subclass 0x03. Das DWord an Offset 0x10 ist die Adresse der Register. Die angesprochenen Register sind alle 32 Bit breit (Offset in Klammern)

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

**CBSR** (ControlBulkServiceRatio): In einem Frame werden sowohl Transfers für Bulk-Endpunkte als auch für Control-Endpunkte durchgeführt. Hier wird spezifiziert, wieviele Control-Endpunkte auf einen Bulk-Endpunkt kommen: 00b = 1:1, 01b = 2:1, 10b = 3:1, 11b = 4:1

**PLE** (PeriodicListEnable): Ist dieses Bit gestzt, dann arbeitet der HC die Liste mit periodischen Transfers ab (-\> HcPeriodCurrentED)

**IE** (IsochronousEnable): Ist dieses Bit gestzt, dann führt der HC auch Isochronous Transfers in der Liste der periodischen Transfers aus

**CLE** (ControlListEnable): Ist dieses Bit gestzt, dann arbeitet der HC die Liste mit Control Transfers ab (-\>HcControlCurrentED)

**BLE** (BulkListEnable): Ist dieses Bit gestzt, dann arbeit der HC die Liste mit Bulk Transfers ab (-\>HcBulkCurrentED)

**HCFS** (HostControllerFunctionalState): Der Zustand, in den der HC den USB setzen soll: 00b=USB_RESET, 01b=USB_RESUME, 10b=USB_OPERATIONAL, 11b=USB_SUSPEND

**IR** (InterruptRouting): Ist dieses Bit gesetzt, dann werden alle Interrupts vom [SMI](https://github.com/lowlevel-eu/wiki/wiki/SMI "SMI") behandelt. Ist es gelöscht, werden Interrupts vom Betriebssystem behandelt.

**RWC** (RemoteWakeupConnected): Ist dieses Bit gesetzt, dann unterstützt der HC Remote Wakeup. Dieses Bit sollte nur gelesen werden.

- **HcCommandStatus** (0x08)
- **HcInterruptStatus** (0x0C)
- **HcInterruptEnable** (0x10)
- **HcInterruptDisable** (0x14)
- **HcHCCA** (0x18)
- **HcPeriodCurrentED** (0x1C)
- **HcControlHeadED** (0x20)
- **HcControlCurrentED** (0x24)
- **HcBulkHeadED** (0x28)
- **HcBulkCurrentED** (0x2C)
- **HcDoneHead** (0x30)
- **HcFmInterval** (0x34)
- **HcFmRemaining** (0x38)
- **HcFmNumber** (0x3C)
- **HcPeriodicStart** (0x40)
- **HcLSThreshold** (0x44)
- **HcRhDescriptorA** (0x48)
- **HcRhDescriptorB** (0x4C)
- **HcRhStatus** (0x50)
- **HcRhPortStatus**\[1\] (0x54)

### Host Controller Communications Area (HCCA)

| Offset | Größe | Feld | Lesen | Schreiben | Beschreibung |
| -------- | ------- | --------------------- | ------- | ----------- | -------------------------------------------------------------------- |
| 0x00 | 128 | HccaInterrruptTable | x | \- | 32 Zeiger auf Interrupt Transfers |
| 0x80 | 2 | HccaFrameNumber | \- | x | Laufende Frame Nummer für periodische Transfers |
| 0x82 | 2 | HccaPad1 | \- | x | Der HC setzt dieses Feld auf Null, wenn er HccaFrameNumber ändert. |
| 0x84 | 4 | HccaDoneHead | \- | x | ??? |
| 0x88 | 116 | *reserviert* | x | x |  |

## Transfers

### Arten

Das OHCI teilt die vier Transferarten in zwei Gruppen ein: periodische und nicht-periodische.

- Control Transfer: Nicht-periodischer Transfer mit geringen Datenmengen zur Konfguration von USB-Geräten
- Bulk Transfer: Nicht-periodischer Transfer mit hohen Datenmengen, die verlustfrei zwischen USB-Gerät und HC transferiert werden
- Interrupt Transfer: Periodischer Transfer mit gernigen Datenmengen, die in regelmäßigen Abständen beim USB-Gerät abgefragt werden
- Isochronous Transfers: Periodischer Transfer zur (meist verlustbehafteten) Übertragung von großen Datenmengen

### Organisation von Transfers

#### Organisation von nicht-periodischen Transfers

Die Organisation der Datentransfers erfolgt über zwei Datenstrukturen, die über einfach verkettete Listen miteinander verknüpft sind. Die Datenstrukturen sind zum einen der Endpoint Descriptor (ED) und zum anderen der Transfer Descriptor (TD). Die EDs beschreiben genau einen Endpunkt einer Funktion (d.h. eines USB-Geräts). Die TDs beschreiben einen Transfer, der einem Endpunkt zugeordnet wird. Die EDs sind in einfach verketteten Listen organisiert. Von diesen Listen gibt es zwei für die nicht-periodischen, d.h. Bulk und Control Transfers. Die Zeiger auf die Anfänge dieser Listen sind in den Registern HcBulkHeadED sowie HcControlHeadED gespeichert. Jeder ED enthält wiederum einen Zeiger auf den Kopf einer verketteten Liste von TDs, die für diesen Endpunkt ausgeführt werden sollen.

//BILD

//Aufbau ED / TD

Es ist dabei Aufgabe des USB-Treibers diese Listen im Arbeitsspeicher anzulegen, wobei beide Deskriptoren an 16 Byte Grenzen im Arbeitsspeicher ausgerichtet sein müssen. Außerdem muss der Treiber die Felder HcBulkHeadED, HcControlHeadED sowie die Bits CLE/BLE im Feld HcControl entsprechend zu setzen. Es ist dann Aufgabe des HCs die Listen abzuarbeiten und die Felder HcBulkCurrentED und HcControlCurrentED zu setzen. Außerdem entfernt er die TDs und fügt sie in die sogenannte Done-Liste ein, auf die HcDoneHead zeigt.

#### Organisation von Interrupt Transfers

#### Organisation von Isochronous Transfers

## Initialisierung des HCs

## Weblinks

- [Open Host Controller Interface Specification V1.0a](http://h18000.www1.hp.com/productinfo/development/openhci.html)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/10016/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1575/index.html)

<!-- MediaWiki page 1575; revision 10016; parent 9848; 2011-07-30T14:21:59Z -->
