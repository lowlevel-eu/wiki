# TriviaOS

TriviaOS ist ein kleines Einmann-Hobby OS. Es wird von [Nooooooooos](https://lowlevel-eu.github.io/wiki/pages/1457/index.html "Benutzer:Nooooooooos") entwickelt.

TriviaOS hat einen Mikrokernel und arbeitet nur mit einer GUI. Allerdings werden da nicht Fenster im Sinne von Windows verwendet. Erstens soll damit die Bedinung einfacher sein und zweitens auch die Programmierung. Zudem ist geplant, dass alle Daten im Internet gespeichert sind. Das hat den Vorteil, dass man sich von überallher mit seinem Account einloggen kann und sofort mit seinen Daten arbeiten kann. So kann man Dateien ganz einfach unter verschiedenen Usern teilen. Auch muss man sich dann vor Datencrashs weniger Sorgen machen. Von der Geschwindigkeit her ist das sicher waghalsig - Jedoch bis das System so weit ist, sind hoffentlich auch die Internet-Verbindungen schnell genug geworden.

Ein weiteres Merkaml ist der ausschließlich in Assembler geschriebene Quellcode. Das bringt dem System sicher einen kleiner oder grösseren Geschwindigkeits- und Speichervorteil.

Programme können in beliebig viele Tasks unterteilt werden. Somit bekommen aufwendige Programme automatisch mehr Rechenzeit und eine Aufteilung in Threads für mehrere Prozessoren wird so auch ganz einfach. TriviaOS wird also mit mehreren Prozessoren umgehen können, aber eine 64-Bit Version ist vorläufig nicht geplant, da ich es wichtiger finde, dass die gesamte Rechenpower genutzt wird, anstatt von etwas mehr Speicher, welchen ich momentan sowieso nicht brauche...

Ich hoffe in der Zeit zwischen Weihnachten und Sport-/Winterferien ein erstes Release vorstellen zu können. Dieses wird in etwa die Folgenden "Features" beinhalten:

- einen vollständigen [Mikrokernel](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel") mit funktionierendem [IPC](https://github.com/lowlevel-eu/wiki/wiki/Interprozesskommunikation "IPC")
- [SMP](https://github.com/lowlevel-eu/wiki/wiki/Symmetrisches-Multiprozessorsystem "SMP")-Unterstützung
- Task und Speicherverwaltung
- I/O-Verwaltung
- Dateisystemtreiber
- Tastaturtreiber
- Vesatreiber
- GUI
- evtl. Maustreiber
- Test-Tool
- Ausführliche Dokumentation der [IPC](https://github.com/lowlevel-eu/wiki/wiki/Interprozesskommunikation "IPC") und der Ansprechung dieser Treibermodule

  
Somit wäre es ab diesem Release möglich Software für TriviaOS zu entwickeln.

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/2139/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1448/index.html)

<!-- MediaWiki page 1448; revision 2139; parent 2138; 2007-10-07T09:52:06Z -->
