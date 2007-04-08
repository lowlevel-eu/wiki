# Assembler

Bei einem Assembler handel es sich um eine einfach Programmiersprache. Sie wird direkt für einen bestimmten Prozessortyp verdendet und stellt die einzelnen Prozessorbefehle als Wörter mit eventuellen Parametern da. Zusäzlich vereinfach der Assembler die Adressberrechnung und ermöglicht das Berrechnen von Konstanten, die sich aus Formeln zusammensetzen.

## Syntax

Es gibt für die x86 Prozessorfamilie verschiedene Syntax die sich durchgesetzt haben und noch heute verwendung finden.  

### Intel

Der Intel Syntax wird meistens verwendet wenn man Assembler von hand schreibt.  

Beispielcode:

    mov al, 0x10

### AT&T

Dieser Syntax wurde für das schnelle Assemblieren entwickelt um ihn beim Kompilieren von Hochsprachenquellcode als Zwischenschritt zu verwenden.

Beispielcode:

    movb $0x10, %al

## Liste bekannter Assemlber

### Assemlber für x86

FASM (flat assembler) [\[1\]](http://flatassembler.net/)  
MASM (Microsoft Macro Assembler) [\[2\]](http://msdn2.microsoft.com/de-de/library/afzk3475(VS.80).aspx)  
NASM (The Netwide Assembler) [\[3\]](http://nasm.sourceforge.net/)  
TASM (Turbo Assembler) [\[4\]](http://info.borland.com/borlandcpp/cppcomp/tasmfact.html)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/1923/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1514/index.html)

<!-- MediaWiki page 1514; revision 1923; parent 0; 2007-04-08T09:11:33Z -->
