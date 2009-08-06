# Address Resolution Protocol

Das Address Resolution Protocol (ARP) dient dazu, Netzwerkadressen zu physikalischen Adressen (bzw. Hardwareadressen) aufzulösen. Es wird fast ausschließlich in [Ethernetnetzwerken](https://github.com/lowlevel-eu/wiki/wiki/Ethernet "Ethernet") verwendet, um [IPv4](https://github.com/lowlevel-eu/wiki/wiki/Internet-Protocol "Internet Protocol")-Adressen zu MAC-Adressen aufzulösen.

## Ablauf

Wenn ein Computer A ein IP-Paket zu einem anderen Computer B im Netzwerk senden will, muss er dessen IP-Adresse kennen. Damit B das Paket sicher empfängt, muss jedoch auch dessen MAC-Adresse bekannt sein. Diese wird mittels ARP bestimmt. Dazu sendet A einen ARP-Request, in welchem er seine eigene MAC-Adresse, seine IP-Adresse und die IP-Adresse von B einträgt. Dieser Request wird an alle Computer im Netzwerk gesendet, indem als Ziel-MAC-Adresse FF:FF:FF:FF:FF:FF eingetragen wird. Der Computer mit der angegebenen IP-Adresse - also B - sollte dann mit einem ARP-Reply antworten. Dort trägt er seine MAC-Adresse, seine IP-Adresse, die IP-Adresse von A und die MAC-Adresse von A ein. A wird dieses Paket empfangen und kann dort die MAC-Adresse von B auslesen.

Die Zuordnung IP \<-\> MAC sollte dann von A in einem ARP-Cache eingetragen werden, damit A nicht vor jedem Paket nach der MAC-Adresse von B fragen muss. B muss nun übrigens keinen ARP-Request an A senden, um dessen MAC-Adresse herauszufinden, da B diese Adresse aus dem ARP-Request von A herauslesen kann.

## Aufbau von ARP-Paketen

Bitte beachten: Wie bei vielen Netzwerkprotokollen wird auch bei ARP Big-Endian verwendet.

| Offset | Länge | Beschreibung |
| -------- | ------- | --------------------------------------------------- |
| 0x00 | 2 | Hardwareadresstyp (0x0001 für Ethernet, also MAC) |
| 0x02 | 2 | Netzwerkadresstyp (0x0800 für IPv4) |
| 0x04 | 1 | Hardwareadresslänge (6 Bytes für MAC-Adressen) |
| 0x05 | 1 | Netzwerkadresslänge (4 Bytes für IPv4-Adressen) |
| 0x06 | 2 | Typ der Operation (1 für Request, 2 für Reply) |
| 0x08 | 6 | MAC-Adresse des Absenders |
| 0x0E | 4 | IP-Adresse des Absenders |
| 0x12 | 6 | MAC-Adresse des Zieles |
| 0x18 | 4 | IP-Adresse des Zieles |

Bei unbekannter MAC-Adresse wird im Ethernetpaket als Ziel-MAC-Adresse FF:FF:FF:FF:FF:FF eingetragen und im ARP-Paket zum Beispiel 00:00:00:00:00:00 (wobei man dort theoretisch irgendeine beliebige Adresse eintragen könnte).

Im Typfeld des Ethernetpaketes muss übrigens 0x0806 für ARP eingetragen werden.

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/5250/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1937/index.html)

<!-- MediaWiki page 1937; revision 5250; parent 5105; 2009-08-06T15:08:23Z -->
