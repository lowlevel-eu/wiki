# Binary Coded Decimal

**BCD**(**B**inary **C**oded **D**ecimal)ist ein Format zur binären Kodierung von Dezimalzahlen. Man unterscheidet zwischen gepackten- und ungepackten-BSD Zahlen.

Im **BCD** Format werden die einzelnen Dezimalstellen einer Zahl in jeweils einem Nibble(4Bit) gespeichert. Dies kann man mit der folgenden Tabelle machen:

| Dezimal | BCD |
| --------- | ------ |
| 0 | 0000 |
| 1 | 0001 |
| 2 | 0010 |
| 3 | 0011 |
| 4 | 0100 |
| 5 | 0101 |
| 6 | 0110 |
| 7 | 0111 |
| 8 | 1000 |
| 9 | 1001 |

## gepackte BCD Zahlen

Im gepackten BCD-Format befinden sich die Nibble der BCD-Zahl direkt hinter einander. Beispiel:

    Dezimal  : 42
    Gepacktes BCD-Format: 0100 0010b (42)

## ungepackte BCD Zahlen

Im ungepackten BCD-Format steht jedem BCD-Nibbel ein leeres Nibbel voran. Beispiel:

     Dezimal  : 42
     Ungepacktes BCD-Format: 0000 0100b (04)  0000 0010b (02)

Der Vorteil hierbei ist, dass durch eine einfache **or**-Verknüpfung mit 0x30 eine BCD-Ziffer in das passende ASCII-Zeichen umgewandelt werden kann.

## Weblinks

- [Artikel auf Wikipedia](http://de.wikipedia.org/wiki/Binary_Coded_Decimal)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/2389/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1589/index.html)

<!-- MediaWiki page 1589; revision 2389; parent 2388; 2007-12-15T21:01:08Z -->
