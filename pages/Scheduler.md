# Scheduler

Der Scheduler hat die Aufgabe einzuteilen, welcher Prozess als nächstes wieviel Zeit auf welcher CPU zugeteilt bekommt. Er ist einer der wichtigsten Bestandteile eines Betriebssystems, weil er maßgeblich für dessen Performance verantworlich ist. Bei der Implementierung des Schedulers sollte man sich also vorher gut überlegen, welche Ansprüche man hat und welcher Scheduling-Algorithmus diesen am besten genügt.

## Allgemeine Kriterien

### Kooperativ oder präemptiv

Bei kooperativen (engl. non-preemptive) Schedulingverfahren geben Prozesse die Kontrolle freiwillig ab. Kooperierened Scheduling-Strategien sind für Dialogbetrieb weniger und für Echtzeit-Betrieb überhaupt nicht geeignet. Ein Benutzer könnte im ersten Fall die Rechnerbenutzung für alle anderen Benutzer unmöglich machen, im zweiten Fall könnte ein ´Langläufer´ andere Prozesse daran hindern, vor ihrer Deadline fertig zu werden – mit allen möglichen Folgen... Diese Gefahr besteht bei präemptiven (engl. preemptive) Verfahren nicht. Hierbei wird das OS ermächtigt, Prozessen den Prozessor wieder wegzunehmen – bei den meisten Strategien findet das auch in periodischen Intervallen statt, zB. über den Timer-[Interrupt](Interrupt.md "Interrupt").

### Fairness und Wartezeiten

Der Scheduling-Algorithmus sollte so angelegt sein, dass jeder Prozess nach einer für ihn akzeptablen Wartezeit CPU-Rechenzeit zugeteilt bekommt. Besonders wichtig ist natürlich, dass jeder Prozess soviel CPU-Zeit bekommt, dass er fertig werden kann und nicht "aushungert".

### CPU Auslastung

Wenn viele Prozesse im System sind, sollte zu keiner Zeit eine CPU "brachliegen", weil zB. ein Prozess auf eine Hardwareeingabe wartet. In dieser Wartezeit könnte besser ein anderer Prozess die CPU nutzen.

### Antwortzeiten

Die Zeit zwischen einer Benutzereingabe und der Reaktion durch einen Prozess ist insbesondere bei interaktiven Systemen durch einen geeigneten Scheduling-Algorithmus möglichst klein zu halten.

## Kooperative Verfahren

### FCFS - First Come First Served

Prozesse werden in der Reihenfolge in der sie erstellt werden abgearbeitet. Erst wenn der erste beendet ist kommt der nächste an die Reihe. Bsp:

    P1, P2, P3, P4 und P5 werden in dieser Reihenfolge gestartet.
    Bedienzeiten: P1=22, P2=2, P3=3, P4=5, P5=8
    Antwortzeiten: R1=22, R2=22+2=24, R3=24+3=27, R4=27+5=32, R5=32+8=40
    durchschnittliche Antwortzeit: 29

Vorteile:

- einfach zu implementieren
- geringer Verwaltungsaufwand
- Fairness, alle Prozesse erreichen der Reihe nach die CPU

Nachteile:

- kurz laufende Prozesse müssen u.U. sehr lange warten, daher für Dialogsysteme nicht geeignet.

### SJF - Smallest Job First

Prozess mit küzester Bedienzeit kommt zuerst. Bsp:

    Bedienzeiten: P1=22, P2=2, P3=3, P4=5, P5=8
    Antwortzeiten: R1=40, R2=2, R3=5, R4=10, R5=18
    durchschnittliche Antwortzeit: 15

Vorteile:

- garantiert minimale durchschnittliche Antwortzeit
- kurz laufende Prozesse werden nicht benachteiligt
- Algorithmus relativ leicht zu implementieren, wenn die Dauer des nächsten CPU burst bekannt ist

Nachteile:

- lang laufene Prozesse müssen evt sehr lange warten
- größerer Verwaltungsaufwand

### Priority scheduling

Reihenfolge nach Priorität der Prozesse. Prioritäten können statisch oder dynamisch vergeben werden.

