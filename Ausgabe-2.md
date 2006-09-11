# Ausgabe 2

## Vorwort

Das ist nun die zweite Ausgabe von Lowlevel. Nach der doch sehr positiven Resonanz von Ausgabe 1 habe ich beschlossen, das Projekt fort zu führen. Und ich hoffe, dass ich es nicht umsonst mache...

Eine Bitte habe ich jedoch: ich habe nicht ewig Zeit, um an Lowlevel zu schreiben. Wenn ihr also Content habt, den ihr mir zu Verfügung stellen könnt - egal was, Hauptsache OS Dev-mäßig - dann schickt es mir! Ich mache mir wirklich extrem viel Mühe, um die Zeitschrift regelmäßig voll zu kriegen, also... ihr könntet mir ein wenig Arbeit abnehmen ;-)

Aber auf jeden Fall danke ich allen, die mich unterstützen und die mir ihre Meinung gemailt haben.

Und ich bitte um Entschuldigung wegen den zahlreichen Verspätungen, denn die deutsche Terrorkom hatte mir irrtümlicherweise das Internet gesperrt.

## News

Sorry, keine News diesmal... leider keine Zeit. Wer Newsredakteur bei Lowlevel werden will, kann mir eine Mail schreiben.

## Leserbriefe

Hallo, ich habe gerade auf www.coder-area.de deine Werbung zu deiner Zeitschrift gelesen und gleich einmal reingeschnuppert. Da ich bisher wenig Ahnung vom Aufbau eines Betriebssystems habe, kommt mir diese Gelegenheit gerade recht, um mein Wissen in dieser Beziehung ein wenig aufzufrischen. Weiter so! \[...\]

Freut mich, dass es dir gefallen hat! Ich werde auf jeden Fall weitermachen!

\[...\] Sehr schönes Magazin. Die erste Ausgabe hat mich sehr begeistert. Leider beherrsche ich noch nicht all zu Viel Grundlagen von Assembler, um ganz durchzusteigen, hast du mir da nicht ein Paar Adressen die sich mit Assembler-Programmierung beschäftigen? \[...\]

Tja... da wäre zum Beispiel Snakebytes berühmtes Assembler-Tutorial: <http://kryptocrew.de/archiv/coding/asm/Asmtut.html>, hier eine Art "Referenz":<http://webster.cs.ucr.edu/> und Andre Müllers Tutorial, von dem wir auch Teile hier abdrucken: <http://andremueller.gmxhome.de/toc.html>

  

## OS-Dev-Tutorial, Teil 2

Bevor man ein Betriebssystem programmiert, sollte man sich überlegen, wie das Ganze aufgebaut werden soll. Die zur Zeit wichtigsten Modelle sind:

      1. Monolithischer Kernel
      2. Microkernel
      3. Exokernel

Jeder dieser Kernels hat seine eigenen Vor- und Nachteile, die ich hier kurz darstellen möchte.

### Der monolithische Kernel

Der monolithische Kernel ist noch die meistgenutzte Architektur. OSes wie z.B. Windows benutzen diese traditionelle Form des Kernels. Der größte Teil des Hardware-Interfaces und der Interrupts sind direkt im Kernel implementiert.

Einen monolithischen Kernel zu schreiben, kann ganz schön schwierig sein, da die einzelnen Module des OSes untereinander kommunizieren müssen, und das ist wegen der fehlenden Hardware-Abstraktion recht schwierig. Im Idealfall bietet jedes Modul eine Art **Interface**, über das andere Module mit ihm kommunizieren können.

Leider ist dies leichter gesagt als getan. Da bei einem monolithischen Kernel meistens alle Module in einem Speicherbereich liegen, kann ein Bug gleich den gesamten Kernel zum Absturz bringen.

Beispiele für monolithische Kernels: **Windows** und **Linux**.

### Der Microkernel

Der Microkernel wurde erfunden, um die Probleme zu lösen, die bei einem monolithischen Kernel auftreten. Ein Microkernel wird, wie der Name schon sagt, möglichst klein gehalten. Er hat nur die Aufgabe der Verwaltung von **Ressourcen**: er bestimmt lediglich, wann ein Programm welche Teile des Systems nutzen darf.Das Nutzen der Ressourcen, also die eigentliche Arbeit übernehmen dann **Treiber** oder **Server**.

