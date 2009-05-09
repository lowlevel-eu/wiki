# Global Descriptor Table

Der Global Descriptor Table (auch GDT) ist eine i386 spezifische Struktur, welche Informationen über Speicherabschnitte enthält.

Der Ort der GDT wird mit dem Befehl lgdt mitgeteilt.

## Struktur

Jeder Eintrag in den GDT besteht aus acht Bytes.

### Struktur eines Eintrages

| Byte | Name | Bits |
| ------ | ------------ | ------------------- |
| 0 | Limit | 0-7 |
| 1 | Limit | 8-15 |
| 2 | Base | 0-7 |
| 3 | Base | 8-15 |
| 4 | Base | 16-23 |
| 5 | Accessbyte | 0-7 (vollständig) |
| 6 | Flags | 0-3 (vollständig) |
| 6 | Limit | 16-19 |
| 7 | Base | 24-31 |

### Bedeutung

| Name | Bedeutung |
| ------------ | --------------------------------------------------------------------------------- |
| Limit | Größe des Segments - 1 (entweder in Bytes oder in 4KiB-Einheiten - siehe Flags) |
| Base | Die Addresse wo das Segment beginnt |
| Accessbyte | Zugriffsinformationen (Ring, executable, etc.) |
| Flags | Definiert die Segmentgrößeneinheit und 16/32 Bit. |

### Das Access-Byte

| Bit | Wert | Name | Bedeutung |
| -------- | ------ | ------------------------------ | --------------------------------------------------------------------------------------------- |
| 7 | 0x80 | present bit | Muss 1 für einen aktiven Eintrag sein |
| 6 u. 5 | 0x20 | Privilege | Ring - von Ring 0 (Kernel Mode) zu Ring 3 (User Mode) |
| 4 | 0x10 | 1 | Ist 1 |
| 3 | 0x08 | Executable bit | Bei 1 ist das Speichersegment ein Codesegment, bei 0 ein Datensegment |
| 2 | 0x04 | Direction bit/Conforming bit | Abhängig vom Executable bit |
| 1 | 0x02 | Readable bit/Writable bit | Bei einem Codesegment ob lesen erlaubt ist, bei einem Datensegment ob schreiben erlaubt ist |
| 0 | 0x01 | Accessed bit | Sollte 0 gesetzt werden, wird dann vom Prozessor bei Zugriff gesetzt. |

#### Beispielcode

    char Set_Accessbyte(char enable, char privilege, char code, char read_write){
        char Bitmaske = 0x00;
        /** enable geht von 0 bis 1
        0x01 ist in Bits 00000001b*/
        if (enable = 1){
            Bitmaske = (Bitmaske | 0x01);
        }
        /* privilege geht von 0 bis 3
        0x02 ist in Bits 00000010b
        0x04 ist in Bits 00000100b
        0x06 ist in Bits 00000110b*/
        if (privilege = 1) {
            Bitmaske = (Bitmaske | 0x02);
        }
        else if (privilege = 2){
            Bitmaske = (Bitmaske | 0x04);
        }
        else if(privilege = 3){
            Bitmaske = (Bitmaske | 0x06);
        }
        Bitmaske = (Bitmaske | 0x08);
        /* code 0 bis 1 */
        if (code = 1){
            Bitmaske = (Bitmaske | 0x0f);
        }
        /* read_write geht von 0 bis 1 */
        if (read_write = 1){
            Bitmaske = (Bitmaske | 0x40);
        }
        Return(Bitmaske);
    }

### Die Flags

| Bit | Wert | Name | Bedeutung |
| ----- | ------ | ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 3 | 0x8 | Granularity bit | Bei 0 wird als Einheit bei Limit ein Byte benutzt, bei 1 stattdessen 4 KiB |
| 2 | 0x4 | Size bit | 0 bedeuted 16 bit protected mode, bei 1 32 bit protected mode. |
| 1 | 0x2 | Long Mode bit | 0 bedeuted Protected Mode, 1 bedeutet Long Mode. Bei gesetztem Long Mode Bit **muss** das Size Bit 0 sein! Ist das Long Mode Bit 0, so gibt das Size Bit die Bit-Größe des Protected Mode Segments an. *Dieses Bit sollte nur bei einem Code Segment gesetzt werden, bei anderen Segment-Typen sollte es auf 0 gesetzt sein.* |
| 0 | 0x1 | Available Bit | Dieses Bit steht dem Programmierer zur freien Verfügung. |

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/4356/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1661/index.html)

<!-- MediaWiki page 1661; revision 4356; parent 3754; 2009-05-09T07:52:05Z -->
