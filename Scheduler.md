# Scheduler

Der Scheduler hat die Aufgabe festzustellen welcher Prozess als nächstes CPU-Zeit zugeteilt bekommt. Dabei gibt es mehr oder weniger komplizierte Systeme. Das einfachste System ist [Round Robin](#round-robin). Dabei bekommt ein Prozess nach dem anderen CPU-Zeit zugeteilt. Man kann aber auch Prioritäten setzen und damit Prozesse, die wichtiger sind mehr CPU-Zeit zuteilen.

## Round Robin

Alle Prozesse werden gleichberechtigt. Ein Prozess kommt nach dem Anderen an die Reihe. Jeder Prozess wird nach einer festen Zeit gestoppt und der nächste gestartet.

## Round Robin (mit Prioritäten)

Jeder Prozess bekommt zu Anfang nach Priorität eine gewisse Zeit (Ausführzeit) zugeordnet. Dabei sollte die Zeit gleich oder ein Vielfaches der Scheduler-Frequenz (Die Frequenz in der der Scheduler aufgerufen wird) sein. Die Prozesse werden wie beim "normalen" [Round Robin](#round-robin) nacheinander ausgeführt. Diesmal wird aber zum nächsten Prozess erst gewechselt, wenn beim vorherigen die Ausführzeit abgelaufen ist.

## Kürzester als Nächstes

Bei diesem Scheduling-System wird probiert die voraussichtliche absolute Ausführzeit eines Prozesses zu ermitteln und danach bestimmt, welche Priorität dieser Prozess hat. Kurze Prozesse bekommen dabei eine höhere Priorität, da sie damit schnell fertig sind und die CPU somit schneller wieder entlasten. Nachteil: Lange Prozesse dauern noch länger als üblich.

## Schudeling mit "Prioritätswarteschlangen"

Die Prozesse werden in Klassen eingeteilt, bei denen jeder Prozess einem, seiner Klasse entsprechenden Anteil Rechenleistung zugeteilt bekommt. Der höchsten Klasse wird am wenigsten Rechenleistung zugeteilt. Je niedriger die Klasse, desto höher ist der Anteil der Rechenleistung für den Prozess. Ein Prozess steigt einen Rang ab, wenn er vom Scheduler "gestoppt" werden muss. Andernfalls steigt der Prozess einen Rang auf. Hierzu ein Beispiel:

Ein Prozess rechnet. Er bekommt zuerst einen Anteil Rechnerleistung, den er komplett verbraucht. -\> er steigt ab und bekommt 5 Teile der Rechenleistung. Er verbraucht auch diese und steigt wieder ab und bekommt nun 10 Teile Rechenleistung. Er verbraucht diese 10 Teile wieder restlos und steigt weiter ab und bekommt nun 20 Teile Rechenleistung. Von diesen verbraucht er nur 17. Also steigt er wieder auf 10 ab.

Der Vorteil dieses Systems ist, dass jedem Prozess, bei einer entsprechenden Implementierung, individuell der optimale Teil der Rechenleistung zugeteilt wird. Nachteil ist allerdings, dass diese Variante nur in Verbindung mit anderen Varianten zur Optimierung eingesetzt werden kann (zumindest ist der alleinige Einsatz schwierig).

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/4526/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1711/index.html)

<!-- MediaWiki page 1711; revision 4526; parent 4211; 2009-07-01T19:11:02Z -->
