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

**Dies ist die Liste der Befehle, die zur Adjustierung der Maus dienen. Bevor einer dieser Befehle an den Port 60h gesendet werden kann, muss zuerst per "D4h" an den Port 64h, dem Controller gesagt werden, dass das nächste Byte, also eins aus dieser Liste, auch an die Maus gesendet wird. Wir "D4h" nicht zuvor verwendet, würde der Befehl an die Tastatur und nicht die Maus gehen. **Achtung**: Bei zwei Byte großen Befehlen muss auch vor dem Senden des zweiten Bytes dies mit "D4h" initiiert werden.**

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
| *F5h* | 1 Byte | Deaktivierz die Maus im Stream-Modus und setze die vorgegebenen Parameter |
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

Die Overflow-Bits geben an, ob die Maus auf der jeweiligen Achse zu schnell bewegt wurden. Die Sign-Bits geben an, ob die jeweiligen Movements negativ sind. Und die Button-Bits geben an, ob die jeweilige Taste gedrückt ist. Der Beispiel-Code, der das Daten-Paket der Maus abholt ist beim Code für den [IRQ12-Handler](#handler-code) in der Rubrik Anwendung zu finden.

\<asm\>

     147 irq12-handler:
      . zum Anschauend des Codes gehe bitte zum IRQ12-Handler in der Rubrik Anwendung (Link in Text oben)
      .
      .
      .
     286 .read.mouse:
     287     push cx             ;cx sichern
     288     mov cx,0FFFFh       ;auf cx die Höchstmögliche Zahl schieben, damit getmb nicht alles aufhält, nur da es auf ein Byte wartet
     289     .waitforbytes:      ;und da loop zuerst dekremntiert und dann vergleicht, obs 0 ist, ist 0 die höchste Zahl für cx
     290         in al,64h           ;nach al das Statusregister vom Keyboard-Contoller holen
     291         test al,20h         ;und schauen, ob Bit5 gesetzt ist, ob im Mouse-Output-Buffer Daten warten
     292         jnz .byte_ready     ;wenn ja, dann springe aus dem loop heruas
     293     loop .waitforbytes  ;ansonsten führe loop-schleife fort, spätestens bis cx 0 ist
     294         pop cx              ;stelle cx wieder her
     295         mov ah,1            ;zeroflag löschen, indem 1 auf ah gemoved wird, damit dies dem anwender gegeben werden kann
     296         or ah,ah            ;und setze ggf. das zeroflag, damit der user gleich danach jz o.ä. schreiben kann
     297         ret                 ;und springe zum Aufrufsort zurück
     298     .byte_ready:        ;wenn IP hier ist, dann wartet ein Byte darauf abgeholt zu werden
     299     in al,60h           ;jetzt holen wir vom Mouse-Output-Buffer das lang ersehnte Byte :)
     300     pop cx              ;und cx wiederherstellen
     301     xor ah,ah           ;und lösche ah, da bei fehler auf ah der errorcode ist; setze ggf. zeroflag (macht xor...)
     302     ret                 ;zum Abschluss springen wir zum Aufrufsort zurück; das Byte liegt dabei in al und ZF zeigt Erfolg bei 1 an
     303 ;************************* wartet eine Weile ob Daten kommen und speichert diese ggf. in al ab *************************

\</asm\>

Besonders interessant ist eig. nur die Prozedur kb.read.mouse, die vom irq12 3x angesprungen wird, um die einzelnen Bytes des Maus-Pakets abzurufen. Der Rest des Codes des IRQ12's speichert diese Bytes, untersucht diese Bytes und verändert die xy-Coordinate des Mauszeigers in den Variablen \[x\] und \[y\] entsprechend der Movement- und Sign-Bits.

### Wheel-Mode-Packet

Wie manch einer vlt. bemerkt hat, fehlt bei dem Daten-Paket noch was... nämlich das Rad und evtl. die Tasten 4+5. Das Problem ist, dass auch Mäuse, die ein Rad besitze zuerst nur diese Daten an die Maus senden, da dies aus Kompatibilätsgründen notwendig ist, sonst könnte man ja keine alte Maus an einem neuen PC anschließen und anderes. Um nun den Wheel-Modus der Maus zu betreten reagieren neuere Mäuse auf eine bestimmte Befehlsequenz, die wie folgt aussieht:

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

Byte 4, also die Z-Bewegung kann eigentlich nur Werte von -8(1111) bis +7(0000) annehmen und nutzt deswegen eigentlich nur Bit 3-0, die anderen Bits dienen dabei nur als Sign-Extension, also nehmen den Zustand von Bit3 an (man schlage auch mal die Befehle movsx, movzx nach x) ). Dazu noch der Code, der in den Wheel-Mode schaltet, der Code zum abholen sollte klar sein, dass ist der selbe wie bei dem Standard-Paket nur, dass noch per call kb.read.mouse ein Byte mehr abgeholt werden muss. Der COde gibt am Ende noch die ID plus dem Error auf ah aus... dafür die Zeilen 45-47.

