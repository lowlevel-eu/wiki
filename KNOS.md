# KNOS

## **KNOS**

KNOS ist ein monolitischer Kernel, der im Moment nur Programme aus dem Speicher laden kann. Es gibt eine Shell und ein Testprogramm.

### Aufbau

Der Kernel hat eine Speicherverwaltung, eine Verwaltung für die GDT und eine Prozessverwaltung. Alle Daten für den Grafikzugriff (Text) und die Abfragen der Tastatur werden über Interrupts gehandelt. Die Grafikdaten werden direkt in den Grafikspeicher geschrieben und die Tastaturdaten in einen Speicher, der abgefragt werden kann.

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/5646/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2042/index.html)

<!-- MediaWiki page 2042; revision 5646; parent 5645; 2009-08-19T09:38:50Z -->
