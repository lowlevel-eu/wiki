# Multithreading

Diese Seite ist ein Artikel, welcher **mehr** haben könnte..  

Wenn du mehr darüber weißt oder recherchieren willst, bist **du** aufgerufen, dies zu tun. Wenn du dir in einer Sache nicht sicher bist, dann stell es auf die Diskussionsseite.

Multithreading (=Mehrfädigkeit) bezeichnet die gleichzeitige Ausführung mehrerer Aufgaben innerhalb eines Prozesses. Dabei wird zwischen Software- und Hardwaremultithreading unterschieden.

## Softwaremultithreading

Bei softwareseitigem Multithreading wird jeder Thread in dem Prozesstask als eigener Task ausgeführt, der sich aber von einen normalen Task darinn unterscheidet, dass er sich den Speicher und die zugeteilte Rechenzeit vom Scheduler mit dem Rest des Prozesstaskes teilen muss, dies klingt vieleicht banal, bringt aber dennoch einen Geschwindigkeitsvorteil. Die Umsetzung muss durch eine selbstgeschriebene Bibliothek erfolgen, die mit den Userprogrammen gelinkt wird.

## Hardwaremultithreading

Hardwaremultithreading macht es möglich, auch auf einem Prozessorkern mehrere Prozesse gleichzeitig auszuführen. Dies wird durch das Duplizieren der Allzweckregister, des Stackpointers sowie des Instructionpointers erreicht. Intel nennt diese Technik bei ihren Prozessoren Hyper-Threading und wendet dies z.B. beim recht leistungsschwachen Intel Atom an, der durch Hyper-Threading dem Betriebssystem zwei Prozessorkerne zur Verfügung stellt, wobei der Zweite ein rein virtueller Kern ist.

## Hyper-Threading

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/5773/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2058/index.html)

<!-- MediaWiki page 2058; revision 5773; parent 5763; 2009-08-27T18:25:13Z -->
