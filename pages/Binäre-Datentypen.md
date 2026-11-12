# Binäre Datentypen

Diese Seite oder Abschnitt ist zwar komplett, es wird aber folgende Verbesserungen gewünscht:  

*Fließkommazahlen beschreiben*

Hilf Lowlevel, den Artikel zu verbessern.

  

## Einführung in Zahlensysteme

Bevor wir uns mit den einzelnen Datentypen beschäftigen ist es notwendig, dass wir generell verstehen wie Dualzahlen (Binärzahlen) aufgebaut sind.

### Dezimalzahlen

Betrachten wir zunächst eine Zahl aus dem Zahlensystem mit dem wir wohl alle aufgewachsen sind: Das Dezimalsystem.

    3458

Man schreibt auch

    3458(10)

um zu verdeutlichen, dass eine Zahl aus dem Dezimalsystem (10er-System) gemeint ist, um Verwechslungen mit anderen Zahlensystemen auszuschließen.

Ebenfalls aus der Schule bekannt sein sollte folgende Schreibweise:

    3458(10) = 3*1000 + 4*100 + 5*10 + 8*1

Nun wir befinden uns im Dezimalsystem und es fällt auf, dass „zufällig“ jeder 2. Faktor der Produkte als eine Potenz von 10 darstellbar ist:

    3458(10) = 3*103 + 4*102 + 5*101 + 8*100

### Dualzahlen

Das Dualsystem funktioniert ganz genauso, nur mit dem Unterschied, dass keine 10er-Potenzen benutzt werden, sondern 2er-Potenzen. Also:

    10101(2) = 1*24 + 0*23 + 1*22 + 0*21 + 1*20 = 16 + 0 + 4 + 0 + 1 = 21(10)

Nebenbei kann man an diesem Beispiel auch gut sehen, wie man Dualzahlen in das Dezimalsystem konvertieren kann.

#### MSB und LSB

Das MSB (**M**ost **S**ignificant **B**it) und das LSB (**L**east **S**ignificant **B**it) sind die Bezeichnungen von zwei besonderen Bits einer Dualzahl.

  
Das **MSB** ist das höchstwertige Bit. D. h. das Bit einer Dualzahl mit der höchsten 2er-Potenz.  
Das **LSB** ist das niedrigwertigste Bit, d. h. immer das Bit mit der Wertigkeit 2<sup>0</sup>.

    110010(2)

## Codierung

### Begriffserklärung

Codierung – jeder hat wahrscheinlich diesen Begriff schonmal gehört. Aber was bedeutet „Codierung“ eigentlich? Schauen wir uns an, was die große Wikipedia dazu sagt:

> Im Allgemeinen ist ein Code eine Vereinbarung über einen Satz (eine Menge) von Symbolen \[…\] zum Zweck des Informationsaustauschs.

Was heißt das nun?

Ich bin mir sicher, dass du dir sicher schonmal (als Kind) darüber Gedanken gemacht hast warum ein Baum „Baum“ heißt und nicht „Stuhl“. Wahrscheinlich hast du von deinen Eltern die Antwort bekommen, dass es eben so sei.

Nun, als du damals gelernt hast zu sprechen, da hast du erstmal eine ganze Weile nur deinen Eltern zugehört. Und aus dem jeweiligen Zusammenhang heraus hast du dir gemerkt, dass ein „Baum“ sowas ist, was meistens draußen rumsteht, einen braunen Stamm hat, mit Ästen und (meistens) grünen Blätteren dran. Du hast also das Wort, bzw. damals wohl eher nur den Laut, den deine Eltern gemacht haben, als sie beispielsweise auf einen Baum gezeigt haben, mit diesem Objekt assoziiert, was da draußen im Garten stand.

Und das war schon eine Codierung. Du hast einem an sich bedeutungslosen Laut, der erzeugt wird, wenn Menschen „Baum“ sagen, eine Bedeutung gegeben.

Man kann also genauso einen eigenen Code erzeugen, den dann jeder verstehen kann, der dessen Bedeutung kennt, mit dem du also eine Bedeutung **vereinbart** (--\> siehe Zitat aus Wikipedia) hast.

