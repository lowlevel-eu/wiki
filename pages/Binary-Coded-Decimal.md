# Binary Coded Decimal

**Binary Coded Decimal** (kurz **BCD**) ist ein Format zur binären Kodierung von Dezimalzahlen. Man unterscheidet zwischen gepackten und ungepackten BCD-Zahlen. Im BCD-Format werden die einzelnen Dezimalstellen einer Zahl in einem Byte bzw. in gepackter Form in einem Nibble (4 Bit) gespeichert.

Dies kann man mit der folgenden Tabelle verdeutlichen:

| Dezimal | BCD gepackt | BCD ungepackt |
| --------- | ------------- | --------------- |
| 0 | 0000 | 00000000 |
| 1 | 0001 | 00000001 |
| 2 | 0010 | 00000010 |
| 3 | 0011 | 00000011 |
| 4 | 0100 | 00000100 |
| 5 | 0101 | 00000101 |
| 6 | 0110 | 00000110 |
| 7 | 0111 | 00000111 |
| 8 | 1000 | 00001000 |
| 9 | 1001 | 00001001 |

  

## Gepackte BCD Zahlen

Im gepackten BCD-Format befinden sich die Nibbles der BCD-Zahl direkt hintereinander.

Beispiel:

    Dezimal  : 42
    Gepacktes BCD-Format: 0100 0010b (0x42)

## Ungepackte BCD Zahlen

Im ungepackten BCD-Format steht jedem BCD-Nibble ein leeres Nibble voran, so dass eine Dezimalstelle in einem Byte gespeichert wird. Dies wurde zur einfacheren Handhabung gemacht, da in den Systemen, für die BCD entwickelt wurde, ein Byte die kleinste Dateneinheit war, die man direkt ansprechen konnte.

Beispiel:

     Dezimal  : 42
     Ungepacktes BCD-Format: 0000 0100b (0x04)  0000 0010b (0x02)

Der Vorteil hierbei ist z. B., dass durch eine einfache *or*-Verknüpfung mit 0x30 eine BCD-Ziffer in das passende [ASCII](Codepage-437.md "ASCII")-Zeichen umgewandelt werden kann.

## Weblinks

- [Artikel auf Wikipedia](http://de.wikipedia.org/wiki/Binary_Coded_Decimal)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/7668/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1589/index.html)

<!-- MediaWiki page 1589; revision 7668; parent 5814; 2010-05-09T09:07:08Z -->
