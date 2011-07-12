# Teil 4 - Hello World

|  |  |  |
| ---------------------------------------------------------------------------------------------------------------------------- | ---------------- | ----------------------------------------------------------------------------------------------------------- |
| « [Teil 3 - Trockenübungen](https://github.com/lowlevel-eu/wiki/wiki/Teil-3-Trocken%C3%BCbungen "Teil 3 - Trockenübungen") | **Navigation** | [Teil 5 - Interrupts](https://github.com/lowlevel-eu/wiki/wiki/Teil-5-Interrupts "Teil 5 - Interrupts") » |

## Der Bootprozess

Bevor wir anfangen, Code zu schreiben, zunächst ein kleiner Blick auf den Bootprozess. Aus Sicht des Kernels könnte dieser Abschnitt den Titel "was bisher geschah" tragen.

Bei einem CPU-Reset (der beispielsweise beim Anschalten passiert) wird der gesamte Prozessorzustand neu gesetzt. Insbesondere schaltet der Prozessor in den Real Mode und springt an die lineare Adresse 0xffff0 (z.B. cs:ip = f000:fff0). An dieser Adresse liegt das BIOS. Das BIOS initialisiert die Hardware, führt einen Selbsttest durch und wenn es fertig ist, löst es einen Interrupt 0x19 aus. Der Handler lädt den Bootsektor von der Festplatte oder Diskette nach linear 0x7c00 (z.B. 07c0:0000) und springt an diese Adresse.

Der Bootloader ist anschließend dafür zuständig, den Kernel des Betriebssystems in den Speicher zu laden, eine passende Umgebung aufzusetzen und an den Einsprungspunkt des Kernels zu springen. Zum Vorbereiten der Umgebung gehört der Wechsel in den passenden Prozessormodus (in unserem Fall der [32-Bit-Protected-Mode](https://github.com/lowlevel-eu/wiki/wiki/Protected-Mode "Protected Mode") des x86) und die Übergabe bestimmter Informationen an den Kernel (z.B. über den vorhandenen Speicher, eine Kernelkommandozeile, usw.)

Sobald der Bootloader an den Einsprungspunkt des Kernels gesprungen ist, gibt er die Kontrolle komplett an den Kernel ab. Er wird dann nicht mehr benötigt und sein Speicher kann anderweitig verwendet werden.

## Multiboot

Für unser Betriebssystem werden wir [GRUB](https://github.com/lowlevel-eu/wiki/wiki/Grand-Unified-Bootloader "GRUB") als Bootloader benutzen. GRUB ist einfach zu benutzen, weit verbreitet und hat einen großen Funktionsumfang.

Es gibt Leute, die der Meinung sind, man sollte seinen Bootloader selbst schreiben, damit man die Sache wirklich selbst gemacht hat. Diese Leute benutzen dann in ihrem Bootloader die Funktionen des BIOS, fangen also nur an einer anderen Stelle an, auf den Code anderer aufzusetzen. Dazu müssen sie auf Dauer viel Zeit in die Funktionalität des Bootloaders investieren, wenn sie nicht in ihrem Betriebssystem mit Einschränkungen leben wollen. Bootloader sind nette Projekte, aber wir konzentrieren uns hier auf das Betriebssystem.

[Multiboot](https://github.com/lowlevel-eu/wiki/wiki/Multiboot "Multiboot") ist der Name der Spezifikation, die ein Kernel einhalten muss, um von GRUB geladen werden zu können. Der verlinkte Artikel enthält dazu mehr Informationen.

## Der Hello-World-Kernel

"Hello World" ausgeben zu wollen stellt uns vor zwei Schwierigkeiten: Zum ersten müssen wir wissen, wie man Text auf den Bildschirm bekommt - und zum zweiten müssen wir dafür sorgen, dass der entsprechende Code überhaupt ausgeführt wird.

Fangen wir mit dem einfachen an: Direkt nach dem Booten ist ein PC im Textmodus. Im Textmodus werden auf dem Bildschirm die Zeichen dargestellt, die im Grafikspeicher ab der Adresse 0xb8000 liegen. Dabei braucht jedes Zeichen zwei Bytes: Das erste Byte ist das Zeichen selbst. Das zweite Byte ist das sogenannte Attributbyte, das die Farbe und Hintergrundfarbe des Texts festlegt - mehr Details stehen bei Bedarf im Artikel [Textausgabe](https://github.com/lowlevel-eu/wiki/wiki/Textausgabe "Textausgabe"). Wir legen also folgendermaßen los (die Datei heißt bei mir init.c):

\<c\>void init(void) {

       const char hw[] = "Hello World!";
       int i;
       char* video = (char*) 0xb8000;

       // C-Strings haben ein Nullbyte als Abschluss
       for (i = 0; hw[i] != '\0'; i++) {

           // Zeichen i in den Videospeicher kopieren
           video[i * 2] = hw[i];

           // 0x07 = Hellgrau auf Schwarz
           video[i * 2 + 1] = 0x07;
       }

}\</c\>

Nachdem wir das erste Problem souverän gelöst haben, müssen wir den Code jetzt nur noch zur Ausführung bringen. Wir müssen also irgendwie den Multiboot-Header in unsere Binary bekommen. Außerdem benutzt unsere Funktion ein paar lokale Variablen. Lokale Variablen landen auf dem [Stack](https://github.com/lowlevel-eu/wiki/wiki/Stack "Stack"), deswegen müssen wir etwas Speicherplatz für den Stack vorsehen. Diesen Teil erledigen wir in Assembler (diese Datei ist die start.S):

\<asm\>.section .text

// Init ist eine Funktion aus init.c .extern init

1.  define MB_MAGIC 0x1badb002
2.  define MB_FLAGS 0x0
3.  define MB_CHECKSUM -(MB_MAGIC + MB_FLAGS)

// Der Multiboot-Header .align 4 .int MB_MAGIC .int MB_FLAGS .int MB_CHECKSUM

// \_start muss global sein, damit der Linker es findet und als Einsprungspunkt // benutzen kann (alle Labels, die nicht global sind, sind nur in dieser Datei // sichtbar) .global \_start \_start:

       // Stack initialisieren
       mov $kernel_stack, %esp

       // C-Code aufrufen
       call init

       // Falls wir jemals aus init zurueckkommen sollten, halten wir einfach
       // den Prozessor an. (man braucht ihn ja nicht unnötig heißlaufen lassen.)
       hlt
       
       // Sollte es doch weitergehen, gehen wir in eine Endlosschleife
       jmp .

// 8 kB Stack fuer den Kernel. Das Label steht hinter dem freien Speicher, // weil der Stack nach unten waechst .section .bss .space 8192 kernel_stack:\</asm\>

An dieser Stelle wären wir mit dem Code fertig. Jetzt müssen wir ihn noch kompilieren und irgendwie ausprobieren. Man kann natürlich von Hand den Compiler und den Linker aufrufen, aber es empfiehlt sich, *make* dafür zu benutzen. make übersetzt immer nur alle Dateien neu, die sich tatsächlich geändert haben, und es vergisst dabei auch nichts. Eine passende *[Makefile](https://github.com/lowlevel-eu/wiki/wiki/Makefile "Makefile")* (das ist der Dateiname der Steuerdatei für make) könnte beispielsweise so aussehen:

    SRCS = $(shell find -name '*.[cS]')
    OBJS = $(addsuffix .o,$(basename $(SRCS)))

    CC = gcc
    LD = ld

    ASFLAGS = -m32
    CFLAGS = -m32 -Wall -g -fno-stack-protector -nostdinc
    LDFLAGS = -melf_i386 -Ttext=0x100000

    kernel: $(OBJS)
        $(LD) $(LDFLAGS) -o $@ $^

    %.o: %.c
        $(CC) $(CFLAGS) -c -o $@ $^

    %.o: %.S
        $(CC) $(ASFLAGS) -c -o $@ $^

    clean:
        rm $(OBJS)

    .PHONY: clean

Erwähnenswert ist vor allem die Option *-Ttext=0x100000* für ld. Das ist die Adresse, an die der Kernel geladen werden soll und an der er ausgeführt wird. GRUB kann einen Kernel nicht an eine niedrigere Adresse als 1 MB laden und 0x100000 sind genau 1 MB.

Die Werte für CC und LD müssen ggf. angepasst werden, so dass sie auf einen Compiler bzw. Linker zeigen, der i386-ELF-Dateien erzeugt. Mit dem Crosscompiler unter Windows könnte es beispielsweise sein, dass für CC *i586-elf-gcc* und für LD *i586-elf-ld* eingetragen werden muss.

Nach einem Aufruf von *make* solltest Du jetzt eine Datei *kernel* vorfinden. Jetzt müssen wir ihn nur noch irgendwie ausführen. Dazu gibt es mehrere Möglichkeiten:

- qemu kann ab Version 0.11 Multiboot-Kernel direkt laden. *qemu -kernel kernel* bringt unseren Kernel zur Ausführung und schreibt ein wunderschönes Hello World in die linke obere Ecke. Den Rest des Bildschirms zu löschen haben wir leider vergessen, so dass das über irgendwelche BIOS-Meldungen geschrieben wird.
- Jeder beliebige Emulator kann von Disketten-Images booten, z.B. qemu mit *qemu -fda floppy.img*. Wir brauchen also ein Diskettenimage, das GRUB und unseren Kernel enthält. Dazu gibt es den Artikel zu [GRUB legacy](https://github.com/lowlevel-eu/wiki/wiki/Grand-Unified-Bootloader#grub-legacy "GRUB") in diesem Wiki.
- Ein echter PC und eine echte Floppy geht natürlich auch. Dazu entweder das Image erstellen und auf Diskette schreiben (z.B. mit *dd* oder *rawrite*) oder direkt eine GRUB-Diskette nehmen und den Kernel darauf kopieren

Wenn wir nicht mit qemu 0.11 direkt booten, sondern ein Diskettenimage (bzw. eine echte Diskette) benutzen, begrüßt uns nach dem Booten GRUB (jedenfalls, wenn keine menu.lst angelegt wurde). Der Kernel kann dann folgendermaßen gestartet werden:

    kernel /kernel
    boot

## Multiboot-Header in einer eigenen Sektion

Der Kernel scheint zwar wunderbar zu funktionieren, aber er enthält einen Fehler. Der Fehler ist im Moment nicht dramatisch, aber irgendwann wird er unerwartet zuschlagen - wir sollten es deshalb lieber gleich richtig machen.

Wie bereits erwähnt muss der Multiboot-Header des Kernels in den ersten 8 kB der Datei liegen. Das funktioniert im Moment mehr oder weniger zufälligerweise. Die Sektion .text landet zwar am Anfang der Binary, aber in welcher Reihenfolge die Dateien hineingeschrieben werden, bleibt dem Linker überlassen. Wir können es aber erzwingen, dass .text mit dem Multiboot-Header anfängt: Wir legen ihn zunächst in seine eigenen Sektion und sagen dem Linker dann, wie er es zusammenbauen soll.

Dazu ändern wir den Anfang der start.S folgendermaßen ab: \<asm\>.section multiboot

1.  define MB_MAGIC 0x1badb002
2.  define MB_FLAGS 0x0
3.  define MB_CHECKSUM -(MB_MAGIC + MB_FLAGS)

// Der Multiboot-Header .align 4 .int MB_MAGIC .int MB_FLAGS .int MB_CHECKSUM

.section .text

// Init ist eine Funktion aus init.c .extern init

// \_start muss global sein, damit der Linker es findet und als Einsprungspunkt ...\</asm\>

Außerdem erstellen wir ein *Linkerskript*, die Datei kernel.ld:

    /*  Bei _start soll die Ausfuehrung losgehen */
    ENTRY(_start)

    /*
     * Hier wird festgelegt, in welcher Reihenfolge welche Sektionen in die Binary
     * geschrieben werden sollen
     */
    SECTIONS
    {
        /*
         * . ist die aktuelle Position in der Datei. Wir wollen den Kernel wie gehabt
         * an 1 MB laden, also muessen wir dort die erste Sektion hinlegen
         */
        . = 0x100000;

        /*
         * Der Multiboot-Header muss zuerst kommen (in den ersten 8 kB).
         * Die Standardsektionen einfach hintereinander weg einbinden.
         */
        .text : {
            *(multiboot)
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

Anschließend muss der Linker auch noch wissen, dass er die Datei benutzen soll. Daher wird in der Makefile das *-Ttext=0x100000* zu einem *-Tkernel.ld*

## printf

Nach sehr viel sehr detailliert besprochenem Code kommen wir zu einigen Aufgaben, die ich dem geneigten Leser gern zur Übung überlassen würde. Es handelt sich dabei um Funktionen zur [Textausgabe](https://github.com/lowlevel-eu/wiki/wiki/Textausgabe "Textausgabe") - denn man kann keine Fehler finden, wenn man sich keine Informationen anzeigen lassen kann. Wir brauchen mindestens:

- Eine Funktion zum Löschen des Bildschirms (nicht zwingend, sieht aber einfach schöner aus)
- Eine Funktion um Text auszugeben
- Eine Funktion um Zahlen in dezimaler Schreibweise auszugeben
- Eine Funktion um Zahlen und Pointer in hexadezimaler Schreibweise auszugeben

In den folgenden Teilen gehe ich davon aus, dass die unteren drei Aufgaben von einer Funktion kprintf() übernommen werden, die für die genannten Fälle genau so funktioniert, wie die normale printf()-Funktion. Die Funktionen kommen am besten in ihre eigene Quellcodedatei (z.B. console.c) und werden in den Beispielen in der Headerdatei *console.h* erwartet.

Für die Implementierung von printf benötigt man *stdarg.h*, um die variable Parameterliste auszuwerten. gcc bietet dafür bereits Builtins an (bzw. eine komplette *stdarg.h*, wenn man einen [Cross-Compiler](https://github.com/lowlevel-eu/wiki/wiki/Cross-Compiler "Cross-Compiler") benutzt), so dass die Headerdatei nur folgendes enthalten muss: \<c\> typedef \_\_builtin_va_list va_list;

1.  define va_start(ap, X) \_\_builtin_va_start(ap, X)
2.  define va_arg(ap, type) \_\_builtin_va_arg(ap, type)
3.  define va_end(ap) \_\_builtin_va_end(ap)

\</c\>

Außerdem könnte es eine gute Idee sein, alle Ausgaben auch auf der [seriellen Schnittstelle](https://github.com/lowlevel-eu/wiki/wiki/Serielle-Schnittstelle "Serielle Schnittstelle") auszugeben. Die Emulatoren können eigentlich alle die Ausgaben auf der seriellen Schnittstelle auf der Konsole anzeigen oder in eine Datei schreiben. Das macht es unnötig, Dinge aus dem Emulator abzuschreiben (z.B. Adressen in Fehlermeldungen).

Die Datei init.c sollte hinterher nur noch so aussehen (abgesehen vielleicht von einem Aufruf, um den Bildschirm zu löschen): \<c\>#include "console.h"

void init(void) {

       kprintf("Hello World!\n");

}\</c\>

## Troubleshooting

*→ Hauptartikel: [Troubleshooting](https://github.com/lowlevel-eu/wiki/wiki/Erste-Hilfe "Troubleshooting") (gilt natürlich auch für die folgenden Artikel der OS-Dev für Einsteiger Serie)*

### undefined reference to \`init'

Du benutzt einen [C++](https://github.com/lowlevel-eu/wiki/wiki/C%2B%2B "C++")-Compiler zum kompilieren und hast die Funktion *void init(void)* im Sourcecode aber nicht *extern "C"* deklariert, siehe auch [hier](https://github.com/lowlevel-eu/wiki/wiki/C%2B%2B "C++").

## Weitere Quellen

Hier und jeweils am Ende der folgenden Teile der Reihe folgt eine Auflistung von externen Quellen, die sich eignen, um bei Unklarheiten nachzuschlagen oder das jeweilige Thema zu vertiefen. Es ist empfehlenswert, sich vor allem auch damit vertraut zu machen, wie man offizielle Spezifikationen zu lesen hat (denn spätestens zu fortgeschritteneren Themen gibt es keine Tutorials mehr).

- [Multiboot](https://github.com/lowlevel-eu/wiki/wiki/Multiboot "Multiboot")-Spezifikation: <http://www.gnu.org/software/grub/manual/multiboot/multiboot.pdf>
- Der Quellcode eines Beispielkernels zu diesem und den folgenden Teilen der Tutorialreihe kann man [hier](http://git.tyndur.org/?p=tutorial.git;a=summary) einsehen. Der Sourcecode ist **nicht** dazu gedacht, kopiert zu werden, sondern sollte nur im Notfall verwendet werden, um eine unverstandene Kleinigkeit nachzuschauen. Falls größere Verständnisprobleme auftauchen, kann jederzeit im Forum oder im [IRC](https://github.com/lowlevel-eu/wiki/wiki/IRC "IRC") nachgefragt werden.

  

|  |  |  |
| ---------------------------------------------------------------------------------------------------------------------------- | ---------------- | ----------------------------------------------------------------------------------------------------------- |
| « [Teil 3 - Trockenübungen](https://github.com/lowlevel-eu/wiki/wiki/Teil-3-Trocken%C3%BCbungen "Teil 3 - Trockenübungen") | **Navigation** | [Teil 5 - Interrupts](https://github.com/lowlevel-eu/wiki/wiki/Teil-5-Interrupts "Teil 5 - Interrupts") » |

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/9919/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1897/index.html)

<!-- MediaWiki page 1897; revision 9919; parent 9366; 2011-07-12T18:42:48Z -->
