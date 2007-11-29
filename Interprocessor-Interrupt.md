# Interprocessor Interrupt

Ein **IPI** (= **Interprocessor Interrupt**) ist ein [Interrupt](https://github.com/lowlevel-eu/wiki/wiki/Interrupt "Interrupt"), welcher von einem Prozessor (bzw. der [LAPIC](https://github.com/lowlevel-eu/wiki/wiki/Local-Advanced-Programmable-Interrupt-Controller "LAPIC") dieses Prozessors) an einen anderen/den gleichen Prozessor (bzw. die [LAPIC](https://github.com/lowlevel-eu/wiki/wiki/Local-Advanced-Programmable-Interrupt-Controller "LAPIC") dieses Prozessors) gesendet wird. Diese Interrupts werden in [SMP](https://github.com/lowlevel-eu/wiki/wiki/Symmetrisches-Multiprozessorsystem "SMP")- und [NUMA](https://github.com/lowlevel-eu/wiki/wiki/Non-Uniform-Memory-Architecture "NUMA")-Systemen dazu verwendet bestimmte Aktionen zwischen mehreren Prozessoren zu synchronisieren.

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/2331/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1582/index.html)

<!-- MediaWiki page 1582; revision 2331; parent 2330; 2007-11-29T17:14:26Z -->
