# ARM-OS-Dev Teil 4 – Hello World

|  |  |  |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| « [ARM-OS-Dev Teil 3 – Trockenübungen](https://github.com/lowlevel-eu/wiki/wiki/ARM-OS-Dev-Teil-3-%E2%80%93-Trocken%C3%BCbungen "ARM-OS-Dev Teil 3 – Trockenübungen") | **Navigation** | [ARM-OS-Dev Teil 5 – Interrupts](https://github.com/lowlevel-eu/wiki/wiki/ARM-OS-Dev-Teil-5-%E2%80%93-Interrupts "ARM-OS-Dev Teil 5 – Interrupts") » |

## Der Bootprozess

Im Gegensatz zu x86 gibt es auf dem Integrator/CP-Board kein BIOS und keinen Bootloader. An den Anfang des RAMs wird ein Teil des Flashspeichers gemappt (die letzten 256 kB), auf dem sich der Kernel befindet. Die CPU beginnt ihre Ausführung am Beginn des RAMs, bei 0x00000000. Da dort der gemappte Flashspeicher liegt, wird sofort unser Code ausgeführt.

Wer kein I/CP-Board hat, dem bleibt QEMU zur Emulation. QEMU emuliert keinen Flashspeicher, es bietet nur die Möglichkeit, eine ELF-Datei als Kernel zu laden. Wir werden eine ELF-Datei so erstellen lassen, dass sie an den Anfang des Speichers geladen wird, so, als befände sie sich in den letzten 256 kB des Flashspeichers (nachdem man die ELF in eine rohe Binärdatei umgewandelt hätte).

## Der Hello-World-Kernel

Wie im Einführungsartikel beschrieben gibt es auf I/CP keinen schönen Textmodus, sodass man nicht einfach Zeichen irgendwo in den Arbeitsspeicher packen kann, sodass diese auf einem Bildschirm erscheinen. Wir werden uns hier damit begnügen, sie über eine serielle Schnittstelle ([UART](https://github.com/lowlevel-eu/wiki/wiki/Serielle-Schnittstelle "Serielle Schnittstelle")) auszugeben. Diese bietet für uns zwei interessante im Speicher liegende Register: Schreibt man ein Byte nach 0x16000000 (hier SERIAL_DR (Data Register) genannt), dann wird es über die Schnittstelle ausgegeben. Dies kann jedoch nur getan werden, wenn der Sendepuffer aktuell frei ist. Um dies zu überprüfen, bedienen wir uns des Registers an der Speicheradresse 0x16000018 (hier SERIAL_FR (Flag Register) genannt). Ist darin das Bit 5 gesetzt, dann ist der Sendepuffer noch gefüllt und wir müssen zunächst warten, bis er leer ist: \<c\>typedef unsigned char uint8_t; typedef unsigned int uint32_t;

1.  define SERIAL_DR \*((volatile uint8_t \*)0x16000000)
2.  define SERIAL_FR \*((volatile uint32_t \*)0x16000018)
3.  define SERIAL_BUFFER_FULL (1 \<\< 5)

void init(void) {

       const char *hw = "Hello World!\n";

       while (*hw != '\0') {
           // Warten, bis Daten gesendet werden können
           while (SERIAL_FR & SERIAL_BUFFER_FULL);

           // Nächstes Zeichen senden
           SERIAL_DR = *(hw++);
       }

}\</c\> Diese Datei kann man zum Beispiel unter dem Namen init.c abspeichern.

Nun müssen wir noch die init-Funktion aufrufen. Dies geschieht mit einem kleinen Assemblerstub, der einen Stack aufsetzt und eben in die Funktion springt (start.S):

    .arm

    /* Init ist eine Funktion aus init.c */
    .extern init

    /* Hier befinden sich die Einsprungspunkte für Exceptions, der erste wird beim
       Reset aufgerufen. Da die Einsprungspunkte nur vier Byte voneinander entfernt
       sind, bleibt jeweils nur Platz für einen Opcode – und damit springen wir
       woanders hin. */
    b       _start
    /* Hier folgen jetzt die Einsprungspunkte für Undefined Instruction, SWI,
       Prefetch Abort, Data Abort, eine bisher reservierte Exception, IRQ und FIQ.
       Da all diese Exceptions noch nicht behandelt werden können, legen wir dort
       einfach Endlosschleifen hin. */
    b       .
    b       .
    b       .
    b       .
    b       .
    b       .
    b       .

    _start:
    /* Stack initialisieren – da man bei ARM keine 32-Bit-Werte laden kann, müssen
       wir die Adresse über einen Umweg laden */
    ldr     r13, [r15, #kernel_stack_addr - 8 - .]

    /* C-Code aufrufen */
    bl      init

    /* Falls wir jemals aus init zurueckkommen sollten, gehen wir in eine
       Endlosschleife */
    b       .

    /* Enthält die Adresse des Kernelstacks */
    kernel_stack_addr:
    .4byte  kernel_stack

    /* 8 kB Stack für den Kernel. Das Label steht hinter dem freien Speicher,
       weil der Stack nach unten wächst */
    .section .bss
    .space 8192
    kernel_stack:

Dieser Code wird später an die Adresse 0x00000000 geladen. Der erste Befehl wird also beim Start des Systems aufgerufen, er springt zur weiteren Initialisierung, die dann einen Stack aufsetzt und init aufruft. Sollte, wieso auch immer, irgendeine andere Exception auftreten (FIQs und IRQs sind beim Start zunächst deaktiviert, also besteht eigentlich keine Gefahr), dann resultiert diese einfach in einer Endlosschleife. Ausgeführt wird der Code übrigens im Supervisor-Modus, dies ist der Modus, den die CPU bei einem Reset einnimmt.

Nun schreiben wir noch eine hübsche Makefile, ähnlich der aus der x86-Reihe (unter der Annahme, dass die Cross-Buildchain aus dem ARM-Crosscompiler-Artikel verwendet wird):

    SRCS = $(shell find -name '*.[cS]')
    OBJS = $(addsuffix .o,$(basename $(SRCS)))

    CC = /usr/cross/arm/bin/arm-unknown-linux-gnu-gcc
    LD = /usr/cross/arm/bin/arm-unknown-linux-gnu-ld

    ASFLAGS = -march=armv5t
    CFLAGS = -march=armv5t -O3 -ffreestanding -nostartfiles -nostdinc -nodefaultlibs -Wall -Wextra -fno-stack-protector
    LDFLAGS = -e 0x00000000 -T link.ld

    kernel: $(OBJS)
        $(LD) $(LDFLAGS) -o $@ $^

    %.o: %.c
        $(CC) $(CFLAGS) -c -o $@ $^

    %.o: %.S
        $(CC) $(ASFLAGS) -c -o $@ $^

    clean:
        rm $(OBJS)

    .PHONY: clean

Als Architektur wird ARMv5 angenommen (ARM9-Prozessoren fallen darunter, wie sie QEMU normalerweise emuliert). Bei Bedarf müssen die Werte für CC und LD angepasst werden.

Damit LD auch alles so linkt, wie er soll, brauchen wir noch ein Linkerscript (link.ld):

    /* Wir nehmen einen ARMv5-Prozessor an (QEMU-Standard) */
    OUTPUT_ARCH("armv5t")
    /* Diese Datei muss im Speicher nach 0x00000000 geladen werden */
    STARTUP(start.o)

    /*
     * Hier wird festgelegt, in welcher Reihenfolge welche Sektionen in die Binary
     * geschrieben werden sollen
     */
    SECTIONS
    {
        /* Die Standardsektionen einfach hintereinander weg ab 0x00000000 einbinden. */
        .text 0x00000000 : AT(0x00000000) {
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

Nach einem *make*-Aufruf sollte eine ELF namens „kernel“ erstellt worden sein. Diese kann man nun mit „qemu-system-arm -kernel kernel -serial stdio“ laden und ausführen, das Ergebnis sollte ein „Hello World!“ auf der Standardausgabe von QEMU sein.

## Weitere Quellen

Das Interface der seriellen Ausgabe ist in [einem I/CP-Manual](http://infocenter.arm.com/help/topic/com.arm.doc.dui0159b/DUI0159B_integratorcp_1_0_ug.pdf) ab Seite 103 beschrieben.

Wie auch vom Kernel der x86-Reihe gibt es ein [git-Repository von diesem Kernel](https://gitorious.org/arm-os-dev/kernel), in dem der Code dieser und der folgenden Teile zu finden ist. Den Code für diesen Teil findet man [hier](https://gitorious.org/arm-os-dev/kernel/trees/e692519a643cca9a65e7c424d364a1be095b5c36), [hier](https://gitorious.org/arm-os-dev/kernel/trees/9dbeaa7b606627787e3681bb5415acd1f074ec28) ist dann noch ein kprintf hinzugefügt worden.

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/9775/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2421/index.html)

<!-- MediaWiki page 2421; revision 9775; parent 9774; 2011-05-12T21:18:17Z -->
