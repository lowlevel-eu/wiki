# Java

Diese Seite ist ein Artikel, welcher **mehr** haben könnte..  

Wenn du mehr darüber weißt oder recherchieren willst, bist **du** aufgerufen, dies zu tun. Wenn du dir in einer Sache nicht sicher bist, dann stell es auf die Diskussionsseite.

| Allgemeines |  |
| -------------------------------- | ------------------------------------------------------------------------------------ |
| Name: | Java |
| Inlineassembler: | Nein |
| Compiler: | JDK, [GCC](GNU-Compiler-Collection.md "GCC") |
| Spracheneigenschaften |  |
| Plattformen: | Alle |
| Beispielkernel in der Sprache: | \- |
| Homepage |  |

[JavaSE](http://www.oracle.com/technetwork/java/javase/overview/index.html)

Java ist eine objektorientierte [Programmiersprache](Kategorie-Programmiersprache.md "Kategorie:Programmiersprache"), die von Sun Microsystems entwickelt wurde (seit dem Aufkauf von Sun durch Oracle 2010 wird Java von Oracle weiterentwickelt).

Java zeichnet sich insbesondere dadurch aus, dass Java-Compiler keine Maschinensprache erzeugen (abgesehen von dem Compiler GCJ aus der [GNU Compiler Collection](GNU-Compiler-Collection.md "GNU Compiler Collection") und einigen weiteren, die das durchaus beherrschen), sondern sogenannten Bytecode, der nicht direkt vom Prozessor ausgeführt wird, sondern vom **Java Runtime Environment** (JRE).

Diese Abstraktion ermöglicht eine Plattformunabhängigkeit sogar ohne erneute Kompilation des Quellcodes (im Gegensatz z. B. zu [C](C.md "C")), sofern Java auf der Zielplattform installiert ist.

Das ist auch einer der größten Nachteile von typischen Bytecode-Java-Programmen, da man erst das JRE installieren muss, bevor man das Programm starten kann. Außerdem bieten nativ kompilierte Programme einen deutlichen Geschwindigkeitsvorteil, weil die JRE noch den Bytecode in Maschinensprache umsetzen muss, was bei ELF- oder .exe-Dateien nicht der Fall ist.

## Kernelprogrammierung mit Java

Wie oben bereits erwähnt, gibt es durchaus auch Java-Compiler, die keinen Bytecode, sondern normalen Maschinencode erzeugen können, z. B. Excelsior JET und der GNU Compiler for Java (GCJ). Dadurch ist es zumindest theoretisch möglich, einen [Kernel](Kernel.md "Kernel") in Java zu implementieren.

Praktisch ist das jedoch nur mit relativ hohem Programmieraufwand möglich. Denn Java unterstützt weder Zeiger noch Assembler, weshalb man direkte [Hardwarezugriffe](Kategorie-Hardware.md "Kategorie:Hardware") in externen Funktionen implementieren müsste, die dann beim Linken eingebunden werden können.

Beispielsweise bräuchte man eine Java-Datei, die den Kernel enthält, eine C-Datei, in der grundlegende Funktionen zum Hardwarezugriff implementiert sind (z. B. eine Funktion, die den Wert der angegebenen Speicheradresse zurückgibt bzw. ändert) oder eine Assembler-Datei, sofern nicht bei den C-Funktionen Inline-Assembler verwendet wurde.

### Beispielkernel in Java

TODO...

## Bekannte Projekte

Ein Betriebssystem, das auf Java basiert, nennt sich JOS (Java Operating System) und ist unter [sourceforge.net](http://jos.sourceforge.net/) zu finden.

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/10762/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2585/index.html)

<!-- MediaWiki page 2585; revision 10762; parent 10750; 2012-08-28T10:58:31Z -->
