# TriviaOS

TriviaOS ist ein kleines Einmann-Hobby OS und wird von [Nooooooooos](https://lowlevel-eu.github.io/wiki/pages/1457/index.html "Benutzer:Nooooooooos") entwickelt.

## Konzept und Ideen

TriviaOS hat einen Mikrokernel und arbeitet nur mit einer GUI. Allerdings werden da nicht Fenster im Sinne von Windows verwendet, sondern nur "Felder" welche sich nicht überlappen können. Erstens soll damit die Bedinung einfacher sein und zweitens auch die Programmierung. Zudem ist geplant, dass alle Daten eines Benutzers auch im Internet gespeichert werden. Das hat den Vorteil, dass man sich von überallher mit seinem Account einloggen kann und sofort mit seinen Daten arbeiten kann. So kann man auch Dateien ganz einfach unter verschiedenen Usern teilen. Man muss sich dann auch vor Datencrashs weniger Sorgen machen und sich nicht um Backups kümmern. Von der Geschwindigkeit her ist das sicher waghalsig - Jedoch bis das System so weit ist, sind hoffentlich auch die Internet-Verbindungen schnell genug geworden.

Ein weiteres Merkmal ist der ausschließlich in Assembler geschriebene Quellcode. Das bringt dem System sicher den einen oder anderen Geschwindigkeits- und Speichervorteil.

Programme können in beliebig viele Tasks unterteilt werden. Somit bekommen aufwendige Programme automatisch mehr Rechenzeit und eine Aufteilung in Threads für mehrere Prozessoren wird so ganz einfach. Damit ist auch die Möglichkeit geschaffen für Programme verschiedene Module desselben Zwecks anzubieten. Bestimmte Module könnten dann von mehreren Programmen genutzt werden, was im Idealfall zur Verflechtung aller laufenden Programme führt. TriviaOS wird also mit mehreren Prozessoren umgehen können, aber eine 64-Bit Version ist vorläufig nicht geplant, da ich es wichtiger finde, dass die gesamte Rechenpower genutzt wird, anstatt von etwas mehr virtuellem Speicher der wegen meinem Konzept sowieso nicht benötigt wird. Sollten aber einmal alle System weit mehr Arbeitsspeicher als 4GB haben, kann ich immer noch mit gerigem Aufwand PAE implementieren.

In weiter Ferne ist noch geplant, für das OS eine grafische Programmiersprache bereitzustellen, welche einerseits dazu dient, auf einfache Weise Tools zu programmieren und andererseits helfen kann, bestimmte Systemfunktionen zu automatisieren. Man könnte dann Befehlsfunktionen realisieren wie: Such mir alle E-Mails, welche zum selben Thema wie das von Datei XY, vom Autor dieser Datei XZ geschrieben wurden.

## Releases

Ich hoffe im Frühling ein erstes Release vorstellen zu können. Dieses wird in etwa die folgenden "Features" beinhalten:

- den vollständigen TriviaOS-[Kernel](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel")1.0 mit funktionierendem [IPC](https://github.com/lowlevel-eu/wiki/wiki/Interprozesskommunikation "IPC")
- [SMP](https://github.com/lowlevel-eu/wiki/wiki/Symmetrisches-Multiprozessorsystem "SMP")-Unterstützung für MultiProcessor, MultiCore und MultiThreading über ACPI und MPS Tabellen ---\> vollständig implementiert
- Task und Speicherverwaltung
- [Dateisystemtreiber](https://github.com/lowlevel-eu/wiki/wiki/Dateisystem "Dateisystem")
- Diskettentreiber
- [Tastaturtreiber](https://github.com/lowlevel-eu/wiki/wiki/Tastatur "Tastatur")
- [Vesatreiber](https://github.com/lowlevel-eu/wiki/wiki/Video-Electronics-Standards-Association "Vesa")
- einfache [GUI](https://github.com/lowlevel-eu/wiki/wiki/Graphical-User-Interface "GUI")
- [Maustreiber](https://github.com/lowlevel-eu/wiki/wiki/Maus "Maus")
- Test-Tool
- Dokumentation der [IPC](https://github.com/lowlevel-eu/wiki/wiki/Interprozesskommunikation "IPC") und der Ansprechung der ersten [Treibermodule](https://github.com/lowlevel-eu/wiki/wiki/Treiber "Treiber")

Somit wäre es ab diesem Release möglich Software für TriviaOS zu entwickeln.

  
Frühstens im Sommer wird dann das nächste Release kommen. Mit Sicherheit wird es die folgenden Features beinhalten:

- I/O-Verwaltung mit [APIC](https://github.com/lowlevel-eu/wiki/wiki/Advanced-Programmable-Interrupt-Controller "APIC") und IO-Permission-Map Unterstützung
- Prozessverwaltung
- EFI Unterstützung
- differenziertere Exception Handler
- [GUI](https://github.com/lowlevel-eu/wiki/wiki/Graphical-User-Interface "GUI")
- Fesplattenfähigkeit
- CD Unterstützung

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/2559/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1448/index.html)

<!-- MediaWiki page 1448; revision 2559; parent 2558; 2008-02-08T15:08:56Z -->
