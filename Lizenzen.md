# Lizenzen

Wenn man sein Betriebssystem veröffentlicht, sollte man sich auch Gedanken über die Lizenz machen. Vor allen Dingen, auch dann, wenn man fremden Code benutzt. Hier werden ein paar Open-Source-Lizenzen vorgestellt. Da diese Seite von Nicht-Juristen bearbeitet wurde, kann für Fehlerfreiheit nicht garantiert werden. Jeder, der eine Lizenz für sein Projekt sucht, sollte darum selbst die Lizenztexte lesen und sich ein eigenes Bild machen!

## Open Source Lizenzen

### GNU General Public License

Die Hauptpunkte der GNU General Public License (GPL) sind:

- Das Programm darf für alle Zwecke, ohne Einschränkung genutzt werden, auch für kommerziellen Nutzen.
- Das Programm darf kostenlos, aber auch gegen Geld, weiterverteilt werden. Der Empfänger hat das Recht den Quellcode zu erhalten, ohne zusätzliche Gebühren. Der Empfänger darf das Programm unter genau den gleichen Bedingungen weiterverteilen - gegen Geld, aber auch kostenfrei. Es dürfen keine Lizenzgebühren verlangt werden. Niemand ist verpflichtet, das Programm weiterzuverteilen.
- Der Quellcode darf eingeschaut und modifiziert werden.
- Das Programm darf auch abgeändert und weiterverteilt werden, aber nur unter den Bedingungen der General Public License.
- Der Quellcode darf nur mit Code unter GPL-kompatiblen freien Lizenzen kombiniert werden.

#### GPL Linking Exception

Manche Libraries (z.B. libgcc) besitzen in ihrer Lizenz einen Zusatz, der das Linken der Library mit Programmen, egal, unter welcher Lizenz diese stehen, erlaubt (Auch GPL Runtime Exception genannt).

