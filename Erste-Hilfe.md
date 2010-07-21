# Erste Hilfe

Dieser Artikel richtet sich an verschiedene Personengruppen:

**Anfänger**: Du hast es gerade geschafft deinen Kernel zu laden und möchtest einfach nur Text auf dem Bildschirm ausgeben. Der Code scheint einwandfrei, der Kernel wird auch geladen und... - der Emulator stürzt ab. Wahrscheinlich ist dir nur irgendwo ein kleiner Fehler unterlaufen, den schon tausende vor dir gemacht haben. Deswegen quäl dich nicht und lies einfach diesen Artikel, am besten behälst du die kleinen Tücken der Betriebssystem-Entwicklung, die hier aufgeführt werden, immer im Hinterkopf. Dann sparst du dir viel Zeit und Ärger.

**Frustrierte**: Schon seit einer Woche hängst du an der einen Codestelle und findest den Fehler einfach nicht? Du möchtest dein Betriebssystemprojekt am liebsten aufgeben und nur dein Ehrgeiz hält dich davon ab? Bestimmt ist es nur ein kleiner Fehler, den du immer wieder überliest. Schau einfach mal in diesem Artikel, ob du nicht vielleicht hier die Rettung findest.

**Doktoren** Du bist häufig im Forum unterwegs und hilfst gerne? Und da ist dieser eine Fehler, den alle immer wieder machen. Damit du ihn nicht tausendmal wieder korrigieren musst, schreib ihn einfach in diesen Artikel.

## Allgeime Fehler

### "ich habe die fehlerhafte Stelle genau gefunden"

NEIN! Es kann sein, dass die Stelle fehlerhaft ist, sie muss es aber nicht sein. Dafür ist die Betriebssystementwicklung einfach viel zu komplex. Vielmehr kann die Codestelle nur der Auslöser für einen Fehler sein, der sich schon viel früher eingeschlichen hat. Beispielsweise kann ein Fehler bei einem bestimmten Funktionsaufruf auftreten, aber nicht, weil die Funktion fehlerhaft ist, sondern weil der Stack zu groß wird.

### Schon im Bootloader

Viele schreiben ihren Bootloader zwar nicht selbst, aber die Unerscchrockenen, die es tun, begeben sich gleich am Anfang in Gefahr: \<asm\> \[org 0x7c00\]

mov si, msg call write jmp \$ \</asm\> Feiner Code, aber wer weiß, welche Registerzustände das BIOS uns überlässt. Wenn es zum Beispiel einen Farjump nach 0x00:0x7C00 macht, dann ist alles in Ordnung. Ist es aber einer nach 0x7C0:0x00, dann ist bei "call write " Schluss, weil die Org-Directive erwartet, dass in IP ein 0x00 steht. Außerdem wissen wir auch nicht, wohin das BIOS den Stack gesetzt hat, also sollte man den auch noch verschieben. Deswegen hat am Anfang jedes Bootloaders folgender (oder ähnlicher) Code zu stehen: \<asm\> %define STACK_SEGMENT 0x1000 %define STACK_OFFSET 0xFFFF

\[org 0x7c00\] cli xor ax, ax ; null segments mov ds, ax mov es, ax mov ax, STACK_SEGMENT mov ss, ax mov sp, STACK_OFFSET jmp 0x00:refresh refresh: sti

mov si, msg call write jmp \$ \</asm\> So gibt es keine Komplikationen. (Die obige Adresse des Stacks ist natürlich nur beispielhaft)

### Der Stack

Kommen wir jetzt zum einem der größten Biester in der Betriebssystemsentwicklung: der Stack. Das erste, was viele vergessen, ist, dass der Stack nach UNTEN hin wächst. Ein *push* vermindert also den Stackpointer! Und der Stack die unangenehme Eigenschaft, alles zu überschreiben, was sich ihm in den Weg stellt, also auch Code und Daten. Deswegen ist folgender Code zum Scheitern verurteilt: \<asm\>

