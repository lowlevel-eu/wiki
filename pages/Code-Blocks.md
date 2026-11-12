# Code::Blocks

Code::Blocks ist eine [Entwicklungsumgebung](Entwicklungsumgebung.md "Entwicklungsumgebung") für [Windows](Windows.md "Windows"), [Linux](Linux.md "Linux"), Mac OS X und einige weitere Unix-Derivate. Sie wird unter der GNU General Public License veröffentlicht und ist in C++ programmiert.

## Unterstützte Programmiersprachen

Code::Blocks unterstützt eine Reihe verschiedener Programmiersprachen. Insbesondere C und C++ werden besonders hervorgehoben. Die Syntaxhervorhebung kommt jedoch auch mit anderen Sprachen zurecht. Man kann für alle unterstützten Sprachen Farbe und Schreibweise (fett, kursiv etc.) unter *Settings-\>Editor...-\>Syntax Highlighting* festlegen, indem man im Feld *Syntax highlighting for:* die Sprache angibt und dann mit den Feldern *Foreground*, *Background* und *Style* das gewünschte Aussehen festlegt.

Hier die wichtigsten unterstützen Sprachen in Kürze:

- [C](C.md "C")/[C++](C%2B%2B.md "C++")
- [D](D.md "D")
- [Ada](Ada.md "Ada")
- Bash-Skripte
- [Fortran](Fortran.md "Fortran")
- [Assembler](Assembler.md "Assembler")

## Unterstützte Compiler

Code::Blocks bringt keinen Compiler mit, man muss ihn also selbst installieren. Unter Linux ist normalerweise der/die [GCC](GNU-Compiler-Collection.md "GCC") schon vorinstalliert, aber man kann neben diesem Compiler auch andere verwenden:

- [GCC](GNU-Compiler-Collection.md "GCC") (für verschiedene Plattformen, wie PowerPC und TriCore, aber auch für Microcontroller wie den MSP 430)
- Microsofts Visual Studio Compiler
- Borlands C++ Compiler
- Digital Mars C/C++ Compiler
- Open Watcom
- LLVM
- ...

## Betriebssystementwicklung mit Code::Blocks

Zum Kompilieren eines Kernels braucht man häufig spezielle Compilerschalter, etwa "-nostdinc" o. ä. Außerdem will man oft zusätzliche Warnungen, Optimierungen oder Debugging-Informationen aktivieren. Dazu bietet Code::Blocks ein hilfreiches Interface an:

In der "Management"-Spalte (meist links neben dem Editor) findet man im Reiter "Projects" die aktuell geöffneten Projekte. Mit einem Rechtsklick auf den Projektbezeichner (der Eintrag mit dem Code::Blocks-Symbol) und einem weiteren Klick auf "Build options..." findet man sich in einem neuen Fenster wieder, in dem man die Einstellungen für Compiler und Linker festlegen kann. Im Reiter "Compiler Flags" kann man beispielsweise einfach die Optionen auswählen, die man benötigt. Das Drop-Down-Menü "Categories" hilft dabei. Des weiteren kann man Optionen, die man in dieser Liste nicht findet, im Reiter "Other Options" angeben. Die Einstellungen für den Linker kann man dann unter "Linker Settings" angeben: Links die benötigten Libraries und rechts die restlichen Optionen.

Nun sollte dem Kompilieren des Kernels mit Code::Blocks nichts mehr im Wege stehen - ein Klick auf das Zahnrad genügt. Den gewünschten Emulator muss man jedoch selbst starten.

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/10867/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2605/index.html)

<!-- MediaWiki page 2605; revision 10867; parent 10866; 2012-09-22T17:44:18Z -->
