# Pipe

Eine Pipe bezeichnet einen gepufferten Datenstrom zwischen zwei [Prozessen](Prozess.md "Prozess"), dieser Strom kann uni- oder bidirektional sein. Oft wird eine Pipe verwendet, um die Standardausgabe eines Prozesses auf die Standardeingabe eines anderen zu lenken. Sie ist somit ein Mittel zur [Interprozesskommunikation](Interprozesskommunikation.md "Interprozesskommunikation").

## Verwendung

Pipes gehören zu den mächtigsten Unix-Werkzeugen, die es gibt. Sie ermöglichen es, die Wirkung zweier an sich einfacher Programme zu kombinieren und so nach dem Baukastenprinzip zu arbeiten, wie es typisch für Unix-artige Betriebssysteme ist. So kann man zum Beispiel mit der folgenden Shelleingabe einer gzippten Datei "patches.gz" nach dem Wort "týndur" durchsuchen und alle Zeilen in einer wiederum gzippten Datei "tyndur-patches.gz" abspeichern:

    zcat patches.gz | grep týndur | gzip > tyndur-patches.gz

Alternativ könnte man auch mit temporären Daten arbeiten:

    zcat patches.gz > tmp
    grep týndur < tmp > tyndur-patches
    gzip tyndur-patches

(Man könnte natürlich auch gunzip auf patches.gz anwenden, aber dann würde patches.gz verschwinden)

Häufig werden Pipes solchen temporären Dateien aber vorgezogen, da sie einerseits kürzer sind und zweitens keine temporären Dateien erzeugen, die später wieder gelöscht werden müssten.

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/11450/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1997/index.html)

<!-- MediaWiki page 1997; revision 11450; parent 9989; 2020-08-02T22:09:09Z -->
