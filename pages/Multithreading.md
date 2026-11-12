# Multithreading

Diese Seite ist ein Artikel, welcher **mehr** haben könnte..  

Wenn du mehr darüber weißt oder recherchieren willst, bist **du** aufgerufen, dies zu tun. Wenn du dir in einer Sache nicht sicher bist, dann stell es auf die Diskussionsseite.

Multithreading (englisch für *Mehrfädigkeit*) bezeichnet die gleichzeitige Ausführung mehrerer Befehlssequenzen. Dabei wird zwischen Software- und Hardwaremultithreading unterschieden.

## Softwaremultithreading

Durch Softwaremultithreading ist es möglich innerhalb eines Prozesses neben dem „Hauptthread“, der z. B. in C die `main()`-Funktion ausführt, weitere Threads, die eine andere Befehlssequenz innerhalb eines Prozesses gleichzeitig zum bzw. unabhängig vom Hauptthread auszuführen, zu erstellen.

Siehe Artikel zu [Threads](Prozess.md#threads "Thread")

## Hardwaremultithreading

Hardwaremultithreading macht es möglich, auch auf einem Prozessorkern mehrere Tasks gleichzeitig auszuführen. Dadurch soll die [Pipeline](Pipeline.md "Pipeline") eines superskalaren Prozessors besser ausgelastet werden. Dazu werden die Register dupliziert, Befehle von allen Tasks gelesen, dekodiert und anschließend in die Pipeline gefüttert. Nach der Ausführung werden die Ergebnisse wieder in die Register des passenden Tasks geschrieben.

Intel nennt diese Technik bei ihren Prozessoren Hyper-Threading und wendet dies z. B. beim recht leistungsschwachen Intel Atom an, der durch Hyper-Threading dem Betriebssystem zwei Prozessorkerne zur Verfügung stellt, wobei der zweite ein rein virtueller Kern ist.

### Hyper-Threading

Hyper-Threading ist die von Intel entwickelte Implementierung von hardwareseitigem Multithreading.

Siehe auch: [Hyperthreading-Artikel von Wikipedia](http://de.wikipedia.org/wiki/Hyperthreading)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/11509/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2058/index.html)

<!-- MediaWiki page 2058; revision 11509; parent 7635; 2020-08-20T13:53:48Z -->
