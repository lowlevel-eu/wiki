# Logical Block Addressing

Bei Logical Block Addressing (Logische Block Adressierung) werden Sektoren von Massenspeichern von 0 aufsteigend adressiert. Das Gegenstück zu LBA ist das ältere [CHS](https://github.com/lowlevel-eu/wiki/wiki/Cylinder-Head-Sector "Cylinder Head Sector").

## Umrechnung von LBA zu CHS

| Abkürzung | Bedeutung |
| ----------- | ------------------------------ |
| mS | Anzahl der Sektoren pro Spur |
| mH | Anzahl der Köpfe |
| S | Sektor |
| H | Kopf |
| C | Zylinder |

    C =   LBA  /  (mH*mS)
    H =  (LBA mod (mH*mS))  /  mS
    S = ((LBA mod (mH*mS)) mod mS) + 1

## Beispiel für eine 3,5"-HD-Diskette

Da es im Bootsektor auf jedes Byte ankommt, habe ich mich darum bemüht, die Umrechnung möglichst klein zu machen. Die Zahlenwerte (Sektoren pro Zylinder und Anzahl der Köpfe) gelten für eine 3,5"-Diskette mit 1440 kB Speicherplatz. \<asm\>; in ax steht die Sektornummer

C

xor dx, dx  ; dx leeren mov bx, 2\*18  ; Anzahl der Heads \* Sektoren pro Zylinder div bx  ; dx:ax / bx = ax, Rest dx mov \[tmpa\], al ; al sichern

H

mov ax, dx  ; mit dem Rest der Division wird jetzt weitergearbeitet xor dx, dx  ; dx wieder leeren shr bx, 1  ; 36/2 = 18, also nur die Anzahl der Sektoren pro Zylinder div bx  ; dx:ax / bx = ax, Rest dx mov \[tmpb\], al ; al sichern

S

inc dx  ; Den Rest um 1 erhöhen mov \[tmpc\], dl ; Und ebenfalls sichern\</asm\>

## siehe auch

- [CHS](https://github.com/lowlevel-eu/wiki/wiki/Cylinder-Head-Sector "CHS") - veraltete Methode zum Adressieren von Sektoren

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/9841/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1442/index.html)

<!-- MediaWiki page 1442; revision 9841; parent 7153; 2011-06-11T20:51:50Z -->
