# Teil 6 - Multitasking

|  |  |  |
| ----------------------------------------------------------------------------------------------------------- | ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| « [Teil 5 - Interrupts](Teil-5-Interrupts "Teil 5 - Interrupts") | **Navigation** | [Teil 7 - Physische Speicherverwaltung](Teil-7-Physische-Speicherverwaltung "Teil 7 - Physische Speicherverwaltung") » |

## Ziel

Wir wollen zwei Tasks erstellen, die wir durch unser Multitasking "gleichzeitig" laufen lassen. Um das ganze sichtbar zu machen, nehmen wir das klassische Multitasking-Beispiel her: Task 1 gibt in einer Endlosschleife A aus, Task 2 gibt B aus. Am Ende sollten abwechselnd As und Bs auf dem Bildschirm erscheinen.

## Unsere Ausgabetasks

Unsere Tasks implementieren wir vorerst als C-Funktion im Kernel. Das ist einfach genug, daher direkt zum Code:

``` c
void task_a(void)
{
    while (1) {
        kprintf("A");
    }
}

void task_b(void)
{
    while (1) {
        kprintf("B");
    }
}
```

## Task starten

Nachdem diese Vorbereitungen getroffen sind, können wir an das eigentliche Multitasking denken. Unser nächster Schritt ist es, in einen Task hineinzuspringen. Teil zwei ist das Herausspringen, aber das heben wir uns erst einmal für später auf.

Was macht jetzt einen Task aus? Was sich zwischen den einzelnen Tasks unterscheidet, ist der Prozessorzustand – also der Inhalt der Register. Wenn wir einen Task unterbrechen, müssen wir seine Registerbelegung speichern, und bevor wir in einen Tasks hineinspringen müssen wir den Zustand wiederherstellen (bzw. beim ersten Einsprung einen vernünftigen Anfangszustand herstellen).

Eine "Struktur für den Prozessorzustand" kommt irgendwie bekannt vor. In der Tat haben wir bei der Interruptbehandlung schon eine *struct cpu_state* definiert, die wir direkt weiterverwenden können. Die Struktur, wie wir sie in Teil 5 definiert haben, sollte vorerst reichen, denn mehr als die Allzweckregister und eflags benutzen unsere Tasks im Moment nicht. Wenn man es richtig macht, könnten beispielsweise noch die Segmentregister dazukommen.

Wir benutzen die Struktur sogar schon an der richtigen Stelle: Ein Taskwechsel findet immer in einem Interrupthandler statt – das kann z.B. ein Timerinterrupt sein, der signalisiert, dass der Prozess seine Zeit aufgebraucht hat, oder ein Syscall, mit dem das Programm anzeigt, dass es vorzeitig den Prozessor abgeben möchte. Genau genommen findet sogar der ganze Kernel nur noch in Interrupthandlern statt, sobald der erste Task gestartet ist.

Legen wir also einmal den Startzustand für die beiden Tasks fest, jeder bekommt seinen Stack und dort drin eine struct cpu_state:

``` c
static uint8_t stack_a[4096];
static uint8_t stack_b[4096];

/*
 * Jeder Task braucht seinen eigenen Stack, auf dem er beliebig arbeiten kann,
 * ohne dass ihm andere Tasks Dinge ueberschreiben. Ausserdem braucht ein Task
 * einen Einsprungspunkt.
 */
struct cpu_state* init_task(uint8_t* stack, void* entry)
{
    /*
     * CPU-Zustand fuer den neuen Task festlegen
     */
    struct cpu_state new_state = {
        .eax = 0,
        .ebx = 0,
        .ecx = 0,
        .edx = 0,
        .esi = 0,
        .edi = 0,
        .ebp = 0,
        //.esp = unbenutzt (kein Ring-Wechsel)
        .eip = (uint32_t) entry,

        /* Ring-0-Segmentregister */
        .cs  = 0x08,
        //.ss  = unbenutzt (kein Ring-Wechsel)

        /* IRQs einschalten (IF = 1) */
        .eflags = 0x202,
    };

    /*
     * Den angelegten CPU-Zustand auf den Stack des Tasks kopieren, damit es am
     * Ende so aussieht als waere der Task durch einen Interrupt unterbrochen
     * worden. So kann man dem Interrupthandler den neuen Task unterschieben
     * und er stellt einfach den neuen Prozessorzustand "wieder her".
     */
    struct cpu_state* state = (void*) (stack + 4096 - sizeof(new_state));
    *state = new_state;

    return state;
}
```

