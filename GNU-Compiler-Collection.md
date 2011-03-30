# GNU Compiler Collection

| Allgemeines |  |
| --------------- | ----------------------------------------------- |
| Name: | GNU Compiler Collection |
| Entwickler: | [Das GCC-Team](http://gcc.gnu.org/about.html) |
| Akt. Version: | 4.6.0 |
| Lizenz: | GNU GPL |
| Plattform: | Linux, Unix<br>(inoffiziell: Windows) |
| Homepage |  |

[gcc.gnu.org](http://gcc.gnu.org/)

Die **GNU Compiler Collection** ist eine Sammlung von Compilern. Unterstützt werden die [Sprachen](https://lowlevel-eu.github.io/wiki/pages/1648/index.html "Kategorie:Programmiersprache") [C](https://github.com/lowlevel-eu/wiki/wiki/C "C"), [C++](https://github.com/lowlevel-eu/wiki/wiki/C%2B%2B "C++"), Java, Objective-C, [Fortran 95](https://github.com/lowlevel-eu/wiki/wiki/Fortran "Fortran"), Treelang und [Ada](https://github.com/lowlevel-eu/wiki/wiki/Ada "Ada") und demnächst auch [D](https://github.com/lowlevel-eu/wiki/wiki/D "D"). Zusätzlich werden die Plattformen [x86](https://github.com/lowlevel-eu/wiki/wiki/X86 "X86"), [AMD64](https://github.com/lowlevel-eu/wiki/wiki/X86-64 "X86-64") (x86_64), Alpha, [ARM](https://github.com/lowlevel-eu/wiki/wiki/ARM "ARM"), IA-64, PowerPC und viele weitere unterstützt.

## GCC unter Windows

Die GCC wird nicht direkt unterstützt, sondern nur durch die Portierung MinGW und die Arbeitsumgebung Cygwin.

## GCC unter Linux

Die GCC gehört zum Standardumfang jeder Linuxdistrubition. Aufgerufen wird sie im Terminal mit dem Befehl *gcc \[Zu kompilierende Datei\]*.

## Zusätzliche Parameter

| Parameter | Beschreibung |
| ----------- | -------------------------------------------------------------------------------------------- |
| -o | Name (und Typ) der Ausgabedatei. Bei .bin-Endung wird auch nur eine binäre Datei erstellt. |
| -c | Kein Linken des Quellcodes. |
| -O | Optimieren des Quellcodes. Grad kann von 0 - 3 angegeben werden. |
| -l | Bindet weitere Bibliotheken ein |
| -Wall | Aktiviert sinnvolle Warnungen. |
| -Werror | Behandelt alle Warnungen wie Fehler |
| -pedantic | Gibt alle Warnungen aus. |

## Siehe auch

[Inline-Assembler mit GCC](https://github.com/lowlevel-eu/wiki/wiki/Inline-Assembler-mit-GCC "Inline-Assembler mit GCC")

## Weblinks

- [Website des GCC](http://gcc.gnu.org)
- [TDM's GCC/mingw32 Builds](http://www.tdragon.net/recentgcc/) (experimentelle Builds von GCC 4.x für Windows)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/9641/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1805/index.html)

<!-- MediaWiki page 1805; revision 9641; parent 7734; 2011-03-30T20:56:29Z -->
