# Register

Diese Seite ist ein Artikel, welcher **mehr** haben könnte..  

Wenn du mehr darüber weißt oder recherchieren willst, bist **du** aufgerufen, dies zu tun. Wenn du dir in einer Sache nicht sicher bist, dann stell es auf die Diskussionsseite.

## x86 CPU Register

### Übersicht

| Bits | Register |
| --------- | -------------------------------------------------------- |
| **8** | AL, BL, CL, DL, AH, BH, CH, DH |
| **16** | AX, BX, CX, DX, DI, SI, BP, SP, CS, DS, ES, FS, GS, SS |
| **32** | EAX, EBX, ECX, EDX, EDI, ESI, EBP, ESP, EIP, EFLAGS |
| **128** | XMM0, XMM1, XMM2, XMM3, XMM4, XMM5, XMM6, XMM7 |

### Allzweckregister

| Bytes |  |  |  |
| ------- | ----- | ----- | ----- |
| 3 | 2 | 1 | 0 |
| E?X |  |  |  |
|  |  | ?X |  |
|  |  | ?H | ?L |

? = A, B, C, D

Die Allzweckregister können, wie ihr Name schon andeutet eigentlich für fast jeden Zweck genutzt werden. Trotzdem gibt es einige gebräuchliche Nutzungen, zum Beispiel

