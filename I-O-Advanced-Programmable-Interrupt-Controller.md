# I/O Advanced Programmable Interrupt Controller

Die **I/O APIC** (= **I/O Advanced Programmable Interrupt Controller**) löst den [Programmable Interrupt Controller](https://github.com/lowlevel-eu/wiki/wiki/Programmable-Interrupt-Controller "PIC") in einem [SMP](https://github.com/lowlevel-eu/wiki/wiki/Symmetrisches-Multiprozessorsystem "SMP")- bzw. [NUMA](https://github.com/lowlevel-eu/wiki/wiki/Non-Uniform-Memory-Architecture "NUMA")-System ab. Da der PIC die [IRQs](https://github.com/lowlevel-eu/wiki/wiki/Programmable-Interrupt-Controller#irq-tabelle "IRQ") ausschließlich an den BSP (= Bootstrap Processor) senden kann, ist in einem System mit mehreren Prozessoren eine I/O APIC notwendig. Darüber hinaus stellt die I/O APIC statt nur 16 IRQ-Leitungen wie der PIC normalerweise 24 IRQ-Leitungen zur Verfügung. Dies minimiert das IRQ-Sharing in Systemen mit sehr vielen Geräten. Außerdem ist die Programmierung der I/O APIC schneller, da sie nicht über I/O Ports, sondern über Speicherbereiche abläuft.

## Programmierung

Die I/O APIC besitzt ein Indexregister (*I/O Register Select* bzw. *IOREGSEL*) und ein Datenregister (*I/O Window* bzw. *IOWIN*). Das Indexregister befindet sich an Offset 0x00 und das Datenregister an Offset 0x10 im Speicherbereich des I/O APIC, der bei 0xfec00xy00¹ beginnt. Beide sind les- und schreibbar. Mit dem Indexregister wählt man ein internes Register der I/O APIC aus und kann dann über das Datenregister das interne Register auslesen bzw. beschreiben.

¹x und y werden mit dem APICBASE Register im PIIX3 festgelegt.

## Weblinks

- [Intel® 82093AA I/O Advanced Programmable Interrupt Controller (I/O APIC) Datasheet](http://www.intel.com/design/chipsets/datashts/290566.htm)
- [Intel® 82093AA I/O Advanced Programmable Interrupt Controller (I/O APIC) Specification Update](http://www.intel.com/design/chipsets/specupdt/290710.htm)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/2992/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1574/index.html)

<!-- MediaWiki page 1574; revision 2992; parent 2531; 2008-06-23T13:19:45Z -->
