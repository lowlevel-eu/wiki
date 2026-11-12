# Inline-Assembler mit GCC

In diesem Artikel geht es um Inline-Assembler mit dem GCC bzw. G++. Inline-Assembler ist nicht nur dafür da, Dinge zu implementieren, wenn dies in C oder einer anderen Hochsprache nicht möglich ist, sondern ist zugleich eines der mächtigsten Werkzeuge des Betriebssystementwicklers.

## AT&T-Syntax

Viele Assembler-Programmierer sind die Intel-Syntax gewohnt. gcc (oder genauer gesagt gas, der GNU Assembler) benutzt stattdessen die AT&T-Syntax. Die Hauptmerkmale der AT&T-Syntax sind:

- Register bekommen ein % vorangestellt: \<asm\>xor %eax, %eax\</asm\>
- Das Quellregister kommt zuerst, das Zielregister als zweites. Der folgende Befehl kopiert von eax nach ecx (nicht umgekehrt, wie man vermuten könnte, wenn man nur Intel-Syntax kennt!): \<asm\>mov %eax, %ecx\</asm\>
- Konstanten bekommen grundsätzlich ein \$ vorangestellt, Hexadezimalzahlen werden durch 0x eingeleitet: \<asm\>mov \$42, %eax\</asm\>\<asm\>mov \$0xBADC0FFE, %eax\</asm\>
- Die Operandengrößen sind im Mnemonic enthalten. Wird die Größe nicht angegeben, versucht der Assembler sie anhand der Operanden festzustellen. \<asm\>movl \$123, %eax\</asm\>\<asm\>movw \$123, %ax\</asm\>\<asm\>movb \$123, %al\</asm\>
- Speicherzugriffe erfolgen im Format "segment:displacement(base, index, scale)", wobei das Displacement als auch Index und Scale optional sind: \<asm\>pushl (%eax)\</asm\>\<asm\>mov %eax, 0x8(%ebp)\</asm\>\<asm\>mov 0xfffffff8(%esp,%eax,1),%eax\</asm\>

Wer sich überhaupt nicht mit der AT&T-Syntax anfreunden kann, für den bleibt immer noch die gcc-Kommandozeilenoption "-masm=intel", die die Intelsyntax aktiviert.

## Einfache Befehle

Die Einbindung von Inline Assembler in den C-Code ist ganz einfach: Das Schlüsselwort asm (oder alternativ \_\_asm\_\_) in Verbindung mit dem Assemblercode als String muss in den C-Code eingebettet werden: \<c\>asm("int \$0x30")\</c\>

Sollen mehrere Assemblerbefehle ausgeführt werden, gibt es nicht nur eine Möglichkeit, dies zu schreiben: Entweder Trennung durch Strichpunkt (Semikolon) oder durch einen Zeilenumbruch. Strings können dabei wie in C üblich getrennt werden, so dass nicht ein längeres Stück Assemblercode in einer Zeile C untergebracht werden muss: \<c\>asm("cli; hlt"); asm("cli\nhlt"); asm(

     "cli;"
     "hlt;"

);\</c\>

## Ein- und Ausgabeparameter

gcc unterstützt darüber hinaus noch die Möglichkeit, im Assemblercode Werte zu verarbeiten, die nicht direkt im Assemblerstring stehen, sondern beispielsweise in C-Variablen gespeichert sind. Diese Möglichkeit macht zu einem großen Teil die Mächtigkeit des Inline-Assemblers von gcc aus. Das asm-Konstrukt wird dann folgendermaßen erweitert: \<c\> asm(code : ausgabe : eingabe) \</c\>

### Übergabe in bestimmten Registern

Wenn die Übergabe von Variablen bzw. Werten in bestimmten Registern stattfinden soll (z.B. für in/out benötigt), können diese Register direkt angegeben werden: \<c\>asm ("inb %1, %0" : "=a" (result) : "d" (port));\</c\>

