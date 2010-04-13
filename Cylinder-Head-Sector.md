# Cylinder Head Sector

**Cylinder Head Sector** (Zylinder-Kopf-Sektor), oder auch **CHS**, ist eine veraltete Methode zur Adressierung von Blöcken/Sektoren auf Festplatten und Disketten. Mit steigender Größe der Massenspeicher wurde die Handhabung per CHS limitiert, weshalb man heute [LBA](https://github.com/lowlevel-eu/wiki/wiki/Logical-Block-Addressing "Logical Block Addressing") nutzt. Bei einigen Funktionen des [BIOS](https://github.com/lowlevel-eu/wiki/wiki/Basic-Input-Output-System "BIOS") werden die Sektoren allerdings noch nach dem CHS-System adressiert.

Bei der Angabe des Sektors wird immer bei 1 begonnen. Der erste Sektor wird also mit Cylinder=0 Head=0 Sector=1 adressiert.

## Umrechnung von CHS nach LBA

| Abkürzung | Bedeutung |
| ----------- | ---------------------------------- |
| mS | Anzahl der Sektoren pro Zylinder |
| mH | Anzahl der Köpfe |
| S | Sektor |
| H | Kopf |
| C | Zylinder |

    LBA = (C*mH*mS) + (H*mS) + S - 1

Die Anzahl der Zylinder ist dabei nicht entscheidend.

## siehe auch

- [LBA](https://github.com/lowlevel-eu/wiki/wiki/Logical-Block-Addressing "LBA") - die neuere, lineare Adressierung der Sektoren

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/7566/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1440/index.html)

<!-- MediaWiki page 1440; revision 7566; parent 7152; 2010-04-13T16:10:50Z -->
