# Erste Hilfe

Dieser Artikel richtet sich an verschiedene Personengruppen:

**Anfänger**: Du hast es gerade geschafft deinen Kernel zu laden und möchtest einfach nur Text auf dem Bildschirm ausgeben. Der Code scheint einwandfrei, der Kernel wird auch geladen und… – der Emulator stürzt ab. Wahrscheinlich ist dir nur irgendwo ein kleiner Fehler unterlaufen, den schon tausende vor dir gemacht haben. Deswegen quäl dich nicht und lies einfach diesen Artikel, am besten behälst du die kleinen Tücken der Betriebssystem-Entwicklung, die hier aufgeführt werden, immer im Hinterkopf. Dann sparst du dir viel Zeit und Ärger.

**Frustrierte**: Schon seit einer Woche hängst du an der einen Codestelle und findest den Fehler einfach nicht? Du möchtest dein Betriebssystemprojekt am liebsten aufgeben und nur dein Ehrgeiz hält dich davon ab? Bestimmt ist es nur ein kleiner Fehler, den du immer wieder überliest. Schau einfach mal in diesem Artikel, ob du nicht vielleicht hier die Rettung findest.

**Doktoren** Du bist häufig im Forum unterwegs und hilfst gerne? Und da ist dieser eine Fehler, den alle immer wieder machen. Damit du ihn nicht tausendmal wieder korrigieren musst, schreib ihn einfach in diesen Artikel.

## Allgemeine Fehler

### „Ich habe die fehlerhafte Stelle genau gefunden“

NEIN! Es kann sein, dass die Stelle fehlerhaft ist, sie muss es aber nicht sein. Dafür ist die Betriebssystementwicklung einfach viel zu komplex. Vielmehr kann die Codestelle nur der Auslöser für einen Fehler sein, der sich schon viel früher eingeschlichen hat. Beispielsweise kann ein Fehler bei einem bestimmten Funktionsaufruf auftreten, aber nicht, weil die Funktion fehlerhaft ist, sondern weil der Stack zu groß wird.

### Schon im Bootloader

Viele schreiben ihren Bootloader zwar nicht selbst, aber die Unerschrockenen, die es tun, begeben sich gleich am Anfang in Gefahr: \<asm\> \[org 0x7c00\]

mov si, msg call write jmp \$ \</asm\> Feiner Code, aber wer weiß, welche Registerzustände das BIOS uns überlässt. Wenn es zum Beispiel einen Farjump nach 0x0000:0x7C00 macht, dann ist alles in Ordnung. Ist es aber einer nach 0x07C0:0x0000, dann ist bei „call write“ Schluss, weil die Org-Directive erwartet, dass in IP ein 0x7C00 steht. Außerdem wissen wir auch nicht, wohin das BIOS den Stack gesetzt hat, also sollte man den auch noch verschieben. Deswegen hat am Anfang jedes Bootloaders folgender (oder ähnlicher) Code zu stehen: \<asm\> %define STACK_SEGMENT 0x1000 %define STACK_OFFSET 0xFFFF

\[org 0x7c00\] cli xor ax, ax ; null segments mov ds, ax mov es, ax mov ax, STACK_SEGMENT mov ss, ax mov sp, STACK_OFFSET jmp 0x00:refresh refresh: sti

mov si, msg call write jmp \$ \</asm\> So gibt es keine Komplikationen. (Die obige Adresse des Stacks ist natürlich nur beispielhaft)

### Der Stack

Kommen wir jetzt zum einem der größten Biester in der Betriebssystemsentwicklung: dem Stack. Das erste, was viele vergessen, ist, dass der Stack nach **unten** hin wächst. Ein *push* vermindert also den Stackpointer! Und der Stack hat die unangenehme Eigenschaft, alles zu überschreiben, was sich ihm in den Weg stellt, also auch Code und Daten. Deswegen ist folgender Code zum Scheitern verurteilt: \<asm\>

1.  define GDT_BASE 0x20000
2.  define STACK_TOP 0x20100

gdt mit 30 Einträgen anlegen

...

...

mov esp, STACK_TOP xor eax, eax mov ss, ax

call ClearScreen

...

\</asm\>

