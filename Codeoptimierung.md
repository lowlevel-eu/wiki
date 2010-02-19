# Codeoptimierung

Durch die Optimierung des Quellcodes eines Programms kann dieses schneller, effektiver und platzsparender arbeiten.

## Allgemeines

### Datengrößen

Die Wortgröße des Prozessors zu verwenden ist oft besser als dies nicht zu tun (32 Bit bei i386, 64 Bit bei x86-64).

### Alignment

## Assembler

### Reduzierung der Codegröße

Die nachfolgenden Tricks eignen sich besonders zum Programmieren in [Assembler](https://github.com/lowlevel-eu/wiki/wiki/Assembler "Assembler"), wie es z. B. im [Bootloader](https://github.com/lowlevel-eu/wiki/wiki/Bootloader "Bootloader") nötig ist.

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

- [Intel ‐ Optimierung für IA32](http://www.intel.com/Assets/PDF/manual/248966.pdf)
- [AMD ‐ Software Optimierung für AMD64](http://support.amd.com/us/Processor_TechDocs/25112.PDF)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/7112/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2187/index.html)

<!-- MediaWiki page 2187; revision 7112; parent 7111; 2010-02-19T17:27:40Z -->
