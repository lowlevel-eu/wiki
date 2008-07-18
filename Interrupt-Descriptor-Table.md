# Interrupt Descriptor Table

**IDT** steht für **I**nterrupt **D**escriptor **T**able. Sie wird verwendet um Interrupts [ISRs](https://github.com/lowlevel-eu/wiki/wiki/Interrupt-Service-Routine "ISR") zuzuordnen. Die Einträge heißen Interrupt Gates

## Aufbau

Die IDT kann maximal 256 Interruptgates beinhalten, da es nur 256 Interrupts gibt. Ein Interruptgate in der IDT ist 8 Byte groß und sieht folgendermaßen aus:

| 63-48 | 47 | 46-45 | 44 | 43 | 42-40 | 39-32 | 31-16 | 15-0 |
| -------------- | --------- | ------- | ----- | ----- | ------------- | ------- | ---------- | ------------- |
| Offset 31-16 | Present | DPL | 0 | D | Type (110b) | 0 | Selektor | Offset 0-15 |

### Offset

Gibt das Offset des ISR innerhalb des Segments an.

### Present

Gibt an ob dieser Eintrag benutzt wird.

### DPL

Gibt das Descriptor Privilege Level an, das man brauch um diesen Interrupt aufrufen zu dürfen.

### D

Gibt an ob es sich um ein 32bit (1b) oder um ein 16bit (0b) Segment handelt.

### Type

Sollte bei einem Interruptgate immer 110b sein.

### Selektor

Gibt den Selektor an.

## Laden einer IDT

Zum Laden einer IDT muss die Instruktion *lidt \<p\>* mit der Adresse eines Selektors geladen werden. Dieser Selektor sind folgendermaßen aus:

| 47-32 | 31-0 |
| ---------------- | ----------------- |
| Größer der IDT | Adresse der IDT |

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/3029/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1603/index.html)

<!-- MediaWiki page 1603; revision 3029; parent 2796; 2008-07-18T12:35:35Z -->