- [Wikipediaartikel zur GPL](http://de.wikipedia.org/wiki/GNU_General_Public_License)
- [Text der GPL Version 3](http://www.gnu.org/licenses/gpl-3.0.html) (englisch)
- [inoffizielle deutsche Übersetzung der GPL](http://www.gnu.de/gpl-ger.html)
- [Wikipediaartikel zur GPL Linking Exception](http://en.wikipedia.org/wiki/GPL_linking_exception)

### GNU LGPL

Die Lesser General Public License besagt, dass ein Programm genau so verbreitet werden darf wie unter der GPL, mit Ausnahme, dass Programme, welche das LGPL-Programm extern benutzen (z.B in Form einer Bibliothek) unter ihrer eigenen Lizenz veröffentlicht werden dürfen. Wenn aber LGPL-Code in ein Programm eingefügt wird, muss dieses unter der LGPL veröffentlicht werden.

- [Wikipediaartikel zur Lesser General Public License](http://de.wikipedia.org/wiki/GNU_Lesser_General_Public_License)

### BSD-Lizenz

Die BSD-Lizenz erlaubt die freie Benutzung, Veränderung und Weiterverbeitung eines Programms. Sie ähnelt hierin der GPL. Allerdings ist der Entwickler der Software nicht verpflichtet den Quellcode mitzuveröffentlichen. Jedoch muss der ursprüngliche Entwickler genannt werden.

#### Werbe-Klausel

Der dritte Absatz der BSD-Lizenz besagt, dass beim Bewerben eines Programms der Name des ursprünglichen Autors genannt werden muss (Mit dieser Klausel ist die Lizenz nicht mehr GPL-kompatibel!).

- [Wikipediaartikel zur BSD-Lizenz](http://de.wikipedia.org/wiki/BSD-Lizenz)

### Zlib/Libpng-Lizenz

Die zlib-Lizenz ist eine GPL-kompatible, sehr unrestriktive Lizenz, die vor allem folgende Bestimmungen setzt:

- Wenn man den Code weiterverbreitet, darf man nicht behaupten, selber der Autor zu sein. Das Nennen des Autors ist außerdem erwünscht, aber nicht zwingend notwendig.
- Wenn der Quellcode geändert wird, muss dies gekennzeichnet werden, die Lizenz darf nicht vom Sourcecode entfernt werden.
- Darüber hinaus erlaubt die Lizenz explizit jede Nutzungsmöglichkeit, ob kommerziell oder nicht.

<!-- -->

- [Wikipediaartikel der zlib-Lizenz](http://de.wikipedia.org/wiki/ZLib_License)

### X11-Lizenz

Die X11-Lizenz (nach ihrer Herkunft auch MIT-Lizenz genannt) ist eine sehr liberale Lizenz, welche zur GPL kompatibel ist.

Sie erlaubt die Nutzung, Veränderung und Weitergabe des Programms, sowie den Verkauf, und die Integration von Quelltext in Closed-Source-Software. Allerdings müssen der Copyrighthinweis und der Lizenztext in alles Kopien der Software verbleiben. Die MIT-Lizenz eignet sich also für Leute, die eine Lizenz suchen, die viele Freiheiten bietet, aber dennoch nicht auf Namensnennung verzichten wollen.

In ihrer Funktion ähnlich zur X11-Lizenz ist die ISC-Lizenz, welche jedoch kürzer ist.

- [Wikipediaartikel zur MIT-Lizenz](http://de.wikipedia.org/wiki/MIT-Lizenz)
- [Wikipediaartikel zur ISC-Lizenz](http://de.wikipedia.org/wiki/ISC-Lizenz)

### WTFPL und Creative Commons Zero

Diese Lizenzen ermöglichen es, alle Rechte an seinem Werk abzugeben (bis auf die unveräußerlichen Urheberrechte, die von Staat zu Staat unterschiedlich sind). Natürlich sind diese Lizenzen somit auch zu der GPL kompatibel.

WTFPL und Creative Commons Zero sind in etwa funktionsgleich: Man gibt Anderen explizit alle Rechte an der Software, die man auch abgeben kann. Jedoch besteht die Gefahr, dass die WTFPL aufgrund ihres "provokativen" Lizenztextes eventuell Interessenten verunsichern kann, weil sie nicht wissen, ob man die Lizenz ernstnehmen kann. Daher ist die formaler gestaltete CC Zero Lizenz eventuell vorzuziehen.

- [Wikipediaartikel zur WTFPL](http://de.wikipedia.org/wiki/WTFPL)
- [Die Creative Commons Zero License Deed](http://creativecommons.org/publicdomain/zero/1.0/deed.de)

## Geht auch Creative Commons?

Natürlich kannst du deinen Code theoretisch auch unter einer Creative-Commons-Lizenz veröffentlicht, jedoch ist davon in einigen Fällen abzuraten, da diese Lizenzen nicht GPL-kompatibel sind, und damit ein Austausch von Code mit GPL-Programmen in beiden Richtungen unmöglich wird.

Für die non-commercial-Varianten von Creative Commons existiert natürlich keine Free-Software-Ersatzlizenz, da die Open-Source-Definition explizit das Recht auf kommerziellen Vertrieb der Software einräumt. Außerdem ist natürlich ein unter der No-Derivative-Works-Klausel veröffentlichter Code kaum noch als offen zu bezeichnen, sodass es hier auch keine freien Alternativen gibt.

Alternativen zu einigen Creative-Commons-Lizenzen:

- CC-by: Wer wirklich nur will, dass sein Name in Verbindung mit den Source genannt wird, der ist für Software mit der [X11-Lizenz](#) wesentlich besser beraten.
- CC-by-sa: Bei dieser Kombination aus Namensnennung und Copyleft steht man vor dem Problem, dass es keine Lizenz gibt, die diese genau ersetzen würde. Wenn man also eine CC-by-sa-Lizenz wählen will, sollte man vorher genau abwägen, ob man nicht doch lieber die [GPL](#gnu-general-public-license) wählt, wordurch die Software trotz der zusätzlichen Auflagen anderen Programmierern wesentlich eher nützen wird.

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/7943/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1552/index.html)

<!-- MediaWiki page 1552; revision 7943; parent 7923; 2010-07-20T00:37:44Z -->
