# Direct Memory Access

Unter **Direct Memory Access** (abgekürzt **DMA**) versteht man eine Methode, Daten von Peripheriegeräten zum Arbeitsspeicher und umgekehrt zu übertragen, ohne dafür die CPU benutzen zu müssen.

Es gibt zwei grundlegend verschiedene Methoden, DMA umzusetzen: Entweder das betreffende Peripheriegerät ist in der Lage, auf die Daten im Arbeitsspeicher selbst zuzugreifen (als *Busmaster*), oder es wird ein Hilfschip, der DMA-Controller, benötigt, dessen einzige Aufgabe es ist, die Daten aktiv zwischen einem Peripheriegerät und dem Arbeitsspeicher zu transferieren. Die erste Methode wird bei [PCI](Peripheral-Component-Interconnect "PCI")-Geräten verwendet und die zweite Methode wird u. a. von [ISA](Industry-Standard-Architecture "ISA")-Geräten benutzt. Aufgrund der unterschiedlichen Konzepte die sich hinter "DMA" verbergen sollte man bei der Verwendung dieses Begriffs immer etwas Vorsicht walten lassen.

Typische DMA- bzw. busmasterfähige PCI-Geräte sind z. B. (S)ATA-Host-Controller, Netzwerkkarten und neuere USB-Host-Controller.

Busmastering bedeutet, dass ein Peripheriegerät selbstständig (in Abhängigkeit von entsprechenden Ereignissen) auf den Speicher oder auch auf andere Peripheriegeräte zugreifen kann &#150; so wie die CPU auch selbstständig (in Abhängigkeit vom gerade ausgeführten Programm) auf den Speicher zugreift. Dieses Feature wird besonders von Multitasking-Betriebssystemen benötigt, da hier der Prozesswechsel sonst durch z. B. Festplattenzugriffe verzögert werden müsste.

  

## Gemeinsamkeiten/Unterschiede von PCI-DMA und ISA-DMA

Eine wesentliche Gemeinsamkeit beider Methoden ist, dass die Software die Speicherzugriffe der Peripheriegeräte vorbereiten muss. Die Software muss bestimmen, an welchen (physischen) Adressen im Speicher die Daten liegen bzw. hingeschrieben werden sollen. Des Weiteren informieren die Peripheriegeräte die CPU meist mit einem Interrupt, wenn alle Daten transferiert wurden, damit der entsprechende Gerätetreiber die Daten verarbeiten und/oder neue Daten vorbereiten kann.

Der wichtigste Unterschied beider Methoden ist, dass es bei PCI-DMA keine einheitliche Möglichkeit gibt, mit der die Software die DMA-Fähigkeiten der Peripheriegeräte steuern kann, wohingegen der ISA-DMA-Controller immer der selbe ist.

Dagegen sind die Fähigkeiten der meisten PCI-DMA-Implementierungen deutlich leistungsfähiger, es können oft mehrere DMA-Jobs auf einmal dem Peripheriegerät mitgeteilt werden, sodass dieses deutlich seltener die CPU in Anspruch nehmen muss. Auch sind die meisten PCI-Geräte in der Lage, die Daten aus mehreren verteilten Speicherbereichen zusammenzutragen (*scatter/gather*). Der ISA-DMA-Controller kann Daten immer nur aus unmittelbar zusammenhängenden Speicherbereichen transferieren.

Grundsätzlich sind die PCI-DMA-Implementierungen deutlich leistungsfähiger; vor allem, weil sie auf die Bedürfnisse des entsprechenden PCI-Gerätes speziell zugeschnitten sind. Der ISA-DMA-Controller ist recht unflexibel, er ist z. B. nicht in der Lage, selbstständig einen neuen DMA-Job zu laden, sondern ist immer auf die Hilfe der Software angewiesen. Der ISA-DMA-Controller kann nur Speicherbereiche in den ersten 16 MByte ansprechen. PCI-Geräte können mindestens 32-Bit-Adressen benutzen, viele sind auch fähig, mit 64-Bit-Adressen umzugehen.

ISA-DMA wird in heutigen PCs nur noch für das Floppy-Laufwerk und ganz selten für ISA-Soundkarten benutzt. In vielen Computern, die z. B. für den Einsatz als Steuerungen in der Industrie gedacht sind, gibt es diese Möglichkeit bereits gar nicht mehr (*Legacy-Free*). Es ist daher nur eine Frage der Zeit, bis dieser Mechanismus aus den PCs komplett verschwunden ist. Die Möglichkeiten, die moderne PCI-DMA-Implementierungen bieten, lassen sich nicht mit ISA-DMA realisieren &#150; nebst dessen, dass PCI und seine (aktuellen) Nachfolger wie PCI-Express, Hypertransport, PCI-X und AGP deutlich schneller arbeiten können.

  

