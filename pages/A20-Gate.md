# A20-Gate

| A20-Gate |  |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| **Schwierigkeit**: [<img src="assets/Stern_gold.gif" width="16" height="16" alt="Stern gold.gif" />](assets/Stern_gold.gif)[<img src="assets/Stern_wei%C3%9F.gif" width="16" height="16" alt="Stern weiß.gif" />](assets/Stern_wei%C3%9F.gif)[<img src="assets/Stern_wei%C3%9F.gif" width="16" height="16" alt="Stern weiß.gif" />](assets/Stern_wei%C3%9F.gif)[<img src="assets/Stern_wei%C3%9F.gif" width="16" height="16" alt="Stern weiß.gif" />](assets/Stern_wei%C3%9F.gif)[<img src="assets/Stern_wei%C3%9F.gif" width="16" height="16" alt="Stern weiß.gif" />](assets/Stern_wei%C3%9F.gif)<br> |  |
| Benötigtes Vorwissen: | [BIOS](Basic-Input-Output-System "BIOS") |
| Sprache: | Assembler |

Das A20-Gate steuert die 21. Adressleitung der CPU. Diese muss aktiviert werden, um ungerade Megabytes (wenn man bei 0 mit Zählen beginnt) im Arbeitsspeicher adressieren zu können.

*Hinweis: Auch wenn in diesem Tutorial der Keyboard-Controller teilweise angesprochen wird, ist dies **kein** ausführliches Tutorial über den Keyboard-Controller selbst, sondern bezieht sich lediglich auf das A20-Gate.*

## Was ist das A20-Gate und warum muss es extra eingeschaltet werden?

Wie wohl bekannt sein sollte, hatte der 8086 20 Adressleitungen (A0 – A19) über die ein Arbeitsspeicher von maximal einem Megabyte adressiert werden konnte. Da man aber nur 16 Bit breite Register hatte, musste man sich mit einem Trick behelfen, um trotzdem Adressen von 20 Bit Länge bilden zu können. Dazu hat man den Arbeitsspeicher in sogenannte Segmente unterteilt, von denen jedes 16 Byte groß ist. Dies geschah nicht willkürlich, sondern hat den Hintergrund, dass man mit 20 Bit 16-mal so große Zahlen darstellen kann wie mit 16 Bits. Um nun eine bestimmte Adresse im Speicher ansprechen zu können, muß zuerst einmal das Segment angegeben werden, in dem sich diese Adresse befindet. Dazu wird eines der Segmentregister mit dem entsprechendem 16-Bit-Wert geladen. Und um sich innerhalb eines Segmentes bewegen zu können, brauchte man noch ein weiteres 16-Bit-Register, das als Offset diente. Dieser Offset beginnt am Anfang des Segmentes.

Beispiel:

Angenommen wir haben 1 MB Speicher und möchten nun das Byte, das sich an der linearen Adresse 0xF0010 befindet, ansprechen.

Da hier eine 20-Bit-Adresse vorliegt, müssen wir diese zuerst einmal in einen Segment- und einen Offsetanteil zerlegen. Dabei haben wir mehrere Möglichkeiten, dies zu tun. Einigen wir uns mal darauf, dass wir als Segment die Adresse 0xF000 und als Offset 0x10 nehmen. Wenn wir nun auf das Byte zugreifen, dann legt der Prozessor zuerst den Segmentteil (0xF000) auf die Adressleitung und verschiebt diesen Wert um 4 Bit nach links. Daraus entsteht dann der Wert 0xF0000. Anschließend wird der Offsetteil dazuaddiert. Nun ist auf dem Adressbus der Wert 0xF0010 und wir können das betreffende Byte lesen.

Wie ich eben schon erwähnt habe, gibt es mehrere Möglichkeiten, eine lineare Adresse in Segment und Offset zu unterteilen. Überlegen wir nun, warum:

Wie eben schon gesagt, wird der Speicher in Segmente zu je 16 Byte unterteilt und dann das Offset dazuaddiert. Das Offset ist aber eine 16-Bit-Zahl. Und mit 16 Bits können wir Zahlen bis 65535 darstellen. Das sind weit mehr als 16 Byte. Nämlich genau 64 kB. Daher könnte man auch meinen, dass ein Segment eigentlich keine 16 Bytes, sondern 64 Kilobytes groß ist. Das stimmt im gewissen Sinne auch. Aber schauen wir uns den Segmentteil von eben (0xF000) nochmal an. Nehmen wir mal an, dass unser Offset auf 0 gesetzt ist. Dann ergibt sich nun eine lineare Adresse von 0xF0000 + 0x0 = 0xF0000.

