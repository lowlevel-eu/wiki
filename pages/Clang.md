# Clang

| Allgemeines |  |
| --------------- | ----------------------------------------------------- |
| Name: | Clang |
| Entwickler: | [Das Clang-Team](https://clang.llvm.org/about.html) |
| Akt. Version: | 10.0.1 |
| Lizenz: | Apache 2.0 |
| Plattform: | alle verbreiteten und ein paar andere |
| Homepage |  |

[clang.llvm.org](https://clang.llvm.org/)

  
Clang ist ein Frontend für die LLVM Compiler Infrastructure für die C-ähnlichen Sprachen [C](C.md "C"), [C++](C%2B%2B.md "C++"), [Objective-C](Objective-C.md "Objective-C")/++, OpenCL, CUDA und RenderScript. Dabei werden auch eine Vielzahl von CPU-Architekturen und Plattformen unterstützt. Clang ist immer ein Cross-Compiler, über das `--target` Attribut kann die Zielplatform als triple angegeben werden (bspw `x86_64-pc-lf_os` oder `x86_64-linux-elf`), extra Cross-Compiler sind also nicht notwendig.

Um Clang ein neues Betriebssystem beizubringen, sind ein paar Änderungen an der Code-Basis notwendig, unter anderem um die Toolchain oder eingebaute `define`s zu definieren.

Clang selber wandelt den Code in LLVM IR Code um, dieser kann dann von anderen LLVM Tools zu Maschinencode umgewandelt werden. Normalerweise erfolgt das aber automatisch mit einem `clang` Aufruf, ähnlich wie auch der [GCC](GNU-Compiler-Collection.md "GCC") intern diverse andere Programme ausführt.

Generell versucht Clang mit dem GCC kompatibel zu sein, verwendet die gleichen Kommandozeilenargumente und Spracherweiterungen. Die meisten höheren Build-Tools (CMake, gn, ..) definieren Clang dabei als einen GCC mit Extras.

## Siehe auch

[Inline-Assembler mit GCC](Inline-Assembler-mit-GCC.md "Inline-Assembler mit GCC")

## Weblinks

- [Blog-Post von LittleFox: Neues OS zu Clang/LLVM hinzufügen (englisch)](https://lf-net.org/blog/posts/2020-05-17-clang-osdev/)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/11484/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2673/index.html)

<!-- MediaWiki page 2673; revision 11484; parent 11483; 2020-08-09T18:35:42Z -->
