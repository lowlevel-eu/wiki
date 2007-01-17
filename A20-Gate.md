# A20-Gate

Auch wenn in diesem Tutorial der Keyboard-Controller teilweise angesprochen wird, ist dies KEIN ausführliches Tutorial über den Keyboard-Controller selbst, sondern bezieht sich lediglich auf das A20 Gate.

## Was ist das A20 Gate und warum muß es extra eingeschaltet werden?

Wie wohl bekannt sein sollt, hatte der 8086 20 Adressleitungen (A0 - A19) über die ein Arbeitsspeicher von maximal 1 Megabyte adressiert werden konnte. Da man aber nur 16 Bit breite Register hatte, musste man sich einem Trick behelfen um trotzdem Adressen von 20 Bit Länge bilden zu können. Dazu hat man den Arbeitsspeicher in sogenannte Segmente unterteilt von dem jedes 16 Byte groß ist. Das ist keine Wilkür gewesen, das es gerade 16 Bytes sind, sondern hat den Hintergrund, das man mit 20 Bit 16 mal so große Zahlen darstellen kann wie mit 16 Bits. Um nun eine bestimmte Adresse im Speicher ansprechen zu können, muß zuersteinaml das Segment angegeben werden in dem sich diese Adresse befindet. Dazu wird eines der Segmentregister mit dem entsprechendem 16 Bit Wert geladen. Und um sich innerhalb eines Segmentes bewegen zu können, brauchte man noch ein weiteres 16 Bit Register, das als Offset diente. Das Offset beginnt am Anfang des Segmentes.

Beispiel:

Angenommen wir haben 1 MB Speicher und möchten nun das Byte das sich an der linearen Adresse 0xF0010 befindet ansprechen.

Da hier eine 20 Bit Adresse vorliegt, müssen wir diese zuersteinmal in einen Segment- und einen Offsetanteil zerlegen. Dabei haben wir mehrere Möglichkeiten dies zu tun. Einigen wir uns mal darauf das wir als Segment die Adresse 0xF000 und als Offset 0x10 nehmen. Wenn wir nun auf das Byte zugreifen, dann legt der Prozessor zuerst den Segmentteil (0xF000) auf die Adressleitung und verschiebt diesen Wert um 4 Bit nach Links. Daraus entsteht dann der Wert 0xF0000. Anschliessend wird der Offsetteil dazuaddiert. Nun ist auf dem Adressbus der Wert 0xF0010 und wir können das betreffende Byte lesen.

Wie ich eben schon erwähnt habe, gibt es mehrer Möglichkeiten eine lineare Adresse in Segment und Offset zu unterteilen. Überlegen wir nun warum:

Wie eben schon gesagt wird der Speicher in Segmente zu je 16 Byte unterteilt und dann das Offset dazuaddiert. Das Offset ist aber ein 16 Bit-Zahl. Und mit 16 Bits können wir Zahlen bis 65535 darstellen. Das sind weit mehr als 16 Byte. Nähmlich genau 64 KB. Daher könnte man auch meinen das ein Segment eigentlich keine 16 Bytes, sonder 64 Kilobytes groß ist. Das stimmt im gewissen Sinne auch. Aber schauen wir uns den Segmentteil von eben (0xF000) nochmal an. Nehmen wir mal an das unser Offset auf 0 gesetzt ist. Dann ergibt sich nun eine lineare Adresse von 0xF0000 + 0x0 = 0xF0000.

Wenn wir nun NUR die Segmentadresse um 1 erhöhen, erhalten wir im Segmentregister den Wert 0xF001. Legen wir diesen wieder zusammen mit dem Offset 0 auf die Adressleitung erhalten wir die Adresse 0xF0010. Siehe da, es ist genau die Adresse die wir oben aus dem Segment und dem Offset "zusammengebaut" haben. Als erstes sollte hier auffalen, das zwischen em Wert 0xF0000 und 0xF0010 genau 16 Bytes Unterschied ist. Also sind die einzelnen Segmente 16 Bytes voneinander getrennt. Da wir aber mit einem 16 Bit Offset 64 Kilobytes vom Anfang des Segmentes adressieren können, sind die die Segmente für uns "virtuell" 64 KB groß. Wir können also 64 Kilobytes ansprechen OHNE den Wert im Segmentregister ändern zu müssen.

