# Programmable Interrupt Controller

Der Programmable Interrupt Controller (**PIC**) empfängt Unterbrechungsanforderungen (Interrupt Requests, kurz IRQs) von Hardwarekomponenten und gibt sie an die CPU weiter. In den ersten PCs gab es ursprünglich nur einen PIC mit 8 IRQ-Kanälen. Da diese nicht genügten, wurde ein zweiter PIC hinzugefügt. Dieser ist an den zweiten IRQ-Anschluss des ersten PIC angeschlossen. Man erhält so 15 IRQ-Kanäle. Die Verwendung der einzelnen IRQ-Kanäle wurde früher fest vorgegeben, da sie direkt mit der Hardware verdrahtet waren. Die restlichen, frei gebliebenen IRQs werden heutzutage dynamisch vergeben z.B. über [ISA PnP](https://github.com/lowlevel-eu/wiki/wiki/Industry-Standard-Architecture "ISA") oder [PCI](https://github.com/lowlevel-eu/wiki/wiki/Peripheral-Component-Interconnect "PCI").

  

## Programmierung

Jeder der beiden PICs hat jeweils zwei IO-Ports, über die er programmiert wird: Einen Befehlsport (0x20 für den Master und 0xA0 für den Slave) und einen Datenport (0x21 bzw. 0xA1).

### Initialisierung

Nach dem Booten beginnen die IRQs 0 bis 7 standardmäßig beim Interrupt 0x08 (und die IRQs 8 bis 15 bei Interrupt 0x70). An dieser Stelle liegen sie aber denkbar ungünstig, weil dieselben Interruptnummern bereits von der CPU für [Exceptions](https://github.com/lowlevel-eu/wiki/wiki/Exception "Exception") verwendet werden. Beim Start des Kernels müssen daher die IRQs auf andere Interruptnummern gelegt werden.

Zunächst muss ein Befehl gesendet werden, dass der PIC sich resetten soll und die nächsten gesendeten Datenbytes als Parameter für die Initialisierung gedacht sind. Anschließend werden bis zu drei Bytes nacheinander auf den Datenport geschrieben. Insgesamt werden folgende Operationen durchgeführt (die einzelnen gesendeten Bytes werden als ICWx durchnummeriert; ICW steht für *Initialization Control Word*):

| Port | Name | Erklärung |  |
| -------- | ------ | ---------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| Befehl | ICW1 | Einleitung der Initialisierung |  |
| Befehl | ICW1 | 0x01 | Gesetzt, wenn anschließend ICW4 gesendet wird |
| Befehl | ICW1 | 0x02 | Single Mode, es gibt keinen Slave. Wenn dieses Bit gesetzt ist, entfällt ICW3 |
| Befehl | ICW1 | 0x10 | Initialisierung einleiten (eigentliches Befehlsbit) |
| Daten | ICW2 | Interruptnummer für IRQ 0 (Vielfaches von 8) |  |
| Daten | ICW3 | Master: IRQs, auf denen Slaves gemappt sind (Bitmaske, normal 0x04)<br>Slave: IRQ, über den der Slave am Master angeschlossen ist (normal 2) |  |
| Daten | ICW4 | Flags<br> |  |
| Daten | ICW4 | 0x01 | Für PCs gesetzt |
| Daten | ICW4 | 0x02 | Automatisches EOI |

### Maskieren von Interrupts

Der PIC bietet außerdem noch die Möglichkeit, bestimmte IRQs zu maskieren, d.h. für diese IRQs keine Interrupts auszulösen, solange sie maskiert sind. Wenn auf den Datenport geschrieben wird, ohne dass vorher ein Befehl gesendet wurde, der auf dem Datenport Parameter erwartet, wird dieser Wert als IRQ-Maske benutzt.

In diesem Wert steht jedes Bit für einen Interrupt (IRQ 0 ist Bit 0 usw.). Gesetztes Bit bedeutet, dass der Interrupt maskiert ist (d.h. nicht an die CPU weitergeleitet wird); gelöschtes Bit bedeutet, dass der Interrupt aktiv ist.

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
| 10 | 0x72 | vierter [ATA/ATAPI/(E)IDE](https://github.com/lowlevel-eu/wiki/wiki/AT-Attachment "ATA") |
| 11 | 0x73 | dritter [ATA/ATAPI/(E)IDE](https://github.com/lowlevel-eu/wiki/wiki/AT-Attachment "ATA") |
| 12 | 0x74 | Zweiter PS/2 Port des [Keyboard Controller](https://github.com/lowlevel-eu/wiki/wiki/Keyboard-Controller "Keyboard Controller") (meist PS/2 Maus) |
| 13 | 0x75 | FPU |
| 14 | 0x76 | primärer [ATA/ATAPI/(E)IDE](https://github.com/lowlevel-eu/wiki/wiki/AT-Attachment "ATA") |
| 15 | 0x77 | sekundärer [ATA/ATAPI/(E)IDE](https://github.com/lowlevel-eu/wiki/wiki/AT-Attachment "ATA") und [Spurious Interrupt](https://github.com/lowlevel-eu/wiki/wiki/Programmable-Interrupt-Controller#spurious-interrupt "PIC") |

¹ IRQ ist die eigentliche IRQ-Nummer. IRQ0-IRQ7 gehören zum ersten PIC, IRQ8-IRQ15 zum zweiten.  
² IVT ist die Standard Interrupt Nummer auf der [Interrupt Vector Table](https://github.com/lowlevel-eu/wiki/wiki/Interrupt-Vector-Table "Interrupt Vector Table") des [Real Mode](https://github.com/lowlevel-eu/wiki/wiki/Real-Mode "Real Mode") nach dem Booten.

## Spurious Interrupt

Ein Spurious Interrupt wird ausgelöst, wenn der PIC irrtümlicherweise einen Interrupt an die CPU meldet und erst danach bemerkt, dass er eigentlich gar kein Interrupt auslösen hätte dürfen. Darum ruft die CPU den Spurious Interrupt auf, welcher sich je nach Konfiguration am letzten Eingang des Master oder Slave PIC befindet. Um ihn von den "normalen" Interrupts (LPT oder ATA) zu unterscheiden kann man im ISR Register des jeweiligen PICs schauen, ob dieser gerade einen "normalen" Interrupt bearbeitet oder eben nicht. Ein Spurious Interrupt kann einfach mit einem iret beendet werden ohne dass anderer Code nötig ist. Bemerkenswert ist, dass ein Spurious Interrupt selbst dann auftreten kann, wenn alle IRQ-Kanäle in der PIC maskiert wurden.

## siehe auch

- [PIC Tutorial](https://github.com/lowlevel-eu/wiki/wiki/PIC-Tutorial "PIC Tutorial")
- [Ausgabe 2](https://github.com/lowlevel-eu/wiki/wiki/Ausgabe-2#lowlevel-grundlagen-teil-2 "Ausgabe 2")
- [APIC](https://github.com/lowlevel-eu/wiki/wiki/Advanced-Programmable-Interrupt-Controller "APIC")

## Links

- [Hardware-Spezifikation (Intel)](http://pdos.csail.mit.edu/6.828/2005/readings/hardware/8259A.pdf)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/9551/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1465/index.html)

<!-- MediaWiki page 1465; revision 9551; parent 7071; 2011-02-14T22:06:36Z -->
