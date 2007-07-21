# Interrupt Vector Table

Die Interrupt Vector Table (kurz IVT) ist besteht aus dem ersten Kilobyte des Arbeitsspeichers. Ihre Aufgabe besteht darin, die Adressen für die Interrupts bereitzustellen.  
Die IVT stellt für jeden Interrupt 2 Addressen zur Verfügung. Daraus folgt, dass genau 256 Interrupts in der IVT platz haben können. Die erste Addresse ist die, an die die CPU springen muss um den Interrupt auszuführen, also die Startaddresse des Interrupt Codes. Die zweite Addresse ist die, an die die CPU nach Ausführung des Interrupts zurückspringen soll.  
Nach dem Start des Computers wird die IVT automatisch geschrieben. Die Addressen zeigen auf Funktionen, die das BIOS für diese Interrupts bereitstellt. Nach dem Start ist daher sinnvoll diese durch eigene zu ersetzen. Beispielsweiße will man bei einer "Division durch 0" ganz bestimmte Dinge tun. So ersetzt man die Addressen des Interrupts 0h durch eigene. So zum Beispiel:

    xor ax, ax
    mov es, ax
    cli; disable interrupt
    mov WORD [es:0x04*0x0h], __int0x00 ; Unsere Interrupt Routine
    mov WORD [es:0x04*0x0h+2], __int0x00_back ; Rücksprungaddresse, man kann hier auch einfach das Register cs angeben
    sti

  

## Quellen

- \[[\[1\]](http://lowlevel.brainsware.org/wiki/index.php/Ausgabe_2)\]
- \[[\[2\]](http://lowlevel.brainsware.org/wiki/index.php/Ausgabe_2)\]

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/2060/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1540/index.html)

<!-- MediaWiki page 1540; revision 2060; parent 0; 2007-07-21T20:27:42Z -->
