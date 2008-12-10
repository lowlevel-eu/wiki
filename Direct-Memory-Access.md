# Direct Memory Access

**Direct Memory Access** (Abkürzung: **DMA**) ist eine Methode um einfache Kopiervorgänge, von Geräten zum Speicher oder umgekehrt, mit einem extra Chip anstelle der CPU zu vollziehen. Dadurch ist die CPU während des Kopierens nicht ausgelastet und kann anderweitig verwendet werden. Dies ist insbesondere bei Betriebssystemen wichtig, die [Multitasking](https://github.com/lowlevel-eu/wiki/wiki/Multitasking "Multitasking") verwenden, da sonst der Prozesswechsel beispielsweise bei Festplattenzugriffen verzögert werden müsste.

## Physikalischer Aufbau

Für DMA-Transfere wurde in früheren PCs ein Chip mit der Bezeichnung 8237A verwendet. Im Laufe der Zeit wurde ein weiterer Controller hinzugefügt und die Hardware in den Chipsatz integriert.

Die beiden Controller sind miteinander verbunden, einer von ihnen arbeitet als Master, der andere als Slave.

## Programmierung der Controller

### Übersicht

Die folgende Tabelle ist eine Übersicht über alle [Ports](https://github.com/lowlevel-eu/wiki/wiki/I-O-Ports "Port"), die von den beiden Controllern belegt werden. Master- und Slave-Controller verwenden dabei verschiedene Ports. Weiterhin muss beachtet werden, dass pro Controller **vier sog. Channel**, also Kanäle, zur Verfügung stehen; sie ermöglichen parallele und unabhängige Datenübertragung. Jeder Channel verwendet dabei wiederum eigene Ports, wodurch eine vergleichsweise hohe Zahl an Ports zusammenkommt.

Mit "Zugriff" ist der [Assemblerbefehl](https://github.com/lowlevel-eu/wiki/wiki/Assembler "Assembler") gemeint, mit dem auf den Port zugegriffen werden kann. Diese Spalte gibt an, ob lesend oder schreibend zugegriffen wird. Die Spalte "Größe" gibt an, wieviele Bits das entsprechende Register umfasst. Auch wenn hier 16 stehen sollte, wird nur byteweise mit den DMA-Controllern kommuniziert - siehe dazu die Beschreibung des Flip-Flop-Registers.

  

| Name des Registers | Port Slave | Port Master | Zugriff | Größe | Beschreibung |
| ----------------------------- | ------------ | ------------- | --------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Startadresse | Ch 0: 0x00 | Ch 0: 0xC0 | out | 16 | Die Startadresse des Buffers für die Daten |
|  | Ch 1: 0x02 | Ch 1: 0xC2 | out | 16 |  |
|  | Ch 2: 0x04 | Ch 2: 0xC4 | out | 16 |  |
|  | Ch 3: 0x06 | Ch 3: 0xC6 | out | 16 |  |
| Zähler | Ch 0: 0x01 | Ch 0: 0xC1 | out | 16 | Anzahl der Bytes, die übertragen werden sollen, minus eins |
|  | Ch 1: 0x03 | Ch 1: 0xC3 | out | 16 |  |
|  | Ch 2: 0x05 | Ch 2: 0xC5 | out | 16 |  |
|  | Ch 3: 0x07 | Ch 3: 0xC7 | out | 16 |  |
| Aktuelle Adresse | Ch 0: 0x00 | Ch 0: 0xC0 | in | 16 | Die Aktuelle Adresse. Sie gibt an, wo der DMA-Controller gerade liest oder schreibt |
|  | Ch 1: 0x02 | Ch 1: 0xC2 | in | 16 |  |
|  | Ch 2: 0x04 | Ch 2: 0xC4 | in | 16 |  |
|  | Ch 3: 0x06 | Ch 3: 0xC6 | in | 16 |  |
| Aktueller Zähler | Ch 0: 0x01 | Ch 0: 0xC1 | in | 16 | Der momentane Zählerstand gibt an, wie viele Bytes noch verbleiben |
|  | Ch 1: 0x03 | Ch 1: 0xC3 | in | 16 |  |
|  | Ch 2: 0x05 | Ch 2: 0xC5 | in | 16 |  |
|  | Ch 3: 0x07 | Ch 3: 0xC7 | in | 16 |  |
| Page | Ch 0: 0x87 | Ch 0: 0x8F | out/in | 8 | Da sich mit Hilfe der Startadresse nur ein 16bit-Adressraum ansprechen lässt, also 64KiB, kann hierüber eine Page festegelegt werden. Die Startadresse wird also auf eine 24bit-Adresse erweiter, womit sich immerhin 1MiB ansprechen lässt. Dieses 8bit-Register nimmt dabei die Bits 16-23 dieser Adresse auf. |
|  | Ch 1: 0x83 | Ch 1: 0x8B | out/in | 8 |  |
|  | Ch 2: 0x81 | Ch 2: 0x89 | out/in | 8 |  |
|  | Ch 3: 0x82 | Ch 3: 0x8A | out/in | 8 |  |
| Status | 0x08 | 0xD0 | in | 8 | Liefert Statusinformationen zum DMA-Controller (siehe dazu unten) |
| Befehle | 0x08 | 0xD0 | out | 8 | Befehle, die der Controller ausführen soll, werden hierein geschrieben (für eine Liste der Befehle siehe unten) |
| Controller zurücksetzen | 0x0D | 0xDA | out | \- | Durch Schreiben in dieses Register wird ein Reset des entsprechenden Controllers durchgeführt |
| Flip-Flop | 0x0C | 0xD8 | out | 8 | Dieses Register ist nötig, um mit 8bit-Zugriffen, die 16bit-Register zu verwenden. Vor dem Zugriff auf ein 16bit-Register sollte eine Null an dieses Register gesendet werden. Dadurch wird der Flip-Flop des Controllers zurückgesetzt und es wird beim anschließenden Zugriff auf ein 16bit-Register das Low-Byte adressiert. Der Controller wird das Flip-Flop-Register danach selbstständig auf Eins setzen, wodurch der nächste Zugriff das High-Byte adressiert. Dies ist sowohl beim Lesen als auch beim Schreiben aus bzw. in 16bit-Register nötig. |
| Transfermodus | 0x0B | 0xD6 | out | 8 | Über dieses Register kann der Übertragungsmodus für einen Channel und einige weitere ergänzende Details zum Befehl, der an das Befehlsregister gesendet wird, festgelegt werden (Für eine genaue Beschreibung siehe unten) |
| Maskierung eines Channels | 0x0A | 0xD4 | out | 8 | Hierüber kann ein einzelner Channel maksiert, also deaktiviert, werden. Dies sollte immer(!) getan werden, wenn der Controller auf einen Transfer vorbereitet wird, um gleichzeitige Zugriffe von mehreren Programmen zu unterbinden. Die Bits 0 und 1 enthalten dabei die Nummer des Channels, dessen Status geändert werden soll. In Bit 2 wird angegeben, ob der gewählte Channel aktiviert (0) oder deaktiviert (1) werden soll. |
| Maskierung mehrerer Channel | 0x0F | 0xDE | out | 8 | Dieses Register hat die gleiche Funktion wie das Maskierungsregister oben, aber mit dem Unterschied, dass mit Hilfe dieses Registers der Zustand meherer Channel gleichzeitig geändert werden kann. Bit 0 bis 3 geben dabei an, ob der entsprechende Channel (0-3) aktiviert (0) oder deaktiviert (1) werden soll. Hierbei muss aufgepasst werden, dass nicht aus Versehen ein Channel irrtümlicherweise (de)aktiviert wird, dessen Status eigentlich unverändert bleiben soll. |
| Request | 0x09 | 0xD2 | out | 8 | Dieses Register ermöglicht es, einen Transfer mittels Software auszulösen. Für den Aufbau des zu sendenen Bytes siehe unten |

### Aufbau der zusammengesetzten Bytes

#### Statusregister

**TODO**

#### Befehlsregister

**TODO**

#### Transfermodusregister

**TODO**

#### Requestregister

**TODO**

  

### Alles zusammensetzen: Vorbereiten einer Übertragung

**TODO**

## Beispiel

**TODO**

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/3667/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1555/index.html)

<!-- MediaWiki page 1555; revision 3667; parent 2693; 2008-12-10T18:00:33Z -->
