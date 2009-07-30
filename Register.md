# Register

Diese Seite ist ein Artikel, welcher **mehr** haben könnte..  

Wenn du mehr darüber weißt oder recherchieren willst, bist **du** aufgerufen, dies zu tun. Wenn du dir in einer Sache nicht sicher bist, dann stell es auf die Diskussionsseite.

## x86 CPU Register

| Bits | Register |
| ------ | -------------------------------------------------------- |
| 8 | AL, BL, CL, DL, AH, BH, CH, DH |
| 16 | AX, BX, CX, DX, DI, SI, BP, SP, CS, DS, ES, FS, GS, SS |
| 32 | EAX, EBX, ECX, EDX, EDI, ESI, EBP, ESP, EIP, EFLAGS |
| 80 |  |
| 128 | XMM0, XMM1, XMM2, XMM3, XMM4, XMM5, XMM6, XMM7 |

## x86-64 CPU Register

### Allzweckregister

| Bytes |  |  |  |  |  |  |  |
| ------- | ----- | ----- | ----- | ----- | ----- | ------ | ----- |
| 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| R?X |  |  |  |  |  |  |  |
|  |  |  |  | E?X |  |  |  |
|  |  |  |  |  |  | ?X |  |
|  |  |  |  |  |  | ?H\* | ?L |

? = A, B, C, D

- Diese Register sind nur in Funktion nutzbar, die KEINEN REX-Präfix benötigen!

| Bytes |  |  |  |  |  |  |  |
| ------- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| R? |  |  |  |  |  |  |  |
|  |  |  |  | R?D |  |  |  |
|  |  |  |  |  |  | R?W |  |
|  |  |  |  |  |  |  | R?L |

? = 8, 9, 10, 11, 12, 13, 14, 15

### Indexregister

| Bytes |  |  |  |  |  |  |  |
| ------- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| R?I |  |  |  |  |  |  |  |
|  |  |  |  | E?I |  |  |  |
|  |  |  |  |  |  | ?I |  |
|  |  |  |  |  |  |  | ?IL |

? = D, S

### Zeigerregister

| Bytes |  |  |  |  |  |  |  |
| ------- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| R?P |  |  |  |  |  |  |  |
|  |  |  |  | E?P |  |  |  |
|  |  |  |  |  |  | ?P |  |
|  |  |  |  |  |  |  | ?PL |

? = B, S

### Instruktionsregister

| Bytes |  |  |  |  |  |  |  |
| ------- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| RIP |  |  |  |  |  |  |  |
|  |  |  |  | EIP |  |  |  |
|  |  |  |  |  |  | IP |  |

### Flagregister

| Bytes |  |  |  |  |  |  |  |
| -------- | ----- | ----- | ----- | -------- | ----- | ----- | ----- |
| 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| RFLAGS |  |  |  |  |  |  |  |
|  |  |  |  | EFLAGS |  |  |  |

### Segmentregister

| Bytes |  |
| ------- | ----- |
| 1 | 0 |
| ?S |  |

? = C, D, E, F, G, S

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

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/4894/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1881/index.html)

<!-- MediaWiki page 1881; revision 4894; parent 4613; 2009-07-30T20:05:58Z -->