Vereinbaren wir also

| Code | Bedeutung |
| ---------- | ----------- |
| „Harry“ | Du |
| „Blumen“ | abwaschen |
| „kauft“ | musst |
| „rote“ | nicht |

Wenn du jetzt also mit jemandem diese Codierung vereinbarst und ihm dann sagst:

    Harry kauft Blumen

Dann weiß diese Person, dass sie abwaschen muss. (==\> Du musst abwaschen)

    Harry kauft rote Blumen

würde dementsprechend bedeuten, dass die angesprochene Person **nicht** abwaschen muss (==\> Du musst nicht abwaschen) Allerdings wird dich wahrscheinlich jeder, der diese Code nicht kennt, nur fragend anschauen.

### Codierung von (Dual)Zahlen

Wie oben schon erklärt bzw. angedeutet sind Dualzahlen so codiert, dass der Wert einer Dualzahl die Summe aller Produkte der i-ten Ziffer (i = 0 – n) mit 2<sup>i</sup>

Hier eine Tabelle mit der Codierung aller 3-Bit Zahlen.

| Code | Wert (Summe) | Wert |
| ------------------- | -------------------------------------------------------- | ------------------ |
| 000<sub>(2)</sub> | 0\*2<sup>2</sup> + 0\*2<sup>1</sup> + 0\*2<sup>0</sup> | 0<sub>(10)</sub> |
| 001<sub>(2)</sub> | 0\*2<sup>2</sup> + 0\*2<sup>1</sup> + 1\*2<sup>0</sup> | 1<sub>(10)</sub> |
| 010<sub>(2)</sub> | 0\*2<sup>2</sup> + 1\*2<sup>1</sup> + 0\*2<sup>0</sup> | 2<sub>(10)</sub> |
| 011<sub>(2)</sub> | 0\*2<sup>2</sup> + 1\*2<sup>1</sup> + 1\*2<sup>0</sup> | 3<sub>(10)</sub> |
| 100<sub>(2)</sub> | 1\*2<sup>2</sup> + 0\*2<sup>1</sup> + 0\*2<sup>0</sup> | 4<sub>(10)</sub> |
| 101<sub>(2)</sub> | 1\*2<sup>2</sup> + 0\*2<sup>1</sup> + 1\*2<sup>0</sup> | 5<sub>(10)</sub> |
| 110<sub>(2)</sub> | 1\*2<sup>2</sup> + 1\*2<sup>1</sup> + 0\*2<sup>0</sup> | 6<sub>(10)</sub> |
| 111<sub>(2)</sub> | 1\*2<sup>2</sup> + 1\*2<sup>1</sup> + 1\*2<sup>0</sup> | 7<sub>(10)</sub> |

Analoges gilt natürlich wie oben beschrieben auch für alle längeren Dualzahlen.

Genauso könnte man aber auch folgendes vereinbaren (d. h. codieren)

| Code | Wert |
| ------------------- | ------------------- |
| 000<sub>(2)</sub> | -3<sub>(10)</sub> |
| 001<sub>(2)</sub> | -2<sub>(10)</sub> |
| 010<sub>(2)</sub> | -1<sub>(10)</sub> |
| 011<sub>(2)</sub> | 0<sub>(10)</sub> |
| 100<sub>(2)</sub> | 1<sub>(10)</sub> |
| 101<sub>(2)</sub> | 2<sub>(10)</sub> |
| 110<sub>(2)</sub> | 3<sub>(10)</sub> |
| 111<sub>(2)</sub> | 4<sub>(10)</sub> |

Wir kommen der Sache schon näher. Wir habe nämlich soeben mit 3 Bit die Zahlen von -3 bis 4 codiert. Ein erster Schritt in die richtige Richtung!

## Natürliche Zahlen

Natürliche Zahlen sind die Zahlen, die wir wohl alle noch aus der Grundschule kennen. Die Menge der natürlichen Zahlen enthält alle positiven Zahlen inklusive der 0. Diese Zahlen lassen sich in binärer Darstellung wunderbar darstellen, denn die Codierung entspricht der „Standard-Codierung“ mit den 2er-Potenzen.

