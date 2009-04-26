# Speicherverwaltung

Die **Speicherverwaltung** (= **Memory Management**) ist ein wichtiger Teil des [Betriebssystems](https://github.com/lowlevel-eu/wiki/wiki/Betriebssystem "Betriebssystem"). Um genau zu sein ist es ein Grundbestandteil eines Betriebssystems und meistens sogar vollständig im [Kernel](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel") enthalten.

## Einleitung

Generell ist die Speicherverwaltung dafür zuständig nachfragenden Prozessen freien Speicher zuzuteilen bzw. freizugebenden Speicher wieder zurückzunehmen. Dazu muss natürlich gespeichert werden, welche Speicherbereiche belegt bzw. frei sind. Es ist wichtig zu verstehen, dass die Speicherverwaltung normalerweise auf 2 Ebenen aufgeteilt wird: Zum einen die [physische Speicherverwaltung](#physische-speicherverwaltung) und darauf aufbauend die [virtuelle Speicherverwaltung](#virtuelle-speicherverwaltung).

## Physische Speicherverwaltung

Die **Physische Speicherverwaltung** bildet die unterste Ebene und ermöglicht das Allozieren und Freigeben von physischen Speicherbereichen. Meist sind diese Speicherbereiche gleich groß und richten sich nach der Seitengröße der jeweiligen Architektur. Die Seitengröße beträgt normalerweise bei der [x86](https://github.com/lowlevel-eu/wiki/wiki/X86 "X86")- und [x86-64](https://github.com/lowlevel-eu/wiki/wiki/X86-64 "X86-64")-Architektur 4kB. Es sind dort auch 4 ([x86](https://github.com/lowlevel-eu/wiki/wiki/X86 "X86")) bzw. 2MB ([x86-64](https://github.com/lowlevel-eu/wiki/wiki/X86-64 "X86-64")) möglich. Intern speichert die physische Speicherverwaltung welche Speicherbereiche im physischen Speicher frei sind.

Hauptartikel: [Physische Speicherverwaltung](https://github.com/lowlevel-eu/wiki/wiki/Physische-Speicherverwaltung "Physische Speicherverwaltung")

## virtuelle Speicherverwaltung

Die **virtuelle Speicherverwaltung** befindet sich eine Schicht über der [physischen Speicherverwaltung](#physische-speicherverwaltung) und ist für die Organisation der Speicherbereiche im virtuellen Adressraum eines Prozesses zuständig. Unter [x86](https://github.com/lowlevel-eu/wiki/wiki/X86 "X86") und [x86-64](https://github.com/lowlevel-eu/wiki/wiki/X86-64 "X86-64") beispielsweise wird ein virtueller Adressraum über den [Paging-Mechanismus](https://github.com/lowlevel-eu/wiki/wiki/Paging "Paging") (siehe dort für eine genauere Erklärung) realisiert. Dieser virtuelle Adressraum hat erstmal nichts mit dem physischen Adressraum gemeinsam. Erst die virtuelle Speicherverwaltung stellt durch Ein- und Ausblenden von physischen Speicherseiten in den virtuellen Adressraum diese Verbindung her und blendet die Segmente des Prozessimage (Code, Daten, nicht initialisierte Daten, ...), den Heap, den Stack, benötigte shared-libraries, [shared-memory](https://github.com/lowlevel-eu/wiki/wiki/Interprozesskommunikation#shared-memory "IPC"), auch den Kernel, etc. in den virtuellen Adressraum ein oder aus. Die dafür benötigten physischen Speicherseiten werden der physischen Speicherverwaltung entnommen.

Die virtuelle Speicherverwaltung übernimmt in einem Multiprozessorsystem auch die Aufgabe die virtuellen Adressräume über mehrere Prozessoren hinweg konsistent zu halten (siehe auch [SMP](https://github.com/lowlevel-eu/wiki/wiki/Symmetrisches-Multiprozessorsystem "SMP")).

### Implementierung von malloc()/free()

Es gibt verschiedene Möglichkeiten malloc() bzw. free() zu implementieren. Eine Möglichkeit ist es vor den Speicherblöcken Header anzulegen, die die Länge, Flags (wie z.B ob der Block frei ist) und gegenfalls einen Pointer auf den nächsten freien Block beinhalten. Zum Anfang sind keine freien Blöcke vorhanden. Es wird vom Kernel eine Page angefordert. Nun wird ein Header an den Anfang der Page gesetzt. Wenn nun malloc() aufgerufen wird, wird der Block aufgeteilt und ein Teilblock als benutzt markiert. Bei einem Aufruf von free() wird der Block als frei markiert und in die Liste der freien Blöcke eingefügt. Wenn benachbarte Blöcke auch frei sind, werden diese zusammengefügt. Wenn man nun eine ganze Page hat, die als frei markiert ist, kann sie vom Kernel freigegeben werden oder aufgehoben werden, bis sie wieder gebraucht wird.

Man kann auch eine der freien malloc()/free() Implementierungen portieren:

- [The HOARD Memory Allocator](http://www.hoard.org/) ([GPL](https://github.com/lowlevel-eu/wiki/wiki/Lizenzen "Lizenzen"))
- [Doug Lea's Malloc (dlmalloc)](http://g.oswego.edu/dl/html/malloc.html) ([Public Domain](https://github.com/lowlevel-eu/wiki/wiki/Lizenzen "Lizenzen"))

## Weblinks

- [Memory Management 1](http://www.osdever.net/tutorials/pdf/memory1.pdf) und [Memory Management 2](http://www.osdever.net/tutorials/pdf/memory2.pdf) by Tim Robinson

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/4325/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1591/index.html)

<!-- MediaWiki page 1591; revision 4325; parent 4045; 2009-04-26T19:22:29Z -->
