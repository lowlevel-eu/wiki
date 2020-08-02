# Streaming SIMD Extensions

Die Streaming SIMD Extensions (oder kurz SSE genannt), ist ein eine Befehlserweiterung für die [x86](https://github.com/lowlevel-eu/wiki/wiki/X86 "X86")-Architektur, die Intel mit dem Pentium III eingeführt hat. SSE stellt neue 128-Bit-Register zur Verfügung, welche oft zum Verrechnen von vierdimensionalen Vektoren genutzt werden, wohingegen [MMX](https://github.com/lowlevel-eu/wiki/wiki/MultiMedia-Extension "MMX") die vorhandenen [FPU](https://github.com/lowlevel-eu/wiki/wiki/Mathematischer-Koprozessor "FPU")-Register nutzt (seit SSE2 können allerdings alle MMX-Befehle auch auf den SSE-Registern ausgeführt werden). Wie auch MMX folgt SSE dem SIMD-Prinzip: Single Instruction, Multiple Data.

## Unterstützung feststellen

## Register

### 32-Bit

Im 32-Bit-Modus stehen 8 Register (xmm0 bis xmm7) zur Verfügung.

  

### 64-Bit

Im 64-Bit-Modus gibt es 8 zusätzliche Register (xmm8 bis xmm15).

<table>
<tbody><tr>
<th colspan="16">Bytes
</th></tr>
<tr>
<th>15
</th>
<th>14
</th>
<th>13
</th>
<th>12
</th>
<th>11
</th>
<th>10
</th>
<th>9
</th>
<th>8
</th>
<th>7
</th>
<th>6
</th>
<th>5
</th>
<th>4
</th>
<th>3
</th>
<th>2
</th>
<th>1
</th>
<th>0
</th></tr>
<tr>
<td colspan="16">XMM?
</td></tr>
<tr>
<td colspan="16">? = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15
</td></tr></tbody></table>

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

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/11445/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2199/index.html)

<!-- MediaWiki page 2199; revision 11445; parent 11231; 2020-08-02T21:57:51Z -->
