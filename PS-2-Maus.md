# PS/2-Maus

Die "Maus" zählt zu den **Human Interface Devices**, dient also als Schnittstelle zwischen dem Computer und dem Menschen.

## Funktionsweise

Die Maus teilt sich mit dem Keyboard die gleiche Schnittstelle, die PS/2-Schnittstelle. Damit unterschieden werden kann, welcher Befehl für welches Gerät ist, ist bei der Übertragung entweder das fünfte Bit im 54h-Status-Byte gesetzt (dann ist der Befehl für die Maus) oder nicht (dann ist der Befehl für die Tastatur).

  

## Spezifikationen

### Der PS/2-Port und der KBC

| Port | Zugriff | Beschreibung |
| --------- | ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **60h** | *Lesezugriff* | Der Port 60h ist zweiseitig, er kann als Keyboard-Controller(64h)-Daten-Port oder als Keyboard-In-/Output-Buffer dienen. An diesen Port werden die Scancodes der gedrückten Tasten gesendet, die dann der Keyboard-Treiber per "in al,60h" auslesen kann. Deaktiviert man bevor man aus diesem Port etwas ausliest das Keybord per Befehl ADh, so erhält man die Daten aus dem Maus-Output-Buffer. Zum Auslesen sei gesagt, dass dies nur geschehen sollte, wenn entweder das erste Bit im Keyboard-Controller-Output-Status-Byte, welches anzeigt, dass das Keyboard an 60h Daten sendet, oder das fünfte Bit in diesem Status-Byte des 64h gesetzt ist, welches anzeigt, dass im Maus-Output-Buffer Daten liegen.<br> |
|  | *Schreibzugriff* | Wenn an diesen Port geschrieben wird, fungiert dieser entweder als Keyboard-Controller-Daten-Port, oder als Input-Buffer des Keyboards. Zweiteres geschieht, wenn man einfach einen der Befehle, die weiter unten für diesen Port aufgelistet sind, an diesen Port sendet. Dies sind überwiegend Befehle zu adjustierung des Keyboards, wie z.b. das Einstellen der Typematic-Rate. Als Ersteres, also als Daten-Port des KBC, wird dieser Port nur genutzt, wenn es Befehle des 64h verlangen. So muss an z.b. den Befehl "60h" für das Senden eines neuen Commado-Bytes zwar an den Port 64h senden, doch das Commando-Byte, was dann nach korrekter Annahme des Befehls gesendet werden muss, muss an den Port 60h gesendet werden.<br>Für die möglichen Befehle, die an das Keyboard gesendet werden können, siehe [hier](#tastatur-befehle-60h). Für die möglichen Mausbefehle, die an diesen Port geschickt werden können, jedoch den Befehl "D4h" auf Port 64h voraussetzen, siehe [hier](#maus-befehle-60h). Für die KBC-Befehle, die ein zweites Daten-Byte an diesen Port geschickt verlangen, sie auch [hier](#keyboard-controller-befehle-64h).<br> |
| **64h** | *Lesezugriff* | Das Lesen für diesen Port ist sehr wichtig, wenn man den Keyboard-Controller programmieren will, da man beim Lesen das Status-Byte des KBC bekommt, welches z.b. anzeigt, ob gerade Daten zum abholen verfügbar sind, oder ob der letzte Befehl bereits vollständig verarbeitet wurde. Für die Bitfields des Statusbytes siehe [hier](#kbc-status-byte-64h)<br> |
|  | *Schreibzugriff* | Beim Schreibzugriff an diesen Port fungiert dieser als Keyboard-Controller-Input-Buffer, sodass eine Reihe von Byte-großen Befehlen gesendet werden können, die zumeist das System des Keyboards beeinflussen, so muss man auch an diese Port den Befehl "D4h" senden, um den nächsten Befehl, der zum Keyboard-Port(60h) geht, an die Maus senden zu lassen. Eine Reihe von Befehlen ist [hier](#keyboard-controller-befehle-64h) aufgelistet.<br> |

  

### Tastatur-Befehle (60h)

**Dies ist die Liste der Befehle, die an den Keyboard-Input-Buffer (60h) gesendet werden können. Werden zwei Bytes verlangt, wird das Zweite auch an den Port 60h gesendet.**

**Befehl:**

*EEh*

**Größe:**

1 Byte

**Beschreibung:**

Dieser Befehl sendet zur Diagnostik EEh an den Port 60h.

------------------------------------------------------------------------

**Befehl:**

*F0h*

**Größe:**

2 Bytes

**Beschreibung:**

Mit diesem Befehl kann, abhängig vom zweiten Byte das Scancode Set, entweder gesetzt oder abgerufen werden

Das Format des zweiten Bytes:

00h - holt den aktuellen Scancode Set ab, sodass dieser an den Port 60h gesendet wird

01h - scancode set 1 (PCs and PS/2 mod 30, except Type 2 ctrlr)

02h - scancode set 2 (ATs, PS/2, default)

03h - scancode set 3

------------------------------------------------------------------------

**Befehl:**

*F2h*

**Größe:**

1 Byte

**Beschreibung:**

Keyboard ID auslesen

-\> AT Keyboards liefern als Wert FAh (ACK) zurück

-\> MF2 Keyboards liefern ABh + 41h oder aber auch ABh 83h an den Port 60h

------------------------------------------------------------------------

**Befehl:**

*F3h*

**Größe:**

2 Bytes

**Beschreibung:**

Setze die typematic rate/delay. Der Typematic-Delay gibt an, ab wann der Scancode der gedrückten Taste wiederholt an 60h gesendet wird,

die Typematic-Rate dagegen gibt an, wie oft dann der Scancode pro Sekunde gesendet wird. Das Format des zweiten Byte:

Bit 7  : 0 (reserved)

Bit 6-5 : geben die Typematic Delay an

                   00 = 250ms                01 = 500ms
                   10 = 750ms                11 = 1000ms

Bit 4-0 : diese beiden geben die Typematic-Rate an, die sich wie folgt zusammen stellt:

1/( (8+A) \* 2^B \* 0,00417 ) pro Sekunde A-\>Bits 2-0 B-\>Bits 4-3

die Formel ein wenig umgestellt:

240/( (8+A) \* 2^B ) pro Sekunde -\> denn ~0,00417 = 1/240

Bei 00000b würde das dann so aussehen:

     1/ ( (8+0) * 2^0 * 0,00417 )    ->    1/(8*0.00417)    ->    ~30 Widerholungen pro Sekunde

Bei 11111b würde es dagegen so aussehen:

     1/ ( (8+7) * 2^3 * 0,00417 )    ->    1/(120*0,00417) ->    ~2 Wiederholungen pro Sekunde

------------------------------------------------------------------------

**Befehl:**

*F4h*

**Größe:**

1 Byte

**Beschreibung:**

Aktivieren des Keyboards

------------------------------------------------------------------------

**Befehl:**

*F5h*

**Größe:**

1 Byte

**Beschreibung:**

Deaktivieren des Keyboards. Wird auch genutzt, wenn etwas aus dem Maus-Output-Buffer gelesen werden soll

------------------------------------------------------------------------

**Befehl:**

*F6h*

**Größe:**

1 Byte

**Beschreibung:**

set default parameters

------------------------------------------------------------------------

**Befehl:**

*F7h*

**Größe:**

1 Byte

**Beschreibung:**

set all keys to typematic (scancode set 3)

------------------------------------------------------------------------

**Befehl:**

*F8h*

**Größe:**

1 Byte

**Beschreibung:**

set all keys to make/release

------------------------------------------------------------------------

**Befehl:**

*F9h*

**Größe:**

1 Byte

**Beschreibung:**

set all keys to make only

------------------------------------------------------------------------

**Befehl:**

*FAh*

**Größe:**

1 Byte

**Beschreibung:**

set all keys to typematic/make/release

------------------------------------------------------------------------

**Befehl:**

*FBh*

**Größe:**

1 Byte

**Beschreibung:**

set all keys to typematic

------------------------------------------------------------------------

**Befehl:**

*FCh*

**Größe:**

2 Bytes

**Beschreibung:**

set specific key to make/release

------------------------------------------------------------------------

**Befehl:**

*FDh*

**Größe:**

2 Bytes

**Beschreibung:**

set specific key to make only

------------------------------------------------------------------------

**Befehl:**

*FEh*

**Größe:**

1 Byte

**Beschreibung:**

resend last scancode

------------------------------------------------------------------------

**Befehl:**

*FFh*

**Größe:**

1 Byte

**Beschreibung:**

perform internal power-on reset function

  

### Maus-Befehle (60h)

**Dies ist die Liste der Befehle, die zur Adjustierung der Maus dienen. Bevor einer dieser Befehle an den Port 60h gesendet werden kann, muss zuerst per "D4h" an den Port 64h, dem Controller gesagt werden, dass das nächste Byte, also eins aus dieser Liste, auch an die Maus gesendet wird. Wird "D4h" nicht zuvor verwendet, würde der Befehl an die Tastatur und nicht die Maus gehen. **Achtung**: Bei zwei Byte großen Befehlen muss auch vor dem Senden des zweiten Bytes dies mit "D4h" initiiert werden.**

| Befehl | Größe | Beschreibung |
| -------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| *E6h* | 1 Byte | Setze Maus-Scaling auf 1:1 |
| *E7h* | 1 Byte | Setze Maus-Scaling auf 2:1 |
| *E8h* | 2 Bytes | Setze Maus-Auflösung. Das zweite Byte sieht dabei wie folgt aus:<br>00h=1/mm<br>01h=2/mm<br>02h=4/mm<br>03h=8/mm |
| *E9h* | 1 Byte | Hole Status-Information -\> liest 2 Bytes aus, die wie folgt aufgebaut sind<br>Byte 0 - Bitmaske (Beschreibung gilt, wenn Bit=1 ist, ansonsten gilt das logische ander):<br>7 = Reserved (0)<br>6 = Remote rather than Stream mode<br>5 = Maus ist aktiviert<br>4 = Scaling auf 2:1 gesetzt<br>3 = Reserved (0)<br>2 = Linke Maustaste ist gedrückt<br>1 = Reserved (0)<br>0 = Rechte Maustaste ist gedrückt<br>Byte 1 = Auflösung (siehe Befehl E8h) |
| *EAh* | 1 Byte | Versetze Maus in den Stream-Modus. In diesem aktiviert die Maus bei jeder Änderung den IRQ12, sodass dieser die Daten auslesen kann |
| *EBh* | 1 Byte | Hole Maus-Data-Paket. Sollte nur genutzt werden, wenn der Remote-Modus gesetzt ist. Für eine Beschreibung des Pakets, siehe [hier](#das-maus-daten-packet) |
| *ECh* | 1 Byte | Versetze Maus aus den Wrap-Modus wieder in den normalen Modus. Der Wrap-Modus ist zur Fehleranalyse gedacht und echoet jeden Befehl, statt ihn mit FAh zu bestätigen. |
| *EEh* | 1 Byte | Betrete Wrap-Mouds |
| *F0h* | 1 Byte | Versetze Maus in den Remote-Modus statt ihn den Stream-Modus. In diesem Modus sendet die Maus die Daten nur beim Befehl EBh |
| *F2h* | 1 Byte | Lese MausID. Returns 00h (siehe auch bei den [SpecialCodes](#spezial-codes-als-r%C3%BCckgabe-von-befehlen-60h)) |
| *F3h* | 2 Bytes | Setze die Maus-Sample-Rate, also wie oft die Maus Daten abfragen soll. Das zweite Byte kann dann so aussehen:<br>0Ah=10/s 50h= 80/s<br>14h=20/s 64h=100/s<br>28h=40/s C8h=200/s<br>3Ch=60/s |
| *F4h* | 1 Byte | Aktiviere die Maus und setze den Modus auf Stream. In diesem Modus wird bei jeder Veränderung der IRQ12 aufgerufen |
| *F5h* | 1 Byte | Deaktiviere die Maus im Stream-Modus und setze die vorgegebenen Parameter |
| *F6h* | 1 Byte | Stelle alles auf die Vorgaben zurück -\> StreamMode, 4/mm-Maus-Resolution, Scaling 1:1, 100/s-Sample-Rate |
| *FEh* | 1 Byte | Sende das letzte Maus-Data-Paket erneut (für Beschreibung des Pakets siehe [hier](#das-maus-daten-packet)) |
| *FFh* | 1 Byte | Reset Maus |

  

#### Spezial-Codes als Rückgabe von Befehlen (60h)

**Spezial-Code Liste - Spezial-Codes werden an den Port 60h nach Befehlen geschickt**

| **Code** | **Beschreibung** |
| ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| *00h* | (Maus) ID |
| *9Ch* | Dieser Code wird empfangen, wenn die Maus in den Streaming-Modus geschickt wurde, bevor ein Handler für den IRQ 12 initialisiert wurde. |
| *AAh* | BAT completion code (sent after errorfree Basic Assurance Test) |
| *ABh* | Das erste der zwei Bytes, die bei MF2-Keyboards als ID geliefert werden (siehe Befehl F2h) |
| *EEh* | Wird als Echo bei der Selbstdiagnostik zurückgegeben (siehe Befehl EEh) |
| *F0h* | Keyboard Break Code |
| *FAh* | Acknowledge (ACK) - wird nach jedem Befehl an den Port 60 außer dem Resend und Echo bei der Tastatur und ECh, F2h, FFh bei der Maus gesendet<br> |
| *FCh* | bei MF2-Keyboards wird dies bei einen BAT-Fehler, also einem Fehler in der zweiten Hälfte des Power on self test, geliefert |
| *FDh* | das selbe wie FCh nur bei AT-Keyboards (AT ist der derzeitige Standard) |
| *FEh* | dieser Befehl sagt, dass letzte Befehl nocheinmal gesendet werden soll |

### KBC-Status-Byte (64h)

**Bitfelder des Statusbytes, das beim Lesen des 64h's geliefert wird**

|  | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| ----- | ------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ | -------------------- | --------------------------------------------------------------------------- | ------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| 0 |  |  | Es liegen keine Daten für bereit | Keyboard verfügbar | Das letzte geschriebene Byte waren Daten und gingnen an den Port 60h | power up or reset | Der Input-Buffer ist leer und alle Befehle sind verarbeitet, nun kann ein Befehl gesendet werden | Es liegen keine Daten bereit und es sollte somit auch noch nichts aus dem Port 60h ausgelesen werden |
| 1 | Parity-Error bei der letzten Übertragung vom Keyboard | Ein Time-Out-Error ist aufgetreten, das heißt, dass die Maus oder die Tastatur nicht reagiert hat. Sollte dieser Fehler auftreten sollte mann den Resend-Befehl nutzen. | Die Maus hat Daten für uns im Maus-Output-Buffer bereit leigen und sollten nun abgeholt werden | Keyboard gesperrt | Das letzte geschrieben Byte war ein Befehl und ging somit an den Port 64h | Selftest OK | Der Input-Buffer hat noch Daten, also es liegt noch der zuletzt gesendete Befehl in 60h/64h und wartet auf seine Verarbeitung | Im OutputBuffer befinden sich Daten für den User. |

### Keyboard-Controller-Befehle (64h)

**Dies ist die Liste der Befehle, die an den Keyboard-Controller (64h) gesendet werden können. Werden zwei Bytes verlangt, wird das Zweite an den Port 60h gesendet.**

| Befehl | Größe | Beschreibung |
| -------- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| *20h* | 1 Byte | Dieser Befehl sendet das derzeitige Commando-Byte an den Port 60h, wo es vom User abgeholt werden muss. Der Aufbau des Commando-Bytes ist folgendermaßen (Beschr. gilt, wenn Bit=1 ist, ansonsten gilt das Gegenteil):<br><br>7 - reserved (0)<br>6 - IBM PC Kompatibilitäts-Modus - Auch XLAT, konvertiert wie der Befehl, alle Scancodes zu Set 1, ansonsten werden Roh-Daten<br>geliefert. -\> dieses Bit muss gelöscht sein, bevor man die Scancode-Sets per F0h wechselt, denn sonst nur Kauderwelsch ensteht :)<br>5 - IBM PC Kompatibilitäts-Modus - 0 - use 11-bit codes, 1 - use 8086 codes<br>4 - deaktiviere Keyboard<br>3 - ignoriere Sicherheitsverschluss-Status<br>2 - System Flag<br>1 - Aktiviert die Aktivierung des IRQ12, wenn Mausdaten, wie das MouseDataPacket, im Buffer vorhanden sind (Bit5 bei 64h gesetzt)<br>0 - Aktiviert die Aktivierung des IRQ1, wenn Tastaturdaten, wie Scancodes, im Buffer vorhanden sind (Bit1 bei 64h gesetzt)<br>Notiz: Eigentlich sind bloß Bit 0 und 1 und evtl. noch Bit 4 für uns interessant!<br> |
| *60h* | 2 Bytes | Dieser Befehl sendet das 2.Byte, Commando-Byte an den Keyboard-Controller. Commando-Byte-Bechreibung siehe 20h |
| *A4h* | 1 Byte | Prüfe, ob ein Passwort installiert ist, wenn ja gibt es FAh und wenn nicht F1h an den Port 60h aus |
| *A5h* | 1 Byte | Lade das Passwort. Das Passwort wird als Byte-Stream an den Port 60h gesendet und endet mit einem Byte=00h |
| *A6h* | 1 Byte | Prüfe Passwort |
| *A7h* | 1 Byte | Deaktiviere den Maus-Port, sodass die Maus wir deaktiviert |
| *A8h* | 1 Byte | Aktiviere die Maus |
| *A9h* | 1 Byte | Teste Mausport, das Ergebnis wird an 60h geschickt und kann folgendermaßen aussehen:<br>00h - no error<br>01h - keyboard clock line stuck low<br>02h - keyboard clock line stuck high<br>03h - keyboard data line is stuck low<br>04h - keyboard data line stuck high<br>05h - (Compaq only) diagnostic feature<br>FFh - Total error |
| *AAh* | 1 Byte | Initiiert Selftest und sendet bei erfolgreichen Test 55h an 60h, bei Fehler jedoch FCh an 60h |
| *ABh* | 1 Byte | Testet das Interface, für mögliche Ergebnisse siehe Befehl A9h |
| *ADh* | 1 Byte | Deaktiviere Keyboard (Bit 4 in Commando-Byte). |
| *AEh* | 1 Byte | Aktiviere Keyboard wieder (Bit 4 in commando-Byte) |
| *C0h* | 1 Byte | Lese Inputport-Byte nach 60h aus. Dieses ist wie folgt aufgebaut<br>7 - Keyboard aktiviert/nicht gesperrt<br>6 - 0 - Video ist CGA (Farbe)<br>1 - Video ist MDA (schwarz/weiß)<br>5 - 0 - Manufaktur-jumper ist installiert (Manufaktor-Testmodus)<br>1 - normal<br>4 - war früher dafür da um die Größe des Ram zu symbolisieren, wir aber nicht mehr genutzt<br>3 - reserved<br>2 - Keyboard hat kein Strom<br>1 - current mouse serial data input state<br>0 - current keyboard serial input state |
| *D0h* | 1 Byte | Lese das Ouputport-Byte und platziere in auf Port 60h um ihn dort abholen lassen zu können. Das Byte sieht folgendermaßen aus(Beschr. gilt, wenn Bit=1 ist):<br><br>7 - keyboard data (output)<br>6 - keyboard clock (output/signal)<br>5 - In OutputBuffer ist ein Mausbyte (sobald dies gesetzt ist wird IRQ12 aufgerufen, sofern Bit1 im Commando-Byte gesetzt ist)<br>4 - In OutputBuffer sind Daten der Tastatur byte (aktiviert IRQ1, sofern Bit0 im Commando-Byte gesetzt ist)<br>3 - mouse data (output)<br>2 - mouse clock (output)<br>1 - Aktiviere die A20-Gate<br>0 - System reset/Reset processor<br>Notiz: Bit 0 sollte immer gesetzt sein, wenn man per D1h das Outputport-Byte schreibt :)<br> |
| *D1h* | 2 Bytes | Das zweite Byte ist das Outpuport-Byte, welches somit das Outputport-Byte neu setzt. siehe auch Befehl D0h |
| *D2h* | 2 Bytes | Dieser Befehl schreibt das zweite Byte in den Output-Buffer des Keyboards (60h) |
| *D3h* | 2 Bytes | Dieser hingegen schreibt das zweite Byte in den Output-Buffer der Maus (auch 60h, aber zum auslesen muss die Tastatur deaktiviert sein) |
| *D4h* | 1 Byte | Dies ist der wichtigstste Befehl, den wir für unsere Mau benötigen, denn mit diesen Befehl wird der Tastatur gesagt, dass das nächste Byte, was an den Port 60h gesendet wird nicht an den Tastatur-Controller sondern an die Maus gesendet werden soll. Für eine Liste der möglichen Mausbefehle siehe hier.<br> |
| *EDh* | 2 Bytes | Dieser Befehl ist zum löschen und anschalten der LEDs der Tastatur. Wenn das entsprechende Bit 1 ist, ist die LED an, ansonsten aus.<br>Bit 7-3  : 0 = reserved<br>Bit 2  : 0 = Caps Lock LED off -\> 1 = on<br>Bit 3  : 0 = Num Lock LED off -\> 1 = on<br>Bit 4  : 0 = Scroll Lock LED off -\> 1 = on |

## Das Maus-Daten-Packet

### Normal-Mode-Packet

Die Sache mit dem Daten-Paket ist eigentlich recht einfach, immer wenn der IRQ12 ausgelöst wird, liegt ein Datenpaket im Maus-Output-Buffer, was Byteweise abgeholt werden sollte, wenn Bit5 im 64h-Status-Byte gesetzt ist. Das Daten-Paket ist dabei wie folgt aufgebaut:

<table>
<tbody><tr>
<th></th>
<th>7</th>
<th>6</th>
<th>5</th>
<th>4</th>
<th>3</th>
<th>2</th>
<th>1</th>
<th>0
</th></tr>
<tr>
<th>Byte 1
</th>
<td>Y overflow</td>
<td>X overflow</td>
<td>Y sign bit</td>
<td>X sign bit</td>
<td>Reserved (1)</td>
<td>Middle Button pressed</td>
<td>Right Button pressed</td>
<td>Left Button pressed
</td></tr>
<tr>
<th>Byte 2
</th>
<td colspan="8">X Movement seit dem letztem Daten-Paket
</td></tr>
<tr>
<th>Byte 3
</th>
<td colspan="8">Y Movement seit dem letztem Daten-Paket
</td></tr></tbody></table>

Die Overflow-Bits geben an, ob die Maus auf der jeweiligen Achse zu schnell bewegt wurden. Die Sign-Bits geben an, ob die jeweiligen Movements negativ sind. Und die Button-Bits geben an, ob die jeweilige Taste gedrückt ist.

### Wheel-Mode-Packet

Wie manch einer vlt. bemerkt hat, fehlt bei dem Daten-Paket noch was... nämlich das Rad und evtl. die Tasten 4+5. Das Problem ist, dass auch Mäuse, die ein Rad besitze zuerst nur diese Daten an die Maus senden, da dies aus Kompatibilitätsgründen notwendig ist, sonst könnte man ja keine alte Maus an einem neuen PC anschließen und anderes. Um nun den Wheel-Modus der Maus zu betreten, reagieren neuere Mäuse auf eine bestimmte Befehlsequenz, die wie folgt aussieht:

Setze Sample-Rate auf 200 reports/s

Setze Sample-Rate auf 100 reports/s

Setze Sample-Rate auf 80 reports/s

Wenn dies erfolgreich gesendet wurde und gleich danach mit F2h die MausID abgefragt wird, senden normale/alte PS2-Mäuse 00h, wie in den Tabellen oben beschrieben. Neuere Mäuse jedoch, die ein Mausrad besitzen, senden als ID 03h. Diese ID sagt dann dem Maustreiber auch, dass ab jetzt die Daten-Pakete 4 Byte groß sind und wie folgt aussehen:

<table>
<tbody><tr>
<th></th>
<th>7</th>
<th>6</th>
<th>5</th>
<th>4</th>
<th>3</th>
<th>2</th>
<th>1</th>
<th>0
</th></tr>
<tr>
<th>Byte 1
</th>
<td>Y overflow</td>
<td>X overflow</td>
<td>Y sign bit</td>
<td>X sign bit</td>
<td>Reserved (1)</td>
<td>Middle Button pressed</td>
<td>Right Button pressed</td>
<td>Left Button pressed
</td></tr>
<tr>
<th>Byte 2
</th>
<td colspan="8">X Movement seit dem letztem Daten-Paket
</td></tr>
<tr>
<th>Byte 3
</th>
<td colspan="8">Y Movement seit dem letztem Daten-Paket
</td></tr>
<tr>
<th>Byte 4
</th>
<td colspan="8">Z Movement seit dem letztem Daten-Paket
</td></tr></tbody></table>

Byte 4, also die Z-Bewegung kann eigentlich nur Werte von -8(1111) bis +7(0000) annehmen und nutzt deswegen eigentlich nur Bit 3-0, die anderen Bits dienen dabei nur als Sign-Extension, also nehmen den Zustand von Bit3 an.

### Wheel-and-5-Button-Mode-Packet

Nun habt ihr aber sicher auch schon gemerkt, dass im vierten Byte noch vier Bits frei sind und wir noch nicht die Status der 4. und 5. Taste bekommen, falls diese vorhanden wären. Damit diese Status auch mit dem vierten Byte mitgesendet werden, gibt es dafür auch wieder eine Sequenz um dies zu aktivieren, die wie folgt aussieht:

Setze Sample-Rate auf 200 reports/s

Setze Sample-Rate auf 200 reports/s

Setze Sample-Rate auf 80 reports/s

Der Code zum Aktivieren des Rades und der 5 Button sollte ganz einfach aus einer modifizierten Version des Quellcodes zum Aktivieren des Wheel-Modus möglich sein. Wenn die Maus die Tasten 4 und 5 unterstützt, dann sendet sie nach dem GetDeviceID(F2h) 04h, statt 00h und sendet ab sofort folgendes Maus-Daten-Paket:

<table>
<tbody><tr>
<th></th>
<th>7</th>
<th>6</th>
<th>5</th>
<th>4</th>
<th>3</th>
<th>2</th>
<th>1</th>
<th>0
</th></tr>
<tr>
<th>Byte 1
</th>
<td>Y overflow</td>
<td>X overflow</td>
<td>Y sign bit</td>
<td>X sign bit</td>
<td>Reserved (1)</td>
<td>Mittlere Taste gedrückt</td>
<td>Rechte Taste gedrückt</td>
<td>Linke Taste gedrückt
</td></tr>
<tr>
<th>Byte 2
</th>
<td colspan="8">X-Bewegung seit dem letztem Daten-Paket
</td></tr>
<tr>
<th>Byte 3
</th>
<td colspan="8">Y-Bewegung seit dem letztem Daten-Paket
</td></tr>
<tr>
<th>Byte 4
</th>
<td colspan="2">reserved (0)</td>
<td>5. Maustaste</td>
<td>4. Maustaste</td>
<td colspan="4">Z-Bewegung seit dem letztem Daten-Paket
</td></tr></tbody></table>

Hierbei enthalten die 4 Bits für die Mausradbewegung (Z) sowohl die Bewegung in horizontale, als auch vertikale Richtung (Es werden also zwei Mausräder unterstützt):

| Wert | Bedeutung |
| ------ | ------------------------ |
| +-1 | vertikales Scrollrad |
| +-2 | horizontales Scrollrad |

## Siehe auch

- [PS/2-Maus Tutorial](https://github.com/lowlevel-eu/wiki/wiki/PS-2-Maus-Tutorial "PS/2-Maus Tutorial")
- [Keyboard Controller](https://github.com/lowlevel-eu/wiki/wiki/Keyboard-Controller "Keyboard Controller")

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/9408/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1559/index.html)

<!-- MediaWiki page 1559; revision 9408; parent 9404; 2011-02-03T17:10:38Z -->