1.  define GDT_BASE 0x20000
2.  define STACK_TOP 0x20100

gdt mit 30 Einträgen anlegen

...

...

mov esp, STACK_TOP xor eax, eax mov ss, ax

call ClearScreen

...

\</asm\>

Und irgendwo in *ClearScreen* schmiert dann der Code ab, weil der Stack eben nach UNTEN wächst und die GDT überschreibt. Also immer vorsichtig sein mit dem Stack, insbesondere wenn irgendwann man für jeden Prozess einen eigenen hat.

### invalid TSS

Das [TSS](https://github.com/lowlevel-eu/wiki/wiki/Task-State-Segment "TSS") ist ein sehr speicherhungriges Konstrukt, wesegen viele Programmierer auf Software-Multitasking umsteigen. Aber ganz ohne TSS geht es dann doch nicht. Dann nimmt man eben nur ein TSS und ändert die einzelnen Felder je nach Prozess. Damit spart man viel Speicherplatz. Dann hat man im [Scheduler](https://github.com/lowlevel-eu/wiki/wiki/Scheduler "Scheduler") folgendes: \<asm\> %define TSS_SELECTOR 0x28 task_switch:

     ;alten Zustand sichern
     ;neuen Prozess suchen
     ;Einträge im TSS ändern
     mov ax, TSS_SELECTOR
     ltr ax
     ;neuen Zustand laden

iret \</asm\> Ja, gut gedacht, funktioniert aber nicht. Bochs beschwert sich zum Beispiel mit einem gut gemeinten *LTR: doesn't point to an available TSS descriptor!*. Das Problem: die CPU setzt im TSS das sogenannte busy-Flag in der GDT beim Laden des TSS. Wenn man Hardware-Multitasking verwendet, wofür daa TSS eigentlich gedacht ist, dann ist das kein Problem, da man ja immer wieder ein neues TSS lädt und im alten das busy-Flag automatisch wieder gelöscht wird. Hier wird aber nur EIN TSS verwendet. Desshalb muss das busy-Flag von Hand gelöscht werden:

\<asm\>

...

      mov BYTE  [ADDRESS_GDT+TSS_SELECTOR+5], 0x89  ;busy-Flag löschen
      mov ax, 40
      ltr ax

...

\</asm\>

### Defekter Sektor

Es kann auch durchaus vorkommen das ein Sektor der Diskette, die zu zum Testen verwendest, defekt ist. Dieser Fehler ist besonders dann schwer zu finden wenn man sein System primär auf realer Hardware testet.

## C-spezifische Fehler

### \_\_attribute\_\_((packed)) in structs vergessen

TODO

### volatile

Der Compiler hat die angenehme Eigenschaft den Code um sinnlose Passagen zu erleichtern. Aber manchmal ist das eben nicht hilfreich, vor allem wenn man inline-Assembler verwendet wird dieser oft wegoptimiert. Dagegen hilft das *volatile* Schlüsselwort. Es fordert den Compiler dazu auf den entsprechenden Code nicht zu optimieren: \<c\> asm volatile("mov %0, %%eax;" : : "a" (value) ); \</c\> Aber volatile kann noch mehr. Folgender Code könnte nicht funktionieren: \<c\> bool key_pressed=false; //wird vom IRQ-handler gesetzt

void wait_keypress() {

     while(!key_pressed);

} \</c\> Aus der Schleife könnte der Compiler eine Endlosschleife machen, da er der Meinung ist, dass sich key_pressed nicht ändern kann in der Schleife. Aber *volatile* löst das Problem: \<c\> volatile bool key_pressed=false; //wird vom IRQ-handler gesetzt

void wait_keypress() {

     while(!key_pressed);

} \</c\> Num wird bei jedem Schleifendurchlauf der Wert von key_pressed neu geladen und getestet.

### Nur ein kleines Zeichen...

**Soll diese Passage im Artikel bleiben?** Die folgenden Fehler sind eigentlich zu banal für diesen Artikel. Leider passieren sie aber doch zu häufig. Außerdem überließt man sie bei längeren Codepassagen schneller als einem lieb ist:

#### "==" ist ungleich "="

#### Zahlensysteme

Die Page Size Extension ist eine tolle Sache, also aktivieren wir sie doch mal. Dafür einfach in cr4 das 4. Bit setzen. Ganz simpel: \<asm\> mov eax, cr4 or eax, 10 mov cr4, eax \</asm\> Mh, funktioniert nicht. Der Fehler ist allerdings leicht behoben: \<asm\> mov eax, cr4 or eax, 0x10 mov cr4, eax \</asm\> Ein sehr ärgerlicher Schreibfehler!

#### Wie ging nochmal dieses NOT?!

Ganz einfache Aufgabe: Alle Bits in einer Maske umkippen, also ein logisches NOT. Wie hieß nochmal der Operator? Achja:

     int gekippt = !0xFA;

Leider falsch geraten. Das Ausrufezeichen liefert nur Null (false) und Eins (true), egal welchen Operanden man ihm liefert. Zweiter Versuch:

     int gekippt = -0xFA;

Nein, wieder falsch. Das Minuszeichen negiert den Wert doch nur, bildet also das Zweierkomplement. Richtig gewsen wäre:

     int gekippt = ~0xFA;

Diese Operation liefert das gewünschte 0x05

## C++ spezifische Fehler

### designated initializers

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

}; \</cpp\> Die andere Möglichkeit ist einen Konstruktor für die Struktur zu definieren - dafür muss aber die Struktur benannt werden: \<cpp\> struct gdt_register {

     uint16_t limit;
     void* pointer;

     gdt_register(uint16_t _limit,
                  void*    _pointer)
       : limit(_limit), pointer(_pointer){}

} \_\_attribute\_\_((packed));

