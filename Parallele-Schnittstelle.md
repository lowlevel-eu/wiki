# Parallele Schnittstelle

**Achtung!**

Dieser Artikel wird gerade bearbeitet, bitte **keine** Änderungen vornehmen! ~[Hartmut](https://lowlevel-eu.github.io/wiki/pages/1865/index.html "Benutzer:Hartmut") 19:40, 6. Aug. 2009 (CEST)

Die **parallele Schnitstelle** ist eine Schnitstelle am PC zur Übertragung von Daten an Peripheriegeräte.

  

## Funktionsweise

Die parallele Schnitstelle ist primär für die Übertragung von Daten an Peripheriegeräte gedacht und eignet sich nur gering für die bidirektionale Übertragung. Meistens wird an der parallelen Schnitstelle ein Drucker angeschlossen, für den es einen extra 36-poligen Druckeranschluss (auch Centronics, nach dem ehemaligen Drucker-Hersteller benannt) gibt. Der parallele Anschuluss an sich ist 25-polig und männlich.

Die Bestätigung für die Datennannahme erfolt von Peripherie-Seite mit dem sogenannten Handshake (eine, sehr vereinfacht ausgedrückt, beidseitige Einverständnis zur Übertragung der Daten), und zwar nach dem 2-Wege und 3-Weg-Verfahren (siehe dazu [\[1\]](http://de.wikipedia.org/wiki/Drei-Wege-Handshake)).

### Spezielle Funktionsweise bei Drucker

Für Drucker wurde die Centronics-Buchse entwickelt. Diese hat andere Betriebsmodi und die Pins vom 25-poligen Stecker werden anders gemappt. Auch ist hier eine geringe bidirektionale Übertragung möglich. Nachfolgend eine Tabelle der möglichen Signale, die der PC an den Drucker und vice versa schicken kann:

| Pin-Nr. (25-polig) | Pin-Nr. (36-polig) | Signal-Bezeichnung | Transfer-Richtung | Funktion/Bedeutung |
| -------------------- | -------------------- | -------------------- | ------------------- | -------------------------------------------------------------- |
| 1 | 1 | Strobe | PC-\>Gerät | Daten sind gültig (valid) |
| 2 | 2 | D1 | PC-\>Gerät | Datenbit 0 |
| 3 | 3 | D2 | PC-\>Gerät | Datenbit 1 |
| 4 | 4 | D3 | PC-\>Gerät | Datenbit 2 |
| 5 | 5 | D4 | PC-\>Gerät | Datenbit 3 |
| 6 | 6 | D5 | PC-\>Gerät | Datenbit 4 |
| 7 | 7 | D6 | PC-\>Gerät | Datenbit 5 |
| 8 | 8 | D7 | PC-\>Gerät | Datenbit 6 |
| 9 | 9 | DD8 | PC-\>Gerät | Datenbit 7 |
| 10 | 10 | Acknowledge | Gerät-\>PC | Daten wurden übernommen (Handshake) |
| 11 | 11 | Busy | Gerät-\>PC | Nicht empfangbereit für neue Daten |
| 12 | 12 | Paper Error | Gerät-\>PC | Kein Papier |
| 13 | 13 | Select | Gerät-\>PC | Gerät ist online |
| 14 | 14 | Auto Feed | PC-\>Gerät | Bei jedem CR (carriage return) ein LF (line feed) hinzufügen |
| \- | 15, 16 | GND oder NC | \- | Masse oder nicht benutzt |
| \- | 17 | Chassis-GND | \- | Gehäuse-Masse |
| \- | 18 | Extern +5V | Gerät-\>PC | +5V extern |
| 19-25 | 19-30 | GND | \- | Einzelne Signal-Messleitungen |
| 16 | 31 | Reset oder Init | PC-\>Gerät | Geräte-Initialisierung |
| 15 | 32 | Error or Fault | Gerät-\>PC | Drucker-Störung |
| 18 | 33 | Extern GND oder NC | Gerät-\>PC | Masse oder nicht belegt |
| \- | 34 | NC | \- | Keine Verbindung |
| \- | 35 | \#5V oder NC | \- | \#5V oder nicht belegt |
| 17 | 36 | Select In | PC-\>Gerät | Online schalten |

Somit ist es möglich, den Drucker über Ports anzusprechen und mit ihm zu kommunizieren.

  

## Register

Das BIOS kennt bis zu vier parallele Schnitstellen (bei einigen nur zwei):

- LPT1: 0x3BC
- LPT2: 0x378
- LPT3: 0x278
- LPT4: 0x2BC

Jede parallele Schnitstelle verfügt dabei über drei Register:

- Basisregister, enspricht dem Datenregister
- Statusregister
- Steuerregister

Das Statusregister hat gegenüber der Basisadresse einen Offset von 1 und das Steuerregister einen Offset von 2.

  

### Datenregister

In das Datenregister werden die zu sendenden Daten geschrieben. Wird eine Centronics-Schnitstelle verwendet, können Daten auch empfangen werden, welche sich dann ebenfalls im Datenregister befinden.

Die Datenregister sind D0 bis D7 und werden auf den Leitungen von D1 bis D8 übertragen.

  

### Statusregister

Vom Statusregister aus kann nur gelesen werden. Dort wird der Zustand der Peripherie gespeichert.

Die Statusregister sind D0 bis D7. Nachfolgen ein kleines Programm, um die Bits zu testen:

` mov ah, 02h xor dx, dx int 17h `

`test ah, 10000000b ; Bit 7 -> Drucker bereit? je error `

`test ah, 00100000b ; Bit 5 -> Kein Papier mehr? jne error `

`error: `

       jmp error

  

### Steuerregister

Ins das Steuerregister kann sowohl gelesen als auch geschrieben werden. Wird das 4. Bit gesetzt, wird ein Interrupt ausgelöst. Wird das 5. Bit gesetzt, ist eine Art bidirektionaler Übertragung möglich.

  

## IEEE 1284

Da der Centronics-Stecker kein Standard war, implementierten viele Druckerhersteller ihre eigenen Funktionen und belegten die Datenleitungen nach eigenen Vorlieben. Dadurch wurden schnell Inkompatibilitäten erreicht. Seit dem Jahr 1994 wird die parallele Schnittstelle um Funktionen erweitert, die unter anderem die bidirektionale Übertragung einführt. Diese Funktionen werden unter der IEEE Norm 1284 standardisiert.

  

## Siehe auch

- [Serielle Schnittstelle](https://github.com/lowlevel-eu/wiki/wiki/Serielle-Schnittstelle "Serielle Schnittstelle")

## Weblinks

- [IEEE_1284-Spezifikation](http://de.wikipedia.org/wiki/IEEE_1284)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/5378/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1996/index.html)

<!-- MediaWiki page 1996; revision 5378; parent 5353; 2009-08-06T19:25:43Z -->
