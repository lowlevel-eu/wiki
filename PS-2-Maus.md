# PS/2-Maus

## Beschreibung

So, wie ich daraus schließe, dass ihr das hier lest, seid ihr sicher schon ganz versessen darauf zu erfahren, wie die PS/2-Maus zu programmieren geht, mir jedenfalls ging es so, als mir vor kurzen ein funktionierendes PS/2-Maus-Assembler-Skript in die Hände gefallen ist :). Die PS/2-Maus teilt sich zusammen mit dem Keyboard eine Schnittstelle, die PS/2-Schnittstelle, wie ihr euch sicher denken könnt xD.

Doch, wenn die beiden sich eine Schnittstelle teilen, wie sollen dann die beiden wissen, welche Commands/Befehle für wen gedacht sind? Eigentlich ist das ja relativ einfach, denn vor jedem Befehl, der an die Maus gehen soll, muss ein Befehl an den Tastatur-Kontroller geschickt werden, dem man damit mitteilt, das der nächste Befehle für die Maus bestimmt ist. Genauso muss auch beim Auslesen der Daten darauf geachtet werden, dass wenn das Bit5 im 54h-Status-Byte gesetzt ist, das nächste auszulesende Byte im Port 60h von der Maus ist.

Das zur kurzen Einführung, jetzt kommen die Spezifikationen des PS/2-Ports, wobei ich hier alle Befehle und Spezifikationen aufgelistet habe, also auch die für die Tastatur. Eigentlich werden trotzdem alle Tabellen außer der, die alle TastaturBefehle aufgelistet hat (60h), für das Arbeiten mit der Maus benötigt und Tabellen nur teils teils aufzuführen, möchte ich auch nicht, da ich ein ordentlicher Mensch bin und es mich stören würde, wenn die Hälfte der Spezifikationen im Maus- und die andere Hälfte im Tastatur-Tutorial liegen würden.

Ich empfehle den meisten erst einmal die Spezifikationen nur zu überfliegen und sie sich dann genauer anzuschauen, wenn diese Anhand des Quelltextes beschrieben werden. Leider konnte ich nicht zu jeden Befehl eine 100%-ige Beschreibung anfertigen, da ich noch nicht das vergnügen hatte, diesen zu testen.

## Spezifikationen

|  |  |  |
| ---------- | ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Port** | **Zugriff** | **Beschreibung** |
| **60h** | *Lesezugriff* | Der Port 60h ist zweiseitig, er kann als Keyboard-Controller(64h)-Daten-Port oder als Keyboard-In-/Output-Buffer dienen. An diesen Port werden die Scancodes der gedrückten Tasten gesendet, die dann der Keyboard-Treiber per "in al,60h" auslesen kann. Deaktiviert man bevor man aus diesem Port etwas ausliest das Keybord per Befehl ADh, so erhält man die Daten aus dem Maus-Output-Buffer! Zum auslesen sei gesagt, dass die nur geschehen sollte, wenn entweder das Bit 1 im Keyboard-Controller-Output-Status-Byte, welches anzeigt, dass das Keyboard am 60h Daten hat, oder das Bit 5 in diesem Status-Byte des 64h gesetzt ist, welches anzeigt, dass im Maus-Output-Buffer Daten liegen! Um das zu realisieren habe ich in meinem Programm ein Schleife genutzt, die eine Zeit lang abfragt, ob Daten da sind.<br> |
|  | *Schreibzugriff* | Wenn an diesen Port geschrieben werden, fungiert dieser entweder als Keyboard-Controller-Daten-Port, oder als Input-Buffer des Keyboards. Zweiteres geschieht, wenn man einfach einen der Befehle, die weiter unten für diesen Port aufgelistet sind, an diesen Port sendet. Dies sind überwiegend Befehle zu adjustierung des Keyboards, wie z.b. das Einstellen der Typematic-Rate. Als Ersteres, also als Daten-Port des KC, wird dieser Port nur genutzt, wenn es Befehle des 64h verlangen. So muss an z.b. den Befehl "60h" für das Senden eines neuen Commado-Bytes zwar an den Port 64h senden, doch das Commando-Byte, was dann nach korrekter Annahme des Befehls gesendet werden muss, muss an den Port 60h gesendet werden!<br>Für die möglichen Befehle, die an das Keyboard gesendet werden können, siehe hier. Für die möglichen Mausbefehle, die an diesen Port geschickt werden können, jedoch den Befehl "D4h" auf Port 64h voraussetzen, siehe hier. Für die KC-Befehle, die ein zweites Daten-Byte an diesen Port geschickt verlangen, sie auch hier.<br> |
| **64h** | *Lesezugriff* | Das Lesen für diesen Port ist sehr wichtig, wenn man den Keyboard-Controller programmieren will, da man beim Lesen das Status-Byte des KC bekommt, welches z.b. anzeigt, ob gerade Daten zum abholen verfügbar sind, oder ob der letzte Befehl SCHON vollständig verarbeitet wurde! Für die Bitfields des Statusbytes siehe hier<br> |
|  | *Schreibzugriff* | Beim Schreibzugriff an diesen Port fungiert dieser als Keyboard-Controller-Input-Buffe, sodass eine Reihe von Byte-großen Befehlen gesendet werden können, die zumeist das System des Keyboards beeinflussen, so muss man auch an diese Port den Befehl "D4h" senden, um den nächsten Befehl, der zum Keyboard-Port(60h) geht, an die Maus senden zu lassen. Eine Reihe von Befehlen sind hier aufgelistet.<br> |

