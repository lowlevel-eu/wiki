# Global Descriptor Table

Der Global Descriptor Table (auch GDT) ist eine i386 spezifische Struktur, welche Informationen über Speicherabschnitte (Segmente) enthält.

Der Ort der GDT wird mit dem Befehl lgdt mitgeteilt.

## Segmentierung

### Real Mode

Der 8086 war ein 16-Bit-Prozessor. Das bedeutet, dass seine Register 16 Bit breit waren und somit Werte bis 2^16 - 1 = 65535 aufnehmen konnten. Nun müssen aber auch Zeiger in dieser Register passen und 64 Kilobytes sind nicht gerade ein großzügiger Adressraum.

Aus diesem Grund wurde im Real Mode eine einfache Art von Segmentierung eingeführt. Zu jedem Speicherzugriff wird noch eine Basisadresse addiert, die durch den Inhalt des entsprechenden Segmentregisters (cs für Code, ds für Daten, ss für den Stack) bestimmt ist. Dadurch wurden 20 Bit (also 1 Megabyte) zugänglich gemacht, wobei beim Zugriff auf mehr als 64 Kilobytes das Segmentregister gewechselt werden musste.

Die Berechnung einer effektiven Adresse - im Beispiel ein Zugriff auf \[ds:ax\] - läuft wie folgt ab:

    0x  1234   Adresse in ax
    0x 4321    Segmentregister ds 
    ========
    0x 44444   Tatsächlich zugegriffene Adresse

### Protected Mode

Auch im Protected Mode des 386 sind Segmente noch vorhanden, sie spielen aber eine etwas andere Rolle. Ihre alte Aufgabe haben sie zumindest teilweise verloren, denn der 386 ist ein 32-Bit-Prozessor und könnte die verfügbaren 4 GB Speicher ohne Segmentierung ansprechen.

Zum einen kann die Basisadresse aber auch weiterhin nützlich sein - sie erlaubt es, Code an beliebigen Stellen im Speicher auszuführen, auch wenn er von festen Adressen ausgeht (dieser Mechanismus wird aber nur selten benutzt). Zum anderen sind die Segmente erweitert worden, so dass sie nicht nur einfach aus einer Basisadresse bestehen, sondern zusätzliche Speicherschutzfunktionalität bieten wie Schreibschutz oder Zugriff erst ab einem bestimmten Privileglevel. Außerdem hat ein Segment nicht mehr eine starre Länge von 64 Kilobytes, sondern die Länge kann vom Betriebssystem für jedes Segment einzeln festgelegt werden.

Die Segmentregister sind aber nach wie vor nur 16 Bit breit und somit wird der Platz etwas knapp für diese ganzen Informationen. Aus diesem Grund enthalten die Segmentregister im Protected Mode nur noch sogenannte Selektoren, d.h. die Nummer eines Segments und einige wenige Flags. Die eigentliche Beschreibung der Segmente liegt in Form einer Tabelle im Speicher, der GDT. Die GDT besteht aus mehreren Einträgen (Segmentdeskriptoren) zu je 64 Bit, die direkt hintereinander liegen. Der erste Eintrag kann nicht benutzt werden, er ist der sogenannte Nulldeskriptor.

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

### Die Flags

| Bit | Wert | Name | Bedeutung |
| ----- | ------ | ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 3 | 0x8 | Granularity bit | Bei 0 wird als Einheit bei Limit ein Byte benutzt, bei 1 stattdessen 4 KiB |
| 2 | 0x4 | Size bit | 0 bedeuted 16 bit protected mode, bei 1 32 bit protected mode. |
| 1 | 0x2 | Long Mode bit | 0 bedeuted Protected Mode, 1 bedeutet Long Mode. Bei gesetztem Long Mode Bit **muss** das Size Bit 0 sein! Ist das Long Mode Bit 0, so gibt das Size Bit die Bit-Größe des Protected Mode Segments an. *Dieses Bit sollte nur bei einem Code Segment gesetzt werden, bei anderen Segment-Typen sollte es auf 0 gesetzt sein.* |
| 0 | 0x1 | Available Bit | Dieses Bit steht dem Programmierer zur freien Verfügung. |

## Laden der GDT

Nachdem der Kernel eine GDT im Speicher liegen hat, die er für seine Segmente verwenden möchte, muss er das Register GDTR ändern. Dieses Register enthält die Adresse und Länge der GDT und wird über den Befehl **lgdt** geladen. Da das Register 6 Bytes breit ist, kann dieser Befehl den neuen Wert nicht direkt als Operand entgegennehmen, sondern erwartet einen Pointer auf eine Speicherstelle, die diese 6 Bytes enthält:

\<c\>static long long unsigned int gdt\[GDT_ENTRIES\];

// ...

struct {

       unsigned short int length;
       void* pointer;

} \_\_attribute\_\_((packed)) gdtp = {

       .length = GDT_ENTRIES * 8,
       .pointer = gdt,

}; asm volatile("lgdt %0" : : "m" (gdtp));\</c\>

Dadurch wird allerdings nur der Verweis auf die Tabelle geändert, tatsächliche Auswirkungen hat die Änderung noch nicht. Auf die Tabelle wird nur zugegriffen, wenn ein Segmentregister neu geladen wird. Daher müssen jetzt noch alle Segmentregister neu geladen werden:

\<asm\> mov \$0x10, %eax mov %eax, %ds mov %eax, %es mov %eax, %ss ljmp \$0x8, \$.1 .1: \</asm\>

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/4360/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1661/index.html)

<!-- MediaWiki page 1661; revision 4360; parent 4359; 2009-05-09T09:36:58Z -->
