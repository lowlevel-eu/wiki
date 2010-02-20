# I/O Advanced Programmable Interrupt Controller

Die **I/O APIC** (= **I/O Advanced Programmable Interrupt Controller**) löst den [Programmable Interrupt Controller](https://github.com/lowlevel-eu/wiki/wiki/Programmable-Interrupt-Controller "PIC") in einem [SMP](https://github.com/lowlevel-eu/wiki/wiki/Symmetrisches-Multiprozessorsystem "SMP")- bzw. [NUMA](https://github.com/lowlevel-eu/wiki/wiki/Non-Uniform-Memory-Architecture "NUMA")-System ab. Da der PIC die [IRQs](https://github.com/lowlevel-eu/wiki/wiki/Programmable-Interrupt-Controller#irq-tabelle "IRQ") ausschließlich an den BSP (= Bootstrap Processor) senden kann, ist in einem System mit mehreren Prozessoren eine I/O APIC notwendig. Darüber hinaus stellt die I/O APIC statt nur 16 IRQ-Leitungen wie der PIC normalerweise 24 IRQ-Leitungen zur Verfügung. Dies verringert die Anzahl der von mehreren Geräten gleichzeitig genutzten IRQs in Systemen mit sehr vielen Geräten. Außerdem ist die Programmierung der I/O APIC schneller, da sie nicht über I/O Ports, sondern über Speicherbereiche abläuft.

  

## Aufbau

### memory-mapped Register

Die folgenden Register sind in den physischen Adressraum des Systems eingeblendet und dienen dazu auf die [internen Register](https://github.com/lowlevel-eu/wiki/wiki/I-O-Advanced-Programmable-Interrupt-Controller#interne-register "I/O APIC") zuzugreifen:

  

| Index | Abkürzung | Beschreibung | Zugriffsart |
| ------- | ----------- | --------------------- | -------------------------- |
| 0x00 | IOREGSEL | I/O Register Select | 8Bit, lesend/schreibend |
| 0x04 | IOWIN | I/O Window | 32Bit, lesend/schreibend |

  

### Interne Register

Die folgenden Register dienen der Konfiguration der I/O APIC:

  

| Index | Abkürzung | Beschreibung | Zugriffsart |
| ---------- | ------------------ | ------------------------------------------------- | -------------------------- |
| 0x00 | IOAPICID | I/O APIC ID | 32Bit, lesend/schreibend |
| 0x01 | IOAPICVER | I/O APIC Version | 32Bit, nur lesend |
| 0x02 | IOAPICARB | I/O APIC Arbitration ID | 32Bit, nur lesend |
| 0x10 - ? | IOREDTBL\[0-23\] | *Redirection Table*-Eintrag 0-? (jeweils 64bit) | 32Bit, lesend/schreibend |

  

#### I/O APIC ID

| Bits | Beschreibung | Zugriffsart |
| ------- | ---------------------- | ------------------- |
| 28-31 | reserviert |  |
| 24-27 | 4Bit ID der I/O APIC | lesend/schreibend |
| 0-23 | reserviert |  |

#### I/O APIC Version

| Bits | Beschreibung | Zugriffsart |
| ------- | -------------------------------------------------------------------- | ------------- |
| 24-31 | reserviert |  |
| 26-23 | maximaler Index eines gültigen Eintrags in der *Redirection Table* | nur lesend |
| 8-15 | reserviert |  |
| 0-7 | I/O APIC Versionsnummer:<br>0x11 = 82093AA | nur lesend |

#### I/O APIC Arbitration ID

| Bits | Beschreibung | Zugriffsart |
| ------- | ---------------------------------- | ------------------- |
| 28-31 | reserviert |  |
| 24-27 | 4Bit Arbitration ID der I/O APIC | lesend/schreibend |
| 0-23 | reserviert |  |

#### Eintrag der *Redirection Table*

**Bits**

**Abkürzung**

**Name**

**Beschreibung**

**Zugriffsart**

56-63Destinationgibt die empfangende(n) [Local APIC](https://github.com/lowlevel-eu/wiki/wiki/Local-Advanced-Programmable-Interrupt-Controller "Local APIC")(s) an:

| Wert von DESTMOD | Modus | Beschreibung |
| ------------------ | --------------- | ----------------------------------------------------------- |
| 0 | Physical Mode | Bits 56-59 enthalten eine APIC ID |
| 1 | Logical Mode | Bits 56-63 werden als Menge von Prozessoren interpretiert |

lesend/schreibend 17-55reserviert 16Interrupt MaskDer Interrupt ist maskiert, falls der Wert 1 istlesend/schreibend 15Trigger Mode0b = edge sensitive  
1b = level sensitivelesend/schreibend 14Remote IRRnur lesend 13INTPOLInterrupt Input Pin Polarity0b = high active  
1b = low activelesend/schreibend 12DELIVSDelivery StatusDer Interrupt wird momentan ausgeliefert, falls der Wert 1 istnur lesend 11DESTMODDestination ModeGibt an wie das Destination-Feld zur Adressierung der empfangenden [Local APICs](https://github.com/lowlevel-eu/wiki/wiki/Local-Advanced-Programmable-Interrupt-Controller "Local APIC") interpretiert wird, siehe Destination-Feldlesend/schreiben 8-10 DELMOD Delivery Mode Gibt an wie die empfangenden [Local APICs](https://github.com/lowlevel-eu/wiki/wiki/Local-Advanced-Programmable-Interrupt-Controller "Local APIC") reagieren sollen:

| Wert | Modus | Beschreibung |
| ------ | ------------------------------------------------------------------------------ | -------------- |
| 000b | Fixed |  |
| 001b | niedrigste Priorität |  |
| 010b | [SMI](https://github.com/lowlevel-eu/wiki/wiki/SMI "SMI") |  |
| 011b | reserviert |  |
| 100b | [NMI](https://github.com/lowlevel-eu/wiki/wiki/Non-Maskable-Interrupt "NMI") |  |
| 101b | INIT |  |
| 110b | reserviert |  |
| 111b | ExtINT |  |

lesend/schreibend 0-7INTVECInterrupt Vectorauszulösender Interruptvektorlesend/schreibend

## Programmierung

### Basisadresse der I/O APIC

Die Basisadresse dieser Speicherbereiche kann im Allgemeinen über die [SMP](https://github.com/lowlevel-eu/wiki/wiki/Symmetrisches-Multiprozessorsystem#intel-multiprocessor-specification "Symmetrisches Multiprozessorsystem")- bzw. die [ACPI](https://github.com/lowlevel-eu/wiki/wiki/Advanced-Configuration-and-Power-Interface "ACPI")-Tabellen ausgelesen werden. Bei einem PIIX3 Chipsatz beginnt der Speicherbereich bei 0xFEC00xy00 (x und y werden mit dem APICBASE Register im PIIX3 festgelegt).

### Lesen/Schreiben der internen Register

Die I/O APIC besitzt ein Indexregister (*I/O Register Select* bzw. *IOREGSEL*) und ein Datenregister (*I/O Window* bzw. *IOWIN*). Mit dem Indexregister wählt man ein [internes Register](https://github.com/lowlevel-eu/wiki/wiki/I-O-Advanced-Programmable-Interrupt-Controller#interne-register "I/O APIC") der I/O APIC aus und kann anschließend über das Datenregister das interne Register auslesen bzw. beschreiben.

Folgender Code kann dazu verwendet werden auf die internen Register zuzugreifen: \<c\> /\* Offset der memory-mapped Register \*/

1.  define IO_APIC_MMREG_IOREGSEL 0x00
2.  define IO_APIC_MMREG_IOWIN 0x04

/\* Basisadresse, sollte vorher initialisiert werden \*/ uint8_t \* volatile io_apic_base;

/\* Lesen eines internen Registers \*/ uint32_t io_apic_read(uint8_t index) {

     *(io_apic_base + IO_APIC_MMREG_IOREGSEL) = index;
     return *(uint32_t * volatile)(io_apic_base + IO_APIC_MMREG_IOWIN);

}

/\* Schreiben eines internen Registers \*/ void io_apic_write(uint8_t index, uint32_t value) {

     *(io_apic_base + IO_APIC_MMREG_IOREGSEL) = index;
     *(uint32_t * volatile)(io_apic_base + IO_APIC_MMREG_IOWIN) = value;

} \</c\>

### Setzen der Einträge der *Redirection Table*

Die Einträge der *Redirection Table* werden basierend auf den Informationen, die die [SMP](https://github.com/lowlevel-eu/wiki/wiki/Symmetrisches-Multiprozessorsystem#intel-multiprocessor-specification "Symmetrisches Multiprozessorsystem")- bzw. die [ACPI](https://github.com/lowlevel-eu/wiki/wiki/Advanced-Configuration-and-Power-Interface "ACPI")-Tabellen enthalten, gesetzt.

## Weblinks

- [Intel® 82093AA I/O Advanced Programmable Interrupt Controller (I/O APIC) Datasheet](http://www.intel.com/design/chipsets/datashts/290566.htm)
- [Intel® 82093AA I/O Advanced Programmable Interrupt Controller (I/O APIC) Specification Update](http://www.intel.com/design/chipsets/specupdt/290710.htm)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/7123/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1574/index.html)

<!-- MediaWiki page 1574; revision 7123; parent 6286; 2010-02-20T16:51:09Z -->
