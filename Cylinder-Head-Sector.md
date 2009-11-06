# Cylinder Head Sector

**Cylinder Head Sector** (Zylinder-Kopf-Sektor), oder auch **CHS**, ist eine veraltete Methode zur Adressierung von Blöcken/Sektoren auf Festplatten und Disketten. Mit steigender Größe der Massenspeicher wurde die Handhabung per CHS limitiert, weshalb man heute [LBA](https://github.com/lowlevel-eu/wiki/wiki/Logical-Block-Addressing "Logical Block Addressing") nutzt.

Bei der Angabe des Sektors wird immer bei 1 begonnen. Der erste Sektor wird also mit Cylinder=0 Header=0 Sector=1 adressiert.

Umrechnung von CHS nach LBA:

| Abkürzung | Bedeutung |
| ----------- | ---------------------------------- |
| mS | Anzahl der Sektoren pro Zylinder |
| mH | Anzahl der Köpfe |
| S | Sektor |
| H | Kopf |
| C | Zylinder |

` LBA = (C*mH*mS) + (H*mS) + S - 1 `

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/6191/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1440/index.html)

<!-- MediaWiki page 1440; revision 6191; parent 5566; 2009-11-06T19:54:03Z -->
