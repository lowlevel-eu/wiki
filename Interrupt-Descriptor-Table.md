# Interrupt Descriptor Table

**IDT** steht für **I**nterrupt **D**escriptor **T**able. Sie wird im [Protected Mode](https://github.com/lowlevel-eu/wiki/wiki/Protected-Mode "Protected Mode") und im [Long Mode](https://github.com/lowlevel-eu/wiki/wiki/Long-Mode "Long Mode") des x86 verwendet, um [Interrupts](https://github.com/lowlevel-eu/wiki/wiki/Interrupt "Interrupt") ihre [Handler (ISRs)](https://github.com/lowlevel-eu/wiki/wiki/Interrupt-Service-Routine "ISR") zuzuordnen. Die Einträge in der Tabelle heißen *Interruptdeskriptoren*.

## Aufbau

Die IDT besteht aus einem Speicherbereich, in dem direkt aufeinanderfolgend die bis zu 256 Interruptdeskriptoren abgelegt sind (d.h. in Hochsprachen aus einem gepackten Array von 256 Deskriptoren). Für die Behandlung des Interrupt 0 wird der erste Eintrag der Tabelle benutzt, für Interrupt 1 der zweite usw.

Die Tabelle kann weniger als 256 Einträge haben. Wenn einer der Interrupts ausgelöst wird, die dadurch nicht von der IDT beschrieben sind und deren Interrupthandler folglich nicht aufgerufen werden kann, wird stattdessen ein \#GP (General Protection Fault, siehe [Exception](https://github.com/lowlevel-eu/wiki/wiki/Exception "Exception")) ausgelöst.

### Deskriptor

Ein Deskriptor in der IDT ist im Protected Mode 64 Bit und im Long Mode 128 Bit lang. Die in der Tabelle grau hinterlegten Einträge gelten nur für den Long Mode.

| Bits | Name | Beschreibung |
| -------- | ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0-15 | Offset 0-15 | Gibt das Offset des ISR innerhalb des Segments an. Wenn der entsprechende Interrupt auftritt, wird eip auf diesen Wert gesetzt. |
| 16-31 | Selector | Gibt den Selector des Codesegments an, in das beim Auftreten des Interrupts gewechselt werden soll. Im Allgemeinen ist dies das Kernel-Codesegment (Ring 0). |
| 32-34 | 000 / IST | Gibt im LM den Index in die IST an, **ansonsten 0**! |
| 35-39 | Reserviert | Wird ignoriert |
| 40-42 | Typ | Gibt die Art des Interrupts an |
| 43 | D | Gibt an, ob es sich um ein 32bit- (1) oder um ein 16bit-Segment (0) handelt. |
| 43 | D | Im LM: Für 64-Bit LDT 0, **ansonsten 1** |
| 44 | 0 |  |
| 45-46 | DPL | Gibt das Descriptor Privilege Level an, das man braucht um diesen Interrupt aufrufen zu dürfen. |
| 47 | P | Gibt an, ob dieser Eintrag benutzt wird. |
| 48-63 | Offset 16-31 |  |
| 64-95 | Offset 32-63 | (Nur im Long Mode, **im Protected Mode hat der Deskriptor nur 64 Bit**!) |
| 96-127 | Reserviert (0) | (Nur im Long Mode, **im Protected Mode hat der Deskriptor nur 64 Bit**!) |

### Interrupt-Arten (Typ)

| Wert | Bedeutung |
| ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 110b | **Interrupt Gate** - Beim Springen in den Interrupthandler wird eflags.if = 0 gesetzt, d.h. Hardwareinterrupts werden deaktiviert, solange der Handler läuft |
| 111b | **Trap Gate** - Beim Sprung in den Interrupthandler bleiben Hardwareinerrupts aktiviert |
| 101b | **Task Gate** - Beim Auftreten des Interrupts wird ein Hardware-Taskswitch durchgeführt. Der Selector zeigt in diesem Fall nicht auf ein Codesegment, sondern auf ein [TSS](https://github.com/lowlevel-eu/wiki/wiki/Task-State-Segment "TSS"). Das Offset bleibt unbenutzt. |

## Laden einer IDT

Zum Laden einer IDT muss die Instruktion *lidt \<p\>* mit der Adresse einer 6 Bytes großen Datenstruktur aufgerufen werden. Die Datenstruktur sieht folgendermaßen aus:

| Offset | Bedeutung |
| -------- | ------------------- |
| 0-15 | Das Limit der IDT |
| 16-47 | Die Base der IDT |

Die Anfangsadresse (Basis) ist die [lineare Adresse](https://github.com/lowlevel-eu/wiki/wiki/Paging "Lineare Adresse") des ersten Eintrags in der IDT und das Limit ist die Größe der IDT verringert um 1.

Damit kann eine IDT beispielsweise mit Code wie dem folgenden geladen werden:

\<c\>static uint64_t idt\[IDT_ENTRIES\];

// ...

struct {

       uint16_t limit;
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

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/11013/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1603/index.html)

<!-- MediaWiki page 1603; revision 11013; parent 10962; 2013-03-01T11:36:54Z -->
