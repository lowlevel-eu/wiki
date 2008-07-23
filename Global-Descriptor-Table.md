# Global Descriptor Table

Der Global Descriptor Table (auch GDT) ist eine i386 spezifische Struktur, welche Informationen über Speicherabschnitte enthält.

Der Ort der GDT wird mit dem Befehl lgdt mitgeteilt.

## Struktur

Jeder Eintrag in den GDT besteht aus acht Bytes.

| Byte | Name | Bits |
| ------ | ------------ | ------------------- |
| 0 | Limit | 0-7 |
| 1 | Limit | 8-15 |
| 2 | Base | 0-7 |
| 3 | Base | 8-15 |
| 4 | Base | 16-23 |
| 5 | Accessbyte | 0-7 (vollständig) |
| 6 | Flags | 0-3 (vollständig) |
| 7 | Limit | 16-19 |
| 8 | Base | 24-31 |

| Name | Bedeutung |
| ------------ | --------------------------------------------------------------------------------- |
| Limit | Größe des Segments - 1 (entweder in Bytes oder in 4KiB-Einheiten - siehe Flags) |
| Base | Die Addresse wo das Segment beginnt |
| Accessbyte | Zugriffsinformationen (Ring, executable, etc.) |
| Flags | Definiert die Segmentgrößeneinheit und 16/32 Bit. |

Der Access-Byte:

| Bit | Name | Bedeutung |
| -------- | ------------------------------ | --------------------------------------------------------------------------------------------- |
| 7 | present bit | Muss 1 für einen aktiven Eintrag sein |
| 6 u. 5 | Privilege | Ring - von Ring 0 (Kernel Mode) zu Ring 3 (User Mode) |
| 4 | 1 | Ist 1 |
| 3 | Executable bit | Bei 1 ist das Speichersegment ein Codesegment, bei 0 ein Datensegment |
| 2 | Direction bit/Conforming bit | Abhängig vom Executable bit |
| 1 | Readable bit/Writable bit | Bei einem Codesegment ob lesen erlaubt ist, bei einem Datensegment ob schreiben erlaubt ist |
| 0 | Accessed bit | Sollte 0 gesetzt werden, wird dann vom Prozessor bei Zugriff gesetzt. |

Die Flags:

| Bit | Name | Bedeutung |
| ----- | ----------------- | ---------------------------------------------------------------------------- |
| 0 | Granularity bit | Bei 0 wird als Einheit bei Limit ein Byte benutzt, bei 1 stattdessen 4 KiB |
| 1 | Size bit | 0 bedeuted 16 bit protected mode, bei 1 32 bit protected mode. |

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/3033/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1661/index.html)

<!-- MediaWiki page 1661; revision 3033; parent 3027; 2008-07-23T15:12:54Z -->
