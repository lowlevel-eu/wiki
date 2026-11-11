# Teil 3 - Trockenübungen

|  |  |  |
| -------------------------------------------------------------------------------------------------------------------- | ---------------- | -------------------------------------------------------------------------------------------------------------- |
| « [Teil 2 - Assembler 101](Teil-2-Assembler-101 "Teil 2 - Assembler 101") | **Navigation** | [Teil 4 - Hello World](Teil-4-Hello-World "Teil 4 - Hello World") » |

## Überblick

In diesem Teil geht es zunächst darum, ein paar Sachen anzuschauen, die nicht direkt mit der Betriebssystementwicklung zu tun haben. Sie haben mehr etwas damit zu tun, wie Programme bzw. die Buildchain allgemein funktionieren. Ein Grundverständnis dafür zu haben, ist für die Entwicklung eines Betriebssystems unverzichtbar. Wer sich mit all dem schon auskennt, möchte diesen Teil möglicherweise überspringen oder nur überfliegen.

Als Basis für die Trockenübungen wird ein Linuxsystem benutzt. Die Konzepte lassen sich ohne weiteres auf Windows oder andere Systeme übertragen, allerdings unterscheiden sich die konkreten Werte und möglicherweise auch die benutzten Programme. Wer unter Windows [MinGW und ggf. MSYS](Crosscompiler-f%C3%BCr-Windows "Crosscompiler für Windows") installiert hat, wird aber die meisten Beispiele ohne weiteres nachvollziehen können.

## Hello World unter Linux

Das erste Objekt, das wir uns genauer anschauen wollen, ist das gute alte Hello World (hello01.c):

``` c
#include <stdio.h>

int main(void)
{
        printf("Hello world!\n");
        return 0;
}
```