Werden 2 Bytes verlangt, wird das zweite auch an den Port 60h gesendet.

|  |  |  |
| ------------ | ----------- | ------------------ |
| **Befehl** | **Größe** | **Beschreibung** |

die Tabelle ist noch unvllständig und 5-6 andere Tabellen fehlen auch noch... muss noch gem,acht werden.. son schrott..

## Das Maus-Daten-Packet

Die Sache mit dem Daten-Paket ist eigentlich recht einfach, immer wenn der IRQ12 angepingt wird, liegt ein Datenpaket im Maus-Output-Buffer, was Byteweise abgeholt werden sollte, wenn Bit5 im 64h-Status-Byte gesetzt ist. Das Daten-Paket ist dabei wie folgt aufgebaut:

<table>
<tbody><tr>
<td></td>
<td><b>7</b></td>
<td><b>6</b></td>
<td><b>5</b></td>
<td><b>4</b></td>
<td><b>3</b></td>
<td><b>2</b></td>
<td><b>1</b></td>
<td><b>0</b>
</td></tr>
<tr>
<td><i>Byte 1</i></td>
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
<td><i>Byte 2</i></td>
<td colspan="8">X Movement seit dem letztem Daten-Paket
</td></tr>
<tr>
<td><i>Byte 3</i></td>
<td colspan="8">Y Movement seit dem letztem Daten-Paket
</td></tr></tbody></table>

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
     156 cmp byte[actualb],0     ;überprüfe, ob der Counter 0 ist (Zähler beginnt mit 0!)
     157 jne .not_first_byte     ;wenn nicht, hole schoneinmal Byte 1 nicht ab und springe somit darüber
     158 
     159     call kb.read.mouse          ;Byte #1 nach al holen 
     160         jnz .end                ;wenn dabei was schief ging, beende den irq
     161     mov [status],al             ;das Byte in Status speichern, damit es die Prozeduren von int33h nutzen können
     162     jmp short .end_part_packet  ;beende den Interrupt, da beim nächsten Byte dieser IRQ sowieso nocheinmal aufgerufen wird
     163 
     164 .not_first_byte:    
     165 cmp byte[actualb],1         ;teste ob der Counter 1 ist (Zähler beginnt mit 0!)
     166 jne .not_second_byte        ;wenn nicht, dann ist es auch nicht das zweite Byte, was wir jetzt holen müssen
     167 
     168     call kb.read.mouse          ;Byte #2 aus dem Output-Buffer der Maus holen
     169         jnz .end                ;wenn dabei was schief ging, beende den irq
     170     mov [xcoord],al             ;ansonsten zwischenspeichere den x-movement
     171     test byte[status],00010000b ;dann teste ob das SignBit von x gesetzt ist, wenn ja, ist das movement negativ
     172     jnz .sign_bit_x             ;und springe zu dem Teil, der subtrahiert statt addiert
     173         add [x],ax              ;ansonsten addiere zur aktuellen Position die Bewegung -> da ah ja 0 sein muss, wenn der 
     174                                 ;Programmzeiger hierhergekommen ist, ist das möglich
     175         jmp short .sign_x       ;und überspringe das Abziehen
     176     .sign_bit_x:
     177         not al                  ;negiere x-coord, damit der overflow aufgehoben wird, der ensteht, wenn man 0-1 rechnet
     178         inc al                  ;da aber -1 = FFh was genoted 0 wäre, addiere nocheinmal 1
     179         sub [x],ax              ;und ziehe den Betrag des Movements der aktuellen Position ab -> da ah ja 0 sein muss, wenn
     180                                 ;der Programmzeiger hierhergekommen ist, ist das möglich
     181     .sign_x:
     182     jmp short .end_part_packet  ;beende den Interrupt, da beim nächsten Byte dieser IRQ sowieso nocheinmal aufgerufen wird
     183 
     184 .not_second_byte:
     185 cmp byte[actualb],2         ;teste ob der Byte-Counter 2 ist (Zähler beginnt mit 0!)
     186 jne .not_third_byte         ;wenn nicht, dann muss es das 4. Byte sein, was wir abholen müssen also springe dahin
     187 
     188     call kb.read.mouse          ;Byte #3 aus dem Output-Buffer der Maus holen
     189         jnz .end                ;wenn dabei was schief ging, beende den irq
     190     mov [ycoord],al             ;ansonsten zwischenspeichere den y-movement
     191     test byte[status],00100000b ;dann teste ob das SignBit von y gesetzt ist, wenn ja, ist das movement negativ
     192     jnz .sign_bit_y             ;und springe zu dem Teil, der subtrahiert statt addiert
     193         add [y],ax              ;ansonsten addiere zur aktuellen Position die Bewegung -> da ah ja 0 sein muss, wenn der
     194                                 ;Programmzeiger hierhergekommen ist, ist das möglich
     195         jmp short .sign_y       ;und überspringe das Abziehen
     196     .sign_bit_y:
     197         not al                  ;negiere y-coord, damit der overflow aufgehoben wird, der ensteht, wenn man 0-1 rechnet
     198         inc al                  ;da aber -1 = FFh was genoted 0 wäre, addiere nocheinmal 1
     199         sub [y],ax              ;und ziehe den Betrag des Movements der aktuellen Position ab -> da ah ja 0 sein muss, wenn
     200                                 ;der Programmzeiger hierhergekommen ist, ist das möglich
     201     .sign_y:
     202     
     203     cmp byte[mouseid],0         ;prüfe ob die MouseID 0 ist, falls nicht, werden 4 Bytes gesendet, egal ob mouseid 3 oder 4 ist
     204         jz short .end_packet    ;beende nun den Interrupt, code setzt actualb auf 0 und gibt paket aus
     205     jmp short .end_part_packet  ;beende den Interrupt, da beim nächsten Byte dieser IRQ sowieso nocheinmal aufgerufen wird
     206 
     207 .not_third_byte:
     208 
     209     call kb.read.mouse      ;hole Byte #4 aus dem Output-Buffer der Maus
     210         jnz .end            ;wenn dabei was schief ging, beende den irq
     211     mov [zbtn45],al         ;sonst speichere es für spätere Benutzung
     212     test al,00000001b       ;teste ob überhaupt ein z-movement vorliegt, da es nur 1111b und 0001b gibt und dabei bit1 immer 1 ist
     213         jz .end_packet      ;falls kein z-movment vorhanden sit, überspringe das berechnen eines diesen
     214     test al,00000010b       ;ansonsten teste, ob es 1111b ist und somit z incrementiert wird, oder es 0001b ist und z dec wird
     215     jnz .z_mov_plus_1       ;wenn 1111b, dann springe zu code, der [z] incrementiert
     216         dec byte[z]             ;ansonsten decrementiere [z]
     217         jmp short .end_packet   ;überspringe den code, der [z] inkrementieren würde
     218     .z_mov_plus_1:
     219         inc byte[z]             ;incrementiere [z]
     220 
     221 .end_packet:
     222     mov byte[actualb],-1;setze Byte-Counter auf -1(da es bei .end_.. um 1 incrementiert wird), da Paketbytes abgeholt worden
     223     call display_mouse  ;dies ist eine sehr umfangreiche Prozedur zur Veranschaulichung der Daten
     224 .end_part_packet:
     225     inc byte[actualb]   ;incrementiere den Byte counter um 1, damit beim der irq12-handler weiß, welches byte er bearbeitet
     226 
     227 .end:
     228     mov al,20h      ;schiebe das OCW1/EOI auf al
     229     out 20h,al      ;und sende den EOI an den Master
     230     out 0A0h,al     ;und den Slave, da beide ihn benötigen, da Slave am IRQ2 hängt
     231     pop es          ;es wiederherstellen
     232     pop ds          ;stelle ds wieder her
     233     popa            ;stelle auch die anderen Register wieder her

