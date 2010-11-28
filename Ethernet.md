# Ethernet

Ethernet ist eine Datenübertragungstechnik für kabelgebundene LANs. Bis heute wurden Geschwindigkeiten von 10 Mbit/s bis hin zu 100 Gbit/s spezifiziert. Es ist die meistverwendete LAN-Technik und hat andere Standards wie FDDI oder Token-Ring verdrängt. Diese werden nur noch in Spezialbereichen genutzt.

## Ethernetpakete

Es gibt im Grunde zwei Formen von Ethernetpaketen: Ethernet I und Ethernet II. Beide Formen sind kompatibel zueinander. Zu erwähnen ist noch, dass alle Bytes mit dem LSB voran übertragen werden (Little Endian). Words und DWords (bzw. short ints und long ints) werden hingegen (meist) mit dem höchstwertigen Byte voran übertragen. Das Ändern dieser Bytereihenfolge müsst ihr übernehmen (natürlich nur dann, wenn euer OS auf einem Little-Endian-Prozessor (z. B. x86) läuft).

### Ethernet I

[<img src="https://raw.githubusercontent.com/wiki/lowlevel-eu/wiki/assets/ea7a62df1b460e1b00e2.png" width="827" height="62" alt="Ethernet1.png" />](https://raw.githubusercontent.com/wiki/lowlevel-eu/wiki/assets/ea7a62df1b460e1b00e2.png)

Dies ist die "Abbildung" eines Ethernet-I-Paketes. Den Teil, der aus den MAC-Adressen, dem Längenfeld, den Nutzdaten, dem PAD-Feld und der CRC32-Checksumme gebildet wird, nennt man Ethernetframe.

| Feld | Bedeutung |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Präambel | Die Präambel besteht aus sieben Bytes von wechselnden Bits (101010...1010). Sie diente früher dazu, dass sich das Empfangsgerät auf die Abstände der Bits voneinander einstimmen konnte. Heutzutage ist dies unnötig geworden, da diese Synchronisation auch aufrecht erhalten wird, wenn nichts übertragen wird. |
| SFD | Er (der Start Frame Delimiter) markiert mit der Bitfolge 10101011 das Ende der Präambel und den anschließenden Beginn des Ethernetframes. |
| Empfänger-MAC-Adresse | Hier steht die MAC-Adresse des Empfängers. Ein FF:FF:FF:FF:FF:FF bedeutet, dass das Paket an alle Geräte im LAN gerichtet ist. Ein Ethernetpaket kann nur an andere Geräte im gleichen LAN geschickt werden, will man es in ein anderes LAN oder gar in ein WAN (z. B. Internet) übertragen, dann muss es an einen Router gesendet werden, der die Vermittlung zwischen den Netzen übernimmt. |
| Absender-MAC-Adresse | Hier steht die MAC-Adresse des Absenders - also meist deine. |
| Länge | Die Länge der Nutzdaten und des PAD-Feldes zusammen in Bytes. Muss mindestens 46 und darf höchstens 1500 betragen, da der Ethernetframe mindestens 64 Bytes lang sein muss und höchstens 1518 Bytes lang sein darf. |
| Nutzdaten | Hier kommen endlich die Daten, die versendet werden sollen (zum Beispiel ARP- oder IP-Pakete). Die Nutzdaten müssen zwischen 0 (sic!) und 1500 Bytes lang sein. |
| PAD | Ist das Nutzdatenfeld kürzer als 46 Bytes, so muss hier aufgefüllt werden, damit Nutzdaten und PAD zusammen 46 Bytes lang sind. Gibt es zum Beispiel nur 28 Bytes Nutzdaten (wie bei einem ARP-Request), dann muss PAD 46-28=18 Bytes lang sein. Man trägt am besten Nullen ein. |
| CRC32 | Hier steht noch eine CRC32-Prüfsumme, um die Korrektheit der Daten zu gewährleisten. Sie wird über den Ethernetframe ohne dieses Feld berechnet (also über die MAC-Adressen, das Längenfeld, die Nutzdaten und das PAD-Feld). |

### Ethernet II

[<img src="https://raw.githubusercontent.com/wiki/lowlevel-eu/wiki/assets/251c283c3864cad6e788.png" width="827" height="62" alt="Ethernet2.png" />](https://raw.githubusercontent.com/wiki/lowlevel-eu/wiki/assets/251c283c3864cad6e788.png)

Ein Ethernet-II-Paket unterscheidet sich nur geringfügig von einem Ethernet-I-Paket: Statt dem Längenfeld gibt es ein Typfeld, welches den Typ der Nutzdaten angibt. Der Wert im Typfeld ist stets größer als 0x0600 (1536), sodass zwischen Ethernet-I-Paketen (der Wert muss kleiner oder gleich 0x05DC (1500) sein) und zwischen Ethernet-II-Paketen unterschieden werden kann. Wichtige Typwerte sind 0x0800 ([IP](https://github.com/lowlevel-eu/wiki/wiki/Internet-Protocol "Internet Protocol")) und 0x0806 ([ARP](https://github.com/lowlevel-eu/wiki/wiki/Address-Resolution-Protocol "Address Resolution Protocol")).

## Was muss ich senden?

Heutzutage wird Ethernet I kaum noch verwendet. Daher ist es ratsam, Ethernet-II-Pakete zu benutzen.

An die [Netzwerkkarte](https://lowlevel-eu.github.io/wiki/pages/1826/index.html "Kategorie:Netzwerkkarte") übergibt man nur den Ethernetframe. Präambel und SFD fügt die Karte selbst an. Üblicherweise kann man das CRC32-Feld auch weglassen und die Netzwerkkarte berechnet dieses für dich und fügt es automatisch an das Paket an.

## Weblinks

- [Wikipedia-Artikel "Ethernet"](http://de.wikipedia.org/wiki/Ethernet)
- [Englischer Wikipedia-Artikel zu Ethernet II](http://en.wikipedia.org/wiki/Ethernet_II_framing)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/9004/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1876/index.html)

<!-- MediaWiki page 1876; revision 9004; parent 7594; 2010-11-28T10:32:24Z -->
