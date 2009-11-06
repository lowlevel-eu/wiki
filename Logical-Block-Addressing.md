# Logical Block Addressing

Bei Logical Block Addressing (Logische Block Adressierung) werden Sektoren von Massenspeichern von 0 aufsteigend adressiert. Das Gegenstück zu LBA ist das ältere [CHS](https://github.com/lowlevel-eu/wiki/wiki/Cylinder-Head-Sector "Cylinder Head Sector").

Umrechnung von LBA zu [CHS](https://github.com/lowlevel-eu/wiki/wiki/Cylinder-Head-Sector "CHS"):

       Abkürung Bedeutung
       
       mS       maximale Anzahl Sektoren (auf einem Zylinder)
       mH       maximale Anzahl Köpfe
       
       S        Sektor
       H        Kopf
       C        Zylinder

       C =   LBA  /  (mH*mS)
       H =  (LBA mod (mH*mS))  /  mS
       S = ((LBA mod (mH*mS)) mod mS) + 1

## Beispiel

Da es im bootsektor auf jedes byte ankommt habe ich mich darum bemüht die Umrechnung möglichst klein zu machen. \<asm\>

in ax steht der Sektornummer

       ; C
       xor  dx, dx     ; dx leeren
       mov  bx, 2*18   ; Anzahl der Heads * Sektoren pro Cluster
       div  bx         ; dx:ax / bx = ax rest dx
       mov  [tmpa], al ; al sichern

       ; H
       mov  ax, dx     ; mit dem Rest der Division wird jetzt weitergearbeitet
       xor  dx, dx     ; dx wieder leeren
       shr  bx, 1      ; 36/2 = 18, also nur die Anzahl der Sektoren pro Cluster
       div  bx         ; dx:ax / bx = ax rest dx
       mov  [tmpb], al ; al sichern

       ;S
       inc  dx         ; Den Rest um 1 erhöhen
       mov  [tmpc], dl ; Und ebenfalls sichern

\</asm\>

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/6188/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1442/index.html)

<!-- MediaWiki page 1442; revision 6188; parent 5816; 2009-11-06T19:09:07Z -->