234 iret  ;und verlasse den Interrupt

\</asm\>

\<asm\>

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

Wie manch einer vlt. bemerkt hat, fehlt bei dem Daten-Paket noch was... nämlich das Rad und evtl. die Tasten 4+5. Das Problem ist, dass auch Mäuse, die ein Rad besitze zuerst nur diese Daten an die Maus senden, da dies aus Kompatibilätsgründen notwendig ist, sonst könnte man ja keine alte Maus an einem neuen PC anschließen und anderes. Um nun den Wheel-Modus der Maus zu betreten reagieren neuere Mäuse auf eine bestimmte Befehlsequenz, die wie folgt aussieht:

Setze Sample-Rate auf 200 reports/s

Setze Sample-Rate auf 100 reports/s

Setze Sample-Rate auf 80 reports/s

Wenn dies erfolgreich gesendet wurde und gleich danach mit F2h die MausID abgefragt wird, senden normale/alte PS2-Mäuse 00h, wie in den Tabellen oben beschrieben. Neuere Mäuse jedoch, die ein Mausrad besitzen, senden als ID 03h. Diese ID sagt dann dem Maustreiber auch, dass ab jetzt die Daten-Pakete 4 Byte groß sind und wie folgt aussehen:

<table>
<tbody><tr>
<td></td>
<td><b>7</b></td>
<td><b>6</b></td>
<td><b>5</b></td>
<td><b>4</b></td>
<td><b>3</b></td>
<td><b>2</b></td>
<td><b>1</b></td>
<td><b>0</b>
</td></tr>
<tr>
<td><i>Byte 1</i></td>
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
<td><i>Byte 2</i></td>
<td colspan="8">X Movement seit dem letztem Daten-Paket
</td></tr>
<tr>
<td><i>Byte 3</i></td>
<td colspan="8">Y Movement seit dem letztem Daten-Paket
</td></tr>
<tr>
<td><i>Byte 4</i></td>
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

