# Interrupt

Ein Interrupt ist eine Unterbrechung der CPU. Er kann durch eine [Exception](https://github.com/lowlevel-eu/wiki/wiki/Exception "Exception"), einen [IRQ](https://github.com/lowlevel-eu/wiki/wiki/Programmable-Interrupt-Controller#irq-tabelle "IRQ") oder einen Software-Interrupt ausgelöst werden. Software-Interrupts werden mit der Instruktion *int \<n\>* ausgelöst.

Wenn ein Interrupt ausgelöst wird, werden *eip*,*cs* und *eip* auf dem Stack gesichert.

![int_stack.png](http://wonsheimlan.wo.funpic.de/int_stack.png)

Aus einem Interrupt wird zurückgekehrt mit der Instruktion *iret*

## Siehe auch

- [Programmable Interrupt Controller](https://github.com/lowlevel-eu/wiki/wiki/Programmable-Interrupt-Controller "Programmable Interrupt Controller")
- [Interrupt Vector Table](https://github.com/lowlevel-eu/wiki/wiki/Interrupt-Vector-Table "Interrupt Vector Table")
- [Interprocessor Interrupt](https://github.com/lowlevel-eu/wiki/wiki/Interprocessor-Interrupt "Interprocessor Interrupt")
- [Non Maskable Interrupt](https://github.com/lowlevel-eu/wiki/wiki/Non-Maskable-Interrupt "Non Maskable Interrupt")

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/2412/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1596/index.html)

<!-- MediaWiki page 1596; revision 2412; parent 0; 2007-12-16T11:49:41Z -->
