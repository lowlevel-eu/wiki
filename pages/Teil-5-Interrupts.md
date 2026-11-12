# Teil 5 - Interrupts

|  |  |  |
| -------------------------------------------------------------------------------------------------------------- | ---------------- | ----------------------------------------------------------------------------------------------------------------- |
| « [Teil 4 - Hello World](Teil-4-Hello-World.md "Teil 4 - Hello World") | **Navigation** | [Teil 6 - Multitasking](Teil-6-Multitasking.md "Teil 6 - Multitasking") » |

## Das Ziel

In diesem Teil wollen wir unserern Kernel *Interrupts* behandeln lassen. Ein Interrupt ist eine Unterbrechnung des aktuell ausgeführten Code, um eine Kernelfunktion (den *Interrupt-Handler*) aufzurufen. Es gibt drei unterschiedliche interessante Arten von Interrupts und keine davon ist für ein Betriebssystem verzichtbar:

- [Exceptions](Exception.md "Exception") treten bei Fehlern auf. Der Kernel kann in manchen Fällen den Fehler beheben und das unterbrochene Programm fortsetzen. In anderen Fällen bleibt ihm nicht anderes übrig als das Programm (möglicherweise sich selbst) abzubrechen und eine Fehlermeldung auszugeben.
- [IRQs](Programmable-Interrupt-Controller.md#irq-tabelle "IRQ") (auch *Hardware-Interrupts*) werden von angeschlossener Hardware ausgelöst. Sie müssen vom passenden Treiber verarbeitet werden. Beispielsweise löst das Diskettenlaufwerk einen IRQ aus, wenn es einen Lesebefehl fertig ausgeführt hat oder eine Netzwerkkarte, wenn sie ein Ethernetpaket empfangen hat.
- *Software-Interrupts* werden gezielt von Programmen aufgerufen, z.B. mit der *int*-Instruktion. Das häufigste Einsatzgebiet ist der Aufruf von *Syscalls*, also von Kernelfunktionen, in Programmen.

## Global Descriptor Table

Die Multibootspezifikation garantiert uns, dass unser Kernel bei seinem Aufruf mit Segmenten arbeitet, die bei Null beginnen und die gesamten 4 GB abdecken, die i386 unterstützt. Sie macht aber keine Angaben darüber, welche Werte genau in den Segmentregistern stehen. Sobald wir ein Segmentregister neu laden wollen, müssen wir das also wissen. Weil ein Interrupt immer auch zumindest das Codesegment neu setzt, müssen wir die Segmente selbst so definieren, wie wir sie brauchen. Die Tabelle, die die Segmentdefinitionen enthält, ist die Global Descriptor Table (GDT).

Es gibt in diesem Wiki schon einen sehr ausführlichen Artikel zum Thema, daher möchte ich an dieser Stelle einfach nur darauf verweisen anstatt ihn zu kopieren:

- [Global Descriptor Table](Global-Descriptor-Table.md "Global Descriptor Table")

Ich gehe im Folgenden davon aus, dass die im Artikel beschriebenen Code- und Datensegmente in der Reihenfolge angelegt worden sind, in der sie im Artikel vorgeschlagen sind. Die TSS-Einträge brauchen wir vorerst noch nicht. Wir haben also in etwa den folgenden Code:

``` c
#define GDT_FLAG_DATASEG 0x02
#define GDT_FLAG_CODESEG 0x0a
#define GDT_FLAG_TSS     0x09

#define GDT_FLAG_SEGMENT 0x10
#define GDT_FLAG_RING0   0x00
#define GDT_FLAG_RING3   0x60
#define GDT_FLAG_PRESENT 0x80

#define GDT_FLAG_4K_GRAN 0x800
#define GDT_FLAG_32_BIT  0x400

void init_gdt(void)
{
    set_entry(0, 0, 0, 0);
    set_entry(1, 0, 0xfffff, GDT_FLAG_SEGMENT | GDT_FLAG_32_BIT |
        GDT_FLAG_CODESEG | GDT_FLAG_4K_GRAN | GDT_FLAG_PRESENT);
    set_entry(2, 0, 0xfffff, GDT_FLAG_SEGMENT | GDT_FLAG_32_BIT |
        GDT_FLAG_DATASEG | GDT_FLAG_4K_GRAN | GDT_FLAG_PRESENT);
    set_entry(3, 0, 0xfffff, GDT_FLAG_SEGMENT | GDT_FLAG_32_BIT |
        GDT_FLAG_CODESEG | GDT_FLAG_4K_GRAN | GDT_FLAG_PRESENT | GDT_FLAG_RING3);
    set_entry(4, 0, 0xfffff, GDT_FLAG_SEGMENT | GDT_FLAG_32_BIT |
        GDT_FLAG_DATASEG | GDT_FLAG_4K_GRAN | GDT_FLAG_PRESENT | GDT_FLAG_RING3);

    load_gdt();
}
```

Testen lässt sich die GDT ganz einfach: Wenn der Kernel nach dem Laden der GDT und dem Neuladen der Segmentregister noch läuft, war es wohl hinreichend richtig. Wenn der Rechner neu startet, stimmt noch irgendetwas nicht ganz.

## Interrupt Descriptor Table

Eine zweite Tabelle, die [Interrupt Descriptor Table](Interrupt-Descriptor-Table.md "Interrupt Descriptor Table") (IDT), beschreibt, wie mit den unterschiedlichen Interrupts umzugehen ist. Schau Dir am besten auch hier den Artikel an, um herauszufinden, wie die Einträge der Tabelle aussehen.

Für einen ersten Test nimmst Du am besten einen einfachen Handler her, ohne aus dem Interrupt zurückzuspringen:

``` c
void int_handler(void)
{
    kprintf("Ein Interrupt!\n");
    while(1);
}
```

Nachdem Du die GDT und IDT eingerichtet hast (und den Handler für Interrupt 0, also in den ersten Eintrag der IDT eingetragen hast), kannst Du versuchen, diesen Interrupt auszulösen:

``` c
asm volatile("int $0x0");
```

Wenn alles funktioniert, bekommst Du jetzt unsere Erfolgsmeldung aus dem Interrupt.

## Programmable Interrupt Controller

Dummerweise liegen auf den ersten paar Interruptnummern sowohl einige Exceptions als auch einige Hardware-Interrupts. Wir müssen diese beiden Fälle natürlich unterscheiden können, um sinnvoll mit ihnen umzugehen. Exceptions lassen sich nicht auf andere Nummern legen, aber bei Hardware-Interrupts ist es glücklicherweise möglich: Wir müssen dazu nur den [Programmable Interrupt Controller](Programmable-Interrupt-Controller.md "Programmable Interrupt Controller") (PIC) umprogrammieren.

Ein übliches Modell ist es, auf den Interrupts 0 bis 0x1f die Exceptions zu haben, direkt anschließend von 0x20 bis 0x2f die IRQs und ab 0x30 die Software-Interrupts, z.B. Syscalls. In diesem Fall müssten wir den beiden PICs also mitteilen, sie sollen die IRQs ab 0x20 bzw. 0x28 anfangen lassen:

``` c
// Master-PIC initialisieren
outb(0x20, 0x11); // Initialisierungsbefehl fuer den PIC
outb(0x21, 0x20); // Interruptnummer fuer IRQ 0
outb(0x21, 0x04); // An IRQ 2 haengt der Slave
outb(0x21, 0x01); // ICW 4

// Slave-PIC initialisieren
outb(0xa0, 0x11); // Initialisierungsbefehl fuer den PIC
outb(0xa1, 0x28); // Interruptnummer fuer IRQ 8
outb(0xa1, 0x02); // An IRQ 2 haengt der Slave
outb(0xa1, 0x01); // ICW 4

// Alle IRQs aktivieren (demaskieren)
outb(0x21, 0x0);
outb(0xa1, 0x0);
```

Dabei ist *outb* eine Funktion, um einen 8-Bit-Wert an einen [I/O-Port](I-O-Ports.md "I/O Ports") zu schreiben, und kann wie in [Inline-Assembler mit GCC](Inline-Assembler-mit-GCC.md "Inline-Assembler mit GCC") beschrieben definiert werden:

``` c
static inline void outb(uint16_t port, uint8_t data)
{
    asm volatile ("outb %0, %1" : : "a" (data), "Nd" (port));
}
```

Nachdem die IRQs auf sinnvolle Nummern gelegt sind und Handler in der IDT installiert sind, kannst Du Hardware-Interrupts aktivieren:

``` c
asm volatile("sti");
```

**Achtung**: Der Kernel kann von der *sti*-Instruktion an an jeder beliebigen Stelle unterbrochen werden, auch wenn die Initialisierung an dieser Stelle noch nicht vollständig abgeschlossen ist. Es ist daher in der Regel eine gute Idee, Interrupts erst als allerletztes in der Kernelinitialisierung zu aktivieren.

Beispielsweise liegt der Timer auf IRQ 0 und löst in regelmäßigen Abständen mehrmals pro Sekunde einen IRQ aus. Zumindest IRQ 0 muss also auf jeden Fall sinnvoll behandelt werden, ansonsten währt die Freude nicht lang. Je nachdem, welche Hardware vorhanden ist und was der Benutzer mit ihr macht, können aber natürlich auch andere IRQs, wie etwa Tastatur und Maus, jederzeit auftreten.

## Nützliche Interrupthandler

Jetzt fehlt nur noch die eigentliche Funktion, die aufgerufen werden soll, wenn ein Interrupt auftritt. Meistens möchte man nur einen einzigen Handler für alle Interrupts zusammen haben, der allerdings die Interruptnummer (und den sonstigen Prozessorzustand beim Auftreten des Interrupts) als Parameter übergeben bekommt.

Ein vorgeschalteter Teil soll den Prozessorzustand sichern und der eigentliche Handler soll nur noch ungefähr so aussehen:

``` c
void handle_interrupt(struct cpu_state* cpu)
{
    if (cpu->intr <= 0x1f) {
        kprintf("Exception %d, Kernel angehalten!\n", cpu->intr);

        // Hier den CPU-Zustand ausgeben

        while(1) {
            // Prozessor anhalten
            asm volatile("cli; hlt");
        }
    } else {
        // Hier den Hardwareinterrupt behandeln
    }
}
```

Das lässt sich einfach genug erreichen, dazu nehmen wir zur Abwechslung wieder einmal Assembler zur Hilfe. Wir müssen dazu für jeden Interrupt einen eigenen Handler definieren, der aber nichts anderes macht, als die Interruptnummer auf den Stack zu legen und in einen gemeinsamen Handler für alle Interrupts zu springen. Außerdem müssen wir aufpassen, weil manche Exceptions einen Fehlercode auf den Stack legen, bei allen anderen Interrupts fehlt er. Um alle Interrupts gleich aussehen zu lassen, legen wir vor der Interruptnummer noch eine 0 auf den Stack, wenn kein Fehlercode vorhanden ist. Wir definieren also:

``` asm
.macro intr_stub nr
.global intr_stub_\nr
intr_stub_\nr:
    pushl $0
    pushl $\nr
    jmp intr_common_handler
.endm

.macro intr_stub_error_code nr
.global intr_stub_\nr
intr_stub_\nr:
    pushl $\nr
    jmp intr_common_handler
.endm

// Exceptions
intr_stub 0
intr_stub 1
intr_stub 2
intr_stub 3
intr_stub 4
intr_stub 5
intr_stub 6
intr_stub 7
intr_stub_error_code 8
intr_stub 9
intr_stub_error_code 10
intr_stub_error_code 11
intr_stub_error_code 12
intr_stub_error_code 13
intr_stub_error_code 14
intr_stub 15
intr_stub 16
intr_stub_error_code 17
intr_stub 18

// IRQs
intr_stub 32
// usw. bis 47

// Syscall
intr_stub 48
```

Im zweiten Teil müssen wir jetzt den *intr_common_handler* definieren. Er soll den CPU-Zustand auf den Stack speichern und dann die oben genannte Funktion *handle_interrupt* aufrufen. Nachdem der Interrupt fertig behandelt ist, stellen wir den CPU-Zustand wieder her und springen zurück in das unterbrochene Programm. Das könnte ungefähr so aussehen:

``` asm
.extern handle_interrupt
intr_common_handler:
    // CPU-Zustand sichern
    push %ebp
    push %edi
    push %esi
    push %edx
    push %ecx
    push %ebx
    push %eax

    // Handler aufrufen
    push %esp
    call handle_interrupt
    add $4, %esp

    // CPU-Zustand wiederherstellen
    pop %eax
    pop %ebx
    pop %ecx
    pop %edx
    pop %esi
    pop %edi
    pop %ebp

    // Fehlercode und Interruptnummer vom Stack nehmen
    add $8, %esp

    // Ruecksprung zum unterbrochenen Code
    iret
```

Die passende Definition für struct cpu_state sähe in diesem Fall so aus, dass sie einfach die auf den Stack gepushten Werte enthält. Zur Erinnerung, der Stack wächst nach unten, daher fängt die Struktur mit dem zuletzt gepushten (also eax) an:

``` c
struct cpu_state {
    // Von Hand gesicherte Register
    uint32_t   eax;
    uint32_t   ebx;
    uint32_t   ecx;
    uint32_t   edx;
    uint32_t   esi;
    uint32_t   edi;
    uint32_t   ebp;

    uint32_t   intr;
    uint32_t   error;

    // Von der CPU gesichert
    uint32_t   eip;
    uint32_t   cs;
    uint32_t   eflags;
    uint32_t   esp;
    uint32_t   ss;
};
```

Nachdem die Handler für die einzelnen Interrupts nun fertig geschrieben sind, müssen sie (falls noch nicht geschehen) natürlich noch in die IDT eingetragen werden, damit sie beim Auftreten eines Interrupts angesprungen werden. Andernfalls würde der Code nie ausgeführt werden.

Eine geeignete Implementierung für Exceptions ist die oben schon vorgeschlagene Fehlermeldung mit anschließendem Anhalten des Systems (später könnte man das aktuell ausgeführte Programm beenden, aber wir haben so etwas ja noch nicht). Für Hardware-Interrupts muss zumindest ein EOI (End of Interrupt) an den PIC gesendet werden, damit der Interrupt gleich beim nächsten Mal wieder gemeldet wird und nicht noch vom letzten Aufruf blockiert ist:

``` c
if (cpu->intr >= 0x20 && cpu->intr <= 0x2f) {
    if (cpu->intr >= 0x28) {
        outb(0xa0, 0x20);
    }
    outb(0x20, 0x20);
}
```

Mit diesen Interrupthandlern ließe sich an dieser Stelle beispielsweise schon ein [Tastaturtreiber](Keyboard-Controller.md "Keyboard Controller") schreiben.

## Weitere Quellen

- [Offizielle Handbücher zu den Prozessoren](Linkliste.md#offizielle-spezifikationen "Linkliste"):
  - Intel Architecture Software Developer's Manuals, Band 3A
    - Kapitel 3: Protected Mode Memory Management
    - Kapitel 6: Interrupt and Exception Handling
  - AMD64 Architecture Programmer's Manual, Band 2
    - Kapitel 4: Segmented Virtual Memory
    - Kapitel 8: Exceptions and Interrupts
- [Protected-Mode-Tutorial der FH Zwickau](http://www.fh-zwickau.de/doc/prmo/pmtutor/text/index.htm), Kapitel 2

  

|  |  |  |
| -------------------------------------------------------------------------------------------------------------- | ---------------- | ----------------------------------------------------------------------------------------------------------------- |
| « [Teil 4 - Hello World](Teil-4-Hello-World.md "Teil 4 - Hello World") | **Navigation** | [Teil 6 - Multitasking](Teil-6-Multitasking.md "Teil 6 - Multitasking") » |

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/11391/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1898/index.html)

<!-- MediaWiki page 1898; revision 11391; parent 11377; 2018-09-04T10:10:29Z -->