\<asm\>

      71     mov al,0F3h         ;Befehl zum senden und neu setzen der SampleRate auf al schieben
      72     call kb.write.mouse ;und per vordefinierter Prozedur an die Maus senden
      73     mov al,0C8h         ;dann das zweite Byte des Befehls, die Sample-Rate (200 reports/s) auf al kopieren
      74     call kb.write.mouse ;und auch dies per vordefinierter Prozedur an die Maus senden
      75     mov al,0F3h         ;Befehl zum senden und neu setzen der SampleRate auf al schieben
      76     call kb.write.mouse ;und per vordefinierter Prozedur an die Maus senden
      77     mov al,0C8h         ;dann das zweite Byte des Befehls, die Sample-Rate (200 reports/s) auf al kopieren
      78     call kb.write.mouse ;und auch dies per vordefinierter Prozedur an die Maus senden
      79     mov al,0F3h         ;Befehl zum senden und neu setzen der SampleRate auf al schieben
      80     call kb.write.mouse ;und per vordefinierter Prozedur an die Maus senden
      81     mov al,50h          ;dann das zweite Byte des Befehls, die Sample-Rate (80 reports/s) auf al kopieren
      82     call kb.write.mouse ;und auch dies per vordefinierter Prozedur an die Maus senden
      83     cli                 ;alle Interrupts auschalten, damit nicht unser Keyboard-Int das gesendete Byte erhält xD
      84     mov al,0F2h         ;sende Befehl F2h für GetDeviceID an Maus, sodass wenn die Maus ein Mausrad besitzt mit 04h antwortet,
      85     call kb.write.mouse ;ansonsten erwidert sie 00h -> Dies wird durch die Sequenz SetSampleRate 200,100,80 aktiviert.
      86     call kb.read        ;die ID der Maus auslesen. kb.write.mouse liest nur die Bestätigung FAh aus
      87     sti                 ;nun da wir das Byte entgegengenommen haben, können wir die IRQs wieder aktivieren
      88     mov [mouseid],al    ;speichere die erhaltene MausID in einer Variable, damit der IRQ12-Handler weiß, ob die Maus ein Rad hat

\</asm\>

\<asm\>

     304 .write.mouse:
     305     push ax             ;al sichern, da dort der zu sendende Befehl gesichert ist
     306     mov al,0d4h         ;auf al d4h kopieren -> sagt dem KC, dass das nächste Byte an die Maus anstatt der Tastatur gesendet wird
     307     out 64h,al          ;... werden soll -> dann schicke das Byte an den KC
     308     call kb.checkcmd    ;und warte, bis es angenommen und verarbeitet wurde
     309     pop ax              ;hole den eig. zu sendenden Befehl nach al
     310     cli                 ;Interrupts deaktivieren, damit Byte nicht von einem falsch geproggten IRQ1-Int-Handler abgefangen wird
     311     out 60h,al          ;und sende ihn nun, da D4h gesendet wurde an den Maus-Controller
     312     call kb.checkcmd    ;und warte, bis auch dieser Befehl vollständig angenommen unf abgearbeitet wurde
     313     call kb.read        ;hole die response. die ist bei succes FAh. bei manch anderen gibt es special-codes, wie 00h bei GetID
     314     sti                 ;Interrupts wieder aktivieren, sonst bleibt sicher der PC hängen xD
     315     ret                 ;verlasse Prozedur und springe zumi Aufruf zurück
     316 ;******* Prozedur schickt den Befehl per D4h an die Maus und gibt error von kb.read aus (prc succesfull if ah=0 und al=FAh sein) *********

\</asm\>

### Wheel-and-5-Button-Mode-Packet

Nun habt ihr aber sicher auch schon gemerkt, dass in dem 4. Byte noch 4 Bits frei sind und wir noch nicht die Stati der 4.+5. Taste bekommen, falls diese vorhanden wären. Damit diese Stati auch mit dem 4.Byte mitgesendet werden, gibt es dafür auch wieder eine Sequenz um dies zu aktivieren, die wie folgt aussieht:

Setze Sample-Rate auf 200 reports/s

Setze Sample-Rate auf 200 reports/s

Setze Sample-Rate auf 80 reports/s

Der Code zum Aktivieren des Rades und der 5 Button sollte ganz einfach aus einer modifizierten Version des Sources zum Aktivieren des Wheel-Modus möglich sein. Wenn die Maus Taste 4+5 unterstützt, dann sendet sie nach dem GetDeviceID(F2h) 04h, statt 00h und sendet ab sofort folgendes Maus-Daten-Paket:

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
<td colspan="2">reserved (0)</td>
<td>5th Maustaste</td>
<td>4th Maustaste</td>
<td colspan="4">Z Movement seit dem letztem Daten-Paket
</td></tr></tbody></table>

Hierbei enthalten die 4 Bits für die Mausradbewegung (Z) sowohl die Bewegung in horizontale, als auch vertikale Richtung (Es werden also zwei Mausräder unterstützt):

| Wert | Bedeutung |
| ------ | ------------------------ |
| +-1 | vertikales Scrollrad |
| +-2 | horizontales Scrollrad |

## Anwendung

### IRQ12-Handler installieren

