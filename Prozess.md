# Prozess

Diese Seite oder Abschnitt ist zwar komplett, es wird aber folgende Verbesserungen gewünscht:  

*Vor- und Nachteile von Kernel- und Benutzerthreads, konkrete Implementierungsbeispiele*

Hilf Lowlevel, den Artikel zu verbessern.

  
Unter **Prozess** (auch **Task** genannt) versteht man ein sich in der Ausführung befindendes Programm, welches vom Betriebssystem in Form einer Prozessliste verwaltet wird.

Um den Unterschied zwischen Prozess und Programm deutlich zu machen, gibt es hier eine kleine Analogie von Andrew Tanenbaum: Wenn ein Koch (die CPU) einen Kuchen backt, dann benutzt er dazu Zutaten (die Daten) und ein Kochbuch (das Programm). Weder der Koch, noch die Zutaten oder das Kochbuch sind der Prozess des Kuchenbackens, alle sind nur Teil dieses abstrakten Vorgangs. <sup>\[[1](https://github.com/lowlevel-eu/wiki/wiki/Prozess#quellen "Prozess")\]</sup>

## Threads

Normalerweise wird in einem Prozess der Programmcode sequenziell abgearbeitet. Oftmals ist es aber erwünscht, dass in einem Prozess gewisse Abläufe parallel ablaufen, zum Beispiel, um zwei CPU-Kerne auslasten zu können, oder einfach um ein GUI ansprechbar zu halten, während eine große Berechnung im Hintergrund läuft.

Ein Prozess kann dazu einen Kindprozess erzeugen, und diesem eine Aufgabe übergeben. Dieses Vorgehen ist zwar völlig legitim und würde funktionieren, hat jedoch zwei große Nachteile. Erstens gibt es bei einem Task Switch einen relativ großen Overhead, also wäre der Wechsel zwischen den Prozessen zu langsam, um damit sorglos umzugehen. Außerdem hängen die Prozesse womöglich relativ nah zusammen, sodass sie oft gemeinsame Daten brauchen. Sie müssten also durch verschiedene [Interprozesskommunikationsmethoden](https://github.com/lowlevel-eu/wiki/wiki/Interprozesskommunikation "Interprozesskommunikation") kommunizieren, was ebenfalls langsam sein kann.

Als Lösung wurde das Prinzip des Threads (engl. für (Ausführungs-) Faden) entwickelt und in den Prozessbegriff integiert. Jeder Prozess hat mindestens einen Thread, der jeweils seinen eigenen Stack und Instruction Pointer hat. Jedoch teilen die Threads eines Prozesses sich die Daten, und können gleichberechtigt darauf zugreifen.

Für die Implementierung von Threads existieren im Großen und Ganzen zwei Prinzipien: Kernelthreads und Benutzerthreads. Außerdem können beide Verfahren noch kombiniert werden, sodass es noch die Möglichkeit eines hybriden Systems gibt.

Ein Kernelthread ist dem Betriebssystem genauso bekannt wie ein Prozess, vielleicht bekommen sie sogar eine PID. Der Scheduler kann sie verwalten und Threads ihre Rechenzeit entziehen. [Linux](https://github.com/lowlevel-eu/wiki/wiki/Linux "Linux") nutzt dieses Prinzip. Aufgrund ihrer Ähnlichkeit zu normalen Prozessen heißen sie dort auch *light-weight processes* (leichtgewichtige Prozesse, kurz: LWP).

Die Voraussetzungen für Benutzerthreads sind in den Programmen selbst enthalten (was nicht bedeutet, dass der Programmierer sie selbst implementieren muss, er kann einfach gegen eine Bibliothek linken). Ein solcher Prozess bekommt seine Rechenzeit zugeteilt, als hätte er gar keine Threads (denn der Scheduler weiß nichts von ihnen), und das Programm teilt diese unter ihren Threads auf. Es ist jedoch absolut notwendig, dass die Threads kooperieren, denn wenn ein Thread rechnet, dann rechnet er, und das Threadsystem kann nicht selbstständig die Kontrolle erhalten, wie es der Kernel durch [Interrupts](https://github.com/lowlevel-eu/wiki/wiki/Interrupt "Interrupt") tun würde.

## Siehe auch

- [Scheduler](https://github.com/lowlevel-eu/wiki/wiki/Scheduler "Scheduler")

## Quellen

1.  Andrew S. Tanenbaum, "Moderne Betriebssysteme", 2. überarbeitete Auflage, Pearson Studium 2003, S. 88f.

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/10826/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1993/index.html)

<!-- MediaWiki page 1993; revision 10826; parent 10825; 2012-09-15T10:22:15Z -->