Das hat den Vorteil, dass man den Microkernel in Supercomputern genauso wie in kleinsten Geräten, zum Beispiel einem Handy verwenden kann, weil der Kernel selbst nichts von den vorhandenen Ressourcen weiß oder wissen muss.

Da also Kernel und die verschiedenen Treiber/Server getrennt laufen, ist ein Microkernel sehr viel stabiler als ein monolithischer Kernel, weil ein Fehler in einem Modul lediglich das Modul zum Absturz bringt, aber nicht gleich den ganzen Kernel.

Ein Beispiel für einen Microkernel ist **QNX RTOS**, das man als Privatanwender kostenlos downloaden kann. Für kommerzielle Entwickler kostet es, soweit ich weiß, 3000 €.

<http://www.qnx.com>

### Der Exokernel

Der Exokernel ist dem Microkernel in dem Punkt, dass die Hardwareabstraktion vom Kernel getrennt wird, sehr ähnlich. Allerdings wird das Hardwareinterface bei dieser Architektur nicht in Programmen mit Kernelrechten, sondern in einer Art von **DLLs** (oder für Linux-User: **Shared Librarys**) implementiert, die auf der User-Ebene laufen.

Diese Vorgehensweise hat den Vorteil, dass Anwendungsprogrammierer, wenn sie das wünschen, direkt auf die Hardware zugreifen können. Normale Anwendungen, beispielsweise Windowsprogramme, brauchen die Hardwareabstraktion natürlich. Sie können auf die "DLL", das sogenannte **LibOS** zugreifen. LibOSes können z.B. harmonisch nebeneinander ein Windows- und ein Linux-System simulieren, auf denen dann gewöhnliche Programme laufen.

Soweit ich weiß, ist das bisher einzige Exo OS für den PC **"xok/ExOS"**, das man kostenlos herunterladen kann. Das libOS ExOS simuliert ein Unix-System, auf dem Anwendungen wie gcc laufen. <http://www.pdos.lcs.mit.edu/exo/>

### Abschließende Worte

Leute, die sich ernsthaft mit OS Dev beschäftigen, sollten dieses wichtige Kapitel - nämlich das Design des Kernels - auf keinen Fall überspringen. Ich kann aus Erfahrung sagen, dass ein OS umso stabiler, sicherer und schneller läuft, je mehr man sich vor der eigentlichen Implementierung Gedanken über den Kernel macht.

Denn wenn man einfach so drauflos programmiert, kommt man vielleicht am Anfang schnell weiter, doch irgendwann steht man vor einem riesigen Designproblem und man weißt nicht, wo man anpacken soll. Deshalb befolgt meinen Ratschlag und plant eure Software genau aus.

  

## Lowlevel-Grundlagen, Teil 2

Die CPU ist kein Alleskönner. Auf einem IBM-PC gibt es noch andere Einheiten, die unabhängig von der CPU arbeiten. Um an die Daten zu kommen, die diese Geräte an die CPU senden, gibt es zwei Methoden, die ich kurz darstellen möchte.

### Polling

Die CPU stoppt nach bestimmten Zeitabschnitten die Ausführung des Programms (oder des Betriebssystems), und checkt bei jedem Gerät, ob Daten angekommen sind und ob diese verarbeitet werden müssen. Wenn ja, wird eine entsprechende Routine gecallt, die die jeweilige Verarbeitung aufnimmt.

Leider ist diese Methode sehr ineffizient, da sie sehr viel Rechenkapazität in Anspruch nimmt und dadurch die CPU völlig ausbremsen kann. Außerdem besteht die Gefahr, dass Daten verloren gehen, wenn größere Datenmengen von verschiedenen Ports an die CPU gesendet werden.

### Interrupts

Eine sehr viel bessere Methode ist die Methode der Interrupts. Bei diesem Konzept bekommt jedes Gerät, das mit der CPU kommuniziert, eine Art "Signalgeber", mit der es der CPU signalisieren kann, dass Daten gesendet wurden und die CPU nun die Daten verarbeiten muss. Die CPU unterbricht (**interrupts**) nun das Programm und verarbeitet die Daten mit einer Routine, die vorher festgelegt wurde. Wie diese System genau funktioniert, werden wir uns später anschauen.

