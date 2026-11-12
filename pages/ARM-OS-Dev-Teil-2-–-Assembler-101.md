# ARM-OS-Dev Teil 2 – Assembler 101

|  |  |  |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| « [ARM-OS-Dev Teil 1 – Entwicklungsumgebung](ARM-OS-Dev-Teil-1-%E2%80%93-Entwicklungsumgebung.md "ARM-OS-Dev Teil 1 – Entwicklungsumgebung") | **Navigation** | [ARM-OS-Dev Teil 3 – Trockenübungen](ARM-OS-Dev-Teil-3-%E2%80%93-Trocken%C3%BCbungen.md "ARM-OS-Dev Teil 3 – Trockenübungen") » |

## Ziel

Hier sollen Grundlagen der ARM-Assemblerprogrammierung vermittelt werden (nur ARM, nicht Thumb). Im weiteren Verlauf des Tutorials wird der Assemblerteil jedoch so klein wie möglich gehalten.

Im Gegensatz zu x86 gibt es für ARM nur eine Syntax. Wer sich unter x86 bereits einigermaßen mit Assembler auskennt, der sollte keine Probleme haben, ARM-Assembler zu verstehen. Insgesamt ähnelt die ARM-Syntax eher der Intel- als der AT&T-Syntax, was zum Beispiel die Reihenfolge der Operanden angeht (im Allgemeinen zuerst das Ziel, dann die Quelle(n), wobei es bei Speicherbefehlen auch anders sein kann).

## Begriffe

