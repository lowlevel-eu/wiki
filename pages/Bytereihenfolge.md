# Bytereihenfolge

Die Bytereihenfolge ist die Reihenfolge in der die Bytes im Speicher abgelegt sind. Es gibt zwei grundlegende Typen von Bytereihenfolge, Big-Endian und Little-Endian, welche auch für die Bitreihenfolge benutzt werden.

## Little Endian

Little Endian ist die häufigste Byte- und Bitreihenfolge die bei Computern verwendet wird. Sie ist dem Zahlsystem von LTR-Sprachen (Also z.B. europäische Sprachen) genau entgegengesetzt. Ein Beispiel:

| Hex | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | A | B | C | D | E | F | Dez | Hi | Lo |
| ------ | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ------- | ----- | ----- |
| AFFE | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 0 | 1 | 0 | 1 | 1 | 1 | 1 | 45054 | FE | AF |

Little Endian hat den Vorteil, dass man um den 8-bit einer 32-bit Zahl zu erhalten man nicht die Basis der Position der Zahl verändern muss.

## Big Endian

Big Endian wird im PPC und Alpha CPUs eingesetzt. Es ist unserem natürlichem Zahlensystem entsprochen, denn die höchstwertigste Ziffer ist rechts

| Hex | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | A | B | C | D | E | F | Dez | Hi | Lo |
| ------ | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ------- | ----- | ----- |
| AFFE | 0 | 1 | 0 | 1 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 45054 | AF | FE |

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/11339/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2658/index.html)

<!-- MediaWiki page 2658; revision 11339; parent 0; 2016-01-29T18:52:35Z -->
