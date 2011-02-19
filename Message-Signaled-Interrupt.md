# Message Signaled Interrupt

Diese Seite ist ein Artikel, welcher **mehr** haben könnte..  

Wenn du mehr darüber weißt oder recherchieren willst, bist **du** aufgerufen, dies zu tun. Wenn du dir in einer Sache nicht sicher bist, dann stell es auf die Diskussionsseite.

Mit einem **M**essage-**S**ignaled-**I**nterrupt kann ein Hardware-Gerät dem System einen Interrupt melden ohne dafür eine spezielle Leitung zu benötigen, der Interrupt wird als Nachricht über den normalen Bus zum Interrupt-Controller geschickt. Neben der Ersparnis von Leitungen hat das vor allem den Vorteil das mehr verschiedene Interrupts möglich sind weil so eine Nachricht einen Interrupt-Vector mit mehreren Bits aufnehmen kann.

Das einzigste aktuelle Bussystem das Message-Signaled-Interrupts bietet ist [PCI](https://github.com/lowlevel-eu/wiki/wiki/Peripheral-Component-Interconnect "PCI") und seine Verwandten bzw. Nachfolger. Auf dem PC sind Message-Signaled-Interrupts nur nutzbar wenn man die [I/O APICs](https://github.com/lowlevel-eu/wiki/wiki/I-O-Advanced-Programmable-Interrupt-Controller "I/O APIC") benutzt.

## Message Signaled Interrupts bei PCI

Bei PCI müssen für die Benutzung von Message Signaled Interrupts eigentlich nur das Gerät und der I/O-APIC dazu passend konfiguriert werden, alle anderen Komponenten (inklusive eventueller Bridges u.ä.) müssen keine speziellen Voraussetzungen erfüllen. Die Message Signaled Interrupts werden als ganz normale Speicher Schreib Zugriffe an eine bestimmte Adresse geschickt. Diese Adresse muss beim PC ein I/O-APIC zur Verfügung stellen. Bei Message Signaled Interrupts kann jede PCI-Funktion mehrere unabhängige Interrupts haben und es ist kein Interrupt-Sharing erforderlich. Bei PCI gibt es Message Signaled Interrupts in 2 verschiedenen Geschmacksrichtungen, einmal als einfaches MSI und einmal als erweitertes MSI-X. Das einfache MSI unterstützt bis zu 32 Interrupts pro PCI-Funktion und die gehen alle an den selben Interrupt-Controller, das verbesserte MSI-X unterstützt bis zu 2048 Interrupts pro PCI-Funktion die alle an unterschiedliche Interrupt-Controller gehen können.

Einen speziellen Vorteil bieten die Message Signaled Interrupts bei PCI im Zusammenhang mit busmasterfähigen Geräten: bei den klassischen INTx-Signalen kann es sein das dieses eher bei der CPU eintrifft als die letzten Daten die das Gerät in den Hauptspeicher geschrieben hat. Es ist also möglich das ein Gerät die letzten Daten in Richtung Hauptspeicher abschickt und unmittelbar danach das INTx-Signal generiert (weil aus Sicht des Gerätes der aktuelle Vorgang erledigt ist und nun der Treiber diese Daten verarbeiten soll) und während die Daten noch in den Puffern irgendwelcher Bridges darauf warten irgendwann den Hauptspeicher zu erreichen kann das INTx-Signal schon längst beim Interrupt-Controller angekommen sein und dieser könnte bereits die CPU unterbrochen haben so das der Interrupt-Handler vom Treiber die erwarteten Daten noch gar nicht im Hauptspeicher vorfindet. Da für die Message Signaled Interrupts ganz normale Speicher-Schreibzugriffe benutzt werden und diese sich auf ihrem Weg nicht gegenseitig überholen dürfen ist es quasi immer gewährleistet das der Interrupt (als Message) erst dann den Chipsatz erreicht wenn auch die letzten zugehörigen Daten den Chipsatz passiert haben. Um diesem Problem bei den klassischen Interrupts vorzubeugen wird empfohlen einfach ein noncacheable Register des entsprechenden Gerätes zu lesen, auch wenn der Treiber eigentlich genau weiß was im Interrupt zu tun ist, da dieser Zugriff auch den gesamten Weg von der CPU bis zum Gerät und wieder zurück nehmen muss und so sichergestellt ist das eben keine Daten mehr irgendwo auf dem Weg noch in Puffern feststecken. Dieses Problem lässt sich nicht debuggen, da es ja ein Hardware-Timing-Problem ist und tritt auch bei den üblichen Emulatoren und Virtualisierern gar nicht auf.

## Weblinks

- [Erklärung der PCI-Capabilities für MSI und MSI-X von der PCI-SIG](http://www.pcisig.com/specifications/conventional/msi-x_ecn.pdf)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/9575/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2400/index.html)

<!-- MediaWiki page 2400; revision 9575; parent 9574; 2011-02-19T17:58:21Z -->
