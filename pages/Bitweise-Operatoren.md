# Bitweise Operatoren

Bitweise Operatoren sind Operatoren die (Binär-)Zahlen Bit für Bit verarbeiten.

## Operatoren

### NOT

Der **NOT**-Operator ist ein unärer Operator, d. h. er arbeitet mit nur einem Argument. Seine Funktion ist es, einen Bit-String Bit für Bit umzudrehen (aus *1* wird *0* und aus *0* wird *1*). Bsp.:

    NOT ( 11011010b ) = 00100101b

[C](C.md "C")-Code: \<c\>int a = ~0xda; // a = 0x25\</c\>

[ASM](Assembler.md "Assembler")-Code: \<asm\>mov al, 11011010b not al  ; al = 00100101b\</asm\>

### AND

Der **AND**-Operator veknüpft zwei Bit-Strings miteinander über ein logisches *und*. Das Bit im Zielstring wird genau dann gesetzt, wenn die beiden entsprechenden Bits der Quellstrings *1* sind.

Bsp.:

    (11001100b AND 01100110b) = 01000100b

        11001100b
    AND 01100110b
    -------------
        01000100b

C-Code: \<c\>int a = (0xcc & 0x66); // a = 0x44\</c\>

ASM-Code: \<asm\>mov al, 11001100b and al, 01100110b  ; al = 01000100b\</asm\>

### OR

Der **OR**-Operator verknüpft zwei Bit-Strings über das logische *oder*. Im Zielstring wird das Bit gesetzt, wenn mindestens eines der beiden Bits der Quellstrings *1* ist.

Bsp.:

    (11001100b OR 01100110b) = 11101110b

        11001100b
    OR  01100110b
    -------------
        11101110b

C-Code: \<c\>int a = (0xcc \| 0x66); // a = 0xee\</c\>

ASM-Code: \<asm\>mov al, 11001100b or al, 01100110b  ; al = 1110111b\</asm\>

### XOR

Der **XOR**-Operator verknüpft zwei Bit-Strings über ein *e**x**klusives* logisches *oder*. Das Bit im Zielstring wird nur dann gesetzt, wenn genau eines der beiden entsprechenden Bits in den Quellstrings *1* ist.

Bsp.:

    (11001100b XOR 01100110b) = 10101010b

        11001100b
    XOR 01100110b
    -------------
        10101010b

C-Code: \<c\>int a = (0xcc ^ 0x66); // a = 0xaa\</c\>

ASM-Code \<asm\>mov al, 11001100b xor al, 01100110b  ; al = 10101010b\</asm\>

## Anwendung

Besonders bei hardwarenaher Programmierung kann man auf die Bit-Operatoren kaum verzichten. Sie sind nötig, da in [Hardware](https://lowlevel-eu.github.io/wiki/pages/1953/index.html "Hardware") einzelnen Bits oft dazu dienen einen Zustand der Hardware wiederzuspiegeln: Sie dienen als Flags. Da Software über die CPU aber immer nur auf Bytes zugreifen kann, und so den Zustand einzelner Bits nicht überprüfen kann verwendet man die Bit-Operatoren, um z. B. irrelevante Bits zu löschen oder bestimmte Bits zu setzen ohne den Zustand der anderen Bits zu beeinflussen.

### Bits löschen

Um bestimmte Bits in einem oder mehreren Bytes zu löschen wird eine (Bit-)Maske benötigt. Die Maske gibt an welche Bits gelöscht werden sollen. Angenommen du hast ein Byte, dessen 5. Bit unbedingt *0* sein muss, weil es für eine Hardware-Funktion steht, die du ausschalten willst. Du erstellst dir also eine Maske in der nur das 5. Bit gesetzt ist: 00100000b.

Um das Bit jetzt löschen zu können invertierst du die Maske zunächst mit NOT

    NOT(00100000b) = 11011111b

und Verknüpfst dein Byte per AND mit dem Resultat

    (????????b AND 11011111b) = ??0?????b

Das ganze funktioniert natürlich auch mit mehreren Bits gleichzeitig.

C-Code: \<c\>PORTx &= ~(1 \<\< BitNummer); // Bit in PORTx löschen\</c\>

### Bits setzen

Wie beim Löschen eines Bits wird auch hier eine (Bit-)Maske benötigt. Allerdings gibt sie diesmal an, welches Bit gesetzt werden soll. Um z. B. die Bits 1,4,5 auf *1* zu setzen erstellt man sich als Maske: 00110010b Im Gegensatz zum Löschen wird jetzt allerdings mit einem einfachen OR verknüpft.

    (????????b OR 00110010b) = ??11??1?b

C-Code: \<c\>PORTx \|= (1 \<\< BitNummer); // Bit in PORTx setzen \</c\>

### Bit testen

Oft muss man auch testen, ob ein Bit gesetzt ist, um z.B. zu erfahren, ob man aus einem Port lesen darf. Dafür löscht man einfach alle Bits, die nicht betrachtet werden sollen mithilfe der AND Verknüpfung. Ist das Resultat 0, dann war das betrachtete Bit gelöscht, andernfalls war es gesetzt.

    (????????b AND 00100000b) = 00?00000b

C-Code: \<c\>if (PORTx & (1 \<\< BitNummer) == 0) //bit gelöscht else //bit gesetzt

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/7835/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1757/index.html)

<!-- MediaWiki page 1757; revision 7835; parent 7428; 2010-07-13T15:26:32Z -->
