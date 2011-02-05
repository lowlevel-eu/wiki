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

Man unterscheidet bei Assembler grob zwischen Intel- und AT&T-Syntax. Zu den Assemblern, deren Syntax auf der Intel-Syntax aufbaut, gehören [FASM](https://github.com/lowlevel-eu/wiki/wiki/Flat-Assembler "FASM"), [NASM](https://github.com/lowlevel-eu/wiki/wiki/Netwide-Assembler "NASM"), MASM, TASM und YASM. Die AT&T-Syntax kann von dem GNU Assembler, der in den binutils enthalten ist, und YASM verarbeitet werden.

#### Intel-Syntax

Zu den Hauptmerkmalen der Intel-Syntax gehört die Reihenfolge der Operanden, bei Befehlen mit zwei Operanden oder mehr. Das Ziel einer derartigen Operation steht immer als erstes in der Operandenliste. Die Addition von eax zu ebx sieht dann z. B. so aus, wobei das Ergebnis in ebx ist: \<asm\>add ebx, eax\</asm\>

#### AT&T-Syntax

In der AT&T-Syntax werden die Register mit einem % als Präfix versehen, und der Zieloperand ist der letzte Operand. Das Beispiel von eben sieht dann so aus: \<asm\>add %eax, %ebx\</asm\>

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

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/9452/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1514/index.html)

<!-- MediaWiki page 1514; revision 9452; parent 8143; 2011-02-05T14:20:00Z -->
