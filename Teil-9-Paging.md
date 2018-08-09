# Teil 9 - Paging

|  |  |  |
| -------------------------------------------------------------------------------------------------------------------------------------- | ---------------- | ----- |
| « [Teil 8 - Ein erstes Programm](https://github.com/lowlevel-eu/wiki/wiki/Teil-8-Ein-erstes-Programm "Teil 8 - Ein erstes Programm") | **Navigation** |  |

  

## Ziel

Ein einzelnes Programm funktioniert nach dem letzten Teil, aber zwei Programme können sich ins Gehege kommen, weil sie denselben Speicher benutzen - wir brauchen noch irgendeinen Mechanismus, um sie voneinander zu trennen: Virtuellen Speicher, den wir über [Paging](https://github.com/lowlevel-eu/wiki/wiki/Paging "Paging") umsetzen werden.

## Tasks im Konflikt

Die Voraussetzungen, um mehrere Programme starten zu können, sind mittlerweile vorhanden: Anstatt nur das erste Multibootmodul zu starten, könnte *init_multitasking* eine Schleife enthalten, die einfach alle Multiboot-Module nacheinander startet. Wenn wir das mit diesem Testprogramm machen, scheint zunächst auch alles zu funktionieren und wir bekommen mit *-initrd test.bin,test.bin* die folgende Ausgabe:

    0123401234

Es gibt da nur ein kleines Problem: Alle diese Programme erwarten ihren Code und ihre Daten an einer bestimmten Stelle im Speicher. Und das zweite Programm möchte dabei natürlich denselben Speicher verwenden wie das erste. Dass es trotzdem scheinbar funktioniert, haben wir zwei Tatsachen zu verdanken:

- Es ist zweimal dasselbe Programm. Dass beim Laden das erste Programm direkt wieder vom zweiten überschrieben wird, ist egal, weil es sowieso dasselbe ist.
- Die Laufvariable *i* im Testprogramm liegt auf dem Stack, von dem jedes Programm seinen eigenen hat.

Durch eine einfache Abwandlung des Testprogramms wird der Fehler aber deutlich:

``` c
#include <stdint.h>

int i = 0;
void _start(void)
{
    int j = i + 5;
    for (; i < j; i++) {
        asm("int $0x30" : : "a" (0), "b" ('0' + i));
    }

    while(1);
}
```

Es wird sicher jeder zustimmen, dass dieses Programm eigentlich die gleiche Ausgabe haben sollte. Dadurch, dass *i* jetzt aber nicht mehr auf dem Stack, sondern in *.data* liegt, wird es aber zwischen den beiden Tasks geteilt und wir bekommen:

    0123456789

## Virtueller Speicher

Um den Konflikt zu beseitigen, gibt es zwei Möglichkeiten: Entweder das Programm wird so verändert, dass es damit zurechtkommt, an anderen Adressen zu laufen, oder wir kriegen es im OS irgendwie geregelt, die Programme zu trennen, aber trotzdem an ihrer Adresse laufen zu lassen.

Für die erste Variante gibt es zum Beispiel folgende Möglichkeiten ein, das umsetzen:

- Die Programme jeweils an eine andere Adresse linken. Offensichtlich, aber auch offensichtlich unflexibel: Jedes Programm braucht seine eindeutige Adresse, die kein anderes Programm belegt. Es kann insbesondere auch nur einmal laufen.
- Erst beim Programmstart dynamisch linken und dabei jeweils eine freie Adresse benutzen
- Das Programm wird als *Position Independent Code (PIC)* kompiliert, so dass es an jeder Adresse funktioniert

Die letzten beiden Punkte können beispielsweise sinnvolle Optionen sein, wenn man für Hardware ohne MMU programmiert. Auf x86 haben wir allerdings glücklicherweise Hardwareunterstützung und können die zweite Variante wählen: Das Programm sieht zwar eine bestimmte Adresse, aber diese Adresse muss nicht zwingend etwas mit der Adresse im physischen RAM zu tun haben, sondern kann ganz woanders hinzeigen. Die beiden Optionen, um dies umzusetzen, sind:

- Segmentierung: In der [GDT](https://github.com/lowlevel-eu/wiki/wiki/Global-Descriptor-Table "GDT") und/oder [LDT](https://github.com/lowlevel-eu/wiki/wiki/Local-Descriptor-Table "LDT") werden zusätzliche Segmente angelegt - eins für jedes Programm. Während wir bisher Segmente mit Basis 0 und Limit 4 GB benutzen, würde man dann Segmente mit anderer Basis und anderem Limit benutzen. Das erste Programm könnte z.B. Basis 0x10000000 und das zweite Basis 0x20000000 bekommen. Wenn Programm eins jetzt auf seine *virtuelle Adresse* 0x200000 zugreift, ist das in Wirklichkeit die *physische Adresse* 0x12000000. Das Limit wird entsprechend gesetzt, damit ein Programm keinen Zugriff auf den Speicher anderer Prozesse (oder des Kernels) hat.
- [Paging](https://github.com/lowlevel-eu/wiki/wiki/Paging "Paging"): Der komplette Speicher wird in *Seiten* (z.B. von 4 Kilobytes Größe) eingeteilt. Jeder Seite im *virtuellen Speicher* wird individuell eine entsprechende Seite im *physischen Speicher* zugeordnet. Vorteil gegenüber Segmentierung ist, dass ein einzelnes Segment immer noch am Stück im physischen Speicher liegen muss. Beim Paging kann ein virtuell zusammenhängender Bereich dagegen physisch beliebig verteilt sein. Dadurch wird beispielsweise Speicherfragmentierung vermieden und es ist leichter, die zugeteilte Speichergröße nachträglich zu erhöhen.

Virtueller Speicher bringt ganz nebenbei auch noch ein paar andere Vorteile mit sich: Erst dadurch werden Dinge wie Swapping oder Copy on Write möglich.

Wegen der erwähnten Flexibilität habe ich (wie die meisten anderen Betriebssysteme) Paging ausgewählt, um in unserem Kernel virtuellen Speicher umzusetzen.

Wenn man besonders abenteuerlustig ist, kann man übrigens Paging und Segmentierung auch gleichzeitig benutzen (tatsächlich gibt es in kleinem Umfang keinen Weg darum herum, wenn man Paging benutzt: Ein [TSS](https://github.com/lowlevel-eu/wiki/wiki/Task-State-Segment "TSS") braucht jeder, und das ist ein Segment mit echter Basis und Limit). Für diesen Fall sollte man sich die Reihenfolge merken, in der eine vom Code benutzte virtuelle Adresse umgesetzt wird:

- Zuerst übersetzt die Segmentierung die *virtuelle* in eine *lineare Adresse*
- Dann übersetzt Paging die *lineare Adresse* in eine *physische Adresse*

## Paging aktivieren

Nachdem wir uns mit den theoretischen Grundlagen ein bisschen befasst haben, kommen wir zur zentralen Frage: Wie schaltet man Paging ein? Die einfach Antwort lautet: Das Paging-Bit (Bit 31) im Steuerregister *cr0* muss gesetzt werden (direkt nach dem Initialisieren der physischen Speicherverwaltung ist vermutlich ein guter Platz, um *vmm_init* aufzurufen):

``` c
void vmm_init(void)
{
    uint32_t cr0;

    asm volatile("mov %%cr0, %0" : "=r" (cr0));
    cr0 |= (1 << 31);
    asm volatile("mov %0, %%cr0" : : "r" (cr0));
}
```

Wenn wir den Kernel jetzt aber ausprobieren, merken wir schnell, dass das so keine gute Idee war: Ein Triple Fault führt dazu, dass es einen CPU-Reset gibt. Was ist passiert? Schauen wir uns an, was qemu dazu zu sagen hat: Mit dem Paramenter *-d int,cpu_reset* werden alle Interrupts in die Logdatei in */tmp/qemu.log* geschrieben (unter Windows kann im Monitor per *logfile* ein anderer Pfad gesetzt werden; ab qemu 0.13 wird standardmäßig *qemu.log* im aktuellen Verzeichnis benutzt). Die interessanten Einträge sehen (mit zusammengekürztem Registerdump) wie folgt aus:

         0: v=0e e=0000 i=0 cpl=0 IP=0008:0000000000100385 pc=0000000000100385 SP=0010:0000000000105fd4 CR2=0000000000100385
    EAX=80000011 EBX=00009500 ECX=0000000b EDX=00000002
    ESI=00000000 EDI=0012c000 EBP=00105fe4 ESP=00105fd4
    EIP=00100385 EFL=00000002 [-------] CPL=0 II=0 A20=1 SMM=0 HLT=0
    CR0=80000011 CR2=00100385 CR3=00000000 CR4=00000000

    check_exception old: 0xe new 0xe
         1: v=08 e=0000 i=0 cpl=0 IP=0008:0000000000100385 pc=0000000000100385 SP=0010:0000000000105fd4 EAX=0000000080000011
    EAX=80000011 EBX=00009500 ECX=0000000b EDX=00000002
    ESI=00000000 EDI=0012c000 EBP=00105fe4 ESP=00105fd4
    EIP=00100385 EFL=00000002 [-------] CPL=0 II=0 A20=1 SMM=0 HLT=0
    CR0=80000011 CR2=00000070 CR3=00000000 CR4=00000000

    check_exception old: 0x8 new 0xe
    Triple fault
    CPU Reset (CPU 0)
    EAX=80000011 EBX=00009500 ECX=0000000b EDX=00000002
    ESI=00000000 EDI=0012c000 EBP=00105fe4 ESP=00105fd4
    EIP=00100385 EFL=00000086 [--S--P-] CPL=0 II=0 A20=1 SMM=0 HLT=0
    CR0=80000011 CR2=00000040 CR3=00000000 CR4=00000000

*v=0e* verrät den Interrupt, mit dem alles angefangen hat. Interrupt 0x0e = 14 ist eine Exception, und zwar genauer gesagt ein *Page Fault* (#PF). Der Page Fault sagt uns, dass Paging angeschaltet ist und beim Zugriff auf eine (virtuelle) Adresse ein Problem gemacht hat. Das Steuerregister *cr2* verrät uns, welche Adresse das war, und der Fehlercode welcher Art der Fehler war:

| Bit | Wert | Beschreibung |
| ----- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 0 | 0x1 | 0: Der virtuellen Adresse ist keine physische Adresse zugeordnet (sie ist nicht *gemappt*)<br>1: Die Seite ist gemappt, aber eine Berechtigung fehlt (z.B. Schreiben auf eine schreibgeschützte Seite)<br> |
| 1 | 0x2 | 0: Der fehlerhafte Zugriff war ein Lesezugriff 1: Der fehlerhafte Zugriff war ein Schreibzugriff<br> |
| 2 | 0x4 | 0: Der Zugriff war im Kernel (Ring 0, 1 oder 2) 1: Der Zugriff war im Userspace (Ring 3)<br> |

Mit *e=0000* wissen wir also, dass der Kernel von Adresse 0x100385 lesen wollte, aber die Seite nicht gemappt war. Eine Suche nach dem Wert von eip in der Ausgabe von objdump verrät uns auch, wo dieser Zugriff passiert ist:

      100382:       0f 22 c0                mov    %eax,%cr0
      100385:       c9                      leave
      100386:       c3                      ret

Er wollte also einfach die nächste Instruktion ausführen (deswegen sind eip und cr2 auch gleich). Beim Zugriff auf den Speicher (die Instruktion will ja erst einmal eingelesen werden) hat es dann geknallt, weil wir nicht gesagt haben, welche virtuelle Adresse an welcher physischen Adresse liegt.

Der Rest ist einfach: Beim Versuch, einen Page Fault auszulösen, ist der Zugriff auf die IDT schiefgegangen. Das führt zu einem Double Fault, dessen Handler ebenfalls nicht ausgeführt werden kann, weil die IDT immer noch nicht gelesen werden kann. Und damit sind wir beim Triple Fault, der quasi als letzten Ausweg einen CPU-Reset zur Folge hat.

## Page Directory und Page Tables

Bevor wir Paging anschalten, müssen wir dem Prozessor also erst einmal mitteilen wie unser virtueller Adressraum aussehen soll. Das Prinzip von Paging ist einfach: Wie oben erwähnt wird der gesamte Speicher in Pages von 4k Größe eingeteilt. Wir müssen im Prinzip nur noch in eine große Tabelle eintragen, welche physische Adresse gemeint ist, wenn eine bestimmte virtuelle Adresse angesprochen wird (siehe [Paging#Funktionsweise](https://github.com/lowlevel-eu/wiki/wiki/Paging#funktionsweise "Paging")).

Weil eine einzige große Tabelle aber in der Regel zu viel Speicher verschwenden würde, wird auf i386 aber ein zweistufiges System eingesetzt: Blöcke von jeweils 1024 Pages (also 4 MB) werden in einer *Page Table* beschrieben. Das *Page Directory* enthält dann Verweise auf die einzelnen Page Tables. Wenn eine Page Table nicht benötigt wird, kann sie im Page Directory einfach weggelassen werden (z.B. 0 als Eintrag) und wir haben 4k Speicher gespart.

Aber fangen wir zunächst einfach einmal damit an, unseren virtuellen Adressraum (auch *Speicherkontext* genannt) in Code zu gießen. Der gesamte Adressraum wird durch das Page Directory beschrieben. Wir haben also folgendes (später kommt hier noch mehr dazu, deswegen gleich ein struct):

``` c
struct vmm_context {
    uint32_t* pagedir;
};
```

Ein neues leeres Page Directory anzulegen ist auch nicht schwer: Wir holen uns einfach eine freie Page (sowohl Page Directory als auch Page Tables sind genau 4k groß) und schreiben sie mit Nullen voll:

  

``` c
struct vmm_context* vmm_create_context(void)
{
    struct vmm_context* context = pmm_alloc();
    int i;

    /* Page Directory anlegen und mit Nullen initialisieren */
    context->pagedir = pmm_alloc();
    for (i = 0; i < 1024; i++) {
        context->pagedir[i] = 0;
    }

    return context;
}
```

Jetzt müssen wir in diesem Page Directory nur noch die passenden *Mappings* anlegen, d.h. für jede benutzte virtuelle Adresse die zugehörige physische Adresse angeben. Im Moment ist das nicht besonders schwer. Wir müssen folgendermaßen vorgehen:

1.  Berechnen, welche Pagenummer die Adresse hat, die wir mappen wollen (d.h. durch 4096 teilen)
2.  Die Indizes in den Tabellen berechnen (wir erinnern uns: eine Page Table hat 1024 Einträge)
    - Im Page Directory ist das also *Pagenummer / 1024*
    - In der Page Table ist es *Pagenummer mod 1024*
3.  Wenn die passende Page Table im Page Directory schon eingetragen ist, die Adresse der Page Table auslesen. Wenn nicht, eine neue Page allozieren, mit Nullen initialisieren und ihre physische Adresse ins Page Directory eintragen
4.  In der Page Table am richtigen Index die physische Adresse eintragen
5.  Den TLB für die neu gemappte virtuelle Adresse invalidieren

Wie sieht nun ein Eintrag in einer Page Table oder einem Page Directory aus? Es ist einfach eine physische Adresse mit 4k-Alignment, so dass die letzten 12 Bits unbenutzt sind und für ein paar Flags benutzt werden können. Die wichtigsten Felder sind:

| Bit | Maske | Beschreibung |
| -------------- | ------------ | ------------------------------------------------------------------------------------------------ |
| 0 | 0x1 | Gesetzt, wenn das Mapping gültig ist (dieses Bit auf 0 setzen für unbenutzte Pages) |
| 1 | 0x2 | Gesetzt, wenn die Page beschreibbar sein soll |
| 2 | 0x4 | Gesetzt, wenn der Userspace auf die Seite zugreifen können soll |
| 12 &#150; 31 | 0xfffff000 | Physische Adresse der Page (in einer Page Table) bzw. der Page Table (in einem Page Directory) |

Für Kernelspeicher fährt man also mit der Formel *pte = phys_addr \| 0x3* am besten (PTE = *Page Table Entry*). Nicht zu vergessen ist nach jeder Änderung einer (aktiven) Page Table den TLB für die virtuelle Adresse zu invalidieren: Der Prozessor cacht im TLB einige PTEs, damit er nicht bei jedem Speicherzugriff zunächst langwierig die Paging-Strukturen durchgehen muss. Wenn man den TLB nicht invalidiert (d.h. den entsprechenden Eintrag aus dem TLB löscht; entweder mit der Instruktion *invlpg* oder durch Neuladen des Steuerregisters *cr3*), kann der Page-Table-Eintrag im Speicher geändert sein, aber es wird weiterhin die alte Adresse benutzt. Eine Quelle für sehr unangenehm zu debuggende Fehler!

Nachdem das alles erledigt ist, muss das Page Directory auch noch aktiviert werden. Das aktuelle Page Directory steht im Steuerregister *cr3*, wir müssen also einfach dorthin die Adresse des vorbereiteten Page Directory schreiben. Zusammenfassend haben wir also in etwa folgenden Code:

  

``` c
int vmm_map_page(struct vmm_context* context, uintptr_t virt, uintptr_t phys)
{
    /* Page Table heraussuchen bzw. anlegen */
    ...

    /* Neues Mapping in the Page Table eintragen */
    page_table[pt_index] = phys | PTE_PRESENT | PTE_WRITE;
    asm volatile("invlpg %0" : : "m" (*(char*)virt));

    return 0;
}

void vmm_activate_context(struct vmm_context* context)
{
    asm volatile("mov %0, %%cr3" : : "r" (context->pagedir));
}

/*
 * Dieser Speicherkontext wird nur waehrend der Initialisierung verwendet.
 * Spaeter laeuft der Kernel immer im Kontext des aktuellen Prozesses.
 */
static struct vmm_context* kernel_context;

void vmm_init(void)
{
    uint32_t cr0;
    int i;

    /* Speicherkontext anlegen */
    kernel_context = vmm_create_context();

    /* Die ersten 4 MB an dieselbe physische wie virtuelle Adresse mappen */
    for (i = 0; i < 4096 * 1024; i += 0x1000) {
        vmm_map_page(kernel_context, i, i);
    }

    vmm_activate_context(kernel_context);

    asm volatile("mov %%cr0, %0" : "=r" (cr0));
    cr0 |= (1 << 31);
    asm volatile("mov %0, %%cr0" : : "r" (cr0));
}
```

Mit diesem Code funktioniert unser Kernel jetzt wieder. Er bricht allerdings mit einer Exception 14 (einem Page Fault) ab: Das passiert, sobald er in einen Userspace-Task springen möchte. Bisher haben wir alle Pages nur für den Kernel gemappt. Man könnte jetzt natürlich hergehen und einfach das User-Flag setzen, dann funktionieren auch die Tasks wieder. Aber zukunftsfähig ist die Methode, einfach mal die ersten vier Megabytes zu mappen natürlich nicht.

## Aufteilung des Adressraums

Bevor wir nun daran gehen, das endgültige und etwas sauberere Mapping aufzusetzen, müssen wir uns erst einmal darüber klar werden, wie es dann genau aussehen muss. Es gibt an dieser Stelle wieder einmal mehrere Möglichkeiten, aber ein paar Dinge sind auf jeden Fall klar:

- Ein Prozess darf den Speicher keines anderen Prozesses lesen oder schreiben. Das bedeutet in der Regel, dass jeder Prozess sein eigenes Page Directory bekommt, in dem nur Seiten vorkommen, die zum Prozess gehören.
- Ein Prozess darf den Speicher des Kernels nicht lesen oder schreiben. Dafür gibt es das User-Bit in den Pagetable-Einträgen.
- Zumindest Teile des Kernels müssen in allen Prozessen gemappt sein, nämlich die GDT, die IDT und das TSS.
  - Anfänger versuchen oft, dem Kernel ein eigenes Page Directory zu geben. Das geht grundsätzlich (mit der obigen Einschränkung), aber dabei muss man beachten, dass Kontextwechsel (also das Laden eines neuen Page Directory) teuer ist und diese Methode daher Systemaufrufe verlangsamen kann.
  - In der Regel mappt man den vollständigen Kernel in allen Prozessen

Wenn man für den Kernel kein eigenes Page Directory benutzt, sondern ihn immer mappt, muss man darauf achten, dass er auch in allen Page Directories gleich gemappt ist. Deswegen empfiehlt es sich, die auf i386 vorhandenen 4 GB virtuellen Adressraum in zwei große Bereiche einzuteilen: Einen für den Kernel und einen für den Userspace. Wenn die Größe des Kernelbereichs durch 4 MB teilbar ist, können in allen Page Directories für den Kernel einfach dieselben Page Tables wiederverwendet werden. Um alle Page Directories dauerhaft gleich zu halten, gibt wieder zwei Ansätze:

- Entweder man merkt sich, welches Page Directory zuletzt im Kernelbereich geändert worden ist und kopiert von dort, wenn zu einem Page Directory gewechselt wird, das noch nicht auf dem aktuellen Stand ist
- Oder man legt alle Page Tables für den Kernelspeicher einfach gleich am Anfang an, dann bleibt das Page Directory unverändert und alle Kopien sind immer auf dem gleichen Stand (dafür kostet es ein wenig Speicher)

Die verbreitetste Aufteilung des Speichers ist 1 GB für den Kernel und 3 GB für den Userspace, aber man hört auch gelegentlich von der umgekehrten oder einer 2/2-Aufteilung. Aber nachdem man sich für eine Größe entschieden hat, muss auch noch entschieden werden, wo im virtuellen Speicher die Bereiche genau liegen:

- 0-1 GB für den Kernel, 1-4 GB für den Userspace ist sehr einfach zu implementieren, weil man für den Kernelcode dann ein 1:1-Mapping beibehalten kann
- 0-3 GB für den Userspace, 3-4 GB für den Kernel (ein *Higher Half Kernel*) ist etwas komplizierter, weil der Teil des Kernelcodes vor dem Einschalten von Paging mit physischen Adressen arbeiten muss und der folgende Code mit virtuellen Adressen. Er wird dafür gelegentlich als schöner empfunden. Ein praktischer Vorteil ist es, dass VM86-Tasks (die als Userspace angesehen werden sollten) zwingend im Bereich von 0-1 MB laufen müssen.

## Dynamisches Mapping

Bisher werden einfach beim Start des Kernels auf Verdacht die ersten 4 MB gemappt. Auf Dauer ist das natürlich nicht ausreichend, und wir haben damit auch keine Trennung zwischen Kernel und Userspace erreicht, d.h. Programme können den Kernel beliebig manipulieren. Was wir also wirklich wollen, ist bei Bedarf zu mappen:

- Beim Kernelstart müssen einige Bereiche gemappt werden
  - Der Kernelcode selbst
  - Der Videospeicher von B8000 bis BFFFF
  - Evtl. Multiboot-Strukturen, die noch verwendet werden sollen
  - Zum Zeitpunkt der Paging-Initialisierung schon dynamisch angelegte Kerneldaten, z.B. die Bitmap der physischen Speicherverwaltung
- Aus allen *pmm_alloc*-Aufrufen müssen *vmm_alloc*-Aufrufe werden, wobei *vmm_alloc* eine Funktion ist, die physischen Speicher reserviert und ihn gleich auch noch mappt, und anschließend die virtuelle Adresse zurückgibt
- Beim Anlegen des Userspace-Speichers muss das User-Bit in den PTEs gesetzt sein

Die Umsetzung erscheint auf den ersten Blick ganz einfach, aber es gibt dabei noch ein Problem: Bisher haben wir das Mapping immer angelegt, während Paging noch ausgeschaltet war. Wenn Paging jetzt aber schon an ist und wir ein neues Mapping durchführen wollen, müssen wir eine gültige virtuelle Adresse der Page Table haben. Das heißt, wenn die Paging-Strukturen selbst nicht mehr gemappt sind, haben wir keine Chance, sie jemals wieder zu ändern!

- Für das Mappen eines Page Directory und allen zugehörigen Page Tables gibt es einen Trick: Wenn ein Eintrag eines Page Directory wieder auf ein Page Directory (z.B. sich selbst) zeigt, dann wird dieses Page Directory an dieser Stelle als Page Table verwendet. Dadurch werden alle enthaltenen Page Tables hintereinander in den virtuellen Speicher gemappt. Dieser Trick wird oft für das aktuelle Page Directory benutzt, d.h. ein bestimmter Eintrag in jedem PD zeigt wieder auf das PD selbst.
- Für andere Page Directories kann man die Page Table temporär mappen.

## Auflösung des Konflikts

Nachdem der Kernel darauf vorbereitet ist, Speicherbereiche einzeln zu mappen und mit den richtigen Berechtigungen zu versehen, können wir uns endlich daran machen, den Konflikt unserer beiden Tasks aufzulösen. Dazu erweitern wir zunächst die Taskstruktur um einen Eintrag für das Page Directory (ja, unsere Tasks entsprechen im Moment Prozessen - mehrere Threads würden denselbenb Adressraum benutzen, wenn wir sie denn unterstützen würden).

``` c
struct task {
    struct cpu_state*   cpu_state;
    struct task*        next;
    struct vmm_context* context;
};
```

Beim Anlegen eines Tasks müssen wir jetzt einen neuen Speicherkontext anlegen (dafür gibt es ja schon *vmm_create_context*) und ggf. den Kernelteil des Page Directory kopieren. *init_elf* kann den Speicher jetzt im Kernel an eine beliebige Stelle im aktuellen Page Directory mappen, muss das Programm aber zusätzlich noch in dessen Page Directory an die richtige Stelle (nämlich 0x200000) mappen.

Den Wechsel des Page Directory kann man am Ende des Interrupt-Handlers durchführen:

``` c
struct cpu_state* handle_interrupt(struct cpu_state* cpu)
{
    ...

    if (cpu != new_cpu) {
        asm volatile("mov %0, %%cr3" : : "r" (current_task->context->pagedir_phys));
    }

    return new_cpu;
}
```

Weil ein Kontextwechsel teuer ist, wird cr3 nur dann neu geladen, wenn tatsächlich ein anderer Task laufen soll. Außerdem brauchen wir jetzt für cr3 die *physische* Adresse des Page Directory. *vmm_create_context* muss also sowohl die virtuelle als auch die physische Adresse abspeichern, damit wir mit dem Page Directory arbeiten können.

Nachdem alle Mappings korrekt aufgesetzt sind und das aktuelle Page Directory beim Taskwechsel geändert wird, steht nun nichts mehr im Weg, zwei unserer Beispielprogramm gleichzeitig laufen zu lassen - ohne dass sie sich unabsichtlich gegenseitig beeinflussen.

  

|  |  |  |
| -------------------------------------------------------------------------------------------------------------------------------------- | ---------------- | ----- |
| « [Teil 8 - Ein erstes Programm](https://github.com/lowlevel-eu/wiki/wiki/Teil-8-Ein-erstes-Programm "Teil 8 - Ein erstes Programm") | **Navigation** |  |

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/11384/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2358/index.html)

<!-- MediaWiki page 2358; revision 11384; parent 10968; 2018-08-09T17:50:35Z -->
