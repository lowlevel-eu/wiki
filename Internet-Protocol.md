# Internet Protocol

Das Internet Protocol (IP) ist ein sehr weit verbreitetes Netzwerkprotokoll. Es ist die Grundlage des Internets, daher auch der Name. Es wird sehr häufig zusammen mit dem Transfer Control Protocol (TCP) verwendet, das auf dem IP aufbaut.

## Nutzen

In [Ethernetnetzwerken](https://github.com/lowlevel-eu/wiki/wiki/Ethernet "Ethernet") baut IP direkt auf Ethernet auf. Ethernetpakete können nur innerhalb eines LANs verschickt werden, da es zum Beispiel im Internet kein Ethernet gibt. Das IP ermöglicht es, Pakete in andere LANs oder über Internetworks (wie das Internet) zu verschicken, da die IP-Adresse eine logische und keine physikalische Adresse wie die MAC-Adresse ist. Daher muss keine direkte Verbindung zum Ziel bestehen, sondern nur eine logische, die über mehrere Zwischenstationen (z. B. Router) verlaufen kann. Mit Protokollen wie Ethernet können nur direkte Verbindungen (zum Beispiel zum Router) hergestellt werden.

## Aufbau von IP-Paketen

### Übersicht

<table>
<tbody><tr>
<td>0</td>
<td>4</td>
<td>8</td>
<td>12</td>
<td>16</td>
<td>20</td>
<td>24</td>
<td>28</td>
<td>31
</td></tr>
<tr>
<td colspan="1">Version</td>
<td colspan="1">Headerlänge</td>
<td colspan="2">Priorität</td>
<td colspan="5">Paketlänge
</td></tr>
<tr>
<td colspan="4">Paket-ID</td>
<td colspan="5">Fragment Offset und Flags
</td></tr>
<tr>
<td colspan="2">TTL</td>
<td colspan="2">Protokolltyp</td>
<td colspan="5">Prüfsumme
</td></tr>
<tr>
<td colspan="9">Absender-IP
</td></tr>
<tr>
<td colspan="9">Ziel-IP
</td></tr>
<tr>
<td colspan="9">evtl. Optionen
</td></tr>
</tbody></table>

  

### Genaue Betrachtung

Bitte beachten: Wie bei vielen Netzwerkprotokollen wird auch bei IP Big-Endian verwendet.

| Offset | Länge | Beschreibung |
| ------------ | --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 0x00 | 0,5 | Version (4 für IPv4) |
| 0x00 + 1/2 | 0,5 | Länge des Headers in DWords (Also 5 (denn 5 \* 4B = 20B), wenn keine Optionen verwendet werden) |
| 0x01 | 1 | Priorität (z. B. 0 (normal)) |
| 0x02 | 2 | Größe von Header und Daten zusammen in Bytes |
| 0x04 | 2 | ID des Paketes (z. B. 0x0000, wird für Fragmentation benötigt) |
| 0x06 | 2 | Fragment Offset und Flags (auf 0x4000 (bzw. 0x0040 für Little-Endian) setzen, um Fragmentation zu deaktivieren) |
| 0x08 | 1 | TTL (Time to Live, wird von jeder Station, die das Paket weiterleitet um eins dekrementiert, ist der Wert 0, so wird das Paket verworfen, dies verhindert, dass Pakete im Kreis geleitet werden und so das Netzwerk unnötig überlasten; ein Standardwert ist 128) |
| 0x09 | 1 | Protokoll (gibt das in den Nutzdaten verwendete Protokoll an (z. B. 0x01 für ICMP, 0x06 für TCP, 0x11 für UDP)) |
| 0x0A | 2 | Prüfsumme (siehe [Netzwerkprüfsumme](https://github.com/lowlevel-eu/wiki/wiki/Netzwerkpr%C3%BCfsumme "Netzwerkprüfsumme") zur Berechnung, wird ausschließlich über den Kopf berechnet) |
| 0x0C | 4 | IP des Absenders |
| 0x10 | 4 | IP des Empfängers |
| 0x14 | Länge des Headers - 20 | Hier können noch Optionen angegeben werden, wie das Paket zu behandeln ist. Die Größe dieses Feldes muss immer ohne Rest durch vier teilbar sein (da die Länge des Headers in Viererschritten angegeben wird), daher muss es gegebenenfalls mit Nullbytes aufgefüllt werden. |
| 0x14+? | Gesamtlänge - Länge des Headers | Die Nutzdaten |

Im Typfeld des Ethernetpaketes muss übrigens 0x0800 für IP eingetragen werden.

### Fragmentierung

IP-Pakete können in mehrere Pakete unterteilt werden. So unterstützt z. B. Ethernet nur ca. 1,5-kB-Pakete. Um diese Grenze zu umgehen, kann man IP-Pakete so unterteilen, dass sie z. B. in 1-kB-Paketen gesendet werden können. Diese Fragmentierung wird jedoch kaum verwendet, da höhere Protokolle wie TCP dies auch unterstützen. Diese werden somit weitaus häufiger zur Fragmentierung verwendet (gerade bei TCP ist diese Fragmentierung sehr wichtig, da die Daten dem Anwender als ein Datenstrom und nicht als einzelne Datenpakete erscheinen sollen).

### C-Struktur

Hier noch eine C-Struktur für einen IP-Paketheader, funktionsfähig zumindest für i386: \<c\>typedef uint32_t IP_t; struct ip_header {

     unsigned headerlen : 4; //Vertauscht, da höherwertige Bits zuerst kommen (Big Endian wird nur für die Bytereihenfolge verwendet)
     unsigned version : 4;
     uint8_t  priority;
     uint16_t packetsize;
     uint16_t id;
     uint16_t fragment;
     uint8_t  ttl;
     uint8_t  protocol;
     uint16_t checksum;
     IP_t     sourceIP;
     IP_t     destinationIP;

} \_\_attribute\_\_((packed));\</c\>

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/9771/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1970/index.html)

<!-- MediaWiki page 1970; revision 9771; parent 8656; 2011-05-12T14:33:08Z -->
