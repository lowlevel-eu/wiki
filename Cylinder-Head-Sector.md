# Cylinder Head Sector

Cylinder Head Sector (Zylinder Kopf Sektor) kurz CHS genannte ist eine alte Adressierungsmethode für Massenspeichern wie Festplatten und Disketten. Das Gegenstück dazu ist die lineare Adressierung namens [LBA](https://github.com/lowlevel-eu/wiki/wiki/Logical-Block-Addressing "Logical Block Addressing").

Bei der Angabe des Sektors wird immer bei 1 begonnen. Der erste Sektor wird also mit Cylinder=0 Header=0 Sector=1 adressiert.

Umrechnung von CHS nach LBA:

       Abkürung Bedeutung
       
       mS       maximale Anzahl Sektoren (auf einem Zylinder)
       mH       maximale Anzahl Köpfe
       
       S        Sektor
       H        Kopf
       C        Zylinder

       LBA = (C*mH*mS) + (H*mS) + S - 1

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/1676/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1440/index.html)

<!-- MediaWiki page 1440; revision 1676; parent 1594; 2007-01-15T22:46:01Z -->
