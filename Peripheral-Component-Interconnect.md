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

## Classcodes

| Class | Beschreibung |
| ----------- | ------------------------------------------------------------------------------------------------ |
| 0x00 | [Alle Geräte die gebaut wurden bevor Classcodes eingeführt wurden](#subclasses---pre-20) |
| 0x01 | [Massenspeicher](#subclasses---massenspeicher) |
| 0x02 | [Netzwerk-Controller](#subclasses---netzwerk-controller) |
| 0x03 | [Bildschirm-Controller](#subclasses---bildschirm-controller) |
| 0x04 | [Multimedia-Geräte](#subclasses---multimedia-ger%C3%A4te) |
| 0x05 | [Speicher-Controller](#subclasses---speicher-controller) |
| 0x06 | [Bridge-Geräte](#subclasses---bridge-ger%C3%A4te) |
| 0x07 | [Controller zur einfachen Kommunikation](#subclasses---controller-zur-einfachen-kommunikation) |
| 0x08 | [System-Peripherie](#subclasses---system-peripherie) |
| 0x09 | [Input-Geräte](#subclasses---input-ger%C3%A4te) |
| 0x0A | [Docking-Stationen](#subclasses---docking-stationen) |
| 0x0B | [Prozessoren](#) |
| 0x0C | [Seriell-Bus-Controller](#subclasses---seriell-bus-controller) |
| 0x0D-0xFE | Reserviert |
| 0xFF | Sonstige |

  

### Subclasses - Pre 2.0

| Subclass | Beschreibung |
| ---------- | ----------------------- |
| 0x00 | Alle nicht-VGA-Geräte |
| 0x01 | VGA-Geräte |

  

### Subclasses - Massenspeicher

| Subclass | Beschreibung |
| ---------- | ------------------------ |
| 0x00 | SCSI |
| 0x01 | IDE |
| 0x02 | Floppy |
| 0x03 | IPI |
| 0x04 | RAID |
| 0x80 | Anderer Massenspeicher |

  

### Subclasses - Netzwerk-Controller

| Subclass | Beschreibung |
| ---------- | ----------------------------- |
| 0x00 | Ethernet |
| 0x01 | Token Ring |
| 0x02 | FDDI |
| 0x03 | ATM |
| 0x80 | Anderer Netzwerk-Controller |

  

### Subclasses - Bildschirm-Controller

| Subclass | Beschreibung |
| ---------- | ------------------------------- |
| 0x00 | VGA-Kompatibel |
| 0x01 | XGA |
| 0x80 | Anderer Bildschirm-Controller |

  

### Subclasses - Multimedia-Geräte

| Subclass | Beschreibung |
| ---------- | -------------------------- |
| 0x00 | Video-Gerät |
| 0x01 | Audio-Gerät |
| 0x80 | Anderes Multimedia-Gerät |

  

### Subclasses - Speicher-Controller

| Subclass | Beschreibung |
| ---------- | ------------------ |
| 0x00 | RAM |
| 0x01 | Flash-Speicher |
| 0x80 | Anderer Speicher |

  

### Subclasses - Bridge-Geräte

| Subclass | Beschreibung |
| ---------- | ------------------------- |
| 0x00 | Host/PCI-Bridge |
| 0x01 | PCI/ISA-Bridge |
| 0x02 | PCI/EISA-Bridge |
| 0x03 | PCI/MicroChannel-Bridge |
| 0x04 | PCI/PCI-Bridge |
| 0x05 | PCI/PCMCIA-Bridge |
| 0x06 | PCI/NuBus-Bridge |
| 0x07 | PCI/CardBus-Bridge |
| 0x80 | Anderer Bridge-Typ |

  

### Subclasses - Controller zur einfachen Kommunikation

| Subclass | Beschreibung |
| ---------- | ------------------------ |
| 0x00 | Serielle Schnittstelle |
| 0x01 | Parallelport |
| 0x80 | Andere |

  

### Subclasses - System-Peripherie

| Subclass | Beschreibung |
| ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0x00 | [Programmable Interrupt Controller](https://github.com/lowlevel-eu/wiki/wiki/Programmable-Interrupt-Controller "Programmable Interrupt Controller") |
| 0x01 | [Direct Memory Access](https://github.com/lowlevel-eu/wiki/wiki/Direct-Memory-Access "Direct Memory Access") |
| 0x02 | Timer |
| 0x03 | Realtime Clock |
| 0x80 | Andere System-Peripherie |

  

### Subclasses - Input-Geräte

| Subclass | Beschreibung |
| ---------- | --------------------- |
| 0x00 | Tastatur |
| 0x01 | Digitizer (Stift) |
| 0x02 | Maus |
| 0x80 | Anderes Input-Gerät |

  

### Subclasses - Docking-Stationen

| Subclass | Beschreibung |
| ---------- | ------------------------- |
| 0x00 | Normale Docking-Station |
| 0x80 | Andere Docking-Station |

  

### Subclasses - Processors

| Subclass | Beschreibung |
| ---------- | -------------- |
| 0x00 | 386 |
| 0x01 | 486 |
| 0x02 | Pentium |
| 0x10 | Alpha |
| 0x20 | PowerPC |
| 0x40 | Co-Processor |

  

### Subclasses - Seriell-Bus-Controller

| Subclass | Beschreibung |
| ---------- | --------------------------------------------------------------------------------------------------- |
| 0x00 | Firewire (IEEE 1394) |
| 0x01 | ACCESS-Bus |
| 0x02 | SSA (Serial Storage Architecture) |
| 0x03 | [USB](https://github.com/lowlevel-eu/wiki/wiki/Universal-Serial-Bus "USB") (Universal Serial Bus) |

  

## Weblinks

- [Linux PCI ID Repositorium](http://pci-ids.ucw.cz/iii/) - Enthält viele VendorIDs und die dazugehörigen DeviceIDs

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/2592/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1626/index.html)

<!-- MediaWiki page 1626; revision 2592; parent 2591; 2008-02-19T17:01:50Z -->
