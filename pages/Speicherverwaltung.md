# Speicherverwaltung

Die **Speicherverwaltung** (= **Memory Management**) ist ein wichtiger Teil des [Betriebssystems](Betriebssystem.md "Betriebssystem"). Um genau zu sein ist es ein Grundbestandteil eines Betriebssystems und meistens sogar vollständig im [Kernel](Kernel.md "Kernel") enthalten.

## Einleitung

Generell ist die Speicherverwaltung dafür zuständig, nachfragenden Prozessen freien Speicher zuzuteilen bzw. freizugebenden Speicher wieder zurückzunehmen. Dazu muss natürlich gespeichert werden, welche Speicherbereiche belegt bzw. frei sind. Es ist wichtig zu verstehen, dass die Speicherverwaltung normalerweise auf drei Ebenen aufgeteilt wird:

- Die [physische Speicherverwaltung](Physische-Speicherverwaltung.md "Physische Speicherverwaltung") verwaltet Speicherblöcke (physische Seiten) im tatsächlich verfügbaren RAM
- Die [virtuelle Speicherverwaltung](#virtuelle-speicherverwaltung) baut auf der physischen Speicherverwaltung auf. Sie verwaltet Seiten im virtuellen Adressraum und deren Zuordnung zu physischen Seiten.
- malloc/free [verwalten den Heap](Heapverwaltung.md "Heapverwaltung"). Im Gegensatz zu den unterliegenden Schichten, die nur in Blöcken gleicher Größe arbeiten, sind malloc/free dafür zuständig, Speicher für unterschiedlich große Objekte bereitzustellen.

## Physische Speicherverwaltung

*Hauptartikel: [Physische Speicherverwaltung](Physische-Speicherverwaltung.md "Physische Speicherverwaltung")*

Die **Physische Speicherverwaltung** bildet die unterste Ebene und ermöglicht das Allozieren und Freigeben von physischen Speicherbereichen. Meist sind diese Speicherbereiche gleich groß und richten sich nach der Seitengröße der jeweiligen Architektur. Die Seitengröße beträgt normalerweise bei der [x86](X86.md "X86")- und [x86-64](X86-64.md "X86-64")-Architektur 4 kB. Es sind dort auch 4 ([x86](X86.md "X86")) bzw. 2 MB ([x86-64](X86-64.md "X86-64")) möglich. Intern speichert die physische Speicherverwaltung, welche Speicherbereiche im physischen Speicher frei sind.

## Virtuelle Speicherverwaltung

*Hauptartikel: [Paging](Paging.md "Paging")*

Die **virtuelle Speicherverwaltung** befindet sich eine Schicht über der [physischen Speicherverwaltung](#physische-speicherverwaltung) und ist für die Organisation der Speicherbereiche im virtuellen Adressraum eines Prozesses zuständig. Unter [x86](X86.md "X86") und [x86-64](X86-64.md "X86-64") beispielsweise wird ein virtueller Adressraum über den [Paging-Mechanismus](Paging.md "Paging") (siehe dort für eine genauere Erklärung) realisiert. Dieser virtuelle Adressraum hat erstmal nichts mit dem physischen Adressraum gemeinsam. Erst die virtuelle Speicherverwaltung stellt durch Ein- und Ausblenden von physischen Speicherseiten in den virtuellen Adressraum diese Verbindung her und blendet die Sektionen des Prozessimage (Code, Daten, nicht initialisierte Daten, ...), den Heap, den Stack, benötigte shared-libraries, [shared-memory](Interprozesskommunikation.md#shared-memory "IPC"), auch den Kernel, etc. in den virtuellen Adressraum ein oder aus. Die dafür benötigten physischen Speicherseiten werden der physischen Speicherverwaltung entnommen.

Die virtuelle Speicherverwaltung übernimmt in einem Multiprozessorsystem auch die Aufgabe, die virtuellen Adressräume über mehrere Prozessoren hinweg konsistent zu halten (siehe auch [SMP](Symmetrisches-Multiprozessorsystem.md "SMP")).

## Heapverwaltung

*Hauptartikel: [Heapverwaltung](Heapverwaltung.md "Heapverwaltung")*

Die **Heapverwaltung** stellt auf der virtuellen Speicherverwaltung aufbauend Funktionen zur Verwaltung von dynamisch allozierten Speichers beliebiger Größe, wie beispielsweise malloc/free der C-Standardbibliothek zur Verfügung.

## Weblinks

- [Memory Management 1](http://www.osdever.net/tutorials/pdf/memory1.pdf) und [Memory Management 2](http://www.osdever.net/tutorials/pdf/memory2.pdf) by Tim Robinson

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/9423/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1591/index.html)

<!-- MediaWiki page 1591; revision 9423; parent 7876; 2011-02-04T21:29:39Z -->
