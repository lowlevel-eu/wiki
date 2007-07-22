# Interrupt Vector Table

Die Interrupt Vector Table (kurz IVT) befindet sich im ersten Kilobyte des Arbeitsspeichers (siehe [Speicherbereiche](https://github.com/lowlevel-eu/wiki/wiki/Speicherbereiche "Speicherbereiche")). Ihre Aufgabe besteht darin, die Adresse der [Interrupt Service Routine](https://github.com/lowlevel-eu/wiki/wiki/Interrupt-Service-Routine "ISR") für jeden [Interrupt](https://github.com/lowlevel-eu/wiki/wiki/Interrupt "Interrupt") bereitzustellen. Die IVT hat nur im real mode Bedeutung und wird im [Protected Mode](https://github.com/lowlevel-eu/wiki/wiki/Protected-Mode "Protected Mode") durch die [IDT](https://github.com/lowlevel-eu/wiki/wiki/Interrupt-Descriptor-Table "IDT") abgelöst.

## Aufbau

Insgesamt stehen 256 Interrupts zur Verfügung, deshalb muss die IVT auch 256 Einträge (einen für jeden Interrupt) haben. Ein Eintrag ist 4 Byte groß und enthält eine Realmodeadresse, die aus 2 Byte Segment und 2 Byte Offset besteht. Ein Eintrag sieht im Speicher folgendermaßen aus:

    Byte
           +---------------+---------------+
       0   |             Offset            |
           +---------------+---------------+
           +---------------+---------------+
       2   |            Segment            |
           +---------------+---------------+

Die IVT belegt somit genau 256 \* 4 = 1024 Byte. Die genaue Verwendung dieser Einträge bei Auftreten eines Interrupts wird im Artikel [Interrupt](https://github.com/lowlevel-eu/wiki/wiki/Interrupt "Interrupt") erklärt.

## Während des Bootvorgangs

Nach dem Start des Computers wird die IVT automatisch vom [BIOS](https://github.com/lowlevel-eu/wiki/wiki/Basic-Input-Output-System "BIOS") erstellt und die Adressen zeigen auf Funktionen, die entweder das BIOS einem Betriebssystem zur Verfügung stellt oder die benötigt werden, um mit der Hardware zu kommunizieren. Nach dem [Bootvorgang](https://github.com/lowlevel-eu/wiki/wiki/Bootprozess-auf-x86 "Bootvorgang") kann es für ein Betriebssystem sinnvoll sein einige Interrupts durch eigene Funktionen behandeln zu lassen. Dazu zählt vor allem die Exceptions.

## Beispiel

Beispielsweise will man wahrscheinlich eine "Division durch 0" (Interrupt 0) anders als das BIOS behandeln (z.B. den momentanen Prozess beenden und zur Shell zurückkehren):

    xor ax, ax
    mov es, ax
    cli                            ; IRQs deaktivieren: Dies ist nur notwendig, wenn man einen Eintrag für einen IRQ verändert
    mov WORD [es:0], __int0x00      ; Offset: Die Adresse unserer Interrupt Service Routine
    mov WORD [es:0+2], cs           ; Segment: Wir geben hier das momentane Codesegment an
    sti                            ; IRQs aktivieren

## Links

- [Ralf Brown's Interrupt List](http://www.cs.cmu.edu/afs/cs.cmu.edu/user/ralf/pub/WWW/files.html) (Download)
- [Ralf Brown's Interrupt List](http://www.ctyme.com/intr/int.htm) (online anschaubar)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/2069/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1540/index.html)

<!-- MediaWiki page 1540; revision 2069; parent 2068; 2007-07-22T19:09:13Z -->
