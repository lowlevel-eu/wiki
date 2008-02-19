# Aufrufkonventionen

Unter dem Begriff "Aufrufkonventionen" versteht man die Art und Weise wie Parameter für eine aufzurufende Funktionen übergeben werden. Welche Aufrufkonvention verwendet wird, hängt vom Compiler ab.

## cdecl

Cdecl wird von vielen Compilern verwendet die für x86-Systeme kompilieren. Die Parameter werden, beginnend mit den letzten, nacheinander auf den Stack gelegt. Der Rückgabewert einer Funktion wird über das EAX-Register übergeben. \<c\> int a,b,c,r; int test(int a,int b,int c); r = test(a,b,c) \</c\> \<asm\>

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

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/2593/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1525/index.html)

<!-- MediaWiki page 1525; revision 2593; parent 2588; 2008-02-19T17:40:46Z -->