Wie im Code angedeutet, können wir ss und esp im Prozessorzustand erst einmal ignorieren. Wir haben sie schon in unsere struct cpu_state aufgenommen, weil sie bei einem Interrupt automatisch von der CPU gespeichert werden, wenn wir dazu von einem normalen unprivilegierten Programm (also aus Ring 3) in den Kernel (also Ring 0) wechseln. Wir lassen bisher aber alles mit vollen Privilegien laufen und bekommen daher bei Interrupts auch keinen Stackwechsel.

Als nächstes brauchen wir einen primitiven Scheduler, der uns sagt, welcher Task als nächstes dran ist. Ein Teil ist die Initialisierung, die die beiden Tasks startet und die Datenstrukturen bereitstellt. Dieser Teil muss aufgerufen werden, bevor Hardwareinterrupts aktiviert werden. Der zweite Teil ist der Scheduler selbst, der speichert, wo der alte Task gerade steht und den Zustand des nächsten Tasks zurückgibt.

``` c
static int current_task = -1;
static int num_tasks = 2;
static struct cpu_state* task_states[2];

void init_multitasking(void)
{
    task_states[0] = init_task(stack_a, task_a);
    task_states[1] = init_task(stack_b, task_b);
}

/*
 * Gibt den Prozessorzustand des naechsten Tasks zurueck. Der aktuelle
 * Prozessorzustand wird als Parameter uebergeben und gespeichert, damit er
 * beim naechsten Aufruf des Tasks wiederhergestellt werden kann
 */
struct cpu_state* schedule(struct cpu_state* cpu)
{
    /*
     * Wenn schon ein Task laeuft, Zustand sichern. Wenn nicht, springen wir
     * gerade zum ersten Mal in einen Task. Diesen Prozessorzustand brauchen
     * wir spaeter nicht wieder.
     */
    if (current_task >= 0) {
        task_states[current_task] = cpu;
    }

    /*
     * Naechsten Task auswaehlen. Wenn alle durch sind, geht es von vorne los
     */
    current_task++;
    current_task %= num_tasks;

    /* Prozessorzustand des neuen Tasks aktivieren */
    cpu = task_states[current_task];

    return cpu;
}
```

Jetzt müssen wir den Scheduler nur noch zum Einsatz bringen. Dieser Teil ist das, was das eigentliche Multitasking macht. Der passende Code dazu ist so kurz wie die Idee einfach ist: Anstatt bei einem Interrupt den gerade eben gesicherten Prozessorzustand wiederherzustellen, stellen wir einfach den Zustand eines anderen Tasks wieder her. Dazu wird handle_interrupt so geändert, dass es *cpu* wieder zurückgibt. Im Fall des Timerinterrupts geben wir allerdings den Zustand des neuen Tasks zurück:

``` c
struct cpu_state* handle_interrupt(struct cpu_state* cpu)
{
    struct cpu_state* new_cpu = cpu;

    ...

    if (cpu->intr == 0x20) {
        new_cpu = schedule(cpu);
    }

    ...

    return new_cpu;
}
```

Der Interrupt-Handler muss jetzt nur noch diesen Rückgabewert verarbeiten, d.h. den Stack entsprechend wechseln:

``` asm
    ...
    // Handler aufrufen
    // Der Rueckgabewert ist der Prozessorzustand des moeglicherweise
    // gewechselten Tasks. Wir muessen also den Stack dorthin wechseln
    // um die Register wiederherzustellen.
    push %esp
    call handle_interrupt
    mov %eax, %esp

    // CPU-Zustand wiederherstellen
    ...
```

Das war's. Beim nächsten Timerinterrupt fängt der Kernel fröhlich an, Multitasking zu machen, und abwechselnd As und Bs auf den Bildschirm zu schreiben. Wer nicht auf den Timerinterrupt warten möchte kann auch den Interrupt 0x20 als Software-Interrupt auslösen.

## Userspace

So schön es ist, jetzt mehrere Programm gleichzeitig laufen lassen zu können, perfekt ist das alles noch nicht. Die Tasks laufen alle in Ring 0, haben also alle Privilegien, die sie sich wünschen. Was, wenn ein Programm einfach Interrupts ausschaltet? Das System wäre dann lahmgelegt. Die Programme müssen also nach Ring 3.

