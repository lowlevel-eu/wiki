# GNU Compiler Collection

| Allgemeines |  |
| --------------- | ----------------------------------------------- |
| Name: | GNU Compiler Collection |
| Entwickler: | [Das GCC-Team](http://gcc.gnu.org/about.html) |
| Akt. Version: | 4.8.0 |
| Lizenz: | GNU GPL |
| Plattform: | Linux, Unix<br>(inoffiziell: Windows) |
| Homepage |  |

[gcc.gnu.org](http://gcc.gnu.org/)

Die **GNU Compiler Collection** ist eine Sammlung von Compilern. Unterstützt werden die [Sprachen](https://lowlevel-eu.github.io/wiki/pages/1648/index.html "Kategorie:Programmiersprache") [C](https://github.com/lowlevel-eu/wiki/wiki/C "C"), [C++](https://github.com/lowlevel-eu/wiki/wiki/C%2B%2B "C++"), [Java](https://github.com/lowlevel-eu/wiki/wiki/Java "Java"), Objective-C, [Fortran 95](https://github.com/lowlevel-eu/wiki/wiki/Fortran "Fortran"), Treelang und [Ada](https://github.com/lowlevel-eu/wiki/wiki/Ada "Ada") und demnächst auch [D](https://github.com/lowlevel-eu/wiki/wiki/D "D"). Zusätzlich werden die Plattformen [x86](https://github.com/lowlevel-eu/wiki/wiki/X86 "X86"), [AMD64](https://github.com/lowlevel-eu/wiki/wiki/X86-64 "X86-64") (x86_64), Alpha, [ARM](https://github.com/lowlevel-eu/wiki/wiki/ARM "ARM"), IA-64, PowerPC und viele weitere unterstützt.

## GCC unter Windows

Die GCC wird nicht direkt unterstützt, sondern nur durch die Portierung MinGW und die Arbeitsumgebung Cygwin.

## GCC unter Linux

Die GCC gehört zum Standardumfang jeder Linuxdistribution. Aufgerufen wird sie im Terminal mit dem Befehl *gcc \[Zu kompilierende Datei\]*.

## Zusätzliche Parameter

| Parameter | Beschreibung |
| ------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| -o | Name (und Typ) der Ausgabedatei. Bei .bin-Endung wird auch nur eine binäre Datei erstellt. |
| -c | Kein Linken des Quellcodes. |
| -O | Optimieren des Quellcodes. Grad kann von 0 – 3 angegeben werden. |
| -l | Bindet weitere Bibliotheken ein |
| -Wall | Aktiviert sinnvolle Warnungen. |
| -Werror | Behandelt alle Warnungen wie Fehler |
| -pedantic | Gibt alle Warnungen aus. |
| --mno-red-zone | Verhindert, dass bei x86_64 Systemen die [Red Zone](http://en.wikipedia.org/wiki/Red_zone_%28computing%29) direkt hinter dem Stack überschrieben wird. |
| -fno-tree-loop-distribute-patterns | Deaktiviert die automatische Erkennung, ob ein bestimmter Codeabschnitt durch eine libc-Funktion wie memcpy oder memset ersetzt werden kann. Sollte für die eigene memcpy-, memset-, …-Implementierung gesetzt werden (in der eigenen libc oder im Kernel), da sonst potentiell eine Endlosrekursion erzeugt wird. |

  
Alle Compiler-Flags könnt ihr nachlesen unter:

| Version | Link |
| --------- | ------------------------------------------------------------------- |
| 4.8.1 | <http://gcc.gnu.org/onlinedocs/gcc-4.8.1/gcc/Option-Summary.html> |

## Siehe auch

[Inline-Assembler mit GCC](https://github.com/lowlevel-eu/wiki/wiki/Inline-Assembler-mit-GCC "Inline-Assembler mit GCC")

## Weblinks

- [Website des GCC](http://gcc.gnu.org)
- [TDM's GCC/mingw32 Builds](http://www.tdragon.net/recentgcc/) (experimentelle Builds von GCC 4.x für Windows)
- [GCC Compiler-Flags](http://gcc.gnu.org/onlinedocs/gcc-3.3.6/gcc/i386-and-x86_002d64-Options.html)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/11130/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1805/index.html)

<!-- MediaWiki page 1805; revision 11130; parent 11129; 2013-07-28T12:30:24Z -->
