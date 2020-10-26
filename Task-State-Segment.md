# Task State Segment

Das **Task State Segment** (kurz TSS) wird von der CPU benötigt, um Informationen über einen Task zu speichern. Eigentlich vor allem für [Hardware-Multitasking](https://github.com/lowlevel-eu/wiki/wiki/Hardware-Multitasking "Hardware-Multitasking") verwendet, benötigt man es jedoch auch für Software-Multitasking, um der CPU im Falle eines Ringwechsels von einem niedriger privilegierten [Ring](https://github.com/lowlevel-eu/wiki/wiki/Ring "Ring") in einen höheren einen Stack zu übergeben. Um ein TSS benutzen zu können, legt man einen entsprechenden Deskriptor in der GDT an, der darauf zeigt. Der Selektor dieses Deskriptors muss dann mit *ltr \<Selektor\>* ins Taskregister der CPU geladen werden.

  

### Aufbau &#150; TSS-Deskriptor

**Task State Segment Deskriptor**

| 31-24 | 23 | 22-21 | 20 | 19-16 | 15 | 14-13 | 12 | 11-8 | 7-0 |
| -------------------- | ----- | ------- | ----- | ------------- | ----- | ------- | ----- | ------ | -------------------- |
| Basisadresse 31-24 | G | 0 | AVL | Limit 19-16 | P | DPL | 0 | Type | Basisadresse 16-23 |

| 31-16 | 15-0 |
| ------------------- | ------------ |
| Basisadresse 15-0 | Limit 15-0 |

- *Type* (Deskriptortyp) - Hier muss als Wert 1001b eingetragen werden. Die hintere Null wird zusätzlich als Busy-Flag verwendet. Dieses wird auf 1 gesetzt, sobald der Task in das System geladen ist und gestartet wurde. Tasks sind nicht wiedereintrittsfähig. Das heißt, sie dürfen sich nicht selbst aufrufen. Dies wird mit dem Busy-Flag verhindert.

## Aufbau TSS

**Aufbau &#150; Task State Segment**

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

Man kann die Felder des TSS in zwei Kategorien einteilen:

1.  **Statische Felder** werden einmal mit Werten belegt und dann jeweils beim Taskwechsel von der CPU in die entsprechenden Register geladen, aber niemals automatisch verändert. Zu den statischen Feldern zählen IOMap Base Address, LDT Segment Selektor, CR3, ESP0-2 und SS0-2. Das CR3-Feld muss nicht initialisiert werden, falls Paging nicht aktiv ist, ebenso der LDT Selektor, falls man keine LDTs verwendet. Mit der IOMap kann man bestimmte Ports maskieren, auf die der Task kein Zugriff haben soll. IOMap Base Address kann auf 0 gesetzt werden, wenn man diese Funktion der CPU nicht nutzen möchte.
2.  **Dynamische Felder** müssen auch initialisiert werden, werden dann aber beim Taskwechsel von der CPU immer mit den entsprechenden geänderten Registerwerten belegt. Zu den dynamischen Feldern gehören EAX bis EDX, CS bis GS/SS, EFLAGS, ESI/EDI/EBP/ESP und der Previous Task Link.

Auch wenn man Hardware-Multitasking nicht verwendet, muss mindestens ein TSS angelegt und dessen Selektor im Taskregister gespeichert worden sein. Die CPU lädt nämlich bei einem Ringwechsel einen neuen Stack, damit weniger privilegierte Software nicht höher privilegierte Software durch einen Stackfault zum Absturz bringt. Dafür lädt die CPU die Register ss0 (bzw ss1 oder ss2) sowie esp0 (bzw. esp1 oder esp2) als neuen Stack. Ein Stackwechsel wird ausgeführt, wenn ein Programm die Kontrolle an ein anderes durch ein [Interrupt](https://github.com/lowlevel-eu/wiki/wiki/Interrupt "Interrupt"), Call Gate oder Task Gate abgibt.

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/11527/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1599/index.html)

<!-- MediaWiki page 1599; revision 11527; parent 9428; 2020-10-26T16:15:21Z -->
