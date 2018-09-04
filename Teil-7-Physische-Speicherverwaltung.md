# Teil 7 - Physische Speicherverwaltung

|  |  |  |
| ----------------------------------------------------------------------------------------------------------------- | ---------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| « [Teil 6 - Multitasking](https://github.com/lowlevel-eu/wiki/wiki/Teil-6-Multitasking "Teil 6 - Multitasking") | **Navigation** | [Teil 8 - Ein erstes Programm](https://github.com/lowlevel-eu/wiki/wiki/Teil-8-Ein-erstes-Programm "Teil 8 - Ein erstes Programm") » |

## Ziel

Wir haben mittlerweile zwei Kernelfunktionen, die als Tasks abwechselnd laufen und langweilige Dinge machen wie einen Buchstaben auszugeben. Jetzt wollen wir etwas weitergehen und beliebig viele Tasks langweilige Sachen machen lassen (solange uns der Speicher nicht ausgeht, jedenfalls).

Ich möchte hier auch gleich im Voraus erwähnen, dass wir langsam die Stellen hinter uns gebracht haben, wo wir entweder keine Wahl haben, wie es zu implementieren ist, oder wo es eine eindeutige Empfehlung gibt. Ab hier gibt es für die meisten Probleme mehrere gute Wege zum Ziel. Welche Wege man wählt, entscheidet am Ende, was für ein Kernel entsteht. Ich werde jeweils nur einen Weg beispielhaft ausführen, aber gelegentlich kurz auf andere Möglichkeiten hinweisen.

## Physische Speicherverwaltung

Fangen wir zunächst damit an, unseren Kernel von der Einschränkung zu befreien, dass er nur genau zwei Tasks ausführen kann. Eigentlich haben wir mit init_task schon eine ganz nette Schnittstelle, um neue Tasks zu erstellen - das einzige, was nicht so schön ist, ist dass wir den Task von Hand ins Array eintragen und ihm seine fest deklarierten Stacks geben müssen.

Für jeden Task im Voraus Speicher zu reservieren, ist zu unflexibel, also müssen die Variablen *stack_a*, *stack_b*, *user_stack_a* und *user_stack_b* weg. Die Funktion *init_task* braucht die entsprechenden Parameter jetzt auch nicht mehr, denn sie soll sich den benötigten Speicher jetzt selbst (und zwar zur Laufzeit) holen. Wir schreiben also ungefähr so etwas:

``` c
struct cpu_state* init_task(void* entry)
{
    uint8_t* stack = pmm_alloc();
    uint8_t* user_stack = pmm_alloc();
    ...
}
```

Den neuen Speicher muss uns die [physische Speicherverwaltung](https://github.com/lowlevel-eu/wiki/wiki/Physische-Speicherverwaltung "Physische Speicherverwaltung") (engl. *physical memory manager*, daher das *pmm*) zur Verfügung stellen. Die Aufgabe der Speicherverwaltung ist es - Überraschung - den vorhandenen Speicher zu verwalten, so dass zur Laufzeit neuer Speicher angefordert werden und auch wieder freigegeben werden kann. Man arbeitet an dieser Stelle üblicherweise mit Speicherblöcken einer festen Größe - auf x86 sind das üblicherweise 4 Kilobyte (was nicht völlig willkürlich ist: Wir werden später dazu kommen, dass das genau die Größe ist, mit der man für virtuellen Speicher auch arbeiten muss).

Bevor wir uns einer möglichen Implementierung widmen, möchte ich kurz die Funktionen aufzählen, die die Speicherverwaltung bieten muss. Der Artikel [Physische Speicherverwaltung](https://github.com/lowlevel-eu/wiki/wiki/Physische-Speicherverwaltung "Physische Speicherverwaltung") nennt einige Möglichkeiten, die Funktionen zu implementieren. Wer mag, kann hier gern eine andere Methode wählen und den nächsten Abschnitt nur überfliegen. Die Funktionen sind also:

- *pmm_init*: Inititalisiert die Speicherverwaltung. Alle Speicherbereiche, die beim Start des Systems frei sind, müssen als frei markiert werden, der Rest als belegt.
- *pmm_alloc*: Reserviert eine bislang freie Seite (ein Speicherblock von 4k) und gibt ihre Startadresse zurück.
- *pmm_free*: Gibt eine zuvor reservierte Seite wieder frei, damit sie von einem neuen *pmm_alloc* wieder benutzt werden kann.

### Speicher reservieren und freigeben

Eine relativ simple Art, den Speicher zu verwalten, ist eine Bitmap, daher benutzen wir sie hier als Beispiel. Die Idee ist ganz einfach, dass man für jede Seite (also für je 4k) ein Bit benutzt, das anzeigt, ob die Seite frei oder belegt ist. Man könnte die Datenstruktur also wie folgt definieren:

``` c
/*
 * Der Einfachheit halber deklarieren wir die maximal benoetige Bitmapgroesse
 * statisch (Wir brauchen 4 GB / 4 kB = 1M Bits; 1M Bits sind 1M/32 = 32k
 * Eintraege fuer das Array)
 *
 * Willkuerliche Festlegung: 1 = Speicher frei, 0 = Speicher belegt
 */
#define BITMAP_SIZE 32768
static uint32_t bitmap[BITMAP_SIZE];
```

Wenn jetzt zum Beispiel bitmap\[0\] = 0xc wäre, würde das bedeuten, dass die Seiten 2 und 3 frei sind (von Null an gezählt; also der Speicherbererich von 8k bis 16k) während die Seiten 0, 1 und 4 bis 31 belegt sind. Beim Reservieren einer neuen Seite geht man jetzt das Array durch bis man ein gesetztes Bit, also eine freie Seite findet. Man löscht dann das Bit und gibt die gefundene Adresse zurück. Beim Freigeben wird das Bit entsprechend wieder gesetzt.

Da die Implementierung offensichtlich ist, möchte ich sie hier nicht direkt in Code ausführen. Da man die Bitoperationen außerhalb des OS-Dev nicht ganz so oft braucht, hier nochmal eine kleine Übersicht:

    Angenommen x ist ein int und wir interessieren uns für ein Flag in Bit 5.
    Definieren wir also zunächst:

        #define FLAG (1 << 5)

    Wir können jetzt...

        ...prüfen, ob das Bit gesetzt ist:  (x & FLAG)
        ...das Bit setzen:                  x |= FLAG
        ...das Bit löschen:                 x &= ~FLAG

### Speicherverwaltung initialisieren

Eigentlich fehlt jetzt nur noch der Anfangszustand für die Speicherbitmap. Wir müssen dazu wissen, welche Speicherbereiche frei sind und wo wir besser nicht hinschreiben. Zum Glück weiß das BIOS das und GRUB gibt uns die entsprechende Information auch weiter. Wir ignorieren sie bisher nur.

Wenn unser Kernel gestartet ist, liegt im Register *ebx* ein Pointer auf die [Multiboot Information Structure](https://github.com/lowlevel-eu/wiki/wiki/Multiboot#multiboot-structure "Multiboot"). Der verlinkte Artikel enthält eine Tabelle über den Aufbau der Struktur, die wir am geschicktesten als C-struct deklarieren (zumindest bis zu den mmap-Feldern). Das Feld mbs_mmap_addr ist ein Pointer auf die gesuchten Daten und der Abschnitt [mbs_mmap_addr](https://github.com/lowlevel-eu/wiki/wiki/Multiboot#mbs_mmap_addr "Multiboot") enthält den Aufbau eines Eintrags der Memory Map.

Wir müssen also zunächst einmal zurück in die start.S und den Pointer weitergeben:

``` asm
// C-Code aufrufen und Multiboot-Infostruktur als Parameter uebergeben
push %ebx
call init
```

Und auch die init-Funktion gibt den Pointer einfach direkt weiter an pmm_init:

``` c
void init(struct multiboot_info *mb_info)
{
    pmm_init(mb_info);
    ...
```

pmm_init geht anschließend wie folgt vor:

1.  Zunächst wird der gesamte Speicher als belegt angesehen
2.  Anschließend wird der Speicher freigegeben, der in der Memory Map als frei gekennzeichnet ist
3.  Weil das BIOS aber nichts vom Betriebssystem weiß, müssen nachher alle Speicherbereiche, die das OS benutzt gleich wieder als belegt gekennzeichnet werden (d.h. in erster Linie der komplette Kernel)

Widmen wir uns zunächst der Memory Map. Wir haben Basisadresse und Länge und können damit über alle Einträge laufen und die freien Bereiche (Typ 1) als frei markieren:

``` c
struct multiboot_mmap* mmap = mb_info->mbs_mmap_addr;
struct multiboot_mmap* mmap_end = (void*)
    ((uintptr_t) mb_info->mbs_mmap_addr + mb_info->mbs_mmap_length);

while (mmap < mmap_end) {
    if (mmap->type == 1) {
        // Der Speicherbereich ist frei, entsprechend markieren
        uintptr_t addr = mmap->base;
        uintptr_t end_addr = addr + mmap->length;

        while (addr < end_addr) {
            pmm_free((void*) addr);
            addr += 0x1000;
        }
    }
    mmap++;
}
```

Den vom OS benutzten Speicher als belegt zu markieren (z.B. die Multiboot-Infostruktur oder zusätzliche Multiboot-Module) ist einfach und braucht wohl keine weitere Erläuterung. Die einzige Stelle, die nicht offensichtlich sein dürfte, ist, wie man herausbekommt, wo der Kernel eigentlich anfängt und aufhört. Dazu sagen wir dem Linker im Linkerskript, er soll ein neues Symbol vor den ganzen Sektionen anlegen und ein weiteres nach den Sektionen:

    ...

        . = 0x100000;

        /* Symbol fuer den Kernelanfang definieren */
        kernel_start = .;

        /*
         * Der Multiboot-Header muss zuerst kommen (in den ersten 8 kB).

    ...

            *(.bss)
        }

        /* Symbole fuer das Kernelende definieren (auf 4k aufrunden) */
        . = ALIGN(4096);
        kernel_end = .;
    }

In C können wir diese Symbole anschließend als extern-Variablen deklarieren. Da die Variable keinen Datentyp hat (es zeigt ja nur ein Symbol an diese Stelle, ohne dass dort Platz für irgendwelche Daten reserviert wäre), ist void die richtige Wahl (da dieses Nichts zudem so ziemlich unveränderlich ist, kann man gleich ein const void verwenden (sonst kann es passieren, dass der Compiler eine Warnung ausgibt)). Wir sind hinterher sowieso nur an der Adresse der Variablen interessiert:

``` c
extern const void kernel_start;
extern const void kernel_end;

uintptr_t addr = (uintptr_t) &kernel_start;
while (addr < (uintptr_t) &kernel_end) {
    pmm_mark_used((void*) addr);
    addr += 0x1000;
}
```

## Taskliste

Der Task muss jetzt aber immer noch von Hand ins task_states-Array geschrieben werden. Ein Array dazu noch, das besser kein Array wäre, denn wir wollen die Anzahl der Tasks ja nicht begrenzen. Es wäre also an der Zeit, eine verkettete Liste herzunehmen. Im Moment haben wir noch Task und Prozessorzustand gleichgesetzt, aber ein Task ist natürlich noch mehr. Daher wäre jetzt eine gute Gelegenheit, einen Task neu zu definieren:

``` c
struct task {
    struct cpu_state*   cpu_state;
    struct task*        next;
};

static struct task* first_task = NULL;
static struct task* current_task = NULL;
```

init_task muss jetzt statt nur dem Stack entsprechend auch eine Taskstruktur anlegen und zurückgeben (wobei sie strenggenommen gar nichts zurückgeben müsste, denn der Task wird jetzt gleich richtig überall eintragen. Aber irgendwann später können wir den Rückgabewert garantiert brauchen). Ändern wir also das Ende ab:

``` c
    /*
     * Neue Taskstruktur anlegen und in die Liste einhaengen
     */
    struct task* task = pmm_alloc();
    task->cpu_state = state;
    task->next = first_task;
    first_task = task;
    return task;
}
```

Der Scheduler muss jetzt statt den Arrayindex weiterzuzählen zum nächsten Listenelement weitergehen (current_task = current_task-\>next) und wenn das Ende erreicht ist (next also NULL ist), wieder beim ersten Task anfangen. Das Array task_states, num_tasks und das alte current_task mit dem Arrayindex sind jetzt unnötig geworden und können gelöscht werden. Einen neuen Task anzulegen bedeutet jetzt nur noch ein init_task mit dem passenden Einsprungpunkt aufzurufen.

|  |  |  |
| ----------------------------------------------------------------------------------------------------------------- | ---------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| « [Teil 6 - Multitasking](https://github.com/lowlevel-eu/wiki/wiki/Teil-6-Multitasking "Teil 6 - Multitasking") | **Navigation** | [Teil 8 - Ein erstes Programm](https://github.com/lowlevel-eu/wiki/wiki/Teil-8-Ein-erstes-Programm "Teil 8 - Ein erstes Programm") » |

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/11393/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2094/index.html)

<!-- MediaWiki page 2094; revision 11393; parent 7763; 2018-09-04T10:16:13Z -->
