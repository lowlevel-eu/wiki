# Teil 2 - Assembler 101

|  |  |  |
| ----------------------------------------------------------------------------------------------------------------------------------------- | ---------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| « [Teil 1 - Entwicklungsumgebung](Teil-1-Entwicklungsumgebung "Teil 1 - Entwicklungsumgebung") | **Navigation** | [Teil 3 - Trockenübungen](Teil-3-Trocken%C3%BCbungen "Teil 3 - Trockenübungen") » |

## Ziel

Dieser Artikel versucht, in aller Kürze zumindest die Grundlagen der Assemblerprogrammierung für [x86](X86 "X86") zu vermitteln. Ganz ohne Assembler kommt man bei der Betriebssystemprogrammierung nicht aus, deswegen ist ein Grundverständnis dafür nötig.

An dieser Stelle sei angemerkt, dass es mehrere verschiedene Assembler-Varianten gibt. Wir verwenden hier die AT&T-Syntax, die vom GNU-Assembler unterstützt wird.

## Begriffe

- Eine *Instruktion* ist ein kompletter Prozessorbefehl, z.B. addiere 5 auf den Inhalt des Registers eax (*add \$5, %eax*). Mit Instruktion kann sowohl die Assemblerdarstellung als auch der Opcode gemeint sein.
- Der *Opcode* ist der binäre Maschinenbefehl, wie er vom Prozessor verstanden wird. Er wird meistens hexadezimal und byteweise geschrieben: *05 05 00 00 00* für unser Beispiel. Oft wird unter Opcode auch nur der eigentliche Befehl (*05* für add ..., %eax) verstanden.
- Der *Operand* sind die Daten, auf denen der Maschinenbefehl arbeitet. Das ist zum einen die Zahl 5 und zum anderen das Register eax.
- Das *Mnemonic* ist der Assemblername eines Befehls, z.B. *add*

## Operanden

Als Operanden für Assemblerbefehle kommen nur drei verschiedene Arten in Frage:

- *Immediatewerte* sind konstante Zahlen. Sie beginnen in Assembler mit *\$*, wie im obigen Beispiel das *\$5*.
- *Prozessorregister* sind der Platz, wo Daten, mit denen gearbeitet wird, normalerweise liegen. x86 hat acht Allzweckregister, die jeweils 32 Bit groß sind. Die Register befinden sich direkt im Prozessor, so dass sie viel schneller sind als Zugriffe auf Arbeitsspeicher. Registernamen beginnen mit *%*, wie im obigen Beispiel das *%eax*.
- Der *Speicher* ist schließlich, wo die meisten Daten liegen. Auf Speicher wird grundsätzlich über Adressen zugegriffen. Dabei gibt es folgende Möglichkeiten:
  - Direkte Angabe der Adresse: *mov 5, %eax* ohne \$ kopiert den Wert von der Speicheradresse 5 ins Register eax
  - Indirekte Angabe über Register: *mov (%ebx), %eax* liest die Adresse aus dem Register ebx und kopiert dann von dieser Adresse nach eax
  - Indirekte Angabe mit Displacement: *mov 8(%ebx), %eax* liest wieder die Adresse aus ebx, zählt aber noch 8 dazu, bevor es die Adresse verwendet
  - Es geht noch mehr: *mov 8(%ebx, %edx, 2)* berechnet die Adresse als *ebx + 2 \* edx + 8*

## Labels

Oft bezieht sich ein Operand auf eine andere Stelle im Assemblercode, z.B. ein Sprung an eine andere Codestelle oder Auslesen von Daten. In diesem Fall möchte sich natürlich niemand die Mühe machen, von Hand auszurechnen, an welcher Adresse diese Stelle steht. Aus diesem Grund kann man überall sogenannte Labels definieren, Sprungmarken mit einem selbstgewählten Namen. Bei der Definition kommt hinter dem Namen ein Doppelpunkt: *my_label:*

Der Name des Labels kann dann für Operatoren anstatt von Zahlen verwendet werden. Wenn die Adresse benutzt werden soll, nicht vergessen, auch hier wieder ein \$ vor den Namen des Labels zu schreiben. Ansonsten wird auf die Daten direkt nach dem Label zugegriffen.

