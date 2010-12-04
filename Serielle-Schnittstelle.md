# Serielle Schnittstelle

Die **serielle Schnittstelle** (Abkürzung: **COM** von *Communication* oder **RS232**, heute **EIA232** genannt) ist eine 1980 eingeführte Schnittstelle für die Übertragung von Daten, meist von Computer zu Computer.

  

## Funktionsweise

Daten werden bei der seriellen Schnittstellen als Wörter übertragen, welche je nach Konfiguration fünf bis neun Bits entsprechen. Codiert werden diese Wörter nach dem ASCII-Zeichensatz. Der wichtigste Unterschied zur [parallelen Schnittstelle](https://github.com/lowlevel-eu/wiki/wiki/Parallele-Schnittstelle "Parallele Schnittstelle") ist, dass die Bits nacheinander übertragen werden.

## Aufbau

### Basis-I/O-Ports

Normalerweise haben die COM-Ports folgende Basis-I/O-Ports:

| Name | I/O-Port | IRQ |
| ------ | ---------- | ----- |
| COM1 | 0x3F8 | 4 |
| COM2 | 0x2F8 | 3 |
| COM3 | 0x3E8 | 4 |
| COM4 | 0x2E8 | 3 |

Man sollte die Basis-I/O-Ports aber aus der [BIOS Data Area](https://github.com/lowlevel-eu/wiki/wiki/BIOS-Data-Area "BIOS Data Area") auslesen.

### Offsets der einzelnen Register

Da ein COM-Port mehrere Register benutzt, braucht er auch mehrere I/O-Ports. Die oben angegebenen I/O-Ports sind nur die Basis-I/O-Ports. Man muss also nachher noch das Offset der einzelnen Register addieren. Folgende Register verbergen sich hinter den Offsets:

| Offset | Lesen/Schreiben | Name |
| -------- | ----------------- | ---------------------------------- |
| 0 | rw | Transmitting-Buffer |
| 1 | rw | InterruptEnable-Register |
| 2 | r | InterruptIdentification-Register |
| 2 | w | FIFOControl-Register |
| 3 | rw | LineControl-Register |
| 4 | rw | ModemControl-Register |
| 5 | r | LineStatus-Register |
| 6 | r | ModemStatus-Register |
| 7 | rw | Scratch-Register |

Der Transmitting-Buffer und der InterruptEnable-Buffer wird bei einem gesetzten DLAB (Umschaltbit) dazu verwendet die Baudrate zu speichern.

## Programmierung

### Baudrate einstellen

Um die Baudrate einzustellen muss erstmal das DLAB-Bit gesetzt werden, es ist eine Art Umschaltbit um 12 Register über 8 I/O-Port-Adressen benutzen zu können. Dafür muss im LineControl-Register das 7. Bit gesetzt sein.

Die Baudrate wird allerdings nicht direkt gespeichert, es wird immer nur ein Teiler gespeichert. Diesen kann man wie folgt berechnen:\\ *t = 115200/b*\\ Wobei *t* der Teiler und *b* die Baudrate ist.

Nun kann in den Transmitting-Buffer das Lowbyte des Teilers und in das InterruptEnable-Register das Highbyte geschrieben werden.

Danach sollte das DLAB-Bit wieder zurückgesetzt werden.

### Parität setzen

Es gibt vier verschiedene Paritäten: *Odd*, *Even*, *High Parity* und *Low Parity*. Diese setzt man mit Hilfe von drei Bits, es sind die Bits 3-5 des LineControl-Registers.

| Parität | Bit 3 | Bit 4 | Bit 5 |
| ------------- | ------- | ------- | ------- |
| Keine | 0 | X | X |
| Odd | 1 | 0 | 0 |
| Even | 1 | 1 | 0 |
| High Parity | 1 | 0 | 1 |
| Low Parity | 1 | 1 | 1 |

### Bytelänge setzen

Die Bytelänge bestimmt wie viel Bits ein Byte ergeben. Heutzutage werden eigentlich immer 8 Bits zu einem Byte zusammengefasst. Ein Byte kann 5 bis 8 Bits haben. Zum Setzen der Anzahl werden Bits 0 und 1 im LineControl-Register benutzt. 00b entspricht 5 Bits 01b 6 usw. Also einfach die Anzahl an Bits minus 5 und in einen Zwei-Bit-Wert wandeln.

### Anzahl Stoppbits setzen

Die Anzahl an Stoppbits wird mit Bit 2 des LineControl-Registers gesetzt. 0b entspricht einem Stoppbit und 1b zwei Stoppbits (für Bytes mit 5 Bits 1.5 Stoppbits).

### Senden

Um Daten Senden zu können muss erst überprüft werden, ob überhaupt gesendet werden darf. Wenn Bit 5 des LineStatus-Registers gesetzt ist darf gesendet werden. Dazu wir das zu sendende Byte in den Transmitting-Buffer geschrieben.

### Empfangen

Im InterruptControl-Register wird bestimmt zu welchen Ereignissen man einen Interrupt bekommt. Welche Bits für was stehen wird hier nicht besprochen, doch wenn man 0x00 in das InterruptControl-Register schreibt, wird man nie einen Interrupt bekommen. So wollen wir vorgehen und einfach Lesen ohne vorher auf einen Interrupt zu warten. Das Prinzip des Lesens ist allerdings gleich, auch wenn man vorher auf einen Interrupt wartet. In Bit 0 des LineStatus-Registers sieht man ob ein Byte empfangen wurde. Man kann es dann einfach aus dem Transmitting-Buffer lesen.

## Beispiel

\<c\>

    // Einige Definitionen
    #define IER 1
    #define IIR 2
    #define FCR 2
    #define LCR 3
    #define MCR 4
    #define LSR 5
    #define MSR 6

    // Funktion zum initialisieren eines COM-Ports
    void init_com(uint16_t base, uint32_t baud, uint8_t parity, uint8_t bits) {
      // Teiler berechnen
      union {
        uint8_t b[2];
        uint16_t w;
      } divisor;
      divisor.w = 115200/baud;;

      // Interrupt ausschalten
      outb(base+IER,0x00);
      
      // DLAB-Bit setzen
      outb(base+LCR,0x80);
      
      // Teiler (low) setzen
      outb(base+0,divisor.b[0]);
      
      // Teiler (high) setzen
      outb(base+1,divisor.b[1]);
      
      // Anzahl Bits, Parität, usw setzen (DLAB zurücksetzen)
      outb(base+LCR,((parity&0x7)<<3)|((bits-5)&0x3));
      
      // Initialisierung abschließen
      outb(base+FCR,0xC7);
      outb(base+MCR,0x0B);
    }

    // Prüft, ob man bereits schreiben kann
    uint8_t is_transmit_empty(u16 base) {
      return inb(base+LSR)&0x20;
    }

    // Byte senden
    void write_com(uint16_t base, uint8_t chr) {
      while (is_transmit_empty(base)==0);
      outb(base,chr);
    }

    // Prüft, ob man bereits lesen kann
    uint8_t serial_received(uint16_t base) {
      return inb(base+LSR)&1;
    }

    // Byte empfangen
    uint8_t read_serial(uint16_t base) {
      while (!serial_received(base));
      return inb(base);
    }

\</c\>

## Weblinks

- [Tutorial zur seriellen Schnittstelle](http://www.nondot.org/sabre/os/files/Communication/CP_serial.pdf)
- [Tutorial zum RS232-Standard](http://www.camiresearch.com/Data_Com_Basics/RS232_standard.html)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/9038/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1561/index.html)

<!-- MediaWiki page 1561; revision 9038; parent 9012; 2010-12-04T00:33:07Z -->
