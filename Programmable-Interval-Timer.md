# Programmable Interval Timer

Der Programmable Interval Timer (PIT) ist ein Baustein auf dem Mainboard, der in regelmäßigen Zeitabständen Signale erzeugt. Er arbeitet intern mit einer Frequenz von rund 1193182 Hz und kann z. B. für präemptives Multitasking oder als Systemuhr genutzt werden.

## Register

Der PIT belegt vier Ports:

| Port | Verwendung |
| ------ | --------------------------------------------- |
| 0x40 | Counter-Register für Channel 0 setzen/lesen |
| 0x41 | Counter-Register für Channel 1 setzen/lesen |
| 0x42 | Counter-Register für Channel 2 setzen/lesen |
| 0x43 | Initalisierung (siehe unten) |

## Channels

Der PIT besitzt drei verschiedene *Channels*, die jeweils mit unterschiedlichen Intervallen laufen und unterschiedliche Signale erzeugen. Dabei kann lediglich der erste Channel (0) beliebig benutzt werden, da die beiden anderen Channels bereits eine Sonderfunktion haben.

### Channel 0

Dieser Channel ist mit dem [PIC](https://github.com/lowlevel-eu/wiki/wiki/Programmable-Interrupt-Controller "PIC") verbunden und löst je nach Modus in regelmäßigen Abständen den [IRQ 0](https://github.com/lowlevel-eu/wiki/wiki/Programmable-Interrupt-Controller#irq-tabelle "IRQ") aus. Standardmäßg ist der PIT darauf initialisiert, alle 54,9254 ms den IRQ 0 auszulösen (das entspricht einer Frequenz von ungefähr 18,2 Hz). Im [Real Mode](https://github.com/lowlevel-eu/wiki/wiki/Real-Mode "Real Mode") hat das BIOS für den IRQ 0 eine entsprechende [ISR](https://github.com/lowlevel-eu/wiki/wiki/Interrupt-Service-Routine "ISR") eingerichtet, die bei jedem Aufruf einen 16-Bit-Zähler an der Adresse 0000:046C erhöht.

### Channel 1

Dieser Channel wurde früher verwendet, um den Arbeitsspeicher zu synchronisieren. Heutzutage hat er keinen Nutzen mehr, sollte aber dennoch nicht verwendet werden, da es keine Garantie gibt, dass er nicht doch von irgendeinem Bauteil verwendet wird.

### Channel 2

Dieser Channel ist mit dem [Systemlautsprecher](https://github.com/lowlevel-eu/wiki/wiki/Systemlautsprecher "Systemlautsprecher") verbunden und bestimmt die Frequenz des ausgegebenen Tons.

## Modi

Der PIT unterstützt mehrere verschiedene Modi, in denen er arbeiten kann. Der am häufigste verwendete Modus ist Mode 2, da man mit diesem leicht eine Systemuhr implementieren kann.

### Mode 0: Interrupt on terminal count

Wenn das Counter-Register mit einem neuen Wert geladen wurde, wird dieses dekrementiert, bis es 0 erreicht. Dann wird der IRQ ausgelöst. Der Vorgang beginnt erst wieder von vorne, wenn ein neuer Wert ins Counter-Register geladen wird.

### Mode 1: Hardware Retriggerable One-Shot

In diesem Modus wird der IRQ in regelmäßigen Abständen ausgelöst. Dabei wird das Counter-Register bis 0 heruntergezählt, dann dessen ursprünglicher Wert wiederhergestellt und der IRQ ausgelöst. Danach beginnt der Vorgang von vorn.

### Mode 2: Rate Generator

Es wird ein Zähler dekrementiert, bis dieser den Wert 1 enthält, dann wird der IRQ ausgelöst und der ursprüngliche Wert des Zählers wiederhergestellt. Der Vorgang beginnt von vorn. Der Wert des Zählers ergibt sich folgendermaßen:

     Zähler=Interne Freqenz / Counter-Register

### Mode 3: Square Wave Generator

Ähnlich Mode 2, nur dass die Hälfte der Zeit während des Dekrementierens ein IRQ ausgelöst wird. Dieser Modus sollte für Channel 2 verwendet werden.

### Mode 4: Software Triggered Strobe

Das Counter-Register wird bis 0 heruntergezählt, ein Interrupt ausgelöst und der ursprüngliche Wert wiederhergestellt. Der Vorgang beginnt von vorn.

### Mode 5: Hardware Triggered Strobe

Das Herunterzählen beginnt erst, wenn andere Hardware dieses auslöst. Der IRQ wird bei Erreichen des Wertes 0 ausgelöst, dann wird wieder auf das Hardwaresignal gewartet usw.

## Initialisierung

Zur Initialisierung muss ein Byte an den Port 0x43 gesendet werden:

| Bit | Bedeutung | Mögliche Werte |
| ----- | -------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0 | Counterformat | 0: binär, 1: [BCD](https://github.com/lowlevel-eu/wiki/wiki/Binary-Coded-Decimal "BCD") |
| 1-3 | Modusnummer (siehe oben) | 0-5, alle anderen sind nicht definiert |
| 4,5 | Lesen/Schreiben des Counterregisters | 00: Wert ist in einem internen Register, 01:nur [LSB](https://github.com/lowlevel-eu/wiki/wiki/Bin%C3%A4re-Datentypen#msb-und-lsb "LSB"), 10: nur [MSB](https://github.com/lowlevel-eu/wiki/wiki/Bin%C3%A4re-Datentypen#msb-und-lsb "MSB"), 11: [LSB](https://github.com/lowlevel-eu/wiki/wiki/Bin%C3%A4re-Datentypen#msb-und-lsb "LSB") dann [MSB](https://github.com/lowlevel-eu/wiki/wiki/Bin%C3%A4re-Datentypen#msb-und-lsb "MSB") |
| 6,7 | Channel, der geändert werden soll | 0-2 |

Nachdem der entsprechende Channel des PITs (re-)initialisiert wurde, kann das Counter-Register geschrieben werden.

### Beispielcode

Dieser Code initialisiert den PIT in Modus 2 für Channel 0. Als Parameter wird die Frequenz übergeben (Rechnung siehe unten).

\<c\> void pit_init(int freq) {

      freq = 1193182 / freq;
      outb(0x43, 0x34);
      outb(0x40,freq & 0xFF);
      outb(0x40,freq >> 8);

} \</c\>

### Frequenzberechnung

Frequenzen haben die Einheit Hz = 1/s, wodurch man sich leicht deren Bedeutung klar machen kann: Hat die Frequenz z. B. den Wert 10 Hz, wird zehnmal pro Sekunde der IRQ 0 ausgelöst, also alle 100 ms (1 s = 1000 ms).

Im Mode 2 wird die interne Frequenz durch den Wert des Counter-Registers geteilt, um den Zähler zu erhalten. Wenn man nun eine bestimmte Frequenz benötigt, berechnet man den zu übergebenen Wert des Counter-Registers wie folgt:

    Counter-Register = 1193182 Hz / Frequenz.

Entsprechendes steht auch im obigen Beispielcode.

## Weblinks

- <http://www4.informatik.uni-erlangen.de/Lehre/WS07/V_BS/Uebungen/oostubs/web/aufgaben/aufgabe5/timer.shtml>
- <http://www.scs.stanford.edu/09wi-cs140/pintos/specs/8254.pdf> -Intel Spezifikation (englisch)
- <http://www.brokenthorn.com/Resources/OSDevPit.html> (englisch)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/9660/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1432/index.html)

<!-- MediaWiki page 1432; revision 9660; parent 8815; 2011-04-11T12:35:18Z -->
