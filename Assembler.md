# Assembler

Als Assembler wird sowohl die Assemblersprache, als auch das Programm zur Übersetzung von Quelltexten in Assemblersprache in Maschinensprache bezeichnet. Die CPU führt ausschließlich Maschinenbefehle aus, die als Folge von Bytes im Speicher vorliegen. Jedem Maschinenbefehl ist genau ein Assemblerbefehl (Mnemonic) zugeordnet. Diese 1:1-Abbildung auf die CPU-Befehle hat zur Folge, dass in der Regel Assemblerprogramme nicht zwischen verschiedenen Prozessortypen übertragbar sind. Außerdem werden in Assembler geschriebene Programme schnell sehr lang und erfordern, dass der Programmierer sich wenig zielführend mit vielen Details der Architektur auseinandersetzen muss.

Der sinnvolle Einsatz von Assembler beschränkt sich darauf, eine Umgebung für eine Hochsprache aufzubauen, sowie kurze, plattformabhängige Hilfsfunktionen und Einsprungsstellen für z. B. [Interrupt-Behandlungsroutinen](https://github.com/lowlevel-eu/wiki/wiki/Interrupt-Service-Routine "ISR") bereitzustellen.

## Aufgaben eines Assemblers

- Übersetzung von Assembler in Maschinencode
- Auflösen der symbolischen Namen (z. B. von Labels) in numerische Konstanten, soweit möglich
- Erzeugung von Objektcode, der in der Regel noch [gelinkt](https://github.com/lowlevel-eu/wiki/wiki/Linker "Linker") werden muss

## Aufbau von Assemblerbefehlen

Die direkte Abbildung von Assemblerbefehlen auf Maschinenbefehle hat zur Folge, dass Assemblerbefehle immer den selben Aufbau haben. Ein Maschinenbefehl besteht aus einem Opcode, meist gefolgt von einem oder mehreren Operanden. Dieses spiegelt sich auch in Assemblerbefehlen wieder, die immer den gleichen Aufbau haben:

    mnemonic operand1, operand2

Bei der x86-Architektur ist bei zweistelligen Operationen (Addition, Subtraktion, bitweise Operationen, etc.), immer einer der beiden Operanden sowohl Quelle als auch Ziel. Es existiert also z. B. ein Befehl, um das Register eax zu ebx zu addieren, und das Ergebnis in ebx zu speichern. Aber es existiert kein Befehl, um das Ergebnis in einem dritten Register zu speichern.

### Syntax

Bei Assembler unterscheidet man verschiedene Syntax. Bei der x86-CPU-Familie unterscheidend man zwischen Intel- und AT&T-Syntax. Zu den Assemblern, deren Syntax auf der Intel-Syntax aufbaut, gehören [FASM](https://github.com/lowlevel-eu/wiki/wiki/Flat-Assembler "FASM"), [NASM](https://github.com/lowlevel-eu/wiki/wiki/Netwide-Assembler "NASM"), MASM und TASM. Die AT&T-Syntax kann von dem GNU Assembler, der in den binutils enthalten ist, und anderen Unix-Assemblern ("as") verarbeitet werden. YASM und neuere Versionen des GNU Assemblers können zwischen beiden Syntax umschalten. Die Programme in den binutils können aber mit beiden Syntax-Varianten souverän umgehen, ebenfalls kann der gcc beides ausgeben.

#### Intel-Syntax

Als Intel-Syntax bezeichnet man diejenigen Syntax Formen, die von der Syntax des alten Assemblers ASM86 von der Firma Intel abgeleitet worden sind. Zu den Hauptmerkmalen der Intel-Syntax gehört die Reihenfolge der Operanden, bei Befehlen mit zwei Operanden oder mehr. Das Ziel einer derartigen Operation steht immer als erstes in der Operandenliste. Die Addition von eax zu ebx sieht dann z. B. so aus, wobei das Ergebnis in ebx ist: \<asm\>add ebx, eax\</asm\>

Kommentare werden in der Intel-Syntax mit einem Semikolon eingeleitet: \<asm\>; Das ist ein Kommentar.\</asm\>

Darüber hinaus wird die Wortlänge anhand der Registerbezeichnung bestimmt. Speicherzugriffe werden mit eckigen Klammern angedeutet. \<asm\>mov ax, \[ebp\] ; lädt ein word (2 Byte Zahl) von der Adresse in ebp nach ax\</asm\> \<asm\>mov cl, \[esi\] ; lädt ein Byte von der Adresse in esi nach cl\</asm\>

Wenn die Wortlänge nicht eindeutig feststellbar ist, muss sie angegeben werden: \<asm\>push dword ptr \[ebp + 4\] ; schiebt ein dword (4 Byte Zahl) von der Adresse, welche um 4 größer ist als die in ebp, auf den Stack\</asm\>

Alle Bestandteile der Adresse werden in der Klammer angegeben, werden die Klammern Weggelassen wir eine Konstante oder der Registerinhalt verwendet: \<asm\>add dh, \[ebp + eax\*4 + 5\] ; addiert dh mit den Byte, dessen Adresse sich durch ebp + eax\*4 + 5 berechnen lässt und speichert das Ergebnis wieder in dh ab\</asm\> \<asm\>sub ecx, 16 ; verringert den Wert in ecx um 16\</asm\> \<asm\>or ecx, eax ; ecx = Wert in ecx OR Wert in eax\</asm\>

Allerdings wird die Zuordnung Adresse = eckige Klammer in einigen Assembler nicht konsequent verwendet, so das man Aufpassen muss.

#### AT&T-Syntax

Der AT&T-Syntax leitet sich von derjenigen Syntax ab, die der Unix Assembler (as) für verschiedene Prozessorplattformen verwendet. Auf der x86-Plattform ist sie zwar weniger verbreitet, allerdings arbeitet die GNU Implementierung der Unix-Werkzeuge (gcc, gdb, ...) vorwiegend damit. In der AT&T-Syntax werden die Register mit einem % als Präfix versehen und der Zieloperand ist der letzte Operand. Das Beispiel von eben sieht dann so aus: \<asm\>add %eax, %ebx\</asm\>

Kommentare werden im AT&T-Syntax mit einem Doppelkreuz eingeleitet: \<asm\># Das ist ein Kommentar.\</asm\>

Die Wortlänge wird als Suffix an den Opcode angehängt, "b" steht für Byte, "w" für Word (2 Byte), "l" für DWord (4 Byte) und "q" für QWord (8 Byte). Die Wortlänge kann aber weggelassen werden, wenn die Länge aus den Registernamen hervorgeht. Register als Addresszeiger verwendet, werden sie eingeklammert. \<asm\>movw (%ebp), ax \# lädt ein Word (2 Byte Zahl) von der Adresse in ebp nach eax\</asm\> \<asm\>movb (%esi), cl \# lädt ein Byte von der Adresse in esi nach cl\</asm\> \<asm\>pushl 4(%ebp) \# schiebt ein dword (4 Byte Zahl) von der Adresse, welche um 4 größer ist als die in ebp, auf den Stack. S.u.\</asm\>

Die Bezeichnung von Addressen ist allerdings komplizierter. Sie werden wie folgt dargestellt (wobei alle Bestandteile Optional sind.):

    <Address Basis>(<Erstes Register das Addiert werden soll>,<Zweites Register>,<Faktor mit dem das zweite Register zuvor Multipliziert wird>)

Also z.B. \<asm\>addb 5(ebp,eax,4), dh \# addiert dh mit den Byte, dessen Adresse sich durch ebp + eax\*4 + 5 berechnen lässt\</asm\> \<asm\>addb 12345, dh \# addiert dh mit den Byte von der Adresse 12345 und speichert das Ergebnis wieder in dh ab\</asm\>

Konstanten wird ein Dollarzeichen vorgestellt, um sie von Addressen zu unterscheiden. \<asm\>subl \$16, ecx \# Verringert den Wert in ecx um 16\</asm\>

## Inline-Assembler

Als Inline-Assembler bezeichnet man die Einbettung von Assemblerbefehlen im Quelltext eines Hochsprachenprogramms. Dieses erweist sich als nützlich, wenn man nicht den Umweg über einen Funktionsaufruf gehen will, um Assemblercode auszuführen. Siehe auch [Inline-Assembler mit GCC](https://github.com/lowlevel-eu/wiki/wiki/Inline-Assembler-mit-GCC "Inline-Assembler mit GCC").

## Weblinks

### Assembler

- [NASM (Netwide Assembler)](http://www.nasm.us/)
- [MASM (Microsoft Macro Assembler)](http://msdn.microsoft.com/en-us/library/afzk3475.aspx)
- [FASM (Flat Assembler)](http://www.flatassembler.net/)
- [YASM](http://www.tortall.net/projects/yasm/)
- [GAS (GNU Assembler)](http://sourceware.org/binutils/docs-2.19/as/GNU-Assembler.html)

### Befehlsübersichten

- [Intel Manual Volume 2A/B: Instruction Set Reference](http://www.intel.com/products/processor/manuals/)
- [AMD Manual Volume 3: General-Purpose and System Instructions](http://www.amd.com/us-en/Processors/DevelopWithAMD/0,,30_2252_875_7044,00.html)
- [ASM86FAQ](http://www.pbhq.de/asm86faq/) (10 Jahre alt, aber auf Deutsch)
- [i8086.de](http://www.i8086.de)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/10215/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1514/index.html)

<!-- MediaWiki page 1514; revision 10215; parent 10213; 2011-11-11T16:57:18Z -->
