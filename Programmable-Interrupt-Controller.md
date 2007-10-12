# Programmable Interrupt Controller

Der Programmable Interrupt Controller (PIC) empfängt Unterbrechungsanforderungen (Interrupt Requests, kurz IRQs) von der Hardware und gibt sie an die CPU weiter.

Nach einer gewissen Zeit benötigte man mehr als die 8 IRQ-Kanäle, die von einem PIC zur verfügung gestellt wurden. Deshalb wurde ein zweiter PIC über den IRQ2-Anschluss an den ersten PIC angeschlossen. Man erhielt so 15 IRQ-Kanäle.  
Heutzutage werden keine echten PICs verwendet und es gibt eine verbesserte Variante namens Advanced Programmable Interrupt Controller ([APIC](https://github.com/lowlevel-eu/wiki/wiki/Advanced-Programmable-Interrupt-Controller "APIC")). Aus gründen der Abwährtskompatibilität emulieren jedoch alle PCs die alte variante mit 2 PICs, bis man diese emulation ausschaltet.

Die Verwendung der einzelnen IRQ-Kanäle wurde früher fest vorgegeben, da sie direkt mit der Hardware verdrahtet waren. Die restlichen, freigebliebenen IRQs werden heutzutage dynamisch vergeben. (etwa über PnP)

    IRQ  Hardware/Funktion

    PIC1
     0  PIT (Proganable Interrupt Timer)
     1  KBC (Tastatur)
     2  Verbindung zum PIC2
     3  RS-232 port 2 and 4
     4  RS-232 port 1 and 3
     5  LPT 2
     6  Floppy
     7  LPT 1 / Spurious Interrupt

    PIC2
     8  RTC (CMOS Real Time Clock)
     9
    10
    11
    12  KBC (PSAUX, meist PS/2-Maus)
    13  FPU
    14  Primary ATA/ATAPI   (aka IDE EIDE)
    15  Secondary ATA/ATAPI (aka IDE EIDE) / Spurious Interrupt

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/2169/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1465/index.html)

<!-- MediaWiki page 1465; revision 2169; parent 1949; 2007-10-12T20:21:52Z -->
