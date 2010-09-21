# C

| Allgemeines |  |
| -------------------------------- | ----------------------------------------------------------------------------------------------------- |
| Name: | C |
| Inlineassembler: | Ja |
| Compiler: | [gcc](https://github.com/lowlevel-eu/wiki/wiki/GNU-Compiler-Collection "Gcc"), icc, ... |
| Spracheneigenschaften |  |
| Plattformen: | Alle |
| Beispielkernel in der Sprache: | [C-Kernel mit GRUB](https://github.com/lowlevel-eu/wiki/wiki/C-Kernel-mit-GRUB "C-Kernel mit GRUB") |
| Homepage |  |

[The C Standards Committee](http://www.open-std.org/jtc1/sc22/wg14/)

C ist eine bekannte, ältere Programmiersprache. Sie verfolgt das Ziel, bei vergleichbarer Ausführungsgeschwindigkeit plattformunabhängiger und abstrakter als [Assembler](https://github.com/lowlevel-eu/wiki/wiki/Assembler "Assembler") zu sein. Direkte Weiterentwicklung von C ist [C++](https://github.com/lowlevel-eu/wiki/wiki/C%2B%2B "C++").

## Geschichte

C wurde 1971–1973 von Dennis Ritchie in den Bell Laboratories entwickelt, er stützte sich dabei auf die Programmiersprache B, die Ken Thompson in den Jahren 1969/70 geschrieben hatte. Ritchie schrieb auch den ersten Compiler für C. 1973 war die Sprache so weit ausgereift, dass man nun den Unix-Kernel in C neu schreiben konnte.

## Kernelprogrammierung mit C

Da man mit C sehr hardwarenah programmieren kann, eignet sich die Sprache zur Programmierung eines Kernels hervorragend. Es ist sogar die überwiegende Anzahl der Betriebssystemkernel in C geschrieben. Für Einsteiger gibt es die [Tutorialserie OS-Dev für Einsteiger](https://lowlevel-eu.github.io/wiki/pages/1895/index.html "Kategorie:OS-Dev für Einsteiger"), welche beschreibt, wie man einen kleinen Kernel in C schreibt mithilfe des Bootloaders [GRUB](https://github.com/lowlevel-eu/wiki/wiki/Grand-Unified-Bootloader "GRUB") entwickelt. Für andere Bereiche ist C jedoch nicht sonderlich geeignet, um Beispiel für einen Bootsektor. Empfehlenswert ist – wie bei jeder anderen Sprache, die im Bereich der Kernelprogrammierung verwendet werden soll – ein Compiler, der Inlineassembler unterstützt. Hierfür eignet sich der [GCC](https://github.com/lowlevel-eu/wiki/wiki/GNU-Compiler-Collection "GCC").

### Assemblercode in C

Während es möglich ist, den allergrößten Teil des Kernels in C zu schreiben, sind für einige wenige Aufgaben nach wie vor einige Zeilen Assemblercode notwendig. Es gibt dabei im Wesentlichen zwei Ansätze:

- **Inline-Assembler**: Assemblercode wird direkt in den C-Code eingebettet. Die konkrete Syntax dafür unterscheidet sich von Compiler zu Compiler, im Allgemeinen wird der Assemblercode durch das Schlüsselwort *asm* eingeleitet. Ein Vorteil dieser Methode ist, dass ein direkter Zugriff auch auf lokale C-Variablen möglich ist. Sie eignet sich daher für sehr kleine Codestücke besonders gut.

  Siehe auch [Inline-Assembler mit GCC](https://github.com/lowlevel-eu/wiki/wiki/Inline-Assembler-mit-GCC "Inline-Assembler mit GCC")

- **Externe Assemblerdatei**: Der Assemblercode wird in eine eigene Datei ausgelagert und vom C-Code als eigenständige Funktion aufgerufen. Die Übergabe von Parametern und des Rückgabewerts wird im Artikel [Aufrufkonventionen](https://github.com/lowlevel-eu/wiki/wiki/Aufrufkonventionen "Aufrufkonventionen") beschrieben.

## Bekannte C-Compiler

- gcc aus der [GNU Compiler Collection](https://github.com/lowlevel-eu/wiki/wiki/GNU-Compiler-Collection "GNU Compiler Collection")
- [tcc](http://bellard.org/tcc/) (Tiny C Compiler)
- [bcc](http://dir.filewatcher.com/d/FreeBSD/4.2-release/i386/bcc-1995.03.12.tgz.79915.html) ein 16Bit Compiler für Linux (im dev86-Paket enthalten)
- Borland [Turbo C](http://dn.codegear.com/article/20841) für DOS (16 Bit/Real Mode)

## siehe auch

- Die [Tutorialserie OS-Dev für Einsteiger](https://lowlevel-eu.github.io/wiki/pages/1895/index.html "Kategorie:OS-Dev für Einsteiger") benutzt C als Programmiersprache der Wahl

## Weblinks

- [C-Tutorial](http://www.c-howto.de/)
- [Draft des nächsten C Standards (C1x)](http://www.open-std.org/JTC1/SC22/WG14/www/docs/n1494.pdf)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/8327/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1526/index.html)

<!-- MediaWiki page 1526; revision 8327; parent 8326; 2010-09-21T02:03:46Z -->
