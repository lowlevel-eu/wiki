# Advanced Vector Extensions

**Advanced Vector Extensions** kurz **AVX** ist eine Erweiterung der x86-Architektur, die Intel im März 2008 vorgeschlagen wurde.

## Eigenschaften

AVX ist eine Erweiterung von [SSE](Streaming-SIMD-Extensions "SSE"). Die Register von AVX sind 256-Bit gross und heissen YMM0 bis YMM15. Prozessoren, die AVX unterstützen führen SSE Befehle auf den unteren 128-Bit der AVX-Register aus. Zusätzlich führt AVX ein Drei-Operanden-SIMD-Befehlsformat ein (c := a + b). Das führt zu einer Optimierung der Abläufe, da das Quellregister nicht mehr überschrieben wird und somit allfällige Kopiervorgänge einspart. Drei-Operanden-SIMD-Befehle können nur mit AVX-Operanden (YMM) verwendet werden.

## Anwendung

- Nützlich für gleitkommaintensive Berechnung, vor allem im Multimedia-, wissenschaftlichen oder Finanzberechnungen. Ganzzahloperationen sollen später folgen.
- Erhöht Parallelität und Durchsatz von Gleitkomma-SIMD-Berechnungen
- Verringert die Registerlast durch nicht destruktive Drei-Operanden-Form

## Unterstützung feststellen

Die Unterstützung von AVX durch die CPU kann durch aufrufen der [CPUID Funktion 0x0000_0001](CPUID#funktion-0x0000_0001 "CPUID") und durch Prüfen des Bit 28 im Register ECX geprüft werden.

## Register

Im 32-Bit-Modus stehen nur YMM0 bis YMM7 zur Verfügung. Im 64-Bit-Modus sind alle Register verfügbar.

<table>
<tbody><tr>
<th colspan="32">Bytes
</th></tr>
<tr>
<th>31
</th>
<th>30
</th>
<th>29
</th>
<th>28
</th>
<th>27
</th>
<th>26
</th>
<th>25
</th>
<th>24
</th>
<th>23
</th>
<th>22
</th>
<th>21
</th>
<th>20
</th>
<th>19
</th>
<th>18
</th>
<th>17
</th>
<th>16
</th>
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
<td colspan="32">YMM?
</td></tr>
<tr>
<td colspan="16">
</td>
<td colspan="16">XMM?
</td></tr>
<tr>
<td colspan="32">? = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15
</td></tr></tbody></table>

## Befehle

| Instruktion | Beschreibung |
| -------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| VBROADCASTSS, VBROADCASTSD, VBROADCASTF128 | Kopiert ein 32-Bit-, 64-Bit- oder 128-Bit-Speicheroperanden in alle Elemente eines XMM- oder YMM-Registers. |
| VINSERTF128 | Ersetzt entweder die obere oder untere Hälfte eines 256-Bit-YMM-Register mit dem Wert aus dem 128-Bit-Operanden. Die andere Hälfte bleibt unverändert. |
| VEXTRACTF128 | Extrahiert entweder die obere oder untere Hälfte eines 256-Bit-YMM-Registers und kopiert den Wert in den 128-Bit-Operanden. |
| VMASKMOVPS, VMASKMOVPD | Liest eine beliebige Anzahl von Vektorelementen bedingt aus einem SIMD-Speicheroperand in ein Zielregister, wobei der verbleibende Platz mit Nullen gefüllt wird. Alternativ schreibt es eine beliebige Anzahl von Vektorelementen bedingt von einem SIMD-Register in ein SIMD-Speicheroperanden, wobei der verbleibende Platz im Speicher nicht verändert wird. |
| VPERMILPS, VPERMILPD | Tauscht 32-Bit- oder 64-Bit-Vektorelemente aus. |
| VPERM2F128 | Mischt die vier 128-Bit-Vektorelemente aus zwei 256-Bit-Ursprungsoperanden in ein 256-Bit-Zieloperanden. |
| VTESTPS, VTESTPD | Setzt die Flag-Bits CF und ZF entsprechend eines Vergleiches aller Vorzeichenbits. |
| VZEROALL | Füllt alle YMM-Register mit Nullen und markiert sie als unbenutzt. Wird beim Umschalten zwischen 128-Bit- und 256-Bit-Modus verwendet. |
| VZEROUPPER | Füllt die obere Hälfte aller YMM-Register mit Nullen. Wird beim Umschalten zwischen 128-Bit- und 256-Bit-Modus verwendet. |

## Links

[Wikipedia-Artikel](http://de.wikipedia.org/wiki/Advanced_Vector_Extensions)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/11444/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2649/index.html)

<!-- MediaWiki page 2649; revision 11444; parent 11214; 2020-08-02T21:57:26Z -->
