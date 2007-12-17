# Programmable Interrupt Controller

Der Programmable Interrupt Controller (PIC) empfängt Unterbrechungsanforderungen (Interrupt Requests, kurz IRQs) von Hardwarekomponenten und gibt sie an die CPU weiter.

In den ersten PCs gab es ursprünglich nur einen PIC mit 8 IRQ-Kanälen. Da diese nicht genügten, wurde ein zweiter PIC hinzugefügt. Dieser ist an den zweiten IRQ-Anschluss des ersten PIC angeschlossen. Man erhält so 15 IRQ-Kanäle.  
Heutzutage werden keine echten PICs verwendet und es gibt eine verbesserte Variante namens Advanced Programmable Interrupt Controller ([APIC](https://github.com/lowlevel-eu/wiki/wiki/Advanced-Programmable-Interrupt-Controller "APIC")). Aus Gründen der Abwärtskompatibilität emulieren jedoch alle PCs die alte Variante mit 2 PICs, bis man diese Emulation ausschaltet.

Die Verwendung der einzelnen IRQ-Kanäle wurde früher fest vorgegeben, da sie direkt mit der Hardware verdrahtet waren. Die restlichen, frei gebliebenen IRQs werden heutzutage dynamisch vergeben. (etwa über PnP)

## IRQ Tabelle

    IRQ ist die eigentliche IRQ-Nummer.
    IVT ist die Standard Interrupt Nummer auf der Interrupt Vector Table des real mode nach dem booten.

    IRQ IVT  Hardware/Funktion

    PIC1
     0  0x08 Programmable Interval Timer
     1  0x09 Erstes PS/2 Port des Keyboard Controller (meist PS/2 Tastatur)
             oder in alten Systemen für anders angeschlossene Tastaturen (z.B. Din5 Stecker)
     2  0x0A Verbindung zum PIC2
     3  0x0B RS-232 port 2 and 4
     4  0x0C RS-232 port 1 and 3
     5  0x0D LPT 2
     6  0x0E Floppy Disk Controller
     7  0x0F LPT 1 / Spurious Interrupt

    PIC2
     8  0x70 RTC (CMOS Real Time Clock)
     9  0x71 
    10  0x72 
    11  0x73 
    12  0x74 frei oder zweites PS/2 Port des Keyboard Controller (meist PS/2-Maus)
    13  0x75 FPU
    14  0x76 Primary ATA/ATAPI   (aka IDE EIDE)
    15  0x77 Secondary ATA/ATAPI (aka IDE EIDE) / Spurious Interrupt

## Spurious Interrupt

Ein Spurious Interrupt wird ausgelöst, wenn der PIC irrtümlicherweise einen Interrupt an die CPU meldet und erst danach bemerkt, dass er eigentlich gar kein Interrupt auslösen hätte dürfen. Darum ruft die CPU den Spurious Interrupt auf, welcher sich je nach Konfiguration am letzten Eingang des Master oder Slave PIC befindet. Um ihn von den "normalen" Interrupts (LPT oder ATA) zu unterscheiden kann man im ISR Register des jeweiligen PICs schauen, ob dieser gerade einen "normalen" Interrupt bearbeitet oder eben nicht. Ein Spurious Interrupt kann einfach mit einem iret beendet werden ohne dass anderer Code nötig ist.

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/2429/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1465/index.html)

<!-- MediaWiki page 1465; revision 2429; parent 2424; 2007-12-17T23:11:19Z -->
