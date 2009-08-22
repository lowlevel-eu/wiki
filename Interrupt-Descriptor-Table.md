# Interrupt Descriptor Table

**IDT** steht für **I**nterrupt **D**escriptor **T**able. Sie wird im [Protected Mode](https://github.com/lowlevel-eu/wiki/wiki/Protected-Mode "Protected Mode") des x86 verwendet, um [Interrupts](https://github.com/lowlevel-eu/wiki/wiki/Interrupt "Interrupt") ihre [Handler (ISRs)](https://github.com/lowlevel-eu/wiki/wiki/Interrupt-Service-Routine "ISR") zuzuordnen. Die Einträge in der Tabelle heißen *Interruptdeskriptoren*.

## Aufbau

Die IDT besteht aus einem Speicherbereich, in dem direkt aufeinanderfolgend die bis zu 256 Interruptdeskriptoren abgelegt sind (d.h. in Hochsprachen aus einem gepackten Array von 256 Deskriptoren). Für die Behandlung des Interrupt 0 wird der erste Eintrag der Tabelle benutzt, für Interrupt 1 der zweite usw.

### Descriptor

| 63-48 | 47 | 46-45 | 44 | 43 | 42-40 | 39-32 |
| -------------- | ----- | ------- | ----- | ----- | ------- | ---------- |
| Offset 31-16 | P | DPL | 0 | D | Typ | 00000000 |

| 31-16 | 15-0 |
| ---------- | ------------- |
| Selector | Offset 15-0 |

- *Selector* gibt den Selector des Codesegments an, in das beim Auftreten des Interrupts gewechselt werden soll. Im Allgemeinen ist dies das Kernel-Codesegment (Ring 0).
- *Offset*: Gibt das Offset des ISR innerhalb des Segments an. Wenn der entsprechende Interrupt auftritt, wird eip auf diesen Wert gesetzt.
- Das ***P***resent flag gibt an, ob dieser Eintrag benutzt wird.
- *DPL* gibt das Descriptor Privilege Level an, das man braucht um diesen Interrupt aufrufen zu dürfen.
- *D* gibt an, ob es sich um ein 32bit- (1) oder um ein 16bit-Segment (0) handelt.
- *Typ* gibt die Art des Interrupts an:

| Wert | Bedeutung |
| ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 110b | **Interrupt Gate** - Beim Springen in den Interrupthandler wird eflags.if = 0 gesetzt, d.h. Hardwareinterrupts werden deaktiviert, solange der Handler läuft |
| 111b | **Trap Gate** - Beim Sprung in den Interrupthandler bleiben Hardwareinerrupts aktiviert |
| 101b | **Task Gate** - Beim Auftreten des Interrupts wird ein Hardware-Taskswitch durchgeführt. Der Selector zeigt in diesem Fall nicht auf ein Codesegment, sondern auf ein [TSS](https://github.com/lowlevel-eu/wiki/wiki/Task-State-Segment "TSS"). Das Offset bleibt unbenutzt. |

## Laden einer IDT

Zum Laden einer IDT muss die Instruktion *lidt \<p\>* mit der Adresse einer 6 Bytes großen Datenstruktur aufgerufen werden. Die Datenstruktur sieht folgendermaßen aus:

| 47-16 | 15-0 |
| ------------------------ | --------------- |
| Anfangsadresse der IDT | Limit der IDT |

Die Anfangsadresse (Basis) ist die [lineare Adresse](https://github.com/lowlevel-eu/wiki/wiki/Paging "Lineare Adresse") des ersten Eintrags in der IDT und das Limit ist die Größe der IDT verringert um 1.

Damit kann eine IDT beispielsweise mit Code wie dem folgenden geladen werden:

\<c\>static long long unsigned int idt\[IDT_ENTRIES\];

// ...

struct {

       unsigned short int limit;
       void* pointer;

} \_\_attribute\_\_((packed)) idtp = {

       .limit = IDT_ENTRIES * 8 - 1,
       .pointer = idt,

}; asm volatile("lidt %0" : : "m" (idtp));\</c\>

Oder in Assembler: \<asm\>lidt \[idtr\]

...

idtr:

       dw IDT_ENTRIES * 8 - 1,
       dd idt

idt:

       ...</asm>

## Siehe auch

- [Interrupt](https://github.com/lowlevel-eu/wiki/wiki/Interrupt "Interrupt")
- [Exception](https://github.com/lowlevel-eu/wiki/wiki/Exception "Exception")
- [Programmable Interrupt Controller](https://github.com/lowlevel-eu/wiki/wiki/Programmable-Interrupt-Controller "Programmable Interrupt Controller")
- [Bran's Kernel-Development Tutorial ... IDT](http://www.osdever.net/bkerndev/Docs/idt.htm)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/5702/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1603/index.html)

<!-- MediaWiki page 1603; revision 5702; parent 4704; 2009-08-22T13:00:36Z -->
