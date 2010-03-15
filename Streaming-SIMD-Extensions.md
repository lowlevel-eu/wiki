# Streaming SIMD Extensions

Die Streaming SIMD Extensions (oder kurz SSE genannt), ist ein eine Befehlserweiterung für die x86-Architektur, die Intel mit dem Pentium III eingeführt hat. SSE stellt neue 128-Bit-Register zur Verfügung, wohingegen MMX die vorhandenen FPU-Register nutzt, welche oft zum verrechnen von vierdimensionalen Vektoren genutzt werden. Wie auch MMX folgt SSE dem SIMD-Prinzip: Single Instruction, Multiple Data.

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
| ADDSS | Addiert Skalar zu Komponenten eines Registers | ADDPS xmm0, xmm1 |
| SUBSS | Subtrahiert Skalar von den Komponenten eines Registers | SUBPS xmm0, xmm1 |
| MULSS | Multipliziert die Komponenten eines Registers mit Skalar | MULPS xmm0, xmm1 |
| DIVSS | Dividiert die Komponenten eines Registers durch Skalar | DIVPS xmm0, xmm1 |

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/7385/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2199/index.html)

<!-- MediaWiki page 2199; revision 7385; parent 7256; 2010-03-15T20:49:59Z -->