- Die Ausgabe bzw. Eingabe wird durch *"register" (wert)* spezifiziert. *result* und *port* wären im Beispiel zwei C-Variablen.
- Mehrere Ausgabe- bzw. Eingabevariablen werden durch Komma getrennt
- Register werden in der Ausgabe- und Eingabeliste folgendermaßen bezeichnet: a, b, c, d stehen für eax, ebx, ecx, edx (bzw. die entsprechenden Word- und Byte-Varianten, je nach Größe der übergebenen Variablen), D für edi und S für esi
- Die Spezifikation der Ausgabewerte beginnt mit =
- Zugriff innerhalb des Assemblercodes erfolgt über %0, %1, ... in der Reihenfolge der Nennung.
- Register werden in der Form %%eax adressiert, wenn Ausgabe-/Eingabeparameter verwendet werden

### Allgemeine Übergabe

Außerdem bietet gcc noch Möglichkeiten, die Übergabe nur grob zu spezifizieren und die konkrete Entscheidung dem Compiler zu überlassen:

- "m" steht für Speicherübergabe, %0 ist dann die Adresse, an der der Wert zu finden ist
- "r" steht für Registerübergabe, das konkrete Register wird aber dem Compiler zur Wahl überlassen
- "g" steht für "general". Der Compiler hat die freie Wahl, wie er den Befehl umsetzen will. Er wird dabei nicht immer eine funktionierende Variante wählen, deswegen ist es oft notwendig, direkt "r" oder "m" anzugeben.
- "i" steht für einen Immediate-Wert, "N" steht für einen Immediate-Wert in Bytegröße. Dies funktioniert nur, wenn der Wert konstant und bereits beim Kompilieren bekannt ist.
- Mehrere Buchstaben können aneinandergereiht werden, um mehrere Optionen zu ermöglichen. Die vorderste Option, die funktioniert, wird dann gewählt. Der obenstehende Code für inb ließe sich also folgendermaßen ergänzen: \<c\>asm ("inb %1, %0" : "=a" (result) : "Nd" (port));\</c\> Wird inb darüber inline deklariert, kann der Compiler dann einen Funktionsaufruf wie *inb(0x60)* direkt in eine einzige Assemblerzeile übersetzen und muß kein Register zur Zwischenspeicherung von 0x60 verwenden. Bei einem Aufruf wie *inb(my_port_variable)* würde die traditionelle Variante gewählt und das Register benutzt werden.

## Beispiele

Die folgenden Beispiele sind dem Community-Projekt von Lowlevel, [LOST](Kategorie-T%C3%BDndur "Kategorie:Týndur"), entnommen und unterliegen dessen Lizenz (4-Klausel-BSD-Lizenz). Diese Lizenz ist beim Kopieren von Code aus den Beispielen einzuhalten.

Aufruf des sleep-Syscalls in LOST: \<c\>

       asm(
           "mov %0, %%eax;"
           "int $0x30;"
       : : "i" (SYSCALL_PM_SLEEP) : "eax");

\</c\>

Laden der GDT: \<c\> struct {

       word size;
       dword base;

} \_\_attribute\_\_((packed)) gdt_ptr = {

       .size  = GDT_SIZE*8 - 1,
       .base  = (dword)gdt,

}; asm("lgdtl %0" : : "m" (gdt_ptr)); \</c\>

Senden einer IPC-Nachricht in LOST: \<c\> void send_message(dword pid, dword function, dword correlation_id, dword len, char\* data) {

       asm(
           "movl %4, %%eax;"
           "add %5, %%eax;"
           "movl %5, %%ecx;"
           ".1: sub $4, %%eax;"
           "pushl (%%eax);"
           "sub $4, %%ecx;"
           "jg .1;"
           "pushl %3;"
           "pushl %2;"
           "pushl %1;"
           "pushl %0;"
           "mov $51, %%eax;"
           "int $0x30;"
           "add $0x10, %%esp;"
           "add %5, %%esp;"
       : : "g" (pid), "g" (len+8), "g"(function), "g" (correlation_id), "g" (data) , "g" (len) : "eax", "ecx");

} \</c\>

  

## Weblinks

[gcc-Manual: Constraints](http://gcc.gnu.org/onlinedocs/gcc-4.3.0/gcc/Constraints.html)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/8892/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1472/index.html)

<!-- MediaWiki page 1472; revision 8892; parent 7916; 2010-11-13T23:40:34Z -->