So nun führen wir das ganze ein Stück weiter. Wie ja bekannt ist, ist der höchste Wert den ich in 16 Bit darstellen kann 0xFFFF (dez 65535). Nehmen wir diesen Wert einmal und schreiben ihn in ein Segmentregister. Jetzt legen wir diesen Wert wieder auf die Adressleitung und belassen das Offset bei 0. Dann erhalten wir als lineare Adresse 0xFFFF0. Und diese Adresse ist genau 16 Bytes unterhalb der 1 MB-Grenze.

Was nun aber wenn wir als Offset nicht mehr 0, sondern vielleicht 1000 nehmen? Dann wären wir doch ÜBER der 1 MB Grenze!? Genau so ist es. Aber es entsteht kein Fehler im Sinne, das wir irgendeinen Speicherbereich addressieren, den es eigentlich garnicht gibt, sondern der Rechner fängt dann einfach wieder bei 0 an. Das bedeutet, das jede Adresse die ich oberhalb der 1 MB Grenze anspreche, eigentlich am Anfang des Speichers liegt. Das ganze nennt man Wrap-Around.

Zu Zeiten von DOS hat man diesen Wrap-Around ganz gezielt für gewisse Programme genutzt.

Was würde nun aber passieren, wenn wir dieses DOS-Programm, das ja damit rechnet das es oberhalb von 1 MB einen Wrap-Around gibt in einem 386er laufen lassen, der ja bekanntlich nicht mehr nur 20, sondern 32 Bit für den Adressbus hat. In diesem Fall würde ja ein Speicherbereich oberhalb von 1 MB existieren und das DOS-Programm würde womöglich einen Fehler machen, der im ersten Augenblick wohl garnicht auffallen würde, aber am Ende vielleicht fatal wäre.

Und um der Sache abhilfe zu schaffen, haben die IBM-Entwickler eine Möglichkeit geschaffen die 21te Adressleitung abschalten zu können. Somit würde es bei 1 MB wieder einen Wrap-Around geben und alle Programm wären zufrieden. Und da beim Booten des PCs der Prozessor von Anfang an eh im Real-Mode arbeitet, ist auch die 21te Adressleitung (A20) von Anfang an abgeschaltet.

Wenn wir nun aber in den Protected Mode wechseln und nun ohne Probleme mit 32 Bit arbeiten können und möchten, müssen wir diese 21te Leitung wieder aktivieren, da wir sonst bei manchen Speicherzugriffen fehler haben, da die 21te Adressleitung ja deaktiviert ist. Das würde bedeuten, das wir unter umständen auf eine andere Speicherstelle zugreifen würden, als wir das eigentlich möchten. Also sollten wir diese anschalten BEVOR wir groß andere Programme (Kernel) starten.

Um den "Schaden" so gering wie möglich zu halten, haben die IBM Entwickler nicht gleich einen extra Chip in den PC eingebaut NUR um das A20Gate aktivieren zu können, sondern haben diese Funktion in den Tastatur-Controller eingebaut, da dieser noch genügen ungenutzte Ressourcen hatte. Daher werden wir gleich mit jenem In Verbindung treten um das A20Gate zu überreden, das es aus dem Winterschlaf erwachen soll.

  

## Einschalten

Nachdem wir dir Ursache und Notwendigkeit des A20 Gates geklärt haben, widmen wir uns num dem Einschalten des Gates zu. Dazu ist ein lediglich minimales Wissen über den Tastatur-Controller notwendig, welches ich natürlich nicht für mich behalten werde :)

