# Hardware-Multitasking

Im Gegensatz zum häufig eingesetzten Software Multitasking, übernimmt beim Hardware Multitasking die CPU die Aufgaben des Dispatchers. Viele moderne Betriebssysteme verzichten auf Hardware Multitasking, da es angeblich keinen großen Zeitvorteil gegenüber dem Software Multitasking hat.

## Grundlagen

### Das Task State Segment

Das Hardware Multitasking beruht auf dem sogenannten Task State Segment, welches jedem Task zugeordnet wird und unter anderem dessen Registerwerte speichert. Der Aufbau des TSS wird hier exakt beschrieben. Vereinfacht sieht er so aus:

Datei:Tss.jpg

Die dynamischen Felder werden von der CPU automaitsch beim TaskWechsel mit den entsprechenden Registerwerten des laufenden Tasks gefüllt. Die statischen Felder werden mit Anfangswerten belegt und später nicht mehr verändert. Meiner Meinung nach nicht so entsprechend sind die unwichtigen Felder. (alle Felder haben DWORD Größe) Der Speicherort des TSS wird als Eintrag in der GDT gespeichert. Der Selektor dieses Eintrags wird im Task Register der CPU gespeichert, wodurch die diese bei einem Taskwechsel weiß, wo sie die (dynamischen) Registerwerte speichern soll, damit diese beim Wiederaufruf des Tasks unverändert sind. Folgender Code legt ein TSS an, und erzeugt dann den Descriptor in der GDT an, der darauf zeigt.

\<c\>

1.  define GDT_TYPE_TSS 0x89

struct tss task_state_segment; gdt_create_descriptor ( n, //die Nummer des Descriptor-Eintrags (DWORD) &task_state_segment, //Adresse sizeof(struct tss)-1, //Länge 0, //flags GDT_TYPE_TSS); //access \</c\>

## Taskwechsel

Für einen Taskwechsel (TaskSwitch) springt man mit einem jmp-Befehl zum Selektor der TSS, der dem neuen Task zugeordnet ist:

\<asm\>Jmp TSS_SELECTOR : 0000\</asm\>

(Das RPL des TSS_SELECTORS sowie das Offset werden von der CPU ignoriert.)

Dieser Befehl sorgt dafür, dass die CPU die Registerwerte des aktuellen Tasks in dessen TSS speichert, dessen Selektor ist im TaskRegister gespeichert. Dann lädt die CPU den im jmp-Befehl angegebenen neuen Selektor ins TaskRegister und schreibt die Werte des zugehörigen TSS in die Register, wodurch die Registerwerte des Tasks, zu dem durch den jmp-Befehl gewechselt werden soll, wiederhergestellt werden. Allerdings gibt es hier ein kleines Problem:

\<asm\>jmp ax : 0000\</asm\>

...funktioniert nicht. Daher muss man sich eines kleinen Tricks bedienen: \<asm\> mov \[opcode_hack+5\], ax opcode_hack: jmp 1234 : 1234 \</asm\>

Das sieht nicht schön aus, ist aber die einzige Möglichkeit „dynamisch“ zu springen. Ich hoffe ich habe diesen Code korrekt in die AT&T Assembler Syntax (siehe unten) übertragen, da ich den Code nicht vollständig getestet habe.

  
Zu beachten ist allerdings, dass der TaskWechsel von der Software (dem Scheduler) implementiert werden muss, weil die CPU nur das Disptching übernimmt. Es gibt zwar einen Trick, wie man das Scheduling auch von der CPU ausführen lassen kann, aber diese Möglichkeit würde ich nicht empfehlen (siehe dazu unten). Außerdem sollte man wissen, dass man den TaskSwitch auch mit einem Call oder Int-Befehl ausführen kann, was allerdings etwas komplizierter ist.

### Initialisierung

Bevor überhaupt ein TaskSwitch ausgeführt werden kann, muss einmal ein Start-TSS-Selektor in das TaskRegister geladen werden. Dazu dient folgender Befehl:

\<asm\> mov ax, 3\*8 ltr ax \</asm\>

Diese Sequenz lädt den dritten Selektor in das TaskRegister. Dieser muss auf einen gültigen TSS-Descriptor zeigen, der wiederrum die Adresse des TSS des Starttasks angibt. (Der dritte Selektor wurde hier nur als Beispiel verwendet)

## Implementierung

Schritt 1: Task State Segmente anlegen

Jeder spätere Task benötigt ein TSS. Diese müssen mit den Werten gefüllt werden, die der Task zu Beginn seiner Ausführung in den Registern stehen haben soll:

\<c\>

1.  define NUM_TASKS 10 //oder wieviele auch immer du möchtest

struct tss task_state_segments\[NUM_TASKS\]; DWORD stacks\[NUM_TASKS \* 7\]; // (1)

/\*\*\* Hilfsfunktionen \*\*\*/

void create_task ( DWORD n, //die ID/Nummer des Tasks WORD cs, WORD ss, WORD ds, DWORD adr_code, DWORD adr_stack) {

     if(n > NUM_TASKS) return;
     task_state_segments[n].cs = cs;
     task_state_segments[n].ds = ds;
     task_state_segments[n].ss = ss;
     task_state_segments[n].eip = adr_code;
     task_state_segments[n].esp = adr_stack;
     task_state_segments[n].eflags = 0x1600;    // (4)
     task_state_segments[n].ss0 = 0x10; // (2)
     task_state_segments[n].esp0 = (DWORD) &stacks[n*7];    // (3)

} \</c\>

Diese Funktion kann man natürlich noch ausweiten. Einige Dinge muss man dennoch dazu sagen, die entsprechenden Codezeilen sind markiert: **1-3:** Da wohl keiner der Tasks im Ring0 laufen wird, wie der Kernel, erfolgt bei einem Interrpt in den Ring0 ein Stackwechsel. Das entsprechende Stacksegment / der Stackpointer wird im ss0 und esp0 Feld des TSS gespeichert. Damit sich die Stacks nicht gegenseitig überschreiben, bekommt jeder Task seinen eigenen Kernelstack. **4:** Dieses Bitmuster sorgt dafür, dass das Interruptflag gesetzt ist, was sehr wichtig ist, weil sonst das ganze System einfrieren würde. Natürlich kann man das EFLAGS Bitmuster auch modifizieren, aber dieses hier eignet sich zu Anfgang.

### Schritt 2: TSS-Deskriptoren anlegen

Damit der Scheduler auch via jmp die TSS-Selektoren anspringen kann, legen wir die entsprechenden Deskriptoren an: \<c\>

1.  define TSS_SEL_BASE 30

void create_tss_descriptors () {

     int i;
     for(i=0; i<NUM_TASKS; i++)
     {
       gdt_create_descriptor (

i+TSS_SEL_BASE, (DWORD) &task_state_segment\[i\], sizeof(struct tss)-1, 0, GDT_TYPE_TSS);

     }

} \</c\>

### Schritt 3: Task Tabelle anlegen

Jetzt benötigt man nur noch eine Tabelle, die alle Tasks beinhaltet. Da diese zum Scheduler gehört, gibt es hier keine Hardwareseitigen Vorgaben. Folgender Tabellenaufbau ist nur ein Beispiel und kann nach Belieben verändert werden.

\<c\> struct task {

      BYTE present;
      BYTE priority;

}\_\_attribute\_\_((packed));

struct task task_table\[NUM_TASKS\]; \</c\>

Der Scheduler wird diese Tabelle später immer wieder durchlaufen. Wenn er ein present-Feld findet, das nicht Null ist, führt er den zugehörigen Task aus. Das heißt wir müssen in die obige Funktion create_task noch folgende Zeile einfügen:

\<c\>task_table\[n\].present=0xFF;\</c\>

### Schritt 4: Der Scheduler

Dieses doch recht kleine Codestück wird das eigentliche Multitasking übernhemen Ich gehe dabei davon aus, dass in deinem OS bereichts PIT und PIC initalisiert worden sind, denn denn immer wenn der PIT „feuert“, dann wechselt der Scheduler zum nächsten Task. Dafür muss er ersteinmal den nächsten Eintrag in der TaskTable finden, der aktiv ist (pressnet-Feld ist nicht Null)

\<c\> DWORD current_task_id=0;

void irq_pit(DWORD cs, DWORD eflags) //das hier ist ein Interupt {

      current_task_id++;
      while(task_table[current_task_id].present==0)
      {
         current_task_id++;
         if (current_task_id = NUM_TASKS]) current_task_id=0;
      }