So, um dieses ganze Wissen alles in ein Programm zu packen habe ich für ein einen kleinen Maustreiber erstellt, was aber eher nur als Programm arbeitet. Das Programm ist für den RealMode geschrieben und sollte deswegen, so denke ich zum testen im ProtectedMode einfach ALLE Rechte wie Selbstmodifizierung und Co eingeräumt bekommen. Unter DOS/Windows funktioniert der Code nicht, er kann zwar die Maus ansprechen und Co, aber die Daten gehen alle an den Windowseigenen Treiber.

Das Programm hakt sich in den IRQ12 ein, der auf den INT74h sein sollte, ansonsten muss diese Zeile geändert werden:

\<asm\>

      13     mov [es:74h*4+2],cs         ;und dann an den Eintrag für den Int74h/IRQ12 das Segment
      14     mov [es:74h*4],word irq12   ;und den Offset des Int-Handlers speichern

\</asm\>

### Maus im Stream-Modus aktivieren

Nun da der Handler installiert ist, müssen wir die Maus immernoch dazu bringen ihre Daten an diesen zu senden, dies geschieht mit folgenden Befehlszeilen, in denen in dieser Reihenfolge erst dem KBC gesagt wird, dass er die Maus aktivieren soll, danach der Maus selber gesagt, dass sie sich aktivieren soll und zuletzt im CommanByte des KBC das ansprignen des IRQ12 bei Daten aktiviert wird.

\<asm\>

      18     mov al,0a8h         ;schiebe auf al den Befehl zur Aktivierung der Maus
      19     out 64h,al          ;schicke den Befehl an den Keyboard-Controller
      20     call kb.checkcmd    ;und warte bis der Befehl angenommen und verarbeitet wurde
      21     
      22     mov al,0f4h         ;danach an die Maus den Befehl zum Eintritt in den Streaming-Mode auf al kopieren
      23     call kb.write.mouse ;um diesen an die Maus über den Input-Buffer-Port zu senden
      24     
      25     cli                 ;alle Interrupts auschalten, damit nicht unser Keyboard-Int das gesendete Byte erhält xD
      26     mov al,20h          ;Befehl zum auslesen des Kommando-Bytes auf al schieben
      27     out 64h,al          ;um es an den Keyboard-Controller zu senden
      28     call kb.checkcmd    ;nun noch warten, bis dieser angenommen wurde
      29     call kb.read        ;und wir können das command-Byte abholen
      30     sti                 ;nun da wir das Byte entgegengenommen haben, können wir die IRQs wieder aktivieren
      31         push ax         ;speichere al, da dies für out gebraucht wird
      32             lea si,[got_command_byte_str]   ;zum debuggen->gibt erhaltenes commandbyte aus
      33             call write                      ;   ~
      34             xchg ah,al                      ;   ~
      35             mov ebx,16                      ;   ~
      36             call zahlausgabe                ;   ~
      37     mov al,60h          ;und kopiere auf al den Befehl zum einlesen eines neuen Command-Bytes
      38     out 64h,al          ;und schicke diesen nun an den Keyboard-Controller
      39     call kb.checkcmd    ;warte auf Annahme dessen -> nun wartet der KC auf das Command-Byte am Port 60h(Datenport des 64h)
      40         pop ax          ;stelle nun das mit 20h erhaltene Byte wieder her um es zu modifizieren und neu zu setzen
      41     or al,00000011b     ;setze Bit1, bei dessem Setzen der IRQ12 immer angesprungen wird, sobald Bit5 im 64h-Status-Byte =1 ist
      42     and al,11101111b    ;lösche das Bit, das wenn es gesetzt ist die Tastatur deaktiviert.
      43     out 60h,al          ;und schicke das Command-Byte an den Daten-Port 60h, durch den Befehl 60h wird dieses neu eingelesen
      44     call kb.checkcmd    ;und warte, bis das Byte vollständig angenommen wurde

\</asm\>

### Rad und/oder 5 Tasten-Modus aktivieren

Nachdem der Handler installiert ist und die Maus eingeschalten ist, prüft es, ob die Maus ein Rad und/oder 5 Tasten hat, dies geshieht mit folgenden Zeilen, in dem es die gerade eben besprochenen Sample-Rate-Sequenzen durchführt und dann die ID in eine Variable speichert, die der Int-Handler ausliest um zu wissen, ob er nun 3 oder 4 Bytes holen soll:

