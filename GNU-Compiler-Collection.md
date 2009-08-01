# GNU Compiler Collection

| Allgemeines |  |
| --------------- | ----------------------------------------------- |
| Name: | GNU Compiler Collection |
| Entwickler: | [Das GCC-Team](http://gcc.gnu.org/about.html) |
| Akt. Version: | 4.4.1 |
| Lizenz: | GNU GPL |
| Plattform: | Linux, Unix<br>(inoffiziell: Windows) |
| Homepage |  |

[gcc.gnu.org](http://gcc.gnu.org/)

  
Die **GNU Compiler Collection** ist eine Sammlung von Compilern. Unterstützt werden die Sprachen C, C++, Java, Objective-C, Fortran 95, Treelang und Ada und demnächst auch D. Zusätzlich werden die Plattformen x86, AMD64 (x86_64), Alpha, Arm, IA-64, PowerPC und viele weitere unterstützt.

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

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/5015/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1805/index.html)

<!-- MediaWiki page 1805; revision 5015; parent 4753; 2009-08-01T18:54:41Z -->
