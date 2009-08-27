# Multithreading

Diese Seite oder Abschnitt ist zwar komplett, es wird aber folgende Verbesserungen gewünscht:  

*Dieser Artikel wird noch von mir erweitert, kann aber auch von anderen überarbeitet werden!*

Hilf Lowlevel, den Artikel zu verbessern.

Multithreading (=Mehrfädigkeit) bezeichnet die gleichzeitige Ausführung mehrerer Aufgaben innerhalb eines Prozesses. Dabei wird zwischen Software- und Hardwaremultithreading unterschieden. Da aber Softwaremultithreading für uns OS-Dever nicht von Belang ist, gehe ich hier nicht weiter darauf ein.

## Hardwaremultithreading

Hardwaremultithreading macht es möglich auch auf einem Prozessorkern mehrere Prozesse gleichzeitig auszuführen. Dies wird durch das Duplizieren der Allzweckregister, des Stackpointers sowie des Instruction Pointer erreicht. Intel nennt diese Technik bei ihren Prozessoren Hyper-Threading und wendet dies z. B. beim recht leistungsschwachen Intel Atom an, der durch Hyper-Threading dem Betriebssystem zwei Prozessorkerne zur Verfügung stellt, wobei der zweite ein rein virtueller Kern ist.

## Hyper-Threading

## Anwendung

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/5754/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2058/index.html)

<!-- MediaWiki page 2058; revision 5754; parent 5753; 2009-08-27T15:43:06Z -->
