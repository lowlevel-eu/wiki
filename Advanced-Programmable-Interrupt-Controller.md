# Advanced Programmable Interrupt Controller

Diese Seite ist ein Artikel, welcher **mehr** haben könnte..  

Wenn du mehr darüber weißt oder recherchieren willst, bist **du** aufgerufen, dies zu tun. Wenn du dir in einer Sache nicht sicher bist, dann stell es auf die Diskussionsseite.

Die **APIC**-Architektur (**A**dvanced **P**rogrammable **I**nterrupt **C**ontroller) sorgt für die Verteilung der [Interrupts](https://github.com/lowlevel-eu/wiki/wiki/Interrupt "Interrupt") auf [x86](https://github.com/lowlevel-eu/wiki/wiki/X86 "X86")-Systemen und besteht aus mehreren separaten Controllern:

- eine oder mehrere [I/O APICs](https://github.com/lowlevel-eu/wiki/wiki/I-O-Advanced-Programmable-Interrupt-Controller "I/O APIC")
- eine [Local APIC](https://github.com/lowlevel-eu/wiki/wiki/Local-Advanced-Programmable-Interrupt-Controller "Local APIC") pro Prozessor

## Aufbau

Der schematische Aufbau kann aus folgendem Bild entnommen werden:

  

[<img src="https://raw.githubusercontent.com/wiki/lowlevel-eu/wiki/assets/6bd762e3a5c69e74b59a.png" width="412" height="293" alt="APIC.png" />](https://raw.githubusercontent.com/wiki/lowlevel-eu/wiki/assets/6bd762e3a5c69e74b59a.png)

  
Die I/O APIC ist mit der Hardware verbunden und nimmt von ihr Interrupts entgegen. Diese verteilt die I/O APIC dann anhand ihrer *Redirection Table* an die Local APICs, welche pro Prozessor jeweils ein Mal vorhanden sind. Diese signalisieren dem Prozessor dann den jeweiligen Interrupt.

Aufgrund von Abwärtskompatibilität ist außerdem natürlich noch der [Programmable Interrupt Controller](https://github.com/lowlevel-eu/wiki/wiki/Programmable-Interrupt-Controller "Programmable Interrupt Controller") weiterhin vorhanden der verschieden mit den auf den Bild sichtbaren Komponenten verbunden sein kann.

## Weblinks

- [www.osdev.org: Enable local-apic interrupts?](http://www.osdev.org/phpBB2/viewtopic.php?t=14808&postdays=0&postorder=asc)
- [Advanced Programmable Interrupt Controller (Tutorial von Mike Rieker)](http://osdev.berlios.de/pic.html)
- [Wikipedia-Artikel](http://de.wikipedia.org/wiki/Advanced_Programmable_Interrupt_Controller)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/9430/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1584/index.html)

<!-- MediaWiki page 1584; revision 9430; parent 7144; 2011-02-05T12:29:28Z -->
