# Aufrufkonventionen

Unter dem Begriff **Aufrufkonventionen** versteht man in der Programmierung die Art und Weise wie Parameter für eine aufzurufende Funktionen übergeben werden und wie der Rückgabewert zurückgegeben wird. Welche Aufrufkonvention verwendet wird, hängt von der Architektur, vom Compiler, den Compileroptionen und eventuell verwendeten Sprachkonstrukten ab.

## cdecl

Cdecl wird von vielen Compilern verwendet die für x86-Systeme kompilieren. Die Parameter werden, beginnend mit den letzten, nacheinander auf den Stack gelegt. Der Rückgabewert einer Funktion wird über das EAX-Register übergeben.

Um zwischen einen in Assembly geschriebenen Teil, und einem in C oder C++ geschriebenen Teil zu interagieren sind folgende Punkte zu beachten:

1.  Name der Funktion
2.  Argumente
3.  Rückgabewert

Der **Funktionsname** wird beim gcc 4 ( [C](https://github.com/lowlevel-eu/wiki/wiki/C "C") ) nicht verändert. Nennt man die Funktion in C *test* so heißt diese auch im objectfile *test*.\\ Beim g++ ( [C++](https://github.com/lowlevel-eu/wiki/wiki/C%2B%2B "C++") ) ist das schon etwas komplizierter. Bei C++ kann man namensräume verwenden, und Funktionen überladen, entsprechend wird der Funktionsname aufwändiger codiert:\\ Als Beispiel folgende Funktion: \<cpp\>namespace namensraum {

    int test(int x)
    {
     return x;
    }

}\</cpp\> Im Objectfile heißt die Funktion nun *\_ZN10namensraum4testEi*  
Aufgelöst bedeutet *N10* Das ein Namensraum mit 10 Buchstaben folgt (*namensraum*)  
Die *4* gibt an, das nun der funktionsname mit 4 Buchstaben folgt (*test*)  
Und nach dem *E* werden die datentypen der parameter aufgelistet - hier ein *i* für int  
Dies kann bei anderen Compilern auch anders sein; Am besten einfach mal in ein objectfile gucken, das mit dem Compiler erstellt wurde, und die Namen, mit den Namen des entsprechenden sourcefiles vergleichen. Wenn man eine Funktion mit dem Namen *test* erstellen möchte, muss man neben dem üblichen lable den Assembler noch anweisen, das dieses lable auch für andere "Dateien" sichtbar sein soll. Dazu verwendet man (unter nasm) das schlüsselwort *global* \<asm\>\[global test\] test:

    ret</asm>

Damit man diese Funktion jetzt von C aus aufrufen kann, muss man in C angeben, dass irgendwo eine Funktion ist, die *test* heißt. Das geht über das Schlüsselwort *extern* \<c\>extern int test(int x);\</c\>

Die **Argumente** Werden in C über den Stack übergeben. Dabei werden die Argumente von rechts nach links auf den Stack gepushed. \<asm\>\[global test\] test:

    mov eax, [esp+4]
    ret</asm>

Unter *\[esp\]* liegt die Rücksprungadresse, unter *\[esp+4\]* liegt das 1. Argument. Das 2. Argument würde unter *\[esp+8\]* liegen, usw.

Der **Rückgabewert** steht in *eax*. Mann sollte also bei der Verwendung von *popad* darauf achten, dass der Rückgabewert nicht verlohren geht. Die Beispeilfunktion *test* würde hier das Argument zurückgeben.

Das asm-file und das C-file müssen nun jeweils zu einem object-file assembliert/compiliert werden, und können dann zusammen geliked werden.

Ein Aufruf einer C-Funktion (oder der Funktion einer anderen Hochsprache) aus einem Assembley-code geht natürlich auch: \<c\> //int a,b,c,r; int test(int a,int b,int c); //r = test(a,b,c) \</c\> \<asm\>

     ; Parameter werden auf den Stack gelegt
     push c
     push b
     push a
     ; Funktion wird aufgerufen
     call test
     ; Stackpointer wird zurückgesetzt
     add esp,3*4
     ; Rückgabewert wird in r gespeichert
     mov r,eax

\</asm\>

## Pascal

Die Pascal-Aufrufkonvention gibt vor, dass die Parameter, beginnend mit dem ersten, auf den Stack gelegt werden. Außerdem muss die aufgerufene Funktion den Stackpointer zurücksetzen.

## Register- oder Fastcall-Konvention

Bei der Register- oder Fastcall-Konvention werden aus Geschwindigkeitsgründen die ersten zwei oder drei Parameter in die Register EAX, EDX und ECX gespeichert. Die übrigen Parameter werden, beginnend mit dem letzen, auf den Stack gelegt. Der Rückgabewert wird in AL, AX oder EAX übergeben. \<c\> int a,b,c,d,e,r; int test(int a,int b,int c,int d,int e); r = test(a,b,c) \</c\> \<asm\>

Die ersten drei Parameter werden über Register übergeben

mov eax,a mov edx,b mov ecx,c

Die letzen 2 Parameter werden über den Stack übergeben

push e push d

Funktion wird aufgerufen

call test

Stackpointer wird zurückgesetzt

add esp,2\*4

Rückgabewert wird in r gespeichert

mov r,eax \</asm\>

## Links

- [x86-64 ABI (Application Binary Interface)](http://www.x86-64.org/documentation.html)
- [System V ABI für i386](https://x-os.homeip.net/x-os/hdir/pdf/sysv/psABI-i386.pdf)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/5818/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1525/index.html)

<!-- MediaWiki page 1525; revision 5818; parent 4059; 2009-08-31T18:44:23Z -->