\<asm\>

      46             lea si,[three_button_mode]      ;zum debuggen, gibt nachricht aus, dass maus sich
      47             call write                      ;im 3-tasten-modus befindet
      48     mov al,0F3h         ;Befehl zum senden und neu setzen der SampleRate auf al schieben
      49     call kb.write.mouse ;und per vordefinierter Prozedur an die Maus senden
      50     mov al,0C8h         ;dann das zweite Byte des Befehls, die Sample-Rate (200 reports/s) auf al kopieren
      51     call kb.write.mouse ;und auch dies per vordefinierter Prozedur an die Maus senden
      52     mov al,0F3h         ;Befehl zum senden und neu setzen der SampleRate auf al schieben
      53     call kb.write.mouse ;und per vordefinierter Prozedur an die Maus senden
      54     mov al,64h          ;dann das zweite Byte des Befehls, die Sample-Rate (100 reports/s) auf al kopieren
      55     call kb.write.mouse ;und auch dies per vordefinierter Prozedur an die Maus senden
      56     mov al,0F3h         ;Befehl zum senden und neu setzen der SampleRate auf al schieben
      57     call kb.write.mouse ;und per vordefinierter Prozedur an die Maus senden
      58     mov al,50h          ;dann das zweite Byte des Befehls, die Sample-Rate (80 reports/s) auf al kopieren
      59     call kb.write.mouse ;und auch dies per vordefinierter Prozedur an die Maus senden
      60     cli                 ;alle Interrupts auschalten, damit nicht unser Keyboard-Int das gesendete Byte erhält xD
      61     mov al,0F2h         ;sende Befehl F2h für GetDeviceID an Maus, sodass wenn die Maus ein Mausrad besitzt mit 03h antwortet,
      62     call kb.write.mouse ;ansonsten erwidert sie 00h -> Dies wird durch die Sequenz SetSampleRate 200,100,80 aktiviert.
      63     call kb.read        ;die ID der Maus auslesen. (kb.write.mouse liest nur die Bestätigung FAh aus)
      64     sti                 ;nun da wir das Byte entgegengenommen haben, können wir die IRQs wieder aktivieren
      65             cmp al,03h                      ;testen ob id 3h gesendet hat
      66             jne .no_wheel_mode              ;wenn nicht, wurde nicht in den wheelmode geswitched
      67                 lea si,[wheel_mode]         ;zum debuggen->gibt aus, ob Maus-mode geändert wurde
      68                 call write                  ;   ~
      69             .no_wheel_mode
      70 
      71     mov al,0F3h         ;Befehl zum senden und neu setzen der SampleRate auf al schieben
      72     call kb.write.mouse ;und per vordefinierter Prozedur an die Maus senden
      73     mov al,0C8h         ;dann das zweite Byte des Befehls, die Sample-Rate (200 reports/s) auf al kopieren
      74     call kb.write.mouse ;und auch dies per vordefinierter Prozedur an die Maus senden
      75     mov al,0F3h         ;Befehl zum senden und neu setzen der SampleRate auf al schieben
      76     call kb.write.mouse ;und per vordefinierter Prozedur an die Maus senden
      77     mov al,0C8h         ;dann das zweite Byte des Befehls, die Sample-Rate (200 reports/s) auf al kopieren
      78     call kb.write.mouse ;und auch dies per vordefinierter Prozedur an die Maus senden
      79     mov al,0F3h         ;Befehl zum senden und neu setzen der SampleRate auf al schieben
      80     call kb.write.mouse ;und per vordefinierter Prozedur an die Maus senden
      81     mov al,50h          ;dann das zweite Byte des Befehls, die Sample-Rate (80 reports/s) auf al kopieren
      82     call kb.write.mouse ;und auch dies per vordefinierter Prozedur an die Maus senden
      83     cli                 ;alle Interrupts auschalten, damit nicht unser Keyboard-Int das gesendete Byte erhält xD
      84     mov al,0F2h         ;sende Befehl F2h für GetDeviceID an Maus, sodass wenn die Maus ein Mausrad besitzt mit 04h antwortet,
      85     call kb.write.mouse ;ansonsten erwidert sie 00h -> Dies wird durch die Sequenz SetSampleRate 200,100,80 aktiviert.
      86     call kb.read        ;die ID der Maus auslesen. kb.write.mouse liest nur die Bestätigung FAh aus
      87     sti                 ;nun da wir das Byte entgegengenommen haben, können wir die IRQs wieder aktivieren
      88     mov [mouseid],al    ;speichere die erhaltene MausID in einer Variable, damit der IRQ12-Handler weiß, ob die Maus ein Rad hat
      89             cmp al,03h                      ;testen ob id 4h gesendet hat
      90             jne .no_5_button_mode           ;wenn nicht, wurde nicht in den wheelmode geswitched
      91                 lea si,[five_button_mode]   ;zum debuggen->gibt aus, ob Maus-mode geändert wurde
      92                 call write                  ;   ~
      93             .no_5_button_mode

\</asm\>

### PIC - IRQ12 aktivieren

Um nun sicher zu gehen, dass der IRQ12 überhaupt angeschalten ist, schalten wir ihn lieber nocheinmal persönlich mit folgenden Zeilen über den PIC ein:

\<asm\>

      95     in al,0A1h          ;hole von dem PIC2 das IMR
      96     and al,11101111b    ;um darin den IRQ12 zu maskieren, damit er aktiviert wird
      97     out 0A1h,al         ;und sende das modifizierte IMR an den Slave

\</asm\>

### Schleife, in der Mauseingaben möglich sind

Nun da die Maus aktiviert und ein funktionierender IRQ12-Handler installiert sein solte, wartet eine Schleife auf ESC. Solange diese Schleife ausgeführt wird, kann der IRQ12 ja trotzdem den Handler anspringen, also kurz gesagt, solange man sich in folgender Schleife befindet werden alle Bewegungen der Maus abgefangen und grafisch dargestellt.

