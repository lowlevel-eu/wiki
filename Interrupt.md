# Interrupt

Ein Interrupt ist eine Unterbrechung der CPU. Er kann durch eine [Exception](https://github.com/lowlevel-eu/wiki/wiki/Exception "Exception"), einen [IRQ](https://github.com/lowlevel-eu/wiki/wiki/Programmable-Interrupt-Controller#irq-tabelle "IRQ") oder einen Software-Interrupt ausgelöst werden. Software-Interrupts werden mit der Instruktion *int \<n\>* ausgelöst.

Wenn ein Interrupt ausgelöst wird, werden *eip*,*cs* und *eip* auf dem Stack gesichert.

![int_stack.png](http://wonsheimlan.wo.funpic.de/int_stack.png)

Aus einem Interrupt wird zurückgekehrt mit der Instruktion *iret*

Interrupts können mithilfe von *sti* und *cli* eingeschaltet bzw. ausgeschaltet werden. Dabei wird das 9. Bit im Register *eflags* gesetzt bzw. zurückgesetzt.

## Siehe auch

- [Programmable Interrupt Controller](https://github.com/lowlevel-eu/wiki/wiki/Programmable-Interrupt-Controller "Programmable Interrupt Controller")
- [Interrupt Vector Table](https://github.com/lowlevel-eu/wiki/wiki/Interrupt-Vector-Table "Interrupt Vector Table")
- [Interprocessor Interrupt](https://github.com/lowlevel-eu/wiki/wiki/Interprocessor-Interrupt "Interprocessor Interrupt")
- [Non Maskable Interrupt](https://github.com/lowlevel-eu/wiki/wiki/Non-Maskable-Interrupt "Non Maskable Interrupt")
- [Interrupt 13h](https://github.com/lowlevel-eu/wiki/wiki/Interrupt-13h "Interrupt 13h")

## Links

[Liste von BIOS-Interrupts](http://www.cs.cmu.edu/afs/cs/user/ralf/pub/WWW/files.html)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/4243/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1596/index.html)

<!-- MediaWiki page 1596; revision 4243; parent 3055; 2009-04-01T19:23:21Z -->