Diese Methode hat einige Vorteile. Zum Beispiel kann die CPU das Programm, das geladen ist, permanent ausführen, und das Programm wird nur dann unterbrochen, wenn es wirklich sein muss.

So, Schluss jetzt mit dem theoretischen Gelaber. Schauen wir uns an, wie das genau funktioniert und wie das auf dem IBM-PC implementiert ist ;-)

Datei:Ausgabe1/irq2.gif Implementierung auf dem IBM-PC

Intel hat für diese Zwecke extra einen neuen Chip gebaut, den **8259 Interrupt Controller** (auch **PIC** genannt, **Programmable Interrupt Controller**). Dieser Chip hat 8 Leitungen (IRQ 0 - 7) für jedes einzelne Gerät, das der CPU etwas mitteilen muss. Die einzelnen Leitungen nennt man **IRQ Lines** (Interrupt ReQuest). Da jedoch 8 IRQs zuwenig waren, baute Intel einen zweiten Interrupt Controller in den IBM-PC, der über IRQ 2 mit dem ersten verbunden war.

Wie man sieht, ist IRQ 2 nicht als solches verwendbar, sondern dient lediglich zur Kommunikation. Aus Kompatibilitätsgründen wurde deshalb IRQ 2 mit IRQ 9 des 2. Controllers verbunden.

Zu kompliziert? Ganz einfach: wenn ein Gerät IRQ 2 benutzt, dann benutzt es in Wirklichkeit IRQ 9.

Datei:Ausgabe1/irq3.gif

Was passiert nun, wenn ein Gerät einen Interrupt Request über eine IRQ Line sendet? Als erstes gelangt das Signal ins Interrupt **Mask Register (IMR)**. Hier wird festgestellt, ob der IRQ überhaupt verarbeitet werden muss oder nicht (Masking, darauf werde ich allerdings nicht näher eingehen).

Als nächstes gelangt das Signal in den **Priority Resolver**. Dieser findet heraus, welche IRQs zuerst, bzw. welche zuletzt verarbeitet werden müssen. Je niedriger die IRQ-Nummer, desto mehr Priorität hat das Signal (IRQ 0 hat also am meisten Priorität, gefolgt von IRQ 1 usw.)

Nun ist der Interrupt Controller mit allen Vorarbeiten fertig und muss der CPU sagen, dass ein Interrupt ausgelöst wurde. Dies geschieht durch ein **INT-Signal** (Interrupt-Signal), das durch die Interrupt-Leitung des Prozessors gesendet wird. Der Prozessor wird die Anweisung beenden, die er gerade ausführt, und anschließend ein **INTA (Interrupt Acknowledge)** zurücksenden, das den Erhalt des IRQs bestätigt.

Wenn der PIC das INTA-Signal bekommt, wird die Nummer des IRQs im **In Service Register (ISR)** gespeichert, welches also zeigt, welcher IRQ gerade aktiv ist. Außerdem wird es aus dem Interrupt Request Register gelöscht, weil der Prozessor sich ja schon um den IRQ kümmert.

Der Prozessor wird nun ein weiteres INTA-Signal an den PIC senden, um ihm zu sagen, dass er einen 8 Bit-Pointer mit der Nummer des ausgelösten IRQs in den Daten-Bus stellen soll. Die CPU muss schließlich wissen, welcher Interrupt ausgelöst wurde.

Anschließend wird der Prozessor den Interrupt Handler (auch **ISR, Interrupt Service Routine** genannt, aber nicht mit dem In Service Register verwechseln!) aufrufen, der zum jeweiligen Interrupt dazugehört.

Nur: woher weiß der Prozessor, wo der Interrupt Handler ist?

### Interrupt Vector Table

8086-Prozessoren benötigen eine so genannte **Interrupt Vector Table**, an der Adresse 0000:0000, die 1024 Bytes lang ist. Diese Tabelle beinhaltet die Adressen der Interrupt Handler, die aufgerufen werden, wenn ein Interrupt ausgelöst wird. Jede dieser Adressen ist 4 Bytes lang, deshalb kommen wir auf 1024 / 4 = 256 Interrupts, die in der Tabelle sein können.

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/1463/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1415/index.html)

<!-- MediaWiki page 1415; revision 1463; parent 1462; 2006-09-11T18:30:21Z -->