## Ganze Zahlen

### Lineare Codierung

Oben hatte ich bereits eine Codierung vorgestellt, die in 3 Bit die Zahlen -3 bis +4 codiert hat. Dabei wurde eine untere Grenze gewählt (in dem Fall -3) und dann wurde „hochgezählt“ bis wir schließlich dem letzten Code (111<sup>(2)</sup>) den Wert 4 zugeordnet hatten.

Das scheint erstmal ganz gut zu funktionieren. Ist aber dennoch etwas unübersichtlich und die -3 kann mit dieser Methode in einer n-Bit-Codierung schon ganz anders aussehen. Das nächste Problem ist, dass man mit dieser Codierung nicht ohne weiteres rechnen kann.

Nehmen wir aus obiger Tabelle folgende Zahlen und addieren sie:

     010 (=-1)
    +011 (= 0)
    ---------
     101 (= 2)

Offensichtlich scheint das Ergebnis nicht ganz zu stimmen.

### Das Vorzeichenbit

Nunja. Allein aus Gründen der Übersichtlichkeit war unser erster Versuch nicht besonders schön. Eine gute Idee wäre es doch 1 Bit zu reservieren, welches das Vorzeichen angibt.

Also codieren wir unsere ganzen Zahlen nun folgendermaßen:

Das MSB einer n Bit langen Binärkette stellt das **V**orzeichen dar.

| Vorzeichenbit | Bedeutung |
| ----------------- | --------------- |
| 0<sub>(2)</sub> | positive Zahl |
| 1<sub>(2)</sub> | negative Zahl |

Die restlichen n-1 Bits stellen den **B**etrag der Zahl dar. Der Betrag wird wie eine natürliche Zahl codiert.

Also sieht eine (in diesem Fall 4-Bit) Zahl mit dieser Codierung allgemein so aus:

    VBBB

Beispiele:

    1100 = -4
    0011 = +3

Sieht doch gut aus oder? Vorallem recht einprägsam. Allerdings muss ich euch mitteilen, dass auch dies nicht die Lösung ist. Denn schauen wir mal was geschieht wenn wir die beiden Zahlen oben aus dem Beispiel addieren:

     1100 (-4)
    +0011 (+3)
    ---------
     1111 (-7)

Nun, da hätte -1 rauskommen sollen. Also anscheinend auch nicht geeignet für arithmetische Operationen. Andererseits schaut euch mal diese beiden Zahlen an:

    0000 = -0
    1000 = +0

Seltsam, oder? Selbst wenn die Addition erfolgreich gewesen **wäre**, dann wäre diese Phänomen immer noch sehr fragwürdig.

### Das Einerkomplement

Die Sache mit dem Vorzeichenbit hat immer noch ein Problem.

Was machen wir, wenn wir die Zahl der Bits vergrößern wollen?

Wir müssen immer wissen, das MSB nicht zur Zahl selber, sondern zum Vorzeichen gehört.

    Denn:
        1011 ist -3

    Aber:
    00001011 ist 11

    Es müsst aber heißen:
    10000011 ist 11

Das kopieren eines einzelnen Bits ist ziemlich aufwendig. Also probieren wir doch mal folgenes:

  
Wir sagen einfach:

  

| Bedeutung | Darstellung |
| ----------------- | --------------------------------------------------- |
| positive Zahl | einfache Binärzahl wobei das MSB 0 bleiben sollte |
| 1<sub>(2)</sub> | Logisches Komplent des Betrags. |

Also zum Beispiel:

    0100 = +4
    1011 = -4 
    0011 = +3

Dadurch das das logische Komplement des MSB 1 ergeben muss, lässt sich das Vorzeichen dort ablesen.

Die Addition funktioniert doch schon ganz gut:

     1011 (-4)         1001 (-6)
    +0011 (+3)        +0011 (+3)
    ---------         ----------
     1110 (-1)         1100 (-3)

