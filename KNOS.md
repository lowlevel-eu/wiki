# KNOS

## **KNOS**

KNOS ist ein monolitischer Kernel, der im Moment nur Programme aus dem Speicher laden kann. Es gibt eine Shell und ein Testprogramm.

### Aufbau

#### Allgemein

Der Kernel hat eine Speicherverwaltung, eine Verwaltung für die GDT und eine Prozessverwaltung. Alle Daten für den Grafikzugriff (Text) und die Abfragen der Tastatur werden über Interrupts gehandelt. Die Grafikdaten werden direkt in den Grafikspeicher geschrieben und die Tastaturdaten in einen Speicher, der abgefragt werden kann.

#### Speicherverwaltung

Die Speicherverwaltung basiert auf dem Hardwarepaging des IA32.

#### Prozessverwaltung

Die Prozesse werden automatisch in den Speicher kopiert, welcher für diesen Prozess von der Speicherverwaltung zur Verfügung gestellt wird. Gleichzeitig wird die GDT aktualisiert. Bei der Prozessbeendigung wird der Speicher wieder frei gegeben und der GDT-Eintrag gelöscht.

#### Multitasking

Das Multitasking basiert auf der Hardware des IA32. Für jeden Prozess wird ein TSS-Eintrag in der GDT gebraucht. der Stack wird an den Speicher des Prozesses angehangen.

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/5648/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2042/index.html)

<!-- MediaWiki page 2042; revision 5648; parent 5647; 2009-08-19T09:45:46Z -->
