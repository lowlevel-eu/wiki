# Programmable Interrupt Controller

Der **Programmable Interrupt Controller** (**PIC**) empfängt Unterbrechungsanforderungen (Interrupt Requests, kurz IRQs) von Hardwarekomponenten und gibt sie an die CPU weiter. In den ersten PCs gab es ursprünglich nur einen PIC mit 8 IRQ-Kanälen. Da diese nicht genügten, wurde ein zweiter PIC hinzugefügt. Dieser ist an den zweiten IRQ-Anschluss des ersten PIC angeschlossen. Man erhält so 15 IRQ-Kanäle. Die Verwendung der einzelnen IRQ-Kanäle wurde früher fest vorgegeben, da sie direkt mit der Hardware verdrahtet waren. Die restlichen, frei gebliebenen IRQs werden heutzutage dynamisch vergeben z.B. über PnP.

## IRQ Tabelle

  

| IRQ ¹ | IVT ² | Hardware/Funktion |
| ------- | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0 | 0x08 | [Programmable Interval Timer](https://github.com/lowlevel-eu/wiki/wiki/Programmable-Interval-Timer "Programmable Interval Timer") |
| 1 | 0x09 | Erster PS/2 Port des [Keyboard Controller](https://github.com/lowlevel-eu/wiki/wiki/Keyboard-Controller "Keyboard Controller") (meist PS/2 Tastatur) |
| 2 | 0x0A | Verbindung zum zweiten PIC |
| 3 | 0x0B | [RS-232](https://github.com/lowlevel-eu/wiki/wiki/Serielle-Schnittstelle "Serielle Schnittstelle") Port 2/4 |
| 4 | 0x0C | [RS-232](https://github.com/lowlevel-eu/wiki/wiki/Serielle-Schnittstelle "Serielle Schnittstelle") Port 1/3 |
| 5 | 0x0D | LPT 2 |
| 6 | 0x0E | [Floppy Disk Controller](https://github.com/lowlevel-eu/wiki/wiki/Floppy-Disk-Controller "Floppy Disk Controller") |
| 7 | 0x0F | LPT 1 und [Spurious Interrupt](https://github.com/lowlevel-eu/wiki/wiki/Programmable-Interrupt-Controller#spurious-interrupt "PIC") |
| 8 | 0x70 | RTC ([CMOS](https://github.com/lowlevel-eu/wiki/wiki/CMOS "CMOS") Real Time Clock) |
| 9 | 0x71 | frei |
| 10 | 0x72 | frei |
| 11 | 0x73 | frei |
| 12 | 0x74 | Zweiter PS/2 Port des [Keyboard Controller](https://github.com/lowlevel-eu/wiki/wiki/Keyboard-Controller "Keyboard Controller") (meist PS/2 Maus) |
| 13 | 0x75 | FPU |
| 14 | 0x76 | primärer [ATA/ATAPI/(E)IDE](https://github.com/lowlevel-eu/wiki/wiki/AT-Attachment "ATA") |
| 15 | 0x77 | sekundärer [ATA/ATAPI/(E)IDE](https://github.com/lowlevel-eu/wiki/wiki/AT-Attachment "ATA") und [Spurious Interrupt](https://github.com/lowlevel-eu/wiki/wiki/Programmable-Interrupt-Controller#spurious-interrupt "PIC") |

  
¹ IRQ ist die eigentliche IRQ-Nummer. IRQ0-IRQ7 gehören zur ersten PIC, IRQ8-IRQ15 zur zweiten.  
² IVT ist die Standard Interrupt Nummer auf der [Interrupt Vector Table](https://github.com/lowlevel-eu/wiki/wiki/Interrupt-Vector-Table "Interrupt Vector Table") des real mode nach dem booten.

## Spurious Interrupt

Ein Spurious Interrupt wird ausgelöst, wenn der PIC irrtümlicherweise einen Interrupt an die CPU meldet und erst danach bemerkt, dass er eigentlich gar kein Interrupt auslösen hätte dürfen. Darum ruft die CPU den Spurious Interrupt auf, welcher sich je nach Konfiguration am letzten Eingang des Master oder Slave PIC befindet. Um ihn von den "normalen" Interrupts (LPT oder ATA) zu unterscheiden kann man im ISR Register des jeweiligen PICs schauen, ob dieser gerade einen "normalen" Interrupt bearbeitet oder eben nicht. Ein Spurious Interrupt kann einfach mit einem iret beendet werden ohne dass anderer Code nötig ist. Bemerkenswert ist, dass ein Spurious Interrupt selbst dann auftreten kann, wenn alle IRQ-Kanäle in der PIC maskiert wurden.

## siehe auch

- [Ausgabe 2](https://github.com/lowlevel-eu/wiki/wiki/Ausgabe-2#lowlevel-grundlagen-teil-2 "Ausgabe 2")
- [APIC](https://github.com/lowlevel-eu/wiki/wiki/Advanced-Programmable-Interrupt-Controller "APIC")

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/2528/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1465/index.html)

<!-- MediaWiki page 1465; revision 2528; parent 2527; 2008-01-02T02:59:02Z -->
