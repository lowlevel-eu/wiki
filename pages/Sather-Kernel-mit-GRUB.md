# Sather-Kernel mit GRUB

Wie schon im Hauptartikel zu [Sather](Sather.md "Sather") erwähnt, ist es im Allgemeinen nicht empfehlenswert, einen Kernel in Sather zu schreiben. Dennoch werden wir hier genau das tun. Als Compiler wird GNU Sather verwendet (s. Hauptartikel), als Assembler [FASM](Flat-Assembler.md "FASM") und außerdem noch verschiedene Standard-GNU-Tools ([GCC](GNU-Compiler-Collection.md "GCC"), Binutils, Make, ...).

## Dateien

### kernel.sa

Beginnen wir mit dem Einfachsten: Dem Sathercode. Dazu brauchen wir zuerst einmal die MAIN-Klasse, die sieht so aus:

    class MAIN is
        main is
            io: STDIO := #STDIO;

            io.clear;

            io < "Moin, Welt!\n";
        end;
    end;

Wir erstellen also das Objekt io, das vom Typ STDIO ist. \#STDIO ist ein Alias für STDIO::create, ruft also den Konstruktor auf, der ein Objekt dieses Typs zurückgibt, welches schlussendlich eben io zugewiesen wird.

Anschließend wird die Routine clear aufgerufen, welche später den Bildschirm löschen soll. io \< "Moin, Welt!\n"; ist ein Alias (Syntactic Sugar ist das Stichwort) für io.is_lt("Moin, Welt!\n");, hier wird somit die Routine is_lt aufgerufen und ihr der String "Moin, Welt!\n" übergeben. Den muss sie dann „nur“ noch ausgeben.

Jetzt wird es schon schwieriger &#150; schreiben wir uns die Klasse STDIO. Die sieht in ihrer ganzen Pracht so aus:

    class STDIO is
        private attr x, y, flags: INT;

        create: STDIO is
            io: STDIO := new;
            io.x := 0;
            io.y := 0;
            io.flags := 0x07;
            return io;
        end;

        clear is
            SYS::inlined_C("memset((void *)0xB8000, 0, 4000);");
        end;

        is_lt(s: STR) is
            i: INT := 0;
            c: CHAR := '\0';
            addr: INT := 0xB8000 + (y * 80 + x) * 2;
            tflags: INT := flags;

            loop while!(i < s.length);
                c := s.char(i);
                i := i + 1;

                if c = '\n' then
                    x := 0;
                    y := y + 1;
                    if y >= 25 then
                        y := 24;
                        SYS::inlined_C("memcpy((void *)0xB8000, (void *)0xB80A0, 3840);"
                                       "memset((void *)0xB8F00, 0, 160);");
                    end;
                    addr := 0xB8000 + (y * 80 + x) * 2;
                else
                    SYS::inlined_C("*((unsigned char *)#addr++) = #c;"
                                   "*((unsigned char *)#addr++) = #tflags");
                    x := x + 1;
                    if x >= 80 then
                        x := 0;
                        y := y + 1;
                        if y >= 25 then
                            y := 24;
                            SYS::inlined_C("memcpy((void *)0xB8000, (void *)0xB80A0, 3840);"
                                           "memset((void *)0xB8F00, 0, 160);");
                            addr := 0xB8000 + (y * 80 + x) * 2;
                        end;
                    end;
                end;
            end;
        end;
    end;

