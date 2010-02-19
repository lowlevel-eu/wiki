# Codeoptimierung

Durch die Optimierung des Quellcodes eines Programms kann dieses schneller, effektiver und platzsparender arbeiten.

## Allgemeines

### Datengrößen

DWORD ist beser...

### Alignment

## Assembler

### Reduzierung der Codegröße

Die nachfolgenden Tricks eignen sich besonders zum Programmieren in [Assembler](https://github.com/lowlevel-eu/wiki/wiki/Assembler "Assembler"), wie es z.B. im [Bootloader](https://github.com/lowlevel-eu/wiki/wiki/Bootloader "Bootloader") nötig ist.

| Beschreibung | Optimierter Code |
| --------------------------------------- | --------------------------------------------------------------------------------------------- |
| Register 0 setzen | \<asm\>xor eax, eax\</asm\> |
| Prüfen, ob Register 0 ist | \<asm\>test eax, eax jz ...\</asm\><br> |
| Multiplikation mit einer Zweierpotenz | \<asm\>shl eax, log<sub>2</sub>Faktor\</asm\> |
| Division durch eine Zweierpotenz | \<asm\>shr eax, log<sub>2</sub>Divisor\</asm\> |
| Beliebige Multiplikation | \<asm\>imul eax, \[Faktor_1\], \[Faktor_2\]\</asm\> |
| Schleife | \<asm\>mov ecx, \[Anzahl_Wiederholungen\] von_vorn:<br><br>...<br>loop von_vorn\</asm\><br> |

### Steigerung der Effektivität

#### PUSHA / POPA

Ist es schneller jedes Register einzeln zu pushen, oder besser pusha?

## Hochsprachen

### Optimierungstools

TODO

## siehe auch

- [Ausgabe 8](https://github.com/lowlevel-eu/wiki/wiki/Ausgabe-8#tipps--tricks "Ausgabe 8")

## Weblinks

- <http://www.intel.com/Assets/PDF/manual/248966.pdf>

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/7107/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2187/index.html)

<!-- MediaWiki page 2187; revision 7107; parent 0; 2010-02-19T16:13:30Z -->
