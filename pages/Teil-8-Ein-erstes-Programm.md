# Teil 8 - Ein erstes Programm

|  |  |  |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- | ----------------------------------------------------------------------------------------------- |
| « [Teil 7 - Physische Speicherverwaltung](Teil-7-Physische-Speicherverwaltung.md "Teil 7 - Physische Speicherverwaltung") | **Navigation** | [Teil 9 - Paging](Teil-9-Paging.md "Teil 9 - Paging") » |

## Ziel

Eigentlich wäre der Kernel inzwischen so weit, dass man kleine Programme dafür schreiben könnte, die aus einer externen Datei geladen werden. Versuchen wir es!

## Ein kleines Testprogramm

Der einfachste Test ist wie immer, ein paar Zeichen auf den Bildschirm auszugeben - das ist es also, was wir als erstes erreichen wollen. In unseren bisherigen Tasks haben wir dazu direkt kprintf() aufgerufen. Wenn wir ein externes Programm ausführen, geht das nicht mehr so einfach - das Programm müsste dazu ja wissen, an welcher Adresse diese Funktion liegt. Innerhalb des Kernels hat der Linker die Adresse für uns aufgelöst, aber im externen Programm gibt es kein kprintf, das der Linker auflösen könnte.

Wir gehen daher erst einmal wieder einen Schritt zurück und schreiben direkt in den Videospeicher. Wir werden das weiter unten dann ordentlich machen. Wir erstellen also zunächst einmal eine Datei *test.c* in einem anderen Verzeichnis (die Makefile des Kernels sammelt alle .c-Dateien im Kernelverzeichnis und seinen Unterverzeichnissen auf, und das wollen wir ja gerade nicht):

``` c
#include <stdint.h>

uint16_t* videomem = (uint16_t*) 0xb8000;

void _start(void)
{
    int i;
    for (i = 0; i < 3; i++) {
        *videomem++ = (0x07 << 8) | ('0' + i);
    }

    while(1);
}
```

Das Programm sollte also den String "012" ausgeben. Ans Ende setzen wir eine Endlosschleife, damit der Prozessor beim Ausführen nicht über das Ende des Programms hinausläuft und irgendwelches Zeug ausführt, das dort zufällig steht.

Wir brauchen auch wieder ein Linkerskript, das für das Programm ähnlich aussieht wie für den Kernel (nur ein bisschen einfacher). Wir legen willkürlich fest, dass wir das Programm an den Speicher ab 2 MB legen wollen - mehr als 1 MB sollte der Kernel im Moment nicht verbrauchen. Außerdem bauen wir eine flache Binary statt einer ELF-Datei, damit das Laden einfacher wird. Auch das ist natürlich keine Dauerlösung.

    /*  Bei _start soll die Ausfuehrung losgehen */
    ENTRY(_start)

    OUTPUT_FORMAT(binary)

    /*
     * Hier wird festgelegt, in welcher Reihenfolge welche Sektionen in die Binary
     * geschrieben werden sollen
     */
    SECTIONS
    {
        /* Das Programm wird an 2 MB geladen */
        . = 0x200000;

        .text : {
            *(.text)
        }
        .data ALIGN(4096) : {
            *(.data)
        }
        .rodata ALIGN(4096) : {
            *(.rodata)
        }
        .bss ALIGN(4096) : {
            *(.bss)
        }
    }

Und schließlich wieder eine Makefile, um das Programm zusammenzubauen (auch hier müssen für Crosscompiler die Werte wieder entsprechend angepasst werden):

    SRCS = $(shell find -name '*.c')
    OBJS = $(addsuffix .o,$(basename $(SRCS)))

    CC = gcc
    LD = ld

    ASFLAGS = -m32
    CFLAGS = -m32 -Wall -g -fno-stack-protector -nostdinc -I include
    LDFLAGS = -melf_i386 -Ttest.ld

    test.bin: $(OBJS)
        $(LD) $(LDFLAGS) -o $@ $^

    %.o: %.c
        $(CC) $(CFLAGS) -c -o $@ $^

    clean:
        rm $(OBJS)

    .PHONY: clean

Ein einfaches *make* erstellt uns jetzt unser Testprogramm als flache Binary in *test.bin*.

## Multiboot-Module

