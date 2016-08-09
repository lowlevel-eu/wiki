# Accelerated Graphics Port

Der **Accelerated Graphics Port** (kurz: **AGP**) ist ein [Bus](https://lowlevel-eu.github.io/wiki/pages/1769/index.html "Kategorie:Bus") zum Anschluss von Grafikkarten. Die Schnittstelle basiert auf [PCI](https://github.com/lowlevel-eu/wiki/wiki/Peripheral-Component-Interconnect "PCI"), bietet jedoch höhere Transferraten und eine Anbindung der Grafikkarte an den Speicher (GART) an. Mittlerweile wurde die Schnittstelle von PCI-Express abgelöst.

## Registerstruktur

Die relevanten Register liegen im PCI-Konfigurationsraum in einer Capability mit der ID 0x2. Aus dieser Struktur können die Eigenschaften der Karte ausgelesen und AGP aktiviert werden. Die Capability ist folgendermaßen formatiert (Die Benennung folgt der AGP-3.0-Spezifikation):

<table>
<tbody><tr>
<th>Offset</th>
<th>Register-Name</th>
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
<td>0x00</td>
<td>NCAPID</td>
<td colspan="8">Reserviert</td>
<td colspan="4">MAJOR</td>
<td colspan="4">MINOR</td>
<td colspan="8">NEXT_PTR</td>
<td colspan="8">CAP_ID = 0x2
</td></tr>
<tr>
<td>0x04</td>
<td>AGPSTAT</td>
<td colspan="8">RQ</td>
<td colspan="8">Reserviert</td>
<td colspan="3">ARQSZ</td>
<td colspan="3">CAL_Cycle</td>
<td>SBA</td>
<td colspan="2">Reserviert</td>
<td>htrans#</td>
<td>OVER4G</td>
<td>FW</td>
<td>AGP3.0_MODE</td>
<td colspan="3">RATE
</td></tr>
<tr>
<td>0x08</td>
<td>AGP_CMD</td>
<td colspan="8">PRQ</td>
<td colspan="8">Reserviert</td>
<td colspan="3">PARQSZ</td>
<td colspan="3">PCAL_Cycle</td>
<td>SBA_ENABLE</td>
<td>AGP_ENABLE</td>
<td colspan="2">Reserviert</td>
<td>OVER4G</td>
<td>FW_ENABLE</td>
<td>Reserviert</td>
<td colspan="3">DRATE
</td></tr>
<tr>
<td>0x12</td>
<td>...</td>
<td colspan="32">Optionale Register...
</td></tr></tbody></table>

Die Register unterscheiden sich in ihrer Bedeutung für sog. Master- und Target-Geräte, sowie zwischen Versionen 2.0 und 3.0 der Spezifikation. Grün hinterlegte Felder sind nur in AGP 3.0 definiert. Nur auf einige dieser Unterschiede wird im Folgenden eingegangen.

## Erkennung

Grundsätzlich werden AGP-Gerate wie gewöhnliche PCI-Geräte enumeriert. Anhand der o.g. Capability können sie von normalen PCI-Geräten unterschieden werden. Im zweiten Schritt können dann anhand des Felder MAJOR zwischen den Spezifikationen 2.0 und 3.0 unterschieden werden. Allerdings bedeutet ein Wert von "3" als Major-Version nicht, dass die Karte im AGP-3.0-Modus läuft; dies wird zwischen Grafikkarte und Mainboard automatisch ausgehandelt. Wenn sich die Geräte auf AGP 3.0 geeinigt haben, ist AGP3.0_MODE gesetzt.

## Aktivierung und Einstellungen

Das Betriebssystem ist für die Aktivierung von AGP und die Auswahl eines geeigneten Transfermodus verantwortlich. Das [BIOS](https://github.com/lowlevel-eu/wiki/wiki/Basic-Input-Output-System "BIOS") übergibt die Karte mit abgeschaltetem AGP-Modus, sodass sie mit der Geschwindigkeit eines PCI-Gerätes läuft. AGP wird aktiviert, wenn im Register AGP_CMD das AGP_ENABLE-Bit gesetzt wird.

Im AGP-2.0-Modus werden die Transfermodi 1x, 2x und 4x unterstützt, während im AGP-3.0-Modus die Modi 4x und 8x möglich sind. Die unterstützten Modi können anhand des RATE-Feldes erkannt werden und im DRATE-Feld ausgewählt werden (in letzterem darf nur genau ein Bit gesetzt sein):

| Bit | AGP 2.0 | AGP 3.0 |
| ----- | --------- | ------------ |
| 0 | 1x | 4x |
| 1 | 2x | 8x |
| 2 | 4x | Reserviert |

Weiterhin können Fast-Writes (FW, FW_ENABLE) und Side-Band-Adressing (SBA, SBA_ENABLE) aktiviert werden. Letzteres muss im AGP-3.0-Modus aktiviert werden.

Im PRQ-Feld wird die Höchstzahl der Elemente Request-Queue festgelegt. Der Wert muss kleiner oder gleich der Angabe im Feld RQ sein. (P)ARQSZ gibt die optimale Größe asynchroner Requests an (2^(ARQSZ+4); 0 bedeuetet: keine Empfehlung). PCAL_Cycle muss für AGP-Targets auf das Minimum von CAL_Cycle von Master- und Target-Gerät gesetzt werden.

**Achtung:** Die Angaben im AGPSTAT-Register geben nur Auskunft über die Funktionen, die von dem AGP-Gerät, d.h. der Grafikkarte unterstützt werden, und geben nicht an, ob auch das Mainboard mit diesen umgehen kann.

## Weblinks

- [Spezifikation AGP 3.0](http://www.playtool.com/pages/agpcompat/agp30.pdf)
- [Spezifikation AGP 2.0](http://www.motherboards.org/files/techspecs/agp20.pdf)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/11364/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2660/index.html)

<!-- MediaWiki page 2660; revision 11364; parent 11361; 2016-08-09T17:53:14Z -->
