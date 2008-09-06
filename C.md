# C

C ist eine bekannte ältere Programmiersprache. Sie verfolgt das Ziel bei vergleichbarer Ausführungsgeschwindigkeit plattformunabhängiger und abstrakter als [Assembler](https://github.com/lowlevel-eu/wiki/wiki/Assembler "Assembler") zu sein. Direkte Weiterentwicklung von C ist [C++](https://github.com/lowlevel-eu/wiki/wiki/C%2B%2B "C++").

# Kernelprogrammierung mit C

Da man mit C sehr hardwarenah programmieren kann, eignet sich die Sprache zur Programmierung eines Kernels. Es ist sogar die überwiegende Anzahl der Betriebssystemkernel in C geschrieben. Für andere Bereiche ist C jedoch nicht sonderlich geeignet: beispielsweise für einen Bootsektor. Empfehlenswert ist - wie bei jeder anderen Sprache, die im Bereich der Kernelprogrammierung verwendet werden soll - ein Compiler, der Inlineassembler unterstützt. Hierfür eignet sich der [gcc](https://github.com/lowlevel-eu/wiki/wiki/GNU-Compiler-Collection "Gcc").

# Bekannte C-Compiler

- gcc aus der [GNU Compiler Collection](http://gcc.gnu.org/)
- [tcc](http://bellard.org/tcc/) (Tiny C Compiler)
- Borland [Turbo C](http://dn.codegear.com/article/20841) für DOS (16 Bit/Real Mode)

# Assemblercode in C

Während es möglich ist, den allergrößten Teil des Kernels in C zu schreiben, sind für einige wenige Aufgaben nach wie vor einige Zeilen Assemblercode notwendig. Es gibt dabei im Wesentlichen zwei Ansätze:

- **Inline-Assembler**: Assemblercode wird direkt in den C-Code eingebettet. Die konkrete Syntax dafür unterscheidet sich von Compiler zu Compiler, im Allgemeinen wird der Assemblercode durch das Schlüsselwort asm eingeleitet. Ein Vorteil dieser Methode ist, dass ein direkter Zugriff auch auf lokale C-Variablen möglich ist. Sie eignet sich daher für sehr kleine Codestücke besonders gut.

  Siehe auch [Inline-Assembler mit GCC](https://github.com/lowlevel-eu/wiki/wiki/Inline-Assembler-mit-GCC "Inline-Assembler mit GCC")

- **Externe Assemblerdatei**: Der Assemblercode wird in eine eigene Datei ausgelagert und vom C-Code als eigenständige Funktion aufgerufen. Die Übergabe von Parametern und des Rückgabewerts wird im Artikel [Aufrufkonventionen](https://github.com/lowlevel-eu/wiki/wiki/Aufrufkonventionen "Aufrufkonventionen") beschrieben

# Links

- [Draft des C Standards](http://www.open-std.org/JTC1/SC22/WG14/www/docs/n1124.pdf)
- [Tutorial](http://www.c-howto.de/)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/3300/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1526/index.html)

<!-- MediaWiki page 1526; revision 3300; parent 3291; 2008-09-06T08:41:10Z -->
