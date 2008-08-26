# C

C ist eine bekannte ältere Programmiersprache. Sie verfolgt das Ziel bei vergleichbarer Ausführungsgeschwindigkeit plattformunabhängiger und abstrakter als [Assembler](https://github.com/lowlevel-eu/wiki/wiki/Assembler "Assembler") zu sein. Direkte Weiterentwicklung von C ist [C++](https://github.com/lowlevel-eu/wiki/wiki/C%2B%2B "C++").

# Kernelprogrammierung mit C

Da man mit C sehr hardwarenah programmieren kann, eignet sich die Sprache zur Programmierung eines Kernels. Es ist sogar die überwiegende Anzahl der Betriebssystemkernel in C geschrieben. Für andere Bereiche ist C jedoch nicht sonderlich geeignet: beispielsweise für einen Bootsektor. Empfehlenswert ist - wie bei jeder anderen Sprache, die im Bereich der Kernelprogrammierung verwendet werden soll - ein Compiler, der Inlineassembler unterstützt. Hierfür eignet sich der [gcc](https://github.com/lowlevel-eu/wiki/wiki/GNU-Compiler-Collection "Gcc").

# Assembly in C

## Inline Assembler

## Funktionen auslagern

Manchmal ist es einfacher und übersichtlicher eine Funktion, oder ein ganzen Teil des Kernels komplett in Assembly zu schreiben, anstatt häufig vom inlie-assembler gebrauch zu machen. Um zwischen einen in Assembly geschriebenen Teil, und einem in C geschriebenen Teil zu interagieren sind folgende Punkte zu beachten:

1.  Name der Funktion
2.  Argumente
3.  Rückgabewert

Der **Funktionsname** wird beim gcc 4 nicht verändert. Nennt man die Funktion in C *test* so heißt diese auch im objectfile *test* Dies kann bei anderen Compilern auch anders sein; Am besten einfach mal in ein objectfile gucken, das mit dem Compiler erstellt wurde, und die Namen, mit den Namen des entsprechenden sourcefiles vergleichen. Wenn man eine Funktion mit dem Namen *test* erstellen möchte, muss man neben dem üblichen lable den Assembler noch anweisen, das dieses lable auch für andere "Dateien" sichtbar sein soll. Dazu verwendet man (unter nasm) das schlüsselwort *global* \<asm\>\[global test\] test:

    ret</asm>

Damit man diese Funktion jetzt von C aus aufrufen kann, muss man in C angeben, dass irgendwo eine Funktion ist, die *test* heißt. Das geht über das Schlüsselwort *extern* \<c\>extern int test(int x);\</c\>

Die **Argumente** Werden in C über den Stack übergeben. Dabei werden die Argumente von rechts nach links auf den Stack gepushed. \<asm\>\[global test\] test:

    mov eax, [esp+4]
    ret</asm>

Unter *\[esp\]* liegt die Rücksprungadresse, unter *\[esp+4\]* liegt das 1. Argument. Das 2. Argument würde unter *\[esp+8\]* liegen, usw.

Der **Rückgabewert** steht in *eax*. Mann sollte also bei der Verwendung von *popad* darauf achten, dass der Rückgabewert nicht verlohren geht. Die Beispeilfunktion *test* würde hier das Argument zurückgeben.

Das asm-file und das C-file müssen nun jeweils zu einem object-file assembliert/compiliert werden, und können dann zusammen geliked werden.

# Links

- [Draft des C Standards](http://www.open-std.org/JTC1/SC22/WG14/www/docs/n1124.pdf)
- [Tutorial](http://www.c-howto.de/)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/3243/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1526/index.html)

<!-- MediaWiki page 1526; revision 3243; parent 2830; 2008-08-26T00:20:07Z -->