\<asm\>

      99     wait_esc:
     100         mov ah,1        ;Funktion 1 des Int16h wählen, um abzufragen, ob ein Tastendruck vorhanden ist
     101         int 16h         ;diese Funktion ausführen, zeroflag gesetzt, wenn nichts vorhanden ist
     102         or ah,ah        ;teste ob ein Scancode <> 0 erhalten wurde und somit eine Taste gedrückt wurde...
     103             jz wait_esc ;wenn keine Taste gedrückt wurde, führe die Prozedur so lange aus, bis die geschieht
     104         xor ax,ax       ;lösche ax für funktion 00h
     105         int 16h         ;und hole die Taste ab, die bei ah=1 int 16 den Tastendruck ausgelöst hat, da diese ja nicht abgeholt wird
     106         cmp ah,1        ;vergleicht den asciicode mit dem von ESC
     107     jne wait_esc        ;wenn ESC nicht gedrückt wurde, warte auf näcshten Tastendruck

\</asm\>

### Maus deaktivieren, Programm beenden

Wenn die Schleife durch drücken von Esc verlassen wurde, dann lösche als erstes Bit1 im command-Byte des Keyboards, damit das anspringen des IRQ12 bei Daten deaktiviert wird.^

\<asm\>

     109     cli                 ;alle Interrupts auschalten, damit nicht unser Keyboard-Int das gesendete Byte erhält xD
     110     mov al,20h          ;Befehl zum auslesen des Kommando-Bytes auf al schieben
     111     out 64h,al          ;um es an den Keyboard-Controller zu senden
     112     call kb.checkcmd    ;nun noch warten, bis dieser angenommen wurde
     113     call kb.read        ;und wir können das command-Byte abholen
     114     sti                 ;nun da wir das Byte entgegengenommen haben, können wir die IRQs wieder aktivieren
     115         push ax         ;spiechere al, da dies für out gebraucht wird
     116     mov al,60h          ;und kopiere auf al den Befehl zum einlesen eines neuen Command-Bytes
     117     out 64h,al          ;und schicke diesen nun an den Keyboard-Controller
     118     call kb.checkcmd    ;warte auf Annahme dessen -> nun wartet der KC auf das Command-Byte am Port 60h(Datenport des 64h)
     119         pop ax          ;stelle nun das mit 20h erhaltene Byte wieder her um es zu modifizieren und neu zu setzen
     120     and al,11101101b    ;lösche Bit1, bei dessem Setzen der IRQ12 immer angesprungen wird, sobald Bit5 im 64h-Status-Byte =1 ist
     121                         ;lösche auch noch Bit 5, da bei manchen PCs anscheined ein falsches command-byte geliefert wird.. und
     122                         ;wenn bit 5 gesetzt ist, wird der Keyboard-streaming-mode sozusagen beendet.. (hat sich erledigt, lag
     123                         ;daran, dass mein keyboard-treiber das commandbyte abgefangen hatte, kann aber nicht schades das Bit5 
     124                         ;zu löschen, wer will soll und kann es wegmachen)
     125     out 60h,al          ;und schicke das Command-Byte an den Daten-Port 60h, durch den Befehl 60h wird dieses neu eingelesen
     126     call kb.checkcmd    ;und warte, bis das Byte vollständig angenommen wurde

\</asm\>

Danach wird einfach nur noch ein mal die Maus selber deaktiviert, danach wird dem Keyboard-Controller gesagt, dass diese deaktiviert wird und zuletzt wird der IRQ12 im PIC wieder maskiert. Am Ende der Ende-Sequenz wird mit "retf" zu meinem Kernel zurückgesprungen. Retf sollte man je nach seinem eigenen OS anpassen.

\<asm\>

     128     mov al,0F5h         ;auf al den Befehl zum deaktivieren der Maus selbst schieben
     129     call kb.write.mouse ;und an die Maus senden
     130     
     131     mov al,0a7h         ;schiebe auf al den Befehl zur Deaktivierung der Maus und 
     132     out 64h,al          ;schicke dies dem Keyboard-Controller, sodass die Maus auch auf diesem deaktiviert ist
     133     call kb.checkcmd    ;warte bis der Befehl angenommen wurde
     134 
     135     in al,0A1h          ;hole von dem PIC2 das IMR
     136     or al,00010000b     ;um darin den IRQ12 zu maskieren, damit er deaktiviert wird
     137     out 0A1h,al         ;und sende das modifizierte IMR an den Slave
     138 
     139     retf                ;springe zum Kernel zurück

\</asm\>

### Programm Konzept

So, das war nun unser Programm, das im Konzept so aussehen würde:

IRQ12 im PIC deaktivieren

Offset des Handlers in der IVT bei Int 74h eintragen

Maus im KC aktivieren

Maus selbst aktivieren und in StreamMode setzen

Im CommandByte aktivieren, dass IRQ12 bei Mausdaten angepingt wird

WheelModus betreten, falls vorhanden

5-Tasten-Modus betreten, falls vorhanden

IRQ12 im PIC aktivieren

Auf ESC warten, derzeit arbeitet MausHandler und visualisiert MausDaten

Aufrufen des IRQ12 bei Daten im CommandByte deaktivieren

Maus im KC deaktivieren

Maus selbst deaktivieren

IRQ12 im PIC maskieren/deaktivieren

Programm beenden

