# Exception

Diese Seite ist ein Artikel, welcher **mehr** haben könnte..  

Wenn du mehr darüber weißt oder recherchieren willst, bist **du** aufgerufen, dies zu tun. Wenn du dir in einer Sache nicht sicher bist, dann stell es auf die Diskussionsseite.

Als Exception (engl. Ausnahme) bezeichnet man einen Fehler, der während des Ausführens eines Programmes auftritt. Es entsteht also eine Ausnahmesituation, in der die Programmausführung nicht wie geplant fortgesetzt werden kann. Das kann passieren, wenn man beispielsweise eine Zahl durch 0 dividieren will.

Auf der x86-Architektur löst eine Exception, die nicht abgefangen wird, zunächst einen Double Fault aus, der selbst wieder eine Exception ist. Wird auch der Double Fault nicht abgefangen, führt dies zum Triple Fault und ein CPU-Reset wird durchgeführt.

## Abfangen von Exceptions

Wird noch editiert.

## Planmäßiger Einsatz von Exceptions

Exceptions können vom Kernel auch dazu benutzt werden, bestimmte Aktionen eines Userspace-Programms abzufangen und darauf zu reagieren. Die Exception stellt in diesem Sinn keinen echten Fehler dar, sondern der Kernel führt nötige Aktionen durch und lässt das Programm anschließend weiterlaufen.

Das typische Beispiel für solche Exceptions ist der Page Fault. Wenn bei aktiviertem [Paging](https://github.com/lowlevel-eu/wiki/wiki/Paging "Paging") eine Speicherseite nicht zugegriffen werden kann, kann das beispielsweise daran liegen, dass diese Seite auf die Festplatte ausgelagert worden ist. In diesem Fall lädt der Kernel die Seite wieder in den Speicher und springt zurück in das Programm.

Eine weitere Anwendungsmöglichkeit ist Copy on Write. Es kommt zum Einsatz, wenn ganze Pages kopiert werden - z.B. bei unixoiden Systemen bei fork(), dem Klonen von Prozessen. Dabei werden alle zu kopierenden Seiten zunächst nicht wirklich kopiert, sondern sowohl im alten als auch neuen Prozess als schreibgeschützt markiert. Erst bei Bedarf, also wenn sich die Originalpage und Kopie zum ersten Mal unterscheiden, wird wirklich kopiert: Beim ersten Schreibzugriff auf eine solche Seite wird ein Page Fault abgefangen (der ausgelöst wird, weil der Bereich schreibgeschützt ist) und eine zweite Page für die Kopie alloziert.

## Liste der Exceptions

| Vektor | Bezeichnung |
| ----------- | ----------------------------- |
| 0x00 | \#DE - Divide by Zero |
| 0x01 | \#DB - Debug |
| 0x02 | NMI |
| 0x03 | \#BP - Break Point |
| 0x04 | \#OF - Over Flow |
| 0x05 | \#BR - Bound Range |
| 0x06 | \#UD - Invalid Upcode |
| 0x07 | \#NM - Device Not Available |
| 0x08 | \#DF - Double Fault |
| 0x09 | Coprocessor Segment Overrun |
| 0x0a | \#TS - Invalid TSS |
| 0x0b | \#NP - Segment not Present |
| 0x0c | \#SS - Stack |
| 0x0d | \#GP - General Protection |
| 0x0e | \#PF - Page Fault |
| 0x0f | *Reserviert* |
| 0x10 | \#MF - x87 Floating Point |
| 0x11 | \#AC - Alignment Check |
| 0x12 | \#MC - Machine Check |
| 0x13 | \#XF - SIMD Floating Point |
| 0x14-0x1f | *Reserviert* |

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/4518/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1824/index.html)

<!-- MediaWiki page 1824; revision 4518; parent 4168; 2009-06-29T18:16:33Z -->