Was ändert sich für uns mit Ring-3-Tasks? An sich ist es nicht viel. Wie oben schon angemerkt, kommt zum bereits Bekannten nur noch ein Stackwechsel dazu. Wenn der Prozessor bei einem Interrupt in Ring 3 ist, also einen Ringwechsel durchführen muss, sichert er esp und ss auf den Stack (wie es in struct cpu_state schon vorgesehen ist). Beim Zurückspringen aus dem Interrupt mittels *iret* stellt er diese Register auch wieder her. Nachdem er die Register gesichert hat, lädt der Prozessor den Kernel-Stack (bestehend aus ss und esp). Diese beiden Werte kommen aus dem aktiven [Task State Segment](Task-State-Segment "Task State Segment") (TSS).

Aber fangen wir beim leichten Teil an. Stellen wir den Taskzustand auf Ring 3 um. Dazu brauchen wir jetzt zusätzlich zum Kernelstack jedes Tasks, der für den Prozessorzustand und die Ausführung der Interrupt-Handler benutzt wird, einen zweiten getrennten Stack für jeden Task, auf dem dieser beliebig arbeiten kann. Außerdem benutzen wir jetzt die Ring-3-Segmente aus der GDT:

``` c
static uint8_t user_stack_a[4096];
static uint8_t user_stack_b[4096];

struct cpu_state* init_task(uint8_t* stack, uint8_t* user_stack, void* entry)
{

...

        .esp = (uint32_t) user_stack + 4096,
        .eip = (uint32_t) entry,

        /* Ring-3-Segmentregister */
        .cs  = 0x18 | 0x03,
        .ss  = 0x20 | 0x03,
```

Code und Stack wären damit abgedeckt, aber wir brauchen auch noch die Datensegmente. Unser Aufruf des Interrupthandlers sieht damit folgendermaßen aus:

``` asm
    // Kernel-Datensegmente laden
    mov $0x10, %ax
    mov %ax, %ds
    mov %ax, %es

    // Handler aufrufen
    // Der Rueckgabewert ist der Prozessorzustand des moeglicherweise
    // gewechselten Tasks. Wir muessen also den Stack dorthin wechseln
    // um die Register wiederherzustellen.
    push %esp
    call handle_interrupt
    mov %eax, %esp

    // User-Datensegmente laden
    mov $0x23, %ax
    mov %ax, %ds
    mov %ax, %es
```

Als nächstes legen wir das TSS an. Der Aufbau wird im Artikel [Task State Segment](Task-State-Segment "Task State Segment") beschrieben, wir brauchen davon nur die Felder esp0 und ss0. ss0 können wir konstant auf unser Ring-0-Datensegment setzen, esp0 muss für jeden Task angepasst werden.

``` c
static uint32_t tss[32] = { 0, 0, 0x10 };

...

        if (cpu->intr == 0x20) {
            new_cpu = schedule(cpu);
            tss[1] = (uint32_t) (new_cpu + 1);
        }
```

Außerdem müssen wir das TSS noch aktivieren. Dazu fügen wir der GDT einen zusätzlichen Eintrag hinzu und laden anschließend auch das Taskregister TR neu (nicht vergessen, das Limit der GDT zu erhöhen, wenn nötig):

``` c
    set_entry(5, (uint32_t) tss, sizeof(tss),
        GDT_FLAG_TSS | GDT_FLAG_PRESENT | GDT_FLAG_RING3);

    // Taskregister neu laden
    asm volatile("ltr %%ax" : : "a" (5 << 3));
```

Damit wäre auch der Userspace implementiert. Wer möchte, kann das gern durch ein *asm("cli; hlt");* in einem der Tasks ausprobieren. Bevor die Tasks nach Ring 3 verschoben worden sind, durften sie die Befehle ausführen und der Kernel kam zum Stillstand. Jetzt wird eine Exception ausgelöst (13 = \#GP = General Protection Fault) und der Kernel gibt eine Fehlermeldung aus (bevor er sich ebenfalls in eine Endlosschleife begibt – normal würde er hier stattdessen einfach den Task beenden).

  

|  |  |  |
| ----------------------------------------------------------------------------------------------------------- | ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| « [Teil 5 - Interrupts](Teil-5-Interrupts "Teil 5 - Interrupts") | **Navigation** | [Teil 7 - Physische Speicherverwaltung](Teil-7-Physische-Speicherverwaltung "Teil 7 - Physische Speicherverwaltung") » |

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/11392/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1899/index.html)

<!-- MediaWiki page 1899; revision 11392; parent 7128; 2018-09-04T10:13:02Z -->