Als nächstes müssen wir das Programm irgendwie in den Speicher bekommen, um es im Kernel starten zu können. Wir haben noch keine Treiber für Festplatten oder irgendwelche anderen Speichermedien, aber wir haben eine Möglichkeit, Dateien zu laden, die wir auch schon für den Kernel benutzen: Der Bootloader kann das für uns machen. [Multiboot](Multiboot.md "Multiboot") erlaubt es, sogenannte *Module* laden zu lassen, die dem Kernel dann in der [Multibootstruktur](Multiboot.md#multiboot-structure "Multiboot") aufgelistet sind (relevant sind die Felder [mbs_mods_count](Multiboot.md#mbs_mods_count "Multiboot") und [mbs_mods_addr](Multiboot.md#mbs_mods_addr "Multiboot")).

Mit dieser Information können wir jetzt *init_multitasking* umschreiben: Falls ein Multibootmodul übergeben worden ist, starten wir nicht die vier Testtasks, sondern dieses eine Modul. Der Bootloader legt uns dieses Modul allerdings einfach irgendwo hin, während das Programm davon ausgeht, an 2 MB geladen zu werden. Wir müssen es also erst einmal dorthin kopieren.

``` c
void init_multitasking(struct multiboot_info* mb_info)
{
    if (mb_info->mbs_mods_count == 0) {
        /*
         * Ohne Module machen wir dasselbe wie bisher auch. Eine genauso gute
         * Alternative waere es, einfach mit einer Fehlermeldung abzubrechen.
         */
        init_task(task_a);
        init_task(task_b);
        init_task(task_c);
        init_task(task_d);
    } else {
        /*
         * Wenn wir mindestens ein Multiboot-Modul haben, kopieren wir das
         * erste davon nach 2 MB und erstellen dann einen neuen Task dafuer.
         */
        struct multiboot_module* modules = mb_info->mbs_mods_addr;
        size_t length = modules[0].mod_end - modules[0].mod_start;
        void* load_addr = (void*) 0x200000;

        memcpy(load_addr, (void*) modules[0].mod_start, length);
        init_task(load_addr);
    }
}
```

Wichtig ist jetzt, dass die Speicherverwaltung die entsprechenden Speicherbereiche nicht schon für eine andere Verwendung hergegeben hat. Spätestens an dieser Stelle müssen wir *pmm_init* also entsprechend erweitern:

``` c
    ...

    /*
     * Die Multibootstruktur ist auch besetzt, genauso wie die Liste von
     * Multibootmodulen. Wir gehen bei beiden davon aus, dass sie maximal 4k
     * gross werden.
     */
    struct multiboot_module* modules = mb_info->mbs_mods_addr;

    pmm_mark_used(mb_info);
    pmm_mark_used(modules);

    /* Und die Multibootmodule selber sind auch belegt */
    int i;
    for (i = 0; i < mb_info->mbs_mods_count; i++) {
        addr = modules[i].mod_start;
        while (addr < modules[i].mod_end) {
            pmm_mark_used((void*) addr);
            addr += 0x1000;
        }
    }
}
```

Das war's im Prinzip schon, jetzt müssen wir das Modul nur noch testen:

- Wer den Kernel direkt von qemu laden lässt, gibt das Modul per -initrd an: *qemu -kernel kernel -initrd test.bin*. Mehrere Module werden per Komma getrennt angegeben.
- Wer ein Diskettenimage (oder eine echte Diskette) benutzt, kopiert test.bin auf das Image und benutzt in GRUB vor dem Booten noch den Befehl *module /test.bin*.

## Syscalls

Direkt auf den Videospeicher zuzugreifen ist natürlich kein netter Zug von einem Programm (und abgesehen davon wird ein etwas weiter entwickelter Kernel das auch gar nicht mehr zulassen). Sobald mehr als eines läuft, würden sie sich ihre Ausgaben gegenseitig überschreiben. Der Kernel auf der anderen Seite hat eine aktuelle Cursorposition, die für alle gilt. Eigentlich wäre das also eine Aufgabe für den Kernel.

Als Syscall benutzen wir den Interrupt 0x30 (das ist nach Exceptions und IRQs der erste freie). Falls noch nicht geschehen, muss dieser Interrupt in die IDT eingetragen und ein passender Interrupt-Stub angelegt werden. In *handle_interrupt* lassen wir für Interrupt 0x30 eine neue Funktion syscall aufrufen:

``` c
struct cpu_state* syscall(struct cpu_state* cpu)
{
    switch (cpu->eax) {
        case 0: /* putc */
            kprintf("%c", cpu->ebx);
            break;
    }

    return cpu;
}
```

In eax sollen Aufrufer die Funktionsnummer übergeben (und als Funktion 0 definieren wir eine Funktion, die ein einzelnes Zeichen ausgibt) und die Parameter werden in den übrigen Registern übergeben. Stattdessen könnte man natürlich auch andere Aufrufkonventionen benutzen und Parameter z.B. über den Stack übergeben. Außerdem geben wir hier gleich von Anfang an einen neuen CPU-Zustand zurück, um Syscalls zu erlauben, die aktiv den aktuellen Task wechseln.

Das Programm muss natürlich auch noch entsprechend angepasst werden, den Syscall zu verwenden - der Aufruf sieht ungefähr aus wie in [Teil 3](Teil-3-Trocken%C3%BCbungen.md "Teil 3 - Trockenübungen") für Linux. Um sicherzugehen, dass wir die neue Version sehen, ändern wir auch gleich noch die Anzahl der ausgegebenen Ziffern:

``` c
for (i = 0; i < 5; i++) {
    asm("int $0x30" : : "a" (0), "b" ('0' + i));
}
```

## ELF

Im Moment benutzen wir flache Binaries für das Testprogramm. Für einen ersten Test waren sie ganz geschickt, aber sie haben auch einige Nachteile: Sie enthalten beispielsweise keine Debuginformationen. objdump wird daher nicht mehr als den reinen Assemblercode anzeigen können. gdb kann nicht benutzt werden. Die Dateien werden unter Umständen auch größer als nötig, weil auch uninitialisierte Bereiche in der Datei enthalten sein müssen, und das Dateiformat ist nicht flexibel genug, um dynamisch gelinkte Bibliotheken zu ermöglichen. Aber für die OS-Entwicklung ist der Punkt mit dem Debugging eigentlich schon tödlich genug.

Es muss also ein "richtiges" Binärformat her. Wir benutzen für den Kernel bereits [ELF](Executable-and-Linking-Format.md "Executable and Linking Format") und haben alle nötigen Tools dazu bereit, insofern bietet es sich an, ELF zu benutzen. Es steht natürlich jedem frei, ein anderes Format zu benutzen, z.B. das unter Windows benutzte [PE](Microsoft-Portable-Executable-and-Common-Object-File-Format.md "Microsoft Portable Executable and Common Object File Format") oder etwas ganz eigenes. Hier führe ich das Vorgehen beispielhaft für ELF aus.

Ändern wir also zunähst das Ausgabeformat also in der *test.ld* ab:

    OUTPUT_FORMAT(elf32-i386)

Anschließend kompilieren wir neu und zeigen uns dann mit *readelf -l test.bin* erst einmal an, wie die entstandene ELF-Datei aussieht:

    Elf file type is EXEC (Executable file)
    Entry point 0x200000
    There are 3 program headers, starting at offset 52

    Program Headers:
    Type           Offset   VirtAddr   PhysAddr   FileSiz MemSiz  Flg Align
    LOAD           0x001000 0x00200000 0x00200000 0x00029 0x00029 R E 0x1000
    LOAD           0x002000 0x00201000 0x00201000 0x00004 0x00004 RW  0x1000
    GNU_STACK      0x000000 0x00000000 0x00000000 0x00000 0x00000 RW  0x4

Dazu lässt sich folgendes sagen:

- Eine ELF-Datei hat mehrere Program Header. Alle Header vom Typ LOAD (entspricht dem Wert 1) müssen geladen werden.
- Die Spalte Offset gibt an, an welcher Stelle in der Datei der jeweilige Abschnitt anfängt.
- FileSiz gibt an, wie groß der Abschnitt in der Datei ist, MemSiz wie groß er im Speicher ist. Wenn MemSiz größer als FileSiz ist, muss hinten mit Nullen aufgefüllt werden.
- VirtAddr gibt an, an welcher Adresse der Abschnitt geladen werden muss, damit das Programm funktioniert.
- Und den Entry Point haben wir auch wieder, an 2 MB.

Zunächst brauchen wir eine Headerdatei *elf.h*, die uns die nötigen Datenstrukturen - den ELF-Header und die Program Header - zur Verfügung stellt:

``` c
#ifndef ELF_H
#define ELF_H

#include <stdint.h>

#define ELF_MAGIC 0x464C457F

struct elf_header {
    uint32_t    magic;
    uint32_t    version;
    uint64_t    reserved;
    uint64_t    version2;
    uint32_t    entry;
    uint32_t    ph_offset;
    uint32_t    sh_offset;
    uint32_t    flags;
    uint16_t    header_size;
    uint16_t    ph_entry_size;
    uint16_t    ph_entry_count;
    uint16_t    sh_entry_size;
    uint16_t    sh_entry_count;
    uint16_t    sh_str_table_index;
} __attribute__((packed));

struct elf_program_header {
    uint32_t    type;
    uint32_t    offset;
    uint32_t    virt_addr;
    uint32_t    phys_addr;
    uint32_t    file_size;
    uint32_t    mem_size;
    uint32_t    flags;
    uint32_t    alignment;
} __attribute__((packed));

#endif
```

Damit lässt sich dann ein kleiner ELF-Loader bauen - er bringt die Datei irgendwie in den Speicher und startet einen neuen Task:

``` c
void init_elf(void* image)
{
    /*
     * FIXME Wir muessen eigentlich die Laenge vom Image pruefen, damit wir bei
     * korrupten ELF-Dateien nicht ueber das Dateiende hinauslesen.
     */

    struct elf_header* header = image;
    struct elf_program_header* ph;
    int i;

    /* Ist es ueberhaupt eine ELF-Datei? */
    if (header->magic != ELF_MAGIC) {
        kprintf("Keine gueltige ELF-Magic!\n");
        return;
    }

    /*
     * Alle Program Header durchgehen und den Speicher an die passende Stelle
     * kopieren.
     *
     * FIXME Wir erlauben der ELF-Datei hier, jeden beliebigen Speicher zu
     * ueberschreiben, einschliesslich dem Kernel selbst.
     */
    ph = (struct elf_program_header*) (((char*) image) + header->ph_offset);
    for (i = 0; i < header->ph_entry_count; i++, ph++) {
        void* dest = (void*) ph->virt_addr;
        void* src = ((char*) image) + ph->offset;

        /* Nur Program Header vom Typ LOAD laden */
        if (ph->type != 1) {
            continue;
        }

        memset(dest, 0, ph->mem_size);
        memcpy(dest, src, ph->file_size);
    }

    init_task((void*) header->entry);
}
```

Aus der Blickwinkel der Sicherheit ist er eine ziemliche Katastrophe (wie die FIXME-Kommentare zeigen), aber viel schlechter als der bisherige Loader für flache Binaries ist er auch nicht. Die Länge des Images zu prüfen ist einfach genug, dass ich es nicht weiter beschreiben muss, und wohin die Dateien geladen werden, ändert sich ohnehin wieder, sobald Paging ins Spiel kommt.

In *init_multitasking* müssen wir die neue Funktion natürlich auch noch aufrufen:

``` c
    ...
    } else {
        /*
         * Wenn wir mindestens ein Multiboot-Modul haben, kopieren wir das
         * erste davon nach 2 MB und erstellen dann einen neuen Task dafuer.
         */
        struct multiboot_module* modules = mb_info->mbs_mods_addr;
        init_elf((void*) modules[0].mod_start);
    }
    ...
```

Damit haben wir einen Kernel, der eine ELF-Datei ausführen kann.

|  |  |  |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- | ----------------------------------------------------------------------------------------------- |
| « [Teil 7 - Physische Speicherverwaltung](Teil-7-Physische-Speicherverwaltung.md "Teil 7 - Physische Speicherverwaltung") | **Navigation** | [Teil 9 - Paging](Teil-9-Paging.md "Teil 9 - Paging") » |

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/11394/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2241/index.html)

<!-- MediaWiki page 2241; revision 11394; parent 8242; 2018-09-04T10:19:30Z -->
