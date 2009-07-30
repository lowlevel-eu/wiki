# Multitasking

Unter Multitasking versteht man die (subjektive) parallele Ausführung mehrerer Programme/Prozesse. Subjektiv deswegen, weil (zumindest bei einem Single-Prozessor-System) zwischen den verschiedenen Programmen/Prozessen hin- und hergeschaltet wird (die Zeit, die jeder Prozess zwischen dem Hin- und Herschalten bekommt bestimmt der [Scheduler](https://github.com/lowlevel-eu/wiki/wiki/Scheduler "Scheduler")).

  

## Prinzip

Beim Multitasking wird ein Prozess ausgeführt, und dann nach einer bestimmten Zeit zum nächsten Prozess geschaltet. Dabei gibt es verschieden Sheduling - Algorithmen, also bestimmte Methoden, wie der nächste Task ausgewählt wird. Das einfachste hierbei ist das Round Robin. Es wird einfach eine Liste geführt, in der jeder Task angeführt ist. Ausgewählt wird dann immer der nächste Task in der Liste. Eine Idee ist es auch, mit Prioritäten zu arbeiten, das heißt, dass verschiedene Prozesse unterschiedlich gewichtet werden. (z.B. mehr Prozessorzeit bekommen, oder öfters aufgerufen werden) Beim Umschalten muss folgendes erledigt werden:

- ALLE Register speichern
- Rücksprungadresse speichern (damit man weiß, wo man das Programm fortführen muss)
- Stack wechseln
- Register des nächsten Prozesses wiederherstellen
- An die Rücksprungadresse des nächsten Prozesses springen.

## Zwei Methoden

Dabei wird zwischen zwei Methoden unterschieden:

- Software - Multitasking

und

- Hardware - Multitasking

### Software - Multitasking

Hierbei wird die Umschaltarbeit komplett vom Betriebsystem ausgeführt. Der Prozessor macht dabei nichts.

### Hardware - Multitasking

Im Gegensatz zum Software-Multitasking, wird hier die meiste Arbeit vom Prozessor erledigt.

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/4828/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1495/index.html)

<!-- MediaWiki page 1495; revision 4828; parent 2733; 2009-07-30T01:41:35Z -->
