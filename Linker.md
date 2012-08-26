# Linker

Diese Seite ist ein Artikel, welcher **mehr** haben könnte..  

Wenn du mehr darüber weißt oder recherchieren willst, bist **du** aufgerufen, dies zu tun. Wenn du dir in einer Sache nicht sicher bist, dann stell es auf die Diskussionsseite.

Ein **Linker** ist ein Programm, das die vom Compiler generierten Objektdateien mit anderen Objektdateien und/oder Libraries verknüpft.

  

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

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/10755/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1932/index.html)

<!-- MediaWiki page 1932; revision 10755; parent 10003; 2012-08-26T13:27:09Z -->
