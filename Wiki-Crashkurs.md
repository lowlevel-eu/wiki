# Wiki-Crashkurs

Diese Seite fasst die wichtigsten Formatierungsbefehle, die man in diesem Wiki verwenden kann, zusammen. In erster Linie ist sie dafür gedacht eine schnelle Übersicht über die Gestaltungsmöglichkeiten zu liefern, und ist deswegen in einem relativ knappen Stil gehalten. Eine umfangreichere Dokumentation bietet die offizielle [MediaWiki-Dokumentation](http://www.mediawiki.org/wiki/Help:Contents/de).

## Text

Um Text hervorzuheben, wird dieser von jeweils zwei oder drei Apostrophen (') vorne und hinten eingeschlossen.

Beispiel: ''kursiv'' und '''fett''' wird zu *kursiv* bzw. **fett**

## Überschriften

Überschriften werden von jeweils zwei oder mehr Gleichheitszeichen (=) vorne und hinten eingeschlossen. Die Überschriften der obersten Ebene, werden von zwei Gleichheitszeichen umschlossen, und niedrigere Ebenen von mehr als zweien.

== Erste Überschriftsebene ==

=== Zweite Überschriftsebene ===

Überschriften, die von nur einem Gleichheitszeichen umschlossen sind, existieren zwar auch, werden aber in den Artikeln **nicht** benutzt, da diese eine Überschrift erster Ordnung darstellen und damit semantisch auf der selben Ebene wie die Artikelüberschrift ständen.

Vor einer Überschrift wird genau eine Zeile freigelassen.

### Inhaltsverzeichnis

Wenn eine bestimmte Anzahl an Überschriften im Artikel vorhanden ist, generiert die MediaWiki-Software automatisch ein Inhaltsverzeichnis. Dieses wird vor der ersten Überschrift (also nach den einleitenden Absätzen) platziert.

## Links

- \[\[Artikelname\]\] - Bsp: „Ein \[\[Interrupt\]\]“ wird zu: „Ein [Interrupt](https://github.com/lowlevel-eu/wiki/wiki/Interrupt "Interrupt")“
- \[\[Artikelname\|Text im Artikel\]\] - Bsp: „Eine \[\[Interrupt\|Unterbrechung\]\] macht Spaß“ wird zu: „Eine [Unterbrechung](https://github.com/lowlevel-eu/wiki/wiki/Interrupt "Interrupt") macht Spaß“
- \[http://example.com externer Link\] - Bsp: „Das \[http://www.lowlevel.eu Lowlevel-Wiki\] macht Spaß“ wird zu: „Das Lowlevel-Wiki macht Spaß“
- \[http://example.com\] - Bsp: „Siehe \[http://www.lowlevel.eu\]“ wird zu: „Siehe \[1\]“

## Listen

### Nicht nummeriert

    * punkt x
    * punkt y
    * punkt z

wird zu:

- punkt x
- punkt y
- punkt z

### Nummeriert

    # punkt x
    # punkt y
    # punkt z

wird zu:

1.  punkt x
2.  punkt y
3.  punkt z

### Mehrere Ebenen (kombiniert)

    * foo
    *# unterfoo1
    *#* unterunterfoo
    *# unterfoo2
    * bar

wird zu:

- foo
  1.  unterfoo1
      - unterunterfoo
  2.  unterfoo2
- bar

## Tabellen

Tabellen werden immer durch ein „{\|“ begonnen und mit „\|}“ beendet. Dazwischen definiert man dann die einzelnen Reihen. Die Inhalte einer Reihe werden wiederrum durch „\|-“ voneinander abgegrenzt. Jede Zelle selbst wird auf im Code auf eine eigene Zeile geschrieben, die mit „\|“ beginnen muss, um anzuzeigen, dass nun eine neue Zelle der aktuellen Reihe beginnt. Außerdem kann man eine Überschriftenzelle erzeugen, die aber statt mit „\|“ mit „!“ beginnen muss.

Es empfiehlt sich in der ersten Zeile der Tabelle (nach dem „{\|“) diese mit dem Attribut {{prettytable}} zu versehen, um den [Designrichtlinien](https://github.com/lowlevel-eu/wiki/wiki/Designrichtlinien "Designrichtlinien") treu zu bleiben. Außerdem sieht es einfach besser aus. Mit dem Attribut width='??%' kann man zudem festlegen, über wieviel Prozent der Seite sich die Tabelle erstrecken soll.

**Anzeige**

**Code**

| Auto | Fahrrad |
| ------ | ---------- |
| Boot | Bahn |
| Taxi | Flugzeug |

     
    {| {{prettytable}}
    !Auto
    !Fahrrad
    |-
    |Boot
    |Bahn
    |-
    |Taxi
    |Flugzeug 
    |}

  

## Code

### In bestimmter Sprache

C-Code und Assembler-Code wird in \<c\>- bzw. \<asm\>-Tags gesetzt, um bunten Code zu erhalten.

Bsp:

    <c>int main() {
        int i = 1;
    }</c>

wird zu: \<c\>int main() {

      int i = 1;

}\</c\>

Bsp:

    <asm>mov eax, cr0
    or eax, 1
    mov cr0, eax</asm>

wird zu: \<asm\>mov eax, cr0 or al, 1 mov cr0, eax\</asm\>

Eine Liste aller verfügbaren Sprachen befindet sich bei den Versionsinformationen.

### In anderen Sprachen

    <code>REM Important
    ECHO Hello Batch</code>

Wird zu `REM Important ECHO Hello Batch` Außerdem bekommt man diese schöne Code-Formatierung, wenn man einfach ein Leerzeichen vor jede Zeile des Codes setzt.

## Diskussionsfäden

Diskussionsfäden können mittels Listen ohne Auflistungszeichen relativ übersicht gestaltet werden. Zum Beispiel so:

    : Also ich finde diese Diskussion verdient Antworten. --~~~~
    :: Ich bin eine Antwort. --~~~~
    ::: Ich bin eine mehrzeilige Antwort
    ::: auf die Antwort. --~~~~
    :: Ich bin auch wichtig. --~~~~

Und das sieht so aus

Also ich finde diese Diskussion verdient Antworten. --Autor1 0:00, 1. Jan. 1900 (CEST)

Ich bin eine Antwort. --Autor2 10:10, 1. Jan. 1900 (CEST)

Ich bin eine mehrzeilige Antwort

auf die Antwort. --Autor3 13:37, 1. Jan. 1900 (CEST)

Ich bin auch wichtig. --Autor4 21:42, 1. Jan. 1900 (CEST)

### Signatur

Kommentare in Diskussionsseiten sollten immer durch ein --\~\~\~~ am Ende signiert werden. Die Wiki-Software fügt dann automatisch Uhrzeit/Datum sowie den Nutzernamen ein. Dies erleichtert in Diskussionen den Überblick zu behalten, wer was gesagt hat.

## Wikiformatierung unterdrücken

Wenn man zum Beispiel Wikibefehle erklären will, oder einfach eine Kollision mit den Befehlen von Mediawiki hat, kann man das \<nowiki\>-Tag benutzen, um zu verhindern, dass Mediawiki den enthaltenen Text formatiert.

## HTML

Die Verwendung von HTML ist möglichst zu vermeiden, und es sollten ausschließlich die eingebauten MediaWiki-Befehle (auch die, die hier nicht dokumentiert sind) verwendet werden. Man kann auch in der [MediaWiki-Dokumentation](http://meta.wikimedia.org/wiki/Help:Editing) nach Alternativen suchen, oder im [IRC](https://github.com/lowlevel-eu/wiki/wiki/IRC "IRC") nachfragen.

## Siehe auch

- [Designrichtlinien](https://github.com/lowlevel-eu/wiki/wiki/Designrichtlinien "Designrichtlinien")
- [Wikiteam](https://github.com/lowlevel-eu/wiki/wiki/Wikiteam "Wikiteam")

## Weblinks

- [Mediawiki-Benutzerdokumentation](http://www.mediawiki.org/wiki/Help:Contents/de)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/10513/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2049/index.html)

<!-- MediaWiki page 2049; revision 10513; parent 10512; 2012-03-16T23:23:52Z -->
