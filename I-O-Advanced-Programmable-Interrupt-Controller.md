# I/O Advanced Programmable Interrupt Controller

Der **I/O APIC** (= **I/O Advanced Programmable Interrupt Controller**) löst den [Programmable Interrupt Controller](https://github.com/lowlevel-eu/wiki/wiki/Programmable-Interrupt-Controller "PIC") in einem [SMP](https://github.com/lowlevel-eu/wiki/wiki/Symmetrisches-Multiprozessorsystem "SMP")- bzw. [NUMA](https://github.com/lowlevel-eu/wiki/wiki/Non-Uniform-Memory-Architecture "NUMA")-System ab. Da der PIC die [IRQs](https://github.com/lowlevel-eu/wiki/wiki/Programmable-Interrupt-Controller#irq-tabelle "IRQ") ausschließlich an den BSP (= Bootstrap Processor) senden kann, ist in einem System mit mehreren Prozessoren ein I/O APIC notwendig. Darüber hinaus stellt der I/O APIC statt nur 16 IRQ-Leitungen wie der PIC normalerweise 24 IRQ-Leitungen zur Verfügung. Dies verringert die Anzahl der von mehreren Geräten gleichzeitig genutzten IRQs in Systemen mit sehr vielen Geräten. Außerdem ist die Programmierung des I/O APIC schneller, da sie nicht über I/O Ports, sondern über Speicherbereiche abläuft.

  

## Aufbau

### memory-mapped Register

Die folgenden Register sind in den physischen Adressraum des Systems eingeblendet und dienen dazu auf die [internen Register](https://github.com/lowlevel-eu/wiki/wiki/I-O-Advanced-Programmable-Interrupt-Controller#interne-register "I/O APIC") zuzugreifen:

  

| Offset | Abkürzung | Beschreibung | Zugriffsart |
| -------- | ----------- | --------------------- | -------------------------- |
| 0x00 | IOREGSEL | I/O Register Select | 8Bit, lesend/schreibend |
| 0x10 | IOWIN | I/O Window | 32Bit, lesend/schreibend |

  

### Interne Register

Die folgenden Register dienen der Konfiguration des I/O APIC:

  

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
| 24-27 | 4Bit ID des I/O APIC | lesend/schreibend |
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
| 24-27 | 4Bit Arbitration ID des I/O APIC | lesend/schreibend |
| 0-23 | reserviert |  |

#### *Redirection Table*

##### Aufbau eines Eintrags

| Bits | Abkürzung | Name | Beschreibung | Zugriffsart |
| ------- | ----------- | ------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------- |
| 56-63 |  | Destination | gibt den/die empfangenden [Local APIC](https://github.com/lowlevel-eu/wiki/wiki/Local-Advanced-Programmable-Interrupt-Controller "Local APIC")(s) an, Erklärung siehe [*Destination*-Tabelle](https://github.com/lowlevel-eu/wiki/wiki/I-O-Advanced-Programmable-Interrupt-Controller#destination "I/O APIC") | lesend/schreibend |
| 17-55 |  |  | reserviert |  |
| 16 |  | Interrupt Mask | Der Interrupt ist maskiert, falls der Wert 1 ist | lesend/schreibend |
| 15 |  | Trigger Mode | 0b = edge sensitive<br>1b = level sensitive | lesend/schreibend |
| 14 |  | Remote IRR | Dieses Bit ist nur gültig, wenn der *Trigger Mode* *edge* ist:<br>0b = EOI mit passendem Interruptvektor wurde gesendet<br>1b = Interrupt wurde vom [Local APIC](https://github.com/lowlevel-eu/wiki/wiki/Local-Advanced-Programmable-Interrupt-Controller "Local APIC") bzw. den Local APICs angenommen | nur lesend |
| 13 | INTPOL | Interrupt Input Pin Polarity | 0b = high active<br>1b = low active | lesend/schreibend |
| 12 | DELIVS | Delivery Status | Der Interrupt wird momentan ausgeliefert, falls der Wert 1 ist | nur lesend |
| 11 | DESTMOD | Destination Mode | Gibt an wie das Destination-Feld zur Adressierung der empfangenden [Local APICs](https://github.com/lowlevel-eu/wiki/wiki/Local-Advanced-Programmable-Interrupt-Controller "Local APIC") interpretiert wird, siehe Destination-Feld | lesend/schreiben |
| 8-10 | DELMOD | Delivery Mode | Gibt an wie die empfangenden [Local APICs](https://github.com/lowlevel-eu/wiki/wiki/Local-Advanced-Programmable-Interrupt-Controller "Local APIC") reagieren sollen, Erklärung siehe [*Delivery Mode*-Tabelle](https://github.com/lowlevel-eu/wiki/wiki/I-O-Advanced-Programmable-Interrupt-Controller#delivery-mode "I/O APIC") | lesend/schreibend |
| 0-7 | INTVEC | Interrupt Vector | auszulösender Interruptvektor | lesend/schreibend |

##### *Destination*

| Wert von DESTMOD | Modus | Beschreibung |
| ------------------ | --------------- | ----------------------------------------------------------- |
| 0 | Physical Mode | Bits 56-59 enthalten eine APIC ID |
| 1 | Logical Mode | Bits 56-63 werden als Menge von Prozessoren interpretiert |

##### *Delivery Mode*

| Wert | Modus | Beschreibung |
| ------ | ------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 000b | Fixed | Löst in den durch das *Destination*-Feld ausgewählten Prozessoren einen normalen Interrupt aus. |
| 001b | niedrigste Priorität | Löst in dem Prozessor mit der momentan geringsten Priorität der durch das *Destination*-Feld ausgewählten Prozessoren einen normalen Interrupt aus. |
| 010b | [SMI](https://github.com/lowlevel-eu/wiki/wiki/SMI "SMI") | Es wird allen durch das *Destination*-Feld ausgewählten Prozessoren ein SMI signalisiert. Dabei wird der Interruptvektor ignoriert, sollte aber aus Kompatibilitätsgründen auf 0 gesetzt werden. Der *Trigger Mode* muss *edge* sein. |
| 011b | reserviert |  |
| 100b | [NMI](https://github.com/lowlevel-eu/wiki/wiki/Non-Maskable-Interrupt "NMI") | Es wird allen durch das *Destination*-Feld ausgewählten Prozessoren ein NMI signalisiert. Dabei wird der Interruptvektor ignoriert. Der *Trigger Mode* muss *edge* sein. |
| 101b | INIT |  |
| 110b | reserviert |  |
| 111b | ExtINT | Analog zu *Fixed* wird ein normaler Interrupt ausgelöst. Der Interruptvektor kommt allerdings nicht vom I/O APIC sondern wird von einem externen Controller (z.B. des [PIC](https://github.com/lowlevel-eu/wiki/wiki/Programmable-Interrupt-Controller "PIC")) geliefert. Der *Trigger Mode* muss *edge* sein. |

  

## Programmierung

### Basisadresse des I/O APIC

Die Basisadresse dieser Speicherbereiche kann im Allgemeinen über die [SMP](https://github.com/lowlevel-eu/wiki/wiki/Symmetrisches-Multiprozessorsystem#intel-multiprocessor-specification "Symmetrisches Multiprozessorsystem")- bzw. die [ACPI](https://github.com/lowlevel-eu/wiki/wiki/Advanced-Configuration-and-Power-Interface "ACPI")-Tabellen ausgelesen werden. Bei einem PIIX3 Chipsatz beginnt der Speicherbereich bei 0xFEC00xy00 (x und y werden mit dem APICBASE Register im PIIX3 festgelegt).

### Lesen/Schreiben der internen Register

Der I/O APIC besitzt ein Indexregister (*I/O Register Select* bzw. *IOREGSEL*) und ein Datenregister (*I/O Window* bzw. *IOWIN*). Mit dem Indexregister wählt man ein [internes Register](https://github.com/lowlevel-eu/wiki/wiki/I-O-Advanced-Programmable-Interrupt-Controller#interne-register "I/O APIC") des I/O APIC aus und kann anschließend über das Datenregister das interne Register auslesen bzw. beschreiben.

Folgender Code kann dazu verwendet werden auf die internen Register zuzugreifen: \<c\> /\* Offset der memory-mapped Register \*/

1.  define IO_APIC_MMREG_IOREGSEL 0x00
2.  define IO_APIC_MMREG_IOWIN 0x10

/\* Basisadresse, sollte vorher initialisiert werden \*/ volatile uint8_t \* io_apic_base;

/\* Lesen eines internen Registers \*/ uint32_t io_apic_read(uint8_t index) {

     *(io_apic_base + IO_APIC_MMREG_IOREGSEL) = index;
     return *(volatile uint32_t *)(io_apic_base + IO_APIC_MMREG_IOWIN);

}

/\* Schreiben eines internen Registers \*/ void io_apic_write(uint8_t index, uint32_t value) {

     *(io_apic_base + IO_APIC_MMREG_IOREGSEL) = index;
     *(volatile uint32_t *)(io_apic_base + IO_APIC_MMREG_IOWIN) = value;

} \</c\>

### Setzen der Einträge der *Redirection Table*

Die Einträge der *Redirection Table* werden basierend auf den Informationen, die die [SMP](https://github.com/lowlevel-eu/wiki/wiki/Symmetrisches-Multiprozessorsystem#intel-multiprocessor-specification "Symmetrisches Multiprozessorsystem")- bzw. die [ACPI](https://github.com/lowlevel-eu/wiki/wiki/Advanced-Configuration-and-Power-Interface "ACPI")-Tabellen enthalten, gesetzt.

## Weblinks

- [Intel® 82093AA I/O Advanced Programmable Interrupt Controller (I/O APIC) Datasheet](http://www.intel.com/design/chipsets/datashts/290566.htm)
- [Intel® 82093AA I/O Advanced Programmable Interrupt Controller (I/O APIC) Specification Update](http://www.intel.com/design/chipsets/specupdt/290710.htm)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/11141/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1574/index.html)

<!-- MediaWiki page 1574; revision 11141; parent 11048; 2013-09-08T23:53:32Z -->