Nun habt ihr aber sicher auch schon gemerkt, dass in dem 3 Byte noch 4 Bits frei sind und wir noch nicht die Stati der 3.+4. Taste bekommen, falls diese vorhanden wären. Damit diese Stati auch mit dem 4.Byte mitgesendet werden, gibt es dafür auch wieder eine Sequenz um dies zu aktivieren, die wie folgt aussieht:

Setze Sample-Rate auf 200 reports/s

Setze Sample-Rate auf 200 reports/s

Setze Sample-Rate auf 80 reports/s

Der Code zum Aktivieren des Rades und der 5 Button sollte ganz einfach aus einer modifizierten Version des Sources zum Aktivieren des Wheel-Modus möglich sein. Wenn die Maus Taste 4+5 unterstützt, dann sendet sie nach dem GetDeviceID(F2h) 04h, statt 00h und sendet ab sofort folgendes Maus-Daten-Paket:

<table>
<tbody><tr>
<td></td>
<td><b>7</b></td>
<td><b>6</b></td>
<td><b>5</b></td>
<td><b>4</b></td>
<td><b>3</b></td>
<td><b>2</b></td>
<td><b>1</b></td>
<td><b>0</b>
</td></tr>
<tr>
<td><i>Byte 1</i></td>
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
<td><i>Byte 2</i></td>
<td colspan="8">X Movement seit dem letztem Daten-Paket
</td></tr>
<tr>
<td><i>Byte 3</i></td>
<td colspan="8">Y Movement seit dem letztem Daten-Paket
</td></tr>
<tr>
<td><i>Byte 4</i></td>
<td>reserved (0)</td>
<td>reserved (0)</td>
<td>5th Maustaste</td>
<td>4th Maustaste</td>
<td colspan="4">Z Movement seit dem letztem Daten-Paket
</td></tr></tbody></table>

## Anwendung

So, um dieses ganze Wissen alles in ein Programm zu packen habe ich für ein einen kleinen Maustreiber erstellt, was aber eher nur als Programm arbeitet. Das Programm ist für den RealMode geschrieben und sollte deswegen, so denke ich zum testen im ProtectedMode einfach ALLE Rechte wie Selbstmodifizierung und Co eingeräumt bekommen. Unter DOS/Windows funktioniert der Code nicht, er kann zwar die Maus ansprechen und Co, aber die Daten gehen alle an den Windowseigenen Treiber. Das Programm hakt sich in den IRQ12 ein, der auf den INT74h sein sollte, ansonsten muss diese Zeile geändert werden:

\<asm\>

      13     mov [es:74h*4+2],cs         ;und dann an den Eintrag für den Int74h/IRQ12 das Segment
      14     mov [es:74h*4],word irq12   ;und den Offset des Int-Handlers speichern

\</asm\>

Nachdem es sich in den IRQ gehakt hat, prüft es, ob die Maus ein Rad und/oder 5 Tasten hat, dies geshieht mit folgenden Zeilen, in dem es die gerade eben besprochenen Sample-Rate-Sequenzen durchführt und dann die ID in eine Variable speichert, die der Int-Handler ausliest um zu wissen, ob er nun 3 oder 4 Bytes holen soll:

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

Um nun sicher zu gehen, dass der IRQ12 überhaupt angeschalten ist, schalten wir ihn lieber nocheinmal persönlich mit folgenden Zeilen über den PIC ein:

\<asm\>

      95     in al,0A1h          ;hole von dem PIC2 das IMR
      96     and al,11101111b    ;um darin den IRQ12 zu maskieren, damit er aktiviert wird
      97     out 0A1h,al         ;und sende das modifizierte IMR an den Slave

\</asm\>

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

Danach wird einfaxch nur noch ein mal die Maus selber deaktiviert, danach wird dem Keyboard-Controller gesagt, dass diese deaktiviert wird und zuletzt wird der IRQ12 im PIC wieder maskiert. Am Ende der Ende-Sequenz wird mit "retf" zu meinem Kernel zurückgesprungen. Retf sollte man je nach seinem eigenen OS anpassen.

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

