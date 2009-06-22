# Interrupt Service Routine

Eine **Interrupt Service Routine** (ISR) ist ein Programmabschnitt, der aufgerufen wird, wenn in der CPU ein [Interrupt](https://github.com/lowlevel-eu/wiki/wiki/Interrupt "Interrupt") ausgelöst wird. Damit die CPU die Routine findet, muss ein entsprechender Zeiger in die [IVT](https://github.com/lowlevel-eu/wiki/wiki/Interrupt-Vector-Table "IVT") (Real Mode) bzw. [IDT](https://github.com/lowlevel-eu/wiki/wiki/Interrupt-Descriptor-Table "IDT") (Protected Mode und Long Mode) eingetragen werden.

## Aufgaben

Eine ISR hat als Aufgabe gezielt auf die Unterbrechung zu reagieren. Dies gestaltet sich je nach Art des Interrupt unterschiedlich. Wenn die Ursache ein [asynchroner Interrupt](https://github.com/lowlevel-eu/wiki/wiki/Interrupt#asynchrone-interrupts "Interrupt") war, muss die Routine außerdem dafür sorgen, dass der Zustand des Programms (insbesondere Register, Programmzähler, Speicher, ...) nicht unbeabsichtigt verändert wird. Bei [synchronen Interrupts](https://github.com/lowlevel-eu/wiki/wiki/Interrupt#synchrone-interrupts "Interrupt") ist es hingegen in der Regel erforderlich, entweder das Programm zu terminieren, oder die weitergehende Behandlung des Interrupts (Signal-Handler wie z.B. [POSIX](https://github.com/lowlevel-eu/wiki/wiki/POSIX "POSIX")-Signale, Exception-Handler, Debuggeraufruf, ...) zu veranlassen.

### Systemaufrufe

Systemaufrufe (und BIOS-Aufrufe) fallen in die Kategorie synchronen Interrupts. Diese werden mittels eines Software-Interrupts (*int xx*) ausgelöst, und ihre Seiteneffekte (d.h. ihre eigentliche Funktion) werden in der Regel in Form eines Application Binary Interfaces dokumentiert.

## Einfache Implementierung

Die Unterscheidung zwischen asynchronen und synchronen Interrupts, sowie die korrekte Behandlung letzterer, ist für eine erste Implementierung viel zu komplex. Auf der x86-Architektur reicht es aus, alle Interrupts gleich zu behandeln. Dies bedeutet, die ISRs für alle Interrupts haben den selben Aufbau, und teilen sich auch Teile des Codes.

Eine sehr einfache Implementierung, die so in der Praxis wohl nicht zu finden ist, aber anhand der das Grundprinzip erläutert werden soll, könnte wie folgt aussehen. (Einsatztauglichere Handler, die darauf aufbauen, gibt es weiter unten.)

\<asm\>; Vereinfachter Interrupt-Stub für den Protected Mode

Verwendbar für IRQs und Software Interrupts

NICHT für alle Exceptions verwendbar!

interrupt_stub:

       ; Alle Register sichern
       pusha
       push ds
       push es
       push fs
       push gs

       ; In die Datensegmente einen Kernelselektor laden, damit wir 
       ; garantiert mit Kernelprivilegien auf den Speicher zugreifen
       mov ax, KERNEL_DS
       mov ds, ax
       mov es, ax
       mov fs, ax
       mov gs, ax

       ; Aufruf der eigentlichen Behandlung
       call behandlung

       ; Alte Registerwerte in umgekehrter Reihenfolge wiederherstellen
       pop gs
       pop fs
       pop es
       pop ds
       popa

       ; Rücksprung
       iret</asm>

Der Code ist noch recht übersichtlich, trotzdem sollen hier noch einmal einige Details erläutert werden:

### Stack-Layout

Wenn die CPU zu dieser Interrupt-Behandlung gesprungen ist, dann hat sie bereits einige Register auf dem Stack gesichert. Wenn sich die CPU im Ring 0 befunden hat, als der Interrupt ausgelöst wurde, sind dies EFLAGS, CS und EIP, die in dieser Reihenfolge auf den Stack gelegt werden. Wenn die CPU im Ring 1-3 war, wurden vorher noch SS und ESP auf den Stack gelegt. (Und es wurde ein neuer Wert für diese beiden Register aus dem [TSS](https://github.com/lowlevel-eu/wiki/wiki/Task-State-Segment "TSS") geladen.)

An der Speicherstelle \[ESP\] befindet sich somit der alte EIP-Wert, an \[ESP + 4\] der alte CS-Wert und so weiter. Es ergibt sich also folgendes Bild für den Stackframe, zu dem Zeitpunkt, wenn die CPU sich bei dem Label *interrupt_stub* befindet:

`(Erinnerung: Der Stack wächst nach unten, also in Richtung der niedrigen Adressen) `

 : hohe Adressen

 :

+-----------+ \| USER SS \| (nur bei Interrupt in Ring 1-3) +-----------+ \| USER ESP \| (nur bei Interrupt in Ring 1-3) +-----------+ \| EFLAGS \| +-----------+ \| CS \| +-----------+ \| EIP \| \<---- ESP zeigt hier hin +-----------+

 :

` : niedrige Adressen`

Diese 3 bzw. 5 Werte, die sich auf dem Stack befinden müssen wir also nicht noch einmal sichern. Allerdings müssen wir noch die General Purpose Register und die 4 Segment Register retten. Dies geschieht mit dem *pusha*, sowie den 4 *push*s. Zum Schluss werden mittels *pop* und *popa* die alten Werte dieser Register wiederhergestellt, bevor zum Aufrufer zurückgesprungen wird. Dies ist notwendig, um unsere weiter oben formulierte Forderung, dass wir den Zustand des Programms nicht ändern, zu erfüllen. Diese pauschale Sicherung aller Register erlaubt es uns im folgenden Code frei über alle Register zu verfügen.

Kleiner Einschub: Dies hat allerdings auch Folgen für die Wertrückgabe von einem Systemaufruf. Wir können jetzt ja nicht einfach *mov eax, ERGEBNIS* machen, weil der alte Wert von eax ja am Ende wieder überschrieben wird. Man könnte jetzt natürlich damit anfangen an den pushs und pops herumzubasteln, aber das wird schnell unübersichtlich und fehlerträchtig. Weiter unten werde ich dafür eine elegantere Lösung präsentieren.

Der Stack-Frame sieht nach dem *push gs* wie folgt aus:

`(Erinnerung: Der Stack wächst nach unten, also in Richtung der niedrigen Adressen) `

 : hohe Adressen

 :

+-----------+ \| USER SS \| (nur bei Interrupt in Ring 1-3) +-----------+ \| USER ESP \| (nur bei Interrupt in Ring 1-3) +-----------+ \| EFLAGS \| +-----------+ \| CS \| +-----------+ \| EIP \| +-----------+ \| EAX \| +-----------+ \| ECX \| +-----------+ \| EDX \| +-----------+ \| EBX \| +-----------+ \| ESP \| (das ESP das im letzten Bildchen auf EIP gezeigt hat) +-----------+ \| EBP \| +-----------+ \| ESI \| +-----------+ \| EDI \| +-----------+ \| DS \| +-----------+ \| ES \| +-----------+ \| FS \| +-----------+ \| GS \| \<---- ESP zeigt hier hin +-----------+

 :

` : niedrige Adressen`

### Kernel-Bedingungen

Bisher haben wir also dafür gesorgt, dass die General Purpose Register und die Segment Register gesichert und wiederhergestellt werden. Dazwischen kommt jetzt der eigentliche Code, der den Interrupt behandeln soll. Dafür ist es allerdings Voraussetzung, dass sich das System in einem definierten Zustand befindet. Zum Beispiel die Segmentregister könnten Ring 3 Selektoren enthalten. Die sind nicht unbedingt geeignet, um auf Daten im Kernel zuzugreifen, deswegen sollten wir diese zunächst mit Kernel Selektoren laden. Dies macht dieser Abschnitt: \<asm\> mov ax, KERNEL_DS

       mov ds, ax
       mov es, ax
       mov fs, ax
       mov gs, ax</asm>

Dabei ist KERNEL_DS ggf. durch eine passende Konstante zu ersetzen, die den Kernel Daten Selektor repräsentiert. Das Stack Segment Register (SS) muss nicht mehr geladen werden, denn das hatte entweder bereits zum Zeitpunkt des Interrupts einen gültigen Selektor geladen (Ring 0), oder wurde beim Interrupt aus dem TSS geladen (Ring 1-3). Alles andere hätte längst einen General Protection Fault (#GPF) ausgelöst, auf den (bei unserem Stand) unweigerlich ein Double Fault, und dann ein Triple Fault also ein Reboot gefolgt wäre.

### Behandlung

Dann sind wir endlich bereit den Interrupt zu behandeln. In dem Code oben wird einfach zur Routine *behandlung* gesprungen, die am besten in einer Hochsprache wie C geschrieben ist:

\<c\>void behandlung() {

       // schreibt ein buntes A in die obere linke Ecke
       short *video = (short*)0xb8000;
       video[0] = 0x4141; // 0x??41 = A und 0x41?? = blaue Schrift, roter Hintergrund

}\</c\>

Jetzt haben wir eine ISR, die uns ein buntes A auf den Bildschirm malt. Wenn unser Interrupt allerdings sowas wie ein Systemaufruf ist, dann wäre es doch praktisch, wenn er auf die Register zugreifen könnte.

Dazu nutzen wir aus, dass wir die Registerwerte auf den Stack gesichert haben. Diese dienen praktisch als Parameter für die Methode *behandlung*. Der erste Parameter einer C-Funktion ist dabei das, was zuletzt auf den Stack gepusht wurde. Bei uns also GS, dann kommt FS und so weiter. Wenn wir das wie folgt machen wird die Funktionsdefinition allerdings etwas lang: \<c\>void behandlung(unsigned int gs, unsigned int fs, unsigned int es ...\</c\>

Schlauer ist es ein struct dafür zu nehmen: \<c\>struct stack_frame {

       unsigned int gs, fs, es, ds;
       unsigned int edi, esi, ebp, _esp, ebx, edx, ecx, eax;
       unsigned int eip, cs, eflags, esp, ss;

}

void behandlung(struct stack_frame sf) {

       // ein buntes Zeichen auf den Bildschirm schreiben
       unsigned short *video = (unsigned short*)0xb8000;
       unsigned char zeichen = (unsigned char)sf.eax; // AL auslesen (unteres Byte von EAX)

       video[0] = 0x4100 | zeichen; // 0x41?? = blaue Schrift, roter Hintergrund

       sf.eax = 0x12345678; // Rückgabewert in eax

}\</c\>

Ein Programm könnte jetzt in AL ein Zeichen laden (z.B. 0x42 für B), und unsere ISR aufrufen. Dann würde auf dem Bildschirm ein buntes AL erscheinen.

Außerdem können wir die Werte in dem *struct stack_frame* dafür benutzen, um Rückgabewerte zu realisieren. Weil das struct auf dem Stack liegt, wird es am Ende der ISR von den *pop*s wieder in die Register zurückgelesen, und unsere Rückgabewerte

Im Folgenden soll nun erläutert werden, wie man der CPU mitteilt, dass diese unsere ISR benutzen soll

## Installation

Im Protected Mode muss der Zeiger für ein ISR in die [Interrupt Descriptor Table (IDT)](https://github.com/lowlevel-eu/wiki/wiki/Interrupt-Descriptor-Table "IDT") eingetragen werden. Das Format ist im dazugehörigen Artikel erklärt. Dabei ist zu beachten, dass die Flags richtig gesetzt werden. TODO

## Nachteile der einfachen Implementierung

### Behandlung mehrerer Interrupts

Folgendes Beispiel soll einen Nachteil dieser ISR illustrieren:

Zunächst weisen wir den [PIC](https://github.com/lowlevel-eu/wiki/wiki/Programmable-Interrupt-Controller "PIC") an die [IRQs](https://github.com/lowlevel-eu/wiki/wiki/Programmable-Interrupt-Controller#irq-tabelle "IRQ") 0-15 auf die Interrupts 0x20 bis 0x2f zu mappen, und tragen für all diese Interrupts unsere ISR in die IDT ein. Wenn dann z.B. IRQ 0 ausgelöst wird, schaut die CPU in die IDT an den Eintrag 0x20, und sieht dort, dass sie zu *interrupt_stub* springen soll. Bei einem anderen IRQ (z.B. IRQ 1) läuft dieses auf genau das selbe hinaus: Die CPU schaut in den Eintrag (z.B. Interrupt 0x21), und sieht, dass sie zu *interrupt_stub* springen soll. Dort angekommen, wissen wir aber in beiden Fällen nicht, welcher IRQ bzw. Interrupt ausgelöst wurde, weil die CPU uns sowas nicht mitteilt.

Die einzige Lösung dafür ist, für jeden IRQ eine andere ISR einzutragen. Diese Handler sehen genauso aus wie unser Beispiel, aber mit jeweils unterschiedlichen Namen. (Auch bekannt als Copy&Paste):

\<asm\>; Handler für IRQ 0 interrupt_stub_irq0:

       pusha
       ...
       call behandlung_irq0
       ...
       popa
       iret

Handler für IRQ 1

interrupt_stub_irq1:

       pusha
       ...
       call behandlung_irq1
       ...
       popa
       iret

Und so weiter\</asm\>

In jeden Eintrag in der IDT tragen wir einen anderen Handler ein. In Interrupt 0x20 also interrupt_stub_irq0, in Interrupt 0x21 interrupt_stub_irq1, usw. Dann ruft die CPU für jeden IRQ einen anderen Interrupt auf, und wenn wir z.B. in behandlung_irq0 ankommen, wissen wir, dass IRQ 0 ausgelöst wurde.

Das ganze müsste man dann mindestens für die 16 IRQs, die 32 CPU-Exceptions (bzw. eigentlich 19) und einen Software Interrupt machen. Das wird eine Menge Arbeit, was auch eine Menge Bugs bedeutet.

### Weitere Nachteile

- Einige Exceptions legen zusätzlich einen Fehlercode auf den Stack, nachdem sie EIP auf den Stack gelegt haben. Dieser Fehlercode enthält weitere Informationen zur Ursache des Fehlers. Genaueres steht dazu im Intel Manual.

<!-- -->

- Um präemptives oder kooperatives Software-[Multitasking](https://github.com/lowlevel-eu/wiki/wiki/Multitasking "Multitasking") zu implementieren, muss man den Stack Pointer wechseln. Zwar legt unsere Variante mit dem *pusha* einen Stack Pointer (\_esp) auf den Stack, aber das *popa* ignoriert den immer. Dieser Stack Pointer zeigt übrigens auf den Kernel Stack, denn entweder wurde er aus dem TSS geladen, wenn der Interrupt im Ring 3 auftrat, oder wir haben uns die ganze Zeit schon im Kernel Mode (Ring 0) befunden. Der Stack Pointer, der zusätzlich auf den Stack gelegt wird, wenn ein Interrupt im Ring 3 aufgetreten ist (esp), nützt uns wenig. Wenn wir diesen austauschen, dann tauschen wir maximal die Stacks von zwei Tasks aus, aber dann ist es bereits zu spät für einen kompletten Kontextwechsel: Die General Purpose Register, sowie EIP und EFLAGS wurden noch vom alten Stack geladen. Das heißt wir müssen den Stack irgendwie anders wechseln.

Deswegen arbeiten wir im Folgenden an einer Generalisierung und Vereinfachung des gesamten Aufbaus unserer ISRs.

## Allgemeiner Interruptstub

*So langsam wird das hier ne ganze Menge Text. Deswegen erstmal ein Päuschen und -\>* TODO

- Interruptnummer auf den Stack
- Makros
- Zeiger auf den Stackframe als Parameter und Rückgabewert von *behandlung*.

Aber wer schon mal sehen will, worauf das ganze hinauslaufen soll, kann sich die Implementierung in tyndur anschauen:

- <http://git.tyndur.org/?p=tyndur.git;a=blob;f=src/kernel/src/stubs.asm;hb=HEAD> (kernel)
- <http://git.tyndur.org/?p=tyndur.git;a=blob;f=src/kernel2/src/arch/i386/interrupts/int_stubs.S;hb=HEAD> (kernel2)

## Task Gates

TODO

## Real Mode

Im Real Mode sind im Prinzip die selben Schritte wie im Protected Mode erforderlich. Allerdings werden SS und ESP nie automatisch gesichert bzw. automatisch geladen, weil es ja keine Ring-Unterscheidungen gibt. Die Konstante KERNEL_DS wäre für einen Kernel außerdem einfach CS.

## Siehe auch

- Intel Manual Volume 3A - Chapter 5 Interrupt and Exception Handling

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/4471/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1857/index.html)

<!-- MediaWiki page 1857; revision 4471; parent 4467; 2009-06-22T21:13:20Z -->
