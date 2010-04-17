# Streaming SIMD Extensions

Die Streaming SIMD Extensions (oder kurz SSE genannt), ist ein eine Befehlserweiterung für die x86-Architektur, die Intel mit dem Pentium III eingeführt hat. SSE stellt neue 128-Bit-Register zur Verfügung, welche oft zum verrechnen von vierdimensionalen Vektoren genutzt werden, wohingegen MMX die vorhandenen FPU-Register nutzt. Wie auch MMX folgt SSE dem SIMD-Prinzip: Single Instruction, Multiple Data.

## Unterstützung feststellen

## Register

Im 32-Bit-Modus stehen 8 Register (xmm0 bis xmm7) zur Verfügung. Im 64-Bit-Modus gibt es 8 zusätzliche Register (xmm8 bis xmm15).

## Befehle

### Arithmetische Befehle

Hinweis: Das zuerst angegebene Register enthält das Ergebnis.

| Befehl | Funktion | Beispiel |
| -------- | ---------------------------------------------------------- | --------------------------------- |
| ADDPS | Addiert die Komponenten von zwei Registern | \<asm\>ADDPS xmm0, xmm1\</asm\> |
| SUBPS | Subtrahiert die Komponenten von zwei Registern | \<asm\>SUBPS xmm0, xmm1\</asm\> |
| MULPS | Multipliziert die Komponenten von zwei Registern | \<asm\>MULPS xmm0, xmm1\</asm\> |
| DIVPS | Dividiert die Komponenten von zwei Registern | \<asm\>DIVPS xmm0, xmm1\</asm\> |
| ADDSS | Addiert Skalar zu Komponenten eines Registers |  |
| SUBSS | Subtrahiert Skalar von den Komponenten eines Registers |  |
| MULSS | Multipliziert die Komponenten eines Registers mit Skalar |  |
| DIVSS | Dividiert die Komponenten eines Registers durch Skalar |  |

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/7586/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2199/index.html)

<!-- MediaWiki page 2199; revision 7586; parent 7413; 2010-04-17T16:22:09Z -->
