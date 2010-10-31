# Interrupt Vector Table

Die **Interrupt Vector Table** (kurz **IVT**) befindet sich im ersten Kilobyte des Arbeitsspeichers (siehe [Speicherbereiche](https://github.com/lowlevel-eu/wiki/wiki/Speicherbereiche "Speicherbereiche")). Ihre Aufgabe besteht darin, die Adresse der [Interrupt Service Routine](https://github.com/lowlevel-eu/wiki/wiki/Interrupt-Service-Routine "ISR") für jeden [Interrupt](https://github.com/lowlevel-eu/wiki/wiki/Interrupt "Interrupt") bereitzustellen. Die IVT hat nur im [Real Mode](https://github.com/lowlevel-eu/wiki/wiki/Real-Mode "Real Mode") Bedeutung und wird im [Protected Mode](https://github.com/lowlevel-eu/wiki/wiki/Protected-Mode "Protected Mode") durch die [IDT](https://github.com/lowlevel-eu/wiki/wiki/Interrupt-Descriptor-Table "IDT") abgelöst.

## Aufbau

Insgesamt stehen 256 Interrupts zur Verfügung, deshalb muss die IVT auch 256 Einträge (einen für jeden Interrupt) haben. Ein Eintrag ist 4 Byte groß und enthält eine Realmodeadresse, die aus 2 Byte Segment und 2 Byte Offset besteht. Ein Eintrag sieht im Speicher folgendermaßen aus:

    Byte
           +---------------+---------------+
       0   |             Offset            |
           +---------------+---------------+
           +---------------+---------------+
       2   |            Segment            |
           +---------------+---------------+

| Byte |  |
| ------ | --------- |
| 0 | Offset |
| 2 | Segment |

Die IVT belegt somit genau 256 \* 4 = 1024 Byte. Die genaue Verwendung dieser Einträge bei Auftreten eines Interrupts wird im Artikel [Interrupt](https://github.com/lowlevel-eu/wiki/wiki/Interrupt "Interrupt") erklärt.

## Während des Bootvorgangs

Nach dem Start des Computers wird die IVT automatisch vom [BIOS](https://github.com/lowlevel-eu/wiki/wiki/Basic-Input-Output-System "BIOS") erstellt, und die Adressen zeigen auf Funktionen, die entweder das BIOS einem Betriebssystem zur Verfügung stellt, oder die benötigt werden, um mit der Hardware zu kommunizieren.

Nach dem [Bootvorgang](https://github.com/lowlevel-eu/wiki/wiki/Bootprozess-auf-x86 "Bootvorgang") kann es für ein Betriebssystem sinnvoll sein, einige Interrupts durch eigene Funktionen behandeln zu lassen. Dazu zählen vor allem die Exceptions.

## Beispiel

Beispielsweise will man wahrscheinlich eine "Division durch 0" (Interrupt 0) anders als das BIOS behandeln (z.B. den momentanen Prozess beenden und zur Shell zurückkehren):

\<asm\> xor ax, ax  ;ax = 0x00 (mov ax, 0x00 wäre ein Byte mehr) mov es, ax  ;es = ax (also 0)

IRQs deaktivieren

Dies ist nur notwendig, damit nicht während des Anpassens der IVT ein IRQ auftritt, welcher für den Fall, dass

a\) wir hier den Interruptvektor des IRQ verändern

b\) der IRQ-Handler seinerseits den hier veränderten Interruptvektor aufruft

zu undefiniertem Verhalten führen kann.

cli

Offset  
Die Adresse unserer Interrupt Service Routine

mov WORD \[es:0\], \_\_int0x00

Segment  
Wir geben hier das momentane Codesegment an

mov WORD \[es:0+2\], cs

IRQs wieder aktivieren

sti \</asm\>

### Ein NASM Macro

Jetzt ein macro für NASM: \<asm\> %macro IVT.Handlerwahl 2 push ax push es xor ax, ax mov es, ax cli mov WORD \[es:%1\*4\], %2 mov WORD \[es:%1\*4+2\], cs sti pop es pop ex %endmacro \</asm\> Das erste Argument muss dann die IRQ-Nummer sein, das zweite ein Label von dem Handler. Das kann dann so benutzt werden: \<asm\>

... hier ist der Startcode ...

IVT.Handlerwahl 0x00, IRQ_0x00

... hier kommt dann noch irgendein Code ...

IRQ_0x00:  ;Handler für IRQ 0

... hier kann ein Hinewistext geschreiben werden o.ä. ...

iret \</asm\>

## Links

- [Ralf Brown's Interrupt List](http://www.cs.cmu.edu/afs/cs.cmu.edu/user/ralf/pub/WWW/files.html) (Download)
- [Ralf Brown's Interrupt List](http://www.ctyme.com/intr/int.htm) (online anschaubar)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/8751/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1540/index.html)

<!-- MediaWiki page 1540; revision 8751; parent 8660; 2010-10-31T15:05:29Z -->
