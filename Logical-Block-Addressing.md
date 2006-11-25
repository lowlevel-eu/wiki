# Logical Block Addressing

Bei Logical Block Addressing (Logische Block Adressierung) werden Sektoren von Massenspeichern von 0 aufsteigend adressiert. Das Gegenstück zu LBA ist das ältere [CHS](https://github.com/lowlevel-eu/wiki/wiki/Cylinder-Head-Sector "Cylinder Head Sector").

Umrechnung von LBA zu CHS:

       Abkürung Bedeutung
       
       mS       maximale Anzahl Sektoren (auf einem Zylinder)
       mH       maximale Anzahl Köpfe
       
       S        Sektor
       H        Kopf
       C        Zylinder

       C =   LBA  /  (mH*mS)
       H =  (LBA mod (mH*mS))  /  mS
       S = ((LBA mod (mH*mS)) mod mS) + 1

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/1561/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1442/index.html)

<!-- MediaWiki page 1442; revision 1561; parent 1559; 2006-11-25T16:54:29Z -->
