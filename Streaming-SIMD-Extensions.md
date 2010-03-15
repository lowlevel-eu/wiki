# Streaming SIMD Extensions

Die Streaming SIMD Extensions (oder kurz SSE genannt), ist ein eine Befehlserweiterung für die x86-Architektur, die Intel mit dem Pentium III eingeführt hat. SSE stellt neue 128-Bit-Register zur Verfügung, wohingegen MMX die vorhandenen FPU-Register nutzt, welche oft zum verrechnen von vierdimensionalen Vektoren genutzt werden. Wie auch MMX folgt SSE dem SIMD-Prinzip: Single Instruction, Multiple Data.

## Unterstützung feststellen

## Register

## Befehle

### Arithmetische Befehle

Hinweis: Das zuerst angegebene Register enthält das Ergebnis.

| Befehl | Funktion | Beispiel |
| -------- | ---------------------------------------------------------- | ------------------ |
| ADDPS | Addiert die Komponenten von zwei Registern | ADDPS xmm0, xmm1 |
| SUBPS | Subtrahiert die Komponenten von zwei Registern | SUBPS xmm0, xmm1 |
| MULPS | Multipliziert die Komponenten von zwei Registern | MULPS xmm0, xmm1 |
| DIVPS | Dividiert die Komponenten von zwei Registern | DIVPS xmm0, xmm1 |
| ADDSS | Addiert Skalar zu Komponenten eines Registers |  |
| SUBSS | Subtrahiert Skalar von den Komponenten eines Registers |  |
| MULSS | Multipliziert die Komponenten eines Registers mit Skalar |  |
| DIVSS | Dividiert die Komponenten eines Registers durch Skalar |  |

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/7386/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2199/index.html)

<!-- MediaWiki page 2199; revision 7386; parent 7385; 2010-03-15T20:52:48Z -->