\</c\> Jetzt muss zu diesem Task geswechselt werden, indem zu dessen TSS-Selektor gesprungen wird: \<c\>

     asm(„mov %%ax, *$lf+5;“
         „1:“
         „ltr $1234:$1234;“ :

 : „a“ (8\*(current_task_id + TSS_SEL_BASE));

     asm(„leave; iret“);     //nicht vergessen: interrupt!

} \</c\> Dieser Code kann natürlich noch erweitert werden, zum Beispiel, wenn man jedem Task eine unterschiedliche Priorität zuweist. Eventuell ist hier die AT&T Syntax falsch, da ich mit dieser nicht ganz vertraut bin.

### Schritt 5: Multitasking initalisieren

Eine kleine Funktion noch zum Schluss: \<c\> void init_mt(void) {

       asm(„ltr %%ax“ : : „a“ (TSS_SEL_BASE*8) ); //StartTssSselektor
       asm(„sti“);

} \</c\> Jetzt muss der Code nur noch zusammengesetzt werden: \<c\> int kernel_main() {

     int i;

//... //remap_PIC() //init_PIT() //...

      for (i=0; i<NUM_TASKS; i++)
      {
         task_table[i].present = 0;
      }

//hier muss create_task() aufgerufen werden, um die //verschiedenen Tasks zu erzeugen

      create_tss_descriptors();
      init_mt();
      for(;;);  //idle-loop

} \</c\>

Beim nächsten Tick wird dann der scheduler aufgerufen und verrichtet seine Arbeit.

## Tipps und Tricks

### Hardwaregestütztes Scheduling

Wie bereits erwähnt ist es möglich, auch das Scheduling zum Teil von der Hardware ausführen zu lassen. Dafür muss man den PIT-Interrupt als TaskGate anlegen, die auf das TSS des nächsten Tasks zeigt. Dadurch wechselt die CPU automatisch zum nächsten Task. Dann setzt man Bit 0 im letzten DWORD jeder TSS (Debug-Trap-Bit), wodurch jedes mal eine Debugexception nach einem TaskSwich ausgelöst wird, in der man dann das TaskGate auf den nächsten Task zeigen lässt. Diese Methode ist allerdings sehr kompliziert, man kommt dennoch nicht um etwas Software Scheduling herum, und ausprobiert habe ich es auch noch nicht.

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/6835/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2158/index.html)

<!-- MediaWiki page 2158; revision 6835; parent 0; 2010-01-08T19:33:47Z -->
