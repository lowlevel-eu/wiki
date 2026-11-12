# Cylinder Head Sector

**Cylinder Head Sector** (Zylinder-Kopf-Sektor), oder auch **CHS**, ist eine veraltete Methode zur Adressierung von Blöcken/Sektoren auf Festplatten und Disketten. Mit steigender Größe der Massenspeicher wurde die Handhabung per CHS limitiert, weshalb man heute [LBA](Logical-Block-Addressing.md "Logical Block Addressing") nutzt. Bei einigen Funktionen des [BIOS](Basic-Input-Output-System.md "BIOS") werden die Sektoren allerdings noch nach dem CHS-System adressiert.

## Zählweise

Wie nach dem CHS-System die Sektoren gezählt werden, soll hier anhand einer 3,5" Diskette (18 Sektoren pro Zylinder, 2 Seiten) erläutert werden: Zu beachten ist, dass bei der Angabe des Sektors immer bei 1 begonnen wird, während die Zylinder- und Kopfangaben bei 0 anfangen. Der erste Sektor liegt also auf der Unterseite (Head 0), auf dem innersten Zylinder (Cylinder 0) und ist auf diesem Zylinder der erste Sektor (Sector 1). Der nächste Sektor liegt auf demselben Zylinder, entsprechend einen Sektor weiter (C=0, H=0, S=2). So werden die Sektoren weiter gezählt bis "der Zylinder voll ist". Dies ist beim 18. Sektor der Fall (C=0, H=0 und S=18). Der nächste Sektor liegt dann auf demselben Zylinder aber auf der **Oberseite**. Für ihn gilt also: C=0, **H=1** und S=1. Auch hier wird wieder weiter gezählt, bis der Zylinder voll ist. Dann geht man zum nächsten Zylinder (weiter außen) und auf die Unterseite. Dieser Sektor ist der 37. Sektor (=18+18+1) und liegt entsprechend bei C=1, H=0, S=1. Wenn man diese Zählweise versteht, kann man auch das LBA System besser verstehen, bei dem von der Sektornummer einfach noch 1 subtrahiert wird:

| Sektornummer | LBA | C | H | S |
| -------------- | ----- | ----- | ----- | ----- |
| 1 | 0 | 0 | 0 | 1 |
| 2 | 1 | 0 | 0 | 2 |
| usw. |  |  |  |  |
| 19 | 18 | 0 | 1 | 1 |
| 20 | 19 | 0 | 1 | 2 |
| usw |  |  |  |  |
| 37 | 36 | 1 | 0 | 1 |
| 38 | 37 | 1 | 0 | 2 |
| usw |  |  |  |  |
| 73 | 72 | 2 | 0 | 1 |
| usw |  |  |  |  |

**Für die Zählung im CHS-System muss man demzufolge nicht die Anzahl der Zylinder wissen!**

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

- [LBA](Logical-Block-Addressing.md "LBA") - die neuere, lineare Adressierung der Sektoren

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/10544/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1440/index.html)

<!-- MediaWiki page 1440; revision 10544; parent 9072; 2012-03-28T14:13:22Z -->
