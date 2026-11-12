# Ring

Diese Seite ist ein Artikel, welcher **mehr** haben könnte..  

Wenn du mehr darüber weißt oder recherchieren willst, bist **du** aufgerufen, dies zu tun. Wenn du dir in einer Sache nicht sicher bist, dann stell es auf die Diskussionsseite.

Ein "Ring" bezeichnet die Sicherheitsstufe eines Prozesses und definiert seine Privilegien, also ob und welche systemkritischen Operationen er durchführen darf.

## Ringe in der x86-Architektur

Am höchsten privilegierte Prozesse befinden sich im Ring 0 (z. B. der Kernel oder Treiber), am niedrigsten privilegierte Prozesse im Ring 3. Ring-0-Prozesse dürfen auf den gesamten Speicherbereich zugreifen und alle Befehle ausführen, die die CPU zur Verfügung stellt. Weniger privilegierte Prozesse müssen auf bestimmte Befehle, wie zum Beispiel *lgdt* oder *sti* verzichten, wenn IOPL im [EFLAGS](EFLAGS.md "EFLAGS")-Register nicht gerade größer oder gleich deren Ring ist. Außerdem können sie nur auf Speicherbereiche von Prozessen zugreifen, die weniger privilegiert sind oder auf Speicherbereiche, die ihnen selbst gehören.

Die meisten Betriebssysteme benutzen ausschließlich die Ringe 0 und 3. In OS/2 jedoch laufen Grafiktreiber in Ring 2. Einige Virtualisierungslösungen legen außerdem Betriebssystemkerne in Ring 1 ab, und laufen selbst in Ring 0. Deshalb haben Intel und AMD auf einigen Plattformen einen Ring -1 geschaffen.

Das Prinzip der "Ringe" wurde mit dem [Protected Mode](Protected-Mode.md "Protected Mode") eingeführt.

## Ringe in anderen Architekturen

In anderen Architekturen gibt es andere Anzahlen von Ringen. Im Honeywell 6180 gibt es beispielsweise 8, in moderneren Architekturen oftmals nur zwei Ringe.

## Aufteilung

Die übliche Aufteilung der Ringe lautet wie folgt: Der [Kernel](Kernel.md "Kernel") läuft im Ring 0, der Rest im Ring 3 (siehe auch [Userspace](Userspace.md "Userspace")). Die beiden anderen Ringe werden kaum noch genutzt, was wohl auch der Grund dafür ist, dass andere Architekturen gar auf sie verzichten und nur zwei Ringe einführen (siehe [oben](Ring.md#ringe-in-anderen-architekturen "Ring")). Lediglich ein Verwendungszweck wird heute noch genutzt: Beim Virtualisieren von Betriebssystemen wird häufig der eigentliche Kernel in den Ring 1 verschoben, um dem Virtualisierungsprogramm zu erlauben, sich selbst als "Aufpasser" in den Ring 0 zu setzen.

## Siehe auch

[Protected Mode](Protected-Mode.md "Protected Mode")

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/10905/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1990/index.html)

<!-- MediaWiki page 1990; revision 10905; parent 10882; 2012-10-16T19:19:10Z -->
