# Designrichtlinien

Natürlich ist jedem gestattet, seinen Artikel zu gestalten, wie er es gern möchte. Dennoch gibt es hier ein paar Richtlinien, die möglichst eingehalten werden sollten, damit möglichst alle Artikel die selbe Basis haben und gleich formatiert sind.

## Mediawikicode

- Artikel zu Kategorien immer mit *Kategorie: Kategoriename* einordnen, nicht mit *Category: Kategoriename*
- C bzw. Assembler-Beispielcode in \<c\>code...\</c\> bzw. \<asm\>code...\</asm\> einfassen. Sieht schöner aus, siehe Beispiel:

\<c\>int main() {

       int Test1;
       int Test2;
       Test2 = 1000;
       Test1 = 500:
       int Ergebnis = Test1 * Test2 ^ 2;

}\</c\>

## Artikelaussehen

- Sinnvoll verlinken, das heißt nur auf Artikel verlinken die zum Thema beitragen/weiterhelfen und in den aktuellen Kontext passen

Beispiel: Im Artikel [Prozess](Prozess.md "Prozess") tauchen die Wörter Kernel, Linux, Windows und Scheduler auf. Sinnvoll ist nun eine Verlinkung auf [Scheduler](Scheduler.md "Scheduler"), da der Scheduler mit Prozessen zu tun hat. Das haben die drei anderen Begriffe auch, aber eine Verlinkung nur auf Scheduler ist im Kontext des "Prozesses" sinnvoller.

- Wo zwei Artikelnamen in ein Wort stecken, gar nichts verlinken. Zum Beispiel C-Kernel, *nicht* mittels \[\[C\]\]-\[\[Kernel\]\] auf C und Kernel verlinken.
- *Siehe auch*-Kapitel für interne und themenverwandte Wikilinks
- *Weblinks*-Kapitel für externe Weblinks
- Taucht ein eventuell per Wikilink zu erläutender Begriff mehrmals im Text auf, so reicht es, diesen **einmal** zu verlinken. Am besten ist hier, das erste Vorkommen des Begriffs auf den entsprechenden Wikiartikel zu verlinken

## Weiterleitungen

- Keine Weiterleitungen von Synonymen erstellen, wenn es überhaupt keine Links auf diese Weiterleitung gibt. In Artikeln kann man auch gleich den richtigen Artikel verlinken, anstatt den Umweg übers Synonym zu nehmen.

## Anrede

In technischen Artikeln sollte die Anrede des Lesers sowie die Erwähnung der eigenen Person nicht benutzt werden: Beispiel:

~~"Ich erkläre euch nun was ein Kernel ist"~~ Im Folgenden wird nun erklärt, was ein Kernel ist

~~Du solltest keine Exceptions ignorieren~~ Man sollte keine Exceptions ignorieren

  
Anders als bei Tutorials: Dort wird durch die persönliche Anrede Lockerheit vermittelt und der Leser kann sich besser in das gelesene "einfühlen".

Das Wiki richtet sich zwar an keine spezielle Altersgruppe, aber dennoch wird bei persönlicher Anrede "Du" verwendet, um die eh schon teilweise trockene Materie nicht auch noch zu versteifen.

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/8074/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1832/index.html)

<!-- MediaWiki page 1832; revision 8074; parent 5794; 2010-08-16T11:22:35Z -->
