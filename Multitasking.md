# Multitasking

Multitasking ist die Bezeichnung für das (nahezu) gleichzeitige Abarbeiten von Aufgaben (Tasks). Dies wird realisiert, indem blitzschnell zwischen mehreren Prozessen hin und her geschaltet wird und so jedem Prozess für eine bestimmte Zeit die CPU zur Verfügung gestellt wird.

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

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/2733/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1495/index.html)

<!-- MediaWiki page 1495; revision 2733; parent 2131; 2008-03-22T17:17:04Z -->