Zuersteinmal sollte klar sein, das es ZWEI Controller gibt, die für die Tastatur zuständig sind. Zum einen der eigentliche Controller auf dem Mainboard und einen weietern der direkt in der Tastatur integriert ist. Um die beiden besser auseinander halten zu können, nennen wir den Tastatur-Controller auf dem Mainboard auch einfach Tastatur-Controller und den Controller in der Tastatur selbst betiteln wir einfach mal als Tastatur-Chip.

Das erste was man wissen muß, ist das der Tastatur-Controller über Port 0x64 und der Tastatur-Chip über Port 0x60 angesprochen wird. Der Tastatur-Controller übernimmt dabei die Hauptaufgaben und nimmt in erster Linie die Befehle entgegen. Der Tastatur-Chip liefert meistens nur Daten oder empfäng solche.

Als nächste wäre zu wissen, das das einschalten des A20 Gates mit dem einfachen setzen eines bestimmten Bits geschieht. Nämlich dem Bit0 im Tastatur-Chip Output Port. Die Bezeichnung Port soll hier nicht irreführend sein. DIESEN Port können wir nämlich nicht direkt ansteuern, sondern nur über einen kleinen Umweg.

Und diesen Umweg will ich nun beschreiben.

Zuersteinmal müssen wir überprüfen ob der Tastatur-Controller empfangsbereit ist. Dies ist er, sobald sein "Input Buffer" leer ist. Und das können wir testen, indem wir ein Byte vom Port 0x64 lesen und schauen ob das Bit1 gesetzt ist. Wenn es NICHT gesetzt ist, dann ist der Input Buffer leer und wir können einen Befehl an den Tastatur-Controller schicken. Wenn dieser NICHT leer ist, dann lassen wir einfach eine endlosschleife laufen, die immer wieder überprüft ob der Buffer nun leer ist.

Hier der Code um abzufragen ob der Tastatur-Controller Input Buffer frei ist:

    .1:
        in  al, 0x64    ;Tastatur-Controller-Statusbyte lesen
        test    al, 00000010b   ;Ist das Bit1 gesetzt?
        jnz     .1  ;Wenn ja, dann wiederhole den Vorgang

Wenn die Schleife nun beendet wird, wenn also das Bit1 NICHT MEHR gesetzt ist, dann können wir dem Tastatur-Controller einen Befehl senden. Und zwar möchten wir das Statusbyte des Tastatur-Chips Output Ports lesen.

Dazu schicken wir den Befehl 0xD0 an den Tastatur-Controller.

Das geschieht mit folgendem Code:

        mov  al, 0xD0    ;Befehl zum lesen des Output Port Statusbytes in AL speichern
        out     0x64, al    ;Befehl an den Tastatur-Controller senden

  
Nun wird der Tastatur-Controller mit dem Tastatur-Chip kommunizieren und ihm mitteilen, das er sein Output Port Statusbyte auf den Port 0x60 legen soll, damit wir es von dort lesen können. Da das ganze aber auch seine Zeit braucht, bis das Byte bereit steht, brauchen wir wieder eine kleine Endlosschleife die uns EBENFALLS von Port 0x64 das Statusbyte des Tastatur-Controllers liest und das Bit0 prüft. Das Bit0 wird nämlich auf 1 gesetzt, sobald Daten vom Tastatur-Chip abrufbar sind. Man sieht also, das die beiden Controller sehr eng miteinander verknüpft sind.

Hier der Code zum warten auf das Byte:

    .2:
        in  al, 0x64    ;Tastatur-Controller Statusbyte lesen
        test    al, 00000001b   ;Bit0 testen ob es gesetzt ist
        jz  .2  ;Wenn es NOCH NICHT gesetzt ist, wiederhole den Vorgang

  
