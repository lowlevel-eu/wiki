# Interrupt Descriptor Table

**IDT** steht für **I**nterrupt **D**escriptor **T**able. Sie wird im [Protected Mode](https://github.com/lowlevel-eu/wiki/wiki/Protected-Mode "Protected Mode") des x86 verwendet, um Interrupts ihre [Handler (ISRs)](https://github.com/lowlevel-eu/wiki/wiki/Interrupt-Service-Routine "ISR") zuzuordnen. Die Einträge in der Tabelle heißen *Interruptdeskriptoren*.

## Aufbau

Die IDT kann maximal 256 Interruptdeskriptoren beinhalten, da es nur 256 Interrupts gibt. Ein Interruptdeskriptor in der IDT ist 8 Byte groß und sieht folgendermaßen aus:

| 63-48 | 47 | 46-45 | 44 | 43 | 42-40 | 39-32 | 31-16 | 15-0 |
| -------------- | --------- | ------- | ----- | ----- | ------------ | ------- | ---------- | ------------- |
| Offset 31-16 | Present | DPL | 0 | D | Typ (110b) | 0 | Selektor | Offset 0-15 |

Die IDT besteht aus einem Speicherbereich, in dem direkt aufeinanderfolgend die bis zu 256 Interruptdeskriptoren abgelegt sind (d.h. in Hochsprachen aus einem gepackten Array von 256 Deskriptoren). Für die Behandlung des Interrupt 0 wird der erste Eintrag der Tabelle benutzt, für Interrupt 1 der zweite usw.

### Offset

Gibt das Offset des ISR innerhalb des Segments an. Wenn der entsprechende Interrupt auftritt, wird eip auf diesen Wert gesetzt.

### Present

Gibt an, ob dieser Eintrag benutzt wird.

### DPL

Gibt das Descriptor Privilege Level an, das man braucht um diesen Interrupt aufrufen zu dürfen.

### D

Gibt an, ob es sich um ein 32bit- (1b) oder um ein 16bit-Segment (0b) handelt.

### Typ

| Wert | Bedeutung |
| ------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 110b | **Interrupt Gate** - Beim Springen in den Interrupthandler wird eflags.if = 0 gesetzt, d.h. Hardwareinterrupts werden deaktiviert, solange der Handler läuft |
| 111b | **Trap Gate** - Beim Sprung in den Interrupthandler bleiben Hardwareinerrupts aktiviert |
| 101b | **Task Gate** - Beim Auftreten des Hardwareinterrupts wird ein Hardware-Taskswitch durchgeführt. Der Selektor zeigt in diesem Fall nicht auf ein Codesegment, sondern auf ein [TSS](https://github.com/lowlevel-eu/wiki/wiki/Task-State-Segment "TSS"). Das Offset bleibt unbenutzt. |

### Selektor

Gibt den Selektor des Codesegments an, in das beim Auftreten des Interrupts gewechselt werden soll. Im Allgemeinen ist das das Kernel-Codesegment (Ring 0).

## Laden einer IDT

Zum Laden einer IDT muss die Instruktion *lidt \<p\>* mit der Adresse einer 6 Bytes großen Datenstruktur aufgerufen werden. Die Datenstruktur sieht folgendermaßen aus:

| 47-32 | 31-0 |
| --------------- | ------------------------ |
| Größe der IDT | Anfangsadresse der IDT |

Damit kann eine IDT beispielsweise mit Code wie dem folgenden geladen werden:

\<c\>static long long unsigned int idt\[IDT_ENTRIES\];

// ...

struct {

       unsigned short int length;
       void* pointer;

} \_\_attribute\_\_((packed)) idtp = {

       .length = IDT_ENTRIES * 8,
       .pointer = idt,

}; asm volatile("lidt %0" : : "m" (idtp));\</c\>

## Siehe auch

- [Interrupt](https://github.com/lowlevel-eu/wiki/wiki/Interrupt "Interrupt")
- [Exception](https://github.com/lowlevel-eu/wiki/wiki/Exception "Exception")
- [Programmable Interrupt Controller](https://github.com/lowlevel-eu/wiki/wiki/Programmable-Interrupt-Controller "Programmable Interrupt Controller")
- [Bran's Kernel-Development Tutorial ... IDT](http://www.osdever.net/bkerndev/Docs/idt.htm)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/4601/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1603/index.html)

<!-- MediaWiki page 1603; revision 4601; parent 4239; 2009-07-09T20:32:38Z -->
