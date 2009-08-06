# I/O Advanced Programmable Interrupt Controller

Diese Seite ist ein Artikel, welcher **mehr** haben könnte..  

Wenn du mehr darüber weißt oder recherchieren willst, bist **du** aufgerufen, dies zu tun. Wenn du dir in einer Sache nicht sicher bist, dann stell es auf die Diskussionsseite.

Die **I/O APIC** (= **I/O Advanced Programmable Interrupt Controller**) löst den [Programmable Interrupt Controller](https://github.com/lowlevel-eu/wiki/wiki/Programmable-Interrupt-Controller "PIC") in einem [SMP](https://github.com/lowlevel-eu/wiki/wiki/Symmetrisches-Multiprozessorsystem "SMP")- bzw. [NUMA](https://github.com/lowlevel-eu/wiki/wiki/Non-Uniform-Memory-Architecture "NUMA")-System ab. Da der PIC die [IRQs](https://github.com/lowlevel-eu/wiki/wiki/Programmable-Interrupt-Controller#irq-tabelle "IRQ") ausschließlich an den BSP (= Bootstrap Processor) senden kann, ist in einem System mit mehreren Prozessoren eine I/O APIC notwendig. Darüber hinaus stellt die I/O APIC statt nur 16 IRQ-Leitungen wie der PIC normalerweise 24 IRQ-Leitungen zur Verfügung. Dies verringert die Anzahl der von mehreren Geräten gleichzeitig genutzten IRQs in Systemen mit sehr vielen Geräten. Außerdem ist die Programmierung der I/O APIC schneller, da sie nicht über I/O Ports, sondern über Speicherbereiche abläuft.

## Programmierung

Die I/O APIC besitzt ein Indexregister (*I/O Register Select* bzw. *IOREGSEL*) und ein Datenregister (*I/O Window* bzw. *IOWIN*). Das Indexregister befindet sich an Offset 0x00 und das Datenregister an Offset 0x10 im Speicherbereich des I/O APIC, der bei einem PIIX3 Chipsatz bei 0xfec00xy00 (x und y werden mit dem APICBASE Register im PIIX3 festgelegt) beginnt. Im Allgemeinen ist die Basisadresse der I/O APICs über die [Multiprocessor Tabellen](https://github.com/lowlevel-eu/wiki/wiki/Symmetrisches-Multiprozessorsystem#intel-multiprocessor-specification "Symmetrisches Multiprozessorsystem") bzw. die [ACPI-Tabellen](https://github.com/lowlevel-eu/wiki/wiki/Advanced-Configuration-and-Power-Interface "ACPI") auslesbar. Beide sind les- und schreibbar. Mit dem Indexregister wählt man ein internes Register der I/O APIC aus und kann dann über das Datenregister das interne Register auslesen bzw. beschreiben.

## Weblinks

- [Intel® 82093AA I/O Advanced Programmable Interrupt Controller (I/O APIC) Datasheet](http://www.intel.com/design/chipsets/datashts/290566.htm)
- [Intel® 82093AA I/O Advanced Programmable Interrupt Controller (I/O APIC) Specification Update](http://www.intel.com/design/chipsets/specupdt/290710.htm)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/5340/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1574/index.html)

<!-- MediaWiki page 1574; revision 5340; parent 4109; 2009-08-06T16:30:03Z -->