Wenn das Label auch außerhalb der Datei sichtbar sein soll, muss zusätzlich *.global my_label* angegeben werden. Es ist auch möglich, auf Labels zuzugreifen, die in anderen Dateien definiert sind, sie müssen dann mit *.extern my_label* eingebunden werden. Diese Möglichkeit besteht nur, wenn ein Binärformat wie z.B. ELF benutzt wird und die vom Assembler erzeugten Objektdateien anschließend noch miteinander gelinkt werden.

## Daten

Im Assemblercode können auch Daten definiert werden, auf die zugegriffen werden kann. Man muss dabei nur darauf achten, dass die Daten nicht mitten im Code stehen, sonst wird der Prozessor versuchen, die Daten als Befehle zu interpretieren.

| Befehl | Erklärung |
| -------------------------- | ------------------------ |
| .byte 0xff | 8-Bit-Daten |
| .word 0xffff | 16-Bit-Daten |
| .int 0xffffffff | 32-Bit-Daten |
| .quad 0xffffffffffffffff | 64-Bit-Daten |
| .space 256 | 256 Bytes freier Platz |

## Sektionen

Bei der Benutzung von Binärformaten wie ELF kann der Assemblercode in verschiedene Sektionen unterteilt werden. Mit *.section name* wird festgelegt, in welcher Sektion der folgende Code landen soll. Dabei kann auch zwischen Sektionen hin- und hergewechselt werden. Die Standardsektionen sind:

| Befehl | Erklärung |
| ------------------ | ------------------------------------------------------------------------------------- |
| .section .text | Ausführbare Befehle |
| .section .data | Veränderbare Daten |
| .section .rodata | Nur lesbare Daten |
| .section .bss | Veränderbare Daten mit beim Start undefiniertem Wert (Platz mit .space reservieren) |

## Kommentare

Kommentare funktionieren wie in C:

    // Einzeiliger Kommentar

    /*
     * Mehrzeiliger Kommentar
     */

## Register

Wie oben erwähnt, besitzt x86 acht 32-Bit-Allzweckregister: eax, ebx, ecx, edx, ebp, esp, esi, edi. Obwohl sie als Allzweckregister bezeichnet werden, gibt es Befehle, die nur mit einem bestimmten Register funktionieren. Bei allen diesen Registern ist es auch möglich, nur auf die niederwertigen 16 Bit zuzugreifen. Dabei fällt das e im Namen weg: ax sind die unteren 16 Bit von eax. ax, bx, cx und dx unterteilen sich wiederum in ein höherwertiges und ein niederwertiges Byte, genannt z.B. ah und al.

Außerdem existieren noch Segmentregister, Steuerregister, FPU-Register und mehr, aber diese haben eine spezielle Funktion und sollen hier außen vor bleiben.

## Befehlssatz

An dieser Stelle ein kurzer Abriss über die von x86 unterstützten Befehle. Ich werde dabei im Allgemeinen nicht angeben, welche Kombinationen von Operanden alles erlaubt sind. Eine allgemeine Sache, die gilt, ist dass in einer Instruktion immer maximal ein Operand aus dem Speicher kommen darf. Eine andere ist, dass man mit Registern außer den Allzweckregistern nichts anderes machen kann als sie aus einem Allzweckregister zu laden oder ihren Inhalt in ein Allzweckregister zu kopieren.

### Zuweisungen und Stack

| Befehl | Erklärung |
| ---------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| mov *Quelle, Ziel* | Kopiert den Wert von Quelle nach Ziel |
| lea *Speicher, Ziel* | Lädt die Adresse des Speichers nach Ziel (*lea (%eax), %edx* ist dasselbe wie *mov %eax, %edx*) |
| push *Operand* | Legt den Wert auf den Stack; d.h. esp wird um die Größe des Operanden verringert und der Operand an die neue Speicheradresse von esp kopiert. |
| pop *Operand* | Holt den Wert vom Stack; d.h. der Wert an der Adresse von esp wird zum Operanden kopiert und esp um die Größe des Operanden erhöht. |

### Arithmetik

