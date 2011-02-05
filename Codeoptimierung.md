# Codeoptimierung

Durch die Optimierung des Quellcodes eines Programms kann dieses schneller, effektiver und platzsparender arbeiten.

## Allgemeines

### Datengrößen

- Die Wortgröße des Prozessors zu verwenden ist meist vorteilhaft. (32 Bit bei i386, 64 Bit bei x86-64).

### Alignment

- Code und Daten sollten in getrennten [Pages](https://github.com/lowlevel-eu/wiki/wiki/Paging "Paging") gehalten werden.
- Wenn man aber gezwungen ist, Code und Daten zu mischen, dann sollte man die Daten so legen, dass Sprünge nicht darüber hinweg springen müssen.
- Selbst modifizierender Code widerspricht diesem Prinzip.
- Sprungziele sollten am Anfang eines Paragrafs (16Byte) stehen.

<!-- -->

- Die CPU hat einen internen Datencache von 64KB.

Daten, die über eine 64KB Grenze verteilt sind, müssen dann zweimal gecacht werden, was die Performance mindert. Somit sollten Daten ihrer Größe entsprechen ausgerichtet werden, also z.B. DWORDs auch nur am Anfang der 4 Byte Grenzen.

- Ebenso sollte der [Stack](https://github.com/lowlevel-eu/wiki/wiki/Stack "Stack") 64KB aligned sein, und die Größe seiner Elemente gleich bleiben.

### Sprünge und Schleifen

Sprünge sind ein Problem für die CPU, weil sie das cachen des Codes erheblich erschweren.

- Sprünge sollten vermieden werden, wann immer dies möglich ist
- Unnötige Sprünge können vermieden werden, indem der wahrscheinlichere Zweig in einer Verzweigung (if/switch) zuerst ausgeführt wird.

Somit sind auch Schleifen performancekritisch, da in ihnen sehr oft gesprungen wird.

- Schleifen sollten, wenn möglich, aufgelöst werden.
- Bei verschachtelten Schleifen sollte diejenige innen stehen, die am längsten läuft.
- Wenn in einer Schleife dieselbe Berechnung immer wieder ausgeführt wird, dann kann diese auch einmalig vor der Schleife berechnet werden.

Auch Funktionsaufrufe fallen unter Sprünge.

- Funktionen, die nur wenig leisten, sollten vermieden und ihr Code direkt eingearbeitet werden (diesem Zweck dient das inline-Schlüsselwort in C, allerdings werden kurze Funktionen bei entsprechender Optimierung vom C-Compiler oft auch automatisch entsprechend behandelt)

### Caching

- Je weniger Sprünge, desto effektiver kann der Code gecacht werden.
- Die CPU kann bis zu 16 verschachtelte Funktionsaufrufe cachen, mehr als 16 Verschachtelungen verringern die Performance.
- Die CPU kann Befehle am besten cachen, die weniger als 8 Byte lang sind. Außerdem sollten dabei WORD-Konstanten vermieden werden. Komplexe Befehle wie sysenter oder leave
- Alignments sollten immer eingehalten werden!

## Assembler

### Reduzierung der Codegröße

Die nachfolgenden Tricks eignen sich besonders zum Programmieren in [Assembler](https://github.com/lowlevel-eu/wiki/wiki/Assembler "Assembler"), wie es z. B. im [Bootloader](https://github.com/lowlevel-eu/wiki/wiki/Bootloader "Bootloader") nötig ist.

| Beschreibung | Optimierter Code |
| ------------------------------------------------- | ------------------------------------------------------------------------------------- |
| Register 0 setzen | \<asm\>xor eax, eax\</asm\> |
| Prüfen, ob Register 0 ist | \<asm\>test eax, eax jz ...\</asm\><br> |
| Multiplikation mit einer Zweierpotenz | \<asm\>shl eax, log2 Faktor\</asm\> |
| Division durch eine Zweierpotenz | \<asm\>shr eax, log2 Divisor\</asm\> |
| Beliebige Multiplikation | \<asm\>imul eax, \[Faktor_1\], \[Faktor_2\]\</asm\> |
| Schleife | \<asm\>mov ecx, \[Anzahl_Wiederholungen\] von_vorne: ... loop von_vorne\</asm\><br> |
| Bedingte Wertzuweisung, Register | \<asm\>cmov?? eax, \[Wert\]\</asm\> |
| Bedingte Wertzuweisung, Byte im Arbeitsspeicher | \<asm\>set?? \[Wert\]\</asm\> |
| Addition, Subtraktion | \<asm\>lea eax, \[ebx + ecx + 4\]\</asm\> |
| Bestimmte Multiplikationen (z. B. mit 3 oder 5) | \<asm\>lea eax, \[edx \* 4 + edx\]\</asm\> |

### Steigerung der Effektivität

- Registerzugriffe sind immer schneller als Arbeitsspeicherzugriffe.
- Daher sollten Parameter an Funktionen über Register, nicht über den Stack übergeben werden.

#### PUSHA / POPA

- Von der Verwendung von pusha/popa ist meist abzuraten, da man auch jedes einzelne Register direkt pushen/popen kann, und dabei selektiver vorgehen kann.

## Hochsprachen

### Codeoptimierung durch Compiler

TODO

### Optimierungstools

*Bisher keine Vorschläge*

  

## siehe auch

- [Ausgabe 8](https://github.com/lowlevel-eu/wiki/wiki/Ausgabe-8#tipps--tricks "Ausgabe 8")

## Weblinks

- [Intel - Optimierung für IA32](http://www.intel.com/Assets/PDF/manual/248966.pdf) (Kapitel 3.3 bis 3.9 sind empfehlenswert)
- [AMD - Software Optimierung für AMD64](http://support.amd.com/us/Processor_TechDocs/25112.PDF)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/9462/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2187/index.html)

<!-- MediaWiki page 2187; revision 9462; parent 7118; 2011-02-05T23:46:35Z -->
