# Gameport

Der Gameport ist ein ein 15-poliger Anschluss, meist auf Soundkarten anzufinden (da er auch für MIDI verwendet wird). Er eignet sich besonders gut für Joysticks und Lenkräder, da die Daten vorher nicht vom jeweiligen Gerät bearbeitet werden müssen.

## Programmierung

Der Gameport wird über den [I/O-Port](I-O-Ports "I/O-Ports") 0x201 angesprochen. In ihm sind 8 Bits auf 2 Eingabegeräte aufgeteilt, und diese 4 Bits sind jeweils nochmal auf 2 Buttons und 2 Achsen geteilt.

| Bit | Beschreibung |
| ------- | ---------------------- |
| Bit 0 | Joystick A, X-Achse |
| Bit 1 | Joystick A, Y-Achse |
| Bit 2 | Joystick B, X-Achse |
| Bit 3 | Joystick B, Y-Achse |
| Bit 4 | Joystick A, Button 1 |
| Bit 5 | Joystick A, Button 2 |
| Bit 6 | Joystick B, Button 1 |
| Bit 7 | Joystick B, Button 2 |

### Buttons

Um den Status eines Buttons zu lesen, muss man nur das jeweilige Bit auslesen. 0b steht für Taste gedrückt und 1b für Taste losgelassen.

### Achsen

Um die Achsen auszulesen, muss man erst ein beliebigen Wert in den [I/O-Port](I-O-Ports "I/O-Ports") schreiben. Dadurch werden alle Achsen-Bits auf 1b gesetzt. Nun muss man die Zeit messen bis das jeweilige Bit wieder 0b wird. Da die Werte von Treiber zu Treiber abweichen, ist meistens eine Kalibrierung erforderlich.

### Kalibrierung

Da der Joystick keine linearen Werte zurückgibt, ist es sinnvoll nicht nur die Ecken als Bezugspunkte bei der Kalibrierung zu benutzen. Ansonsten würde sich die Mitte in Richtung einer Ecke verschieben. Man muss also auch die Mitte als Bezugspunkt nehmen. Je nachdem, ob der eingelesene Wert über der Mitte oder unter der Mitte liegt, wird dann ein anderer Skalierungsfaktor benutzt.

Es ist außerdem sinnvoll, in der Mitte eine kleine Deadzone einzurichten bei der dann sofort der Mittelwert zurückgegeben wird, da viele Joysticks beim Zurückschnappen nicht genau in der Mitte halten.

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/5369/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1674/index.html)

<!-- MediaWiki page 1674; revision 5369; parent 4863; 2009-08-06T18:17:46Z -->
