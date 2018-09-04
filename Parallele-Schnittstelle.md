# Parallele Schnittstelle

Die **parallele Schnittstelle** ist eine Schnittstelle am PC zur Übertragung von Daten an Peripheriegeräte.

  

## Funktionsweise

Die parallele Schnittstelle ist primär für die Übertragung von Daten an Peripheriegeräte gedacht und eignet sich nur gering für die bidirektionale Übertragung. Meistens wird an ihr ein Drucker angeschlossen, für den es einen besonderen 36-poligen Druckeranschluss (auch Centronics, nach dem ehemaligen Drucker-Hersteller benannt) gibt. Der parallele Anschluss an sich ist 25-polig und wird als *männlich* bezeichnet.

Die Bestätigung für die Datenannahme erfolgt von Peripherie-Seite mit dem sogenannten Handshake (ein, sehr vereinfacht ausgedrückt, beidseitiges Einverständnis zur Übertragung der Daten), und zwar nach dem 2-Wege- und 3-Wege-Verfahren (siehe dazu [\[1\]](http://de.wikipedia.org/wiki/Drei-Wege-Handshake)).

### Spezielle Funktionsweise bei Druckern

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
| 9 | 9 | D8 | PC-\>Gerät | Datenbit 7 |
| 10 | 10 | Acknowledge | Gerät-\>PC | Daten wurden übernommen (Handshake) |
| 11 | 11 | Busy | Gerät-\>PC | Nicht empfangsbereit für neue Daten |
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

Das BIOS kennt bis zu vier parallele Schnittstellen (bei einigen nur zwei):

- LPT1: 0x3BC
- LPT2: 0x378
- LPT3: 0x278
- LPT4: 0x2BC

Jede parallele Schnittstelle verfügt dabei über drei Register:

- Basisregister, enspricht dem Datenregister
- Statusregister
- Steuerregister

Das Statusregister hat gegenüber der Basisadresse einen Offset von 1 und das Steuerregister einen Offset von 2.

  

### Datenregister

In das Datenregister werden die zu sendenden Daten geschrieben. Wird eine Centronics-Schnittstelle verwendet, können Daten auch empfangen werden, welche sich dann ebenfalls im Datenregister befinden.

Die Datenregister sind D0 bis D7 und werden auf den Leitungen von D1 bis D8 übertragen.

  

### Statusregister

Vom Statusregister aus kann nur gelesen werden. Dort wird der Zustand der Peripherie gespeichert.

Die Bits haben folgende Bedeutung:

| Bit | Signal-Bezeichnung | Info |
| ----- | -------------------- | ----------------------------------------------------------- |
| 0 | \- | unbenutzt |
| 1 | \- | unbenutzt |
| 2 | \- | unbenutzt |
| 3 | /ERROR | 0 = Fehler |
| 4 | SELECT | 1 = Drucker ist On-Line (Selected) |
| 5 | PE | 1 = Drucker hat kein Papier mehr (Paper Error) |
| 6 | /ACK | 0 = Drucker ist für nächstes Zeichen bereit (Acknowledge) |
| 7 | /BUSY | 0 = Drucker ist beschäftigt |

Nachfolgend ein kleines Programm, um die Bits zu testen:

``` asm
    mov ah, 02h
    xor dx, dx
    int 17h

    test ah, 10000000b ; Bit 7 -> Drucker bereit?
    je error

    test ah, 00100000b ; Bit 5 -> Kein Papier mehr?
    jne error

error:
    jmp error
```

### Steuerregister

In das Steuerregister kann sowohl gelesen als auch geschrieben werden. Wird das 4. Bit gesetzt, wird ein Interrupt ausgelöst. Wird das 5. Bit gesetzt, ist eine Art bidirektionaler Übertragung möglich.

  
Die Bits haben folgende Bedeutung:

| Bit | Signal-Bezeichnung | Info |
| ----- | -------------------- | ---------------------------------------------- |
| 0 | /STROBE | 0 = Daten liegen auf D0 - D7 an |
| 1 | AUTO FEED | 1 = LF nach CR (auto linefeed) |
| 2 | /INIT | 0 = Reset des Druckers herbeiführen |
| 3 | SELECT IN | 1 = Drucker on-line schalten (Select Input) |
| 4 | IRQ Enable | 1 = Interrupt auslösen, wenn /ACK auf 0 geht |
| 5 | \- | unbenutzt |
| 6 | \- | unbenutzt |
| 7 | \- | unbenutzt |

  

## IEEE 1284

Da der Centronics-Stecker kein Standard war, implementierten viele Druckerhersteller ihre eigenen Funktionen und belegten die Datenleitungen nach eigenen Vorlieben. Dadurch wurden schnell Inkompatibilitäten erreicht. Seit dem Jahr 1994 wird die parallele Schnittstelle um Funktionen erweitert, die unter anderem die bidirektionale Übertragung einführt. Diese Funktionen werden unter der IEEE Norm 1284 standardisiert.

Unter anderem gibt es nun neue Modi zur Dateiübertragung.

### Compatible Mode

Der Compatible Mode dient dazu, dass ältere Drucker an einer IEEE-1284-Schnitstelle benutzt werden können. Der Modus entspricht einer Centronics-Verbindung mit der oben genannten Registerbelegung.

  

### Nibble Mode

Beim Nibble Mode arbeitet die Schnittstelle mit einer Breite von 4 Bit (einem Halbbyte, auch Nibble). Die restlichen 4 Bit werden gebraucht, damit Daten vom Gerät zum PC zurückgeschickt werden können, es ist also eine Art bidirektionale Verbindung möglich.

  

### Byte Mode

Der Byte Mode entspricht dem bidirektionalen Centronics Mode, der mit der damaligen PS/2-Architektur standardmäßig eingeführt wurde. Im Gegensatz zum obigen Nibble Mode werden die Daten hier byteweise über das Datenregister übertragen bzw. ausgetauscht. Dabei ist das Datenregister sowohl für die Sende- als auch die Empfangsdaten verantwortlich. Um die Übetragungsrichtung zu ändern, muss hier das fünfte Bit im Steuerregister dementsprechend gesetzt werden (gesetzt: Senden; gelöscht: Empfangen).

  

### Enhanced Parallel Port Mode

Dieser Modus ist von Intel, Xircom und Zenith entwickelt worden und wird am häufigsten implementiert. Hier können Daten sowie Adressen bidirektional ebenfalls übertragen werden und es können bis zu 256 Geräte (bei 8-Bit-Adressbus, in Form von Schaltungen) mit Hilfe eines Hubs verbunden, angesprochen und in einem Pool verwaltet werden. Allerdings kann auch ein Gerät die bis zu 256 Schaltungen erhalten, was besonders für Multifunktionsgeräte geeignet ist. Die Datenübertragungsrate beträgt 2 MB/s und es können bis zu 5 Meter überbrückt werden.

Die Daten werden in diesem Modus in bestimmten Zyklen übertragen.

  

### Enhanced Capability Mode

Dieser Modus wurde von Microsoft und Hewlett-Packard (HP) entwickelt und verfügt über ähnliche Eigenschaften wie der EPP-Mode. Allerdings sind hier nur maximal 128 Schaltungen (also maximal 128 miteinander verbundene Geräte) möglich.

## Siehe auch

- [Serielle Schnittstelle](https://github.com/lowlevel-eu/wiki/wiki/Serielle-Schnittstelle "Serielle Schnittstelle")
- [SCSI - Ebenfalls eine parallele Schnittstelle](https://github.com/lowlevel-eu/wiki/wiki/Small-Computer-System-Interface "SCSI")

## Weblinks

- [IEEE-1284-Spezifikation](http://de.wikipedia.org/wiki/IEEE_1284)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/11387/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1996/index.html)

<!-- MediaWiki page 1996; revision 11387; parent 11386; 2018-09-04T09:48:29Z -->
