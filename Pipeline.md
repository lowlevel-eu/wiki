# Pipeline

Diese Seite ist ein Artikel, welcher **mehr** haben könnte..  

Wenn du mehr darüber weißt oder recherchieren willst, bist **du** aufgerufen, dies zu tun. Wenn du dir in einer Sache nicht sicher bist, dann stell es auf die Diskussionsseite.

Diese Seite oder Abschnitt ist zwar komplett, es wird aber folgende Verbesserungen gewünscht:  

- nettes Bild von der Pipeline und eine ausführlichere Erklärung der Stufen
- Ressourcenkonflikten und deren Lösungsmöglichkeiten
- andere Arten von Pipelines VLIW, EPIC
- eventuell was zum Microcode von x86-Prozessoren
- eine x86-Pipeline wäre auch schön

Hilf Lowlevel, den Artikel zu verbessern.

  
Eine **Pipeline** ist eine Art "Fließbandmechanismus" moderner Prozessoren, der es ermöglicht, die Abarbeitung eines einzelnen Befehls in verschiedene Phasen zu zerlegen. Jede dieser Phasen wird dann in einer Pipelinestufe bearbeitet. Eine Aufteilung in Phasen/Pipelinestufen sieht bei einem DLX-Prozessor folgendermaßen aus:

IF -\> DE -\> EX -\> MEM -\> WB

|  |  |  |
| ----- | --------------------- | -------------------------------------------------- |
| IF | (Instruction Fetch) | Befehl laden |
| DE | (Decode) | Befehl dekodieren und Register laden |
| EX | (Execute) | Befehl ausführen bzw. Adressrechnung durchführen |
| MEM | (Memory access) | (Lese-/Schreib-)Zugriff auf den Speicher |
| WB | (Write-back) | Zurückschreiben der Register |

In der ersten Phase (IF) wird der Befehl aus dem Cache bzw. dem Arbeitsspeicher geladen. Anschließend wird der Befehl in der DE-Phase dekodiert und die von dem Befehl verwendeten Register geladen. In der EX-Phase wird der Befehl ausgeführt, falls es sich um einen arithmetisch-logischen Befehl handelt oder die Adressberechnung durchgeführt, falls es sich um einen LOAD/STORE-Befehl handelt. In der MEM-Phase wird das adressierte Wort eines LOAD/STORE-Befehls geladen bzw. gespeichert. In der WB-Phase werden veränderte Register zurückgeschrieben. Wie man bereits hier schon sieht eignen sich [RISC](Reduced-Instruction-Set-Computing "RISC")-Prozessoren sehr viel besser zum Pipelining, da die Befehle relativ einfach sind und deshalb sehr viel leichter in einheitliche Phasen unterteilt werden können. Beispielsweise wäre es nicht möglich einen Befehl mit indirekter Adressierung in das DLX-Pipelineschema zu zwingen, da es nicht möglich ist vor der Ausführung eines arithmetisch-logischen Befehls in irgendeiner Weise auf den Speicher zuzugreifen.

Davon abgesehen zeigt sich, dass man verschiedene Befehle in unterschiedlichen Pipelinestufen parallel bearbeiten kann. Damit erreicht man bei gleicher Taktfrequenz natürlich keinen erhöhten Durchsatz (Anzahl der Befehle die in einem Zeitintervall die Pipeline verlassen), sondern nur eine höhere Latenz (Zeitspanne zwischen dem Eintreten und dem Verlassen eines Befehls in die bzw. aus der Pipeline). Der Vorteil einer Pipeline ist nun, dass man den Prozessor weit höher takten kann als einen ohne Pipeline. Der Grund dafür ist, dass eine Pipelinestufe physisch kleiner ist als der Prozessor ist und ein Signal sehr viel weniger Zeit benötigt um vom Anfang der Pipelinestufe bis zum Ende vorzudringen (im Ggs. zum gesamten Prozessor).

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/8351/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2107/index.html)

<!-- MediaWiki page 2107; revision 8351; parent 8350; 2010-09-23T08:06:50Z -->
