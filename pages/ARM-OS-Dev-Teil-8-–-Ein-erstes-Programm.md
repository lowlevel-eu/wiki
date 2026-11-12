# ARM-OS-Dev Teil 8 – Ein erstes Programm

|  |  |  |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| « [ARM-OS-Dev Teil 7 – Physische Speicherverwaltung](ARM-OS-Dev-Teil-7-%E2%80%93-Physische-Speicherverwaltung.md "ARM-OS-Dev Teil 7 – Physische Speicherverwaltung") | **Navigation** | [ARM-OS-Dev Teil 9 – Paging](ARM-OS-Dev-Teil-9-%E2%80%93-Paging.md "ARM-OS-Dev Teil 9 – Paging") » |

## Ein erstes Testprogramm

Wie in der [x86-Reihe](Teil-8-Ein-erstes-Programm.md#ein-kleines-testprogramm "Teil 8 - Ein erstes Programm") auch soll das erste Testprogramm einfach die Zahlen 0 bis 2 ausgeben. Auch hier geschieht das durch direkten Hardwarezugriff: \<c\>#include \<stdint.h\>

1.  define SERIAL_DR \*((volatile uint8_t \*)0x16000000)
2.  define SERIAL_FR \*((volatile uint32_t \*)0x16000018)
3.  define SERIAL_BUFFER_FULL (1 \<\< 5)

static void putchar(char c) {

       while (SERIAL_FR & SERIAL_BUFFER_FULL);

       SERIAL_DR = c;

}

void \_start(void) {

       for (int i = 0; i < 3; i++)
           putchar('0' + i);

       for (;;);

}\</c\>

Das Linkerscript kann fast aus der x86-Reihe übernommen werden, außer, dass der ARM-LD kein Verständnis dafür zu haben scheint, wenn man ELFs zu einer Binary linken möchte. Daher muss die Zeile „OUTPUT_FORMAT(binary)“ entfernt werden, sodass LD eine ELF erstellt, die anschließend mit objcopy zu einer Binary umgewandelt werden kann.

## Das Programm laden

Leider haben wir keinen Bootloader, der unser Programm laden könnte – normalerweise würde man es auf den Flashspeicher laden und dann davon lesen, aber QEMU unterstützt so einen Speicher nicht. Daher müssen wir ein wenig tricksen und das Programm in den Kernel linken. Dies geschieht wieder mit einem objcopy-Aufruf.

Nehmen wir an, LD hat eine ELF-Datei namens *usertest* erstellt und unser ARM-objcopy heißt *arm-elf-objcopy*, dann könnte man mit dem folgenden Aufruf eine Binary namens *usertest.bin* erstellen:

    arm-elf-objcopy -O binary usertest usertest.bin

Diese muss nun wieder in eine Objektdatei umgewandelt werden, damit wir sie in den Kernel linken können:

    arm-elf-objcopy -I binary -O elf32-littlearm -B armv5t --rename-section .data=.rodata,alloc,load,readonly,data,contents usertest.bin usertest.incelf

Das Ergebnis ist eine Datei namens *usertest.incelf*, die die ursprüngliche Binary in einer .rodata-Section enthält. Den Anfang der Daten markiert ein Symbol namens *\_binary_usertest_bin_start*, das Ende *\_binary_usertest_bin_end*. Um die Binärdaten im Kernel zu laden, müssen diese Symbole also lediglich als *extern const void* (oder ähnlich) definiert werden und dann genügen folgende zwei Zeilen, um die Datei nach 0x00200000 zu laden und auszuführen: \<c\>memcpy((void \*)0x00200000, &\_binary_usertest_bin_start, &\_binary_usertest_bin_end - &\_binary_usertest_bin_start); init_task((void \*)0x00200000);\</c\>

## Syscalls

Als nächstes soll der direkte Hardwarezugriff durch einen Systemaufruf ersetzt werden. Systemaufrufe werden auf ARM-Prozessoren mit dem SWI-Befehl ausgeführt, er enthält eine 24-Bit-Zahl, mit der normalerweise angegeben wird, welche Funktion ausgeführt werden soll. Wir werden Funktion 0 (wird mit *swi \#0* aufgerufen) als eine *putc*-Funktion nutzen.

Parameter werden übergeben, wie das bei ARM üblich ist: Die ersten vier Parameter liegen in den Registern *r0* bis *r3* und mehr werden wir hier sowieso nicht benötigen. Nun müssen wir uns aber überlegen, wie wir die Systemaufrufsnummer in den Opcode bekommen: An sich könnten wir einfach konstant *swi \#0* benutzen, aber das wird unschön, wenn wir noch andere Systemaufrufe haben wollen. Ich habe mich hier für selbstmodifizierenden Code entschieden. Die Syscallnummer wird also vor dem SWI-Aufruf in den Opcode hineingeschrieben. Dazu benötigen wir ein Array aus zwei ARM-Befehlen, die zusammen eine einfache Funktion darstellen, ein *swi* und ein *bx r14*. Auf dieses Array kann man einen Funktionspointer zeigen lassen und damit den Code ausführen: \<c\>static uint32_t swi\[\] = {

       0xEF000000, // SWI #0
       0xE12FFF1E  // BX R14

};

static uint32_t (\*do_swi)(uint32_t r0, uint32_t r1, uint32_t r2, uint32_t r3) = (uint32_t (\*)(uint32_t, uint32_t, uint32_t, uint32_t))(uintptr_t)swi;\</c\>

Aufgabe der *putchar*-Funktion ist es dann, *swi\[0\]* zu verändern (der *swi*-Opcode) und *do_swi* mit den entsprechenden Parametern aufzurufen: \<c\>swi\[0\] = 0xEF000000 \| 0; // Syscall \#0 do_swi(c, 0, 0, 0)\</c\>

Für den Syscall Nummer 1 würde man dementsprechend *0xEF000000 \| 1* benutzen.

Damit der Kernel Syscalls erlaubt, müssen wir zunächst zur Taskerstellung zurückkommen: Entgegen unseres Kommentars brauchen wir nämlich jetzt doch einen Supervisorstack (Erinnerung: Syscalls laufen im Supervisormodus ab). Um den einzurichten, brauchen wir nur ein \<c\>uint8_t \*svc_stack = (uint8_t \*)pmm_alloc();\</c\> und ein \<c\>.svc_r13 = (uintptr_t)(svc_stack + STACK_SIZE),\</c\> an den entsprechenden Stellen.

Dann müssen wir den Systemaufruf noch abfangen. Dazu installieren wir in *start.S* einen Exceptionhandler, indem das zweite *b .* von oben durch ein *b asm_handle_swi* ersetzt wird (oben ist dann natürlich noch ein *.extern asm_handle_swi* nötig). Dieser Assembler-SWI-Handler kann dann zum Beispiel so aussehen:

    .arm
    .extern syscall
    .global asm_handle_swi

    asm_handle_swi:
    push    {r14}
    bl      syscall
    pop     {r14}
    movs    r15, r14

Nun wird noch die *syscall*-Funktion benötigt. Deren erste vier Parameter sind *r0* bis *r3*, also die Syscallparameter aus dem Userspace. Wir lassen sie allerdings noch einen fünften Parameter nehmen. Dieser wird nach der ARM-Calling-Convention vom Stack genommen, wo *r14* liegt. Dies ist dann unsere Möglichkeit, die Nummer des Syscalls herauszufinden, da der SWI-Opcode an der Adresse *r14 - 4* liegt und wir ihn damit auslesen können: \<c\>uint32_t syscall(uint32_t r0, uint32_t r1, uint32_t r2, uint32_t r3, uint32_t r14) {

       uint32_t syscall_id = ((uint32_t *)r14)[-1] & 0xFFFFFF;

       switch (syscall_id)
       {
           case 0: // putc
               kprintf("%c", r0);
               return 0;
       }

       return 0;

}\</c\>

## ELF

Anstatt einer rohen Binärdatei wäre ein richtiges Format wie ELF für das Userprogramm schön. Eine ELF statt der Binärdatei einzubinden ist erstmal nicht schwer, dazu müssen wir lediglich den objcopy-Aufruf weglassen, der aus der ELF eben eine rohe Binärdatei macht. Das Laden der ELF kann genauso wie in der [x86-Reihe](Teil-8-Ein-erstes-Programm.md#elf "Teil 8 - Ein erstes Programm") geschehen (da in dem dort gezeigten ELF-Loader darauf verzichtet wird, zu überprüfen, für welche Architektur die ELF gebaut wurde – im Grunde der einzige Unterschied zwischen i386- und ARM-ELFs, wenn man Executables betrachtet).

Geladen und ausgeführt wird die ELF dementsprechend mit: \<c\>init_elf32(&\_binary_usertest_start);\</c\>

Man beachte, dass das Label jetzt nicht mehr *\_binary_usertest\_**bin**\_start* heißt, sondern nur noch *\_binary_usertest_start* (es wird nach dem Dateinamen benannt; da jetzt direkt aus der *usertest*-ELF eine in den Kernel linkbare Objektdatei gemacht wird, heißt also auch das Label anders).

## Weitere Quellen

Der fertige Code bis zum ersten Userprogramm befindet sich [hier](https://gitorious.org/arm-os-dev/kernel/trees/a55784076e5ee62cf744362c1004442001ecc0c0), der mit SWI [hier](https://gitorious.org/arm-os-dev/kernel/trees/c22abdb3f0c57ffc066885c0380c8bb098641499) und der mit ELF-Loader [hier](https://gitorious.org/arm-os-dev/kernel/trees/b0808e5398b36b764b2557df19376527fea0517b).

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/9789/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2427/index.html)

<!-- MediaWiki page 2427; revision 9789; parent 0; 2011-05-14T20:25:17Z -->