Wie wir alle wissen, lässt sich dieses Programm mit *gcc -m32 -o hello01 hello01.c* in eine ausführbare Datei hello01 kompilieren (ich produziere hier absichtlich eine 32-Bit-Datei auf meinem 64-Bit-System, weil noch nicht jeder ein 64-Bit-System hat und wir hinterher auch ein 32-Bit-System schreiben wollen). gcc ist aber nicht eine große Blackbox, die vom C-Code einlesen bis zur ausführbaren Datei alles macht, sondern ruft auch nur andere Programme auf, die die eigentlichen Teilschritte machen. Mit *--verbose* kann man sich diese Schritte anzeigen lassen:

     /usr/lib64/gcc/x86_64-suse-linux/4.3/cc1 -quiet -v -imultilib 32 hello01.c -qu
    iet -dumpbase hello01.c -m32 -mtune=generic -auxbase hello01 -version -o /tmp/c
    ca4VtjX.s
    #include "..." search starts here:
    #include <...> search starts here:
     /usr/local/include
     /usr/lib64/gcc/x86_64-suse-linux/4.3/include
     /usr/lib64/gcc/x86_64-suse-linux/4.3/include-fixed
     /usr/lib64/gcc/x86_64-suse-linux/4.3/../../../../x86_64-suse-linux/include
     /usr/include
    End of search list.
    GNU C (SUSE Linux) version 4.3.2 [gcc-4_3-branch revision 141291] (x86_64-suse-
    linux)
            compiled by GNU C version 4.3.2 [gcc-4_3-branch revision 141291], GMP v
    ersion 4.2.3, MPFR version 2.3.2.
    GGC heuristics: --param ggc-min-expand=100 --param ggc-min-heapsize=131072
    Compiler executable checksum: 8f0c060b821c640f95700a11f41dd35c
    COLLECT_GCC_OPTIONS='-v' '-m32' '-o' 'hello01' '-mtune=generic'
     /usr/lib64/gcc/x86_64-suse-linux/4.3/../../../../x86_64-suse-linux/bin/as -V -
    Qy --32 -o /tmp/ccIFHiAK.o /tmp/cca4VtjX.s
    GNU assembler version 2.19 (x86_64-suse-linux) using BFD version (GNU Binutils;
     openSUSE 11.1) 2.19
    COMPILER_PATH=/usr/lib64/gcc/x86_64-suse-linux/4.3/:/usr/lib64/gcc/x86_64-suse-
    linux/4.3/:/usr/lib64/gcc/x86_64-suse-linux/:/usr/lib64/gcc/x86_64-suse-linux/4
    .3/:/usr/lib64/gcc/x86_64-suse-linux/:/usr/lib64/gcc/x86_64-suse-linux/4.3/../.
    ./../../x86_64-suse-linux/bin/
    LIBRARY_PATH=/usr/lib64/gcc/x86_64-suse-linux/4.3/32/:/usr/lib64/gcc/x86_64-sus
    e-linux/4.3/../../../../x86_64-suse-linux/lib/../lib/:/usr/lib64/gcc/x86_64-sus
    e-linux/4.3/../../../../lib/:/lib/../lib/:/usr/lib/../lib/:/usr/lib64/gcc/x86_6
    4-suse-linux/4.3/:/usr/lib64/gcc/x86_64-suse-linux/4.3/../../../../x86_64-suse-
    linux/lib/:/usr/lib64/gcc/x86_64-suse-linux/4.3/../../../:/lib/:/usr/lib/
    COLLECT_GCC_OPTIONS='-v' '-m32' '-o' 'hello01' '-mtune=generic'
     /usr/lib64/gcc/x86_64-suse-linux/4.3/collect2 --build-id --eh-frame-hdr -m elf
     _i386 -dynamic-linker /lib/ld-linux.so.2 -o hello01 /usr/lib64/gcc/x86_64-suse
     -linux/4.3/../../../../lib/crt1.o /usr/lib64/gcc/x86_64-suse-linux/4.3/../../.
     ./../lib/crti.o /usr/lib64/gcc/x86_64-suse-linux/4.3/32/crtbegin.o -L/usr/lib6
     4/gcc/x86_64-suse-linux/4.3/32 -L/usr/lib64/gcc/x86_64-suse-linux/4.3/../../..
     /../x86_64-suse-linux/lib/../lib -L/usr/lib64/gcc/x86_64-suse-linux/4.3/../../
     ../../lib -L/lib/../lib -L/usr/lib/../lib -L/usr/lib64/gcc/x86_64-suse-linux/4
     .3 -L/usr/lib64/gcc/x86_64-suse-linux/4.3/../../../../x86_64-suse-linux/lib -L
     /usr/lib64/gcc/x86_64-suse-linux/4.3/../../.. /tmp/ccIFHiAK.o -lgcc --as-neede
     d -lgcc_s --no-as-needed -lc -lgcc --as-needed -lgcc_s --no-as-needed /usr/lib
     64/gcc/x86_64-suse-linux/4.3/32/crtend.o /usr/lib64/gcc/x86_64-suse-linux/4.3/
     ../../../../lib/crtn.o

Die wesentlichen Schritte darin sind:

- **Kompilieren**: Zum einen ist da der Aufruf von *cc1*. cc1 ist der eigentliche Compiler, er übersetzt C-Code in Assemblercode. Wenn man *gcc -S hello.c* aufruft, ruft gcc nur den Compiler auf und lässt die Assemblerdatei als *hello.s* liegen.
- **Assemblieren**: Der Assembler wandelt den Assemblercode in eine Objektdatei um. Er heißt üblicherweise *as*, wenn betont werden soll, dass es sich um den GNU-Assembler handelt (z.B. auf anderen Systemen, wo andere Assembler üblich sind), wird er auch *gas* genannt. Wenn man *gcc -c hello.c* aufruft, wird bis an dieser Stelle gebaut und die Objektdatei *hello.o* bleibt übrig. Eine Objektdatei enthält zwar schon Maschinencode, aber er ist noch nicht in seiner endgültigen Form. Externe "Symbole" (d.h. Funkions- oder Variablennamen) sind noch als Verweise (*Referenzen*) vorhanden - printf selbst existiert in der Objektdatei nicht.
- **Linken**: Der Linker *ld* (in meinem Fall indirekt über collect2 aufgerufen) nimmt mehrere Objektdateien (oder Bibliotheken, die im Prinzip auch nur eine Sammlung von Objektdateien sind) und produziert daraus die endgültige ausführbare Datei. An dieser Stelle muss der Linker dann auch printf *auflösen* können, d.h. die Adresse einsetzen, an der printf am Ende tatsächlich liegt. Mit *-lc* wird die Standardbibliothek *libc* eingebunden, die unter anderem diese Funktion enthält.

