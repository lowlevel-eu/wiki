# TriviaOS

**Löschhinweis:**

Dieser Artikel wurde zum Löschen vorgeschlagen.

Recht interessantes Projekt, aber keine Homepage, letzter Page-Edit aus 2008, keine Download-Möglichkeit, wird wohl nicht mehr weiterentwickelt --[DerHartmut](https://lowlevel-eu.github.io/wiki/pages/1865/index.html "Benutzer:Hartmut") 11:52, 30. Aug. 2011 (CEST)

| TriviaOS |  |
| ----------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
|  |  |
| Entwickler: | [Nooooooooos](https://lowlevel-eu.github.io/wiki/pages/1457/index.html "Benutzer:Nooooooooos") |
| Akt. Version: | momentan keine |
| [Lizenz](Lizenzen "Lizenzen"): | momentan keine |
| OS-Eigenschaften |  |
| Plattform: | [x86](X86 "X86") |
| [Kernelart](Kernel "Kernel"): | Microkernel |
| [Sprache](https://lowlevel-eu.github.io/wiki/pages/1648/index.html "Kategorie:Programmiersprache"): | Assembler |
| API: | Zugriff auf laufenden Module |
| Binärformat: | eigenes |
| [IPC-Methode](Interprozesskommunikation "IPC"): | Message Passing, Shared Memory |
| Homepage |  |

momentan keine

## Äusseres Erscheinen

TriviaOS arbeitet nur mit einer GUI, die allerdings nicht Fenster im Sinne von Windows verwendet, sondern nur "Felder" welche sich nicht überlappen können, jedoch in ihrer Grösse sehr flexibel sind. Das wird nicht nur die Bedienung sondern vor allem, auch die Programmierung einfach halten.

Auch ist geplant, dass alle Daten eines Benutzers zusätzlich zur Festplatte auch im Internet gespeichert werden. Das hat den Vorteil, dass man sich von überallher mit seinem Account einloggen kann und sofort mit seinen Daten arbeiten kann. So kann man auch Dateien ganz einfach unter verschiedenen Usern teilen. Man muss sich dann auch vor Datencrashs weniger Sorgen machen und sich nicht um Backups kümmern. Von der Geschwindigkeit her ist das sicher waghalsig - Jedoch bis das System so weit ist, sind hoffentlich auch die Internet-Verbindungen schnell genug geworden.

In weiter Ferne ist noch geplant, für das OS eine grafische Programmiersprache bereitzustellen, welche einerseits dazu dient, auf einfache Weise Tools zu programmieren und andererseits helfen kann, bestimmte Systemfunktionen zu automatisieren. Man könnte dann Befehlsfunktionen realisieren wie: Such mir alle E-Mails, welche zum selben Thema wie das von Datei XY, vom Autor dieser Datei XZ geschrieben wurden.

## Inneres Design

Der Mikrokernel von TriviaOS ist sehr klein und beinhaltet nur die Funktionen fürs Message Passing, den Scheduler und die Weiterleitung von Hardware Interrupts an die entsprechenden Module.

Der Quellcode von TriviaOS ist ausschließlich in Assembler geschrieben. Das bringt dem System sicher den einen oder anderen Geschwindigkeits- und Speichervorteil und gleicht den Performance-Verlust durch das schon extreme Microkernel-Design etwas aus.

Die Tasks in meinem System sind Module eines Programms, die in einem herkömmlichen Programm einer Funktion entsprechen. Sie werden höchstens 8 KB Platz für Code und 4 MB für Daten haben. Sie kommunizieren untereinander in erster Linie über Message Passing. Dabei arbeitet ein Task jeweils eine Nachricht die er gekriegt hat ab und kann weiteren Tasks synchron oder asynchron Nachrichten mit begrenzter Parameteranzahl schicken. Für grössere Datenmengen können die Tasks Shared Memory benutzen. Da Programme in beliebig viele Tasks unterteilt werden können, bekommen aufwendige Programme automatisch mehr Rechenzeit und eine Aufteilung in Threads für mehrere Prozessoren wird so ganz einfach. Damit ist zudem auch die Möglichkeit geschaffen, dass alle Programme für die selbe Funktion das selbe Modul benutzen. Dadurch könnten Programme nicht nur einfacher gewartet werden sondern auch die Entwicklung wird erleichtert und speziell für OpenSource-Entwickler interessant.

TriviaOS wird mit mehreren CPUs, Cores und logischen Prozessoren umgehen können, aber eine 64-Bit Version ist vorläufig nicht geplant, da schon jetzt wegen dem Konzept der extrem kleinen Module nur ein Bruchteil des möglichen virtuellen Speichers genutzt wird. Sollten aber einmal alle Systeme weit mehr als 4GB RAM haben und mein OS diese Ressorcen auch benötigen, kann ich immer noch mit relativ gerigem Aufwand PAE implementieren (oder einen Hairy-Porter erschaffen...).

## Lizenzierung

Die Sourcen des Kernels und der inneren Module meines Systemes werden sobald sie fertiggestellt sind veröffentlicht und jeder darf sie gerne lesen und sich davon inspirieren lassen. Allerings werde ich alle Rechte bei mir behalten, also darf niemand die Sorucen kopieren, oder verändern ohne Absprache mit mir. Die äusseren Module (Tastaturbelegungen, Speicherdevices, Dateisysteme, Druckertreiber, Grafikkartentreiber, Treiber für Geräte wie Webcams...) des Systemes sowie Module von eigenen Programmen für mein OS, werde ich unter die GPL stellen, damit daran alle weiter arbeiten können oder auf diesen Modulen aufbauen können.

## Releases

Ich hoffe demnächst ein erstes Release vorstellen zu können. Dieses wird in etwa die folgenden "Features" beinhalten:

- den vollständigen TriviaOS-[Kernel](Kernel "Kernel")1.0 mit funktionierendem [IPC](Interprozesskommunikation "IPC")
- [SMP](Symmetrisches-Multiprozessorsystem "SMP")-Unterstützung für MultiProcessor, MultiCore und MultiThreading über ACPI und MPS Tabellen ---\> vollständig implementiert
- Task und Speicherverwaltung
- [Dateisystemtreiber](Dateisystem "Dateisystem")
- Diskettentreiber
- [Tastaturtreiber](Tastatur "Tastatur")
- [Vesatreiber](Video-Electronics-Standards-Association "Vesa")
- einfache [GUI](Graphical-User-Interface "GUI")
- [Maustreiber](Maus "Maus")
- Test-Tool
- Dokumentation der [IPC](Interprozesskommunikation "IPC") und der Ansprechung der ersten [Treibermodule](Treiber "Treiber")

Somit wäre es ab diesem Release möglich Software für TriviaOS zu entwickeln.

  

Das nächste Release wird in etwa die folgenden Features beinhalten:

- vollständige [GUI](Graphical-User-Interface "GUI") mit allen geplanten Grafik-Elementen
- Fesplattenfähigkeit
- CD Unterstützung
- getrennte OS-Initialisierung durch BIOS- oder EFI-Funktionen
- Prozessverwaltung
- I/O-Verwaltung mit [APIC](Advanced-Programmable-Interrupt-Controller "APIC") und IO-Permission-Map Unterstützung
- differenzierteres Exception Handling

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/10107/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1448/index.html)

<!-- MediaWiki page 1448; revision 10107; parent 5296; 2011-08-30T09:52:13Z -->
