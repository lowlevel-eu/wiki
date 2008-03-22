# Inline-Assembler mit GCC

Da ich in letzter Zeit immer wieder danach gefragt worden bin, wie das mit Inline-Assembler in gcc denn funktioniere und die Sache durchaus nicht intuitiv (dafür aber recht mächtig) ist, habe ich beschlossen, diese Frage in Zukunft nur noch mit einem Link beantworten zu wollen. Als Vorbereitung entsteht nun also dieser Artikel.

## AT&T-Syntax

Viele Assembler-Programmierer sind die Intel-Syntax gewohnt. gcc (oder genauer gesagt gas, der GNU Assembler) benutzt stattdessen die AT&T-Syntax. Die Hauptmerkmale der AT&T-Syntax sind:

- Register bekommen ein % vorangestellt:

      xor %eax, %eax

- Das Quellregister kommt zuerst, das Zielregister als zweites. Der folgende Befehl kopiert von eax nach ecx (nicht umgekehrt, wie man vermuten könnte, wenn man nur Intel-Syntax kennt!):

      mov %eax, %ecx

- Konstanten bekommen grundsätzlich ein \$ vorangestellt, Hexadezimalzahlen werden durch 0x eingeleitet:

      mov $42, %eax

      mov $0xBADC0FFE, %eax

- Die Operandengrößen sind im Mnemonic enthalten. Wird die Größe nicht angegeben, versucht der Assembler sie anhand der Operanden festzustellen.

      movl $123, %eax

      movw $123, %ax

      movb $123, %al

- Speicherzugriffe erfolgen im Format "segment:displacement(base, index, scale)", wobei das Displacement als auch Index und Scale optional sind:

      pushl (%eax)

      mov %eax, 0x8(%ebp)

      mov 0xfffffff8(%esp,%eax,1),%eax

## Einfache Befehle

Die Einbindung von Inline Assembler in den C-Code ist ganz einfach: Das Schlüsselwort asm (oder alternativ \_\_asm\_\_) in Verbindung mit dem Assemblercode als String muss in den C-Code eingebettet werden:

    asm("int $0x30")

Sollen mehrere Assemblerbefehle ausgeführt werden, gibt es nicht nur eine Möglichkeit, dies zu schreiben: Entweder Trennung durch Strichpunkt (Semikolon) oder durch einen Zeilenumbruch. Strings können dabei wie in C üblich getrennt werden, so daß nicht ein längeres Stück Assemblercode in einer Zeile C untergebracht werden muß:

    asm("cli; hlt");
    asm("cli\nhlt");
    asm(
      "cli;"
      "hlt;"
    );

## Ein- und Ausgabeparameter

gcc unterstützt darüber hinaus noch die Möglichkeit, im Assemblercode Werte zu verarbeiten, die nicht direkt im Assemblerstring stehen, sondern beispielsweise in C-Variablen gespeichert sind. Diese Möglichkeit macht zu einem großen Teil die Mächtigkeit des Inline-Assemblers von gcc aus. Das asm-Konstrukt wird dann folgendermaßen erweitert:

    asm(code : ausgabe : eingabe)

### Übergabe in bestimmten Registern

Wenn die Übergabe von Variablen bzw. Werten in bestimmten Registern stattfinden soll (z.B. für in/out benötigt), können diese Register direkt angegeben werden:

    asm ("inb %1, %0" : "=a" (result) : "d" (port));

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

- Mehrere Buchstaben können aneinandergereiht werden, um mehrere Optionen zu ermöglichen. Die vorderste Option, die funktioniert, wird dann gewählt. Der obenstehende Code für inb ließe sich also folgendermaßen ergänzen:

      asm ("inb %1, %0" : "=a" (result) : "Nd" (port));

  Wird inb darüber inline deklariert, kann der Compiler dann einen Funktionsaufruf wie *inb(0x60)* direkt in eine einzige Assemblerzeile übersetzen und muß kein Register zur Zwischenspeicherung von 0x60 verwenden. Bei einem Aufruf wie *inb(my_port_variable)* würde die traditionelle Variante gewählt und das Register benutzt werden.

## Beispiele

Die folgenden Beispiele sind dem Community-Projekt von Lowlevel, LOST, entnommen und unterliegen dessen Lizenz (4-Klausel-BSD-Lizenz). Diese Lizenz ist beim Kopieren von Code aus den Beispielen einzuhalten.

Aufruf des sleep-Syscalls in LOST:

        asm(
            "mov %0, %%eax;"
            "int $0x30;"
        : : "i" (SYSCALL_PM_SLEEP) : "eax");

Laden der GDT:

    struct {
        word size;
        dword base;
    }  __attribute__((packed)) gdt_ptr = {
        .size  = GDT_SIZE*8 - 1,
        .base  = (dword)gdt,
    };
    asm("lgdtl %0" : : "m" (gdt_ptr));

Senden einer IPC-Nachricht in LOST:

    void send_message(dword pid, dword function, dword correlation_id, dword len, char* data)
    {
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
    }

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/2714/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1472/index.html)

<!-- MediaWiki page 1472; revision 2714; parent 2037; 2008-03-22T16:51:32Z -->