## PCI-DMA

Da bei PCI-DMA jedes Gerät eine eigene Implementierung hat, kann man dazu kaum etwas allgemeines vermitteln. Als einfaches Beispiel kann z. B. die EHCI-Spezifikation gelten; dort wird gezeigt, wie alle relevanten Informationen über die zu erledigenden Arbeiten des EHCI-Host-Controllers und die zu transferierenden Daten in entsprechenden Strukturen im Arbeitsspeicher untergebracht sind. Auf diese Strukturen kann die Software mit ganz normalen Speicherzugriffen arbeiten und auch der EHCI-Host-Controller liest und modifiziert diese Strukturen mit eigenen Speicherzugriffen (eben als Busmaster) auf den Arbeitsspeicher.

Eine ganz wesentliche Eigenschaft nahezu aller PCI-DMA-Implementierungen ist, dass die zu transferierenden Daten nicht an einem Stück im Arbeitsspeicher vorliegen müssen. Dieses Feature wird oft als "*Scatter/Gather*" bezeichnet. Dabei bekommt das PCI-Gerät nicht einfach nur gesagt, wo die Daten liegen bzw. hingeschrieben werden sollen, sondern es wird eine Liste mit einem oder mehreren Pointern+Größenangaben zu den einzelnen Datenhäppchen übergeben, welche das PCI-Gerät dann selbstständig abarbeitet. Dieses Feature ist deshalb so wichtig, weil in modernen Betriebssystemen das [Paging](Paging "Paging") benutzt wird und es daher nur sehr selten vorkommt, dass Daten, die im virtuellen Adressraum der Software am Stück vorliegen, auch physisch an einem Stück im Speicher liegen.

## ISA-DMA Controller

Für DMA-Transfere wurde in früheren PCs ein Chip mit der Bezeichnung 8237A verwendet. Im Laufe der Zeit wurde ein weiterer Controller hinzugefügt und die Hardware in den Chipsatz integriert. Die beiden Controller sind miteinander verbunden, einer von ihnen arbeitet als Master, der andere als Slave. Jeder der beiden Controller stellt vier sog. **Channel**, also Kanäle, zur Verfügung. Dadurch sind parallele und unabhängige Übertragungen möglich.

Vor einer Datenübertragung muss der Controller richtig programmiert bzw. initialisiert werden. Die meisten Einstellungen, die hierfür nötig sind, können für jeden Channel einzeln geändert werden; das heißt, dass alle Channel unabhängig voneinander programmiert werden müssen und unabhängig voneinander die Daten übertragen.

Der eigentliche Transfer wird in der Regel von dem mit diesem Channel verbundenen Stück Hardware gestartet. Dafür hat jeder Controller vier Leitungen mit den Namen DREQ0 bis DREQ3, die den Transfer über den entsprechenden Channel starten. Alternativ kann dieses Signal auch per Software emuliert werden, um die Datenübertragung manuell zu starten. Dazu wird das Requestregister benötigt, das weiter unten beschrieben wird. Die Übertragung wird beendet, wenn die vorab definierte Datenmenge übertragen wurde oder wenn ein Signal auf der EOP-Leitung des Controllers ankommt, d. h. die Übertragung von der Hardware aus beendet wird.

### Übersicht der I/O-Ports

Die folgende Tabelle ist eine Übersicht über alle [Ports](I-O-Ports "Port"), die von den beiden Controllern belegt werden. Master- und Slave-Controller verwenden dabei verschiedene Ports. Weiterhin muss beachtet werden, dass die vier Channel pro Controller ebenfalls etliche getrennte Ports verwenden. So kommt ingesammt eine vergleichsweise hohe Zahl an Ports zusammen.

Mit „Zugriff“ ist der [Assemblerbefehl](Assembler "Assembler") gemeint, mit dem auf den Port zugegriffen werden kann. Diese Spalte gibt an, ob lesend oder schreibend zugegriffen wird. Die Spalte „Größe“ gibt an, wieviele Bits das entsprechende Register umfasst. Auch wenn hier 16 stehen sollte, wird nur byteweise mit den DMA-Controllern kommuniziert &#150; siehe dazu die Beschreibung des Flip-Flop-Registers.

  

