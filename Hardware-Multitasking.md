# Hardware-Multitasking

| Hardware-Multitasking |  |
| ------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Schwierigkeit**: *nicht angegeben*<br> |  |
| Benötigtes Vorwissen: | [TSS](https://github.com/lowlevel-eu/wiki/wiki/Task-State-Segment "TSS"), [GDT](https://github.com/lowlevel-eu/wiki/wiki/Global-Descriptor-Table "GDT"), [Scheduler](https://github.com/lowlevel-eu/wiki/wiki/Scheduler "Scheduler") |
| Sprache: |  |

Im Gegensatz zum häufig eingesetzten Software-Multitasking, übernimmt beim Hardware-Multitasking die CPU die Aufgaben des Dispatchers. Viele moderne Betriebssysteme verzichten auf Hardware-Multitasking, da es angeblich keinen großen Zeitvorteil gegenüber dem Software-Multitasking hat. Im Long Mode kann kein Hardware-Multitasking genutzt werden!

## Grundlagen

### Das Task State Segment

Hardware-Multitasking beruht auf dem sogenannten Task State Segment, welches jedem Task zugeordnet wird und unter anderem dessen Registerwerte speichert. Der Aufbau des TSS wird [hier exakt](https://github.com/lowlevel-eu/wiki/wiki/Task-State-Segment "TSS") beschrieben.

Der Speicherort des TSS wird als Eintrag in der GDT gespeichert. Der Selektor dieses Eintrags wird im Task Register der CPU gespeichert, wodurch sie bei einem Taskwechsel weiß, wo die (dynamischen) Registerwerte gespeichert werden sollen, damit diese beim Wiederaufruf des Tasks unverändert sind.

Folgender Code legt ein TSS an und erzeugt dann den Descriptor in der GDT, der darauf zeigt.

\<c\>

1.  define GDT_TYPE_TSS 0x89

struct tss task_state_segment; gdt_create_descriptor ( n, //die Nummer des Descriptor-Eintrags (uint32_t) &task_state_segment, //Adresse sizeof(struct tss)-1, //Länge 0, //flags GDT_TYPE_TSS); //access \</c\>

### Taskwechsel

Für einen Taskwechsel (Task-Switch) springt man mit einem jmp-Befehl zum Selektor des TSS, der dem neuen Task zugeordnet ist:

\<asm\>jmp TSS_SELECTOR : 0000\</asm\>

(Das RPL des TSS_SELECTORS sowie das Offset werden von der CPU ignoriert.)

Dieser Befehl sorgt dafür, dass die CPU die Registerwerte des aktuellen Tasks in dessen TSS speichert, dessen Selektor ist im Task Register gespeichert. Dann lädt die CPU den im jmp-Befehl angegebenen neuen Selektor ins Task Register und schreibt die Werte des zugehörigen TSS in die Register, wodurch die Registerwerte des Tasks, zu dem durch den jmp-Befehl gewechselt werden soll, wiederhergestellt werden. Allerdings gibt es hier ein kleines Problem:

\<asm\>jmp ax : 0000\</asm\>

...funktioniert nicht. Daher muss man sich eines kleinen Tricks bedienen: \<asm\> mov \[opcode_hack+5\], ax opcode_hack: jmp 1234 : 1234 \</asm\>

Das sieht nicht schön aus, ist aber die einzige Möglichkeit „dynamisch“ zu springen. Ich hoffe, ich habe diesen Code korrekt in die AT&T-Assembler-Syntax (siehe unten) übertragen, da ich den Code nicht vollständig getestet habe.

  
Zu beachten ist allerdings, dass der Taskwechsel von der Software (dem Scheduler) implementiert werden muss, weil die CPU nur das Dispatching übernimmt. Es gibt zwar einen Trick, wie man das Scheduling auch von der CPU ausführen lassen kann, aber diese Möglichkeit würde ich nicht empfehlen (siehe dazu unten). Außerdem sollte man wissen, dass man den Task-Switch auch mit einem call- oder int-Befehl ausführen kann, was allerdings etwas komplizierter ist.

### Initialisierung

Bevor überhaupt ein Task-Switch ausgeführt werden kann, muss einmal ein Start-TSS-Selektor in das Task Register geladen werden. Dazu dient folgender Befehl:

\<asm\> mov ax, 3\*8 ltr ax \</asm\>

Diese Sequenz lädt den dritten Selektor in das Task Register. Dieser muss auf einen gültigen TSS-Descriptor zeigen, der wiederum die Adresse des TSS des Starttasks angibt. (Der dritte Selektor wurde hier nur als Beispiel verwendet)

## Implementierung

### Schritt 1: Task State Segmente anlegen

Jeder spätere Task benötigt ein TSS. Diese müssen mit den Werten gefüllt werden, die der Task zu Beginn seiner Ausführung in den Registern stehen haben soll:

\<c\>

1.  define NUM_TASKS 10 //oder wieviele auch immer du möchtest

struct tss task_state_segments\[NUM_TASKS\]; uint32_t stacks\[NUM_TASKS \* 7\]; // (1)

/\*\*\* Hilfsfunktionen \*\*\*/

void create_task ( uint32_t n, //die ID/Nummer des Tasks uint16_t cs, uint16_t ss, uint16_t ds, uint32_t adr_code, uint32_T adr_stack) {

     if(n > NUM_TASKS) return;
     task_state_segments[n].cs = cs;
     task_state_segments[n].ds = ds;
     task_state_segments[n].ss = ss;
     task_state_segments[n].eip = adr_code;
     task_state_segments[n].esp = adr_stack;
     task_state_segments[n].eflags = 0x1600;    // (4)
     task_state_segments[n].ss0 = 0x10; // (2)
     task_state_segments[n].esp0 = (uint32_t) &stacks[n*7]; // (3)

} \</c\>

Diese Funktion kann man natürlich noch ausweiten. Einige Dinge muss man dennoch dazu sagen, die entsprechenden Codezeilen sind markiert: **1-3:** Da wohl keiner der Tasks im Ring 0 laufen wird, wie der Kernel, erfolgt bei einem Interrpt in den Ring 0 ein Stackwechsel. Das entsprechende Stacksegment / der Stackpointer wird im ss0- und esp0-Feld des TSS gespeichert. Damit sich die Stacks nicht gegenseitig überschreiben, bekommt jeder Task seinen eigenen Kernelstack. **4:** Dieses Bitmuster sorgt dafür, dass das Interruptflag gesetzt ist, was sehr wichtig ist, weil sonst das ganze System einfrieren würde. Natürlich kann man das EFLAGS-Bitmuster auch modifizieren, aber dieses hier eignet sich zu Anfgang.

### Schritt 2: TSS-Deskriptoren anlegen

Damit der Scheduler auch via jmp die TSS-Selektoren anspringen kann, legen wir die entsprechenden Deskriptoren an: \<c\>

1.  define TSS_SEL_BASE 30

void create_tss_descriptors () {

     int i;
     for(i=0; i<NUM_TASKS; i++)
     {
       gdt_create_descriptor (

i+TSS_SEL_BASE, (uint32_TD) &task_state_segment\[i\], sizeof(struct tss)-1, 0, GDT_TYPE_TSS);

     }

} \</c\>

### Schritt 3: Task-Tabelle anlegen

Jetzt benötigt man nur noch eine Tabelle, die alle Tasks beinhaltet. Da diese zum Scheduler gehört, gibt es hier keine hardwareseitigen Vorgaben. Folgender Tabellenaufbau ist nur ein Beispiel und kann nach Belieben verändert werden.

\<c\> struct task {

      uint8_t present;
      uint8_t priority;

}\_\_attribute\_\_((packed));

struct task task_table\[NUM_TASKS\]; \</c\>

Der Scheduler wird diese Tabelle später immer wieder durchlaufen. Wenn er ein present-Feld findet, das nicht null ist, führt er den zugehörigen Task aus. Das heißt, wir müssen in die obige Funktion create_task noch folgende Zeile einfügen:

\<c\>task_table\[n\].present=0xFF;\</c\>

### Schritt 4: Der Scheduler

Dieses doch recht kleine Codestück wird das eigentliche Multitasking übernehmen. Ich gehe dabei davon aus, dass in deinem OS bereits PIT und PIC initalisiert worden sind, denn in der [ISR](https://github.com/lowlevel-eu/wiki/wiki/Interrupt-Service-Routine "ISR") des [PITs](https://github.com/lowlevel-eu/wiki/wiki/Programmable-Interval-Timer "PIT") wird der Schedulercode ausgeführt.

Dafür muss er ersteinmal den nächsten Eintrag in der Task-Table finden, der aktiv ist (present-Feld ist nicht null)

\<c\> uint32_t current_task_id=0; uint16_t tss_sel; void scheduler() {

      current_task_id++;
      while(task_table[current_task_id].present==0)
      {
         current_task_id++;
         if (current_task_id == NUM_TASKS]) current_task_id=0;
      }
      tss_sel = current_task_id + TSS_SEL_BASE;

} \</c\> Jetzt muss zu diesem Task gewechselt werden, indem zu dessen TSS-Selektor gesprungen wird. Es empfiehlt sich diesen Teil in Assembler zu schreiben, da die ISR auch aus einem Assemblerstub heraus aufgerufen werden sollte. Dieser sieht dann so aus:

\<asm\> extern \_tss_sel extern \_scheduler global \_isr_pit \_isr_pit:

     pusha
     call _scheduler
     mov ax, [_tss_sel]
     mov [opcode_hack+5], ax
     popa
     opcode_hack:
     jmp 1234 : 1234

iret \</asm\>

Jetzt musst du nur noch "isr_pit" in deine IDT als PIT Interrupthandler eintragen, damit der Scheduler auch bei jedem Tick aufgerufen wird und zum nächsten Task wechselt.

### Schritt 5: Multitasking initalisieren

Eine kleine Funktion noch zum Schluss: \<c\> void init_mt(void) {

       asm("ltr %%ax" : : "a" (TSS_SEL_BASE*8) ); //Start-TSS-Selektor
       asm("sti");

} \</c\> Jetzt muss der Code nur noch zusammengesetzt werden: \<c\> int kernel_main() {

      int i;
      //...
      //remap_PIC()
      //init_PIT()
      //...
      for (i=0; i<NUM_TASKS; i++)
      {
         task_table[i].present = 0;
      }
      //hier muss create_task() aufgerufen werden, um die
      //verschiedenen Tasks zu erzeugen
      create_tss_descriptors();
      init_mt();
      for(;;); //idle-loop

} \</c\>

Beim nächsten Tick wird dann der Scheduler aufgerufen und verrichtet seine Arbeit.

## Tipps und Tricks

### Hardwaregestütztes Scheduling

Wie bereits erwähnt ist es möglich, auch das Scheduling zum Teil von der Hardware ausführen zu lassen. Dafür muss man den PIT-Interrupt als Task-Gate anlegen, die auf das TSS des nächsten Tasks zeigt. Dadurch wechselt die CPU automatisch zum nächsten Task. Dann setzt man Bit 0 im letzten DWord jeder TSS (Debug-Trap-Bit), wodurch jedes mal eine Debugexception nach einem Task-Switch ausgelöst wird, in der man dann das Task-Gate auf den nächsten Task zeigen lässt. Diese Methode ist allerdings sehr kompliziert, man kommt dennoch nicht um etwas Software-Scheduling herum, und ausprobiert habe ich es auch noch nicht.

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/8930/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2158/index.html)

<!-- MediaWiki page 2158; revision 8930; parent 8861; 2010-11-20T11:02:20Z -->
