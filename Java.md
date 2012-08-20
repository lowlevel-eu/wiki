# Java

| Allgemeines |  |
| -------------------------------- | ------------------------------------------------------------------------------------ |
| Name: | Java |
| Inlineassembler: | Nein |
| Compiler: | JDK, [GCC](https://github.com/lowlevel-eu/wiki/wiki/GNU-Compiler-Collection "GCC") |
| Spracheneigenschaften |  |
| Plattformen: | Alle |
| Beispielkernel in der Sprache: | \- |
| Homepage |  |

[JavaSE](http://www.oracle.com/technetwork/java/javase/overview/index.html)

Java ist eine objektorientierte [Programmiersprache](https://lowlevel-eu.github.io/wiki/pages/1648/index.html "Kategorie:Programmiersprache"), die von Sun Microsystems entwickelt wurde (seit dem Aufkauf von Sun durch Oracle 2010 wird Java von Oracle weiterentwickelt).

Java zeichnet sich insbesondere dadurch aus, dass Java - Compiler keine Maschinensprache erzeugen (abgesehen von dem Java - Compiler GCJ aus der [GNU Compiler Collection](https://github.com/lowlevel-eu/wiki/wiki/GNU-Compiler-Collection "GNU Compiler Collection") und einigen weiteren, die das durchaus beherrschen), sondern sogenannten Bytecode, der nicht direkt vom Prozessor ausgeführt wird, sondern vom **Java Runtime Environment** (JRE).

Diese Abstraktion ermöglicht eine Plattformunabhängigkeit sogar ohne erneute Kompilation des Quellcodes (im Gegensatz z. B. zu [C](https://github.com/lowlevel-eu/wiki/wiki/C "C")), sofern Java auf der Zielplattform installiert ist.

Das ist auch einer der größten Nachteile von typischen Bytecode - Java - Programmen, da man erst das JRE installieren muss, bevor man das Programm starten kann. Außerdem bieten nativ kompilierte Programme einen deutlichen Geschwindigkeitsvorteil, weil die JRE noch den Bytecode in Maschinensprache umsetzen muss, was bei ELF - oder .exe - Dateien nicht der Fall ist.

  

## Geschichte

An dieser Stelle möchte ich auf den umfangreichen Wikipedia - Artikel verweisen:

[Entstehung der Programmiersprache Java](http://de.wikipedia.org/wiki/Java_%28Technik%29#Geschichte)

## Kernelprogrammierung mit Java

Wie oben bereits erwähnt, gibt es durchaus auch Java - Compiler, die keinen Bytecode, sondern normalen Maschinencode erzeugen können, z. B. Excelsior JET und der GNU Compiler for Java (GCJ). Dadurch ist es zumindest theoretisch möglich, einen [Kernel](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel") in Java zu implementieren.

Praktisch ist das jedoch nur mit relativ hohem Programmieraufwand möglich. Denn Java unterstützt weder Zeiger noch Inline - [Assembler](https://github.com/lowlevel-eu/wiki/wiki/Assembler "Assembler"), weshalb man direkte [Hardwarezugriffe](https://lowlevel-eu.github.io/wiki/pages/1447/index.html "Kategorie:Hardware") in externen Funktionen implementieren müsste, die dann beim Linken eingebunden werden können.

Beispielsweise bräuchte man eine Java - Datei, die den Kernel enthält, eine C - Datei, in der grundlegende Funktionen zum Hardwarezugriff implementiert sind (z. B. eine Funktion, die den Wert der angegebenen Speicheradresse zurückgibt bzw. ändert) und eventuell noch eine Assembler - Datei, sofern nicht bereits bei den C - Funktionen Inline - Assembler verwendet wurde.

### Beispielkernel in Java

TODO...

## bekannte Projekte

Ein Betriebssystem, das auf Java basiert, nennt sich JOS (Java Operating System) und ist unter [\[1\]](http://jos.sourceforge.net/) zu finden.

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/10702/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2585/index.html)

<!-- MediaWiki page 2585; revision 10702; parent 10685; 2012-08-20T10:19:52Z -->
