# Peripheral Component Interconnect

Peripheral Component Interconnect (kurz PCI) ist ein Bus zur leichten Verbindung Peripheriegeräten mit mit der CPU.

## Konfigurations-Register

Jedes PCI-Gerät besitzt ein Konfigurations-Register, das 256 Byte groß ist. Gelesen und beschrieben wird es 32bit-weise mithilfe eines Adress-I/O-Ports (0xCF8) und eines Daten-I/O-Ports (0xCFC).

### Aufbau des Adress-I/O-Ports

| 31 | 30-24 | 23-16 | 15-11 | 10-8 | 7-0 |
| ------------ | ------------ | ----------- | -------------- | ----------------- | ---------------- |
| Enable Bit | Reserviert | Busnummer | Gerätenummer | Funktionsnummer | Registernummer |

  

### Aufbau des Konfigurations-Register

| Register | 31-24 | 23-16 | 15-8 | 7-0 |
| ---------- | ---------------------------- | ------------- | --------------------- | ----------------- |
| 00 | Device ID |  | Vendor ID |  |
| 04 | Status |  | Command |  |
| 08 | Classcode | Subclass | Revision ID |  |
| 0x0C | BIST | Header Type | Latency Timer | Cache Line Size |
| 0x10 | Base Address 0 (BAR0) |  |  |  |
| 0x14 | Base Address 1 (BAR1) |  |  |  |
| 0x18 | Base Address 2 (BAR2) |  |  |  |
| 0x1C | Base Address 3 (BAR3) |  |  |  |
| 0x20 | Base Address 4 (BAR4) |  |  |  |
| 0x24 | Base Address 5 (BAR5) |  |  |  |
| 0x28 | Cardbus CIS Pointer |  |  |  |
| 0x2C | Subsystem ID |  | Subsystem Vendor ID |  |
| 0x30 | Expansion ROM base address |  |  |  |
| 0x34 | Reserviert |  |  |  |
| 0x38 | Reserviert |  |  |  |
| 0x3C | Max Latency | Min Grant | Interrupt Pin | Interrupt Line |

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/2583/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1626/index.html)

<!-- MediaWiki page 1626; revision 2583; parent 0; 2008-02-18T19:50:05Z -->
