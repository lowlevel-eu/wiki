# Cylinder Head Sector

Cylinder Head Sector (Zylinder Köpf Sektor) kurz CHS genannte ist eine alte Adressierungsmethode für Massenspeichern wie Festplatten und Disketten. Das Gegenstück dazu ist die lineare Adressierung namens LBA.

Bei der Angabe des Sektors wird immer bei 1 begonnen. Der erste Sektor wird also mit Cylinder=0 Header=0 Sector=1 adressiert.

Umrechnung von CHS nach LBA:

       S  = Sektor
       H  = Kopf
       C  = Zylinder
       
       mS = maximale Anzahl Sektoren (auf einem Zylinder)
       mH = maximale Anzahl Köpfe
       
       
       LBA = (C*mH*mS) + (H*mS) + S - 1

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/1558/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1440/index.html)

<!-- MediaWiki page 1440; revision 1558; parent 1557; 2006-11-25T16:41:37Z -->
