# Pascal

| Allgemeines |  |
| -------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Name: | (Turbo/Object)Pascal |
| Inlineassembler: | Ja (Intel-Syntax) |
| Compiler: | FreePascal, Borland Delphi |
| Spracheneigenschaften |  |
| Plattformen: | [Windows](https://github.com/lowlevel-eu/wiki/wiki/Windows "Windows") (Hier vor allem Delphi), [Linux](https://github.com/lowlevel-eu/wiki/wiki/Linux "Linux"), u.a. |
| Beispielkernel in der Sprache: | s.u. |
| Homepage |  |

[www.freepascal.org](http://www.freepascal.org/)

Pascal ist eine strukturierte, prozedurale, objektorientierte, nach Blaise Pascal benannte, und von Nikolaus Wirth im Jahre 1972 als Lehrsprache konzipierte Programmiersprache. Sie ist ähnlich mächtig wie C und wurde im Laufe der Jahre durch verschiedene Sprachkonstrukte erweitert und weiterentwickelt (Borlands Delphi, ObjectPascal).

## Pascal in der Betriebssystementwicklung

Anders als oft behauptet, ist Pascal eine Programmiersprache, die durchaus auch für die Lowlevel-Entwicklung geeignet ist. Allerdings stehen die Funktionen der Standardbibliothek nicht zur Verfügung. Als Daumenregel kann man festhalten, dass Pascal in diesem Zustand ähnlich mächtig wie C ist.

  

## Beispielkernel in Pascal

Zunächst **kernel.pas** - der eigentliche Kernel, der ein Zeichen ausgibt. \<pascal\>unit kernel;

interface

procedure PASCALMAIN(); type tScreen = array\[1..25, 1..80\] of record

       c: char;
       attr: byte;

end; implementation

  
procedure PASCALMAIN(); var

       screen: ^tScreen;

begin

       screen := Pointer($B8000);
       screen^[1, 1].c := '#';
       screen^[1, 1].attr := $07;

end;

end. \</pascal\> Die Zeile *screen^\[1, 1\].attr := \$07;* definiert die Zeichenfarbe, in diesem Fall Grau auf Schwarz. Wollen wir jetzt aber z.B. einen Bluescreen-Zeichenhintergrund haben müssten wir *screen^\[1, 1\].attr := \$1F;* nehmen. Für weitere Farben siehe [Textausgabe](https://github.com/lowlevel-eu/wiki/wiki/Textausgabe "Textausgabe").

Das war der einfache Teil. Als nächstes brauchen wir eine eigene system-Unit, die allerdings für den Anfang nur zwei Stubs bereitstellen muss. **system.pas**: \<pascal\>unit system;

interface

type hresult = longint; procedure FPC_INITIALIZEUNITS; compilerproc; procedure FPC_DO_EXIT; compilerproc;

implementation

procedure FPC_INITIALIZEUNITS; alias: 'FPC_INITIALIZEUNITS'; compilerproc; begin end;

procedure FPC_DO_EXIT; alias: 'FPC_DO_EXIT'; compilerproc; begin end;

end.\</pascal\>

Und der dritte Teil ist ein Assembler-Stub, **prt0.asm**: \<asm\> extern KERNEL_PASCALMAIN global \_start

section .text \_start:

       ; Stack initalisieren
       mov esp, kernelstack

       call KERNEL_PASCALMAIN
       jmp $

multiboot_header: align 4

     MULTIBOOT_MAGIC     equ 0x1BADB002
     MULTIBOOT_FLAGS     equ 0x03
     MULTIBOOT_CHECKSUM  equ -MULTIBOOT_MAGIC-MULTIBOOT_FLAGS

     dd MULTIBOOT_MAGIC
     dd MULTIBOOT_FLAGS
     dd MULTIBOOT_CHECKSUM

section .bss

     resb  16384

kernelstack:\</asm\>

Jetzt sind nur noch 2 leere Units nötig damit der Kernel läuft.

**si_prc.pas**: \<pascal\> unit si_prc;

interface

implementation

end. \</pascal\> **fpintres.pas**: \<pascal\> unit fpintres;

interface

implementation

end. \</pascal\>

Anschließend müssen diese fünf Dateien kompiliert/assembliert und gelinkt werden. Das ist der Punkt, der mir noch nicht so ganz gefällt, weil ich ld eigentlich nicht von Hand aufrufen müssen will, um text=0x100000 setzen zu können.

    nasm -felf prt0.asm
    fpc kernel
    ld -Ttext=0x100000 *.o -o kernel

Wer jetzt neugierig ist was der Kernel alles so auf dem Bildschirm bringt, kann den Kernel nach dem linken sofort mit [QEMU](https://github.com/lowlevel-eu/wiki/wiki/QEMU "QEMU") ausführen:

    qemu -kernel kernel

## Weblinks

- [FreePascal](http://www.freepascal.org)
- [FpOS - ein in Pascal geschriebenes OS](http://code.google.com/p/fpos/)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/9732/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1623/index.html)

<!-- MediaWiki page 1623; revision 9732; parent 9638; 2011-05-02T18:56:57Z -->
