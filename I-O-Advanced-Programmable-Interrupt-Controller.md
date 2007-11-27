# I/O Advanced Programmable Interrupt Controller

Die I/O APIC (= Advanced Programmable Interrupt Controller) löst den [Programmable Interrupt Controller](https://github.com/lowlevel-eu/wiki/wiki/Programmable-Interrupt-Controller "PIC") in einem [SMP](https://github.com/lowlevel-eu/wiki/wiki/Symmetrisches-Multiprozessorsystem "SMP")- bzw. [NUMA](https://github.com/lowlevel-eu/wiki/wiki/Non-Uniform-Memory-Architecture "NUMA")-System ab. Da der PIC die [IRQs](https://github.com/lowlevel-eu/wiki/wiki/Programmable-Interrupt-Controller#irq-tabelle "IRQ") ausschließlich an den BSP (= Bootstrap Processor) senden kann, ist in einem System mit mehreren Prozessoren eine I/O APIC notwendig. Darüber hinaus stellt die I/O APIC statt nur 16 IRQ-Leitungen wie der PIC normalerweise 24 IRQ-Leitungen zur Verfügung. Dies minimiert das IRQ-Sharing in Systemen mit sehr vielen Geräten.

## Weblinks

- [Intel® 82093AA I/O Advanced Programmable Interrupt Controller (I/O APIC) Datasheet](http://www.intel.com/design/chipsets/datashts/290566.htm)
- [Intel® 82093AA I/O Advanced Programmable Interrupt Controller (I/O APIC) Specification Update](http://www.intel.com/design/chipsets/specupdt/290710.htm)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/2304/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1574/index.html)

<!-- MediaWiki page 1574; revision 2304; parent 2293; 2007-11-27T17:01:51Z -->
