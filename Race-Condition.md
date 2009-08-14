# Race Condition

Eine Race Condition (auf Deutsch "kritischer Wettlauf", wörtlich "Wettlaufsituation") ist eine Konstellation, in der das Resultat einer Operation vom zeitlichen Verhalten bestimmter Einzeloperationen abhängt. Sie stellen eine sehr schwer auffindbare Fehlerquelle dar, da das erfolgreiche Abschließen der bewussten Operation sozusagen vom Zufall abhängt - mal funktioniert das System, mal nicht.

## Beispiel

Wie könnte eine Race Condition aussehen? Meistens handelt es sich um zwei [Prozesse](https://github.com/lowlevel-eu/wiki/wiki/Prozess "Prozess"), die die gleiche Funktion ausführen. Nehmen wir also eine hypothetische Funktion namens I_want_the_printer_now(), die den Drucker für den aktuellen Prozess reserviert, damit kein anderer Prozess darauf zugreifen kann. Außerdem gibt es eine Funktion, die den Drucker wieder freigibt, release_printer(). Der Code könnte zum Beispiel so aussehen: \<c\>static int printer_reserved = 0;

void I_want_the_printer_now() {

     while (printer_reserved);
     printer_reserved = 1;

}

void release_printer() {

     printer_reserved = 0;

}\</c\>

Wenn ein Prozess drucken möchte, macht er das folgendermaßen: \<c\>I_want_the_printer_now(); //Drucken, drucken, drucken... release_printer()\</c\>

Was passiert nun, wenn zwei Prozesse versuchen, zu drucken? Normalerweise wird zuerst I_want_the_printer_now() ausgeführt, dann unterbricht der Scheduler während des Druckens und der nächste Prozess stellt fest, dass der Drucker belegt ist. Das läuft dann so ab:

| Prozess A | printer_reserved | Prozess B |
| --------------------------- | ------------------ | --------------------------- |
| while (printer_reserved); | 0 | \[wartet\] |
| printer_reserved = 1; | 1 | \[wartet\] |
| \[druckt\] | 1 | \[wartet\] |
| Scheduler unterbricht |  |  |
| \[wartet\] | 1 | while (printer_reserved); |
| \[wartet\] | 1 | while (printer_reserved); |
| Scheduler unterbricht |  |  |
| \[druckt\] | 1 | \[wartet\] |
| printer_reserved = 0; | 0 | \[wartet\] |
| \[beendet\] | 0 | \[wartet\] |
| Scheduler unterbricht |  |  |
| \[beendet\] | 0 | while (printer_reserved); |
| \[beendet\] | 1 | printer_reserved = 1; |
| \[beendet\] | 1 | \[druckt\] |
| \[beendet\] | 1 | \[druckt\] |
| \[beendet\] | 0 | printer_reserved = 0; |
| \[beendet\] | 0 | \[beendet\] |

Aber was passiert, wenn der Scheduler genau nach der while-Schleife unterbricht? Schauen wir es uns an...

| Prozess A | printer_reserved | Prozess B |
| --------------------------- | ------------------ | --------------------------- |
| while (printer_reserved); | 0 | \[wartet\] |
| Scheduler unterbricht |  |  |
| \[wartet\] | 0 | while (printer_reserved); |
| \[wartet\] | 1 | printer_reserved = 1; |
| \[wartet\] | 1 | \[druckt\] |
| Scheduler unterbricht |  |  |
| printer_reserved = 1; | 1 | \[wartet\] |
| \[druckt\] | 1 | \[wartet\] |
| \[druckt\] | 1 | \[wartet\] |
| Scheduler unterbricht |  |  |
| \[wartet\] | 1 | \[druckt\] |
| \[wartet\] | 0 | printer_reserved = 0; |
| \[wartet\] | 0 | \[beendet\] |
| Scheduler unterbricht |  |  |
| printer_reserved = 0; | 0 | \[beendet\] |
| \[beendet\] | 0 | \[beendet\] |

Das Problem ist klar: Prozess A hat die Überprüfung nicht korrekt durchgesetzt und printer_reserved auf eins gesetzt, obwohl es das schon war. Dadurch druckt zuerst Prozess B, dann Prozess A und dann Prozess B. Die Folge ist logischerweise Chaos auf dem fertigen Blatt Papier. Und genau das ist eine Race Condition: Sie hängt davon ab, ob Prozess A mit der Überprüfung von printer_reserved und dem Setzen schnell genug fertig wird, bevor ihn der Scheduler unterbricht - quasi ein Wettlauf, ein "Race", zwischen Scheduler und Prozess.

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/5620/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2013/index.html)

<!-- MediaWiki page 2013; revision 5620; parent 5400; 2009-08-14T08:28:13Z -->