Joa und in Assembler würde das wie folgt aussehen (selbe Code wie weiter oben, wo per Beispiel gezeigt wird, wie man das Maus-Daten-Paket abholt):

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
     392     mov ax,0B800h   ;auf ax das Anfangsegment des Grafikspeichers von Modus 3h schieben
     393     mov es,ax       ;um es auf es zu storen
     394     
     395     movzx edi,byte[x_pos_mouse_pic] ;auf al die x-position der oberen linken Ecke holen
     396     shl edi,1                       ;und mit 2 multiplizieren, da ein zeichen im vid-speicher 2bytes einnimmt
     397     movzx ax,byte[y_pos_mouse_pic]  ;auf al die y-position der oberen linken Ecke holen
     398     mov bx,160                      ;auf bx 160 schieben
     399     mul bx                          ;um ax mit 160 zu multiplizieren, y_pos-zeilen im bildschirmspeicher verschieben
     400     add edi,eax                     ;das ergebnis in eax zu edi addieren... edi zeigt nun auf die obere linke ecke des bildes
     401     cmp byte[es:edi+4*2],'_'        ;vergleicht das das erste sichtbare Zeichen des Maus-Bildes mit "_"
     402     je mouse_pic_installed      ;wenn das wirklich dort ist, dann ist unser Mausskellet schon im Grafikspeicher und wir müssen
     403         push edi                ;nur noch z.b. x und y ändern       ....ansonsten sichere edi, da das mit stosb eingesetzt wird
     404         lea si,[mouse_pic]      ;auf si zum laden den Offset unsere Bildes schieben
     405         mov cx,11               ;auf cx 11 schieben, da es 11 zeilen sind und diese schliefe für jede ausgeführt werden muss
     406         mov ah,0Fh              ;auf ah die Attriubte schieben, sodass die schrift weiß ist
     407         copy_pic:
     408             push cx             ;cx speichern, damit sozusagen loop zweimal gleichzeitig laufen kann
     409             mov cx,picw         ;auf cx,pic_width schieben, damit nur eine Zeile kopiert wird, schieben
     410             copy_row:
     411                 lodsb           ;das erste Char laden
     412                 stosw           ;und zusammen mit dem Attribut in den Grafikspeicher schieben
     413                 loop copy_row   ;das ganze für jedes Char in der Zeile wiederholen(15x)
     414             pop cx              ;cx wiederherstellen
     415             add di,(80-picw)*2  ;di solange weiterverschieben, bis er an der nächsten zeile an der selben pos angekommen ist
     416         loop copy_pic           ;und diese Schleife wiederholen wir für die Zeile in unserem AsciiArt-Bild
     417         pop edi                 ;stelle edi wieder her, sodass dies nun auf die postion der oberen linke ecke des bildes zeigt
     418     mouse_pic_installed:
     419     
     420     xor al,al                       ;lösche al, damit man sieht, ob es gesetzt wurde oder nicht
     421     mov bl,[status]                 ;nach bl das Status-Byte des Pakets holen
     422     test bl,00000001b               ;prüfen ob in StatusByte Bit2 für linke-Taste gesetzt ist, oder nicht,
     423     setnz al                        ;sodass al bei gesetztem Byte 1 und bei gelöschten Byte 0 ist
     424     mov cl,4Fh                      ;4Fh mit dem Bit multiplizieren, sodass bei gesetztem Bit die Hintergrundfarbe rot und
     425                                     ;die schriftfarbe weiß ist
     426     mul cl                          ;und ansonsten alles schwar ist, da 1*Zeichen = Zeichen und 0*Zeichen=kein Zeichen ist
     427     mov [es:edi+1*160+2*3+1],al     ;setzt die Attribute der Zeichen in der linken Taste im Bild so, dass diese rot wird. Ich 
     428     mov [es:edi+1*160+2*4+1],al     ;habe sogar die Speicheraddressierung als Rechnung stehen lassen, damit diese besser 
     429     mov [es:edi+1*160+2*5+1],al     ;nachvollziehbar ist, siehe auch nochmal den Befehl: "mov [es:100h],word 1234h"
     430     mov [es:edi+2*160+2*2+1],al     ;   ~
     431     mov [es:edi+2*160+2*3+1],al     ;   ~
     432     mov [es:edi+2*160+2*4+1],al     ;   ~
     433     mov [es:edi+2*160+2*5+1],al     ;   ~
     434     mov [es:edi+3*160+2*2+1],al     ;   ~
     435     mov [es:edi+3*160+2*3+1],al     ;   ~
     436     mov [es:edi+3*160+2*4+1],al     ;   ~
     437     mov [es:edi+3*160+2*5+1],al     ;   ~
     438     xor al,al                       ;lösche al, damit man sieht, ob es gesetzt wurde oder nicht
     439     test bl,00000010b               ;prüfen ob in StatusByte Bit2 für rechte-Taste gesetzt ist, oder nicht,
     440     setnz al                        ;sodass al bei gesetztem Byte 1 und bei gelöschten Byte 0 ist
     441     mov cl,4Fh                      ;4Fh mit dem Bit multiplizieren, sodass bei gesetztem Bit die Hintergrundfarbe rot und 
     442                                     ;die schriftfarbe weiß ist
     443     mul cl                          ;und ansonsten alles schwar ist, da 1*Zeichen = Zeichen und 0*Zeichen=kein Zeichen ist
     444     mov [es:edi+1*160+2*11+1],al    ;setzt die Attribute der  Zeichen in der rechten Taste im Bild so, dass diese rot wird.
     445     mov [es:edi+1*160+2*12+1],al    ;Ich habe sogar die Speicheraddressierung als Rechnung stehen lassen, damit diese
     446     mov [es:edi+1*160+2*13+1],al    ;besser nachvollziehbar ist, siehe auch nochmal den Befehl: mov [es:100h],word 1234h
     447     mov [es:edi+2*160+2*11+1],al    ;   ~
     448     mov [es:edi+2*160+2*12+1],al    ;   ~
     449     mov [es:edi+2*160+2*13+1],al    ;   ~
     450     mov [es:edi+2*160+2*14+1],al    ;   ~
     451     mov [es:edi+3*160+2*11+1],al    ;   ~
     452     mov [es:edi+3*160+2*12+1],al    ;   ~
     453     mov [es:edi+3*160+2*13+1],al    ;   ~
     454     mov [es:edi+3*160+2*14+1],al    ;   ~
     455     xor al,al                       ;lösche al, damit man sieht, ob es gesetzt wurde oder nicht
     456     test bl,00000100b               ;prüfen ob in StatusByte Bit2 für mittlere-Taste gesetzt ist, oder nicht,
     457     setnz al                        ;sodass al bei gesetztem Byte 1 und bei gelöschten Byte 0 ist
     458     mov cl,4Fh                      ;4Fh mit dem Bit multiplizieren, sodass bei gesetztem Bit die Hintergrundfarbe rot und
     459                                     ;die schriftfarbe weiß ist
     460     mul cl                          ;und ansonsten alles schwar ist, da 1*Zeichen = Zeichen und 0*Zeichen=kein Zeichen ist
     461     mov [es:edi+1*160+2*7+1],al     ;setzt die Attribute der  Zeichen in der mittleren Taste im Bild so, dass diese rot wird.
     462     mov [es:edi+1*160+2*8+1],al     ;Ich habe sogar die Speicheraddressierung als Rechnung stehen lassen, damit diese
     463     mov [es:edi+1*160+2*9+1],al     ;besser nachvollziehbar ist, siehe auch nochmal den Befehl: mov [es:100h],word 1234h
     464     mov [es:edi+2*160+2*7+1],al     ;   ~
     465     mov [es:edi+2*160+2*8+1],al     ;   ~
     466     mov [es:edi+2*160+2*9+1],al     ;   ~
     467     mov [es:edi+3*160+2*7+1],al     ;   ~
     468     mov [es:edi+3*160+2*8+1],al     ;   ~
     469     mov [es:edi+3*160+2*9+1],al     ;   ~
     470 
     471     xor al,al                   ;lösche al, damit man sieht, ob es gesetzt wurde oder nicht
     472     test bl,00010000b           ;testen ob Bit4 für negatives Movement gesetzt ist
     473     setnz al                    ;wenn ja, setze al auf 1
     474     mov cl,'-'-' '              ;schiebe auf al das Monuszeichen-Space, damit es bei mul mit 0 und addition von space nur space
     475     mul cl                      ;und bei mul mit 1 und addition mit space nur minus wird -> multipliziere al(0 oder 1) mit dem 
     476                                 ;"pre"-zeichen
     477     add al,' '                  ;und addiere zu al space, damit aus dem pre- ein vollständiges zeichen wird
     478     mov [es:edi+5*160+2*8],al   ;das Vorzeichen an der Stelle vor dem Movement platzieren
     479     movzx eax,byte[xcoord]      ;nach eax die Anzahl der x-Bewegungen seit dem letzten Ping holen
     480     test bl,00010000b           ;testen ob das SignBit von x-movment gesetzt ist, wenn nicht, ist das movement positiv
     481     jz .sign_x                  ;und überspringe den Teil, der aus dem Overflowten, negativen Wert den Betrag erstellt
     482         not al                  ;negiere x-coord, damit der overflow aufgehoben wird, der ensteht, wenn man 0-1 rechnet
     483         inc al                  ;da aber -1 = FFh was genoted 0 wäre, addiere nocheinmal 1
     484     .sign_x:
     485     mov edx,10                  ;nun kann für die Spezial-Zahlausgabe als Basis 10 für das Dezimale System festgelegt werden
     486     push edi                    ;edi speicher, da das noch zum berechnen der anderen Positionen benötigt wird
     487     lea di,[edi+5*160+2*12]     ;auf di die Adresse im Speicher, die am Ende der Zahl liegt geschoben werden
     488     mov cx,3                    ;und auf cx 3 geschoben werden
     489     call ddispdec               ;und prozedur aufrufen, die die Zahl gleich in den Video-Speicher bei es:di speichert
     490     pop edi                     ;nun da edi von ddispdec benutzt wurde, stelle den ursprung wieder her
     491     
     492     xor al,al                   ;lösche al, damit man sieht, ob es gesetzt wurde oder nicht
     493     test bl,00100000b           ;testen ob Bit4 für negatives Movement gesetzt ist
     494                                 ;durch ebx mit 10 gelöscht wurde)
     495     setnz al                    ;wenn ja, setze al auf 1
     496     mov cl,'-'-' '              ;schiebe auf al das Monuszeichen-Space, damit es bei mul mit 0 und addition von space nur space
     497     mul cl                      ;und bei mul mit 1 und addition mit space nur minus wird -> multipliziere al(0 oder 1) mit dem 
     498                                 ;"pre"-zeichen
     499     add al,' '                  ;und addiere zu al space, damit aus dem pre- ein vollständiges zeichen wird
     500     mov [es:edi+6*160+2*8],al   ;das Vorzeichen an der Stelle vor dem Movement platzieren
     501     movzx eax,byte[ycoord]      ;nach eax die Anzahl der y-Bewegungen seit dem letzten Ping holen
     502     test bl,00100000b           ;testen ob das SignBit vom y-movment gesetzt ist, wenn nicht, ist das movement positiv
     503     jz .sign_y                  ;und überspringe den Teil, der aus dem Overflowten, negativen Wert den Betrag erstellt
     504         not al                  ;negiere x-coord, damit der overflow aufgehoben wird, der ensteht, wenn man 0-1 rechnet
     505         inc al                  ;da aber -1 = FFh was genoted 0 wäre, addiere nocheinmal 1
     506     .sign_y:
     507     push edi                    ;edi speicher, da das noch zum berechnen der anderen Positionen benötigt wird
     508     lea di,[edi+6*160+2*12]     ;auf di die Adresse im Video-Speicher, die am Ende der Zahl liegt, schieben
     509     mov cx,3                    ;und auf cx 3 schieben
     510     call ddispdec               ;und prozedur aufrufen, die die Zahl gleich in den Video-Speicher bei es:di speichert
     511     pop edi                     ;nun da edi von ddispdec benutzt wurde, stelle den ursprung wieder her
     512 
     513     movzx eax,word[x]           ;auf eax die auszugebende Zahl, die aktuelle x-Position des MausZeigers, schieben
     514     push edi                    ;edi speicher, da das noch zum berechnen der anderen Positionen benötigt wird
     515     lea di,[edi+7*160+2*11]     ;auf di die Adresse im Video-Speicher, die am Ende der Zahl liegt, schieben
     516     mov cx,5                    ;auf cx 5 schieben, da die auszugebende Zahl maximal 5 Stellen lang sein wird/werden kann
     517     call ddispdec               ;und prozedur aufrufen, die die Zahl gleich in den Video-Speicher bei es:di speichert
     518     pop edi                     ;nun da edi von ddispdec benutzt wurde, stelle den ursprung wieder her
     519 
     520     movzx eax,word[y]           ;auf eax die auszugebende Zahl, die aktuelle y-Position des MausZeigers, schieben
     521     push edi                    ;edi speicher, da das noch zum berechnen der anderen Positionen benötigt wird
     522     lea di,[edi+8*160+2*11]     ;auf di die Adresse im Video-Speicher, die am Ende der Zahl liegt, schieben
     523     mov cx,5                    ;auf cx 5 schieben, da die auszugebende Zahl maximal 5 Stellen lang sein wird/werden kann
     524     call ddispdec               ;und prozedur aufrufen, die die Zahl gleich in den Video-Speicher bei es:di speichert
     525     pop edi                     ;nun da edi von ddispdec benutzt wurde, stelle den ursprung wieder her
     526 
     527     movzx eax,word[z]           ;auf eax die auszugebende Zahl, die aktuelle y-Position des MausZeigers, schieben
     528     push edi                    ;edi speicher, da das noch zum berechnen der anderen Positionen benötigt wird
     529     lea di,[edi+9*160+2*11]     ;auf di die Adresse im Video-Speicher, die am Ende der Zahl liegt, schieben 
     530     mov cx,3                    ;auf cx 3 schieben, da die auszugebende Zahl maximal 3 Stellen lang sein wird/werden kann
     531     call ddispdec               ;und prozedur aufrufen, die die Zahl gleich in den Video-Speicher bei es:di speichert
     532     pop edi                     ;nun da edi von ddispdec benutzt wurde, stelle den ursprung wieder her
     533 
     534     cmp byte[mouseid],4         ;testen ob mausID = 4 für 5 Tasten + Mausrad ist
     535     jne .dont_have_5_buttons    ;wenn nicht, überspringe das abfragen, ob Taste 4 oder 5 gedrückt ist
     536         xor al,al                   ;lösche al, damit man sieht, ob Bit für Taste 4 gesetzt wurde oder nicht
     537         test byte[zbtn45],00010000b ;prüfen ob in Byte4, Bit4 für Taste 4 gesetzt ist, oder nicht,
     538         setnz al                    ;sodass al bei gesetztem Byte 1 und bei gelöschten Byte 0 ist
     539         mov cl,4Fh                  ;4Fh mit dem Bit multiplizieren, sodass bei gesetztem Bit die Hintergrundfarbe rot und
     540                                     ;die schriftfarbe weiß ist
     541         mul cl                      ;und ansonsten alles schwar ist, da 1*Zeichen = Zeichen und 0*Zeichen=kein Zeichen ist
     542         mov [es:edi+5*160],al       ;setzt die Attribute der Zeichen in der linken Taste im Bild so, dass diese rot wird. Ich 
     543         mov [es:edi+6*160],al       ;habe sogar die Speicheraddressierung als Rechnung stehen lassen, damit diese besser 
     544         mov [es:edi+7*160],al       ;nachvollziehbar ist, siehe auch nochmal den Befehl: "mov [es:100h],word 1234h"
     545         mov [es:edi+7*160],al       ;   ~
     546         
     547         xor al,al                   ;lösche al, damit man sieht, ob Bit für Taste 4 gesetzt wurde oder nicht
     548         test byte[zbtn45],00100000b ;prüfen ob in Byte4, Bit5 für Taste 5 gesetzt ist, oder nicht,
     549         setnz al                    ;sodass al bei gesetztem Byte 1 und bei gelöschten Byte 0 ist
     550         mov cl,4Fh                  ;4Fh mit dem Bit multiplizieren, sodass bei gesetztem Bit die Hintergrundfarbe rot und
     551                                     ;die schriftfarbe weiß ist
     552         mul cl                      ;und ansonsten alles schwar ist, da 1*Zeichen = Zeichen und 0*Zeichen=kein Zeichen ist
     553         mov [es:edi+5*160+2*16],al  ;setzt die Attribute der Zeichen in der linken Taste im Bild so, dass diese rot wird. Ich 
     554         mov [es:edi+6*160+2*16],al  ;habe sogar die Speicheraddressierung als Rechnung stehen lassen, damit diese besser 
     555         mov [es:edi+7*160+2*16],al  ;nachvollziehbar ist, siehe auch nochmal den Befehl: "mov [es:100h],word 1234h"
     556         mov [es:edi+7*160+2*16],al  ;   ~
     557     .dont_have_5_buttons:
     558     
     559     popa        ;Register wiederherstellen
     560     ret         ;und Prozedur beenden und zum Aufrufsort zurückkehren
     561 
     562 ddispdec:
     563 ;dies ist die SpezialProzedur, die an die Adresse es:di rückwärtsschreibend (Anfang der Zahl wird es:di-n sein) die Zahl, die in eax liegt 
     564 ;schreibt und den Rest des Platzes, der in cx angegeben ist, aber vlt. von der Zahl nicht ganz ausgenutzt worden ist mit Leezeichen/Space füllt
     565     pushad      ;Register sichern
     566     std         ;Direction-Flag setzen, sodass di nach stosx dekrementiert, statt inkrementiert wird
     567     mov ebx,edx ;edx, die zahlensystembasis nach ebx zum dividieren kopieren
     568     .loop:
     569         xor edx,edx     ;edx löschen, weil dies nach Division der Modulo ist und dann der Dividend edx:eax wäre
     570         div ebx         ;Zahl in eax (eig. edx:eax, aber da edx ja gelöscht ist...) durch ebx teilen
     571         xchg al,dl      ;den Modulo in dx nach al holen um al so auch gleich in dl zu speichern
     572         add al,'0'      ;zu dem Modulo 48 addieren, damit aus der Zahl ein Ascii-Zeichen wird
     573         stosb           ;und Zeichen in Video-Speicher schreiben (die Zahl 12 würde nacheinander 2,1 in den Speicher geschrieben)
     574         dec di          ;di nochmal dekrementieren, da nur ein Zeichen geschrieben wurde und di jetzt auf das Attribut-Byte zeigt
     575         xchg al,dl      ;al und dl wieder tauschen, sodass in eax wie vorher der ganzteilige Quotient der Division liegt
     576         or eax,eax      ;testen ob die Zahl vollständig ausgegeben wurde
     577             jz .loop_end    ;wenn ja, verlasse den loop -> in cx ist dann die Anzahl der Zeichen, die die Zahl einnehmen sollte, 
     578                             ;um diese zu löschen
     579         loop .loop      ;ansonsten führe die schleife so oft aus, bis cx 0 ist
     580     .loop_end:
     581     mov ax,0F20h    ;nach Ende des Ausgebens der Zahl, schiebe auf ax ein Zeichen(Space/20h) und das Attribut-Byte
     582     rep stosw       ;um mit der schnellen Variante mit rep die übrigen in cx angegeben Felder mit Space zu füllen
     583     cld             ;danach lösche das Direction-Flag, da es standardmäßg gelöscht sein sollte
     584     popad           ;dann stelle die Register wieder her
     585     ret             ;und kehre zum Aufrufsort zurück

\</asm\>

Und das wars auch schon von mir, mehr ist nicht zu sagen, vor allem, da ich den Code extra stark kommentiert habe. Am Anfang des Dokuments ist der Downloadlink dessen, viel Spaß damit und viel Glück bei eurem OS xD. Wer sich noch tiefer in das Thema einlesen will, dem empfehle ich folgendes [Dokument](http://maxinator.meugster.net/programming/ps2mouse/tp-intf2-4.PDF) über das Synaptic-Touchpad, in dem auch das PS/2-Protokoll gut beschrieben ist. Das ganze Programm kann auch gleich auf meinem [OS](http://maxinator.meugster.net/programme/downloads.html) getestet werden, indem ihr in die Shell als Befehl einfach "ps2mouse" oder "run ps2mouse" eingebt.

Soviel von mir, für Fragen per ICQ(412207644) stehe ich gerne zur Verfügung. Zum erstellen des "bunten" Codes habe ich [Andres Highlighter 2.6.5](http://www.andre-simon.de/) genutzt. Das Original dieses Dokuments ist auch \[ hier\] zu finde und stammt von mir.

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/2227/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1559/index.html)

<!-- MediaWiki page 1559; revision 2227; parent 2226; 2007-11-11T18:48:14Z -->