### IRQ12-Handler

#### Konzept

Doch wie sieht nun unser Herz der IRQ12-Handler aus? Der Handler wird aufgerufen, sobald Daten in der Maus vorhanden sind, wird der IRQ12 angesprungen, an dem unser Handler gehakt ist. Dieser holt zuerst das vorhandene Byte ab und schaut dann nach, welches Byte im Daten-Paket das nun ist (1,2,3 oder 4). Dieses Nachschauen geschieht, indem der Handler bei jedem erhaltenen Byte einen Counter incrementiert, je nachdem, wie hoch der Counter ist, weiß der Handler welches Byte er momentan abgeholt hat. Ist der Handler dann bei dem Bearbeiten und Interpretieren von Byte 3, prüft dieser per der bei der Aktivierungsequenz gespeicherten MausID, ob ein 4.Byte folgen wird, oder nicht, wenn nicht, setzt er den Byte-Counter auf 0, sodass beim nächsten Erhalten von Daten der IRQ12-Handler das Byte als erstes Byte des Maus-Data-Packets interpretiert. Je nachdem, was für Daten gesendet werden, wird auch die momentan virtuelle x-Position, z-Position(Mausrad), sowie die y-Postion ausgerichtet und in jeweiligen Variablen gespeichert. Hierfür würde das Konzept wie folgt aussehen:

Wenn IRQ12 angesprungen wird, hole Byte

Wenn Byte-Counter 0 ist, ist Byte Byte \#1 des Paketes

Speichere dieses Byte als StatusByte

Incrementiere Byte-Counter

Wenn Byte-Counter 1 ist, ist Byte Byte \#2 des Paketes

Speichere dieses Byte

Erhöhe oder dekrementiere die aktuelle x-Position je nach dem x-sign-bit ind Byte \#1

incrementiere Byte-Counter

Wenn Byte-Counter 2 ist, ist Byte Byte \#3 des Paketes

Speichere dieses Byte

Erhöhe oder dekrementiere die aktuelle y-Position je nach dem y-sign-bit ind Byte \#1

Teste ob Maus sich im Wheel-Modus oder höher befindet und demnach 4 Bytes gesendet werden

Wenn nicht, setze Byte-Counter auf 0 und rufe Prozedur auf, die Daten-Paket visualisert

Ansonsten incrementiere Byte-Counter

Wenn Byte-Counter 3 ist, ist Byte Byte \#4 des Paketes

Speichere Byte

Incrementiere Z-Pos je nach Inhalt um 1 oder -1 (eig. sind zahlen von -8 bis 7 möglich, aber bochs lieferte nur 1 und -1... wird noch getestet und ausgebessert, wenn mein alter PC wieder als Testobjekt verfügbar ist)

Setze Byte-Counter auf 0

Rufe Prozedur auf, die Daten-Paket visualisert

Beende Handler mit iret

#### Handler-Code

Joa und in Assembler würde das wie folgt aussehen:

\<asm\>

     141 ;***************************************************************************************************************
     142 ;dies ist der IRQ12, der immer angesprungen wird, wenn sich die Daten der Maus verändert habe (sofern der Stream-Mode benutzt wird)
     143 ;da der IRQ12 immer nur aufgerufen wird, wenn ein Byte im Mouse-Buffer liegt, holen wie auch immer nur ein Byte ab, zählen jedoch mit,
     144 ;welches Byte des Mouse-data-packets das ist. Unter VirtualBox ging es zwar auch, wenn man alle 3 Byte hintereinander beim Aufrufen
     145 ;abgeholt hat, doch bei meinem alten PC kam es dabei zu disinformation, sodass ich das so ändern musste.
     146 ;***************************************************************************************************************
     147 irq12:
     148     pusha       ;Register sichern
     149     push ds     ;Datensegment sichern
     150     push es     ;es-Segment sichern
     151     mov ax,cs   ;dann auf ax das codesegment, also das segment, wo das Programm ist, holen
     152     mov ds,ax   ;um dies auf ds zu kopieren
     153     mov es,ax   ;und um auch es zu updaten
     154 
     155 .start:
     156 call kb.read.mouse      ;Byte #1,#2,#3 oder #4 nach al holen
     157     jnz .end            ;wenn dabei was schief ging, beende den irq
     158 
     159 cmp byte[actualb],0     ;überprüfe, ob der Counter 0 ist (Zähler beginnt mit 0!)
     160 jne .not_first_byte     ;wenn nicht, hole schoneinmal Byte 1 nicht ab und springe somit darüber
     161 
     162     mov [status],al             ;das Byte in Status speichern, damit es die Prozeduren von int33h nutzen können
     163     jmp short .end_part_packet  ;beende den Interrupt, da beim nächsten Byte dieser IRQ sowieso nocheinmal aufgerufen wird
     164 
     165 .not_first_byte:    
     166 cmp byte[actualb],1         ;teste ob der Counter 1 ist (Zähler beginnt mit 0!)
     167 jne .not_second_byte        ;wenn nicht, dann ist es auch nicht das zweite Byte, was wir jetzt holen müssen
     168 
     169     mov [xcoord],al             ;ansonsten zwischenspeichere den x-movement
     170     test byte[status],00010000b ;dann teste ob das SignBit von x gesetzt ist, wenn ja, ist das movement negativ
     171     jnz .sign_bit_x             ;und springe zu dem Teil, der subtrahiert statt addiert
     172         add [x],ax              ;ansonsten addiere zur aktuellen Position die Bewegung -> da ah ja 0 sein muss, wenn der 
     173                                 ;Programmzeiger hierhergekommen ist, ist das möglich
     174         jmp short .sign_x       ;und überspringe das Abziehen
     175     .sign_bit_x:
     176         not al                  ;negiere x-coord, damit der overflow aufgehoben wird, der ensteht, wenn man 0-1 rechnet
     177         inc al                  ;da aber -1 = FFh was genoted 0 wäre, addiere nocheinmal 1
     178         sub [x],ax              ;und ziehe den Betrag des Movements der aktuellen Position ab -> da ah ja 0 sein muss, wenn
     179                                 ;der Programmzeiger hierhergekommen ist, ist das möglich
     180     .sign_x:
     181     jmp short .end_part_packet  ;beende den Interrupt, da beim nächsten Byte dieser IRQ sowieso nocheinmal aufgerufen wird
     182 
     183 .not_second_byte:
     184 cmp byte[actualb],2         ;teste ob der Byte-Counter 2 ist (Zähler beginnt mit 0!)
     185 jne .not_third_byte         ;wenn nicht, dann muss es das 4. Byte sein, was wir abholen müssen also springe dahin
     186 
     187     mov [ycoord],al             ;ansonsten zwischenspeichere den y-movement
     188     test byte[status],00100000b ;dann teste ob das SignBit von y gesetzt ist, wenn ja, ist das movement negativ
     189     jnz .sign_bit_y             ;und springe zu dem Teil, der subtrahiert statt addiert
     190         add [y],ax              ;ansonsten addiere zur aktuellen Position die Bewegung -> da ah ja 0 sein muss, wenn der
     191                                 ;Programmzeiger hierhergekommen ist, ist das möglich
     192         jmp short .sign_y       ;und überspringe das Abziehen
     193     .sign_bit_y:
     194         not al                  ;negiere y-coord, damit der overflow aufgehoben wird, der ensteht, wenn man 0-1 rechnet
     195         inc al                  ;da aber -1 = FFh was genoted 0 wäre, addiere nocheinmal 1
     196         sub [y],ax              ;und ziehe den Betrag des Movements der aktuellen Position ab -> da ah ja 0 sein muss, wenn
     197                                 ;der Programmzeiger hierhergekommen ist, ist das möglich
     198     .sign_y:
     199     
     200     cmp byte[mouseid],0         ;prüfe ob die MouseID 0 ist, falls nicht, werden 4 Bytes gesendet, egal ob mouseid 3 oder 4 ist
     201         jz short .end_packet    ;beende nun den Interrupt, code setzt actualb auf 0 und gibt paket aus
     202     jmp short .end_part_packet  ;beende den Interrupt, da beim nächsten Byte dieser IRQ sowieso nocheinmal aufgerufen wird
     203 
     204 .not_third_byte:
     205 
     206     mov [zbtn45],al         ;sonst speichere es für spätere Benutzung
     207     test al,00000001b       ;teste ob überhaupt ein z-movement vorliegt, da es nur 1111b und 0001b gibt und dabei bit1 immer 1 ist
     208         jz .end_packet      ;falls kein z-movment vorhanden sit, überspringe das berechnen eines diesen
     209     test al,00000010b       ;ansonsten teste, ob es 1111b ist und somit z incrementiert wird, oder es 0001b ist und z dec wird
     210     jnz .z_mov_plus_1       ;wenn 1111b, dann springe zu code, der [z] incrementiert
     211         dec byte[z]             ;ansonsten decrementiere [z]
     212         jmp short .end_packet   ;überspringe den code, der [z] inkrementieren würde
     213     .z_mov_plus_1:
     214         inc byte[z]             ;incrementiere [z]
     215 
     216 .end_packet:
     217     mov byte[actualb],-1;setze Byte-Counter auf -1(da es bei .end_.. um 1 incrementiert wird), da Paketbytes abgeholt worden
     218     call display_mouse  ;dies ist eine sehr umfangreiche Prozedur zur Veranschaulichung der Daten
     219 .end_part_packet:
     220     inc byte[actualb]   ;incrementiere den Byte counter um 1, damit beim der irq12-handler weiß, welches byte er bearbeitet
     221 
     222 .end:
     223     mov al,20h      ;schiebe das OCW1/EOI auf al
     224     out 20h,al      ;und sende den EOI an den Master
     225     out 0A0h,al     ;und den Slave, da beide ihn benötigen, da Slave am IRQ2 hängt
     226     pop es          ;es wiederherstellen
     227     pop ds          ;stelle ds wieder her
     228     popa            ;stelle auch die anderen Register wieder her
     229     iret            ;und verlasse den Interrupt
     230 
     231 ;************************* Variablen des IRQ12 *************************
     232 status  db 0    ;hier wird das Byte1 des Mouse-data-packes gespeichert
     233 xcoord  db 0    ;hier das zweite
     234 ycoord  db 0    ;und hier das 3.
     235 zbtn45  db 0    ;und hier das 4.
     236 x       dw 0    ;hier ist die aktuelle Position des Mauszeigers gespeichert, die entsprechend
     237 y       dw 0    ; ... der Movement-Bytes verändert werden
     238 z       dw 0    ;hier die aktuelle z-position des rades(nicht die bewegung)
     239 mouseid db 0    ;hier wird die MouseID gespeichert 0 für normal, 3 für Rad und 4 für Rad und 5 Buttons
     240 actualb db 0    ;hier wird gespeichert, welche bytes des Maus-Daten-Pakets schon abgeholt wurden (für jedes Byte wird der IRQ12
     241                 ;einzeln angesprungen)