Und irgendwo in *ClearScreen* schmiert dann der Code ab, weil der Stack eben nach **unten** wächst und die GDT überschreibt. Also immer vorsichtig sein mit dem Stack, insbesondere wenn man irgendwann für jeden Prozess einen eigenen hat.

## Hardware

### Defekter Sektor

Es kann auch durchaus vorkommen das ein Sektor der Diskette, die zu zum Testen verwendest, defekt ist. Dieser Fehler ist besonders dann schwer zu finden, wenn man sein System primär auf realer Hardware testet.

## C-bezogene Fehler

### volatile

Der Compiler hat die angenehme Eigenschaft den Code um sinnlose Passagen zu erleichtern. Aber manchmal ist das eben nicht hilfreich, vor allem wenn man inline-Assembler verwendet, wird dieser oft wegoptimiert. Dagegen hilft das *volatile* Schlüsselwort. Es fordert den Compiler dazu auf, den entsprechenden Code nicht zu optimieren: \<c\> asm volatile("mov %0, %%eax;" : : "a" (value) ); \</c\> Aber volatile kann noch mehr. Folgender Code könnte nicht funktionieren: \<c\> bool key_pressed=false; //wird vom IRQ-handler gesetzt

void wait_keypress() {

     while(!key_pressed);

} \</c\> Aus der Schleife könnte der Compiler eine Endlosschleife machen, da er der Meinung ist, dass sich key_pressed in der Schleife nicht ändern kann. Aber *volatile* löst das Problem: \<c\> volatile bool key_pressed=false; //wird vom IRQ-handler gesetzt

void wait_keypress() {

     while(!key_pressed);

} \</c\> Num wird bei jedem Schleifendurchlauf der Wert von key_pressed neu geladen und getestet.

### \_\_attribute\_\_((packed))

Und wieder macht uns der Compiler ein schönes Codekonstrukt kaputt, weil er structs „optimiert“. Folgender Code erstellt einen IDT-Eintrag: \<c\> VOID idt_set_entry(uint8_t n, uint16_t sel, void\* handler, uint8_t flags) {

      idt_entry[n].resreved = 0;
      idt_entry[n].flags   = flags;
      idt_entry[n].sel     = sel;
      idt_entry[n].baseLo  = (uintptr_t)(handler) & 0x0000FFFF;
      idt_entry[n].baseHi  = (uintptr_t)(handler) >> 16;
      return;

} \</c\> Diese (fehlerfreie) Funktion greift dabei auf ein Array aus folgendem struct zu:

\<c\> struct idt_entry {

       uint16_t baseLo;
       uint16_t sel;
       uint8_t always0; //reserved
       uint8_t flags;
       uint16_t baseHi;

}; \</c\> Und genau an dieser Stelle produziert der Compiler mit seiner Optimierung einen Fehler und die CPU wird sich mit einem freundlichen Triple-Fault verabschieden. Denn der Compiler hat die Eigenart, die Elemente eines structs an DWORD-Grenzen auszurichten (auf i386), weil dann die CPU schneller arbeiten kann. Das hat in diesem Fall aber fatale Folgen, denn aus dem angegebenen WORDs/BYTEs macht der Compiler einfach mal DWORDs. Und damit ist natürlich der IDT-Eintrag komplett falsch. Glücklicherweise gibt es aber eine ganz einfache Lösung: \<c\> struct idt_entry {

     //...

}\_\_attribute\_\_((packed)); \</c\> Das angehängte *\_\_attribute\_\_((packed))* vehindert, dass der Compiler die Elemente ausrichtet, wodurch schließlich der Code funktioniert.

### Nur ein kleines Zeichen…

Die folgenden Fehler sind eigentlich zu banal für diesen Artikel. Leider passieren sie aber doch zu häufig. Außerdem überliest man sie bei längeren Codepassagen schneller, als einem lieb ist:

#### „==“ ist ungleich „=“

Es ist eigentlich ein totaler Anfängerfehler, in Bedingungen das Zuweisungszeichen „=“ mit dem Vergleichsoperator „==“ zu verwechseln. Also bitte aufpassen!

#### Zahlensysteme

Die Page Size Extension ist eine tolle Sache, also aktivieren wir sie doch mal. Dafür einfach in cr4 das 4. Bit setzen. Ganz simpel: \<asm\> mov eax, cr4 or eax, 10 mov cr4, eax \</asm\> Mh, funktioniert nicht. Der Fehler ist allerdings leicht behoben: \<asm\> mov eax, cr4 or eax, 0x10 mov cr4, eax \</asm\> Ein sehr ärgerlicher Schreibfehler!

