# PAT

Mit der *Page Attribute Table* ist es möglich, das Caching von [Pages](Paging "Paging") genauer einzustellen.

## Mögliche x86-Cachemodi

Folgende Cachemodi (*Memory Types*) existieren auf x86-Systemen:

- UC: Strong Uncacheable (nichts wird gecachet)
- UC-: Uncacheable (wie UC, kann über die MTRRs allerdings zu Write Combining überschrieben werden)
- WP: Write Protected (nur Lesezugriffe werden gecachet)
- WT: Write Through (Lesezugriffe werden gecachet, Schreibzugriffe werden sowohl in den Cache als auch in den Speicher geschrieben)
- WC: Write Combining (aufeinander folgende Schreibzugriffe werden in einem WC-Puffer kombiniert und dann gemeinsam in den Speicher geschrieben)
- WB: Write Back (Lese- und Schreibzugriffe werden gecachet)

Für normalen Speicher eignet sich WB, für MMIO-Bereiche je nachdem UC, UC-, WP oder WT. WC eignet sich besonders für Framebuffer.

## Page-Level-Caching ohne PAT

Normalerweise gibt es für jede Page genau zwei Bits, die dafür genutzt werden können: CD (Cache Disable) und WT (Write Through). Je nach Kombination ergeben sich die folgenden Möglichkeiten:

| CD | WT | Bedeutung |
| ----- | ----- | ----------- |
| 0 | 0 | WB |
| 0 | 1 | WT |
| 1 | 0 | UC- |
| 1 | 1 | UC |

## Page-Level-Caching mit PAT

Um die anderen oben genannten Cachemodi zu verwenden, müssen entweder die MTRRs oder die PAT benutzt werden. Die PAT ist eine Tabelle, die die Werte der PAT-, CD- und WT-Bits einer Page ihrem Cachemode zuordnet. Dabei werden diese drei Bits zu einem Wert von 0 bis 7 kombiniert, der dann auf einen PAT-Eintrag zeigt, welcher den Cachemodus enthält. Dabei ist WT Bit 0 (das niederwertigste Bit), CD Bit 1 und PAT Bit 2 (das höchstwertige Bit).

Die acht PAT-Einträge werden im IA32_PAT-[MSR](Machine-Specific-Register "MSR") gesetzt (Index 0x277). Sein Aufbau ist wie folgt:

| Bits | Bedeutung |
| --------- | ------------------------------------------------- |
| 0 – 2 | Cachemode für PAT-Eintrag 0 (PAT=0, CD=0, WT=0) |
| 3 – 7 | *reserviert* |
| 8 – 10 | Cachemode für PAT-Eintrag 1 (PAT=0, CD=0, WT=1) |
| 11 – 15 | *reserviert* |
| 16 – 18 | Cachemode für PAT-Eintrag 2 (PAT=0, CD=1, WT=0) |
| 19 – 23 | *reserviert* |
| 24 – 26 | Cachemode für PAT-Eintrag 3 (PAT=0, CD=1, WT=1) |
| 27 – 31 | *reserviert* |
| 32 – 34 | Cachemode für PAT-Eintrag 4 (PAT=1, CD=0, WT=0) |
| 35 – 39 | *reserviert* |
| 40 – 42 | Cachemode für PAT-Eintrag 5 (PAT=1, CD=0, WT=1) |
| 43 – 47 | *reserviert* |
| 48 – 50 | Cachemode für PAT-Eintrag 6 (PAT=1, CD=1, WT=0) |
| 51 – 55 | *reserviert* |
| 56 – 58 | Cachemode für PAT-Eintrag 7 (PAT=1, CD=1, WT=1) |
| 59 – 63 | *reserviert* |

Die Kodierung der Cachemodi ist wie folgt:

| Wert | Bedeutung |
| ------ | -------------- |
| 0 | UC |
| 1 | WC |
| 2 | *reserviert* |
| 3 | *reserviert* |
| 4 | WT |
| 5 | WP |
| 6 | WB |
| 7 | UC- |

Wird ein reservierter Modus ausgewählt oder ein reserviertes Bit im MSR gesetzt, so wird ein GPF ausgelöst.

Beim Booten sind die acht PAT-Einträge wie folgt belegt:

| Eintrag | Cachemodus |
| --------- | ------------ |
| 0 | WB |
| 1 | WT |
| 2 | UC- |
| 3 | UC |
| 4 | WB |
| 5 | WT |
| 6 | UC- |
| 7 | UC |

Dies führt genau zur oben genannten Defaultbelegung der CD- und WT-Bits. Das PAT-Bit wird ignoriert.

### Unterstützung des Prozessors

Die PAT ist seit Pentium-III-Prozessoren vorhanden. Ob eine CPU das Feature unterstützt, kann mittels des [CPUID-Befehls](CPUID#funktion-0x0000_0001 "CPUID") getestet werden.

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/11434/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2662/index.html)

<!-- MediaWiki page 2662; revision 11434; parent 11374; 2020-08-02T21:47:32Z -->