Genaugenommen habe ich beim Linker nicht ganz die Wahrheit gesagt - was ich beschrieben habe ist *statisches Linken* (das ist auch, was wir vorerst brauchen, wenn wir unser Betriebssystem schreiben). In Wirklichkeit werden Linuxprogramme normal dynamisch gelinkt, d.h. auch die ausführbare Datei enthält noch nicht die endgültigen Adressen, sondern nur Referenzen. Das Programm wird dann erst direkt bei der Ausführung vom Betriebssystem mit den Bibliotheken (Shared Libraries; \*.so unter Linux oder \*.dll unter Windows) gelinkt. Statisches Linken kann man mit *gcc -static* erzwingen, aber das macht die erzeugte Datei nur unübersichtlich, also lassen wir das erst einmal bleiben.

Zeit, uns anzuschauen, was der Compiler uns tatsächlich gebastelt hat. Schauen wir uns also die Objektdatei einmal mit *objdump -d hello01.o* an:

    hello01.o:     file format elf32-i386


    Disassembly of section .text:

    00000000 <main>:
       0:   8d 4c 24 04             lea    0x4(%esp),%ecx
       4:   83 e4 f0                and    $0xfffffff0,%esp
       7:   ff 71 fc                pushl  -0x4(%ecx)
       a:   55                      push   %ebp
       b:   89 e5                   mov    %esp,%ebp
       d:   51                      push   %ecx
       e:   83 ec 04                sub    $0x4,%esp
      11:   c7 04 24 00 00 00 00    movl   $0x0,(%esp)
      18:   e8 fc ff ff ff          call   19 <main+0x19>
      1d:   b8 00 00 00 00          mov    $0x0,%eax
      22:   83 c4 04                add    $0x4,%esp
      25:   59                      pop    %ecx
      26:   5d                      pop    %ebp
      27:   8d 61 fc                lea    -0x4(%ecx),%esp
      2a:   c3                      ret

Wir sehen, dass an der Adresse 0 das Symbol main steht - das ist also der Anfang unserer main-Funktion. Die folgenden Zeilen enthalten immer jeweils die Adresse, an der der Befehl steht (richtig interessant wird das erst in der ausführbaren Datei, aber auch hier schon könnte auf eine der Adressen zugegriffen werden), in der Mitte die Opcodes und rechts die Übersetzung in Assembler. Man sieht außerdem, dass die Referenzen noch nicht aufgelöst sind: Für call wird alles angezeigt, nur nicht, dass es printf aufruft.

Man kann sich vorstellen, dass das mit einer etwas größerern Funktion schnell unübersichtlich wird. Wir können das aber noch besser: *gcc -c -O0 -g hello01.c* fügt mit *-g* Debuginformationen ein und *-O0* schaltet alle Optimierungen aus (die waren bei uns sowieso noch aus, aber ich falls man sie einschaltet, sollte man daran denken, dass mit ausgeschalteter Optimierung der Assemblercode sehr viel leichter zu lesen ist). Anschließend nehmen wir für objdump die Parameter *-S* (zeigt den C-Quellcode an, braucht dafür die Debuginformationen) und *-r* (zeigt an, worauf die Referenzen verweisen). Also *objdump -Sr hello01.o*:

    hello01.o:     file format elf32-i386


    Disassembly of section .text:

    00000000 <main>:
    #include <stdio.h>

    int main(void)
    {
       0:   8d 4c 24 04             lea    0x4(%esp),%ecx
       4:   83 e4 f0                and    $0xfffffff0,%esp
       7:   ff 71 fc                pushl  -0x4(%ecx)
       a:   55                      push   %ebp
       b:   89 e5                   mov    %esp,%ebp
       d:   51                      push   %ecx
       e:   83 ec 04                sub    $0x4,%esp
        printf("Hello world!\n");
      11:   c7 04 24 00 00 00 00    movl   $0x0,(%esp)
                            14: R_386_32    .rodata
      18:   e8 fc ff ff ff          call   19 <main+0x19>
                            19: R_386_PC32  puts
        return 0;
      1d:   b8 00 00 00 00          mov    $0x0,%eax
    }
      22:   83 c4 04                add    $0x4,%esp
      25:   59                      pop    %ecx
      26:   5d                      pop    %ebp
      27:   8d 61 fc                lea    -0x4(%ecx),%esp
      2a:   c3                      ret