Wenn wir nun **nur** die Segmentadresse um 1 erhöhen, erhalten wir im Segmentregister den Wert 0xF001. Legen wir diesen wieder zusammen mit dem Offset 0 auf die Adressleitung, erhalten wir die Adresse 0xF0010. Siehe da, es ist genau die Adresse, die wir oben aus dem Segment und dem Offset „zusammengebaut“ haben. Als erstes sollte hier auffallen, dass zwischen dem Wert 0xF0000 und 0xF0010 genau 16 Bytes Unterschied sind. Also sind die einzelnen Segmente 16 Bytes voneinander getrennt. Da wir aber mit einem 16-Bit-Offset 64 Kilobytes vom Anfang des Segmentes adressieren können, sind die die Segmente für uns „virtuell“ 64 kB groß. Wir können also 64 Kilobytes ansprechen, **ohne** den Wert im Segmentregister ändern zu müssen.

Nun führen wir das ganze ein Stück weiter. Wie ja bekannt ist, ist der höchste in 16 Bit darstellbare Wert 0xFFFF (dez. 65535). Nehmen wir diesen Wert einmal und schreiben ihn in ein Segmentregister. Jetzt legen wir diesen Wert wieder auf die Adressleitung und belassen das Offset bei 0. Dann erhalten wir als lineare Adresse 0xFFFF0. Und diese Adresse ist genau 16 Bytes unterhalb der 1-MB-Grenze.

Was passiert aber, wenn wir als Offset nicht mehr 0, sondern vielleicht 1000 nehmen? Dann wären wir doch **über** der 1-MB-Grenze!? Genau so ist es. Aber es entsteht kein Fehler in dem Sinne, dass wir irgendeinen Speicherbereich addressieren, den es eigentlich gar nicht gibt, sondern der Rechner fängt dann einfach wieder bei 0 an. Das bedeutet, dass jede Adresse, die oberhalb der 1-MB-Grenze angesprochen wird, eigentlich am Anfang des Speichers liegt. Das nennt man Wrap-Around.

Zu Zeiten von DOS hat man diesen Wrap-Around ganz gezielt für gewisse Programme genutzt.

Was würde nun aber passieren, wenn wir dieses DOS-Programm, das ja damit rechnet, dass es oberhalb von 1 MB einen Wrap-Around gibt, in einem 386er laufen lassen, der ja bekanntlich nicht mehr nur 20, sondern 32 Bit für den Adressbus hat? In diesem Fall würde ja ein Speicherbereich oberhalb von 1 MB existieren und das DOS-Programm würde womöglich einen Fehler machen, der im ersten Augenblick wohl gar nicht auffallen würde, aber am Ende vielleicht fatal wäre.

Und um der Sache Abhilfe zu schaffen, haben die IBM-Entwickler eine Möglichkeit geschaffen, die 21te Adressleitung abschalten zu können. Somit würde es bei 1 MB wieder einen Wrap-Around geben und alle Programm wären zufrieden. Und da beim Booten des PCs der Prozessor von Anfang an eh im Real-Mode arbeitet, ist auch die 21te Adressleitung (A20) von Anfang an abgeschaltet.

Wenn wir nun aber in den Protected Mode wechseln und nun ohne Probleme mit 32 Bit arbeiten können und möchten, müssen wir diese 21te Leitung wieder aktivieren, da wir sonst bei manchen Speicherzugriffen Fehler haben, da die 21te Adressleitung ja deaktiviert ist. Das würde bedeuten, dass wir unter Umständen auf eine andere Speicherstelle zugreifen würden, als wir das eigentlich möchten. Also sollten wir diese anschalten, **bevor** wir andere Programme (Kernel) starten.

Um den „Schaden“ so gering wie möglich zu halten, haben die IBM-Entwickler nicht gleich einen extra Chip in den PC eingebaut, nur um das A20Gate aktivieren zu können, sondern haben diese Funktion in den Tastatur-Controller eingebaut, da dieser noch genügend ungenutzte Ressourcen besaß. Daher werden wir gleich mit jenem in Verbindung treten, um das A20-Gate zu überreden, dass es aus dem Winterschlaf erwachen soll.

  

## Einschalten

Nachdem wir die Ursache und Notwendigkeit des A20-Gates geklärt haben, wenden wir uns nun dem Einschalten des Gates zu. Dazu ist lediglich ein minimales Wissen über den Tastatur-Controller notwendig, welches ich natürlich nicht für mich behalten werde. :)

Zuerst einmal sollte klar sein, dass es **zwei** Controller gibt, die für die Tastatur zuständig sind. Zum einen der eigentliche Controller auf dem Mainboard und einen weiteren, der direkt in der Tastatur integriert ist. Um die beiden besser auseinander halten zu können, nennen wir den Tastatur-Controller auf dem Mainboard auch einfach Tastatur-Controller und den Controller in der Tastatur selbst betiteln wir einfach mal als Tastatur-Chip.

