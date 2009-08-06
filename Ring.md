# Ring

Diese Seite ist ein Artikel, welcher **mehr** haben könnte..  

Wenn du mehr darüber weißt oder recherchieren willst, bist **du** aufgerufen, dies zu tun. Wenn du dir in einer Sache nicht sicher bist, dann stell es auf die Diskussionsseite.

Ein "Ring" bezeichnet eine Sicherheitsstufe eines Prozesses bzw. seine Privilegien. Am höchsten privilegierte Prozesse befinden sich im Ring 0 (z. B. der Kernel oder Treiber), am niedrigsten privilegierte Prozesse im Ring 3. Ring-0-Prozesse dürfen auf den gesamten Speicherbereich zugreifen und alle Befehle ausführen, die die CPU zur Verfügung stellt. Weniger privilegierte Prozesse müssen auf bestimmte Befehle verzichten (wenn IOPL im [EFLAGS](https://github.com/lowlevel-eu/wiki/wiki/EFLAGS "EFLAGS")-Register nicht gerade größer oder gleich deren Ring ist), wie zum Beispiel lgdt oder sti und können außerdem nur auf Speicherbereiche von Prozessen zugreifen, die weniger privilegiert sind oder auf Speicherbereich, die ihnen selbst gehören.

Das Prinzip der "Ringe" wurde mit dem [Protected Mode](https://github.com/lowlevel-eu/wiki/wiki/Protected-Mode "Protected Mode") eingeführt.

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/5333/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1990/index.html)

<!-- MediaWiki page 1990; revision 5333; parent 5324; 2009-08-06T16:23:44Z -->
