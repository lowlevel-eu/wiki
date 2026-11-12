# ARM-OS-Dev Teil 5 – Interrupts

|  |  |  |
| --------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| « [ARM-OS-Dev Teil 4 – Hello World](ARM-OS-Dev-Teil-4-%E2%80%93-Hello-World "ARM-OS-Dev Teil 4 – Hello World") | **Navigation** | [ARM-OS-Dev Teil 6 – Multitasking](ARM-OS-Dev-Teil-6-%E2%80%93-Multitasking "ARM-OS-Dev Teil 6 – Multitasking") » |

## Exceptions

Es gibt verschiedene Gründe, die auf einem ARM eine Exception, also eine Unterbrechung des normalen Programmflusses auslösen. An dieser Stelle sei auf den [ARM-Artikel](ARM#exceptions "ARM") verwiesen, der all diese auflistet und beschreibt. Versucht man, die x86-Interrupts auf ARM-Exceptions abzubilden, dann entsprechen Exceptions einem Abort oder einer Undefined Instruction Exception, IRQs einem IRQ oder einem FIQ und Software-Interrupts einem SWI.

Jede Exception verlangt einen bestimmten CPU-Modus mit eigenen Registern. Wir verwenden in diesem Tutorial lediglich die Modi User/System, Supervisor und IRQ, weil wir nur die IRQ- und SWI-Exceptions behandeln (User/System werden für Programme verwendet).

## Initialisierung

IRQs verwenden ist auf dem ARM sehr einfach. Eigentlich muss man lediglich das I-Bit im CPSR löschen (s. [ARM-Artikel](ARM#cpsr "ARM")) und schon können IRQs aufgerufen werden. Aborts, Undefined Instruction Exceptions, und SWIs können sowieso jederzeit auftreten. Zusätzlich enthält eigentlich jedes ARM-System jedoch noch einen Interruptcontroller, damit das OS auch schnell feststellen kann, welcher IRQ aufgetreten ist – von sich aus kennt der Prozessor ja keinen Unterschied zwischen einem IRQ, der von der Netzwerkkarte und einem, der von der Tastatur ausgelöst wurde. Daher möchte auch dieser Interruptcontroller initialisiert werden. Auf dem I/CP-Board gibt es sogar mehrere Interruptcontroller, wobei wir hier nur einen einzigen verwenden (die meisten „interessanten“ IRQs werden von diesem Primary Interrupt Controller abgewickelt). Zudem gibt es jeden Interruptcontroller einmal für IRQs und einmal für FIQs. Wir wollen jedoch der Einfachheit halber nur IRQs benutzen.

Der erste Interruptcontroller bietet seine Register im Speicher ab der Adresse 0x14000000 an. Am Offset +8 befindet sich ein 32-Bit-Register (ENABLESET), mit dem IRQs aktiviert werden können, indem das entsprechende Bit gesetzt wird. Am Offset +12 ist ein Register (ENABLECLR), mit dem IRQs deaktiviert werden können, indem ihr Bit gesetzt wird. Beim Start sollten zunächst alle IRQs deaktiviert werden, damit zum Beispiel die drei Systemtimer nicht einfach wild feuern und die gesamte CPU-Zeit stehlen, wenn man sie nicht konfiguriert hat. Dies geschieht also, indem 0xFFFFFFFF nach 0x1400000C geschrieben wird. Wenn ein Handler für einen IRQ registriert wird, muss der IRQ dann aktiviert werden, indem das entsprechende Bit im ENABLESET-Register gesetzt wird.

Nach der Interrupt-Controller-Initialisierung kann dann einfach das I-Bit im CPSR gelöscht werden, sodass IRQs ausgelöst werden können: \<c\>\_\_asm\_\_ \_\_volatile\_\_ ("mrs r0,cpsr;"

                         "bic r0,#0x80;"
                         "msr cpsr_ctl,r0" ::: "r0");</c>

Diese Befehlsreihe liest das CPSR ins r0-Register, löscht Bit 7 (das I-Bit, Wert 0x80) und schreibt den resultierenden Wert wieder ins CPSR-Register, wobei nur der ctl-Teil, also die untersten acht Bit, verändert wird (am Rest haben wir ja nichts geändert).

## IRQs abfangen

Nun bringt das nicht viel, da der bisherige IRQ-Exception-Handler ja einfach aus einem „b .“ besteht, also einer Endlosschleife. Irgendwas anderes zu tun wäre wohl nicht schlecht. Im Allgemeinen erweist es sich sinnvoll, alle Register zu speichern und eine C-Funktion aufzurufen. Dazu fügen wir oben in unsere init.S ein „.extern asm_handle_irq“ ein, verändern das sechste „b .“ von oben zu einem „b asm_handle_irq“ und erstellen eine neue Datei intr.S mit dem Inhalt:

    .arm
    .extern handle_irq
    .global asm_handle_irq

    asm_handle_irq:
    sub     r14, #4
    /* Nicht gebankte Register speichern */
    push    {r0 - r12, r14}

    /* Supervisor-R13/R14/SPSR und CPSR speichern */
    msr     cpsr_ctl, #0xD3
    mrs     r1, spsr
    mov     r2, r13
    mov     r3, r14
    msr     cpsr_ctl, #0xD2
    mrs     r0, spsr
    push    {r0 - r3}

    /* User-R13/R14 speichern */
    stmdb   r13, {r13, r14}^
    sub     r13, #8

    /* IRQ behandeln */
    mov     r0, r13
    bl      handle_irq
    mov     r13, r0

    /* User-R13/R14 laden */
    ldmia   r13, {r13, r14}^
    add     r13, #8

    /* Supervisor-R13/R14/SPSR und CPSR laden */
    pop     {r0 - r3}
    msr     spsr_all, r0
    msr     cpsr_ctl, #0xD3
    msr     spsr_all, r1
    mov     r13, r2
    mov     r14, r3
    msr     cpsr_all, #0xD2

    /* Nicht gebankte Register laden und zurückkehren */
    pop     {r0 - r12, r14}
    movs    r15, r14

r14 zeigt zu Beginn auf den zweiten Befehl nach dem Befehl, der ausgeführt wurde, bevor der IRQ ausgelöst wurde. Das heißt, wir müssen vier abziehen, damit es auf den als nächstes auszuführenden Befehl zeigt. Dann speichern wir es und alle nicht-Schattenregister (r0 bis r12) auf dem IRQ-Stack. Nun müssen wir auch die Schattenregister speichern. Das betrifft r13, r14 und das SPSR, welches ebenfalls in jedem Prozessormodus extra vorhanden ist (außer im System/User-Modus, dort existiert es gar nicht, weil nur die CPU dieses Register zum Speichern von CPSR im Falle einer Exception benötigt; der User/System-Modus wird von keiner Exception betreten, sodass auch kein SPSR nötig ist). Also wechseln wir mit dem MSR-Befehl in den Prozessormodus 0x13 (mit deaktivierten IRQs und FIQs, deshalb insgesamt 0xD3), also den Supervisormodus, laden r13, r14 und das SPSR in nicht-Schattenregister und speichern dieser Werte nach der Rückkehr in den IRQ-Modus (0x12 ist der Wert für den IRQ-Modus) auf dem Stack, zusammen mit dem IRQ-SPSR, das den CPSR-Wert vor Auslösen des IRQs enthält.

Später möchten wir auch noch den Usermodus verwenden, deshalb müssen wir auch dessen r13 und r14 auf dem Stack speichern. Hier können wir uns einen Wechsel des Prozessormodus sparen, weil es eine spezielle Variante der LDM-/STM-Befehle gibt, die mit Usermoderegistern arbeitet (wird durch das Zirkumflex nach der Registerliste deutlich gemacht). Diese kann allerdings kein Base-Write-Back, sodass wir r13 anschließend manuell um acht verringern müssen.

Dann wird r13 nach r0 geladen, sodass die C-Funktion handle_irq den Stackpointer als ersten (und einzigen) Parameter erhält. Sie gibt einen neuen Stack in r0 zurück, der wieder nach r13 geladen wird. Von diesem Stack werden dann wieder alle Register geladen. Der Aufruf „movs r15, r14“ lädt r14 nach r15 und das SPSR ins CPSR (wechselt also auch den CPU-Modus; dies ist eine Besonderheit der Arithmetik- und Logikbefehle: Werden die *s*-Varianten (die die Flags modifizierenden Varianten) und r15 als Zielregister verwendet, dann wird das SPSR ins CPSR geladen).

Hinweis: Anstatt am Anfang vier von r14 abzuziehen, könnte man am Ende auch einfach „subs r15, r14, \#4“ statt des *movs* verwenden. Dies würde aber bedeuten, dass wir beim Erstellen eines neuen Prozesses, bei dem wir mit dem r14-Wert auf dem Stack den Einsprungspunkt des Programms festlegen, den tatsächlichen Wert plus vier nehmen müssten. Kann man machen, man kann aber auch einfach am Anfang des IRQ-Handlers vier von r14 abziehen und sich das somit sparen, so wie das hier getan wird.

Jetzt können wir noch den C-Teil in einer irq.c schreiben: \<c\>#include "cpu.h"

1.  include "stdint.h"

<!-- -->

1.  define IC_REGS ((volatile uint32_t \*)0x14000000)

void init_irqs(void) {

       // Alle IRQs deaktivieren
       IC_REGS[3] = 0xFFFFFFFF;

       // IRQs an sich aber erlauben
       __asm__ __volatile__ ("mrs r0,cpsr;"
                             "bic r0,#0x80;"
                             "msr cpsr_ctl,r0" ::: "r0");

}

struct cpu_state \*handle_irq(struct cpu_state \*state) {

       // IRQ-Nummer herausfinden
       unsigned irq = 0;
       // In diesem Register sind die Bits der IRQs gesetzt, aufgrund deren dieser
       // IRQ ausgelöst wurde; durch das Lesen werden alle Bits zurückgesetzt
       uint32_t status = IC_REGS[0];

       while (status)
       {
           if (status & 1)
           {
               // Etwas tun, um den IRQ mit der Nummer irq zu behandeln...
           }

           irq++;
           status >>= 1;
       }

       return state;

}\</c\>

(stdint.h enthält typedefs für uint8_t (unsigned char), uint16_t (unsigned short), uint32_t (unsigned int) und uint64_t (unsigned long long), cpu.h definiert *struct cpu_state*)

Um jetzt noch wirklich IRQs zu behandeln, könnte man ein Array aus Funktionspointern anlegen, die auf IRQ-Handler zeigen: \<c\>static struct cpu_state \*(\*irq_handlers\[32\])(struct cpu_state \*state);

void register_irq_handler(unsigned irq, struct cpu_state (\*handler)(struct cpu_state \*state)) {

       // Es gibt nur 32 IRQs
       if (irq >= 32)
           return;

       // Wenn schon ein Handler registriert ist, wird der nicht überschrieben
       if (irq_handlers[irq])
           return;

       irq_handlers[irq] = handler;

       // IRQ aktivieren
       IC_REGS[2] |= 1 << irq;

}\</c\>

Der Teil, um den IRQ zu behandeln (in *handle_irq*), lautet dann wie folgt: \<c\> if (irq_handlers\[irq\])

                   state = irq_handlers[irq](state);</c>

Nun zur *struct cpu_state*, diese wird in cpu.h definiert; sie spiegelt die Werte auf dem Stack wieder, die asm_handle_irq darauf gelegt hat: \<c\>struct cpu_state {

       // r13 und r14 des Usermodes
       uint32_t usr_r13, usr_r14;
       // CPSR vor dem IRQ und SPSR des Supervisormodes
       uint32_t cpsr, svc_spsr;
       // r13 und r14 des Supervisormodes
       uint32_t svc_r13, svc_r14;
       // r0 bis r12 sowie r15
       uint32_t r0, r1, r2, r3, r4, r5, r6, r7;
       uint32_t r8, r9, r10, r11, r12, r15;

} \_\_attribute\_\_((packed));\</c\>

Apropos Stack: Genau da gibt es noch ein Problem. Wir haben noch keinen Stack für IRQs definiert. Das müssen wir in der init.S machen, indem wir nicht nur das r13 des aktiven Supervisormodes ändern, sondern auch das r13 des IRQ-Modes:

    ldr     r13, [r15, #kernel_stack_addr - 8 - .]
    mov     r0, r13
    msr     cpsr_ctl, #0xD2
    add     r13, r0, #8192
    msr     cpsr_ctl, #0xD3

Damit das funktioniert, müssen wir jedoch noch mal 8 kB Speicher nach dem Supervisorstack für den IRQ-Stack reservieren:

    .space 8192
    kernel_stack:
    .space 8192

Irgendwo in der init-Funktion, möglichst am Anfang, sollte jetzt noch die init_irqs-Funktion aufgerufen werden.

Theoretisch könnte man auch hier jetzt schon einen Tastaturtreiber schreiben, wenn man unbedingt wöllte. Dieser unterscheidet sich noch nicht einmal besonders vom x86-Treiber, weil auch bei I/CP-Boards PS/2 als Tastaturinterface benutzt wird, es werden also die gleichen Befehle zur Kommunikation mit der Tastatur verwendet.

## Weitere Quellen

Die/der Interruptcontroller ist in [einem I/CP-Manual](http://infocenter.arm.com/help/topic/com.arm.doc.dui0159b/DUI0159B_integratorcp_1_0_ug.pdf) ab Seite 50 beschrieben.

Der fertige Code für diesen Teil des Tutorials befindet sich [hier](https://gitorious.org/arm-os-dev/kernel/trees/c13720c987aba6d195f60201081cbbb677e4365a).

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/9773/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2422/index.html)

<!-- MediaWiki page 2422; revision 9773; parent 9769; 2011-05-12T21:11:15Z -->