Man sieht, dass jetzt immer zuerst die C-Zeile angezeigt wird und dann der Assemblercode, mit dem sie umgesetzt worden ist. In der Betriebssystementwicklung passiert es einem oft, dass man bei einem Absturz nur die Adresse weiß, an der etwas schiefgegangen ist. Durch diese objdump-Ausgabe findet man dann sehr schnell den zugehörigen C-Befehl, und möglicherweise ist der zugehörige Assemblercode klein genug, dass man ihn nachvollziehen und dann sogar genau sagen kann, welcher Teil der C-Zeile schiefgeht.

Die zweite Neuerung ist, dass die Referenzen aufgelöst werden. Wir haben hier zum einen eine Referenz auf irgendwelche Daten in .rodata (das ist unser String "Hello World") und zum zweiten auf eine externe Funktion, nämlich puts. Huch, wollten wir nicht printf? Ja, aber der Compiler hat hier ein wenig optimiert, weil wir die Komplexität von printf hier nicht brauchen (man kann das übrigens über die Kommandozeilenoption -fno-builtin abschalten). Dumm nur, wenn das eigene Betriebssystem zwar schon printf hat, aber noch kein puts... Gut, dass wir jetzt eine Methode haben, dem Compiler auf die Finger zu schauen und solche Dinge zu erkennen.

Nachdem ich jetzt erklärt habe, wie toll -g ist, möchte ich auch den Nachteil nicht verschweigen:

    -rw-r--r-- 1 kevin users 2,6K 25. Jul 12:36 hello01.debug.o
    -rw-r--r-- 1 kevin users  968 25. Jul 12:36 hello01.o

Es hält sich bei diesem kleinen Beispiel noch in Grenzen, aber Debuginformationen benötigen natürlich Speicherplatz. Die ausführbare Datei wird damit also am Ende größer. Viele OS-Programmierer verwenden am Anfang Disketten, so dass der Platz recht schnell ausgeht. Die Lösung ist einfach: Man kompiliert mit Debuginformationen, damit man sie hat, wenn man etwas untersuchen muss. Auf die Diskette kopiert man aber eine Version, aus der die Debuginformatinen gelöscht sind. Das geht mit dem Befehl *strip hello01* (oder auch mit dem Dateinamen einer einzelnen Objektdatei - probier es aus, objdump zeigt hinterher außer dem Assemblercode nichts nützliches mehr an).

Jetzt ist es Zeit, auch einmal die ausführbare Datei anzuschauen. Es schadet sicher nichts, das mit den schon vorgestellten Methoden zu machen - allerdings wird die Ausgabe etwas länger (interessant ist zum Beispiel, dass jetzt die richtigen Adressen angezeigt werden, an denen das Programm später tatsächlich ausgeführt wird). Ich wähle für hier eine etwas platzsparendere Variante: *objdump -t -j .text hello01* zeigt alle Symbole in der Sektion .text an, also unseren Code.

    hello01:     file format elf32-i386

    SYMBOL TABLE:
    08048360 l    d  .text  00000000              .text
    08048390 l     F .text  00000000              __do_global_dtors_aux
    080483f0 l     F .text  00000000              frame_dummy
    080484b0 l     F .text  00000000              __do_global_ctors_aux
    08048440 g     F .text  00000005              __libc_csu_fini
    08048360 g     F .text  00000000              _start
    08048450 g     F .text  0000005a              __libc_csu_init
    080484aa g     F .text  00000000              .hidden __i686.get_pc_thunk.bx
    08048414 g     F .text  0000002b              main

