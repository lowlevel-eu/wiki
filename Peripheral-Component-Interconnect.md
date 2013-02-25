# Peripheral Component Interconnect

**Peripheral Component Interconnect** (kurz **PCI**) ist ein [Bus](https://lowlevel-eu.github.io/wiki/pages/1769/index.html "Kategorie:Bus") zur leichten Verbindung von Peripheriegeräten mit der CPU.

Die Informationen in diesem Artikel beziehen sich auch auf die vom klassischen PCI-Bus abgeleiteten Bus-Standards: PCI-Express, Hypertransport, PCI-X und AGP. Diese Busse basieren vom logischen Protokoll her auf PCI aber benutzen andere physikalische Daten-Übertragungsmechanismen bzw. andere Topologien.

## Konfigurations-Adressraum

Jedes PCI-Gerät besitzt einen eigenen Konfigurations-Adressraum, welcher 256 Byte groß ist und verschiedene Konfigurations-Register enthält. Bei PCI-Express, Hypertransport und PCI-X ist der Konfigurations-Adress-Raum 4096 Byte groß. Auf den Konfigurations-Adressraum kann immer Zugegriffen werden, unabhängig vom Zustand des PCI-Geräts (von den Zuständen "defekt", "ausgebaut" oder "abgeschaltet" mal abgesehen). Für den Zugriff auf den Konfigurations-Adressraum werden die PCI-Geräte über ihre Bus-Nummer, Device-Nummer und Function-Nummer angesprochen, dazu müssen eventuelle PCI-to-PCI-Bridges korrekt konfiguriert sein.

### Aufbau des Konfigurations-Adressraum

Im Konfigurations-Adressraum sind die ersten 64 Byte fest für den Basis-Header reserviert. Die restlichen Bytes stehen zur freien Nutzung durch das Gerät zur Verfügung, in diesem Bereich sind auch die Capabilities untergebracht.

Im Basis-Header sind die Bytes 0x000 &#150; 0x00F, 0x034, 0x03C und 0x03D für alle PCI-Geräte identisch definiert. Diese Bytes dienen dazu, das PCI-Gerät zu klassifizieren und identifizieren.

| Register | 31-24 | 23-16 | 15-8 | 7-0 |
| ---------- | ---------------------- | ------------- | --------------- | ---------------------- |
| 0x000 | Device ID |  | Vendor ID |  |
| 0x004 | Status |  | Command |  |
| 0x008 | Classcode |  |  | Revision ID |
| 0x00C | BIST | Header Type | Latency Timer | Cache Line Size |
| 0x010 | Header Type Specific |  |  |  |
| 0x014 | Header Type Specific |  |  |  |
| 0x018 | Header Type Specific |  |  |  |
| 0x01C | Header Type Specific |  |  |  |
| 0x020 | Header Type Specific |  |  |  |
| 0x024 | Header Type Specific |  |  |  |
| 0x028 | Header Type Specific |  |  |  |
| 0x02C | Header Type Specific |  |  |  |
| 0x030 | Header Type Specific |  |  |  |
| 0x034 | Header Type Specific |  |  | Capabilities Pointer |
| 0x038 | Header Type Specific |  |  |  |
| 0x03C | Header Type Specific |  | Interrupt Pin | Interrupt Line |

- Die *Vendor ID*s werden von PCI-SIG verwaltet und den Herstellern zugewiesen. Der Wert 0xffff ist für den Fall reserviert, dass an dieser Stelle kein Gerät vorhanden ist.
- Die *Device ID*s verwalten die Hardwarehersteller selbst. Sie dient zusammen mit der *Vendor ID* der eindeutigen Identifikation des Gerätes.
- Im *Status*-Register werden verschiedene Basis-Status und Gerät-Fähigkeiten angezeigt.
- Im *Command*-Register werden verschiedene Basis-Konfigurationen vorgenommen.
- *Classcode* ist noch einmal geteilt. Die oberen 8 Bit (Byte 0x00B) repräsentieren die *Base Class*, die mittleren 8 Bit (Byte 0x00A) stehen für die *Subclass* und die unteren 8 Bit (Byte 0x009) für das *Programming Interface*.
- Die *Revision ID* wird vom Hardwarehersteller selbst verwaltet.
- Mit dem *BIST*-Register kann ein gerätespezifischer Selbsttest ausgelöst und ausgewertet werden. Diese Funktion ist optional und wird nur von wenigen PCI-Geräten unterstützt.
- *Header Type* spezifiziert den Inhalt der Register 0x010 &#150; 0x03F. Dabei gibt Bit 7 an, ob es sich um ein Multifunction-Device handelt oder nicht, in dem Fall muss das Bit 7 in allen vorhandenen Funktionen gesetzt sein.

| Header Type | Kurze Beschreibung |
| ------------- | ------------------------------------- |
| 0x00 | [Standard](#header-type-0x00) |
| 0x01 | [PCI/PCI-Bridge](#header-type-0x01) |
| 0x02 | CardBus-Bridge |

- Der *Capabilities Pointer* zeigt, falls er gültig ist, auf die erste Capability-Struktur, welche der Start einer verketteten Liste ist. Für gültige Capabilities Pointer sind nur Werte von 0x40 bis 0xF0 erlaubt.
- Im *Interrupt Pin*-Register wird angegeben, welches Interrupt-Pin das Gerät verwendet. 0x00 steht für kein Interrupt-Signal, trotzdem kann noch [MSI](https://github.com/lowlevel-eu/wiki/wiki/Message-Signaled-Interrupt "MSI")(-X) benutzt werden. Die Werte 0x01 bis 0x04 stehen für \#INTA bis \#INTD, alle anderen Werte sind nicht erlaubt. Bei Singlefunction-Devices ist nur Pin \#INTA erlaubt. Bei Multifunction-Devices dürfen auch \#INTB bis \#INTD benutzt werden, es dürfen auch mehrere Funktionen in einem PCI-Gerät sich eine Interrupt-Leitung teilen.
- Im *Interrupt Line*-Register legt das BIOS die zugewiesene x86-Interrupt-Nummer ab, welche das \#INT?-Signal des betreffendem PCI-Geräts auslöst. Diese Info ist nur relevant wenn man die IRQs über den klassischen PIC vermitteln lässt, wenn die APICs benutzt werden ist diese Info unter Umständen nur noch von begrenztem Nutzen. Diese Info ist eine reine Freundlichkeit des BIOS der x86-Plattform, auf allen anderen Plattformen bleibt dieses Register leer. Dem PCI-Gerät ist der Wert in diesem Register egal und wird es auch nicht verändern. Falls das PCI-Gerät keine Interrupts benutzt, oder nur per MSI(-X) signalisiert, kann dieses Register auch fest auf 0x00 geklemmt sein.

#### Header Type 0x00

| Register | 31-24 | 23-16 | 15-8 | 7-0 |
| ---------- | ---------------------------- | ----------- | --------------------- | ---------------------- |
| 0x010 | Base Address \#0 (BAR0) |  |  |  |
| 0x014 | Base Address \#1 (BAR1) |  |  |  |
| 0x018 | Base Address \#2 (BAR2) |  |  |  |
| 0x01C | Base Address \#3 (BAR3) |  |  |  |
| 0x020 | Base Address \#4 (BAR4) |  |  |  |
| 0x024 | Base Address \#5 (BAR5) |  |  |  |
| 0x028 | Cardbus CIS Pointer |  |  |  |
| 0x02C | Subsystem ID |  | Subsystem Vendor ID |  |
| 0x030 | Expansion ROM base address |  |  |  |
| 0x034 | Reserviert |  |  | Capabilities Pointer |
| 0x038 | Reserviert |  |  |  |
| 0x03C | Max Latency | Min Grant | Interrupt Pin | Interrupt Line |

#### Header Type 0x01

| Register | 31-24 | 23-16 | 15-8 | 7-0 |
| ---------- | ---------------------------------- | ------------------- | -------------------------- | ---------------------- |
| 0x010 | Base Address \#0 (BAR0) |  |  |  |
| 0x014 | Base Address \#1 (BAR1) |  |  |  |
| 0x018 | Secondary latency timer | Subordinate bus № | Secondary bus № | Primary bus № |
| 0x01C | Secondary Status |  | I/O Limit | I/O base |
| 0x020 | Memory limit |  | Memory base |  |
| 0x024 | Prefetchable memory limit |  | Prefetchable memory base |  |
| 0x028 | Prefetchable base upper 32 bits |  |  |  |
| 0x02C | Prefetchable limit upper 32 bits |  |  |  |
| 0x030 | I/O limit upper 16 bits |  | I/O base upper 16 bits |  |
| 0x034 | Reserviert |  |  | Capabilities pointer |
| 0x038 | Extension ROM base address |  |  |  |
| 0x03C | Bridge control |  | Interrupt pin | Interrupt line |

### Bedeutung einiger Register

#### Status-Register

| Bit | Name | Typ | Bedeutung |
| ------ | ---------------------------------------- | ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 3 | Interrupt Status | RO / dynamic | Wenn dieses Bit auf 1 gesetzt ist möchte das betreffende PCI-Gerät einen Interrupt über sein \#INT?-Signal melden. Nur wenn das Bit 10 im Command-Register gelöscht ist wird auch tatsächlich ein Interrupt (an den PIC o.ä.) signalisiert. Falls das PCI-Gerät keine Interrupts benutzt oder diese ausschließlich per [MSI](https://github.com/lowlevel-eu/wiki/wiki/Message-Signaled-Interrupt "MSI")(-X) signalisiert kann dieses Bit fest auf 0 geklemmt sein. Auf Bridges meldet dieses Bit nur eigene Interrupts, durch geleitete Interrupts, von sekundären Bussen zum übergeordnetem Bus, beeinflussen dieses Bit nicht. |
| 4 | Capabilities List | RO / fix | Wenn dieses Bit auf 1 gesetzt ist ist der Capabilities-Pointer (Offset 0x034) gültig.<br>Bei PCI-Express, Hypertransport und PCI-X (und wahrscheinlich auch AGP) muss dieses Bit immer gesetzt sein da dort bus-spezifische Capabilities Pflicht sind. |
| 5 | 66 MHz Capable | RO / fix | Dieses Bit gibt an ob eine PCI-Karte nicht nur mit maximal 33 MHz-Bus-Takt arbeiten kann sondern bis zu 66 MHz verträgt. Nur wenn alle PCI-Geräte auf dem betreffenden physischen PCI-Bus-Segment mit mehr als 33 MHz umgehen können darf dieses Bus-Segment auch mit mehr als 33 MHz, bis maximal 66 MHz, betrieben werden.<br>Dieses Bit ist nur beim klassischen PCI gültig und bei allen PCI-Nachfolgern immer fest auf 0 geklemmt, außer bei AGP dort ist es immer fest auf 1 geklemmt. Für die Software hat dieses Bit keine Bedeutung, auf dem PCI-Bus wird die Geschwindigkeit in Hardware ausgehandelt, wenn die Software auf den Konfigurations-Adressraum der angeschlossenen Geräte zugreifen kann ist der Bus bereits funktionsfähig. |
| 7 | Fast Back-to-Back Transactions Capable | RO / fix | Wenn diese Bit gesetzt ist bedeutet dasss dass das betreffende PCI-Gerät die minimal schnelleren Back-to-Back Transfers unterstützt. Als Target werden diese Transfers immer unterstützt, aber als Master dürfen diese Transfers nur benutzt werden falls das Bit 9 im Command-Register gesetzt ist. |
| 8 | Master Data Parity Error | RW1C / dynamic | *TODO* |
| 10-9 | DEVSEL Timing | RO / fix | Diese 2 Bits, als unsigned Integer betrachtet, geben an nach wie vielen PCI-Bus-Takten das PCI-Gerät erkannt hat ob es das Target eines Zugriffs ist. Gültige Werte sind 0, 1 und 2. Der Wert 3 darf nicht verwendet werden, jedes PCI-Gerät muss nach spätestens 2 Takten dekodiert haben ob es das gewünschte Target ist oder nicht. Im 3ten Takt wird dann eine eventuell vorhandene Subtractive-Bridge aktiv und nimmt den Transfer entgegen oder der Zugriff geht ins Leere und der Initiator meldet das als Fehler. |
| 11 | Signalled Target-Abort | RW1C / dynamic | *TODO* |
| 12 | Received Target-Abort | RW1C / dynamic | *TODO* |
| 13 | Received Master-Abort | RW1C / dynamic | *TODO* |
| 14 | Signalled System Error | RW1C / dynamic | *TODO* |
| 15 | Detected Parity Error | RW1C / dynamic | *TODO* |

Nicht beschriebene Bits sind reserviert und liefern beim lesen eine 0. Die Bits im Status-Register sind entweder Read-Only (RO) oder lassen sich durch beschreiben mit einer 1 rücksetzen (RW1C), das beschreiben mit einer 0 hat keinen Effekt. Einige Bits ändern ihren Zustand nie (fix) und andere können ihren Zustand durch bestimmte Ereignisse ändern (dynamic).

#### Command-Register

| Bit | Name | Bedeutung |
| ----- | ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 0 | IO Space | Nur wenn dieses Bit gesetzt ist, kann der I/O-Raum des Geräts verwendet werden, sonst ist er deaktiviert.<br>Falls das Gerät keine IO-Ports anbietet, ist dieses Bit fest auf 0 geklemmt. |
| 1 | Memory Space | Nur wenn dieses Bit gesetzt ist, können MMIO-Register verwendet werden, sonst sind diese deaktiviert.<br>Falls das Gerät kein MMIO (oder andere Speicherbereiche) anbietet, ist dieses Bit fest auf 0 geklemmt. |
| 2 | Bus Master | Ist dieses Bit gesetzt, so darf das Gerät als Busmaster auf dem PCI-Bus arbeiten. Das ist z. B. für PCI-DMA notwendig (wird u. a. von Netzwerkkarten und (S)ATA-Host-Controllern verwendet).<br>Falls das Gerät nicht busmasterfähig ist, ist dieses Bit fest auf 0 geklemmt.<br>Wenn dieses Bit auf 0 steht, wird damit auch [MSI](https://github.com/lowlevel-eu/wiki/wiki/Message-Signaled-Interrupt "MSI")(-X) unterbunden. |
| 3 | Special Cycles | Wenn dieses Bit gelöscht ist, dann muss das Gerät alle Special Cycles auf dem PCI-Bus ignorieren. Special Cycles werden zum Broadcasten von speziellen Nachrichten an alle PCI-Geräte benutzt.<br>Es gibt nur wenige PCI-Geräte, bei denen dieses Bit überhaupt beschreibbar ist, bei den meisten ist es fest auf 0 geklemmt. Bei PCI-Express ist es immer fest auf 0 geklemmt. |
| 4 | Memory Write and Invalidate Enable | Falls gesetzt, kann das Gerät diesen Befehl (Memory Write and Invalidate) ausführen, sonst muss es sich mit einem einfachen Memory Write begnügen.<br>Bei PCI-Express ist dieses Bit immer fest auf 0 geklemmt. |
| 5 | VGA Palette Snoop | Dieses Bit ist nur für VGA-kompatible Geräte interessant (ist es gesetzt, so werden Zugriffe auf die VGA-Palettenregister gesondert behandelt), auf allen anderen Geräten ist es immer fest auf 0 geklemmt.<br>Bei PCI-Express und Hypertransport ist dieses Bit immer fest auf 0 geklemmt, dort wird sowas in den Bridges konfiguriert. |
| 6 | Parity Error Response | Ist dieses Bit gesetzt, so wird bei Parityfehlern auf dem PCI-Bus das Detected-Parity-Error-Statusbit im Statusregister gesetzt. Nicht jede PCI-Hardware unterstützt die Generierung und Prüfung des Paritybits auf dem PCI-Bus, sodass dieses Bit dann fest auf 0 geklemmt ist. Daher sollte dieses Bit nur dann auf 1 gesetzt werden, wenn alle PCI-Geräte auf dem betreffenden physischen PCI-Bus-Segment die Parity-Bit-Generierung unterstützen.<br>Bei PCI-Express und Hypertransport gibt es leistungsfähigere Fehlererkennungsmechanismen, deren Benutzung zu bevorzugen ist. |
| 7 | IDSEL Stepping /<br>Wait Cycle Control | Dieses Bit war nur in den ersten PCI-Spezifikationen gültig (vor 2.0) und muss immer auf 0 gesetzt werden. Auf allen PCI-Geräten seit der PCI-Spezifikation 2.0 (ab 1993) ist dieses Bit immer fest auf 0 geklemmt. |
| 8 | SERR# Enable | Wenn dieses Bit gesetzt ist darf/soll das Gerät erkannte schwerwiegende Fehler (z. B. Parityfehler während der Adressierungsphase oder ungültige Kommandos) über die extra \#SERR-Leitung, oder bei PCI-Express über spezielle Messages, melden. Solche Fehler lösen für gewöhnlich einen NMI oder eine Machine-Check-Exception aus.<br>Bei PCI-Express und Hypertransport gibt es leistungsfähigere Fehlererkennungsmechanismen, deren Benutzung zu bevorzugen ist. |
| 9 | Fast Back-to-Back Enable | Wenn dieses Bit auf 1 gesetzt ist soll das PCI-Gerät Back-to-Back-Zugriffe (als Target) unterstützen und darf auch solche Zugriffe (als Master) ausführen. Dieses Bit lässt sich nur auf 1 setzen, wenn das zugehörige Bit 7 im Status-Register diese Fähigkeit signalisiert, andernfalls ist es fest auf 0 geklemmt. Dieses Bit darf nur dann auf 1 gesetzt werden wenn alle PCI-Geräte auf dem betreffenden physischen PCI-Bus-Segment Back-to-Back-Zugriffe unterstützen. Wenn alle Geräte diesen Modus unterstützen, kann die Idle-Phase zwischen zwei PCI-Zyklen entfallen. Das erhöht etwas den Datendurchsatz auf dem PCI-Bus.<br>Bei PCI-Express, Hypertransport und PCI-X ist dieses Bit immer fest auf 0 geklemmt. |
| 10 | Interrupt Disable | Ist dieses Flag gesetzt, dann kann das entsprechende Gerät keine IRQs auslösen. Nach dem Hardware-Reset muss dieses Bit dummerweise immer gelöscht sein, sodass IRQs anfangs nicht verboten sind. MSI(-X) ist davon unabhängig, dafür gibt es spezielle Interrupt-Enable-Bits in den entsprechenden Capabilities. |

Bit 7 ist auf 0 zu setzen, Bits 11 bis 15 sind reserviert (und undefiniert) und müssen ebenfalls immer auf 0 gesetzt werden. Nach dem Reset des Geräts sind alle hier aufgeführten Bits auf 0 gesetzt (wobei das BIOS wohl einige davon setzen wird). Die Software sollte immer prüfen, ob sich die gewünschten Bits auch wirklich auf 1 setzen lassen, einige Bits sind eben fest auf 0 geklemmt. Es sind zwar nicht alle Bits beschreibbar aber kein Bit im Command-Register wird seinen Zustand von alleine ändern.

#### Base-Address-Register

Die Base-Address-Register dienen dem Zuweisen von Adressen an die Ressourcen des PCI-Gerätes. Ein PCI-Gerät kann bis zu 6, bei Bridges nur maximal 2, Ressourcen anbieten, denen das BIOS oder OS eine Adresse zuweist, über welche diese Ressourcen dann ansprechbar sind. Als Ressourcen können Speicherbereiche aber auch IO-Bereiche angeboten werden, der IO-Adress-Raum wird aber nicht auf jeder Plattform unterstützt, eigentlich nur beim PC. Die IO-Ressourcen haben verschiedene Nachteile, u.a. sind sie langsamer da es keine Burst-Zugriffe gibt und es gibt Einschränkungen bei der Adressenraumgröße. Speicher-Ressourcen können neben den einfachen 32-Bit-Adressen auch 64-Bit-Adressen nutzen, wofür dann aber 2 hintereinander liegende BARs für eine Ressource benutzt werden müssen, das folgende BAR enthält dann die oberen 32 Bit der Basis-Adresse.

In den unteren 2 Bit (IO-Ressourcen) oder 4 Bit (Speicher-Ressourcen) eines BAR ist codiert was für eine Ressource dieses BAR anbietet, diese Bits sind immer fest und können nicht verändert werden. Die restlichen Bits können für die Basis-Adresse benutzt werden wobei für die Basis-Adresse als ganzes die unteren 2 oder 4 Bits als 0 angenommen werden. Daraus ergibt sich das IO-Ressourcen immer mindestens 4 Bytes und Speicher-Ressourcen immer mindesten 16 Bytes groß sein müssen. Um größere Ressourcen anzubieten, können oberhalb der fest definierten unteren Bits noch weitere Bits fest auf 0 geklemmt sein. Um z. B. eine 256 Byte große Speicher-Ressource anzubieten müssen dann auch die Bits 4 bis 7 fest auf 0 geklemmt sein. Wenn dann das BIOS oder OS das BAR mit lauter 1en beschreibt und anschließend zurück ließt, was den Wert 0xFFFFFF00 ergibt, kann es ermitteln welche Bits zur Konfiguration der Basis-Adresse zur Verfügung stehen. Wenn z. B. der Wert 0xFFFF0000 von einem BAR für eine 32-Bit-Speicher-Ressource gelesen wird bedeutet dass das die Bits 16 bis 31 für die Basis-Adresse zu Verfügung stehen und diese Speicher-Ressource 64 kBytes groß ist. Daraus das die Bits 0 bis 15 der Basis-Adresse 0 sind ergibt sich das diese Speicher-Ressource auch an einer 64-kByte-Grenze ausgerichtet sein muss. Da immer mindestens 1 Bit für die Basis-Adresse beschreibbar sein muss, können mit einer 32-Bit-Adresse maximal 2 GByte große Ressourcen angeboten werden. Die angebotenen Ressourcen müssen immer eine Zweierpotenz als Größe haben und sind dann auch entsprechend ausgerichtet.

Nur alleine durch lesen der BAR-Register kann man nicht auf die Größe der betreffenden Ressourcen schließen. Zum kompletten analysieren der BARs müssen diese auch immer beschrieben werden. Darüber hinaus haben es die PCI-Erfinder auch versäumt wenigstens dafür zu sorgen das man nur durch lesen den genauen Type des BARs erkennen kann. Falls die unteren 4 Bit alle 0 sind ist es entweder ein unbenutzter BAR oder eine non-prefetchable 32-Bit-Speicher-Ressource, genau kann man das erst ermitteln indem man prüft ob die restlichen Bits beschreibbar sind.

##### Base-Address-Register für Speicher-Ressourcen mit 32-Bit-Adresse

| 31-4 | 3 | 2-1 | 0 |
| -------------- | ----- | ----- | ----- |
| Base Address | P | Typ | 0 |

Das Bit 0 signalisiert mit seinem Wert 0 das es sich bei dem betreffenden BAR um eine Speicher-Ressource handelt und die Werte 00 und 01 in den Bits 2-1 signalisieren das es sich um einen 32-Bit-BAR handelt. Die Bits 31-4 geben die Basis-Adressbits 31-4 der Speicher-Ressource an.

##### Base-Address-Register für Speicher-Ressourcen mit 64-Bit-Adresse

| 63-4 | 3 | 2-1 | 0 |
| -------------- | ----- | ----- | ----- |
| Base Address | P | Typ | 0 |

Das Bit 0 signalisiert mit seinem Wert 0 das es sich bei dem betreffenden BAR um eine Speicher-Ressource handelt und der Wert 10 in den Bits 2-1 signalisiert das es sich um einen 64-Bit-BAR handelt. Die Bits 63-4 geben die Basis-Adressbits 63-4 der Speicher-Ressource an. Das Prefetchable-Bit muss bei 64-Bit-Speicher-Ressourcen eigentlich immer fest auf 1 geklemmt sein, die PCI-Spezifikation verlangt das zwar nicht explizit aber bei Non-Prefetchable-Speicher macht eine 64-Bit-Adresse keinen Sinn da PCI-to-PCI-Bridges Zugriffe auf Non-Prefetchable-Speicher nur mit einer 32-Bit-Adresse weiterleiten können (siehe Bytes 0x020 bis 0x023 im Type 0x01 Konfigurations-Adressraum).

##### Base-Address-Register für IO-Ressourcen

| 31-2 | 1 | 0 |
| -------------- | ----- | ----- |
| Base Address | R | 1 |

Das Bit 0 signalisiert mit seinem Wert 1 das es sich bei dem betreffenden BAR um eine IO-Ressource handelt. Das Bit 1 ist reserviert und muss beim lesen ignoriert und beim schreiben mit 0 gelöscht werden. Die Bits 31-2 geben die Basis-Adressbits 31-2 der IO-Ressource an. Die IO-Ressource muss also mindestens 4 Byte groß sein. Oft sind die Bits 31-16 fest auf 0 geklemmt so das nur 16-Bit-IO-Adressen benutzt werden können, auf der PC-Plattform unterstützen die CPUs sowieso nur 16-Bit-IO-Adressen so das normalerweise daraus kein Problem entsteht.

##### Beispiel-Code zur BAR-Analyse

Der folgende C-Code analysiert alle BARs im Konfigurations-Adressraum eines PCI-Gerätes und gibt alle verfügbaren Informationen aus. Dieser Code sollte möglichst nicht auf aktivierte PCI-Geräte angewendet werden, falls doch wäre es geschickt den Vorgang atomar zu gestalten und alle BARs vorher zu sichern und hinter zu restaurieren. Außerdem sollten die Bits 0 und 1 des Command-Registers gelöscht sein. \<c\>/\*\*\* Diesen Code darf jeder, unter Berücksichtigung der Lizenz für diesen Wiki-Artikel, zu jedem Zweck kopieren, nutzen und verändern!

        (C) <http://www.lowlevel.eu/> ***/

  
/\* deklariert einen Typ der Bus, Device und Function enthält um ein bestimmtes PCI-Gerät zu adressieren,

      außerdem bin ich einfach zu faul 3 Einzelwerte durch meinen Quäl-Code zu schicken */

typedef .... pci_bdf_t;

/\* ließt einen 32Bit-Wert aus dem Config-Space vom PCI-Gerät (addr) an Offset (offset) und gibt ihn zurück \*/ extern uint32_t pci_config_readd(pci_bdf_t addr,uint offset);

/\* schreibt einen 32Bit-Wert (value) in den Config-Space vom PCI-Gerät (addr) an Offset (offset) \*/ extern void pci_config_writed(pci_bdf_t addr,uint offset,uint32_t value);

  
/\* sucht das unterste gesetzte Bit in einem 32Bit-Wert , value darf nicht 0 sein \*/ static uint get_number_of_lowest_set_bit(uint32_t value); static uint get_number_of_lowest_set_bit(uint32_t value) {

     uint pos = 0;
     uint32_t mask = 0x00000001;
     while (!(value & mask))
      { ++pos; mask=mask<<1; }
     return pos;

}

/\* sucht das oberste gesetzte Bit in einem 32Bit-Wert , value darf nicht 0 sein \*/ static uint get_number_of_highest_set_bit(uint32_t value); static uint get_number_of_highest_set_bit(uint32_t value) {

     uint pos = 31;
     uint32_t mask = 0x80000000;
     while (!(value & mask))
      { --pos; mask=mask>>1; }
     return pos;

}

  
/\* analysiert die BARs eines bestimmten PCI-Gerätes, das PCI-Gerät sollte hierfür unbenutzt sein \*/ void pci_config_bar_analyze(const pci_bdf_t addr) {

     // Header-Type auslesen um zu ermitteln wie viele BARs vorhanden sind :
     const uint32_t headerType = ( pci_config_readd(addr,0x00C) >> 16 ) & 0x7F;
     // es werden nur Type 0x00 (normale Devices) und 0x01 (PCI-to-PCI-Bridges) unterstützt :
     if (headerType >= 0x02)
      { printf("FEHLER : nicht unterstützter Header-Type gefunden!\n"); return; }

     // 6 BARs für Type 0x00 und 2 BARs für Type 0x01 :
     const uint max_bars = 6 - (headerType * 4);

     for (uint bar = 0 ; bar < max_bars ; ++bar)
      {
        // Offset des aktuellen BAR ermitteln :
        const uint barOffset = 0x010+(bar*4);

        // prüfen ob Speicher oder IO :
        if ( (pci_config_readd(addr,barOffset) & 0x1) == 0 )
         { // Speicher-Ressource :

           // Prefetchable-Bit auslesen und passenden Text auswählen :
           static const char* ptext_pref = "prefetchable"; // Text für prefetchable
           static const char* ptext_nopr = "non-prefetchable"; // Text für non-prefetchable
           const char* const ptext = (((pci_config_readd(addr,barOffset) >> 3) & 0x1) == 1) ? ptext_pref : ptext_nopr;

           // check Memory-BAR-Type :
           switch((pci_config_readd(addr,barOffset) >> 1) & 0x3)
            {
              case 0x0: // 32Bit Memory-BAR :
                {
                pci_config_writed(addr,barOffset,0xFFFFFFF0); // mit lauter 1en überschreiben
                const uint32_t barValue = pci_config_readd(addr,barOffset) & 0xFFFFFFF0; // und wieder zurücklesen
                if (barValue == 0) // es muss mindestens ein Adressbit 1 (also beschreibbar) sein
                 {
                   if (ptext != ptext_nopr) // unbenutzte BARs müssen komplett 0 sein (auch das Prefetchable-Bit darf nicht gesetzt sein)
                    { printf("FEHLER : 32Bit-Memory-BAR %u enthält keine beschreibbaren Adressbits!\n",bar); return; }

                   // BAR-Infos ausgeben :
                   printf("BAR %u ist unbenutzt.\n",bar);
                 }
                else
                 {
                   const uint lowestBit = get_number_of_lowest_set_bit(barValue);
                   // es muss eine gültige 32Bit-Adresse sein :
                   if ( (get_number_of_highest_set_bit(barValue) != 31) || (lowestBit > 31) || (lowestBit < 4) )
                    { printf("FEHLER : 32Bit-Memory-BAR %u enthält ungültige beschreibbare Adressbits!\n",bar); return; }

                   // BAR-Infos ausgeben :
                   printf("BAR %u enhält eine %s 32Bit-Memory-Ressource mit einer Größe von 2^%u Bytes.\n",bar,ptext,lowestBit);
                 }
                }
                break;

              case 0x1: // 20Bit Memory-BAR :
                {
                if (headerType == 0x01)
                 { printf("FEHLER : 20Bit-Memory-BAR %u ist für eine Bridge nicht erlaubt!\n",bar); return; }

                pci_config_writed(addr,barOffset,0xFFFFFFF0); // mit lauter 1en überschreiben
                const uint32_t barValue = pci_config_readd(addr,barOffset) & 0xFFFFFFF0; // und wieder zurücklesen
                if (barValue == 0) // es muss mindestens ein Adressbit 1 (also beschreibbar) sein
                 { printf("FEHLER : 20Bit-Memory-BAR %u enthält keine beschreibbaren Adressbits!\n",bar); return; }

                const uint lowestBit = get_number_of_lowest_set_bit(barValue);
                // es muss eine gültige 20Bit-Adresse sein :
                if ( (get_number_of_highest_set_bit(barValue) != 19) || (lowestBit > 19) || (lowestBit < 4) )
                 { printf("FEHLER : 20Bit-Memory-BAR %u enthält ungültige beschreibbare Adressbits!\n",bar); return; }

                // BAR-Infos ausgeben :
                printf("BAR %u enhält eine %s 20Bit-Memory-Ressource mit einer Größe von 2^%u Bytes.\n",bar,ptext,lowestBit);
                }
                break;

              case 0x2: // 64Bit Memory-BAR :
                {
                // prüfen ob ein 64Bit-BAR an der aktuellen Position überhaupt möglich ist :
                if (bar >= (max_bars-1))
                 { printf("FEHLER : 64Bit-Memory-BAR %u darf nicht an letzter Position beginnen!\n",bar); return; }
                // non-prefetchable 64-BARs können nicht hinter Bridges benutzt werden (? aber in der Spec sind sie nicht verboten ?) :
                if (ptext != &ptext_pref[0])
                 { printf("FEHLER : 64Bit-Memory-BAR %u enthält eine non-prefetchable Memory-Ressource!\n",bar); return; }

                pci_config_writed(addr,barOffset,0xFFFFFFF0); // mit lauter 1en überschreiben
                pci_config_writed(addr,barOffset+4,0xFFFFFFFF); // mit lauter 1en überschreiben
                const uint32_t barLowValue  = pci_config_readd(addr,barOffset) & 0xFFFFFFF0; // und wieder zurücklesen
                const uint32_t barHighValue = pci_config_readd(addr,barOffset+4); // und wieder zurücklesen

                uint lowestBit = 0;
                if (barLowValue != 0)
                 { // kleiner als 4 GByte :
                   lowestBit = get_number_of_lowest_set_bit(barLowValue);
                   // es muss eine gültige kleine 64Bit-Adresse sein :
                   if ( (barHighValue != 0xFFFFFFFF) || (get_number_of_highest_set_bit(barLowValue) != 31) || (lowestBit > 31) || (lowestBit < 4) )
                    { printf("FEHLER : 64Bit-Memory-BAR %u enthält ungültige beschreibbare Adressbits im unteren Adressteil!\n",bar); return; }
                 }
                else
                 { // größer/gleich als 4 GByte :
                   lowestBit = get_number_of_lowest_set_bit(barHighValue) + 32;
                   // es muss eine gültige große 64Bit-Adresse sein :
                   if ( (get_number_of_highest_set_bit(barHighValue) != 31) || (lowestBit > 63) || (lowestBit < 32) )
                    { printf("FEHLER : 64Bit-Memory-BAR %u enthält ungültige beschreibbare Adressbits im oberen Adressteil!\n",bar); return; }
                 }

                // BAR-Infos ausgeben :
                printf("BAR %u enhält eine %s 64Bit-Memory-Ressource mit einer Größe von 2^%u Bytes.\n",bar,ptext,lowestBit);

                // den nachfolgenden BAR für die Analyse überspringen :
                ++bar;

                // BAR-Infos ausgeben :
                printf("BAR %u ist nicht nutzbar da er die oberen 32 Bits des vorrangegangenen 64Bit-BARs enthält\n",bar);
                }
                break;

              default: // ungültiger Memory-BAR :
                printf("FEHLER : Memory-BAR %u ist ungültig!\n",bar); return;
            }
         }
        else
         { // IO-Ressource :
           pci_config_writed(addr,barOffset,0xFFFFFFFC); // mit lauter 1en überschreiben
           const uint32_t barValue = pci_config_readd(addr,barOffset) & 0xFFFFFFFC; // und wieder zurücklesen
           if (barValue == 0) // es muss mindestens ein Adressbit 1 (also beschreibbar) sein
            { printf("FEHLER : IO-BAR %u enthält keine beschreibbaren Adressbits!\n",bar); return; }

           const uint lowestBit  = get_number_of_lowest_set_bit(barValue);
           const uint highestBit = get_number_of_highest_set_bit(barValue);
           // es muss entwerder eine gültige 32Bit-Adresse oder eine gültige 16Bit-Adresse sein :
           if ( ( (highestBit != 31) && (highestBit != 15) ) || (highestBit < lowestBit) || (lowestBit < 2) )
            { printf("FEHLER : IO-BAR %u enthält ungültige beschreibbare Adressbits!\n",bar); return; }

           // BAR-Infos ausgeben :
           printf("BAR %u enhält eine %uBit-IO-Ressource mit einer Größe von 2^%u Bytes.\n",bar,highestBit+1,lowestBit);
         }
      }
     if (bar != max_bars)
      { printf("interner Fehler in Schleife!\n"); return; }

}\</c\>

### Zugriff auf den Konfigurations-Adressraum

Gelesen und beschrieben wird der Konfigurations-Adressraum, bei PCs, 32bit-weise mithilfe eines Adress-I/O-Ports (0x0CF8) und eines Daten-I/O-Ports (0x0CFC).

#### Aufbau des Adress-I/O-Ports

| 31 | 30-24 | 23-16 | 15-11 | 10-8 | 7-0 |
| ------------ | ------------ | ----------- | -------------- | ----------------- | ----------------------------------------- |
| Enable Bit | Reserviert | Busnummer | Gerätenummer | Funktionsnummer | Registernummer<br>Bit 0 u. Bit 1 sind 0 |

#### Codebeispiel

\<c\>

1.  define PCI_CONFIG_DATA 0x0CFC
2.  define PCI_CONFIG_ADDRESS 0x0CF8

/\*\*

    * Liest ein Dword aus einem PCI-Konfigurations-Register
    *  @param bus Bus
    *  @param dev Gerät
    *  @param func Funktion
    *  @param offset Registernummer
    *  @return Register content
    */

int pci_config_readd(int bus,int dev,int func,int offset) {

     int val;
     int address = 0x80000000|(bus<<16)|(dev<<11)|(func<<8)|(offset&0xFC);
     outl(PCI_CONFIG_ADDRESS,address);
     val = inl(PCI_CONFIG_DATA);
     return val;

}

/\*\*

    * Schreibt ein Dword in ein PCI-Konfigurations-Register
    *  @param bus Bus
    *  @param dev Gerät
    *  @param func Funktion
    *  @param offset Registernummer
    *  @param val Wert zum Schreiben
    */

void pci_config_writed(int bus,int dev,int func,int offset,int val) {

     int address = 0x80000000|(bus<<16)|(dev<<11)|(func<<8)|(offset&0xFC);
     outl(PCI_CONFIG_ADDRESS,address);
     outl(PCI_CONFIG_DATA,val);

} \</c\>

## Classcodes

| Baseclass | Beschreibung |
| ----------- | ------------------------------------------------------------------------------------------------------------------ |
| 0x00 | [Alle Geräte die gebaut wurden bevor Classcodes eingeführt wurden](#class-0x00---pre-20) |
| 0x01 | [Massenspeicher](#class-0x01---massenspeicher) |
| 0x02 | [Netzwerk-Controller](#class-0x02---netzwerk-controller) |
| 0x03 | [Bildschirm-Controller](#class-0x03---bildschirm-controller) |
| 0x04 | [Multimedia-Geräte](#class-0x04---multimedia-ger%C3%A4te) |
| 0x05 | [Speicher-Controller](#class-0x05---speicher-controller) |
| 0x06 | [Bridge-Geräte](#class-0x06---bridge-ger%C3%A4te) |
| 0x07 | [Controller zur einfachen Kommunikation](#class-0x07---controller-zur-einfachen-kommunikation) |
| 0x08 | [System-Peripherie](#class-0x08---system-peripherie) |
| 0x09 | [Input-Geräte](#class-0x09---input-ger%C3%A4te) |
| 0x0A | [Docking-Stationen](#class-0x0a---docking-stationen) |
| 0x0B | [Prozessoren](#class-0x0b---prozessoren) |
| 0x0C | [Serielle Buscontroller](#class-0x0c---serielle-buscontroller) |
| 0x0D | [Wireless-Controller](#class-0x0d---wireless-controller) |
| 0x0E | [Intelligente Controller](#class-0x0e---intelligente-controller) |
| 0x0F | [Satelliten-Kommunikations-Controller](#class-0x0f---satelliten-kommunikations-controller) |
| 0x10 | [Encryption/Decryption-Controller](#class-0x10---encryptiondecryption-controller) |
| 0x11 | [Datenerfassungs- und Signalprozessor-Controller](#class-0x11---datenerfassungs--und-signalprozessor-controller) |
| 0x12-0xFE | *Reserviert* |
| 0xFF | Sonstige |

### Class 0x00 - Pre 2.0

| Subclass | Programming Interface | Beschreibung |
| ---------- | ----------------------- | ---------------------------------------------------------------------------------------------------- |
| 0x00 | 0x00 | Alle nicht-VGA-Geräte |
| 0x01 | 0x00 | [VGA](https://github.com/lowlevel-eu/wiki/wiki/Video-Graphics-Array "Video Graphics Array")-Geräte |

### Class 0x01 - Massenspeicher

| Subclass | Programming Interface | Beschreibung |
| ---------- | ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0x00 | 0x00 | SCSI |
| 0x01 | 0x?? | IDE |
| 0x02 | 0x00 | [Floppy](https://github.com/lowlevel-eu/wiki/wiki/Floppy-Disk-Controller "Floppy Disk Controller") |
| 0x03 | 0x00 | IPI |
| 0x04 | 0x00 | RAID |
| 0x05 | 0x20 | [ATA](https://github.com/lowlevel-eu/wiki/wiki/AT-Attachment "AT Attachment")-Controller (Single [DMA](https://github.com/lowlevel-eu/wiki/wiki/Direct-Memory-Access "Direct Memory Access")) |
| 0x05 | 0x30 | ATA-Controller (Chained DMA) |
| 0x06 | 0x00 | SATA-Controller (Herstellerspezifische Schnittstelle) |
| 0x06 | 0x01 | SATA-Controller (AHCI 1.0) |
| 0x07 | 0x00 | SAS-Controller (Serial Attached SCSI) |
| 0x80 | 0x00 | Anderer Massenspeicher |

### Class 0x02 - [Netzwerk](https://lowlevel-eu.github.io/wiki/pages/1888/index.html "Kategorie:Netzwerk")-Controller

| Subclass | Programming Interface | Beschreibung |
| ---------- | ----------------------- | -------------------------------------------------------------------------- |
| 0x00 | 0x00 | [Ethernet](https://github.com/lowlevel-eu/wiki/wiki/Ethernet "Ethernet") |
| 0x01 | 0x00 | Token Ring |
| 0x02 | 0x00 | FDDI |
| 0x03 | 0x00 | ATM |
| 0x04 | 0x00 | ISDN |
| 0x05 | 0x00 | World FIP (Feldbus) |
| 0x06 | 0x?? | PICMG 2.14, Multi-Computing |
| 0x80 | 0x00 | Anderer Netzwerk-Controller |

### Class 0x03 - Bildschirm-Controller

| Subclass | Programming Interface | Beschreibung |
| ---------- | ----------------------- | ------------------------------- |
| 0x00 | 0x00 | VGA |
| 0x00 | 0x01 | 8514 |
| 0x01 | 0x00 | XGA |
| 0x02 | 0x00 | 3D |
| 0x80 | 0x00 | Anderer Bildschirm-Controller |

### Class 0x04 - Multimedia-Geräte

| Subclass | Programming Interface | Beschreibung |
| ---------- | ----------------------- | -------------------------- |
| 0x00 | 0x00 | Video-Gerät |
| 0x01 | 0x00 | Audio-Gerät |
| 0x02 | 0x00 | Telefonie |
| 0x03 | ?? | HD-Audio-Gerät |
| 0x80 | 0x00 | Anderes Multimedia-Gerät |

### Class 0x05 - Speicher-Controller

| Subclass | Programming Interface | Beschreibung |
| ---------- | ----------------------- | ------------------ |
| 0x00 | 0x00 | RAM |
| 0x01 | 0x00 | Flash-Speicher |
| 0x80 | 0x00 | Anderer Speicher |

### Class 0x06 - Bridge-Geräte

| Subclass | Programming Interface | Beschreibung |
| ---------- | ----------------------- | ----------------------------------------------------------- |
| 0x00 | 0x00 | Host/PCI-Bridge |
| 0x01 | 0x00 | PCI/ISA-Bridge |
| 0x02 | 0x00 | PCI/EISA-Bridge |
| 0x03 | 0x00 | PCI/MicroChannel-Bridge |
| 0x04 | 0x00 | PCI/PCI-Bridge (hat Header Type 0x01) |
| 0x04 | 0x01 | PCI/PCI-Bridge (Subtractive Decode, hat Header Type 0x01) |
| 0x05 | 0x00 | PCI/PCMCIA-Bridge |
| 0x06 | 0x00 | PCI/NuBus-Bridge |
| 0x07 | 0x00 | PCI/CardBus-Bridge |
| 0x08 | 0x?? | Raceway, Switched Fabric |
| 0x09 | 0x40 | Semitransparente PCI/PCI-Bridge (primär zum Host) |
| 0x09 | 0x80 | Semitransparente PCI/PCI-Bridge (sekundär zum Host) |
| 0x0A | 0x00 | InfiniBand/PCI-Brige |
| 0x80 | 0x?? | Anderer Bridge-Typ |

### Class 0x07 - Controller zur einfachen Kommunikation

| Subclass | Programming Interface | Beschreibung |
| ---------- | ----------------------- | ---------------------------------------- |
| 0x00 | 0x00 | Serielle Schnittstelle (XT-kompatibel) |
| 0x00 | 0x01 | Serielle Schnittstelle (16450) |
| 0x00 | 0x02 | Serielle Schnittstelle (16550) |
| 0x00 | 0x03 | Serielle Schnittstelle (16650) |
| 0x00 | 0x04 | Serielle Schnittstelle (16750) |
| 0x00 | 0x05 | Serielle Schnittstelle (16850) |
| 0x00 | 0x06 | Serielle Schnittstelle (16950) |
| 0x01 | 0x00 | Parallelport (Standard) |
| 0x01 | 0x01 | Parallelport (Bidirektional) |
| 0x01 | 0x02 | Parallelport (ECP 1.0) |
| 0x01 | 0x03 | Parallelport (IEEE 1284) |
| 0x01 | 0xFE | IEEE-1284-Gerät, Target |
| 0x02 | 0x00 | Multiport Serial Controller |
| 0x03 | 0x00 | Standard-Modem |
| 0x03 | 0x01 | Hayes-kompatibles Modem (16450) |
| 0x04 | 0x00 | GPIB (IEEE488.1/2) Controller |
| 0x04 | 0x02 | Hayes-kompatibles Modem (16550) |
| 0x04 | 0x03 | Hayes-kompatibles Modem (16650) |
| 0x04 | 0x04 | Hayes-kompatibles Modem (16750) |
| 0x05 | 0x00 | SmartCard |
| 0x80 | 0x00 | Anderer Controller |

### Class 0x08 - System-Peripherie

| Subclass | Programming Interface | Beschreibung |
| ---------- | ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0x00 | 0x00 | 8259- [PIC](https://github.com/lowlevel-eu/wiki/wiki/Programmable-Interrupt-Controller "Programmable Interrupt Controller") |
| 0x00 | 0x01 | ISA-PIC |
| 0x00 | 0x02 | EISA-PIC |
| 0x00 | 0x10 | IO- [APIC](https://github.com/lowlevel-eu/wiki/wiki/Advanced-Programmable-Interrupt-Controller "Advanced Programmable Interrupt Controller") (EISA) |
| 0x00 | 0x20 | IOx-APIC |
| 0x01 | 0x00 | 8237-DMA-Controller |
| 0x01 | 0x01 | ISA-DMA-Controller |
| 0x01 | 0x02 | EISA-DMA-Controller |
| 0x02 | 0x00 | Standard-8254-Timer |
| 0x02 | 0x01 | ISA-System-Timer |
| 0x02 | 0x02 | EISA-System-Timer |
| 0x03 | 0x00 | Standard [Real Time Clock](https://github.com/lowlevel-eu/wiki/wiki/Real-Time-Clock "Real Time Clock") |
| 0x03 | 0x01 | ISA Real Time Clock |
| 0x04 | 0x00 | PCI Hot Plug Controller |
| 0x06 | 0x00 | Root Complex Event Collector (für PCI-Express) |
| 0x80 | 0x00 | Andere System-Peripherie |

### Class 0x09 - Input-Geräte

| Subclass | Programming Interface | Beschreibung |
| ---------- | ----------------------- | ----------------------------------------------------------------------------------- |
| 0x00 | 0x00 | Tastatur |
| 0x01 | 0x00 | Digitizer (Stift) |
| 0x02 | 0x00 | Maus |
| 0x03 | 0x00 | Scanner |
| 0x04 | 0x00 | Standard-[Gameport](https://github.com/lowlevel-eu/wiki/wiki/Gameport "Gameport") |
| 0x04 | 0x10 | Gameport |
| 0x80 | 0x00 | Anderes Input-Gerät |

### Class 0x0A - Docking-Stationen

| Subclass | Programming Interface | Beschreibung |
| ---------- | ----------------------- | ------------------------- |
| 0x00 | 0x00 | Normale Docking-Station |
| 0x80 | 0x00 | Andere Docking-Station |

### Class 0x0B - Prozessoren

| Subclass | Programming-Interface | Beschreibung |
| ---------- | ----------------------- | -------------- |
| 0x00 | 0x00 | 386 |
| 0x01 | 0x00 | 486 |
| 0x02 | 0x00 | Pentium |
| 0x10 | 0x00 | Alpha |
| 0x20 | 0x00 | PowerPC |
| 0x30 | 0x00 | MIPS |
| 0x40 | 0x00 | Coprozessor |

### Class 0x0C - Serielle Buscontroller

| Subclass | Programming Interface | Beschreibung |
| ---------- | ----------------------- | --------------------------------------------------------------------------------------------------------- |
| 0x00 | 0x00 | Firewire (IEEE 1394) |
| 0x00 | 0x10 | Firewire (OHCI) |
| 0x01 | 0x00 | ACCESS-Bus |
| 0x02 | 0x00 | SSA (Serial Storage Architecture) |
| 0x03 | 0x00 | [USB](https://github.com/lowlevel-eu/wiki/wiki/Universal-Serial-Bus "Universal Serial Bus")-Host (UHCI) |
| 0x03 | 0x10 | USB-Host (OHCI) |
| 0x03 | 0x20 | USB-Host (EHCI) |
| 0x03 | 0x30 | USB-Host (xHCI) |
| 0x03 | 0x80 | USB-Host (kein HCI) |
| 0x03 | 0xFE | USB-Device |
| 0x04 | 0x00 | Fibre Channel |
| 0x05 | 0x00 | SMB (System Management Bus) |
| 0x06 | 0x00 | InfiniBand |
| 0x07 | 0x00 | IPMI SMIC Interface |
| 0x07 | 0x01 | IPMI Keyboard Style Interface |
| 0x07 | 0x02 | IPMI Block Transfer Device |
| 0x08 | 0x00 | SERCOS Interface |
| 0x09 | 0x00 | CAN-Bus |

### Class 0x0D - Wireless-Controller

| Subclass | Programming Interface | Beschreibung |
| ---------- | ----------------------- | ----------------------------- |
| 0x00 | 0x00 | iRDA |
| 0x01 | 0x00 | Consumer Infrared |
| 0x10 | 0x00 | Radio Frequency |
| 0x11 | 0x00 | Bluetooth |
| 0x12 | 0x00 | Broadband |
| 0x80 | 0x00 | Anderer Wireless-Controller |

### Class 0x0E - Intelligente Controller

| Subclass | Programming Interface | Beschreibung |
| ---------- | ----------------------- | ----------------- |
| 0x00 | 0x?? | I²O-Architektur |
| 0x00 | 0x00 | Message FIFO |

### Class 0x0F - Satelliten-Kommunikations-Controller

| Subclass | Programming Interface | Beschreibung |
| ---------- | ----------------------- | -------------- |
| 0x01 | 0x00 | TV |
| 0x02 | 0x00 | Audio |
| 0x03 | 0x00 | Sprache |
| 0x04 | 0x00 | Daten |

### Class 0x10 - Encryption/Decryption-Controller

| Subclass | Programming Interface | Beschreibung |
| ---------- | ----------------------- | -------------------- |
| 0x01 | 0x00 | Netzwerk |
| 0x10 | 0x00 | Entertainment |
| 0x80 | 0x00 | Anderer Controller |

### Class 0x11 - Datenerfassungs- und Signalprozessor-Controller

| Subclass | Programming Interface | Beschreibung |
| ---------- | ----------------------- | ------------------------------------- |
| 0x00 | 0x00 | Digital Input/Output Module |
| 0x01 | 0x00 | Zähler |
| 0x10 | 0x00 | Synchronisation und Frequenzmessung |
| 0x20 | 0x00 | Management Card |
| 0x80 | 0x00 | Anderer Controller |

## Weblinks

- [Linux PCI ID Repositorium](http://pci-ids.ucw.cz/) – Enthält viele Vendor- und die dazugehörigen Device-IDs
- [PCI Vendor and Device Lists](http://www.pcidatabase.com/index.php) – Enthält ebenfalls eine große Liste Vendor- und Device-IDs

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/11007/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1626/index.html)

<!-- MediaWiki page 1626; revision 11007; parent 9887; 2013-02-25T22:03:02Z -->
