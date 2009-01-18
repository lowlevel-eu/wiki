# GNU Compiler Collection

Die **Gnu Compiler Collection** ist eine Sammlung von Compilern. Unterstützt werden die Sprachen C, C++, Java, Objective-C, Fortran 95, Treelang und Ada und demnächst auch D. Zusätzlich werden die Plattformen x86, AMD64 (x86_64), Alpha, Arm, IA-64, PowerPC und viele weitere unterstützt.

## GCC unter Windows

Die GCC wird nicht direkt unterstützt, sondern nur durch die Portierung MinGW.

## GCC unter Linux

Die GCC gehört zum Standardumfang jeder Linuxdistrubition. Aufgerufen wird sie im Terminal mit den Befehle *gcc \[Kompilierte Datei\]*.

## Zusätzliche Parameter

| Parameter | Beschreibung |
| ----------- | -------------------------------------------------------------------------------------------- |
| -o | Name (und Typ) der Ausgabedatei. Bei .bin-Endung wird auch nur eine binäre Datei erstellt. |
| -c | Kein Linken des Quellcodes. |
| -O | Optimieren des Quellcodes. Grad kann von 1 - 3 angegeben werden. |
| -l | Bindet weiter Bibliotheken ein |
| -Wall | Aktiviert sinnvolle Warnungen. |
| -pedantic | Gibt alle Warnungen aus. |

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/3893/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1805/index.html)

<!-- MediaWiki page 1805; revision 3893; parent 3889; 2009-01-18T15:24:31Z -->
