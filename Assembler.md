# Assembler

Als **Assembler** wird einerseits eine einfache Programmiersprache andererseits auch der Übersetzer dieser Programmiersprache in Maschinencode bezeichnet. Die Programmiersprache ist auf einen bestimmten Prozessortyp zugeschnitten und stellt die einzelnen Prozessorbefehle als Wörter (Mnemoniks bzw. engl. Mnemonics) mit eventuellen Parametern da. Damit ist die Sprache kaum portabel. Zusätzlich vereinfacht der Übersetzer der Programmiersprache die Adressberrechnung (unter anderem durch Labels) und ermöglicht das Berechnen von Konstanten, die sich aus Formeln zusammensetzen.

## Syntax

Es gibt für die x86 Prozessorfamilie verschiedene Syntaxen.  

### Intel

Die Intel Syntax wird meistens verwendet wenn man Assembler von Hand schreibt.  

Beispielcode: \<asm\> mov al, 0x10 \</asm\>

### AT&T

Diese Syntax wurde speziell für das schnelle Assemblieren entwickelt, um ihn beim Kompilieren von Hochsprachenquellcode als Zwischenschritt zu verwenden.

Beispielcode: \<asm\> movb \$0x10, %al \</asm\>

Diese Syntax wird vor allem im Zusammenhang mit gcc verwendet. Unter [Inline-Assembler mit GCC](https://github.com/lowlevel-eu/wiki/wiki/Inline-Assembler-mit-GCC "Inline-Assembler mit GCC") befindet sich ein kleines Tutorial hierzu.

## Liste bekannter Assembler

### Assembler für x86

FASM (flat assembler) [\[1\]](http://flatassembler.net/)  
MASM (Microsoft Macro Assembler) [\[2\]](http://msdn2.microsoft.com/de-de/library/afzk3475(VS.80).aspx)  
NASM (The Netwide Assembler) [\[3\]](http://nasm.sourceforge.net/)  
TASM (Turbo Assembler) [\[4\]](http://info.borland.com/borlandcpp/cppcomp/tasmfact.html)  
YASM (Diese Buchstabenkombination besitzt keine offizielle Langform) [\[5\]](http://www.tortall.net/projects/yasm/)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/2614/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1514/index.html)

<!-- MediaWiki page 1514; revision 2614; parent 2606; 2008-03-08T13:31:33Z -->
