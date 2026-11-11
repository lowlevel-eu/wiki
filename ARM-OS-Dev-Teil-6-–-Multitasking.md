# ARM-OS-Dev Teil 6 – Multitasking

|  |  |  |
| ------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| « [ARM-OS-Dev Teil 5 – Interrupts](ARM-OS-Dev-Teil-5-%E2%80%93-Interrupts "ARM-OS-Dev Teil 5 – Interrupts") | **Navigation** | [ARM-OS-Dev Teil 7 – Physische Speicherverwaltung](ARM-OS-Dev-Teil-7-%E2%80%93-Physische-Speicherverwaltung "ARM-OS-Dev Teil 7 – Physische Speicherverwaltung") » |

## Ziel

Als nächstes soll unser Kernel zwischen verschiedenen Ausführungssträngen hin und her schalten können, also Multitasking bieten. Zu Anfang sollen dafür zwei einfache Endlosschleifen herhalten, die jeweils A respektive B ausgeben.

## Ausgabetasks

Diese Ausgabetasks werden genau so definiert, wie sie gerade beschrieben wurden. Zur Ausgabe wird hier eine kprintf-Funktion verwendet (die also im Großen und Ganzen printf entspricht, wobei nicht unbedingt alle Formatzeichen unterstützt werden), deren Implementierung wie in der x86-Reihe dem Leser überlassen wird. Da in diesem Beispiel keine Formatzeichen verwendet werden, genügt es hier allerdings auch, eine einfachere Funktion zu verwenden, die einfach einen C-String ausgibt. \<c\>void task_a(void) {

       for (;;)
           kprintf("A\r");

}

void task_b(void) {

       for (;;)
           kprintf("B\r");

}\</c\>

Damit QEMU keine endlose Ausgabe generiert, ist es sinnvoll, jeweils ein Carriage Return (*\r*) nach dem Buchstaben auszugeben, sodass die Ausgabe sich selbst überschreibt (*\r* kehrt zum Anfang der aktuellen Zeile zurück).

## Tasks starten

