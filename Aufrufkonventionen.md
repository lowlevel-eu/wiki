# Aufrufkonventionen

Unter dem Begriff **Aufrufkonventionen** (engl. *calling convention*) versteht man in der Programmierung die Art und Weise wie Parameter für eine aufzurufende Funktionen übergeben werden und wie der Rückgabewert zurückgegeben wird. Welche Aufrufkonvention verwendet wird, hängt von der Architektur, vom Compiler, den Compileroptionen und eventuell verwendeten Sprachkonstrukten ab.

## cdecl

Cdecl wird von vielen Compilern verwendet die für x86-Systeme kompilieren. Die Parameter werden, beginnend mit den letzten, nacheinander auf den Stack gelegt. Der Rückgabewert einer Funktion wird über das EAX-Register übergeben.

Um zwischen einen in Assembly geschriebenen Teil, und einem in C oder C++ geschriebenen Teil zu interagieren sind folgende Punkte zu beachten:

1.  Name der Funktion
2.  Argumente
3.  Rückgabewert

Der **Funktionsname** wird beim gcc 4 ([C](https://github.com/lowlevel-eu/wiki/wiki/C "C")) nicht verändert. Nennt man die Funktion in C *test*, so heißt diese auch in der Objektdatei *test*. Beim g++ ( [C++](https://github.com/lowlevel-eu/wiki/wiki/C%2B%2B "C++") ) ist das schon etwas komplizierter. Bei C++ kann man Namensräume verwenden, und Funktionen überladen, entsprechend wird der Funktionsname aufwändiger codiert: Als Beispiel folgende Funktion: \<cpp\>namespace namensraum {

    int test(int x)
    {
     return x;
    }

}\</cpp\> In der Objektdatei heißt die Funktion nun *\_ZN10namensraum4testEi*. Aufgelöst bedeutet *N10*, dass ein Namensraum mit 10 Buchstaben folgt (*namensraum*), die *4* gibt an, dass nun der Funktionsname mit 4 Buchstaben folgt (*test*) und nach dem *E* werden die Datentypen der Parameter aufgelistet – hier ein *i* für int.  
Dies kann bei anderen Compilern auch anders sein; am besten einfach mal in eine Objektdatei gucken, die mit dem Compiler erstellt wurde, und die Namen, mit den Namen im entsprechenden Quelltext vergleichen.  
Wenn man eine Funktion mit dem Namen *test* erstellen möchte, muss man neben dem üblichen Label den Assembler noch anweisen, dass dieses Label auch für andere „Dateien“ sichtbar sein soll. Dazu verwendet man (unter nasm) das Schlüsselwort *global*: \<asm\>\[global test\] test:

    ret</asm>

Damit man diese Funktion jetzt von C aus aufrufen kann, muss man in C angeben, dass irgendwo eine Funktion ist, die *test* heißt. Das geht über das Schlüsselwort *extern*: \<c\>extern int test(int x);\</c\>

Die **Argumente** werden in C (x86) über den Stack übergeben. Dabei werden die Argumente von rechts nach links auf den Stack gepusht. \<asm\>\[global test\] test:

    mov eax, [esp+4]
    ret</asm>

Unter *\[esp\]* liegt die Rücksprungadresse, unter *\[esp+4\]* liegt das erste Argument. Das zweite Argument würde unter *\[esp+8\]* liegen, usw..

Der **Rückgabewert** steht in *eax*. Mann sollte also bei der Verwendung von *popad* darauf achten, dass der Rückgabewert nicht verloren geht. Die Beispielfunktion *test* würde hier das Argument zurückgeben.

Die Assemblerdatei und die C-Datei müssen nun jeweils zu einer Objektdatei assembliert/kompiliert werden und können dann zusammen gelinkt werden.

Ein Aufruf einer C-Funktion (oder der Funktion einer anderen Hochsprache) aus Assemblercode geht natürlich auch: \<c\> //int a,b,c,r; int test(int a,int b,int c); //r = test(a,b,c) \</c\> \<asm\>

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

## stdcall

stdcall ist die Standardaufrufkonvention unter 32bit-Windows Systemen. Es gleicht in den meisten Aspekten cdecl, allerdings ist die aufgerufene Funktion dafür zuständig, die Parameter vom Stack zu nehmen, z.B. indem sie für den Rücksprung die Instruktion "ret n" (Wobei n für die Größe der Parameter in Bytes auf dem Stack steht) benutzt.

## Register- oder Fastcall-Konvention

Viele Compiler bieten zusätzlich auch noch eine Register- oder Fastcall-Konvention an, die aber meist Compilerspezifisch ist. Bei dieser werden aus Geschwindigkeitsgründen die ersten zwei oder drei Parameter in die Register EAX, EDX und ECX gespeichert. Die übrigen Parameter werden, beginnend mit dem letzen, auf den Stack gelegt. Der Rückgabewert wird in AL, AX oder EAX übergeben. \<c\> int a,b,c,d,e,r; int test(int a,int b,int c,int d,int e); r = test(a,b,c) \</c\> \<asm\>

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

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/10196/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1525/index.html)

<!-- MediaWiki page 1525; revision 10196; parent 10189; 2011-11-02T10:37:11Z -->
