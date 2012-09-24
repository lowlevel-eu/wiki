# Ring

Diese Seite ist ein Artikel, welcher **mehr** haben könnte..  

Wenn du mehr darüber weißt oder recherchieren willst, bist **du** aufgerufen, dies zu tun. Wenn du dir in einer Sache nicht sicher bist, dann stell es auf die Diskussionsseite.

Ein "Ring" bezeichnet eine Sicherheitsstufe eines Prozesses bzw. seine Privilegien. Am höchsten privilegierte Prozesse befinden sich im Ring 0 (z. B. der Kernel oder Treiber), am niedrigsten privilegierte Prozesse im Ring 3. Ring-0-Prozesse dürfen auf den gesamten Speicherbereich zugreifen und alle Befehle ausführen, die die CPU zur Verfügung stellt. Weniger privilegierte Prozesse müssen auf bestimmte Befehle verzichten (wenn IOPL im [EFLAGS](https://github.com/lowlevel-eu/wiki/wiki/EFLAGS "EFLAGS")-Register nicht gerade größer oder gleich deren Ring ist), wie zum Beispiel lgdt oder sti und können außerdem nur auf Speicherbereiche von Prozessen zugreifen, die weniger privilegiert sind oder auf Speicherbereich, die ihnen selbst gehören.

Die meisten Betriebssysteme benutzen ausschließlich die Ringe 0 und 1. In OS/2 jedoch laufen Grafiktreiber in Ring 2. Einige Virtualisierungslösungen legen außerdem Betriebssystemkerne in Ring 1 ab, und laufen selbst in Ring 0. Deshalb haben Intel und AMD auf einigen Plattformen einen Ring -1 geschaffen.

Das Prinzip der "Ringe" wurde mit dem [Protected Mode](https://github.com/lowlevel-eu/wiki/wiki/Protected-Mode "Protected Mode") eingeführt.

In anderen Architekturen gibt es andere Anzahlen von Ringen. Im Honeywell 6180 gibt es beispielsweise 8, in moderneren Architekturen oftmals nur zwei Ringe.

## Siehe auch

[Protected Mode](https://github.com/lowlevel-eu/wiki/wiki/Protected-Mode "Protected Mode")

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/10874/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1990/index.html)

<!-- MediaWiki page 1990; revision 10874; parent 6081; 2012-09-24T14:20:01Z -->
