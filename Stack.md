# Stack

Der Stack (=Kellerspeicher oder Stapel) ist eine der wichtigsten Datenstrukturen sowohl für Software als auch Hardware, da dieser u. a. Parameter und Rücksprungadressen speichert.

### Funktionsweise

Der Stack arbeitet nach dem LIFO-Prinzip ("Last in, first out"). Das bedeutet, dass neue Elemente immer oben auf den Stack gelegt werden, sodass das zuletzt auf den Stack gelegte Element auch das zuerst wieder zurück geholte ist. Dabei kann man bei jedem Stack zwei Grundoperationen ausführen:

- **push** legt ein neues Element oben auf den Stack
- **pop** holt das oberste Element vom Stack

### Implementierung durch die CPU

Die CPU bietet zwei Register zum Arbeiten mit dem Stack:

- **das SS-Register** speichert das Stacksegment (im [Real Mode](https://github.com/lowlevel-eu/wiki/wiki/Real-Mode "Real Mode")) bzw. den Stackselektor (im [Protected Mode](https://github.com/lowlevel-eu/wiki/wiki/Protected-Mode "Protected Mode")).
- **das ESP-Register** (=StackPointer) zeigt auf das oberste Element des aktuellen Stacks. Die [Real-Mode](https://github.com/lowlevel-eu/wiki/wiki/Real-Mode "Real Mode")-Variante dieses Registers ist das SP-Register.

Zudem sind die Befehle PUSH und POP in die CPU integriert. Dabei ist zu beachten, **dass der Stack von den höheren zu den niedrigeren Adressen wächst**.

- Der PUSH-Befehl vermindert den Wert von ESP um die Größe des Operanden und schreibt diesen an die Stelle, auf die das Register dann zeigt
- Der POP-Befehl liest das Element, auf das ESP zeigt und erhöht das Register um die Operandengröße.

Das bedeutet, dass der Stack seine maximale Größe erreicht hat, wenn der Wert 0 im ESP-Register steht. In diesem Fall wird ein [Stackfault](https://github.com/lowlevel-eu/wiki/wiki/Exception#liste-der-exceptions "Exception") ausgelöst.

### Das EPB-Register

Zur Verwendung des Stacks bietet die CPU noch ein EBP-Register (=Base Pointer). Dieses wird von vielen Hochsprachen verwendet, um lokale Variablen auf dem Stack zu speichern.

### Befehle, die sich auf den Stack auswirken

| Befehl | Beschreibung |
| --------------------- | --------------------------------------------------------------------------------------------- |
| push *operand* | schreibt den Operanden auf den Stack |
| pop *operand* | liest das oberste Element vom Stack in den Operanden |
| pushf | schreibt das EFLAGS-Register auf den Stack |
| popf | liest das EFLAGS-Register vom Stack |
| pusha | legt alle "allgemeinen" Register (EAX, ECX, EDX, EBX, ESP, EBP, ESI, EDI) auf den Stack |
| popa | Holt diese Register wieder vom Stack, wobei ESP übersprungen wird |
| call (far) | Legt CS und EIP auf den Stack |
| retf | Lädt diese Register wieder, um zur aufrufenden Codestelle zurückzukehren |
| call | Legt EIP auf den Stack |
| ret | Lädt EIP vom Stack, um zur aufrufenden Codestelle zurückzukehren |
| int | Legt SS, ESP (beide nur bei Ringwechsel), EFLAGS, CS, EIP auf den Stack |
| iret | Lädt diese Register wieder, um zur aufrufenden Codestelle zurückzukehren |
| sysenter / sysleave | siehe [Sysenter](https://github.com/lowlevel-eu/wiki/wiki/Sysenter "Sysenter") |
| syscall / sysret |  |
| enter / leave | siehe [Enter / Leave](https://github.com/lowlevel-eu/wiki/wiki/Enter-Leave "Enter / Leave") |

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/9010/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2165/index.html)

<!-- MediaWiki page 2165; revision 9010; parent 7091; 2010-11-28T13:29:57Z -->