\</asm\>

### Die Ausgabe-Prozedur

Wie schon erwähnt wird evtl. hier noch etwas am Abholen und Interpretieren modifiziert, aber ich wollte euch nicht warten lassen, da ich erst ein externes Disketten-Laufwerk bei Amazon bestellen muss ;). Doch weiter gehts. Zum Schluss möchte ich es wenigstens versuchen euch einen Ansatz zu geben, wie man sich am besten in die Visualisierungs-Prozedur hineinzuversetzen hat, denn auch wenn alles kommentiert ist, ist das ein bisschen schwierig meinen genauen Gedankengang dabei festzuhalten. Das ganze funktioniert, indem das Bild und die Daten und Co alles gleich in den Bildschirmspeicher geschrieben wird. Der Bildschrimspeicher, also die Addressen sind alle darauf eingestellt, dass der momentan VideoModus 03h ist, also 80 Zeichen Zeilenlänge bei 25 Zeilen pro Bildschirm hat. So fängt der Bildschirmspeicher im 03h-Modus am segment 0B800h im Speicher an. Der Speicher selber ist 4000Bytes groß, für jedes Zeichen 2 Bytes, eins für das Attribut des Zeichen wie Hintergrund- und Schriftfarbe und eins, wo das Char gespeichert ist, macht bei 25 Zeilen\*80 Zeichen\*2 Bytes=4000Byte. Das ganze sei an einer Befehlszeile verdeutlicht:

\<asm\>

      01     mov [es:100], word 1234h

\</asm\>

Diese Zeile würde an die Stelle 0;50 auf den Bildschirm eine grüne 4 auf blauem Hintergrund ausgeben. Der Hintergrund ist blau, weil die "1" dies so sagt, bei 2 gilt das für den Vordergrund und 34h ist wie schon gesagt das Zeichen selber. Das wäre es dann auch schon, mehr kann ich dazu einfach nicht sagen, versucht euch einfach in die Prozedur hineinzuversetzen, ein bisschen rumzuspielen und die eigenartige Adressierungen durchzudenken. Und hier ist die langersehnte Prozedur zum veranschaulichen des Pakets xD:

\<asm\>

     369 ;***************************************************************************************
     370 ;Display-Mouse -> eine ganz spezifische Prozedur, die die Daten des Mouse-Packets vernaschaulicht
     371 ;***************************************************************************************
     372 x_pos_mouse_pic db 30   ;obere linke x-position des mausbildes
     373 y_pos_mouse_pic db 7    ;obere linke y-position des mausbildes
     374 picw            equ 17  ;Länge einer Zeile des Bildes
     375 ;                 |-y_pos_mouse_pic
     376 ;<---x_pos_mouse_pic--->|
     377 ;                 <---------pic_width-------->
     378 mouse_pic   db  "   ___________   " ;16 Bytes per line
     379             db  "  /   |   |   \  "
     380             db  " |    |   |    | "
     381             db  " |    |   |    | "
     382             db  " |-------------| "
     383             db  " | xmov=       | "
     384             db  " | ymov=       | "
     385             db  " |  x=         | "
     386             db  " |  y=         | "
     387             db  " |  z=         | "
     388             db  "  \___________/  "
     389 
     390 display_mouse:
     391     pusha           ;Register sichern
      .
      .  aus Gründen der Größe dieses Artikels musste ich leider diesen CodeTeil aus dem Artikel entfernen.
      .  bitte schaut im Sourcecode selber nach, was hier stehen müsste. Die Zeilen-Angaben sind ja gegeben.
      .
     584     popad           ;dann stelle die Register wieder her
     585     ret             ;und kehre zum Aufrufsort zurück

\</asm\>

## Schlusswort

Und das wars auch schon von mir, mehr ist nicht zu sagen, vor allem, da ich den Code extra stark kommentiert habe. Wer sich noch tiefer in das Thema einlesen will, dem empfehle ich folgendes [Dokument](http://maxinator.freehoster.ch/Programming/programming/ps2mouse/tp-intf2-4.PDF) über das Synaptic-Touchpad, in dem auch das PS/2-Protokoll gut beschrieben ist.

--[Maxinator](https://lowlevel-eu.github.io/wiki/pages/1839/index.html "Benutzer:Maxinator") 22:03, 11. Nov 2007 (CET)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/9075/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1559/index.html)

<!-- MediaWiki page 1559; revision 9075; parent 8825; 2010-12-19T19:45:27Z -->
