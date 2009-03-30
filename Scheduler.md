# Scheduler

Der Scheduler hat die Aufgabe festzustellen welcher Prozess als nächstes CPU-Zeit zugeteilt bekommt. Dabei gibt es mehr oder weniger komplizierte Systeme. Das einfachste System ist [Round Robin](#round-robin). Dabei bekommt ein Prozess nach dem anderen CPU-Zeit zugeteilt. Man kann aber auch Prioritäten setzen und damit Prozesse, die wichtiger sind mehr CPU-Zeit zuteilen.

## Round Robin

Alle Prozesse werden gleichberechtigt. Ein Prozess kommt nach dem Anderen an die Reihe. Jeder Prozess wird nach einer festen Zeit gestoppt und der nächste gestartet.

## Round Robin (mit Prioritäten)

Jeder Prozess bekommt zu Anfang nach Priorität eine gewisse Zeit (Ausführzeit) zugeordnet. Dabei sollte die Zeit gleich oder ein Vielfaches der Scheduler-Frequenz (Die Frequenz in der der Scheduler aufgerufen wird) sein. Die Prozesse werden wie beim "normalen" [Round Robin](#round-robin) nacheinander ausgeführt. Diesmal wird aber zum nächsten Prozess erst gewechselt, wenn beim vorherigen die Ausführzeit abgelaufen ist.

## Kürzester als Nächstes

Bei diesem Scheduling-System wird probiert die voraussichtliche absolute Ausführzeit eines Prozesses zu ermitteln und danach bestimmt, welche Priorität dieser Prozess hat. Kurze Prozesse bekommen dabei eine höhere Priorität, da sie damit schnell fertig sind und die CPU somit schneller wieder entlasten. Nachteil: Lange Prozesse dauern noch länger als üblich.

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/4211/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1711/index.html)

<!-- MediaWiki page 1711; revision 4211; parent 3177; 2009-03-30T08:51:37Z -->
