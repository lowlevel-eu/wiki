# Linker

Diese Seite ist ein Artikel, welcher **mehr** haben könnte..  

Wenn du mehr darüber weißt oder recherchieren willst, bist **du** aufgerufen, dies zu tun. Wenn du dir in einer Sache nicht sicher bist, dann stell es auf die Diskussionsseite.

Ein **Linker** ist ein Programm, das (z.B. vom Compiler generierte) Objektdateien mit anderen Objektdateien und/oder Libraries verknüpft.

  

## Funktionsweise

Ein Beispiel: Das gute, alte "Hello, world!"-Programm soll kompiliert, aber noch nicht gelinkt werden.

\<c\>

1.  include \<stdio.h\>

int main() {

       printf("Hello, world!\n");

} \</c\>

Kompilieren kann man das Programm mit folgendem Befehl:

` gcc -c -o hello.o hello.c `

Das "-c" sorgt dafür, dass der gcc vorerst nur kompiliert und noch nicht linkt.

Nun wurde eine Objektdatei erstellt. Diese enthält zwar bereits den übersetzten Code aus hello.c, aber man könnte sie noch nicht ausführen:

` $ gcc -c -o hello hello.c $ ./hello bash: ./hello: Keine Berechtigung $ chmod u+x hello $ ./hello bash: ./hello: Kann die Datei nicht ausführen. `

Woran liegt das? Nun, wir benutzen in hello.c die Funktion printf() aus stdio.h. Allerdings genügt es nicht, stdio.h einfach zu inkludieren, wie man sieht. Zur Erklärung ein Auszug aus stdio.h:

\<c\> extern int printf (\_\_const char \*\_\_restrict \_\_format, ...); \</c\>

Die Parameterliste soll uns hier nicht interessieren. Deutlich wichtiger (zumindest im Zusammenhang mit diesem Artikel) ist das Schlüsselwort "extern" vor der eigentlichen Funktionsdeklaration. Dieses Schlüsselwort besagt, dass die Funktion existiert (jedoch nicht in der aktuellen Quelldatei) und beruhigt somit den Compiler, der sonst eine Fehlermeldung oder zumindest eine Warnung ausgegeben hätte, wenn man printf() ohne diese Deklaration verwendet hätte.

Nun kommt der Linker ins Spiel. Dessen Aufgabe ist es, die Objektdatei (bzw. in diesem Fall Library), die die Funktion enthält, so mit dem Programm zu verknüpfen, dass die Funktion auch tatsächlich aufgerufen werden kann. Dazu genügt folgender Befehl:

` $ gcc -c -o hello.o hello.c $ gcc hello.o -o hello $ ./hello Hello, world! `

Der gcc ruft selbstständig den Linker mit allen benötigten Libraries auf und erzeugt eine ausführbare Datei, die nun auch die Funktion printf() (sowie alle anderen Funktionen, die in stdio.h als extern deklariert wurden) enthält.

## Linkerskript

Ein Linkerskript ist eine Datei, in der die Optionen für den Linker, insbesondere die Position der einzelnen Segmente im Speicher, festgelegt sind. Allerdings können alle Optionen auch als Kommandozeilenargument an den Linker übergeben werden. Ein Linkerskript ist insbesondere in der Betriebssystementwicklung von besonderer Bedeutung, da hier der Kernel an einen Teil im Speicher geladen wird, den der Linker von sich aus nicht kennt (z. B. wird der Bootloader an 0x7C00 geladen und GRUB kann den Kernel erst ab der Position 1 MB laden), anders als etwa Programme für MS DOS, die immer an die Adresse 0x100 geladen werden.

Ein Linkerskript könnte in etwa so aussehen (hier das Beispiel aus der Reihe [OS-Dev für Einsteiger](https://github.com/lowlevel-eu/wiki/wiki/OS-Dev-f%C3%BCr-Einsteiger "OS-Dev für Einsteiger"), das man [hier](https://github.com/lowlevel-eu/wiki/wiki/Teil-4-Hello-World#multiboot-header-in-einer-eigenen-sektion "Teil 4 - Hello World") finden kann): ` /* Bei _start soll die Ausfuehrung losgehen */ ENTRY(_start) `

`/* `

    * Hier wird festgelegt, in welcher Reihenfolge welche Sektionen in die Binary
    * geschrieben werden sollen
    */

SECTIONS {

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

`} `

Am besten nimmt man sich für sein Linkerscript ein vorhandenes Exemplar und ändert die Einträge, z. B. "\_main" statt "\_start", eine andere Position des text-Segments usw. Wer sich dennoch näher mit Linkerscripts befassen möchte, findet [hier](http://sourceware.org/binutils/docs/ld/index.html) das Handbuch zum ld.

## Weblinks

- [GNU ld Handbuch](http://sourceware.org/binutils/docs/ld/index.html)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/10781/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1932/index.html)

<!-- MediaWiki page 1932; revision 10781; parent 10761; 2012-09-10T12:22:01Z -->