Aber wehe man überschreitet den Nullpunkt (Wir schmeißen den Übertrag raus):

     1100 (-3)         1001 (-6)
    +0101 (+5)        +0111 (+7)
    ---------         ----------
     0001 (+1)         0000 (+0)

Das Problem ist klar. Sobald man versucht, 0 zu überschreiten, wird das Ergebnis um eins kleiner als es sein sollte. Ist ja auch logisch, schließlich liegen zwischen -1 und 1 auch zwei Zahlen, nämlich:

    1111 = -0
    0000 = +0

Wir müssen also versuchen wie wir das Problem gelöst bekommen.

### Das Zweierkomplement

Ich hoffe, ihr habt noch nicht die Hoffnung aufgegeben eine geeignete Codierung für ganze Zahlen zu finden – ich kann euch beruhigen: Dieser Ansatz wird zum Erfolg führen!

Das mit dem Einerkomplement war schon kleine Schlechte Idee. Was ist, wenn wir einfach sagen, das man zu jeder negativen Zahl die fehlenden 1 schon mal nach dem Komplementieren dazu zählen?

Dann haben wir das Zweierkomplement (2k)

Wir müssen also folgendes tun:

- Binärkette negieren
- 1 draufaddieren

  
Praktischerweise ergibt sich bei dieser Codierung, dass das MSB negativer Zahlen 1 und das von positiven Zahlen gleich 0 ist, da ja das Vorzeichen nur bei -0 (1111) zu 0000 gewechselt wird. (0 ist also immer eine Positive Zahl)

#### Beispiel

Angenommen wir haben die 4-Bit-2k-Zahl 5<sub>(10)</sub> = 0101<sub>(2)</sub> Wir wollen diese nun negieren:

1\) Binärkette negieren:

    0101 --> 1010

2\) 1 draufaddieren

     1010
    +0001
    -----
     1011

Ergebnis: 1011<sub>(2)</sub> = -5<sub>(10)</sub>

Durch das selbe Verfahren lässt sich aus der -5 auch wieder die +5 gewinnen!

Wenn wir das ganze zu Fuß machen wollen, gibt es da noch einen Weg:

1.  Alle Bits vom LSB bis zum ersten gesetzten Bit (=1) einschließlich übernehmen.
2.  Alle höherwertigen Bits negieren.

## Fließkommazahlen

*TODO*

## Strings

Strings, zu Deutsch „Zeichenketten“, sind Aneinanderreihungen von ASCII-Zeichen.

### C-Strings

In dieser Variante, die von C genutzt wird, werden die Zeichen einfach hintereinander in einem linearen Speicher abgelegt. Das Ende des Strings wird durch ein Nullzeichen (\0) markiert. Somit ist ein String in C im Grunde ein Char-Array.

Wenn man in C eine Stringkonstante definiert, wird das abschließende Nullzeichen automtisch angehängt. Dennoch sollte immer darauf geachtet werden, dass nicht in unerlaubte Speicherbereiche geschrieben wird, falls ein Programm dieses Nullzeichen weglässt.

„LowLevel“ in C:

     Index:   0-1-2-3-4-5-6-7-8
     Inhalt:  L o w L e v e l 0

### Pascal-Strings

In der Pascal-Variante ist ein String ebenfalls ein Char-Array. Allerdings wird die Länge des Strings im nullten Element gespeichert, der eigentliche Text beginnt erst beim ersten Element.

„LowLevel“ in Pascal:

     Index:   0-1-2-3-4-5-6-7-8
     Inhalt:  8 L o w L e v e l

## Weiterführende Artikel

- [Der Signifant](Signifant.md "Signifant")

## Links

- [Wikipedia: Gleitkommazahl](http://de.wikipedia.org/wiki/Gleitkommazahl)
- [Wikipedia: Zweierkomplement](http://de.wikipedia.org/wiki/Zweierkomplement)
- [Wikipedia: Code](http://de.wikipedia.org/wiki/Code)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/10258/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2043/index.html)

<!-- MediaWiki page 2043; revision 10258; parent 10257; 2011-11-20T18:35:07Z -->