| Name des Registers | Port Master | Port Slave | Zugriff | Größe | Beschreibung |
| ----------------------------- | ------------- | ------------ | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Startadresse | Ch 0: 0x00 | Ch 0: 0xC0 | out | 16 | Die Startadresse des Puffers für die Daten |
|  | Ch 1: 0x02 | Ch 1: 0xC2 | out | 16 |  |
|  | Ch 2: 0x04 | Ch 2: 0xC4 | out | 16 |  |
|  | Ch 3: 0x06 | Ch 3: 0xC6 | out | 16 |  |
| Zähler | Ch 0: 0x01 | Ch 0: 0xC1 | out | 16 | Anzahl der zu übertragenden Bytes minus eins |
|  | Ch 1: 0x03 | Ch 1: 0xC3 | out | 16 |  |
|  | Ch 2: 0x05 | Ch 2: 0xC5 | out | 16 |  |
|  | Ch 3: 0x07 | Ch 3: 0xC7 | out | 16 |  |
| Aktuelle Adresse | Ch 0: 0x00 | Ch 0: 0xC0 | in | 16 | Die aktuelle Adresse. Sie gibt an, wo der DMA-Controller gerade liest oder schreibt. |
|  | Ch 1: 0x02 | Ch 1: 0xC2 | in | 16 |  |
|  | Ch 2: 0x04 | Ch 2: 0xC4 | in | 16 |  |
|  | Ch 3: 0x06 | Ch 3: 0xC6 | in | 16 |  |
| Aktueller Zähler | Ch 0: 0x01 | Ch 0: 0xC1 | in | 16 | Der momentane Zählerstand gibt an, wie viele Bytes noch verbleiben. |
|  | Ch 1: 0x03 | Ch 1: 0xC3 | in | 16 |  |
|  | Ch 2: 0x05 | Ch 2: 0xC5 | in | 16 |  |
|  | Ch 3: 0x07 | Ch 3: 0xC7 | in | 16 |  |
| Page | Ch 0: 0x87 | Ch 0: 0x8F | out/in | 8 | Da sich mit Hilfe der Startadresse nur ein 16-Bit-Adressraum ansprechen lässt, also 64 KiB, kann hierüber eine Page festegelegt werden. Die Startadresse wird also auf eine 24-Bit-Adresse erweitert, womit sich immerhin 16 MiB ansprechen lässt. Dieses 8-Bit-Register nimmt dabei die Bits 16 &#150; 23 dieser Adresse auf. |
|  | Ch 1: 0x83 | Ch 1: 0x8B | out/in | 8 |  |
|  | Ch 2: 0x81 | Ch 2: 0x89 | out/in | 8 |  |
|  | Ch 3: 0x82 | Ch 3: 0x8A | out/in | 8 |  |
| Status | 0x08 | 0xD0 | in | 8 | Liefert Statusinformationen zum DMA-Controller (siehe dazu unten). |
| Befehle | 0x08 | 0xD0 | out | 8 | Befehle, die der Controller ausführen soll, werden hierein geschrieben (für eine Liste der Befehle siehe unten). |
| Controller zurücksetzen | 0x0D | 0xDA | out | &#151; | Durch Schreiben in dieses Register wird ein Reset des entsprechenden Controllers durchgeführt. |
| Flip-Flop | 0x0C | 0xD8 | out | 8 | Dieses Register ist nötig, um mit 8-Bit-Zugriffen, die 16-Bit-Register zu verwenden. Vor dem Zugriff auf ein 16-Bit-Register sollte eine Null an dieses Register gesendet werden. Dadurch wird der Flip-Flop des Controllers zurückgesetzt und es wird beim anschließenden Zugriff auf ein 16-Bit-Register das Low-Byte adressiert. Der Controller wird das Flip-Flop-Register danach selbstständig auf Eins setzen, wodurch der nächste Zugriff das High-Byte adressiert. Dies ist sowohl beim Lesen als auch beim Schreiben aus bzw. in 16-Bit-Register nötig. |
| Transfermodus | 0x0B | 0xD6 | out | 8 | Über dieses Register kann der Übertragungsmodus für einen Channel und einige weitere ergänzende Details zum Befehl, der an das Befehlsregister gesendet wird, festgelegt werden (Für eine genaue Beschreibung siehe unten). |
| Maskierung eines Channels | 0x0A | 0xD4 | out | 8 | Hierüber kann ein einzelner Channel maskiert, also deaktiviert, werden. Dies sollte immer(!) getan werden, wenn der Controller auf einen Transfer vorbereitet wird, um gleichzeitige Zugriffe von mehreren Programmen zu unterbinden. Die Bits 0 und 1 enthalten dabei die Nummer des Channels, dessen Status geändert werden soll. In Bit 2 wird angegeben, ob der gewählte Channel aktiviert (0) oder deaktiviert (1) werden soll. |
| Maskierung mehrerer Channel | 0x0F | 0xDE | out | 8 | Dieses Register hat die gleiche Funktion wie das Maskierungsregister oben, aber mit dem Unterschied, dass mit Hilfe dieses Registers der Zustand meherer Channel gleichzeitig geändert werden kann. Bit 0 bis 3 geben dabei an, ob der entsprechende Channel (0 &#150; 3) aktiviert (0) oder deaktiviert (1) werden soll. Hierbei ist zu beachten, dass nicht aus Versehen ein Channel irrtümlicherweise (de)aktiviert wird, dessen Status eigentlich unverändert bleiben soll. |
| Request | 0x09 | 0xD2 | out | 8 | Dieses Register ermöglicht es, einen Transfer mittels Software auszulösen. Für den Aufbau des zu sendenen Bytes siehe unten. |

### Aufbau der I/O Ports

#### Statusregister

Das Statusregister enthält einige Informationen über die Channel des jeweiligen Controllers. Es ist ein Byte groß und ist folgendermaßen zusammengesetzt:

| Bit | Beschreibung bei gesetztem Bit |
| ----- | --------------------------------------- |
| 0 | Terminal Count bei Channel 0 erreicht |
| 1 | Terminal Count bei Channel 1 erreicht |
| 2 | Terminal Count bei Channel 2 erreicht |
| 3 | Terminal Count bei Channel 3 erreicht |
| 4 | DMA-Request für Channel 0 |
| 5 | DMA-Request für Channel 1 |
| 6 | DMA-Request für Channel 2 |
| 7 | DMA-Request für Channel 3 |

Mit Terminal Count ist das Umspringen des Zählers von 0x0000 auf 0xFFFF bzw. von 0xFFFF auf 0x0000 &#150; je nach Zählrichtung &#150; gemeint. Wenn dies der Fall ist, wird die Übertragung beendet.

Die DMA-Request-Bits sind auf Eins gesetzt, wenn das dem Channel zugehörige Gerät eine Übertragung per Hardwaresignal starten möchte.

#### Befehlsregister

| Bit | Beschreibung bei gesetztem Bit |
| ----- | -------------------------------- |
| 0 | x |
| 1 | x |
| 2 | DMA-Controller deaktivieren |
| 3 | x |
| 4 | x |
| 5 | x |
| 6 | x |
| 7 | x |

x: Bit funktioniert anscheinend nicht

#### Transfermodusregister

Mit Hilfe des Transfermodusregisters lassen sich etliche Einstellungen zu jedem Channel bearbeiten. Dazu wird ein Byte nach dem folgenden Schema zusammengesetzt und an den entsprechenden Port geschickt.

| Bit | Beschreibung |
| ----- | ------------------------------------------------------------------ |
| 0-1 | Channelnummer |
| 2-3 | Transferrichtung: |
|  | 00 = Verifizieren: Selbsttest des Controllers |
|  | 01 = Schreiben: Vom Gerät zum RAM |
|  | 10 = Lesen: Von RAM zum Gerät |
|  | 11 = undefiniert |
| 4 | Autoinitialisierung |
| 5 | Zählrichtung: |
|  | 0 = Adressregister wird inkrementiert, es wird aufwärts gezählt. |
|  | 1 = Adressregister wird dekrementiert, es wird abwärts gezählt. |
| 6-7 | Transfermodus: |
|  | 00 = Demand-Transfer |
|  | 01 = Einzel-Transfer |
|  | 10 = Block-Transfer |
|  | 11 = Kaskadierung |

Autoinitialisierung: Wenn das Autoinitialisierungsbit gesetzt ist, wird beim Eintreten des Terminal Counts oder bei einem Signal auf der EOP-Leitung die Startadresse und der Zähler auf den zuletzt einprogrammierten Wert zurückgesetzt. Das kann beispielsweise für den [Floppy](Floppy-Disk-Controller "Floppy")-Treiber interessant sein; der gleiche Puffer wird immer wieder verwendet und der Zähler wird nach jedem Lese- oder Schreibvorgang auf die Sektorlänge zurückgesetzt.

#### Requestregister

Das Requestregister wird verwendet, um einen Transfer manuell per Software auszulösen. Dazu wird ein Byte an den entsprechenden Port geschickt, das so aufgebaut ist:

| Bit | Beschreibung |
| ----- | ----------------------------------------------------------------- |
| 0-1 | Channelnummer |
| 2 | Request-Bit: |
|  | 0 = Kein Request |
|  | 1 = Request; das ist das, was wohl in allen Fällen gewollt ist. |
| 3-7 | ungenutzt, sollte null sein |

  

## Weblinks

- [DMA-Artikel in der englischen Wikipedia](http://en.wikipedia.org/wiki/Direct_memory_access)
- [DMA anhand des Linux-Kernels erklärt](http://www.oreilly.de/german/freebooks/linuxdrive2ger/memdma.html)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/10699/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1555/index.html)

<!-- MediaWiki page 1555; revision 10699; parent 9979; 2012-08-20T10:08:12Z -->
