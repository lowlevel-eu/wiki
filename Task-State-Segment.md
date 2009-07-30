# Task State Segment

Das **Task State Segment** (kurz TSS) wird von der CPU benötigt, um bei einen Ringwechsel den richtigen [Stack](https://github.com/lowlevel-eu/wiki/wiki/Stack "Stack") zu laden. Man kann das TSS auch benutzen, um Hardware-[Multitasking](https://github.com/lowlevel-eu/wiki/wiki/Multitasking "Multitasking") zu realisieren. Dafür wird der TSS-Deskriptor mit einem Longjump angesprungen. Dabei werden auch andere Register (wie EIP) geladen. Um ein TSS für den Ringwechsel benutzen zu können, muss es vorher mit *ltr \<Selektor\>* geladen werden.

## Aufbau - Task State Segment

| Offset | 31-16 | 0-15 |
| -------- | ---------------------- | ---------------------- |
| 0x00 |  | Previous Task Link |
| 0x04 | ESP0 |  |
| 0x08 |  | SS0 |
| 0x0C | ESP1 |  |
| 0x10 |  | SS1 |
| 0x14 | ESP2 |  |
| 0x18 |  | SS2 |
| 0x1C | CR3 |  |
| 0x20 | EIP |  |
| 0x24 | EFLAGS |  |
| 0x28 | EAX |  |
| 0x2C | ECX |  |
| 0x30 | EDX |  |
| 0x34 | EBX |  |
| 0x38 | ESP |  |
| 0x3C | EBP |  |
| 0x40 | ESI |  |
| 0x44 | EDI |  |
| 0x48 |  | ES |
| 0x4C |  | CS |
| 0x50 |  | SS |
| 0x54 |  | DS |
| 0x58 |  | FS |
| 0x5C |  | GS |
| 0x60 |  | LDT Segment Selektor |
| 0x64 | I/O Map Base Address |  |

## Aufbau - TSS-Deskriptor

**Task State Segment Deskriptor (BITs) Teil 1**

| **31 - 24** | **23** | **21 - 22** | **20** | **19 - 16** | **15** | **13 - 14** | **12** | **11 - 8** | **0 - 7** |
| -------------------- | -------- | ------------- | -------- | ------------- | -------- | ------------- | -------- | ------------ | -------------------- |
| Basisadresse 31-24 | G | 0 | AVL | Größe 19-16 | P | DPL | 0 | Type | Basisadresse 16-23 |

**Task State Segment Deskriptor (BITs) Teil 2**

| **31 - 24** | **16 - 0** |
| --------------------- | -------------- |
| Basisadresse 15 - 0 | Größe 15 - 0 |

### Type = Deskriptor Typ

Hier muss als Wert 1001b eingetragen werden. Die hintere Null wird zusätzlich als Busy-Flag verwendet. Dies wird auf 1 gesetzt, sobald der Task in das System geladen ist und gestartet wurde. Tasks sind nicht redundant. Das heißt, sie dürfen sich nicht selbst aufrufen. Dies wird mit dem Busy-Flag verhindert.

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/4830/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1599/index.html)

<!-- MediaWiki page 1599; revision 4830; parent 3221; 2009-07-30T01:46:08Z -->
