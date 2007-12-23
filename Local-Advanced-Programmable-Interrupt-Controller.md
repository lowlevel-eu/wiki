# Local Advanced Programmable Interrupt Controller

Die **LAPIC** oder **Local APIC** (= **Local Advanced Programmable Interrupt Controller**) nimmt [Interrupts](https://github.com/lowlevel-eu/wiki/wiki/Interrupt "Interrupt") von der [I/O APIC](https://github.com/lowlevel-eu/wiki/wiki/I-O-Advanced-Programmable-Interrupt-Controller "I/O APIC") (oder auch von der [PIC](https://github.com/lowlevel-eu/wiki/wiki/Programmable-Interrupt-Controller "PIC")) und anderen prozessorinternen Einheiten an und leitet diese an den Prozessorkern zum Abarbeiten weiter. Außerdem ist es nur über die LAPIC möglich [IPIs](https://github.com/lowlevel-eu/wiki/wiki/Interprocessor-Interrupt "IPI") zu senden und zu empfangen.

## Register

Die Register liegen normalerweise an der Adresse 0xFEE00000, es ist allerdings sicherer diesen Wert z.B aus dem MP-Header zu entnehmen. Außerdem können sie auch umplatziert werden. Alle Register sind 32bit groß und sind 128bit-aligned.

| Offset | Name |
| -------- | ------------------------------------------------------------- |
| 0x20 | [Local APIC ID Register](#local-apic-id-register) |
| 0x30 | [Local APIC Version Register](#local-apic-version-register) |
| 0x80 | Task Priority Register (TPR) |
| 0x90 | Arbitration Priority Register¹ (APR) |
| 0xA0 | Processor Priority Register (PPR) |
| 0xB0 | EOI Register |
| 0xD0 | Logical Destination Register |
| 0xE0 | Destination Format Register |
| 0xF0 | Spurious Interrupt Vector Register |
| 0x100 | In-Service Register (ISR) (0-31) |
| 0x110 | In-Service Register (ISR) (32-63) |
| 0x120 | In-Service Register (ISR) (64-95) |
| 0x130 | In-Service Register (ISR) (96:-27) |
| 0x140 | In-Service Register (ISR) (128-159) |
| 0x150 | In-Service Register (ISR) (160-191) |
| 0x160 | In-Service Register (ISR) (192-223) |
| 0x170 | In-Service Register (ISR) (224-255) |
| 0x180 | Trigger Mode Register (TMR) (0-31) |
| 0x190 | Trigger Mode Register (TMR) (32-63) |
| 0x1A0 | Trigger Mode Register (TMR) (64-95) |
| 0x1B0 | Trigger Mode Register (TMR) (96-127) |
| 0x1C0 | Trigger Mode Register (TMR) (128-159) |
| 0x1D0 | Trigger Mode Register (TMR) (160-191) |
| 0x1E0 | Trigger Mode Register (TMR) (192-223) |
| 0x1F0 | Trigger Mode Register (TMR) (224-255) |
| 0x200 | Interrupt Request Register (IRR) (0-31) |
| 0x210 | Interrupt Request Register (IRR) (32-63) |
| 0x220 | Interrupt Request Register (IRR) (64-95) |
| 0x230 | Interrupt Request Register (IRR) (96-127) |
| 0x240 | Interrupt Request Register (IRR) (128-159) |
| 0x250 | Interrupt Request Register (IRR) (160-191) |
| 0x260 | Interrupt Request Register (IRR) (192-223) |
| 0x270 | Interrupt Request Register (IRR) (224-255) |
| 0x280 | Error Status Register |
| 0x300 | Interrupt Command Register (ICR) (0-31) |
| 0x310 | Interrupt Command Register (ICR) (32-63) |
| 0x320 | LVT Timer Register |
| 0x330 | LVT Thermal Register² |
| 0x340 | LVT Performance Register³ |
| 0x350 | LVT LINT0 Register |
| 0x360 | LVT LINT1 Register |
| 0x370 | LVT Error Register |
| 0x380 | Initial Count Register (für Timer) |
| 0x390 | Current Count Register (für Timer) |
| 0x3E0 | Divide Configuration Register (für Timer) |

1\) Nicht unterstützt in Pentium 4 und Intel Xeon Prozessoren 2) Eingeführt mit dem Pentium 4 und Intel Xeon Prozessoren. Dieses Register ist implementations-abhängig und muss in Zukunft nicht mehr vorhanden sein. 3) Eingeführt mit dem Pentium Pro Prozessor. Dieses Register ist implementations-abhängig und muss in Zukunft nicht mehr vorhanden sein.  

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

## Weblinks

- [Intel® 64 and IA-32 Architectures Software Developer's Manual Volume 3A: System Programming Guide](http://www.intel.com/products/processor/manuals/index.htm) (Kapitel 8)
- [AMD64 Architecture Programmer's Manual Volume 2: System Programming](http://www.amd.com/us-en/Processors/DevelopWithAMD/0,,30_2252_739_7044,00.html) (Kapitel 16)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/2476/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1581/index.html)

<!-- MediaWiki page 1581; revision 2476; parent 2475; 2007-12-23T15:46:13Z -->
