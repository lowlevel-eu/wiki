# AMD PCnet

Vorlage:Hinweiss

Dieser Artikel beschäftigt sich mit der Programmierung der AMD-PCnet-FAST-III-Netzwerkkarte (Am79C973).

## Einführung

### Vorwort

Wenn ich hier von "Bytes" spreche, meine ich acht Bit große Einheiten. Zwei Bytes (16 Bit) sind ein Word und vier Bytes (32 Bit) ein DWord. Acht Bytes (64 Bit) sind ein QWord. Wenn ich keine Endianess explizit angebe, dann ist Little Endian gemeint.

### Grundlagen

Wie beim [RTL8139](https://github.com/lowlevel-eu/wiki/wiki/RTL8139 "RTL8139")-Tutorial gilt auch hier: Euer Betriebssystem sollte bereits einen gewissen Stand aufweisen, um die Karte erkennen und bedienen zu können. Dies sind also [ISRs](https://github.com/lowlevel-eu/wiki/wiki/Interrupt-Service-Routine "Interrupt Service Routine") für [IRQs](https://github.com/lowlevel-eu/wiki/wiki/Programmable-Interrupt-Controller#irq-tabelle "IRQ"), eine [Speicherverwaltung](https://github.com/lowlevel-eu/wiki/wiki/Speicherverwaltung "Speicherverwaltung") und eine Möglichkeit, die [I/O-Ports](https://github.com/lowlevel-eu/wiki/wiki/I-O-Ports "I/O-Ports") eines bestimmten (anhand von Vendor- und Device-ID) [PCI](https://github.com/lowlevel-eu/wiki/wiki/Peripheral-Component-Interconnect "Peripheral Component Interconnect")-Gerätes herauszufinden.

Mögliche Emulatoren für PCnet sind sowohl [QEMU](https://github.com/lowlevel-eu/wiki/wiki/QEMU "QEMU") als auch [VirtualBox](https://github.com/lowlevel-eu/wiki/wiki/VirtualBox "VirtualBox"). Um die Karte unter QEMU zu benutzen, können zum Beispiel die folgenden Kommandozeilenoptionen angegeben werden:

    qemu -net user -net nic,model=pcnet

Dadurch erstellt QEMU eine virtuelle PCnet-Karte. An der IP-Adresse 10.0.2.2 gibt es einen virtuellen Gateway ins Internet. Um mit VirtualBox die gleiche Konfiguration zu erreichen, muss die PCnet-FAST III (Am79C973) an NAT angeschlossen werden.

Die Netzwerkkarte hat die PCI-Vendor-ID 0x1022 und die Geräte-ID 0x2000.

### Verwendete Resourcen

- I/O-Ports: Es gibt einen I/O-Raum, der dazu dient, einige Register der Netzwerkkarte anzusprechen und die weiteren zu erreichen.
- IRQ: Per IRQ wird der Treiber über eine Statusänderung der Netzwerkkarte informiert (zum Beispiel ist ein Paket eingetroffen oder wurde versendet)

## Zugriff

### Grundlagen

Die "direkt" erreichbaren Register (ein Portzugriff) sind nur ein kleiner Teil der gesamten Register der Karte. Neben ihnen gibt es noch die CSR (Control and Status Register) und die BCR (Bus Control Register). Um auf sie zuzugreifen, muss zuerst die Adresse des Registers in den 16-Bit-I/O-Port RAP (Register Address Port) geschrieben werden. Betrifft diese Adresse eines der CSR, so kann der Wert anschließend am 16-Bit-I/O-Port RDP (Register Data Port) ausgelesen oder verändert werden. Betrifft die Adresse eines der BCR, so handelt es sich nicht um den RDP, sondern um den BDP (BCR Data Port).

### Initialisierung

1\. IRQ und I/O-Ports vom PCI-Treiber holen und gegebenenfalls registrieren

2\. MAC-Adresse herausfinden; diese steht in drei 16-Bit-Registern ab 0x00 (APROM0, APROM2 und APROM4) in Little-Endian-Reihenfolge (also in APROM0 (0x00) die niederwertigsten 16 Bit und in APROM4 (0x04) die höchstwertigen 16 Bit).

3\. Die Karte zurücksetzen; es muss ein Word vom Resetregister (0x14) eingelesen werden, um einen Software-Reset durchzuführen. Anschließend empfiehlt es sich, zehn Millisekunden zu warten, bis der Reset beendet ist. Danach sollte das BCR20-Register auf 0x0102 gesetzt werden, dies verändert den Softwarestyle zu PCnet-PCI, dadurch werden 32-Bit- und nicht 16-Bit-Strukturen verwendet. Außerdem wird dadurch das SSIZE32-Bit gesetzt, auch dadurch werden 32-Bit-Strukturen aktiviert.

4\. Nun muss ein STOP-Reset ausgeführt werden. Dies wird erreicht, indem 0x04 nach CSR0 geschrieben wird.

5\. Puffer zum Senden und Empfangen initialisieren; beide müssen 2 kB groß und physisch kontinuierlich sein.

6\. Nun muss die Karte initialisiert werden. Dies geschieht mittels eines Initialization Block, der folgendermaßen aussieht: \<c\>typedef unsigned int uint;

struct initialization_block {

       uint16_t mode;
       uint     reserved1 : 4;
       uint     receive_length : 4;
       uint     reserved2 : 4;
       uint     transfer_length : 4;
       uint64_t physical_address : 48;
       uint16_t reserved3;
       uint64_t logical_address;
       uint32_t receive_descriptor;
       uint32_t transmit_descriptor;

} \_\_attribute\_\_((packed));\</c\> "reservedX"-Felder sind reserviert. "mode" ist 0x8000, wenn die Karte in den Promiscuous-Mode geschaltet werden soll (Alle Pakete empfangen, nicht nur Broadcasts und die für die eigene MAC-Adresse), sonst 0x0000. "receive_length" gibt die Anzahl der Empfangsdeskriptoren an, dazu später. "transfer_length" enthält im Gegensatz dazu die Anzahl der Sendedeskriptoren. Beide Werte können auf 3 gesetzt werden, dies entspricht jeweils acht Deskriptoren. "physical_address" enthält die MAC-Adresse der Karte. "logical_address" kann auf 0 gesetzt werden. "receive_descriptor" enthält die physische Adresse zu einem 2-kB-Puffer, "transmit_descriptor" zu einem anderen. Beide Puffer müssen physisch kontinuierlich sein und an 16-Bytes-Grenzen ausgerichtet.

7\. Jetzt müssen die Empfangs- und Sendedeskriptoren initialisiert werden. So ein Deskriptor sieht so aus: \<c\>struct descriptor {

       uint32_t address;
       uint32_t flags;
       uint32_t flags2;
       uint32_t avail;

} \_\_attribute\_\_((packed));\</c\> "address" gibt die physische Adresse eines 2-kB-Puffers (physisch kontinuierlich) an, "flags" und "flags2" enthalten Flags (siehe unten), "avail" kann vom Benutzer (also von dir) frei verwendet werden.

8\. Wenn auch die Deskriptoren initialisiert sind, sollte der Initialization Block bei der Karte registriert werden. Hierzu werden die niederwertigen 16 Bits der physischen Adresse in das CSR1-Register und die höherwertigen in das CSR2-Register geschrieben.

9\. Danach muss 0x0041 nach CSR0 geschrieben werden. Das initialisiert die Karte und aktiviert Interrupts. Gleich darauf wird ein IRQ eintreffen. Die ISR sollte einfach den Wert von CSR0 nach CSR0 (sic!) schreiben, um den Interrupt anzunehmen.

10\. Wenn der Interrupt empfangen wurde, sollte der Inhalt von CSR4 mit 0xC00 ge-OR-t und wieder nach CSR4 geschrieben werden. Dadurch werden Pakete, die kleiner als 64 Bytes sind, automatisch auf diese größe vergrößert und einige relativ überflüssige Informationen von empfangenen Paketen entfernt.

11\. Jetzt ist die Initialisierung endlich abgeschlossen und die Karte darf in Betrieb genommen werden, indem 0x42 nach CSR0 geschrieben wird.

### Konstanten

\<c\>//Die Werte, auf die RAP gesetzt werden muss, um dieses Register zu benutzen

1.  define CSR0 0
2.  define CSR1 1
3.  define CSR2 2
4.  define CSR3 3
5.  define CSR4 4
6.  define BCR20 20

//16-Bit-I/O-Ports (bzw. Offsets zum Beginn des I/O-Raums)

1.  define APROM0 0x00
2.  define APROM2 0x02
3.  define APROM4 0x04
4.  define RDP 0x10
5.  define RAP 0x12
6.  define RESET 0x14
7.  define BDP 0x16\</c\>

## Siehe auch

- [Ethernet](https://github.com/lowlevel-eu/wiki/wiki/Ethernet "Ethernet")
- [Address Resolution Protocol](https://github.com/lowlevel-eu/wiki/wiki/Address-Resolution-Protocol "Address Resolution Protocol")
- [Internet Protocol](https://github.com/lowlevel-eu/wiki/wiki/Internet-Protocol "Internet Protocol")

## Weblinks

- [Umfangreiche Spezifikation für die Am79C973 (PCnet-FAST III) und Am79C975](http://www.amd.com/us-en/assets/content_type/white_papers_and_tech_docs/21510.pdf)
- [AMD-Hardware-Spezifikation](http://www.amd.com/us-en/assets/content_type/DownloadableAssets/22351.pdf)
- [Umfangreiche Spezifikation für die Am79C972 (PCnet-FAST+)](http://www.amd.com/us-en/assets/content_type/white_papers_and_tech_docs/21485_pt1.pdf) - sollte zur Am79C973 (PCnet-FAST III) kompatibel sein

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/5473/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2025/index.html)

<!-- MediaWiki page 2025; revision 5473; parent 5463; 2009-08-07T20:56:40Z -->