| Befehl | Erklärung |
| --------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| inc *Operand* | Erhöht den Operanden um eins |
| dec *Operand* | Verringert den Operanden um eins |
| add *Quelle, Ziel* | Addiert den Wert von Quelle auf Ziel (der alte Wert von Ziel wird dabei überschrieben; dies gilt auch für alle folgenden Befehle) |
| sub *Quelle, Ziel* | Subtrahiert den Wert von Quelle von Ziel |
| imul *Quelle, Ziel* | Multipliziert Quelle mit Ziel und speichert das Ergebnis in Ziel |
| mul *Quelle* | Multipliziert Quelle (wenn es ein 32-Bit-Register ist) mit eax und speichert das Ergebnis in edx:eax (d.h. die niederwertigen 32 Bit des Ergebnisses stehen in eax, die höherwertigen in edx) |
| div *Quelle* | Dividiert edx:eax durch Quelle (wenn es ein 32-Bit-Register ist) und speichert das ganzzahlige Ergebnis in eax. Der Rest wird in edx gespeichert. |
| neg *Operand* | Überschreibt den Operaden mit seinem negativen Wert (5 wird zu -5) |

### Bitoperationen

| Befehl | Erklärung |
| ----------------------- | -------------------------------------------------------------------------------------------------------------------- |
| and *Quelle, Ziel* | Berechnet das bitweise AND von Quelle und Ziel |
| or *Quelle, Ziel* | Berechnet das bitweise OR von Quelle und Ziel |
| xor *Quelle, Ziel* | Berechnet das bitweise XOR (exklusives Oder) von Quelle und Ziel |
| not *Operand* | Berechnet das bitweise NOT vom Operanden |
| shl *Anzahl, Operand* | Schiebt den Wert des Operanden um Anzahl Bits nach links. Rechts wird mit Nullen aufgefüllt. |
| shr *Anzahl, Operand* | Schiebt den Wert des Operanden um Anzahl Bits nach rechts. Links wird mit Nullen aufgefüllt. |
| rol *Anzahl, Operand* | Rotiert den Wert des Operanden um Anzahl Bits nach links. Was links rausgeschoben wird, kommt rechts wieder rein. |
| ror *Anzahl, Operand* | Rotiert den Wert des Operanden um Anzahl Bits nach rechts. Was rechts rausgeschoben wird, kommt links wieder rein. |

### Vergleiche und Sprünge

Um den Programmfluss zu steuern, gibt es in Assembler zwei Arten von Sprüngen. Die erste Art sind unbedingte Sprünge, sie entsprechen am ehesten einem *goto* in einer Hochsprache. Die zweite Art sind bedingte Sprünge, die benutzt werden, um ein *if* umzusetzen. Bedingte Sprünge führen den Sprung nur aus, wenn eine bestimmte Bedingung erfüllt ist. Die Bedingungen bestehen in einigen Bits im Register eflags, die von vielen Befehlen automatisch gesetzt werden. Diese Bits sind:

- Das Zero Flag: Ist gesetzt, wenn der letzte geschriebene Wert Null war
- Das Carry Flag: Enthält den Übertrag bei vorzeichenlosen Operationen, wenn das Ergebnis zu groß ist, um vom Zieloperanden dargestellt werden zu können
- Das Overflow Flag: Enthält den Übertrag bei vorzeichenbehafteten Operationen, wenn das Ergebnis zu groß oder zu klein ist, um vom Zieloperanden dargestellt werden zu können
- Das Sign Flag: Ist gesetzt, wenn des letzte Ergebnis negativ war

| Befehl | Erklärung |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| cmp *Quelle, Ziel* | Subtrahiert Quell von Ziel, ohne das Ergebnis zu speichern. Es werden nur die Flags angepasst. |
| test *Quelle, Ziel* | Berechnet das bitweise AND von Quelle und Ziel, ohne das Ergebnis zu speichern. Es werden nur die Flags angepasst. |
| jmp *Sprungziel* | Springt zum Sprungziel (unbedingt) |
| jz *Sprungziel* | Springt zum Sprungziel, wenn das Zero Flag gesetzt ist (alternativ *je* für *equal* - da cmp subtrahiert, ist ZF gesetzt, wenn die Operanden gleich waren) |
| jnz *Sprungziel* | Springt zum Sprungziel, wenn das Zero Flag nicht gesetzt ist (alternativ *jne*) |
| jg *Sprungziel* | Springt zum Sprungziel, wenn beim cmp Quelle \> Ziel war |
| jl *Sprungziel* | Springt zum Sprungziel, wenn beim cmp Quelle \< Ziel war |
| jge *Sprungziel* | Springt zum Sprungziel, wenn beim cmp Quelle \>= Ziel war |
| jle *Sprungziel* | Springt zum Sprungziel, wenn beim cmp Quelle \<= Ziel war |
| call *Sprungziel* | Legt die Adresse des nächsten Befehls auf den Stack und springt zum Sprungziel (Funktionsaufruf) |
| ret | Holt die Rücksprungadresse vom Stack und springt dorthin (Rücksprung aus einer Funktion) |