Man sollte auch aufpassen, dass Zahlen mit führenden Nullen im Oktalsystem interpretiert werden, daher sollte man darauf verzichten.

#### Wie ging nochmal dieses NOT?!

Ganz einfache Aufgabe: Alle Bits in einer Maske umkippen, also ein bitweise NOT. Wie hieß nochmal der Operator? Achja: \<c\>int gekippt = !0xFA;\</c\> Leider falsch geraten. Das Ausrufezeichen ist kein bitweises, sondern ein logisches Nicht und liefert nur Null (false) und Eins (true), egal welchen Operanden man ihm liefert. Zweiter Versuch: \<c\>int gekippt = -0xFA;\</c\> Nein, wieder falsch. Das Minuszeichen negiert den Wert doch nur, bildet also das Zweierkomplement. Richtig gewsen wäre: \<c\>int gekippt = ~0xFA;\</c\> Diese Operation liefert das gewünschte 0x05.

## C++-bezogene Fehler

### Designated initializers

Das Problem hier ist, dass C++ im Gegensatz zu C keine *designated initializers* (siehe [GCC Manual](http://gcc.gnu.org/onlinedocs/gcc/Designated-Inits.html) für eine Erklärung) unterstützt, beispielsweise wird der Code \<cpp\> struct {

     uint16_t limit;
     void* pointer;

} \_\_attribute\_\_((packed)) gdtp = {

     .limit = GDT_ENTRIES * 8 - 1,
     .pointer = gdt,

}; \</cpp\> beim Kompilieren eine Fehlermeldung namens *expected primary-expression before ‘.’ token* ausgeben.

Man kann allerdings den gleichen Effekt entweder durch Weglassen des Feldnamens erreichen (dann muss die Initialisierung in der Reihenfolge wie die Definition des Strukturtyps sein): \<cpp\> struct {

     uint16_t limit;
     void* pointer;

} \_\_attribute\_\_((packed)) gdtp = {

     GDT_ENTRIES * 8 - 1,
     gdt,

}; \</cpp\> Die andere Möglichkeit ist einen Konstruktor für die Struktur zu definieren – dafür muss aber die Struktur benannt werden: \<cpp\> struct gdt_register {

     uint16_t limit;
     void* pointer;

     gdt_register(uint16_t _limit,
                  void*    _pointer)
       : limit(_limit), pointer(_pointer){}

} \_\_attribute\_\_((packed));

gdt_register gdtp(GDT_ENTRIES \* 8 - 1, gdt); \</cpp\>

## Linker-bezogene Fehler

### Undefined reference to \`funktionsname'

Diese Fehlermeldung wird vom Linker ausgegeben, wenn er kein Symbol mit dem Namen *funktionsname* findet. Dies kann vorkommen, wenn

- du vergessen hast die Objektdatei mit der Definition der Funktion *funktionsname* zu kompilieren und mit zu linken
- du vergessen hast diese Funktion in der Sourcecodedatei zu definieren
- du aus Versehen die Funktion als *static* deklariert hast
- du [C++](https://github.com/lowlevel-eu/wiki/wiki/C%2B%2B "C++") verwendest und *funktionsname* in einer C++-Quellcodedatei definiert und von einer C/Assembler-Quellcodedatei verwendet wird, eine Lösung findet sich [hier](https://github.com/lowlevel-eu/wiki/wiki/C%2B%2B "C++")
- du Archive (.a-Dateien) verwendest und die Reihenfolge der Kommandozeilenparameter von ld nicht richtig ist oder du vergessen hast *--start-group* und *--end-group* anzugeben, siehe hierfür auch das [ld-Manual](http://sourceware.org/binutils/docs/ld/Options.html)

Falls nichts davon zutrifft, könntest du die Objektdatei, die die deiner Meinung nach entsprechende Funktion enthalten soll, disassemblieren und schauen, ob ein entsprechender Symbolname auftaucht. Alternativ kannst du dir auch mit dem Befehl *readelf* die Symbole der Objektdatei anzeigen lassen:

     readelf -s objectfile.o

### Ladeadresse nicht berücksichtigt

Ein kleiner aber gemeiner Fehler: Man hat einen schönen Kernel, der von dem genauso schönen Bootloader in den RAM geladen wird, z. B. nach 0x10000. Dieser wird dann gelinkt:

    OUTPUT_FORMAT("binary")
    INPUT("kernel.o")
    ENTRY(_main)
    SECTIONS {
     .text : {
        *(.text*)
     }
     .data : {
        *(.data*)
     }
     .bss : {
        *(.bss*)
     }
    }

– die CPU verabschiedet sich, da man die Ladeadresse auch im Linkerscript berücksichtigen muss (die Standardadresse ist 0x00, aber das stimmt ja hier nicht). Deshalb:

    OUTPUT_FORMAT("binary")
    INPUT("kernel.o")
    ENTRY(_main)
    SECTIONS {
     .text (0x10000): {
        *(.text*)
     }
     .data : {
        *(.data*)
     }
     .bss : {
        *(.bss*)
     }
    }

### rodata steht am Anfang

Über folgenden Fehler stolpert man meistens gleich zu Beginn, wenn man im Kernel nur ein wenig Text ausgeben möchte. Nehmen wir beispielsweise folgenden kleinen Kernel: \<c\> void main() {

     clrscr;
     kprintf("Hallo Welt!");
     for(;;);

} \</c\>

Der Kernel wird mit folgendem Linkerscript gelinkt:

    OUTPUT_FORMAT("binary")
    INPUT("kernel.o")
    ENTRY(main)
    SECTIONS
    {
     .text (0x10000):
     {
        *(.text*)
     }
     .data :
     {
        *(.data*)
     }
     .bss :
     {
        *(.bss*)
     }
    }

Funktioniert natürlich nicht. Interessanterweise führt das Ändern des Textes zu ganz anderen Fehlern. Die Begründung ist simpel: Der Text („Hallo Welt!“) landet nicht etwa in der .data-Sektion sondern in der sogenannten .rodata-Sektion. Und da wir diese hier nicht im Linkerscript angeben, wird sie einfach an den Anfang der Ausgabedatei gesetzt. Das führt natürlich zwangsweise zu Fehlern, weil ein Text ja kein Code ist. Es gibt nun zwei Möglichkeiten:

1.  Man ergänzt das Linkerscript um die .rodata-Sektion *oder noch besser*
2.  Man schaltet eine Assemblerdatei vor den eigentlichen Kernel, die zum Label main springt. Da man irgendann sowieseo Assembler benötigt, bietet es sich an, das gleich hiermit zu erledigen.

Diese Assembler-Datei, die dann zu „start.o“ assembliert wird, könnte so aussehen:

\<asm\> extern main  ;das ist unser Einsprunglabel im eigentlichen Kernel global start

start: jmp main \</asm\>

Dann noch das Linkerscript modifizieren und fertig:

    OUTPUT_FORMAT("binary")
    INPUT("kernel.o","start.o")
    ENTRY(start)
    SECTIONS
    {
     .text (0x10000):
     {
        *start.o(*)
        *(.text*)
     }
     .data :
     {
        *(.data*)
     }
     .bss :
     {
        *(.bss*)
     }
    }

## Emulator-bezogene Fehler

### Bochs verabschiedet sich mit einer Endlosschleife der Meldung: "math_abort: MSDOS compatibility FPU exception"

Dieser Fehler tritt auf, wenn dein Code zur Berechnung von Fleißkommazahlen auf die [FPU](https://github.com/lowlevel-eu/wiki/wiki/Mathematischer-Koprozessor "FPU") zugreift, z.B. bei der Verwendung des Daentyps "float". Wenn du vorher die FPU nicht initialisiert hast, dann tritt in Bochs der obige Fehler auf. Die Behebung des Problems lässt sich mit folgendem einfachen Assembler-Befehl beheben, den du nur vor der Verwwendung der FPU aufrufen musst: \<asm\>finit\</asm\> Achtung: Falls mehrere Prozesse die FPU verwenden, musst du die Inhalte der FPU-Register vor dem Task-Switch sichern!

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/10118/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2263/index.html)

<!-- MediaWiki page 2263; revision 10118; parent 8018; 2011-09-05T13:38:00Z -->