Wenn nun die Schleife verlassen wird, steht das Byte abrufbereit. Wir werden es uns dann nun abholen und gleich etwas modifizieren. Es ist das selbe Prinzip wir beim schalten in den Protected Mode. Zuerst wird das Original-Statusbyte gelesen. Dann wird das betreffende Bit (hier Bit1) gesetzt und das Byte wieder zurückgeschrieben.

Mit folgendem Code holen wir uns das Byte, setzen das Bit1 auf 1 und speichern das Byte (befindet sich nach dem lesen in AL bzw. EAX) auf dem Stack zwischen. Das müssen wir tun, da wir Al bzw. EAX noch für ein paar Zwischenschritte benötigen, bevor wir das Statusbyte wieder zurückschreiben können. Man könnte EAX auch in einem anderen Register zwischenspeichern. Das ist dann einfach Ansichtssache.

        in   al, 0x60    ;Output Port Statusbyte von Tastatur-Chip lesen
        or  al, 00000010b   ;Bit1 auf 1 setzen. A20Gate Enable Bit
        push    eax     ;EAX zwischenspeichern

So nun geht das Spielchen nochmal von vorne los. Wir müssen nun erst wieder warten das wir einen Befehl an den Tastatur-Controller schicken können. Dazu der folgende Code, welcher identisch mit bereits oben genannten ist:

    .3:
        in  al, 0x64    ;Tastatur-Controller-Statusbyte lesen
        test    al, 00000010b   ;Ist das Bit1 gesetzt?
        jnz     .3  ;Wenn ja, dann wiederhole den Vorgang

Nun können wir wieder einen Befehl senden und tun dies auch gleich. Diesmal jedoch senden wir den Befehl der dem Tastatur-Controller mitteilt, das wir das Statusbyte des Output Ports wieder zurückschreiben möchten.

Dazu dient folgender Code:

        mov  al, 0xD1    ;Befehl zum schreiben des Statusbytes des Output Ports in AL schreiben
        out     0x64, al    ;Befehl an den Tastatur-Controller senden

  
Und wie so üblich müssen wir WIEDER warten das wir Daten senden können. Also nochmal:

    .4:
        in  al, 0x64    ;Tastatur-Controller-Statusbyte lesen
        test    al, 00000010b   ;Ist das Bit1 gesetzt?
        jnz     .4  ;Wenn ja, dann wiederhole den Vorgang

Und nun holen wir uns das Statusbyte wieder vom Stack und senden es an den Tastatur-Chip.

        pop  eax     ;Statusbyte vom Stack holen
        out     0x60, al    ;An Tastatur-Chip senden

  
Nun sollte das A20 Gate eingeschaltet sein. Um das zu prüfen, lesen wir das Output Port Statusbyte ERNEUT aus und schauen ob das Bit1 (A20 Gate Enable Bit) IMMER NOCH gesetzt ist. Da hier aber nichts neues mehr kommt, sondern im Endeffekt nur nochmal die ersten paar Befehlsfolgen, kürze ich das an dieser Stelle ab. Wer gerne etwas basteln möchte, der reimt sich diese Überprüfung selbst zusammen. Und für die faulen stelle ich den ganzen Code auf in einer feinen Funktion zu Download bereit.

Die Funktion kann vom C-Kernel (möglichst am Anfang natürlich) aufgerufen werden. Als Rückgabewert wird 1 zurückgegeben, wenn nach dem Prüfen das A20 Gate Enable Bit noch gesetzt ist, oder 0, falls dieses nicht gesetzt ist.

Der Prototyp der Funktion für C lautet wie folgt:

    unsigned int EnableA20Gate();

Wer seinen C-Kernel nach meiner Methode (Siehe C-Kernel Tut) startet, der kann diese Funktion am besten in die kernel32.asm Datei packen.

[Download](http://www.jay-code.de/files/a20gate.asm)

  

\(c\) Copyright by TeeJay (teejay@jay-code.de)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/1684/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1462/index.html)

<!-- MediaWiki page 1462; revision 1684; parent 1683; 2007-01-17T08:48:37Z -->