## Oft gebrauchte Muster

### Bitoperationen

    xor %eax, %eax

Setzt eax auf Null. Wird häufig verwendet, weil der Maschinencode dafür kürzer ist als der für *mov \$0, %eax*.

    or %eax, %eax

Setzt die Flags für eax, ohne es zu ändern. Wird zum Beispiel für Nullprüfungen verwendet, mit anschließendem jz.

### Funktionen

    my_func:
        push %ebp
        mov %esp, %ebp
        ...
        mov %ebp, %esp
        pop %ebp
        ret

ebp wird hier als Frame Pointer verwendet. Wenn jede Funktion die C-Aufrufkonvention benutzt (die dieses Schema beinhaltet), sieht der Stack einer Funktion damit folgendermaßen aus:

| Adresse | Inhalt |
| ---------- | ---------------------------------------- |
| ... |  |
| -4(%ebp) | Lokale Variable |
| (%ebp) | Frame Pointer der aufrufenden Funktion |
| 4(%ebp) | Rücksprungadresse |
| 8(%ebp) | Erster Parameter der Funktion |
| ... |  |

Dadurch, dass auch ein Verweis auf den Frame Pointer der aufrufenden Funktion vorhanden ist, lassen sich leicht Stack Backtraces für das Debugging produzieren.

## Beispiel

Das folgende Programm, bestehend aus einem Assembler- und einem C-Teil berechnet die Fakultät einer Zahl:

``` asm
.section .text
.global factorial
factorial:
    push %ebp
    mov %esp, %ebp

    // Den Parameter nach eax laden
    mov 8(%ebp), %eax

    // Die Fakultät von 0 ist 1 (Rückgabewert kommt nach eax)
    or %eax, %eax
    jnz recurse
    mov $1, %eax
    jmp out

recurse:
    // Ansonsten rekursiv factorial für eax - 1 aufrufen und hinterher
    // mit unserem eax multiplizieren
    dec %eax
    push %eax
    call factorial
    add $4, %esp

    // eax enthält jetzt den Rückgabewert, also unseren Parameter nochmal
    // neu von unserem Stack laden
    mov 8(%ebp), %edx

    // Multiplizieren und das Ergebnis in eax (als Rückgabewert) speichern
    imul %edx, %eax

out:
    mov %ebp, %esp
    pop %ebp
    ret
```

``` c
#include <stdio.h>

extern int factorial(int n);

int main(void)
{
    int n = 5;
    printf("Die Fakultät von %d ist %d\n", n, factorial(n));
    return 0;
}
```

Kompiliert wird das ganze (abhängig von den Dateinamen natürlich) wie folgt (-m32 ist auf 64-Bit-Systemen wichtig - wir haben hier 32-Bit-Code geschrieben):

    gcc -m32 -o factorial main.c fact.S

**Hinweis:**

Bei gcc sollte die Assemblerdatei unbedingt die Endung .S (mit großem S) haben. Bei einem kleinen .s erkennt der Assembler die Datei sonst als bereits vom Präprozessor bearbeitet und würde diesen dann nicht mehr aufrufen. C-Kommentare, \#define, andere Präprozessordirektiven und manche Befehle sind dann nicht mehr nutzbar!

## Weblinks

[Intels Prozessordokumentation](http://www.intel.com/products/processor/manuals/)

  

|  |  |  |
| ----------------------------------------------------------------------------------------------------------------------------------------- | ---------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| « [Teil 1 - Entwicklungsumgebung](Teil-1-Entwicklungsumgebung "Teil 1 - Entwicklungsumgebung") | **Navigation** | [Teil 3 - Trockenübungen](Teil-3-Trocken%C3%BCbungen "Teil 3 - Trockenübungen") » |

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/11390/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1918/index.html)

<!-- MediaWiki page 1918; revision 11390; parent 8676; 2018-09-04T09:58:23Z -->
