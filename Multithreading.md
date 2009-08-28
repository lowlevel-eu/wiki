# Multithreading

Diese Seite ist ein Artikel, welcher **mehr** haben könnte..  

Wenn du mehr darüber weißt oder recherchieren willst, bist **du** aufgerufen, dies zu tun. Wenn du dir in einer Sache nicht sicher bist, dann stell es auf die Diskussionsseite.

Multithreading (=Mehrfädigkeit) bezeichnet die gleichzeitige Ausführung mehrerer Aufgaben innerhalb eines Prozesses. Dabei wird zwischen Software- und Hardwaremultithreading unterschieden.

## Softwaremultithreading

Durch softwareseitiges Multithreading ist es möglich neben dem "Hauptthread", der z.B. in C die main() Funktion ausführt, weitere Threads, die eine andere Befehlssequenz innerhalb eines Prozesses gleichzeitig zum bzw. unabhängig vom Hauptthread auszuführen, zu erstellen. Alle Ressourcen (Dateihandles, Speicher, etc.) können von allen Threads benutzt werden, wodurch es zu [Race Conditions](https://github.com/lowlevel-eu/wiki/wiki/Race-Condition "Race Condition") und anderen Problemen (TODO: Wo linken wir hier am besten hin?) kommen kann. Meist wird Softwaremultithreading durch das Betriebssystem durch spezielle Syscalls zum Erstellen und Zerstören von Threads unterstützt. Es ist auch möglich Threads im Userspace zu emulieren.

## Hardwaremultithreading

Hardwaremultithreading macht es möglich, auch auf einem Prozessorkern mehrere Prozesse gleichzeitig auszuführen. Dies wird durch das Duplizieren der Allzweckregister, des Stackpointers sowie des Instructionpointers erreicht. Intel nennt diese Technik bei ihren Prozessoren Hyper-Threading und wendet dies z.B. beim recht leistungsschwachen Intel Atom an, der durch Hyper-Threading dem Betriebssystem zwei Prozessorkerne zur Verfügung stellt, wobei der Zweite ein rein virtueller Kern ist.

## Hyper-Threading

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/5782/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2058/index.html)

<!-- MediaWiki page 2058; revision 5782; parent 5779; 2009-08-28T13:49:26Z -->
