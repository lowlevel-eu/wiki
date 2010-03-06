# Universal Serial Bus

**Hinweis:**

Der Autor kannte sich bei Erstellung des Artikels nicht besonders mit dem Thema aus. Da dieses Thema aber dringend nach einem Artikel verlangte (z. B. aufgrund eines Eintrags in der [TODO](https://github.com/lowlevel-eu/wiki/wiki/TODO "TODO")-Liste), hat er sich dennoch entschieden, seine Kenntnisse niederzuschreiben.

Wenn **du** dich mit diesem Thema einigermaßen auskennst, dann bist du **jetzt** aufgerufen, diesen Artikel zu erweitern und/oder zu korrigieren (oder natürlich diesen Hinweis zu entfernen, wenn du den Artikel für korrekt befindest)!

Der **Universal Serial Bus** (kurz **USB**) ist ein [Bus](https://lowlevel-eu.github.io/wiki/pages/1769/index.html "Kategorie:Bus") zur Verbindung von Geräten mit einem PC und wird von praktisch jedem modernen Computer unterstützt. USB ist abwärtskompatibel, d. h., dass man lagsame USB 1.0-Geräte an den schnelleren USB 2.0 oder 3.0 anschließen kann und umgekehrt.

## Einsatzgebiete

USB ist sehr vielseitig verwendbar, es eignet sich z. B. für externe Festplatten, Flashspeicher (USB-Sticks), Drucker, Kartenleser, Multimediageräte, HID-Geräte und vieles mehr. Ursprünglich wurde es für langsame Geräte wie Drucker, Tastatur oder Maus entworfen, mit den Geschwindigkeitsklassen High-Speed (seit USB 2.0) und SuperSpeed (seit USB 3.0) jedoch eignet es sich auch für Geräte, die eine höhere Bandbreite benötigen, wie Festplatten oder Webcams.

## Spezifikationen

**Für alle USB-Spezifikationen gilt**:

- Spannung: 5 V
- Stromstärke: 100 mA (bei USB 3.0 150 mA); nach besonderer Freigabe bis zu 500 mA (bei USB 3.0 900 mA)

### USB 3.0

USB 3.0 ist noch sehr spärlich verfügbar. Erste Spezifikationen gab es 2008, USB 3.0 erlaubt eine Übertragungsrate von 5,0 GBit/s (SuperSpeed) was durch die [8b10b-Codierung](http://de.wikipedia.org/wiki/8b10b-Code) 500 MByte/s Brutto-Transferrate ergibt. Zudem kann ein Gerät auf Anfrage bis zu 900 mA statt der bisherigen 500 mA erhalten. Damit lassen sich problemlos USB-Festplatten ohne externe Stromquelle anschließen.

### USB 2.0

USB 2.0 wurde im Jahr 2000 veröffentlicht und bot erstmal High-Speed mit einer Übertragungsrate von 480 MBit/s an.

### USB 1.1

USB 1.1 wurde 1998 veröffentlicht und behob einige Fehler und Unklarheiten

### USB 1.0

USB 1.0 wurde 1996 von Intel veröffentlicht und diente (wie auch noch heute) zum Anschluss von Peripheriegeräten an den PC. Es eignete sich wegen der langsamen Datenübertragung von 12 MBit/s nicht zum Anschluss von Festplatten.

## USB-Controller

Es existieren folgende Standards für USB-Host-Controller:

- [OHCI](https://github.com/lowlevel-eu/wiki/wiki/Open-Host-Controller-Interface "OHCI")
- [UHCI](https://github.com/lowlevel-eu/wiki/wiki/Universal-Host-Controller-Interface "UHCI")
- [EHCI](https://github.com/lowlevel-eu/wiki/wiki/Enhanced-Host-Controller-Interface "EHCI")
- [xHCI](https://github.com/lowlevel-eu/wiki/wiki/Extensible-Host-Controller-Interface "XHCI")

## Elektrische Hintergründe

![Usb_kabel_beschriftet.jpg](http://upload.wikimedia.org/wikipedia/de/a/a7/Usb_kabel_beschriftet.jpg)

------------------------------------------------------------------------

Aufgeschnittenes USB-Kabel, Einzelkabel beschriftet  
[Quelle](http://de.wikipedia.org/w/index.php?title=Datei:Usb_kabel_beschriftet.jpg&filetimestamp=20080530215106) ![200px-USB.svg.png](http://upload.wikimedia.org/wikipedia/commons/thumb/6/67/USB.svg/200px-USB.svg.png)

------------------------------------------------------------------------

Kontakte von USB-A- und -B-Steckern  
[Quelle](http://de.wikipedia.org/w/index.php?title=Datei:USB.svg&filetimestamp=20090406174048)

Schneidet man ein USB-Kabel wie z. B. ein altes Handykabel auf, so wird man darin vier weitere Kabel entdecken, meist sind sie rot, schwarz, grün und weiß. Diese Farben stehen für die jeweilige Bedeutung:

| Farbe | Name | Bedeutung |
| --------- | ----------------- | -------------------------------- |
| Rot | V<sub>BUS</sub> | Betriebsspannung (5 Volt) |
| Schwarz | Ground | Masse (also 0 Volt) |
| Grün | D+ | Eine der beiden Datenleitungen |
| Weiß | D- | Die andere Datenleitung |

Die Anschlüsse V<sub>BUS</sub> und GND bilden für das USB-Gerät also eine Spannungsquelle, mit D+ und D- werden Daten seriell übertragen. Ist das Potential von D+ höher als das von D-, so liegt auf dem Bus eine differentielle 1 an, ist es umgekehrt, so handelt es sich um eine differentielle 0. Der Unterschied muss dabei jeweils mindestens 200 mV betragen.

Wenn kein Gerät am USB angeschlossen ist, befindet sich auf beiden Datenleitungen die gleiche Spannung, ist sie hoch, bezeichnet man dies als SE1 (Single Ended 1), ist sie niedrig, so wird dies SE0 (Single Ended 0) genannt. Wie wird nun das Anschließen eines Geräts an einem USB-Port erkannt? Logischerweise muss dazu das Gerät dafür sorgen, dass die beiden Leitungen ein unterschiedliches Potential erhalten. Damit erhält der entsprechende Hub auch sofort eine Information zur Geschwindigkeit des Geräts, dies funktioniert so:

- Low-Speed-Geräte müssen die D--Leitung auf 3,3 V hochziehen (mit einem 1,5-kΩ-Widerstand).
- Full-Speed-Geräte hingegen ziehen die D+-Leitung hoch.

High-Speed-Geräte sind nicht in dieser Liste aufgeführt, sie melden sich zunächst als Full-Speed-Geräte (jedes High-Speed-Gerät muss auch im Full-Speed-Modus arbeiten, ob es seine eigentliche Funktion dann auch erfüllen kann, sei dahingestellt).

Diese Einteilung führt natürlich auch zu Unterschieden in der Handhabung von Low- und Full-Speed-Geräten: Wenn der Hub keine Spannung treibt, so stellt sich der Idle-Zustand ein, das heißt, bei Low-Speed-Geräten gibt es eine differentielle 0 (D- \> D+) und bei Full-Speed-Geräten eine differentielle 1 (D+ \> D-). Dieser Zustand wird auch J-State genannt, der jeweils andere ist der K-State. Bei letzterem muss der Hub aktiv eine Spannung durch beide Datenleitungen treiben, um die vom Gerät eingestellte Spannung zu invertieren.

Auf dem USB kann es also vier Zustände geben: SE0 (D+ = D-, beide niedrig), SE1 (D+ = D-, beide hoch), J (Idle-Zustand, bei Low-Speed D- \> D+, bei High-Speed D+ \> D-) und K (Hub treibt aktiv Signal, bei Low-Speed D+ \> D-, bei High-Speed D- \> D+). Dabei werden für die Datenübertragung selbst nur der J- und K-State verwendet, die anderen sind für das Anzeigen besonderer Ereignisse von Bedeutung.

### Datenübertragung

Daten werden, bevor sie über den USB verschickt werden, doppelt verschlüsselt:

Zuerst findet ein sogenanntes Bitstuffing statt. Das heißt, nach sechs aufeinander folgenden Einsen im eingehenden Datenstrom wird automatisch eine Null eingefügt (unabhängig davon, ob das Bit danach wieder eine Eins wäre). Dies mag merkwürdig erscheinen, erklärt sich jedoch aus der zweiten Verschlüsselung, der NRZI-Kodierung.

NRZI (Non Return to Zero Invert) bedeutet, dass nach jeder 0 der Zustand auf der Datenleitung invertiert wird und nach jeder 1 so gelassen wird, wie er ist. Dies dient dazu, dass Geräte allein aus diesem Wechsel der Spannung den USB-Takt verfolgen können. Daraus erklärt sich auch das Bitstuffing: Viele aufeinander folgende Einsen führen zu einem konstanten Zustand der Datenleitungen, dies muss jedoch verhindert werden, eben damit die Geräte nicht aus dem Takt geraten. Dazu wird dann zwangsweise ein Null eingefügt, um einen Zustandswechsel zu erreichen.

Möchte man also z. B. einen Text wie „Lowlevel?“ per USB verschicken, so sähe das folgendermaßen aus:

Zunächst müssen die Zeichen in einen Bitstrom umgewandelt werden. Da wir ASCII verwenden, sehen die Bytes zuerst so aus:

    0x4C 0x6F 0x77 0x6C 0x65 0x76 0x65 0x6C 0x3F

Wir nehmen Little Endian, also wird daraus der Bitstrom:

    001100101111011011101110001101101010011001101110101001100011011011111100

Jetzt zum Bitstuffing. Wir haben nur einmal im Bitstrom sechs aufeinander folgende Einsen und das ist das Fragezeichen (deshalb habe ich es auch im Beispiel benutzt). Obwohl direkt danach sowieso eine Null käme, müssen wir eine weitere einfügen, denn der Empfänger könnte sonst in manchen Fällen (hier wäre es wohl dank der zweiten Null danach eindeutig) nicht eindeutig wissen, ob die 0 von einem Bitstuff herrührt oder einfach so da war. Unsere Daten erfahren also eine klitzekleine Veränderung:

    0011001011110110111011100011011010100110011011101010011000110110111111000

Jetzt noch zum NRZI. Bevor Daten gesendet werden, befindet sich die Leitung im Idle-Zustand (nehmen wir zumindest an), das heißt, wir haben am Anfang ein J. Hier jetzt der Zustand der Leitung, das erste Zeichen kennzeichnet ihn vor dem Senden, das letzte danach (somit haben wir 74 Zeichen für 73 Bits):

    JKJJJKJJKKKKKJJJKKKKJJJJKJKKKJJJKKJJKJJJKJJJKKKKJJKKJKKKJKJJJKKKJJJJJJJKJK

Vielleicht ist es so deutlicher zu erkennen (- ist J, \_ ist K):

    -_---_––_____---____----_-___---__--_---_---____--__-___-_---___-------_-_

Ob J oder K der differentiellen 1 bzw. 0 entspricht, hängt dann von der Geschwindigkeit des Geräts ab.

### Selbstversuch

Um den ganzen Spaß einmal selbst zu testen, bedarf es nicht viel &#150; natürlich gebe ich hier keine Garantie dafür, dass es funktioniert oder dafür, dass nichts kaputt geht, also:

**Warnung**

Ich garantiere weder dafür, dass dieses Experiment funktioniert, noch dafür, dass eure Hardware bzw. die hier verwendeten Bauteile unbeschädigt bleiben &#150; dieser Versuch läuft komplett auf eigene Gefahr!

[<img src="https://raw.githubusercontent.com/wiki/lowlevel-eu/wiki/assets/cd24193787d81969b564.png" width="300" height="370" />](https://raw.githubusercontent.com/wiki/lowlevel-eu/wiki/assets/7de86316739b6e24aef9.png) [](https://raw.githubusercontent.com/wiki/lowlevel-eu/wiki/assets/7de86316739b6e24aef9.png "vergrößern")Fertiger Schaltplan

Nun gut, wer jetzt noch mutig genug ist, um diese Gefahr auf sich zu nehmen, der benötigt:

- Ein altes USB-Kabel, das nicht mehr benötigt wird
- Ein relativ scharfes Messer
- Eine Möglichkeit zum Verbinden von Kabeln (Steckbretter, Löten, der Fantasie sind hier kaum Grenzen gesetzt)
- Einen Widerstand, der zumindest in die Nähe von 1,5 kΩ kommt sowie einen, der mindestens 200 Ω besitzen sollte (aber nicht viel mehr)
- Einen Transistor (könnte auch ohne gehen)
- Eine LED

So teuer sollte das also nicht sein, wenn was kaputt geht, dann ist das wohl die LED. Heutige Hostcontroller besitzen zudem Überspannungsschutz, sodass auch hier nichts schiefgehen sollte.

Der USB-Verkehr ist natürlich viel zu schnell, um ihn tatsächlich beobachten zu können. Aber einige Teile kann man sichtbar machen. So dauert z. B. der Reset eines Geräts mindestens 50 ms, während dieser Zeit wird ein SE0 auf dem Bus getrieben. Dies könnte man also tatsächlich erkennen.

- Zuerst muss das Kabel aufgeschnitten werden. Darin müssten sich die oben genannten vier farbigen Kabel befinden, vermutlich von Metallfäden und anderen Materialien abgeschirmt. Das Kabel muss nun so aufgeschnitten werden, dass die vier Einzelkabel ziemlich unabhängig voneinander beweglich sind.
- Nun muss zuerst der 1,5-kΩ-Widerstand das rote (V<sub>BUS</sub>) und das grüne Kabel (D+) verbinden, um ein Full-Speed-Gerät vorzutäuschen. Man kann natürlich auch das rote und das weiße Kabel (D-) verbinden, dann handelt es sich um ein Low-Speed-Gerät. Zum Testen kann man theoretisch schon den USB-Stecker einstecken und das Betriebssystem sollte ein neues USB-Gerät melden (welches sich aber natürlich als fehlerhaft erweist), unter Linux sollte dies z. B. in der per Alt+F10 zu erreichenden Console zu beobachten sein (oder auch per dmesg \| tail -f).
- Um jetzt tatsächlich etwas zu sehen, brauchen wir noch Transistor und LED. Die Basis des Transistors kommt an D+ (oder D-, je nachdem, wo der Widerstand von V<sub>BUS</sub> endet), der Kollektor nach V<sub>BUS</sub> und der Emitter wird an die LED angeschlossen (möglichst in Durchlassrichtung, am Emitter liegt der Pluspol). Die andere Seite der LED wird dann an den zweiten Widerstand, unseren Vorwiderstand, angeschlossen. Dessen anderes Ende kommt dann an Ground. Bei einem 200-Ω-Widerstand sollten 11,5 bis 17,5 mA erreicht werden, eine normale LED nimmt 20 &#150; aber besser zu wenig als zu viel.

Sobald man jetzt das USB-Kabel einsteckt, sollte die LED leuchten (hoffentlich nicht rauchen und stinken) und nach kurzer Zeit leicht blinken &#150; in diesem Moment treibt der Hub die D+-Leitung (oder D-) auf 0. Bei Datenübertragungen ist dieser Zeitraum allerdings extrem kurz, sodass es sich dabei vermutlich um einen Reset mit SE0 handelt. Zusätzlich könnte man auch einen Lautsprecher statt der LED anschließen, dann sollte sich ein leichtes Summen einstellen. Dies zeigt an, dass Daten gesendet werden (bzw. nicht wirklich Daten, aber schon diese nicht-wirklich-Daten werden so oft gesendet (1 kHz), dass es für ein Summen reicht). Bei jedem Reset sollte der Lautsprecher knacken.

## Spezielle Ereignisse

### Reset

Für den gesamten USB steht praktisch nur eine einzige Datenleitung zur Verfügung. Deshalb muss jedes Gerät eine eindeutige Adresse erhalten, um die für es bestimmten Daten erkennen zu können, diese Adresse liegt im Bereich von 1 bis 127. Allerdings gibt es ein Problem: Wenn ein Gerät neu an den USB angeschlossen wird, müsste es bereits eine eindeutige Adresse haben, damit der Host damit kommunizieren kann. Diese Adresse wäre dem Host aber unbekannt und somit wäre keine Kommunikation möglich. Also hat man eine ganz bestimmte Adresse festgelgt, die USB-Geräte annehmen müssen, wenn sie noch nicht anders konfiguriert werden, und diese Adresse ist 0.

Nun gibt es aber weitere Fälle, in denen eine USB-Adresse nicht bekannt ist. So zum Beispiel, wenn das BIOS die USB-Geräte initialisiert und ihnen dabei schon eine neue Adresse zugewiesen hat. Diese Geräte müssen also irgendwie auf eine bekannte Adresse und vor allem in einen bekannten Zustand zurückgesetzt werden (denn das BIOS kann diese Geräte ja bereits verwendet und dafür konfiguriert haben). Natürlich könnte man den Benutzer anweisen, alle USB-Geräte in diesem Moment abzuziehen und neu anzustecken, doch das wäre wohl ziemlich nervig. Also gibt es dafür eine spezielle USB-Funktion, den Reset.

Das Resetsignal wird ausgeführt, indem beide Datenleitungen auf unter 0,3 V gezogen werden, es wird also ein SE0 auf dem USB getrieben. Sobald dieses Signal beendet wurde, befindet sich das entsprechende Gerät im Defaultzustand, das heißt, es ist nicht konfiguriert, befindet sich nicht im Suspendmodus und antwortet auf die USB-Adresse 0. Bei Hub-Ports muss der SE0-Zustand mindestens 10 ms getrieben werden, an Rootports sind 50 vorgeschrieben. Ein Reset muss von einem USB-Gerät in so gut wie jedem Zustand ausgeführt werden können (ich kenne keine Ausnahme).

Für High-Speed-Geräte hat der Reset noch eine weitere Bedeutung: Das Gerät gibt sich hier als solches zu erkennen und ermittelt, ob der Hub ebenfalls im High-Speed-Modus arbeitet. Dies geschieht folgendermaßen:

- Zuerst erkennt das Gerät den SE0-Zustand und begibt sich in den Full-Speed-Modus (falls es gerade als High-Speed-Gerät operiert).
- Jetzt wird ein sogenannter K-Chirp ausgeführt, das heißt, das Gerät treibt ein High-Speed-Signal in D-. Wenn der Hub dies nicht erkennt, bleibt eine Antwort aus und D+ und D- bleiben auf SE0. Das Gerät bleibt im Full-Speed-Modus und wartet das Ende des Resets ab.
- Befindet sich der Hub auch im High-Speed-Modus, dann treibt er abwechselnd K- und J-Chirps auf dem Bus (J-Chirp: D+ alterniert schnell), jede Sequenz dauert ca. 50 µs. Diese Chirps halten bis 100 &#150; 500 µs vor Ende des Resets an, damit das Gerät nicht in den Suspendmodus wechselt.
- Sobald das USB-Gerät diese abwechselnden Chirps erkennt, muss es den Pull-Up-Widerstand an D+ entfernen und sich in den High-Speed-Modus begeben.

### Suspend

Der Suspendmodus ist ein Energiesparmodus. Ein USB-Gerät muss sich nach 3 ms Idle-Zustand (also J) in diesen Modus begeben. Dort muss es dann nach insgesamt 10 ms angelangt sein. Währenddessen darf es nur eine extrem geringe Menge an Strom verbrauchen (500 µA oder nach besonderer Freigabe 2,5 mA). Außerdem reagiert es nur auf Reset- und Resume-Signale. Letzteres dient dazu, das Gerät aus dem Suspendmodus aufzuwecken. Dies geschieht, indem für 20 ms ein K-Zustand getrieben wird. Danach hat jedes Gerät noch 10 ms Zeit, wieder in den Normalzustand zurückzukehren (allerdings müsste es sofort wieder in den Suspendmodus wechseln, wenn während dieser 10 ms mindestens 3 ms Idle-Zustand auftreten).

#### Remote Wakeup

Einige Geräte, wie z. B. Tastaturen oder Mäuse, können auch eigenmächtig ein Resumesignal treiben (beispielsweise bei Tastendruck oder bei einer Mausbewegung), dies wird Remote Wakeup genannt. In diesem Fall wird das Signal an den Host weitergeleitet, der dann entscheidet, welche Geräte tatsächlich aufgeweckt werden sollen.

## Links

- [Offizielle USB-Spezifikationen](http://www.usb.org/developers/docs/)
- [USB in a nutshell](http://www.beyondlogic.org/usbnutshell/usb1.htm)

## Literatur

- Udo Eberhardt, Hans-Joachim Kelm: *USB 2.0.* Franzis, Poing 2001, [ISBN 3-7723-7965-6](http://books.google.com/books?as_isbn=3772379656)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/7288/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1690/index.html)

<!-- MediaWiki page 1690; revision 7288; parent 7282; 2010-03-06T16:38:16Z -->