gdt_register gdtp(GDT_ENTRIES \* 8 - 1, gdt); \</cpp\>

## Linker-spezifische Fehler

### undefined reference to \`funktionsname'

Diese Fehlermeldung wird vom Linker ausgegeben, wenn er kein Symbol mit dem Namen *funktionsname* findet. Dies kann vorkommen, wenn

- du vergessen hast die Objektdatei mit der Definition der Funktion *funktionsname* zu kompilieren und mit zu linken
- du vergessen hast in der Sourcecodedatei diese Funktion zu definieren
- du aus Versehen die Funktion als *static* deklariert hast
- du [C++](https://github.com/lowlevel-eu/wiki/wiki/C%2B%2B "C++") verwendest und *funktionsname* in einer C++-Quellcodedatei definiert und von einer C/Assembler-Quellcodedatei verwendet wird, eine Lösung findet sich [hier](https://github.com/lowlevel-eu/wiki/wiki/C%2B%2B "C++")
- du Archive (.a-Dateien) verwendest und die Reihenfolge der Kommandozeilenparameter von ld nicht richtig ist oder du vergessen hast *--start-group* und *--end-group* anzugeben, siehe hierfür auch das [ld-Manual](http://sourceware.org/binutils/docs/ld/Options.html)

Falls nichts davon zutrifft, könntest du die Objektdatei, die die deiner Meinung nach entsprechende Funktion enthalten soll, disassemblieren und schauen, ob ein entsprechender Symbolname auftaucht. Alternativ kannst du dir auch mit dem Befehl *readelf* die Symbole der Objektdatei anzeigen lassen:

     readelf -s objectfile.o

### rodata steht am Anfang

TODO

### Ladeadresse nicht berücksichtigt

TODO

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/7963/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2263/index.html)

<!-- MediaWiki page 2263; revision 7963; parent 7958; 2010-07-21T20:06:45Z -->
