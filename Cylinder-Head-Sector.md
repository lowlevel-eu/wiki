# Cylinder Head Sector

Cylinder Head Sector (Zylinder Köpf Sektor) kurz CHS genannte ist eine alte Adressierungsmethode für Massenspeichern wie Festplatten und Disketten. Das Gegenstück dazu ist die lineare Adressierung namens LBA.

Der erste Sektor in CHS wird mit "Cylinder=0 Head=0 Sector=1" adressiert. NICHT mit "Cylinder=0 Head=0 Sector=0"!

Umrechnung von CHS nach LBA: (aus Wikipedia)

       LBA = ((CYL × HPC + HEAD) × SPT) + SECT − 1

       * CYL : Zylinder
       * HPC : Leseköpfe/Zylinder
       * HEAD : Lesekopfnummer
       * SPT : Sektoren/Track (Track ^= Zylinder)
       * SECT : Sektornummer
       * CL : Cluster

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/1556/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1440/index.html)

<!-- MediaWiki page 1440; revision 1556; parent 1554; 2006-11-25T16:00:54Z -->
