# Wiki-Crashkurs

Diese Seite fasst die wichtigsten Formatierungsbefehle, die man in diesem Wiki verwenden kann, zusammen. Dies ist keine Anleitung, wann welche Befehle zu verwenden sind.

Eine umfangreichere Dokumentation bietet die offizielle [MediaWiki-Dokumentation](http://www.mediawiki.org/wiki/Help:Contents/de).

## Text

Um Text hervorzuheben, wird dieser von jeweils zwei oder drei Apostrophen (') vorne und hinten eingeschlossen.

Beispiel: ''kursiv'' und '''fett''' wird zu *kursiv* bzw. **fett**

## Überschriften

Überschriften werden von jeweils zwei oder mehr Gleichheitszeichen (=) vorne und hinten eingeschlossen. Die Überschriften der obersten Ebene, werden von zwei Gleichheitszeichen umschlossen, und niedrigere Ebenen von mehr als zweien.

== Erste Überschriftsebene ==

=== Zweite Überschriftsebene ===

### Inhaltsverzeichnis

Wenn eine bestimmte Anzahl an Überschriften im Artikel vorhanden ist, generiert die MediaWiki-Software automatisch ein Inhaltsverzeichnis. Dieses wird vor der ersten Überschrift (also nach den einleitenden Absätzen) platziert.

## Links

- \[\[Artikelname\]\] - Bsp: "Ein \[\[Interrupt\]\]" wird zu: "[Interrupt](https://github.com/lowlevel-eu/wiki/wiki/Interrupt "Interrupt")"
- \[\[Artikelname\|Text im Artikel\]\] - Bsp: "Eine \[\[Interrupt\|Unterbrechung\]\] macht Spaß" wird zu: "Eine [Unterbrechung](https://github.com/lowlevel-eu/wiki/wiki/Interrupt "Interrupt") macht Spaß"
- \[http://example.com externer Link\] - Bsp: "Das \[http://lowlevel.brainsware.org Lowlevel Wiki\] macht Spaß" wird zu: "Das [Lowlevel Wiki](http://lowlevel.brainsware.org) macht Spaß"
- \[http://example.com\] - Bsp: "Siehe \[http://lowlevel.brainsware.org\]" wird zu: "Siehe [\[1\]](http://lowlevel.brainsware.org)"

## Wikiformatierung unterdrücken

Wenn man zum Beispiel Wikibefehle erklären will, oder einfach eine Kollision mit den Befehlen von Mediawiki hat, kann man das \<nowiki\>-Tag benutzen, um zu verhindern, dass Mediawiki den enthaltenen Text formatiert.

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

### Diskussionsfäden

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

## Signatur

Kommentare in Diskussionsseiten sollten immer durch ein --\~\~\~~ am Ende signiert werden.

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

### In anderen Sprachen

    <code>REM Important
    ECHO Hello Batch</code>

Wird zu `REM Important ECHO Hello Batch` Außerdem bekommt man diese schöne Code-Formatierung, wenn man einfach ein Leerzeichen vor jede Zeile des Codes setzt.

## HTML

Die Verwendung von HTML ist möglichst zu vermeiden, und es sollten ausschließlich die eingebauten MediaWiki-Befehle (auch die, die hier nicht dokumentiert sind) verwendet werden. Man kann auch in der [MediaWiki-Dokumentation](http://meta.wikimedia.org/wiki/Help:Editing) nach Alternativen suchen, oder im [IRC](https://github.com/lowlevel-eu/wiki/wiki/IRC "IRC") nachfragen.

## Siehe auch

- [Designrichtlinien](https://github.com/lowlevel-eu/wiki/wiki/Designrichtlinien "Designrichtlinien")
- [Wikiteam](https://github.com/lowlevel-eu/wiki/wiki/Wikiteam "Wikiteam")

## Weblinks

- [Mediawiki-Benutzerdokumentation](http://www.mediawiki.org/wiki/Help:Contents/de)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/6704/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2049/index.html)

<!-- MediaWiki page 2049; revision 6704; parent 6698; 2010-01-02T15:29:34Z -->
