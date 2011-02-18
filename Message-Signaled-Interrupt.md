# Message Signaled Interrupt

Diese Seite ist ein Artikel, welcher **mehr** haben könnte..  

Wenn du mehr darüber weißt oder recherchieren willst, bist **du** aufgerufen, dies zu tun. Wenn du dir in einer Sache nicht sicher bist, dann stell es auf die Diskussionsseite.

Mit einem **M**essage-**S**ignaled-**I**nterrupt kann ein Hardware-Gerät dem System einen Interrupt melden ohne dafür eine spezielle Leitung zu benötigen, der Interrupt wird als Nachricht über den normalen Bus zum Interrupt-Controller geschickt. Neben der Ersparnis von Leitungen hat das vor allem den Vorteil das mehr verschiedene Interrupts möglich sind weil so eine Nachricht einen Interrupt-Vector mit mehreren Bits aufnehmen kann.

Das einzigste aktuelle Bussystem das Message-Signaled-Interrupts bietet ist [PCI](https://github.com/lowlevel-eu/wiki/wiki/Peripheral-Component-Interconnect "PCI") und seine Verwandten bzw. Nachfolger. Auf dem PC sind Message-Signaled-Interrupts nur nutzbar wenn man die [I/O APICs](https://github.com/lowlevel-eu/wiki/wiki/I-O-Advanced-Programmable-Interrupt-Controller "I/O APIC") benutzt.

## Message-Signaled-Interrupts bei PCI

Bei PCI müssen für die Benutzung von Message-Signaled-Interrupts eigentlich nur das Gerät und der I/O-APIC dazu passend konfiguriert werden, alle anderen Komponenten (inklusive eventueller Bridges u.ä.) müssen keine speziellen Voraussetzungen erfüllen. Die Message-Signaled-Interrupts werden als ganz normale Speicher-Schreib-Zugriffe an eine bestimmte Adresse geschickt. Diese Adresse muss beim PC ein I/O-APIC zur Verfügung stellen. Bei Message-Signaled-Interrupts kann jede PCI-Funktion mehrere unabhängige Interrupts haben und es ist kein Interrupt-Sharing erforderlich. Bei PCI gibt es Message-Signaled-Interrupts in 2 verschiedenen Geschmacksrichtungen, einmal als einfaches MSI und einmal als erweitertes MSI-X. Das einfache MSI unterstützt bis zu 32 Interrupts pro PCI-Funktion und die gehen alle an den selben Interrupt-Controller, das mächtigere MSI-X unterstützt bis zu 2048 Interrupts die alle an unterschiedliche Interrupt-Controller gehen können.

## Weblinks

- [Erklärung der PCI-Capabilitys für MSI und MSI-X von der PCI-SIG](http://www.pcisig.com/specifications/conventional/msi-x_ecn.pdf)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/9563/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2400/index.html)

<!-- MediaWiki page 2400; revision 9563; parent 0; 2011-02-18T19:33:40Z -->