- **EAX** : Für Rechenoperatioen, als Rückgabewert in [C](https://github.com/lowlevel-eu/wiki/wiki/C "C")
- **ECX** : Als Zähler

### Indexregister

| Bytes |  |  |  |
| ------- | ----- | ----- | ----- |
| 3 | 2 | 1 | 0 |
| E?I |  |  |  |
|  |  | ?I |  |

? = D, S

Die Indexregister werden oft als Indexe in Datenbereichen verwendet. Dabei zeigt

- **ESI** : Auf den Quelloperanden
- **EDI** : Auf den Zieloperanden

### Zeigerregister

| Bytes |  |  |  |
| ------- | ----- | ----- | ----- |
| 3 | 2 | 1 | 0 |
| E?P |  |  |  |
|  |  | ?P |  |

? = B, S

Die Zeigerregister werden genutzt, um auf Stellen im Speicher zu zeigen.

- **ESP** : Zeigt *immer* auf den aktuellen Stack
- **EBP** : Wird meistens für Stackframes und lokale Variablen bei Funktionsaufrufen verwendet

### Instruktionsregister

| Bytes |  |  |  |
| ------- | ----- | ----- | ----- |
| 3 | 2 | 1 | 0 |
| EIP |  |  |  |
|  |  | IP |  |

Das Instruktionsregister **EIP** zeigt *immer* auf den nächsten auszuführenden Befehl. Es kann nicht direkt geändert werden, sondern nur über Funktion wie **jmp**, **call** oder **ret**

### Flagregister

→ *Hauptartikel: [EFLAGS](https://github.com/lowlevel-eu/wiki/wiki/EFLAGS "EFLAGS")*

| Bytes |  |  |  |
| ------- | ----- | ----- | ----- |
| 3 | 2 | 1 | 0 |

EFLAGS

Das Flagregister **EFLAGS** speichert einige Konfigurationsmöglichkeiten und Systemzuständen, beispielweise, ob Interrupts gerade erlaubt sind oder ob ein Übertrag bei einer Addition stattfand.

### Segmentregister

| Bytes |  |
| ------- | ----- |
| 1 | 0 |
| ?S |  |

? = C, D, E, F, G, S

Die Segmentregister geben die Basisadresse des aktuellen Segments an. Dabei steht

- **CS** für das *Code-Segment*
- **DS** für das *Data-Segment*
- **SS** für das *Stack-Segment*

**ES**, **FS** und **GS** sind zusätzliche Daten-Segmente.

Die Segmentregister sind im [Protected Mode](https://github.com/lowlevel-eu/wiki/wiki/Protected-Mode "Protected Mode") auch für die Segmentierung mit Hilfe der [GDT](https://github.com/lowlevel-eu/wiki/wiki/Global-Descriptor-Table "GDT") verantwortlich.

  

## x86-64 CPU Register

### Übersicht

| Bits | Register |
| --------- | ------------------------------------------------------------------------------------------------------ |
| **8** | AL, BL, CL, DL, DIL, SIL, BPL, SPL, R8L, R9L, R10L, R11L, R12L, R13L, R14L, R15L |
| **16** | AX, BX, CX, DX, DI, SI, BP, SP, CS, DS, ES, FS, GS, SS, R8W, R9W, R10W, R11W, R12W, R13W, R14W, R15W |
| **32** | EAX, EBX, ECX, EDX, EDI, ESI, EBP, ESP, EIP, EFLAGS, R8D, R9D, R10D, R11D, R12D, R13D, R14D, R15D |
| **64** | RAX, RBX, RCX, RDX, RDI, RSI, RBP, RSP, RIP, RFLAGS, R8, R9, R10, R11, R12, R13, R14, R15 |
| **128** | XMM0, XMM1, XMM2, XMM3, XMM4, XMM5, XMM6, XMM7, XMM8, XMM9, XMM10, XMM11, XMM12, XMM13, XMM14, XMM15 |

### Allzweckregister

| Bytes |  |  |  |  |  |  |  |
| ------- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| R?X |  |  |  |  |  |  |  |
|  |  |  |  | E?X |  |  |  |
|  |  |  |  |  |  | ?X |  |
|  |  |  |  |  |  | ?H | ?L |

? = A, B, C, D

| Bytes |  |  |  |  |  |  |  |
| ------- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| R? |  |  |  |  |  |  |  |
|  |  |  |  | R?D |  |  |  |
|  |  |  |  |  |  | R?W |  |
|  |  |  |  |  |  |  | R?B |

? = 8, 9, 10, 11, 12, 13, 14, 15

**Achtung!**

*Die **?H**-Register sind nur in Funktion nutzbar, die **keinen** REX-Präfix benutzen!*  
*Die **R?B** Register heißen in manchen Compilern oder Assemblern **R?L***

Die Allzweckregister können, wie ihr Name schon andeutet eigentlich für fast jeden Zweck genutzt werden. Trotzdem gibt es einige gebräuchliche Nutzungen, zum Beispiel

- **RAX** : Für Rechenoperatioen, als Rückgabewert in [C](https://github.com/lowlevel-eu/wiki/wiki/C "C")
- **RCX** : Als Zähler

### Indexregister

| Bytes |  |  |  |  |  |  |  |
| ------- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| R?I |  |  |  |  |  |  |  |
|  |  |  |  | E?I |  |  |  |
|  |  |  |  |  |  | ?I |  |
|  |  |  |  |  |  |  | ?IL |

? = D, S

**Achtung!**

*Die **?IL**-Register sind nur in Funktion nutzbar, die einen REX-Präfix **benutzen**!*

Die Indexregister werden oft als Indexe in Datenbereichen verwendet. Dabei zeigt

- **RSI** : Auf den Quelloperanden
- **RDI** : Auf den Zieloperanden

### Zeigerregister

| Bytes |  |  |  |  |  |  |  |
| ------- | ----- | ----- | ----- | ----- | ----- | ----- | ------- |
| 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| R?P |  |  |  |  |  |  |  |
|  |  |  |  | E?P |  |  |  |
|  |  |  |  |  |  | ?P |  |
|  |  |  |  |  |  |  | ?PL\* |

? = B, S

**Achtung!**

*Die **?PL**-Register sind nur in Funktion nutzbar, die einen REX-Präfix **benutzen**!*

Die Zeigerregister werden genutzt, um auf Stellen im Speicher zu zeigen.

- **RSP** : Zeigt *immer* auf den aktuellen Stack
- **RBP** : Wird meistens für Stackframes und lokale Variablen bei Funktionsaufrufen verwendet

### Instruktionsregister

| Bytes |  |  |  |  |  |  |  |
| ------- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| RIP |  |  |  |  |  |  |  |
|  |  |  |  | EIP |  |  |  |
|  |  |  |  |  |  | IP |  |

Das Instruktionsregister **RIP** zeigt *immer* auf den nächsten auszuführenden Befehl. Es kann nicht direkt geändert werden, sondern nur über Funktion wie **jmp**, **call** oder **ret**

### Flagregister

→ *Hauptartikel: [RFLAGS](https://github.com/lowlevel-eu/wiki/wiki/EFLAGS#rflags "RFLAGS")*

| Bytes |  |  |  |  |  |  |  |
| -------- | ----- | ----- | ----- | -------- | ----- | ----- | ----- |
| 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| RFLAGS |  |  |  |  |  |  |  |
|  |  |  |  | EFLAGS |  |  |  |

Das Flagregister **RFLAGS** speichert einige Konfigurationsmöglichkeiten und Systemzuständen, beispielweise, ob Interrupts gerade erlaubt sind oder ob ein Übertrag bei einer Addition stattfand.

### Segmentregister

| Bytes |  |
| ------- | ----- |
| 1 | 0 |
| ?S |  |

? = C, D, E, F, G, S

  
Die Segmentregister geben die Basisadresse des aktuellen Segments an. Dabei steht

- **CS** für das *Code-Segment*
- **DS** für das *Data-Segment*
- **SS** für das *Stack-Segment*

**ES**, **FS** und **GS** sind zusätzliche Daten-Segmente.

Die Segmentregister sind im [Long Mode](https://github.com/lowlevel-eu/wiki/wiki/Long-Mode "Long Mode") auch für die Segmentierung mit Hilfe der [GDT](https://github.com/lowlevel-eu/wiki/wiki/Global-Descriptor-Table "GDT") verantwortlich.

**Achtung!**

Im [Long Mode](https://github.com/lowlevel-eu/wiki/wiki/Long-Mode "Long Mode") werden viele Bits der [GDT](https://github.com/lowlevel-eu/wiki/wiki/Global-Descriptor-Table "GDT")-Einträge **ignoriert**!

### SSE-Register

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

### Floatingpointregister

<table>
<tbody><tr>
<th colspan="10">Bytes
</th></tr>
<tr>
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
<td colspan="10">ST?
</td></tr>
<tr>
<td colspan="10">? = 0, 1, 2, 3, 4, 5, 6, 7
</td></tr></tbody></table> <table>
<tbody><tr>
<th colspan="16">Bits
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
<td colspan="16">Control Register
</td></tr></tbody></table>

  

<table>
<tbody><tr>
<th colspan="16">Bits
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
<td colspan="16">Status Register
</td></tr></tbody></table>

  

<table>
<tbody><tr>
<th colspan="16">Bits
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
<td colspan="16">Tag Register
</td></tr></tbody></table> <table>
<tbody><tr>
<th colspan="10">Bits
</th></tr>
<tr>
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
<td colspan="10">FOP
</td></tr></tbody></table>

## Siehe auch

- [Control Register](https://github.com/lowlevel-eu/wiki/wiki/Control-Register "Control Register")

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/6013/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1881/index.html)

<!-- MediaWiki page 1881; revision 6013; parent 6006; 2009-10-12T12:03:58Z -->
