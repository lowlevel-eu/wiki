# Peripheral Component Interconnect

Peripheral Component Interconnect (kurz PCI) ist ein Bus zur leichten Verbindung von Peripheriegeräten mit mit der CPU.

## Konfigurations-Register

Jedes PCI-Gerät besitzt ein Konfigurations-Register, welches 256 Byte groß ist. Gelesen und beschrieben wird es 32bit-weise mithilfe eines Adress-I/O-Ports (0xCF8) und eines Daten-I/O-Ports (0xCFC).

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

  

### Codebeispiel

\<c\>

1.  define PCI_CONFIG_DATA 0xCFC
2.  define PCI_CONFIG_ADDRESS 0xCF8

/\*\*

    * Liest ein Dword aus einem PCI-Konfigurations-Register
    *  @param bus Bus
    *  @param dev Gerät
    *  @param func Funktion
    *  @param offset Registernummer
    *  @return Register content
    */

int pci_config_readd(int bus,int dev,int func,int offset) {

     int val;
     int address = 0x80000000|(bus<<16)|(dev<<11)|(func<<8)|(offset&0xFC);
     outl(PCI_CONFIG_ADDRESS,address);
     val = inl(PCI_CONFIG_DATA);
     return val;

}

/\*\*

    * Schreibt ein Dword in in ein PCI-Konfigurations-Register
    *  @param bus Bus
    *  @param dev Gerät
    *  @param func Funktion
    *  @param offset Registernummer
    *  @param val Wert zum Schreiben
    */

void pci_config_writed(int bus,int dev,int func,int offset,int val) {

     int address = 0x80000000|(bus<<16)|(dev<<11)|(func<<8)|(offset&0xFC);
     outl(PCI_CONFIG_ADDRESS,address);
     outl(PCI_CONFIG_DATA,val);

} \</c\>

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/2585/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1626/index.html)

<!-- MediaWiki page 1626; revision 2585; parent 2583; 2008-02-18T20:01:13Z -->
