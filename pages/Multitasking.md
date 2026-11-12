# Multitasking

Unter Multitasking versteht man die (subjektive) parallele Ausführung mehrerer Programme/Prozesse. Subjektiv deswegen, weil (zumindest bei einem Single-Prozessor-System) zwischen den verschiedenen Programmen/Prozessen hin- und hergeschaltet wird (die Zeit, die jeder Prozess zwischen dem Hin- und Herschalten bekommt bestimmt der [Scheduler](Scheduler "Scheduler")).

  

## Prinzip

Beim Multitasking können mehrere Prozesse gestartet werden, d.h. sie werden ins RAM geladen. Nun werden die Prozesse nicht gleichzeitig ausgeführt (zumindest nicht auf Single-Core-Systemen), sondern es wird immer ein Prozess bearbeitet und dann zum Nächsten gewechselt. Um nun zu bestimmen, welcher Prozess als nächstes dran ist und wie viel Zeit er von der CPU bekommt, tritt der [Scheduler](Scheduler "Scheduler") in Aktion. Dieser implementiert einen oder mehrere Algorithmen, die ausrechnen, welcher Prozess wann dran ist. Der einfachste Algorithmus ist "Round Robin". Es wird einfach eine Liste geführt, in der jeder Prozess angeführt ist. Ausgewählt wird dann immer der nächste Task in der Liste. Eine Idee ist es auch, mit Prioritäten zu arbeiten, das heißt, dass verschiedene Prozesse unterschiedlich gewichtet werden. (z.B. mehr Prozessorzeit bekommen, oder öfters aufgerufen werden) Beim Umschalten muss folgendes erledigt werden:

- ALLE Register speichern
- Rücksprungadresse speichern (damit man weiß, wo man das Programm fortführen muss)
- Stack wechseln
- Register des nächsten Prozesses wiederherstellen
- An die Rücksprungadresse des nächsten Prozesses springen.

## Zwei Methoden

Dabei wird zwischen zwei Methoden unterschieden:

- [Software-Multitasking](Software-Multitasking-Tutorial "Software Multitasking Tutorial")

und

- [Hardware-Multitasking](Hardware-Multitasking "Hardware-Multitasking")

### Software - Multitasking

Hierbei wird die Umschaltarbeit komplett vom Betriebsystem ausgeführt. Der Prozessor macht dabei nichts.

### Hardware - Multitasking

Im Gegensatz zum Software-Multitasking, wird hier die meiste Arbeit vom Prozessor erledigt.

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/6889/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1495/index.html)

<!-- MediaWiki page 1495; revision 6889; parent 6837; 2010-01-12T10:52:16Z -->