Das erste, was man wissen muss, ist, dass der Tastatur-Controller über Port 0x64 und der Tastatur-Chip über Port 0x60 angesprochen wird. Der Tastatur-Controller übernimmt dabei die Hauptaufgaben und nimmt in erster Linie die Befehle entgegen. Der Tastatur-Chip liefert meistens nur Daten oder empfängt solche.

Als nächstes wäre zu wissen, dass das Einschalten des A20-Gates mit dem einfachen Setzen eines bestimmten Bits geschieht. Nämlich dem Bit 0 im Tastatur-Chip Output Port. Die Bezeichnung Port soll hier nicht irreführend sein. **Diesen** Port können wir nämlich nicht direkt ansteuern, sondern nur über einen kleinen Umweg.

Und diesen Umweg will ich nun beschreiben.

Zuerst einmal müssen wir überprüfen, ob der Tastatur-Controller empfangsbereit ist. Dies ist er, sobald sein „Input-Buffer“ leer ist. Und das können wir testen, indem wir ein Byte vom Port 0x64 lesen und schauen, ob das Bit 1 gesetzt ist. Wenn es **nicht** gesetzt ist, dann ist der Input-Buffer leer und wir können einen Befehl an den Tastatur-Controller schicken. Wenn dieser **nicht** leer ist, dann lassen wir einfach eine Endlosschleife laufen, die immer wieder überprüft, ob der Buffer nun leer ist.

Hier der Code, um abzufragen, ob der Tastatur-Controller Input-Buffer frei ist:

\<asm\> .1:

        in   al, 0x64      ;Tastatur-Controller-Statusbyte lesen
        test    al, 00000010b ;Ist Bit 1 gesetzt?
        jnz     .1            ;Wenn ja, dann wiederhole den Vorgang</asm>

Wenn die Schleife nun beendet wird, wenn also das Bit 1 **nicht mehr** gesetzt ist, dann können wir dem Tastatur-Controller einen Befehl senden. Und zwar möchten wir das Statusbyte des Tastatur-Chip-Output-Ports lesen.

Dazu schicken wir den Befehl 0xD0 an den Tastatur-Controller.

Das geschieht mit folgendem Code:

\<asm\> mov al, 0xD0 ;Befehl zum Lesen des Output-Port-Statusbytes in AL speichern

        out   0x64, al ;Befehl an den Tastatur-Controller senden</asm>

  
Nun wird der Tastatur-Controller mit dem Tastatur-Chip kommunizieren und ihm mitteilen, dass er sein Output Port Statusbyte auf den Port 0x60 legen soll, damit wir es von dort lesen können. Da das ganze aber auch seine Zeit braucht, bis das Byte bereit steht, brauchen wir wieder eine kleine Endlosschleife die **ebenfalls** von Port 0x64 das Statusbyte des Tastatur-Controllers liest und das Bit 0 prüft. Das Bit 0 wird nämlich auf 1 gesetzt, sobald Daten vom Tastatur-Chip abrufbar sind. Man sieht also, dass die beiden Controller sehr eng miteinander verknüpft sind.

Hier der Code zum Warten auf das Byte:

\<asm\> .2:

        in    al, 0x64       ;Tastatur-Controller-Statusbyte lesen
        test  al, 00000001b  ;Bit 0 testen, ob es gesetzt ist
        jz    .2             ;Wenn es noch nicht gesetzt ist, wiederhole den Vorgang</asm>

  
Wenn nun die Schleife verlassen wird, steht das Byte abrufbereit. Wir werden es uns dann abholen und gleich etwas modifizieren. Das ist das selbe Prinzip wie beim Schalten in den Protected Mode. Zuerst wird das Original-Statusbyte gelesen, dann wird das betreffende Bit (hier Bit 1) gesetzt und das Byte wieder zurückgeschrieben.

Mit folgendem Code holen wir uns das Byte, setzen das Bit 1 auf 1 und speichern das Byte (befindet sich nach dem Lesen in AL bzw. EAX) auf dem Stack. Das müssen wir tun, da wir AL bzw. EAX noch für ein paar Zwischenschritte benötigen, bevor wir das Statusbyte wieder zurückschreiben können. Man könnte EAX auch in einem anderen Register zwischenspeichern. Das ist dann einfach Ansichtssache.

\<asm\> in al, 0x60  ;Output-Port-Statusbyte von Tastatur-Chip lesen

        or    al, 00000010b  ;Bit 1 auf 1 setzen (A20Gate-Enable-Bit)
        push  eax            ;EAX zwischenspeichern</asm>

So nun geht das Spielchen nochmal von vorne los. Wir müssen nun erst wieder warten, bis wir einen Befehl an den Tastatur-Controller schicken können. Dazu der folgende Code, welcher identisch mit bereits oben genannten ist:

\<asm\> .3:

        in    al, 0x64       ;Tastatur-Controller-Statusbyte lesen
        test  al, 00000010b  ;Ist das Bit 1 gesetzt?
        jnz   .3             ;Wenn ja, dann wiederhole den Vorgang</asm>

Nun können wir wieder einen Befehl senden und tun dies auch gleich. Diesmal jedoch senden wir den Befehl, der dem Tastatur-Controller mitteilt, dass wir das Statusbyte des Output-Ports wieder zurückschreiben möchten.

Dazu dient folgender Code:

\<asm\> mov al, 0xD1  ;Befehl zum Schreiben des Statusbytes des Output-Ports in AL schreiben

        out   0x64, al  ;Befehl an den Tastatur-Controller senden</asm>

  
Und wie so üblich müssen wir **wieder** warten, bis wir Daten senden können. Also nochmal:

\<asm\> .4:

        in    al, 0x64       ;Tastatur-Controller-Statusbyte lesen
        test  al, 00000010b  ;Ist das Bit 1 gesetzt?
        jnz   .4             ;Wenn ja, dann wiederhole den Vorgang</asm>

Und nun holen wir uns das Statusbyte wieder vom Stack und senden es an den Tastatur-Chip.

\<asm\> pop eax  ;Statusbyte vom Stack holen

        out   0x60, al  ;An Tastatur-Chip senden</asm>

  
Nun sollte das A20-Gate eingeschaltet sein. Um das zu prüfen, lesen wir das Output-Port-Statusbyte **erneut** aus und schauen, ob das Bit 1 (A20-Gate-Enable-Bit) **immer noch** gesetzt ist. Da hier aber nichts neues mehr kommt, sondern im Endeffekt nur nochmal die ersten paar Befehlsfolgen, kürze ich das an dieser Stelle ab. Wer gerne etwas basteln möchte, der reimt sich diese Überprüfung selbst zusammen. Und für die Faulen stelle ich den ganzen Code in einer feinen Funktion zu Download bereit.

Die Funktion kann vom C-Kernel (möglichst am Anfang natürlich) aufgerufen werden. Als Rückgabewert wird 1 zurückgegeben, wenn nach dem Prüfen das A20-Gate-Enable-Bit noch gesetzt ist, oder 0, falls dieses nicht gesetzt ist.

Der Prototyp der Funktion für C lautet wie folgt:

\<c\>unsigned int EnableA20Gate();\</c\>

Wer seinen C-Kernel nach meiner Methode (Siehe C-Kernel-Tut) startet, der kann diese Funktion am besten in die kernel32.asm-Datei packen.

[Download](http://www.jay-code.de/files/a20gate.asm)

## Einschalten mittels System Control Port A

Es gibt noch eine zweite Möglichkeit, das A20-Gate zu aktivieren. Sie wurde erst später eingeführt, ist dementsprechend nicht auf jedem System verfügbar. Man benutzt dafür Port 0x92. Der Code dafür lautet: \<asm\>in al, 0x92 or al, 02 out 0x92, al\</asm\> Bei dieser Variante sei allerdings gesagt, dass sie immer wieder zu Problemen führt. Oft treten Bildprobleme auf oder es kommt zu Systemabstürzen. Sie ist allerdings bei weitem schneller als die Variante mittels KBC.

## Einschalten über das BIOS

Es gibt sogar noch eine dritte Möglichkeit, das A20-Gate zu aktiveren. Vor allem neuere [BIOS](Basic-Input-Output-System "BIOS") besitzen diese Möglichkeit. Dafür benutzt man den Interrupt 0x15 mit AX=0x2401. Hier eine kleine Tabelle:

INT 0x15 AX=0x2400 --\> A20 auschalten  
INT 0x15 AX=0x2401 --\> A20 einschalten  
INT 0x15 AX=0x2402 --\> Status abfragen (AL: 0 --\> aus; AL: 1 --\> an)  
INT 0x15 AX=0x2403 --\> Support abfragen (BX Bit 0: kbc; Bit 1: Port 0x92)  

Wenn erfolgreich: CF nicht gesetzt, AH = 0x00  
Bei Fehler: CF gesetzt, AH=Status  

Status: 0x01 Keyboard im Secure Mode  
0x86 Funktion wird nicht unterstützt  

## Links

- [Wikipedia A20-Gate](http://de.wikipedia.org/wiki/A20-Gate)
- [A20-Gate – a pain from the past (Englisches Tutorial)](http://www.win.tue.nl/~aeb/linux/kbd/A20.html)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/9429/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1462/index.html)

<!-- MediaWiki page 1462; revision 9429; parent 7637; 2011-02-05T12:24:59Z -->
