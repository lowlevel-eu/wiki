# Local Advanced Programmable Interrupt Controller

Die **LAPIC** oder **Local APIC** (= **Local Advanced Programmable Interrupt Controller**) nimmt [Interrupts](https://github.com/lowlevel-eu/wiki/wiki/Interrupt "Interrupt") von der [I/O APIC](https://github.com/lowlevel-eu/wiki/wiki/I-O-Advanced-Programmable-Interrupt-Controller "I/O APIC") (oder auch von der [PIC](https://github.com/lowlevel-eu/wiki/wiki/Programmable-Interrupt-Controller "PIC")) und anderen prozessorinternen Einheiten an und leitet diese an den Prozessorkern zum Abarbeiten weiter. Außerdem ist es nur über die LAPIC möglich [IPIs](https://github.com/lowlevel-eu/wiki/wiki/Interprocessor-Interrupt "IPI") zu senden und zu empfangen.

## Register

### Aufbau

Die Register der *Local APIC* sind in den physischen Speicher eingeblendet. Jedes der Register beginnt an einer 16 Byte Grenze, erstreckt sich aber nur über die ersten 32 Bit. Falls das Register größer als 32 Bit ist, befinden sich die nächst höheren 32 Bit an der nächst höheren 16 Byte Grenze. Die *Local APIC* stellt folgende Register zur Programmierung bereit:

  

| Offset | r/w | Größe (Bit) | Abkürzung | Name des Registers |
| ------------------ | ----- | ------------- | ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0x0020 | r/w | 32 |  | [Local APIC ID Register](https://github.com/lowlevel-eu/wiki/wiki/Local-Advanced-Programmable-Interrupt-Controller#local-apic-id-register "LAPIC") |
| 0x0030 | r | 32 |  | [Local APIC Version Register](https://github.com/lowlevel-eu/wiki/wiki/Local-Advanced-Programmable-Interrupt-Controller#local-apic-version-register "LAPIC") |
| 0x0080 | r/w | 32 | TPR | Task Priority Register |
| 0x0090 | r | 32 | APR | Arbitration Priority Register ¹ |
| 0x00A0 | r | 32 | PPR | Processor Priority Register |
| 0x00B0 | w | 32 |  | EOI Register |
| 0x00D0 | r/w | 32 |  | Logical Destination Register |
| 0x00E0 | r/w | 32 |  | Destination Format Register |
| 0x00F0 | r/w | 32 |  | Spurious Interrupt Vector Register |
| 0x0100<br>0x0170 | r | 256 | ISR | In-Service Register |
| 0x0180<br>0x01F0 | r | 256 | TMR | Trigger Mode Register |
| 0x0200<br>0x0270 | r | 256 | IRR | Interrupt Request Register |
| 0x0280 | r | 32 |  | Error Status Register |
| 0x0300<br>0x0310 | r/w | 64 | ICR | [Interrupt Command Register](https://github.com/lowlevel-eu/wiki/wiki/Local-Advanced-Programmable-Interrupt-Controller "LAPIC") |
| 0x0320 | r/w | 32 |  | LVT Timer Register |
| 0x0330 | r/w | 32 |  | LVT Thermal Sensor Register ² |
| 0x0340 | r/w | 32 |  | LVT Performance Monitoring Counters Register ³ |
| 0x0350 | r/w | 32 |  | LVT LINT0 Register |
| 0x0360 | r/w | 32 |  | LVT LINT1 Register |
| 0x0370 | r/w | 32 |  | LVT Error Register |
| 0x0380 | r/w | 32 |  | Initial Count Register |
| 0x0390 | r/w | 32 |  | Current Count Register |
| 0x03E0 | r/w | 32 |  | Divide Configuration Register |

  
¹ Nicht unterstützt in Pentium 4 und Intel Xeon Prozessoren  
² Eingeführt mit dem Pentium 4 und Intel Xeon Prozessoren. Dieses Register ist implementationsabhängig und muss in Zukunft nicht mehr vorhanden sein.  
³ Eingeführt mit dem Pentium Pro Prozessor. Dieses Register ist implementationsabhängig und muss in Zukunft nicht mehr vorhanden sein.  

### Local APIC ID Register

P6-Prozessorfamilie und Pentium-Prozessoren:

| 31-28 | 27-24 | 23-0 |
| ------------ | --------------- | ------------ |
| Reserviert | Local APIC ID | Reserviert |

Pentium4, IntelXeon und spätere Prozessoren:

| 31-24 | 23-0 |
| --------------- | ------------ |
| Local APIC ID | Reserviert |

  

### Local APIC Version Register

| 31-24 | 23-16 | 15-8 | 7-0 |
| ------------ | ------------------- | ------------ | --------- |
| Reserviert | Max. LVT-Einträge | Reserviert | Version |

Wenn beim Version-Byte das HighNibble 1 ist, ist es ein Local APIC. Andernfalls ein externer APIC. Bei Pentium 4 und Intel Xeon wird als LocalApic 0x14 zurückgegeben. Bei einem externen APIC entspricht das LowNibble X dem Chip 82489DX.

Das Feld "Max. LVT-Einträge" gibt die Anzahl an maximalen LVT-Einträgen minus 1 an. Das Feld muss bei Pentium 4 und Intel Xeon also auf 5 gesetzt sein, da es maximal 6 LVT-Einträge gibt. Bei der P6-Familie gibt es maximal 5 LVT-Einträge. Pentium-Prozessoren haben nur 4 LVT-Einträge.  

### Interrupt Command Register (ICR)

Das Interrupt Command Register wird verwendet um IPIs zu versenden.

| Bits | Beschreibung |
| ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 63-56 | Destination Field |
| 55-20 | Reserviert |
| 19-18 | Destination Shorthand<br>00b = No shorthand<br>01b = Self<br>10b = All Including Self<br>11b = All excluding Selg |
| 17-16 | Reserviert |
| 15 | Trigger Mode<br>0b = Edge<br>1b = Level |
| 14 | Level<br>0b = De-Assert<br>1b = Assert |
| 13 | Reserviert |
| 12 | Delivery Status<br>0b = Idle<br>1b = Send Pending |
| 11 | Destination Mode<br>0b = Physical<br>1b = Logical |
| 10-8 | Delivery Mode<br>000b = Fixed<br>001b = Lowest Priority<br>010b = SMI<br>011b = Reserviert<br>100b = NMI<br>101b = INIT<br>110b = Startup<br>111b = Reserviert |
| 7-0 | Vector |

## Programmierung

### physische Adresse

Die physische Adresse der Register kann entweder aus der [Configuration Table](https://github.com/lowlevel-eu/wiki/wiki/Symmetrisches-Multiprozessorsystem#configuration-table "SMP") der *Intel Multiprocessor Specification* ausgelesen werden oder über das [MSR](https://github.com/lowlevel-eu/wiki/wiki/Machine-Specific-Register "MSR") 0x001B ausgelesen werden.

### Initialisierung

In folgender Reihenfolge sollten die Register der Local APIC initialisiert werden:

- *Task Priority Register*
- *LVT Timer Register*
- *LVT Thermal Sensor Register*
- *LVT Performance Counter Register*
- *LVT LINT0 Register*
- *LVT LINT1 Register*
- *LVT Error Register*
- *Spurious Interrupt Vector Register*

### End of Interrupt

Ein *End of Interrupt* (EOI) wird der *Local APIC* signalisiert, in dem man in das *EOI Register* den Wert 0 schreibt.

## Weblinks

- [Intel® 64 and IA-32 Architectures Software Developer's Manual Volume 3A: System Programming Guide](http://www.intel.com/products/processor/manuals/index.htm) (Kapitel 8)
- [AMD64 Architecture Programmer's Manual Volume 2: System Programming](http://www.amd.com/us-en/Processors/DevelopWithAMD/0,,30_2252_739_7044,00.html) (Kapitel 16)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/2479/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1581/index.html)

<!-- MediaWiki page 1581; revision 2479; parent 2477; 2007-12-23T17:08:16Z -->
