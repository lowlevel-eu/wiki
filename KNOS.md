# KNOS

**Löschhinweis:**

Dieser Artikel wurde zum Löschen vorgeschlagen.

Letzter Eintrag von anderthalb (deutsche Sprache fdS) Jahren, keine Homepage, keine sichtbare Weiterentwicklung. --[DerHartmut](https://lowlevel-eu.github.io/wiki/pages/1865/index.html "Benutzer:Hartmut") 10:43, 11. Feb. 2011 (CET)

| KNOS |  |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------- |
|  |  |
| Entwickler: | Peabrain |
| Akt. Version: | 0.0.01 |
| [Lizenz](https://github.com/lowlevel-eu/wiki/wiki/Lizenzen "Lizenzen"): |  |
| OS-Eigenschaften |  |
| Plattform: | [x86](https://github.com/lowlevel-eu/wiki/wiki/X86 "X86") |
| [Kernelart](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel"): | monolitisch |
| [Sprache](https://lowlevel-eu.github.io/wiki/pages/1648/index.html "Kategorie:Programmiersprache"): | Asm, C |
| API: |  |
| Binärformat: | com |
| [IPC-Methode](https://github.com/lowlevel-eu/wiki/wiki/Interprozesskommunikation "IPC"): | Semaphoren |
| Homepage |  |

  

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

#### Interprozesskommunikation (IPC)

Die IPC basiert auf Semaphoren.

### Zukunft

#### Version 0.0.02

- Prozess dürfen nur Privilegstufe 3 haben. (im Moment haben sie noch Stufe 0)
- Grobe Device-struktur (I/O) einbauen.
- Keyboard und Grafikspeicher müssen als Devices laufen. Das heißt, als Filesystem.
- RAM-Disk

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/9525/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2042/index.html)

<!-- MediaWiki page 2042; revision 9525; parent 5675; 2011-02-11T09:43:42Z -->