Vorteile:

- dringende Aufgaben werden am schnellsten erledigt

Nachteile:

- bei statischer Prioritätsvergabe evtl ´Aushungern´ von Prozessen
- Vergabe der Prioritäten nicht einfach

## Präemptive Verfahren

### Round Robin

Alle Prozesse werden gleichberechtigt. Ein Prozess kommt nach dem Anderen an die Reihe. Jeder Prozess wird nach einer festen Zeit gestoppt und der nächste gestartet. Bsp

    Bedienzeiten: P1=22, P2=2, P3=3, P4=5, P5=8
    Zeitscheibe: 3 Zeiteinheiten
    Antwortzeiten: R1=40, R2=5, R3=8, R4=19, R5=27
    durchschnittliche Antwortzeit: 19.8

Vorteile:

- Fairness, jeder Prozess bekommt ´seinen´ Anteil an dem Prozessor
- kurz laufende Prozesse werden nicht benachteiligt
- einfach zu implementieren
- wenig Verwaltungsaufwand

Nachteile:

- langlaufende Prozesse müssen bis zu ihrem Ende lange warten

### Round Robin (mit Prioritäten)

Jeder Prozess bekommt zu Anfang nach Priorität eine gewisse Zeit (Ausführzeit) zugeordnet. Dabei sollte die Zeit gleich oder ein Vielfaches der Scheduler-Frequenz (Die Frequenz in der der Scheduler aufgerufen wird) sein. Die Prozesse werden wie beim "normalen" [Round Robin](#round-robin) nacheinander ausgeführt. Diesmal wird aber zum nächsten Prozess erst gewechselt, wenn beim vorherigen die Ausführzeit abgelaufen ist.

### Scheduling mit "Prioritätswarteschlangen"

Die Prozesse werden in Klassen eingeteilt, bei denen jeder Prozess einem, seiner Klasse entsprechenden Anteil Rechenleistung zugeteilt bekommt. Der höchsten Klasse wird am wenigsten Rechenleistung zugeteilt. Je niedriger die Klasse, desto höher ist der Anteil der Rechenleistung für den Prozess. Ein Prozess steigt einen Rang ab, wenn er vom Scheduler "gestoppt" werden muss. Andernfalls steigt der Prozess einen Rang auf. Hierzu ein Beispiel:

Ein Prozess rechnet. Er bekommt zuerst einen Anteil Rechnerleistung, den er komplett verbraucht. -\> er steigt ab und bekommt 5 Teile der Rechenleistung. Er verbraucht auch diese und steigt wieder ab und bekommt nun 10 Teile Rechenleistung. Er verbraucht diese 10 Teile wieder restlos und steigt weiter ab und bekommt nun 20 Teile Rechenleistung. Von diesen verbraucht er nur 17. Also steigt er wieder auf 10 ab.

Der Vorteil dieses Systems ist, dass jedem Prozess, bei einer entsprechenden Implementierung, individuell der optimale Teil der Rechenleistung zugeteilt wird. Nachteil ist allerdings, dass diese Variante nur in Verbindung mit anderen Varianten zur Optimierung eingesetzt werden kann (zumindest ist der alleinige Einsatz schwierig).

## Multilevel-Scheduling

Beim Multilevel-Scheduling werden verschiedene Scheduling-Verfahren (sowohl präemptive also auch kooperative) gemeinsam genutzt, indem man die Prozesse in verschiedene Klassen einteilt und entsprechend eine Ebene mit einem dazugehörigen Scheduling-Algorithmus zuordnet. Die Ebenen werden dann von der obersten bis zur untersten abgearbeitet.

Beispielswiese kann man wichtige Systemprozesse wie Interrupthandler auf die oberste Ebene legen, die dann nach dem FCFS-Prinzip abgearbeitet wird. Auf der untersten Ebene finden sich schließlich unwichtige Hintergrundprozesse, die einfach nach Round-Robin zugeteilt werden.

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/10990/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1711/index.html)

<!-- MediaWiki page 1711; revision 10990; parent 9851; 2013-02-10T18:53:25Z -->
