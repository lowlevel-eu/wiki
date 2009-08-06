# Peripheral Component Interconnect

**Peripheral Component Interconnect** (kurz **PCI**) ist ein [Bus](https://lowlevel-eu.github.io/wiki/pages/1769/index.html "Kategorie:Bus") zur leichten Verbindung von Peripheriegeräten mit der CPU.

## Konfigurations-Register

Jedes PCI-Gerät besitzt ein Konfigurations-Register, welches 256 Byte groß ist. Gelesen und beschrieben wird es 32bit-weise mithilfe eines Adress-I/O-Ports (0xCF8) und eines Daten-I/O-Ports (0xCFC).

### Aufbau des Adress-I/O-Ports

| 31 | 30-24 | 23-16 | 15-11 | 10-8 | 7-0 |
| ------------ | ------------ | ----------- | -------------- | ----------------- | ---------------- |
| Enable Bit | Reserviert | Busnummer | Gerätenummer | Funktionsnummer | Registernummer |

  

### Aufbau des Konfigurations-Adressraum

| Register | 31-24 | 23-16 | 15-8 | 7-0 |
| ---------- | ----------- | ------------- | --------------- | ----------------- |
| 0x00 | Device ID |  | Vendor ID |  |
| 0x04 | Status |  | Command |  |
| 0x08 | Classcode |  |  | Revision ID |
| 0x0C | BIST | Header Type | Latency Timer | Cache Line Size |

Die ersten 16 Byte sind für alle PCI-Geräte gleich.

- Die *Vendor ID*s werden von PCI-SIG verwaltet und den Herstellern zugewiesen. Der Wert 0xffff ist für den Fall reserviert, dass an dieser Stelle kein Gerät vorhanden ist.
- Die *Device ID*s verwalten die Hardwarehersteller selbst. Sie dient zusammen mit der *Vendor ID* der eindeutigen Identifikation des Gerätes.
- *Classcode* ist noch einmal geteilt. Die oberen 8 Bit repräsentieren die *Base Class*. Die mittleren 8 Bit stehen für die *Subclass* und die unter 8 Bit für das *Programming Interface*.

| Header Type | Kurze Beschreibung |
| ------------- | ------------------------------------- |
| 0x00 | [Standard](#header-type-0x00) |
| 0x01 | [PCI/PCI-Bridge](#header-type-0x01) |
| 0x02 | CardBus-Bridge |

- *Header Type* spezifiziert den Inhalt der Register 0x10-0x3C, wobei Bit 7 angibt ob es sich um ein Multifunction-Device handelt oder nicht.

#### Header Type 0x00

| Register | 31-24 | 23-16 | 15-8 | 7-0 |
| ---------- | ---------------------------- | ----------- | --------------------- | ---------------------- |
| 0x10 | Base Address 0 (BAR0) |  |  |  |
| 0x14 | Base Address 1 (BAR1) |  |  |  |
| 0x18 | Base Address 2 (BAR2) |  |  |  |
| 0x1C | Base Address 3 (BAR3) |  |  |  |
| 0x20 | Base Address 4 (BAR4) |  |  |  |
| 0x24 | Base Address 5 (BAR5) |  |  |  |
| 0x28 | Cardbus CIS Pointer |  |  |  |
| 0x2C | Subsystem ID |  | Subsystem Vendor ID |  |
| 0x30 | Expansion ROM base address |  |  |  |
| 0x34 | Reserviert |  |  | Capabilities Pointer |
| 0x38 | Reserviert |  |  |  |
| 0x3C | Max Latency | Min Grant | Interrupt Pin | Interrupt Line |

#### Header Type 0x01

| Register | 31-24 | 23-16 | 15-8 | 7-0 |
| ---------- | ---------------------------------- | ------------------- | -------------------------- | ---------------------- |
| 0x10 | Base address 0 |  |  |  |
| 0x14 | Base address 1 |  |  |  |
| 0x18 | Secondary latency timer | Subordinate bus № | Secondary bus № | Primary bus № |
| 0x1C | Secondary Status |  | I/O Limit | I/O base |
| 0x20 | Memory limit |  | Memory base |  |
| 0x24 | Prefetchable memory limit |  | Prefetchable memory base |  |
| 0x28 | Prefetchable base upper 32 bits |  |  |  |
| 0x2C | Prefetchable limit upper 32 bits |  |  |  |
| 0x30 | I/O limit upper 16 bits |  | I/O base upper 16 bits |  |
| 0x34 | Reserviert |  |  | Capabilities pointer |
| 0x38 | Extension ROM base address |  |  |  |
| 0x3C | Bridge control |  | Interrupt pin | Interrupt line |

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
| ----------- | ------------------------------------------------------------------------------------------------------------------ |
| 0x00 | [Alle Geräte die gebaut wurden bevor Classcodes eingeführt wurden](#class-0x00---pre-20) |
| 0x01 | [Massenspeicher](#class-0x01---massenspeicher) |
| 0x02 | [Netzwerk-Controller](#class-0x02---netzwerk-controller) |
| 0x03 | [Bildschirm-Controller](#class-0x03---bildschirm-controller) |
| 0x04 | [Multimedia-Geräte](#class-0x04---multimedia-ger%C3%A4te) |
| 0x05 | [Speicher-Controller](#class-0x05---speicher-controller) |
| 0x06 | [Bridge-Geräte](#class-0x06---bridge-ger%C3%A4te) |
| 0x07 | [Controller zur einfachen Kommunikation](#class-0x07---controller-zur-einfachen-kommunikation) |
| 0x08 | [System-Peripherie](#class-0x08---system-peripherie) |
| 0x09 | [Input-Geräte](#class-0x09---input-ger%C3%A4te) |
| 0x0A | [Docking-Stationen](#class-0x0a---docking-stationen) |
| 0x0B | [Prozessoren](#class-0x0b---prozessoren) |
| 0x0C | [Serielle Buscontroller](#class-0x0c---serielle-buscontroller) |
| 0x0D | [Wireless-Controller](#class-0x0d---wireless-controller) |
| 0x0E | [Intelligente Controller](#class-0x0e---intelligente-controller) |
| 0x0F | [Satelliten-Kommunikations-Controller](#class-0x0f---satelliten-kommunikations-controller) |
| 0x10 | [Encryption/Decryption-Controller](#class-0x10---encryptiondecryption-controller) |
| 0x11 | [Datenerfassungs- und Signalprozessor-Controller](#class-0x11---datenerfassungs--und-signalprozessor-controller) |
| 0x12-0xFE | *Reserviert* |
| 0xFF | Sonstige |

  

### Class 0x00 - Pre 2.0

| Subclass | Programming Interface | Beschreibung |
| ---------- | ----------------------- | ---------------------------------------------------------------------------------------------------------------- |
| 0x00 | 0x00 | Alle nicht- [VGA](https://github.com/lowlevel-eu/wiki/wiki/Video-Graphics-Array "Video Graphics Array")-Geräte |
| 0x01 | 0x00 | VGA-Geräte |

  

### Class 0x01 - Massenspeicher

| Subclass | Programming Interface | Beschreibung |
| ---------- | ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0x00 | 0x00 | SCSI |
| 0x01 | 0x?? | IDE |
| 0x02 | 0x00 | [Floppy](https://github.com/lowlevel-eu/wiki/wiki/Floppy-Disk-Controller "Floppy Disk Controller") |
| 0x03 | 0x00 | IPI |
| 0x04 | 0x00 | RAID |
| 0x05 | 0x20 | [ATA](https://github.com/lowlevel-eu/wiki/wiki/AT-Attachment "AT Attachment")-Controller (Single [DMA](https://github.com/lowlevel-eu/wiki/wiki/Direct-Memory-Access "Direct Memory Access")) |
| 0x05 | 0x30 | ATA-Controller (Chained DMA) |
| 0x80 | 0x00 | Anderer Massenspeicher |

  

### Class 0x02 - [Netzwerk](https://lowlevel-eu.github.io/wiki/pages/1888/index.html "Kategorie:Netzwerk")-Controller

| Subclass | Programming Interface | Beschreibung |
| ---------- | ----------------------- | -------------------------------------------------------------------------- |
| 0x00 | 0x00 | [Ethernet](https://github.com/lowlevel-eu/wiki/wiki/Ethernet "Ethernet") |
| 0x01 | 0x00 | Token Ring |
| 0x02 | 0x00 | FDDI |
| 0x03 | 0x00 | ATM |
| 0x04 | 0x00 | ISDN |
| 0x05 | 0x00 | World FIP (Feldbus) |
| 0x06 | 0x?? | PICMG 2.14, Multi-Computing |
| 0x80 | 0x00 | Anderer Netzwerk-Controller |

  

### Class 0x03 - Bildschirm-Controller

| Subclass | Programming Interface | Beschreibung |
| ---------- | ----------------------- | ------------------------------- |
| 0x00 | 0x00 | VGA |
| 0x00 | 0x01 | 8514 |
| 0x01 | 0x00 | XGA |
| 0x02 | 0x00 | 3D |
| 0x80 | 0x00 | Anderer Bildschirm-Controller |

  

### Class 0x04 - Multimedia-Geräte

| Subclass | Programming Interface | Beschreibung |
| ---------- | ----------------------- | -------------------------- |
| 0x00 | 0x00 | Video-Gerät |
| 0x01 | 0x00 | Audio-Gerät |
| 0x02 | 0x00 | Telefonie |
| 0x80 | 0x00 | Anderes Multimedia-Gerät |

  

### Class 0x05 - Speicher-Controller

| Subclass | Programming Interface | Beschreibung |
| ---------- | ----------------------- | ------------------ |
| 0x00 | 0x00 | RAM |
| 0x01 | 0x00 | Flash-Speicher |
| 0x80 | 0x00 | Anderer Speicher |

  

### Class 0x06 - Bridge-Geräte

| Subclass | Programming Interface | Beschreibung |
| ---------- | ----------------------- | ------------------------------------------------------- |
| 0x00 | 0x00 | Host/PCI-Bridge |
| 0x01 | 0x00 | PCI/ISA-Bridge |
| 0x02 | 0x00 | PCI/EISA-Bridge |
| 0x03 | 0x00 | PCI/MicroChannel-Bridge |
| 0x04 | 0x00 | PCI/PCI-Bridge |
| 0x04 | 0x01 | PCI/PCI-Bridge (Subtractive Decode) |
| 0x05 | 0x00 | PCI/PCMCIA-Bridge |
| 0x06 | 0x00 | PCI/NuBus-Bridge |
| 0x07 | 0x00 | PCI/CardBus-Bridge |
| 0x08 | 0x?? | Raceway, Switched Fabric |
| 0x09 | 0x40 | Semitransparente PCI/PCI-Bridge (primär zum Host)<br> |
| 0x09 | 0x80 | Semitransparente PCI/PCI-Bridge (sekundär zum Host) |
| 0x0A | 0x00 | InfiniBand/PCI-Brige |
| 0x80 | Anderer Bridge-Typ |  |

  

### Class 0x07 - Controller zur einfachen Kommunikation

| Subclass | Programming Interface | Beschreibung |
| ---------- | ----------------------- | -------------------------------------------- |
| 0x00 | 0x00 | Serielle Schnittstelle (XT-kompatibel)<br> |
| 0x00 | 0x01 | Serielle Schnittstelle (16450) |
| 0x00 | 0x02 | Serielle Schnittstelle (16550) |
| 0x00 | 0x03 | Serielle Schnittstelle (16650) |
| 0x00 | 0x04 | Serielle Schnittstelle (16750) |
| 0x00 | 0x05 | Serielle Schnittstelle (16850) |
| 0x00 | 0x06 | Serielle Schnittstelle (16950) |
| 0x01 | 0x00 | Parallelport (Standard)<br> |
| 0x01 | 0x01 | Parallelport (Bidirektional) |
| 0x01 | 0x02 | Parallelport (ECP 1.0) |
| 0x01 | 0x03 | Parallelport (IEEE 1284) |
| 0x01 | 0xFE | IEEE-1284-Gerät, Target |
| 0x02 | 0x00 | Multiport Serial Controller |
| 0x03 | 0x00 | Standard-Modem |
| 0x03 | 0x01 | Hayes-kompatibles Modem (16450) |
| 0x04 | 0x00 | GPIB (IEEE488.1/2) Controller |
| 0x04 | 0x02 | Hayes-kompatibles Modem (16550) |
| 0x04 | 0x03 | Hayes-kompatibles Modem (16650) |
| 0x04 | 0x04 | Hayes-kompatibles Modem (16750) |
| 0x05 | 0x00 | SmartCard |
| 0x80 | 0x00 | Andere Controller<br> |

  

### Class 0x08 - System-Peripherie

| Subclass | Programming Interface | Beschreibung |
| ---------- | ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0x00 | 0x00 | 8259- [PIC](https://github.com/lowlevel-eu/wiki/wiki/Programmable-Interrupt-Controller "Programmable Interrupt Controller") |
| 0x00 | 0x01 | ISA-PIC |
| 0x00 | 0x02 | EISA-PIC |
| 0x00 | 0x10 | IO- [APIC](https://github.com/lowlevel-eu/wiki/wiki/Advanced-Programmable-Interrupt-Controller "Advanced Programmable Interrupt Controller") (EISA) |
| 0x00 | 0x20 | IOx-APIC |
| 0x01 | 0x00 | 8237-DMA-Controller |
| 0x01 | 0x01 | ISA-DMA-Controller |
| 0x01 | 0x02 | EISA-DMA-Controller |
| 0x02 | 0x00 | Standard-8254-Timer |
| 0x02 | 0x01 | ISA-System-Timer |
| 0x02 | 0x02 | EISA-System-Timer |
| 0x03 | 0x00 | Standard [Real Time Clock](https://github.com/lowlevel-eu/wiki/wiki/Real-Time-Clock "Real Time Clock") |
| 0x03 | 0x01 | ISA Real Time Clock |
| 0x04 | 0x00 | PCI Hot Plug Controller |
| 0x80 | 0x00 | Andere System-Peripherie |

  

### Class 0x09 - Input-Geräte

| Subclass | Programming Interface | Beschreibung |
| ---------- | ----------------------- | ----------------------------------------------------------------------------------- |
| 0x00 | 0x00 | Tastatur |
| 0x01 | 0x00 | Digitizer (Stift) |
| 0x02 | 0x00 | Maus |
| 0x03 | 0x00 | Scanner |
| 0x04 | 0x00 | Standard-[Gameport](https://github.com/lowlevel-eu/wiki/wiki/Gameport "Gameport") |
| 0x04 | 0x10 | Gameport |
| 0x80 | 0x00 | Anderes Input-Gerät |

  

### Class 0x0A - Docking-Stationen

| Subclass | Programming Interface | Beschreibung |
| ---------- | ----------------------- | ------------------------- |
| 0x00 | 0x00 | Normale Docking-Station |
| 0x80 | 0x00 | Andere Docking-Station |

  

### Class 0x0B - Prozessoren

| Subclass | Programming-Interface | Beschreibung |
| ---------- | ----------------------- | -------------- |
| 0x00 | 0x00 | 386 |
| 0x01 | 0x00 | 486 |
| 0x02 | 0x00 | Pentium |
| 0x10 | 0x00 | Alpha |
| 0x20 | 0x00 | PowerPC |
| 0x30 | 0x00 | MIPS |
| 0x40 | 0x00 | Coprozessor |

  

### Class 0x0C - Serielle Buscontroller

| Subclass | Programming Interface | Beschreibung |
| ---------- | ----------------------- | ---------------------------------------------------------------------------------------------------- |
| 0x00 | 0x00 | Firewire (IEEE 1394) |
| 0x00 | 0x10 | Firewire (OHCI) |
| 0x01 | 0x00 | ACCESS-Bus |
| 0x02 | 0x00 | SSA (Serial Storage Architecture) |
| 0x03 | 0x00 | [USB](https://github.com/lowlevel-eu/wiki/wiki/Universal-Serial-Bus "Universal Serial Bus") (UHCI) |
| 0x03 | 0x10 | USB (OHCI) |
| 0x03 | 0x20 | USB (EHCI) |
| 0x03 | 0x80 | USB (kein HCI) |
| 0x03 | 0xFE | USB-Gerät |
| 0x04 | 0x00 | Fibre Channel |
| 0x05 | 0x00 | SMB (System Management Bus) |
| 0x06 | 0x00 | InfiniBand |
| 0x07 | 0x00 | IPMI SMIC Interface |
| 0x07 | 0x01 | IPMI Keyboard Style Interface |
| 0x07 | 0x02 | IPMI Block Transfer Device |
| 0x08 | 0x00 | SERCOS Interface |
| 0x09 | 0x00 | CANBus |

  

### Class 0x0D - Wireless-Controller

| Subclass | Programming Interface | Beschreibung |
| ---------- | ----------------------- | ----------------------------- |
| 0x00 | 0x00 | iRDA |
| 0x01 | 0x00 | Consumer Infrared |
| 0x10 | 0x00 | Radio Frequency |
| 0x11 | 0x00 | Bluetooth |
| 0x12 | 0x00 | Broadband |
| 0x80 | 0x00 | Anderer Wireless-Controller |

  

### Class 0x0E - Intelligente Controller

| Subclass | Programming Interface | Beschreibung |
| ---------- | ----------------------- | ----------------- |
| 0x00 | 0x?? | I²O-Architektur |
| 0x00 | 0x00 | Message FIFO |

  

### Class 0x0F - Satelliten-Kommunikations-Controller

| Subclass | Programming Interface | Beschreibung |
| ---------- | ----------------------- | -------------- |
| 0x01 | 0x00 | TV |
| 0x02 | 0x00 | Audio |
| 0x03 | 0x00 | Sprache |
| 0x04 | 0x00 | Daten |

  

### Class 0x10 - Encryption/Decryption-Controller

| Subclass | Programming Interface | Beschreibung |
| ---------- | ----------------------- | -------------------- |
| 0x01 | 0x00 | Netzwerk |
| 0x10 | 0x00 | Entertainment |
| 0x80 | 0x00 | Anderer Controller |

  

### Class 0x11 - Datenerfassungs- und Signalprozessor-Controller

| Subclass | Programming Interface | Beschreibung |
| ---------- | ----------------------- | ------------------------------------- |
| 0x00 | 0x00 | Digital Input/Output Module |
| 0x01 | 0x00 | Zähler |
| 0x10 | 0x00 | Synchronisation und Frequenzmessung |
| 0x20 | 0x00 | Management Card |
| 0x80 | 0x00 | Anderer Controller |

  

## Weblinks

- [Linux PCI ID Repositorium](http://pci-ids.ucw.cz/) - Enthält viele VendorIDs und die dazugehörigen DeviceIDs

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/5108/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1626/index.html)

<!-- MediaWiki page 1626; revision 5108; parent 5107; 2009-08-06T09:01:09Z -->