Wir selbst hatten eigentlich nur main definiert. Den Rest steuert der Compiler bei. Der tatsächliche Einsprungspunkt eines Programms ist nämlich nicht main, sondern \_start, das sich in der Datei *crt0.o* befindet (und das wir oben dazugelinkt haben). Es initialisiert die Standardbibliothek, holt sich vom Betriebssystem die Kommandozeilenparameter und ruft dann main auf. Wenn main fertig ist, gibt es den Exitcode an das Betriebssystem weiter, das den Prozess dann beendet. Die anderen Symbole sind interne Dinge, die von \_start benutzt werden, die wir aber vorerst ignorieren können (aber wenn man sie in der \_start seines eigenen Betriebssystems nicht aufruft, tun Dinge wie Konstruktoren nicht - was allerdings eine ganze Weile lang gut verschmerzbar ist).

## Hello World selbergemacht

Nachdem wir jetzt wissen, wie das so ungefähr abläuft, wollen wir das ganze selber machen. Keine blöde fertige libc, wir sind selber groß. Wenn wir anfangen, unser Betriebssystem zu schreiben, können wir die Linux-libc ja schließlich auch nicht mehr benutzen.

Wir werden auch hier wieder ein Hello World zum laufen bekommen, allerdings setzen wir direkt auf Linux auf (deswegen wird das Programm auch unter Windows nicht funktionieren - tut mir leid). Wie werden an zwei Stellen Kernelfunktionen von Linux aufrufen, beim Ausgeben des Hello-World-Texts und beim Beenden des Programms. Um den Aufruf durchzuführen, müssen wir den Interrupt 0x80 auslösen; die Nummer der Funktion (des *Syscalls*) steht in eax, die Parameter werden nacheinander in den Registern ebx, ecx, edx, esi und edi übergeben. Der Rückgabewert landet in eax. Die Funktionen, die wir benutzen wollen, sind:

    1 - int sys_exit(int status)
    4 - ssize_t sys_write(unsigned int fd, const char * buf, size_t count)

Also frisch ans Werk:

``` c
#define SYSCALL_EXIT    1
#define SYSCALL_WRITE   4

char hello[] = "Hello World!\n";

void _start(void)
{
    // sys_write(1, hello, sizeof(hello))
    asm("int $0x80" : : "a" (SYSCALL_WRITE), "b" (1), "c" (hello), "d"
        (sizeof(hello)));

    // sys_exit(0)
    asm("int $0x80" : : "a" (SYSCALL_EXIT), "b" (0));
}
```

Wen es interessiert, die genaue Syntax des Inlineassemblers ist in [Inline-Assembler mit GCC](Inline-Assembler-mit-GCC "Inline-Assembler mit GCC") beschrieben. An dieser Stelle befülle ich einfach die Register mit den Parametern und löse dann den Interrupt 0x80 aus. Linken wollen wir dieses Mal selber, damit uns keine libc in die ausführbare Datei hineingezogen wird:

    gcc -c hello02.c
    ld -o hello02 hello02.o

Wenn wir irgendwann das erste Programm für unser System schreiben, wird es vielleicht so ähnlich aussehen wie dieses. Unser Kernel wird kein anderes System aufrufen können, denn wir schreiben einen 32-Bit-Kernel. Würden wir uns im Real Mode (also dem 16-Bit-Modus) aufhalten, könnten wir das BIOS auf diese Weise aufrufen. Das aber nur der Vollständigkeit halber, es spielt für uns eigentlich keine Rolle.

Aber genug der Vorrede, es wird Zeit für den Kernel.

  

|  |  |  |
| -------------------------------------------------------------------------------------------------------------------- | ---------------- | -------------------------------------------------------------------------------------------------------------- |
| « [Teil 2 - Assembler 101](Teil-2-Assembler-101 "Teil 2 - Assembler 101") | **Navigation** | [Teil 4 - Hello World](Teil-4-Hello-World "Teil 4 - Hello World") » |

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/11389/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1896/index.html)

<!-- MediaWiki page 1896; revision 11389; parent 6470; 2018-09-04T09:56:39Z -->