Diese enthält die privaten Attribute (also nicht öffentlich verfügbar) x, y und flags. x enthält die aktuelle Spalte, y die Zeile und flags das Attributbyte. Als nächstes kommt die create-Routine (die per \#STDIO aufgerufen wird). Sie erstellt ein neues Objekt des aktuellen Typs (welcher logischerweise STDIO ist), setzt x und y auf 0 und flags auf 7 (hellgrau auf weiß). Dann gibt sie dieses Objekt zurück.

Nun kommt die erste „sinnvolle“ Funktion, clear. Hier benutzen wir Inline-C, weil es wohl das einfachste ist, um einen Speicherbereich zu leeren. Besagtes passiert über die dem C-Programmierer bekannte memset-Funktion, die den Videospeicher mit 0 befüllt.

Als nächstes zu einer Routine mit kryptischem Namen, is_lt. Diese Bezeichnung stammt nicht von mir und ist eine Abkürzung für „is less than“, wird also bei einer „\<“-Operation ausgeführt (s. o.). Sie bekommt den Operanden übergeben, welcher in unserem Fall ein String sein soll. Nun werden alle Elemente (also Zeichen) des Strings durchgegangen, wenn es sich um ein \n handelt (LF), dann gehen wir auf die nächste Zeile (und verschieben den Bildschirminhalt nötigenfalls per Inline-C nach oben &#150; obwohl ein memmove hier besser wäre, reicht aufgrund der Bufferpositionen auch ein vorwärts kopierendes memcpy). Ist es ein anderes Zeichen, dann geben wir das wieder mit Inline-C aus (und verschieben die aktuelle Ausgabeposition dementsprechend).

Das wäre es für die kernel.sa.

### entry.asm

Irgendwie müssen wir in den Kernel springen (und dabei auch gleich den Multibootheader definieren). Das geschieht hier. Eine entsprechende Assemblerdatei (für FASM) sieht so aus: \<asm\>format ELF use32

extrn main public \_start

section '.multiboot'

MULTIBOOT_PAGE_ALIGN = 00000000000000000000000000000001b MULTIBOOT_MEMORY_INFO = 00000000000000000000000000000010b MULTIBOOT_HEADER_MAGIC = 0x1BADB002 MULTIBOOT_HEADER_FLAGS = MULTIBOOT_PAGE_ALIGN+MULTIBOOT_MEMORY_INFO CHECKSUM = -(MULTIBOOT_HEADER_MAGIC+MULTIBOOT_HEADER_FLAGS)

align 4 dd MULTIBOOT_HEADER_MAGIC dd MULTIBOOT_HEADER_FLAGS dd CHECKSUM

section '.text' executable

\_start: mov esp,0x300000 call main hangman: cli hlt jmp hangman\</asm\>

In dieser ELF32 erstellen wir zwei Sektionen: Eine für den Multibootheader (wird später vom Linker an den Anfang der ELF geschoben) und eine für Code. Der Multibootheader sollte bekannt sein, der Code erstellt einfach einen Stack an der Adresse 0x300000 und ruft dann die main-Funktion auf (oben als extern (bzw. extrn) definiert). Wenn diese Funktion zurückkehrt, halten wir einfach die CPU an.

### stub.c

Jetzt zum wirklich harten Teil: Der Runtime-Lib. Unsere wird das machen, was ihr Name bereits sagt: Stubs bereitstellen. Diese können natürlich optimiert werden, allerdings ist das vorerst zumindest nicht nötig. Da Sather nicht auf Kernelentwicklung ausgelegt ist, werden jede Menge POSIX-Funktionen benutzt.

\<c\>typedef unsigned long size_t; typedef signed long off_t; typedef unsigned char uint8_t; typedef unsigned long uintptr_t; typedef void (\*sighandler_t)(int);

1.  define NULL ((void \*)0)

uintptr_t heap = 0x200000;

void \*GC_malloc_atomic(size_t size) {

       uintptr_t oheap = heap;
       heap += size;
       return (void *)oheap;

}

off_t lseek(int fd, off_t offset, int whence) {

       fd = whence;
       return offset;

}

int open() {

       static int fd = 3;

       return fd++;

}

sighandler_t signal(int signum, sighandler_t handler) {

       signum = 0;
       return handler;

}

char \*getenv() {

       return NULL;

}

size_t fwrite(const void \*ptr, size_t size, size_t nmemb, void \*stream) {

       ptr = stream;
       stream = (void *)size;
       return nmemb;

}

int fflush() {

       return 0;

}

int \_IO_getc() {

       return -1;

}

int getpid(void) {

       return 42;

}

int sprintf() {

       return 0;

}

int fork() {

       return 43;

}

int sleep() {

       return 0;

}

int system() {

       return 0;

}

void exit() {

       for (;;)
           __asm__ __volatile__ ("cli;hlt");

}

int fprintf() {

       return 0;

}

void abort() {

       exit();

}

void \*GC_malloc_atomic_ignore_off_page(size_t size) {

       uintptr_t oheap = heap;
       heap += size;
       return (void *)oheap;

}

void \*memset(void \*address, int val, size_t size) {

       uint8_t *buf = address;
       int i;

       for (i = 0; i < size; i++)
           buf[i] = val;

       return address;

}

void \*memcpy(void \*dest, void \*src, size_t size) {

       uint8_t *d = dest, *s = src;
       int i;

       for (i = 0; i < size; i++)
           d[i] = s[i];

       return dest;

}

void \*GC_malloc_ignore_off_page(size_t size) {

       uintptr_t oheap = heap;
       heap += size;
       return (void *)oheap;

}

void \*GC_malloc(size_t size) {

       uintptr_t oheap = heap;
       heap += size;
       return (void *)oheap;

}

void \*malloc(size_t size) {

       uintptr_t oheap = heap;
       heap += size;
       return (void *)oheap;

}

size_t strlen(const char \*s) {

       size_t l = 0;

       while (*(s++))
           l++;

       return l;

}

int close() {

       return 0;

}

int read() {

       return 0;

}

int setjmp() {

       return 0;

}

void longjmp() { }

int abs(int j) {

       return (j < 0) ? -j : j;

}

int getchar(void) {

       return -1;

}\</c\>

Diese Funktionen jetzt zu erklären, würde wohl zu langwierig, außerdem sollten sie ziemlich selbsterklärend sein (da es zum Großteil POSIX-Funktionen sind, die in entsprechenden Manpages erklärt werden &#150; Funktionen, die mit GC beginnen, gehören zu dem vom Sathercompiler verwendeten Garbage Collector).

### Includes

Desweiteren werden jede Menge C-Header benötigt. Ein Archiv davon habe ich [hochgeladen](http://xanclic.bplaced.net/sather-include.tar.bz2), auch hier wäre es müßig, diese zu erklären.

## Erstellung

Zuerst müssen kernel.sa, entry.asm und stub.c in ein Verzeichnis. Hier muss auch das Include-Archiv entpackt werden (so sollte ein Ordner namens „include“ erstellt werden). Nun nimmt man am besten vorgefertige Makefiles:

    CS      = sacomp
    SAFLAGS = -O_fast -only_C
    OUT     = kernel
    IN      = kernel.sa
    RM      = -rm -f

    .PHONY: all clean $(OUT).code

    all: $(OUT)

    clean:
            $(RM) -r $(OUT).code $(OUT)

    $(OUT): $(OUT).code
            $(MAKE) -C $< -f ../Makefile.fromc

    $(OUT).code: $(IN)
            $(CS) $(SAFLAGS) $< -o $(OUT)

muss als Makefile abgespeichert werden. Der Sathercompiler heißt sacomp und wird mit den Flags -O_fast (Optimieren) und -only_C (nur C-Code im Ordner kernel.code generieren und dann abbrechen, ohne diesen zu kompilieren) aufgerufen.

Die darin verwendete Makefile.fromc muss im gleichen Ordner liegen und enthält:

    LD     = ld
    ASM    = fasm
    SHOME  = $(SATHER_HOME)
    CFLAGS = -I.  -O2  -I$(SHOME)/System/Common -nostdinc -I../include -ffreestanding -nodefaultlibs -nostartfiles -g2
    CC     = gcc
    HDR    = sather.h tags.h
    CS     = kernel
    OBJ    = $(patsubst %.c,%_c.o,$(wildcard *.c))
    RM     = -rm -f

    .PHONY: all clean

    all: ../$(CS)

    clean:
            $(RM) *.o ../$(CS)

    ../$(CS): $(OBJ) entry_asm.o stub.o runtime.o ../link.ld
            $(LD) -e _start -T ../link.ld -o $@ $(OBJ) runtime.o entry_asm.o stub.o

    %_c.o: %.c $(HDR)
            $(CC) $(CFLAGS) -c $< -o $@

    runtime.o: $(SHOME)/System/Common/runtime.c $(HDR)
            $(CC) $(CFLAGS) -c $(SHOME)/System/Common/runtime.c

    entry_asm.o: ../entry.asm
            $(ASM) $< $@

    stub.o: ../stub.c
            $(CC) $(CFLAGS) -c $< -o $@

Diese dient als Ersatz der Makefile, die normalerweise verwendet wird, um den erstellten C-Code zu kompilieren.

Als letztes fehlt noch das Linkerscript link.ld, diese kann z. B. so aufgebaut sein:

    OUTPUT_FORMAT("elf32-i386")
    OUTPUT_ARCH("i386:i386")
    virtual = 0x00100000;
    physical = 0x00100000;

    SECTIONS
    {
        .multiboot virtual : AT(physical)
        {
            multiboot = .;
            *(.multiboot)
            . = ALIGN(4);
        }
        .text : AT(physical + code - multiboot)
        {
            code = .;
            *(.text)
            . = ALIGN(4);
        }
        .data : AT(physical + data - multiboot)
        {
            data = .;
            *(.data)
            . = ALIGN(4);
        }
        .bss : AT(physical + bss - multiboot)
        {
            bss = .;
            *(.bss)
            *(COMMON)
            . = ALIGN(4);
        }
    }

Hier wird eine [ELF32](Executable-and-Linking-Format.md "ELF32")-Datei für [i386](X86.md "X86") erstellt und an die Adresse 0x100000 gelinkt. Die erste Sektion in der Datei ist .multiboot (damit der Multibootheader auf jeden Fall in den ersten 8 kB liegt, wie von der Spezifikation gefordert).

  

Nun sollte ein einfacher make-Aufruf genügen und ein ELF-Kernel namens „kernel“ wird erstellt. Diese kann dann entweder zusammen mit GRUB oder einfach per „qemu -kernel kernel“ verwendet werden.

## Zusammenfassung

Ja, so erstellt man einen Kernel mit Sather. Hoffentlich habe ich euch genügend davon abgeschreckt, das weiter zu verfolgen, denn wenn ihr immer noch darauf brennt, könnte das ein Zeichen von Copy & Paste sein. ;-)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/7009/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2174/index.html)

<!-- MediaWiki page 2174; revision 7009; parent 6999; 2010-02-03T15:15:42Z -->