Das Erstellen und Wechseln von Tasks geschieht im Großen und Ganzen ebenso wie in der [x86-Reihe](Teil-6-Multitasking#task-starten "Teil 6 - Multitasking"). Auch auf dem ARM definiert sich ein Task über seine Registerwerte und auch hier werden Taskwechsel durch das Wechseln des IRQ-Stacks ausgeführt.

Beachtet werden muss jedoch, dass unsere Tasks zwei verschiedene Prozessormodi verwenden: User und IRQ. Das heißt auch, dass sie jeweils zwei Stacks benötigen, einen Userstack und einen IRQ-Stack. Die init_task-Funktion sieht also so aus:

\<c\>#define STACK_SIZE 4096

static uint8_t usr_stack_a\[STACK_SIZE\], usr_stack_b\[STACK_SIZE\]; static uint8_t irq_stack_a\[STACK_SIZE\], irq_stack_b\[STACK_SIZE\];

/\*

    * Jeder Task braucht einen eigenen Stack für den Usermode und einen eigenen
    * für den IRQ-Modus, sodass sich die Stacks verschiedener Tasks nicht in die
    * Quere kommen.
    */

static struct cpu_state \*init_task(uint8_t \*usr_stack, uint8_t \*irq_stack, void \*entry) {

       // CPU-Zustand für den neuen Task
       struct cpu_state *new_state = (struct cpu_state *)(irq_stack + STACK_SIZE) - 1;

       *new_state = (struct cpu_state){
           // Userstack
           .usr_r13 = (uint32_t)(usr_stack + STACK_SIZE),
           // Usermode, IRQs erlaubt, ARM-Modus
           .cpsr = 0x00000050,
           // Einsprungspunkt
           .r15 = (uint32_t)entry
           // Ein Supervisorstack ist noch nicht nötig, diese wären erst für
           // Syscalls per SWI wichtig
       };

       return new_state;

}\</c\>

Wie im Code angemerkt wird, werden unsere Tasks in späteren Teilen auch noch einen dritten Prozessormodus benutzen (Supervisor), um Systemaufrufe durchzuführen. In diesem Fall benötigen sie dann noch einen weiteren Stack für eben diesen Modus. Bisher ist das aber noch nicht nötig.

Da der Scheduler, der den nächsten auszuführenden Task auswählt, im Idealfall architekturunabhängig ist, kann dieser unverändert aus der x86-Reihe übernommen werden. Einzig die *init_task*-Aufrufe sind natürlich ein bisschen anders, da sie bei uns einen dritten Parameter verlangen. Sie lauten somit einfach *init_task(usr_stack_a, irq_stack_a, task_a);* sowie *init_task(usr_stack_b, irq_stack_b, task_b)*.

Nun benötigen wir noch eine IRQ-Quelle, die regelmäßig IRQs auslöst. Das I/CP-Board besitzt zu diesem Zweck drei Timer, zwei davon (Timer 1 und 2) laufen mit einer Grundfrequenz von einem MHz. Diese Grundfrequenz wird je nach Konfiguration durch 16, 256 oder gar nicht geteilt und mit der resultierenden Frequenz wird dann der Wert einer Variable dekrementiert. Erreicht diese Variable den Wert 0, dann wird ein IRQ ausgelöst und ein bestimmter Wert wieder in die Variable geschrieben und das Zählen beginnt von neuem (wenn man den Timer entsprechend konfiguriert). Genau das kann man folgendermaßen tun: \<c\>#define TIMER_REG ((volatile uint32_t \*)0x13000000)

1.  define TIMER1_REG (TIMER_REG + 0x40)

void init_timer(void) {

       // 10 000 µs == alle zehn ms == 100 Hz
       TIMER1_REG[0] = (10000 + 128) / 256;
       TIMER1_REG[2] = 0xEA;

       register_irq_handler(6, &timer1_overflow);

}\</c\>

Damit wird Timer 1 auf eine Frequenz von ca. 100 Hz eingestellt (als Frequenzteiler wird 256 verwendet, sodass sich eine Frequenz von 3906,25 Hz ergibt; der Wert (10000 + 128) ÷ 256 (= 39) ist derjenige, der nach jedem IRQ in die Zählervariable geladen wird. Insgesamt wird der IRQ also mit einer Frequenz von 3905,25 ÷ 39 ≈ 101,16 Hz aufgerufen.

Nun müssen wir noch den IRQ-Handler für den Timer schreiben. Wenn man einen IRQ vom Timer empfangen hat, muss ihm mitgeteilt werden, dass er bearbeitet wurde, sonst wird er sofort wieder ausgelöst (was schlecht wäre, da dann kein anderer Code mehr zum Zuge käme). Dies geschieht, indem ein beliebiger Wert nach 0x1300010C geschrieben wird. Anschließend rufen wir einfach den Scheduler auf, der uns den IRQ-Stack des nächsten Tasks zurückgibt: \<c\>static struct cpu_state \*timer1_overflow(struct cpu_state \*state) {

       // IRQ als bearbeitet melden
       TIMER1_REG[3] = 42;

       return schedule(state);

}\</c\>

Jetzt müssen in der *init*-Funktion nur noch *init_multitasking* und *init_timer* aufgerufen werden (alternativ kann man letztere auch in *init_multitasking* aufrufen) und schon streiten sich Task A und B um die Vorherrschaft bei der Ausgabe – theoretisch. Praktisch haben wir noch ein kleines Problem in *init_task*: Beim Initialisieren von *\*new_state* nutzt gcc ein memset, um die nicht angegebenen Felder auf 0 zu setzen (wie es der C-Standard verlangt). Solch ein memset muss erst noch geschrieben werden – aber das sollte für einen Betriebssystemprogrammierer ja kein Problem darstellen. ;-)

## Weitere Quellen

Das Interface des Timers ist in [einem I/CP-Manual](http://infocenter.arm.com/help/topic/com.arm.doc.dui0159b/DUI0159B_integratorcp_1_0_ug.pdf) ab Seite 108 beschrieben.

Der fertige Code für diesen Teil des Tutorials befindet sich [hier](https://gitorious.org/arm-os-dev/kernel/trees/03b893dd5fdded2f34126588c49845c5de26b6d9).

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/9772/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2423/index.html)

<!-- MediaWiki page 2423; revision 9772; parent 0; 2011-05-12T21:05:42Z -->
