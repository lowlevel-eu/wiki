# TriviaOS

TriviaOS ist ein kleines Einmann-Hobby OS. Es wird von [Nooooooooos](https://lowlevel-eu.github.io/wiki/pages/1457/index.html "Benutzer:Nooooooooos") entwickelt.

TriviaOS hat einen Mikrokernel und arbeitet nur mit einer GUI. Allerdings werden da statt Fenstern Felder verwendet. Erstens soll damit die Bedinung einfacher sein und zweitens natürlich auch die Programmierung. Zudem ist geplant, dass das alle Daten im Internet gespeichert ist. Das hat den Vorteil, dass man sich von überallher einloggen kann und dass man so Dateien ganz einfach unter verschiedenen Usern teilen kann. Auch muss man sich dann wegen Datencrashs weniger Sorgen machen. Von der Geschwindigkeit her ist das sicher waghalsig - Jedoch bis das System so weit ist, sind hoffentlich auch die Internet-Verbindungen schnell genug geworden.

Als weitere Besonderheit ist der ausschliesslich in Assembler geschreibene Quellcode. Das hat einen enormen Geschwindigkeits- und Speichervorteil.

Programme, können in beliebig viele Tasks unterteilt werden. Somit bekommen aufwendige Programme automatisch mehr Rechenzeit und die Aufteilung auf mehrere Prozessoren wird so auch ganz einfach vollzogen. TriviaOS wird also mit mehreren Prozessoren umgehen können, aber eine 64-Bit Version ist vorläufig nicht geplant, da ich den Erfolg und Verbreitung von Mehrkern-Prozessoren inerhalb kürzerer Zeit viel grösser, als der der 64 Prozessoren ansehe.

Ich hoffe in der Zeit zwischen Weihnachten und Sport-/Winterferien ein erstes Release vorzustellen können. Dieses wird in etwa die Folgenden "Features" beinhalten:

- einen vollständigen Mikrokernel
- Tastaturtreiber
- SMP-Unterstützung
- Dateisystemtreiber
- Vesatreiber
- GUI
- Maustreiber
- Ausführliche Dokumentation des IPC und der Ansprechung dieser Treibermodule

  
Somit wäre es ab diesem Moment möglich Software fürs Betriebsystem zu entwickeln.

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/2118/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1448/index.html)

<!-- MediaWiki page 1448; revision 2118; parent 2117; 2007-09-29T10:32:32Z -->
