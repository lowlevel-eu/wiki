# Small Computer System Interface

Diese Seite ist ein Artikel, welcher **mehr** haben könnte..  

Wenn du mehr darüber weißt oder recherchieren willst, bist **du** aufgerufen, dies zu tun. Wenn du dir in einer Sache nicht sicher bist, dann stell es auf die Diskussionsseite.

Das **Small Computer System Inferface**, oder kurz **SCSI** ist ein Schnittstellensystem für Peripheriegeräte. SCSI wurde zuletzt aufgrund der hohen Datenübertragungsrate und der Möglichkeit, mehr als zwei Geräre pro Controller (wie bei [ATA](AT-Attachment "ATA")) anschließen zu können vor allem im Server-Bereich verwendet, dort aber von Serial-Attached SCSI (SAS) verdrängt.

## Geschichtliches

Das SCSI wurde bereits 1979 von Alan Shugart und seiner Firma Shugart Technologies entwickelt und hieß zu dieser Zeit noch SASI (Shugart Associated System Interface). Nachdem die NCR-Corporation ihre Mitarbeite ankündigte wurde das SASI in SCSI umbenannt. Im Jahre 1986 wurde es dann schließlich von dem ANSI (American National Standardization Institute) standardisiert. Seitdem wird es vor allem in der Industrie eingesetzt. Im Server-Bereich, wo SCSI zuletzt verwendet wurde, wurde es ab etwa 2004 durch SAS abgelöst.

## Einsatzzwecke

SCSI wurde überwiegend in Servern genutzt, da hier die Möglichkeit besteht, mehr als zwei Geräte pro Controller anschließen zu können. Auch die hohe Übertragungsrate machte SCSI besonders im Bereich der Server-Festplatten und Ethernet-Verbindungen schnell zum Standard. In heutigen PCs sind auf dem Mainboard keine SCSI-Controller untergebracht, da im Bereich der Desktop-PCs SATA Platzhirsch ist. Dennoch ist es mit Hilfe von Peripheriekarten möglich, SCSI-Controller hinzuzufügen.

Die SCSI Kommandos leben in iSCSI (SCSI über IP also Netzwerk) weiter, außerdem benutzt der Linux-Kernel den SCSI Stack auch für USB-Massenspeicher, SATA und co - was eine gewisse Ähnlichkeit vermuten lässt.

Über SCSI war auch die Anbindung von Scannern üblich.

## Weblinks

- [SCSI-Website](http://www.t10.org/)
- [Exemplarischer Treiber von Adaptec für Linux 2.4](http://www.adaptec.com/de-DE/speed/scsi/linux/aic7Yxx-2_0_15-6_3_11-linux-2_4_tgz.htm)
- [SCSI-Device-Driver HOWTO](http://tldp.org/LDP/khg/HyperNews/get/devices/scsi.html) (**Warnung: Von 1993**)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/11479/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2102/index.html)

<!-- MediaWiki page 2102; revision 11479; parent 7877; 2020-08-02T23:51:47Z -->
