# AMD PCnet

Dieser Artikel beschäftigt sich mit der Programmierung der AMD-PCnet-FAST-III-Netzwerkkarte (Am79C973).

## Einführung

### Vorwort

Wenn ich hier von „Bytes“ spreche, meine ich acht Bit große Einheiten. Zwei Bytes (16 Bit) sind ein Word und vier Bytes (32 Bit) ein DWord. Acht Bytes (64 Bit) sind ein QWord. Wenn ich keine Endianess explizit angebe, dann ist Little Endian gemeint.

### Grundlagen

Wie beim [RTL8139](RTL8139 "RTL8139")-Tutorial gilt auch hier: Euer Betriebssystem sollte bereits einen gewissen Stand aufweisen, um die Karte erkennen und bedienen zu können. Dies sind also [ISRs](Interrupt-Service-Routine "Interrupt Service Routine") für [IRQs](Programmable-Interrupt-Controller#irq-tabelle "IRQ"), eine [Speicherverwaltung](Speicherverwaltung "Speicherverwaltung") und eine Möglichkeit, die [I/O-Ports](I-O-Ports "I/O-Ports") eines bestimmten (anhand von Vendor- und Device-ID) [PCI](Peripheral-Component-Interconnect "Peripheral Component Interconnect")-Gerätes herauszufinden.

Mögliche Emulatoren für PCnet sind sowohl [QEMU](QEMU "QEMU") als auch [VirtualBox](VirtualBox "VirtualBox"). Um die Karte unter QEMU zu benutzen, können zum Beispiel die folgenden Kommandozeilenoptionen angegeben werden:

    qemu -net user -net nic,model=pcnet

Dadurch erstellt QEMU eine virtuelle PCnet-Karte. An der IP-Adresse 10.0.2.2 gibt es einen virtuellen Gateway ins Internet. Um mit VirtualBox die gleiche Konfiguration zu erreichen, muss die PCnet-FAST III (Am79C973) an NAT angeschlossen werden.

Die Netzwerkkarte hat die PCI-Vendor-ID 0x1022 und die Geräte-ID 0x2000.

### Verwendete Resourcen

- I/O-Ports: Es gibt einen I/O-Raum, der dazu dient, einige Register der Netzwerkkarte anzusprechen und die weiteren zu erreichen.
- IRQ: Per IRQ wird der Treiber über eine Statusänderung der Netzwerkkarte informiert (zum Beispiel ist ein Paket eingetroffen oder wurde versendet)

## Zugriff

### Grundlagen

Die „direkt“ erreichbaren Register (ein Portzugriff) sind nur ein kleiner Teil der gesamten Register der Karte. Neben ihnen gibt es noch die CSR (Control and Status Register) und die BCR (Bus Control Register). Um auf sie zuzugreifen, muss zuerst die Adresse des Registers in den 16-Bit-I/O-Port RAP (Register Address Port) geschrieben werden. Betrifft diese Adresse eines der CSR, so kann der Wert anschließend am 16-Bit-I/O-Port RDP (Register Data Port) ausgelesen oder verändert werden. Betrifft die Adresse eines der BCR, so handelt es sich nicht um den RDP, sondern um den BDP (BCR Data Port).

### Initialisierung

1\. IRQ und I/O-Ports vom PCI-Treiber holen und gegebenenfalls registrieren

2\. MAC-Adresse herausfinden; diese steht in drei 16-Bit-Registern ab 0x00 (APROM0, APROM2 und APROM4) in Little-Endian-Reihenfolge (also in APROM0 (0x00) die niederwertigsten 16 Bit und in APROM4 (0x04) die höchstwertigen 16 Bit).

3\. Die Karte zurücksetzen; es muss ein Word vom Resetregister (0x14) eingelesen werden, um einen Software-Reset durchzuführen. Anschließend empfiehlt es sich, zehn Millisekunden zu warten, bis der Reset beendet ist. Danach sollte das BCR20-Register auf 0x0102 gesetzt werden, dies verändert den Softwarestyle zu PCnet-PCI, dadurch werden 32-Bit- und nicht 16-Bit-Strukturen verwendet. Außerdem wird dadurch das SSIZE32-Bit gesetzt, auch dadurch werden 32-Bit-Strukturen aktiviert.

4\. Nun muss ein STOP-Reset ausgeführt werden. Dies wird erreicht, indem 0x04 nach CSR0 geschrieben wird.

5\. Puffer zum Senden und Empfangen initialisieren; beide müssen 2 kB groß und physisch kontinuierlich sein.

6\. Nun muss die Karte initialisiert werden. Dies geschieht mittels eines Initialization Block, der folgendermaßen aussieht:

``` c
struct initialization_block
{
    uint16_t mode;
    unsigned reserved1 : 4;
    unsigned receive_length : 4;
    unsigned reserved2 : 4;
    unsigned transfer_length : 4;
    uint64_t physical_address : 48;
    uint16_t reserved3;
    uint64_t logical_address;
    uint32_t receive_descriptor;
    uint32_t transmit_descriptor;
} __attribute__((packed));
```

„reservedX“-Felder sind reserviert. „mode“ ist 0x8000, wenn die Karte in den Promiscuous-Mode geschaltet werden soll (Alle Pakete empfangen, nicht nur Broadcasts und die für die eigene MAC-Adresse), sonst 0x0000. „receive_length“ gibt die Anzahl der Empfangsdeskriptoren an, dazu später. „transfer_length“ enthält im Gegensatz dazu die Anzahl der Sendedeskriptoren. Beide Werte können auf 3 gesetzt werden, dies entspricht jeweils acht Deskriptoren. „physical_address“ enthält die MAC-Adresse der Karte. „logical_address“ kann auf 0 gesetzt werden. „receive_descriptor“ enthält die physische Adresse zu einem 2-kB-Puffer, „transmit_descriptor“ zu einem anderen. Beide Puffer müssen physisch kontinuierlich sein und an 16-Bytes-Grenzen ausgerichtet.

7\. Jetzt müssen die Empfangs- und Sendedeskriptoren initialisiert werden. So ein Deskriptor sieht so aus:

``` c
struct descriptor
{
    uint32_t address;
    uint32_t flags;
    uint32_t flags2;
    uint32_t avail;
} __attribute__((packed));
```

„address“ gibt die physische Adresse eines 2-kB-Puffers (physisch kontinuierlich) an, „flags“ und „flags2“ enthalten Flags (siehe unten), „avail“ kann vom Benutzer (also von dir) frei verwendet werden. Bei den Empfangsdeskriptoren muss das OWN-Bit (0x80000000) im „flags“-Feld gesetzt werden, zudem müssen die Bits 0 bis 11 des „flags“-Feldes auf 0x7FF gesetzt werden (negative Länge des Puffers, also -2048). Außerdem müssen in beiden Deskriptortypen die Bits 12 bis 15 (0x0000F000) im „flags“-Feld gesetzt werden. Die acht Empfangsdeskriptoren müssen hintereinander in den Puffer geschrieben werden, der in das „receive_descriptor“-Feld des Initialization Blocks eingetragen wurde. Die acht Sendedeskriptoren müssen analog dazu in den Puffer geschrieben werden, der in das „transmit_descriptor“-Feld eingetragen wurde.

8\. Wenn auch die Deskriptoren initialisiert sind, sollte der Initialization Block bei der Karte registriert werden. Hierzu werden die niederwertigen 16 Bits der physischen Adresse in das CSR1-Register und die höherwertigen in das CSR2-Register geschrieben.

9\. Danach muss 0x0041 nach CSR0 geschrieben werden. Das initialisiert die Karte und aktiviert Interrupts. Gleich darauf wird ein IRQ eintreffen. Die ISR sollte einfach den Wert von CSR0 nach CSR0 (sic!) schreiben, um den Interrupt anzunehmen.

10\. Wenn der Interrupt empfangen wurde, sollte der Inhalt von CSR4 mit 0xC00 ge-OR-t und wieder nach CSR4 geschrieben werden. Dadurch werden Pakete, die kleiner als 64 Bytes sind, automatisch auf diese Größe vergrößert und einige relativ überflüssige Informationen von empfangenen Paketen entfernt.

11\. Jetzt ist die Initialisierung endlich abgeschlossen und die Karte darf in Betrieb genommen werden, indem 0x42 nach CSR0 geschrieben wird.

### Konstanten

``` c
//Die Werte, auf die RAP gesetzt werden muss, um dieses Register zu benutzen
#define CSR0   0
#define CSR1   1
#define CSR2   2
#define CSR4   4
#define BCR20 20
//Aliasnamen, damit man auch weiß, was es bedeutet
#define CSR_STATUS                    CSR0
#define CSR_INITIALIZATION_BLOCK_LOW  CSR1
#define CSR_INITIALIZATION_BLOCK_HIGH CSR2
#define CSR_TEST_AND_FEATURES         CSR4
#define BCR_SOFTWARE_STYLE            BCR20

//16-Bit-I/O-Ports (bzw. Offsets zum Beginn des I/O-Raums)
#define APROM0 0x00
#define APROM2 0x02
#define APROM4 0x04
#define RDP    0x10
#define RAP    0x12
#define RESET  0x14
#define BDP    0x16
```

### Die ISR

Wenn ein Interrupt eintrifft, dann zeigt das CSR0-Register den Grund dafür an (Die folgende Tabelle stellt keine vollständige Übersicht über alle möglichen Zustände des CSR0-Registers dar):

| Bit | Name | Erklärung |
| -------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 0x8000 | ERR | Ein Fehler ist aufgetreten. Bit ist gesetzt, wenn CERR-, MISS- oder MERR-Bit in CSR0 gesetzt ist. |
| 0x2000 | CERR | "Collision Error" |
| 0x1000 | MISS | "Missed Frame". Ein eingehendes Paket wurde verloren, weil kein Deskriptor verfügbar war. |
| 0x800 | MERR | "Memory Error" |
| 0x400 | RINT | "Receive Interrupt". Ein Paket wurde abgearbeitet. Siehe dazu „Empfangen von Paketen“. |
| 0x200 | TINT | "Transmit Interrupt". Ein Sendedeskriptor wurde abgearbeitet. Im Fehlerfall wurde das ERROR-Bit im flags-Feld des Deskriptors (0x40000000) gesetzt, andernfalls wurde das Paket gesendet. Die Felder "flags" und "flags2" des Deskriptors sollten dann auf 0 gesetzt werden. |

Am Ende der ISR sollte der Inhalt des CSR0-Registers dorthin zurückgeschrieben werden, um der Karte anzuzeigen, dass der Interrupt abgearbeitet wurde.

### Senden eines Pakets

Um ein Paket zu senden, muss die physische Adresse des entsprechenden Datenpuffers in das „address“-Felds des nächsten Sendedeskriptors geschrieben werden (zuerst Deskriptor 0, dann 1 und so weiter bis Deskriptor 7 (also der achte), danach wieder von vorn beginnen). „flags2“ zeigt ein, ob ein Fehler beim Senden geschehen ist, sollte daher vom Treiber auf 0 gesetzt werden. Im „flags“-Feld muss nun das OWN-Bit gesetzt werden (0x80000000), um der Karte den Deskriptor zu „übergeben“. Desweiteren sollten STP (Start of Packet, 0x02000000) und ENP (End of Packet, 0x01000000) gesetzt werden – dies zeigt an, dass die Daten nicht aufgeteilt werden, sondern dass es sich um ein einzelnes Ethernetpaket handelt. Weiterhin müssen die Bits 12-15 gesetzt werden (0x0000F000, sind wohl reserviert) und die Bits 0-11 geben die **negative** Größe des Pakets an.

Nun könnte man einfach warten, bis die Karte sich das Paket abholt. Alternativ dazu kann man auch das TDMD-Bit (0x08) in CSR0 setzen (Also 0x48 nach CSR0 schreiben, um die Interrupts aktiviert zu lassen), um diese Wartezeit abzukürzen.

Dazu ein Codebeispiel:

``` c
void write_csr(struct pcnet_card *ncard, uint16_t csr, uint16_t val)
{
  outw(ncard->port_base + RAP, csr);
  outw(ncard->port_base + RDP, val);
}

uint16_t read_csr(struct pcnet_card *ncard, uint16_t csr)
{
  outw(ncard->port_base + RAP, csr);
  return inw(ncard->port_base + RDP);
}

void send_packet(struct pcnet_card *ncard, void *buffer, size_t length)
{
  int current_descriptor;

  //Achtung, Beginn eines kritischen Abschnitts!
  if (ncard->current_transmit_descriptor > 7)
    ncard->current_transmit_descriptor = 0;
  current_descriptor = ncard->current_transmit_descriptor++;
  if (current_descriptor == 7) //ncard->current_transmit_descriptor ist also 8
    ncard->current_transmit_descriptor = 0;
  //Ende des Abschnitts

  if (length > 1518) //Maximale Länge eines Ethernetframes
    length = 1518;

  //ncard->linear_transmit_buffer enthält die lineare Adresse des Puffers
  memcpy(ncard->linear_transmit_buffer[current_descriptor], buffer, length);
  //Die physische Adresse (also ncard->physical_transmit_buffer[current_descriptor]) sollte schon bei der
  //Initialisierung in das „address“-Feld geschrieben worden sein
  ncard->linear_transmit_descriptor[current_descriptor].flags2 = 0;
  ncard->linear_transmit_descriptor[current_descriptor].flags = 0x8300F000 | ((-length) & 0xFFF);
  write_csr(ncard, CSR0, 0x48);
}
```

### Empfangen von Paketen

Sobald ein Paket empfangen wurde (das heißt, die ISR wurde aufgerufen und das RINT-Flag im CR0-Register ist gesetzt), müssen alle Empfangsdeskriptoren ab dem aktuellen abgearbeitet werden, bis das OWN-Bit (0x80000000 im „flags“-Feld) bei einem gesetzt ist. Denn alle Deskriptoren mit gelöschtem OWN-Bit wurden gerade von der Karte bearbeitet. Zum Abholen der Daten sollte dann das OWN-Bit gesetzt werden und die Daten können aus dem im Deskriptor angegebenen Puffer kopiert werden. Die Anzahl der Bytes steht in den Bits 0 bis 11 des „flags2“-Feldes.

Die Daten sollten nur dann gelesen werden, wenn das ERROR-Bit (0x40000000) im „flags“-Feld nicht gesetzt ist. Außerdem sollten die Bits STP und ENP (0x02000000 bzw. 0x01000000) – ebenfalls im „flags“-Feld – beide gesetzt sein.

Beispielcode:

``` c
size_t size_of_packet;

while ((ncard->linear_receive_descriptor[ncard->receive_descriptor].flags & 0x80000000) == 0)
{
  if (!(ncard->linear_receive_descriptor[netcard->receive_descriptor].flags & 0x40000000) &&
       (ncard->linear_receive_descriptor[netcard->receive_descriptor].flags & 0x03000000) == 0x03000000)
  {
    size_of_packet = netcard->linear_receive_descriptor[netcard->receive_descriptor].flags2 & 0xFFF;
    //Mach mit den Daten, was du willst!
    //Sie stehen in der virtuellen Version von netcard->linear_receive_descriptor[netcard_receive_descriptor].address
    //und sind [size_of_packet] Bytes lang
  }
  ncard->linear_receive_descriptor[netcard->receive_descriptor].flags = 0x8000F7FF; //OWN-Bit und Standardwerte setzen
  ncard->linear_receive_descriptor[netcard->receive_descriptor++].flags2 = 0;
  if (netcard->last_receive_descriptor == 8)
    netcard->last_receive_descriptor = 0;
}
```

  

## Siehe auch

- [Ethernet](Ethernet "Ethernet")
- [Address Resolution Protocol](Address-Resolution-Protocol "Address Resolution Protocol")
- [Internet Protocol](Internet-Protocol "Internet Protocol")

## Weblinks

- [Datei:Am79C973.pdf](assets/6edd87861edd96ccdcd2.pdf "Datei:Am79C973.pdf") - Umfangreiche Spezifikation für die Am79C973 (PCnet-FAST III) und Am79C975
- [AMD-Hardware-Spezifikation](assets/777e98fb4180ab93b4d0.pdf)
- Umfangreiche Spezifikation für die Am79C972 (PCnet-FAST+): [Teil 1](assets/aa163a95c7c675a38d80.pdf) und [Teil 2](assets/b533b83773bf73697ec4.pdf) – sollte zur Am79C973 (PCnet-FAST III) kompatibel sein

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/11406/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2025/index.html)

<!-- MediaWiki page 2025; revision 11406; parent 11245; 2019-08-03T18:38:27Z -->