Eine Instruktion ist ein kompletter Prozessorbefehl, z. B. addiere 5 auf den Inhalt des Registers r0 (*add r0, \#5*). Mit Instruktion kann sowohl die Assemblerdarstellung als auch der Opcode gemeint sein.

- Der Opcode ist der binäre Maschinenbefehl, wie er vom Prozessor verstanden wird. Er wird meistens hexadezimal und byteweise geschrieben: e2 80 00 05 für unser Beispiel.
- Der Operand sind die Daten, auf denen der Maschinenbefehl arbeitet. Das ist zum einen die Zahl 5 und zum anderen das Register r0.
- Das Mnemonic ist der Assemblername eines Befehls, z. B. *add*.

## Operanden

Als Operanden für Assemblerbefehle kommen nur drei verschiedene Arten in Frage:

- Immediatewerte sind konstante Zahlen. Sie beginnen in Assembler mit *\#*, wie im obigen Beispiel das *\#5*.
- Prozessorregister sind der Platz, wo Daten, mit denen gearbeitet wird, normalerweise liegen. ARM hat 15 Allzweckregister, die jeweils 32 Bit groß sind. Die Register befinden sich direkt im Prozessor, so dass sie viel schneller sind als Zugriffe auf Arbeitsspeicher.
- Der Speicher ist schließlich, wo die meisten Daten liegen. Auf Speicher wird grundsätzlich über Adressen zugegriffen. Dabei gibt es folgende Möglichkeiten:
  - Indirekte Angabe über Register: *ldr r0, \[r1\]* liest die Adresse aus dem Register r1 und kopiert dann von dieser Adresse nach r0.
  - Indirekte Angabe mit Displacement: *ldr r0, \[r1, \#8\]* liest wieder die Adresse aus r1, zählt aber noch 8 dazu, bevor es die Adresse verwendet.
  - Es geht noch mehr: *ldr r0, \[r1, r2, lsl \#1\]* berechnet die Adresse als *r1 + r2 \<\< 1* (also *r1 + r2 \* 2*).

## Labels

S. [x86-Reihe](Teil-2-Assembler-101.md#labels "Teil 2 - Assembler 101") – allerdings wird bei ARM wie beschrieben kein *\$* für Immediates, sondern ein *\#* verwendet. Zudem ist es einfach ein Syntaxfehler, falls man dieses Zeichen vergessen sollte, da Speicheradressen immer von eckigen Klammern umschlossen werden.

## Daten

| Befehl | Erklärung |
| --------------------------- | ------------------------ |
| .byte 0xff | 8-Bit-Daten |
| .2byte 0xffff | 16-Bit-Daten |
| .4byte 0xffffffff | 32-Bit-Daten |
| .8byte 0xffffffffffffffff | 64-Bit-Daten |
| .space 256 | 256 Bytes freier Platz |

## Sektionen und Kommentare

S. [x86-Reihe](Teil-2-Assembler-101.md#sektionen "Teil 2 - Assembler 101").

## Register

Wie gesagt gibt es auf ARM 15 32-Bit-Allzweckregister, die von r0 bis r14 benannt sind. r15 ist theoretisch auch ein Allzweckregister, da man damit so gut wie alle Operationen vollführen kann, die auch mit den anderen 15 (r0 bis r14) möglich sind. Praktisch enthält r15 jedoch die Adresse des als nächsten auszuführenden Befehls (wenn man r15 liest, erhält man jedoch diesen Wert plus vier), sodass man darin keine Daten speichern kann. r13 wird im Allgemeinen als Stackpointer genutzt und r14 wird genutzt, um eine Rücksprungadresse von einer Funktion zu speichern. Der Befehl *bl* lädt so zum Beispiel den aktuellen Wert in r15 minus vier nach r14, sodass ein erneutes Laden von r15 mit r14 zur Stelle nach dem *bl* zurückkehrt.

Das Register r13 wird auch als sp (*Stack Pointer*) bezeichnet, r14 als lr (*Link Register*) und r15 als pc (*Program Counter*). Seltener werden r0 bis r3 als a1 bis a4, r4 bis r9 als v1 bis v6 (r9 manchmal auch als sb (*Stack Base*)), r10 als sl (*Stack Limit*), r11 als fp (*Frame Pointer*) und r12 als ip (*Inter-Procedure call scratch register*) bezeichnet. Dies hängt mit der ARM-Calling-Convention zusammen. r0 bis r3 werden zur Übergabe von Parametern an Funktionen verwendet und dürfen von den Funktionen frei verwendet werden; r4 bis r11 dürfen von einer Funktion nicht verändert werden; r12 ist wieder frei zur Benutzung (und r13 bis r15 haben spezielle Aufgaben).

Weiterhin gibt es noch das CPSR (*Current Program Status Register*), das Informationen zum aktuellen Prozessormodus und Flags enthält, die von arithmetisch-logischen Befehlen gesetzt werden. So setzt zum Beispiel der Befehl *adds* das Zero-Flag, wenn das Ergebnis der Addition 0 ist (Hinweis: Von vielen arithmetisch-logischen Befehlen gibt es zwei Versionen, eine, die die Flags setzt (*adds*) und eine, die sie unverändert lässt (*add*)). Neben dem CPSR gibt es noch das SPSR (*Saved PSR*), welches vom Prozessor verwendet wird, um bei Moduswechseln den Wert des CPSR zu sichern.

## Befehlssatz

Hier folgt nun ein ähnlicher Abriss des Befehlssatzes wie in der x86-Reihe. Auch hier seien nicht viele Worte zu den möglichen Operandenkombinationen verloren: Speicheroperanden sind nur bei Speicherbefehlen erlaubt, und dann auch nur ein Speicheroperand pro Befehl. Bei allen anderen Instruktionen müssen Register oder Immediatewerte verwendet werden. Pro Instruktion ist maximal ein Immediateoperand zulässig. Immediatewerte dürfen nur maximal acht gesetzte Bit nebeneinander besitzen (0x00FF0000 und 0x0003FC00 sind zulässig, 0x000003FF jedoch nicht).

### Zuweisungen und Stack

| Befehl | Erklärung |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| mov *Ziel, Quelle* | Kopiert den Wert von Quelle nach Ziel |
| ldr/ldrh/ldrb *Ziel, \[Quelle\]* | Lädt ein Word/Halfword/Byte aus dem Speicher (32/16/8 Bit) |
| str/strh/strb *Quelle, \[Ziel\]* | Schreibt ein Word/Halfword/Byte in den Speicher |
| push *{Registerliste}* | Legt den Wert auf den Stack; d. h. r13 wird um die Anzahl der Register in der Liste mal vier verringert und die Register werden so von der Stelle im Speicher an gespeichert, auf die r13 zeigt, dass niedrigere Register (r0) weiter unten als höhere Register (r14) liegen. |
| pop *{Registerliste}* | Holt den Wert vom Stack; d. h. die Register werden von der Stelle gelesen, auf die r13 zeigt und dann wird r13 um die Anzahl der Register mal vier erhöht. |

Hinweis: *push {}* und *pop {}* sind Aliasnamen für die Instruktionen *stmdb r13!,{}* und *ldmia r13!,{}*. Mit den *ldm*- und *stm*-Instruktionen (*Load/Store Multiple*) können mehrere Register hintereinander aus dem Speicher geladen oder hineingeschrieben werden. Der erste Operand gibt das Basisregister an, dessen Wert wird als Adresse verwendet. Nun gibt es folgende Varianten von *ldm* und *stm*: *xxxda* (*decrement after*), *xxxdb* (*decrement before*), *xxxia* (*increment after*) und *xxxib* (*increment before*). Bei *ib* wird die Adresse zuerst um vier erhöht, bei *db* um vier verringert. Dann wird ein Register an die Adresse geschrieben oder davon gelesen. Bei *ia* wird dann die Adresse um vier erhöht, bei *da* um vier verringert. Dies wird so lange getan, bis alle Register in den Speicher geschrieben oder von da gelesen wurden. Befindet sich hinter dem Basisregister im Befehl ein Ausrufezeichen, dann wird die am Ende resultierende Adresse ins Basisregister zurückgeschrieben.

Bei einem *push* wird r13 immer zuerst verringert und dann wird der Wert geschrieben, daher *stmdb* (*Store Multiple, Decrement Before*), bei *pop* wird zuerst der Wert gelesen und dann r13 erhöht: *ldmia* (*Load Multiple, Increment After*).

### Arithmetik

| Befehl | Erklärung |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| add *Ziel, Quelle 1, Quelle 2* | Addiert Quelle 1 und Quelle 2 und schreibt das Ergebnis nach Ziel |
| sub *Ziel, Quelle 1, Quelle 2* | Subtrahiert den Wert von Quelle 2 von Quelle 1 und speichert das Ergebnis in Ziel |
| rsb *Ziel, Quelle 1, Quelle 2* | Subtrahiert Quelle 1 von Quelle 2 und speichert das Ergebnis in Ziel (*rsb Ziel, Quelle, \#0* schreibt den negativen Wert von Quelle nach Ziel) |
| mul *Ziel, Quelle 1, Quelle 2* | Multipliziert Quelle 1 mit Quelle 2 und schreibt das Ergebnis nach Ziel |

### Bitoperationen

| Befehl | Erklärung |
| -------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| and *Ziel, Quelle 1, Quelle 2* | Berechnet das bitweise AND der Quellen |
| orr *Ziel, Quelle 1, Quelle 2* | Berechnet das bitweise OR der Quellen |
| eor *Ziel, Quelle 1, Quelle 2* | Berechnet das bitweise XOR (exklusives Oder) der Quellen |
| mvn *Ziel, Quelle* | Berechnet das bitweise NOT der Quelle |
| mov *Ziel, Quelle, lsl Anzahl* | Schiebt den Wert der Quelle um Anzahl Bits nach links. Rechts wird mit Nullen aufgefüllt. |
| mov *Ziel, Quelle, lsr Anzahl* | Schiebt den Wert der Quelle um Anzahl Bits nach rechts. Links wird mit Nullen aufgefüllt. |
| mov *Ziel, Quelle, asr Anzahl* | Schiebt den Wert der Quelle um Anzahl Bits nach rechts. Links wird mit dem höchsten Bit von Quelle aufgefüllt. |
| mov *Ziel, Quelle, ror Anzahl* | Rotiert den Wert der Quelle um Anzahl Bits nach rechts. Was rechts rausgeschoben wird, kommt links wieder rein. |

### Vergleiche und Sprünge

Um den Programmfluss zu steuern, gibt es in Assembler zwei Arten von Sprüngen. Die erste Art sind unbedingte Sprünge, sie entsprechen am ehesten einem *goto* in einer Hochsprache. Die zweite Art sind bedingte Sprünge, die benutzt werden, um ein *if* umzusetzen. Bedingte Sprünge führen den Sprung nur aus, wenn eine bestimmte Bedingung erfüllt ist. Die Bedingungen bestehen in einigen Bits im CPSR, die von vielen Befehlen automatisch gesetzt werden. Diese Bits sind:

- Das Zero Flag: Ist gesetzt, wenn der letzte geschriebene Wert Null war
- Das Carry Flag: Enthält den Übertrag bei vorzeichenlosen Operationen, wenn das Ergebnis zu groß ist, um vom Zieloperanden dargestellt werden zu können (bei Subtraktionen wird dieses Flag allerdings genau dann gesetzt, wenn *kein* Übertrag stattgefunden hat)
- Das Overflow Flag: Enthält den Übertrag bei vorzeichenbehafteten Operationen, wenn das Ergebnis zu groß oder zu klein ist, um vom Zieloperanden dargestellt werden zu können
- Das Negative Flag: Ist gesetzt, wenn des letzte Ergebnis negativ war

| Befehl | Erklärung |
| -------------------- | -------------------------------------------------------------------------------------------------------------------- |
| cmp *Ziel, Quelle* | Subtrahiert Quell von Ziel, ohne das Ergebnis zu speichern. Es werden nur die Flags angepasst. |
| tst *Ziel, Quelle* | Berechnet das bitweise AND von Quelle und Ziel, ohne das Ergebnis zu speichern. Es werden nur die Flags angepasst. |
| b *Sprungziel* | Springt zum Sprungziel. |
| bl *Sprungziel* | Legt die Adresse des nächsten Befehls nach r14 (*sub r14,r15,#4*) und springt zum Sprungziel (Funktionsaufruf). |
| b r14 | Holt die Rücksprungadresse aus r14 und springt dahin zurück (Rücksprung aus einer Funktion). |

Hinweis: Statt *b r14* wird häufig *bx r14* verwendet. Dies hat damit zu tun, dass bei Thumb-ARMs das niederwertigste Bit von r14 von *bl* gesetzt wird, wenn der Code im Thumbmodus ausgeführt wurde. *bx* liest dieses Bit und wechselt entsprechend in den Thumbmodus zurück, wenn es eins ist, sodass dann ein korrektes Zusammenarbeiten von Thumb- und ARM-Code möglich ist. Wenn man nur ARM-Code verwendet, kann man allerdings auch einfach *b* verwenden (wobei *bx* dann auch nicht schadet).

### Bedingte Ausführung

Wie man sieht, gibt es keine speziellen Befehle für bedingte Sprünge. Das liegt daran, dass man auf ARM fast jeden Befehl bedingt ausführen kann, also je nachdem, welche Flags gesetzt sind. Dazu hängt man an den Befehlsnamen ein Suffix an, welches angibt, wann der Befehl ausgeführt werden soll:

| Suffix | Bedeutung | Ausführung, wenn… | Ausführung bei welchem *cmp*-Ergebnis |
| -------- | ------------------ | ------------------- | ---------------------------------------- |
| al | Always | Immer | — |
| eq | EQual | ZF=1 | Gleichheit |
| ne | Not Equal | ZF=0 | Ungleichheit |
| cs | Carry Set | CF=1 | Vorzeichenlos größer oder gleich |
| cc | Carry Clear | CF=0 | Vorzeichenlos kleiner |
| mi | MInus | NF=1 | — (Wert negativ) |
| pl | PLus | NF=0 | — (Wert nichtnegativ) |
| vs | oVerflow Set | VF=1 | — (Vorzeichenüberlauf) |
| vc | oVerflow Clear | VF=0 | — (kein Vorzeichenüberlauf) |
| hi | HIgher | CF=1 und ZF=0 | Vorzeichenlos größer |
| ls | Less or Same | CF=0 oder ZF=1 | Vorzeichenlos kleiner |
| ge | Greater or Equal | NF=VF | Vorzeichenbehaftet größer oder gleich |
| lt | Less Than | NF≠VF | Vorzeichenbehaftet kleiner |
| gt | Greater Than | NF=VF und ZF=0 | Vorzeichenbehaftet größer |
| le | Less or Equal | NF≠VF oder ZF=1 | Vorzeichenbehaftet kleiner oder gleich |

Um einen bedingten Sprung auszuführen, verwendet man solch ein Suffix einfach mit der *b*-Instruktion (z. B. *bne* für *Branch if Not Equal*).

## Oft gebrauchte Muster

…Gibt es auf ARM eigentlich nicht, unter anderem deshalb, weil alle Befehle gleich lang sind. Ein *eor r0,r0,r0* ist genauso lang wie ein *mov r0,#0*.

Da man keine 32-Bit-Immediate-Werte laden kann (Opcodes sind nur insgesamt 32 Bit lang), behilft man sich, indem man den Wert entweder woanders speichert und per *ldr* lädt, oder indem man sie stückchenweise per *mov* und *orr* ins Register schiebt.

Aus einer Funktion wird wie beschrieben entweder mit *bx r14* zurückgesprungen, oder, wenn r14 auf dem Stack gespeichert wurde (was nötig ist, wenn die Funktion eine andere Funktion aufgerufen hat), mit *pop {r15}*.

## Beispiel

Eigentlich ist ein Beispiel hier relativ sinnlos, da kaum jemand einen ARM-Rechner haben wird, um es auszuführen, aber dennoch sei hier das Beispiel aus der [x86-Reihe](Teil-2-Assembler-101.md#beispiel "Teil 2 - Assembler 101") adaptiert:

    .arm
    .section .text
    .global factorial

    // Parameter in r0
    factorial:
        // Die Fakultät von 0 ist 1 (Rückgabewert kommt nach r0)
        cmp     r0, #0
        moveq   r0, #1
        bxeq    r14

        push    {r4, r14}
        // Ansonsten rekursiv factorial für r0 - 1 aufrufen und hinterher
        // mit unserem r0 multiplizieren
        mov     r4, r0
        sub     r0, r0, #1
        bl      factorial
     
        // r0 enthält jetzt den Rückgabewert, der ursprüngliche Parameter ist in r4
        mul     r0, r4, r0
        pop     {r4, r15}

Das *.arm* am Anfang gibt übrigens an, dass ARM-Code generiert werden soll (*.thumb* wäre die Alternative).

Der C-Teil ist der gleiche wie in der x86-Reihe, zum Kompilieren kann mit der Toolchain aus dem ARM-Crosscompiler-Artikel folgende Zeile verwendet werden:

    /usr/cross/arm/bin/arm-unknown-linux-gnu-gcc -o factorial main.c fact.S

Dies wird nur im Allgemeinen nicht funktionieren, da keine libc für ARM installiert sein wird. Um wenigstens die Objektdatei zu erhalten, genügt

    /usr/cross/arm/bin/arm-unknown-linux-gnu-gcc -o fact.o -c fact.S

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/9761/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2419/index.html)

<!-- MediaWiki page 2419; revision 9761; parent 0; 2011-05-11T16:13:16Z -->
