# Serielle Schnittstelle

Die serielle Schnittstelle (Abkürzung: COM) scheint veraltet ist aber sehr nützlich um z.B den Kernel im frühen Entwicklungstand zu debuggen, denn der Bildschirm kann nur begrenzt Text anzeigen und wie in Qemu oder Bochs kann man kein Copy 'n' Paste vom Bildschirm machen. Außerdem sollte bei keinem Betriebssystem ein COM-Port fehlen, da er heute auch noch oft Anwendung findet und leicht zu programmieren ist.

## COM-Ports finden

Normalerweise haben die COM-Ports folgende IO-Ports:

| Name | IO-Port | IRQ |
| ------ | --------- | ----- |
| COM1 | 0x3F8 | 4 |
| COM2 | 0x2F8 | 3 |
| COM3 | 0x3E8 | 4 |
| COM4 | 0x2E8 | 3 |

Man kann aber auch die IO-Ports aus der BIOS-Data-Area lesen

| Adresse | Größe | Beschreibung |
| --------- | ------- | ------------------------- |
| 0x400 | 2 | IO-Port des COM-Ports 1 |
| 0x402 | 2 | IO-Port des COM-Ports 2 |
| 0x404 | 2 | IO-Port des COM-Ports 3 |
| 0x406 | 2 | IO-Port des COM-Ports 4 |

## IO-Ports der einzelnen Register

Da ein COM-Port mehrere Register benutzt, braucht er auch mehrere IO-Ports. Die oben angegebenen IO-Ports sind nur die Basis-IO-Ports. Man muss also nachher noch das Offset der einzelnen Register addieren. Die Offsets sind in dieser Liste:

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

Ich werde hier ein wenig drauf eingehen, wie man verschiedene Optionen setzt und auf einen COM-Port sendet bzw. empfängt.

### Baudrate einstellen

Um die Baudrate einzustellen muss man erstmal das DLAB-Bit setzen, es ist eine Art Umschaltbit um 12 Register über 8 IO-Port-Adressen zu benutzen. Dafür muss man im LineControl-Register das 8. Bit setzen.

Die Baudrate wird aber nicht direkt gespeichert. Es wird immer nur ein Teiler gespeichert. Diesen kann man sich so berechnen:\\ *t = 115200/b*\\ Wobei *t* der Teiler und *b* die Baudrate ist.

Nun kann man in den Transmitting-Buffer das Lowbyte des Teilers und in das InterruptEnable-Register das Highbyte.

Danach sollte man das DLAB-Bit wieder zurücksetzen.

### Parität setzen

Es gibt 4 verschiedene Paritäten: Odd, Even, High Parity und Low Parity. Diese setzt man mithilfe von 3 Bits, es sind die Bits 4-6 des LineControl-Registers.

| Parität | Bit 4 | Bit 5 | Bit 6 |
| ------------- | ------- | ------- | ------- |
| Keine | 0 | X | X |
| Odd | 1 | 0 | 0 |
| Even | 1 | 1 | 0 |
| High Parity | 1 | 0 | 1 |
| Low Parity | 1 | 1 | 1 |

### Bytelänge setzen

Die Bytelänge bestimmt wie viel Bits ein Byte ergeben. Heutzutage werden eigentlich immer 8 Bits zu einem Byte zusammengefasst. Ein Byte kann 5 bis 8 Bits haben. Zum Setzen der Anzahl wird das 1. und 2. Byte im LineControl-Register benutzt. 00b entspricht 5 Bits 01b 6 usw. Also einfach die Anzahl an Bits minus 5 und in einen zwei-Bit-Wert wandeln.

### Anzahl Stopbits setzen

Die Anzahl an Stopbits wird im 3 Bit des LineControl-Registers gesetzt. 0b entspricht einem Stopbit und 1b zwei Stopbits (für Bytes mit 5 Bits 1.5 Stopbits).

### Senden

Zum Senden muss man erstmal nachschauen ob man senden darf. Wenn das 6. Bit des LineStatus-Registers gesetzt ist darf man Senden. Dafür schreibt man einfach das zu sendende Byte in Transmitting-Buffer.

### Empfangen

Im InterruptControl-Register wird bestimmt zu welchen Ereignissen man einen Interrupt bekommt. Welche Bits für was stehen wird hier nicht besprochen, doch wenn man 0x00 in das InterruptControl-Register schreibt, wird man nie einen Interrupt bekommen. So wollen wir vorgehen und einfach Lesen ohne vorher auf einen Interrupt zu warten. Das Prinzip des Lesens ist allerdings gleich, auch wenn man vorher auf einen Interrupt wartet. Im 1. Bit des LineStatus-Registers sieht man ob ein Byte empfangen wurde. Man kann es dann einfach aus dem Transmitting-Buffer lesen.

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

    // IO-Ports der COM-Ports
    u16 com_base[4] = { 0x3F8,0x2F8,0x3E8,0x2E8 };

    // Funktion zum initialisieren eines COM-Ports
    void init_com(u16 base,u32 baud,u8 parity,u8 bits) {
      // Teiler berechnen
      union {
        u8 b[2];
        u16 w;
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
    // Ob man schreiben kann
    u32 is_transmit_empty(u16 base) {
      return inb(base+LSR)&0x20;
    }
    // Byte senden
    void write_com(u16 base,u8 chr) {
      while (is_transmit_empty(base)==0);
      outb(base,chr);
    }
    // Ob man lesen kann
    u32 serial_received(u16 base) {
      return inb(base+LSR)&1;
    }
    // Byte empfangen
    u8 read_serial(u16 base) {
      while (!serial_received(base));
      return inb(base);
    }

\</c\>

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/2252/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1561/index.html)

<!-- MediaWiki page 1561; revision 2252; parent 0; 2007-11-16T18:21:21Z -->
