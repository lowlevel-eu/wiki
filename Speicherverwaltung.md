# Speicherverwaltung

Die **Speicherverwaltung** (= **Memory Management**) ist ein wichtiger Teil des [Betriebssystems](https://github.com/lowlevel-eu/wiki/wiki/Betriebssystem "Betriebssystem"). Um genau zu sein ist es ein Grundbestandteil eines Betriebssystems und meistens sogar vollständig im [Kernel](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel") enthalten.

## Einleitung

Generell ist die Speicherverwaltung dafür zuständig nachfragenden Prozessen freien Speicher zuzuteilen bzw. freizugebenden Speicher wieder zurückzunehmen. Dazu muss natürlich gespeichert werden, welche Speicherbereiche belegt bzw. frei sind. Es ist wichtig zu verstehen, dass die Speicherverwaltung normalerweise auf 2 Ebenen aufgeteilt wird: Zum einen die [physische Speicherverwaltung](https://github.com/lowlevel-eu/wiki/wiki/Speicherverwaltung#physische-speicherverwaltung "Speicherverwaltung") und darauf aufbauend die [virtuelle Speicherverwaltung](https://github.com/lowlevel-eu/wiki/wiki/Speicherverwaltung#virtuelle-speicherverwaltung "Speicherverwaltung").

## physische Speicherverwaltung

Die **physische Speicherverwaltung** bildet die unterste Ebene und ermöglicht das Allozieren und Freigeben von physischen Speicherbereichen. Meist sind diese Speicherbereiche gleich groß und richten sich nach der Seitengröße der jeweiligen Architektur. Die Seitengröße beträgt normalerweise bei der [x86](https://github.com/lowlevel-eu/wiki/wiki/X86 "X86")- und [x86-64](https://github.com/lowlevel-eu/wiki/wiki/X86-64 "X86-64")-Architektur 4kB. Es sind dort auch 4 ([x86](https://github.com/lowlevel-eu/wiki/wiki/X86 "X86")) bzw. 2MB ([x86-64](https://github.com/lowlevel-eu/wiki/wiki/X86-64 "X86-64")) möglich. Intern speichert die physische Speicherverwaltung welche Speicherbereiche im physischen Speicher frei sind. Dies könnte folgendermaßen implementiert werden:

### Bitmap

Dabei wird eine Bitmap der Größe *Speichergröße / (Größe einer Speicherseite \* 8)* erstellt. Das x-te Bit dieser Bitmap gibt an ob die x-te Speicherseite (bzw. die Speicherseite an Adresse *Größe einer Speicherseite \* x*) frei oder belegt ist. Beispielsweise benötigt man bei 4GB RAM und 4kB großen Speicherseiten eine 128kB große Bitmap.  

#### Allokation & Freigabe von Speicherseiten

Um eine Speicherseite zu allozieren wird die Bitmap solange durchsucht, bis man ein Bit mit dem Wert 0 gefunden hat. Dieses Bit setzt man dann auf 1, um anzuzeigen, dass diese Speicherseite ab jetzt belegt ist. Dann errechnet man anhand der Position dieses Bits in der Bitmap die Adresse der Speicherseite. Anschließend kann man die Adresse an die aufrufende Funktion zurückgeben.  
Zum Freigeben einer Speicherseite muss nur die Bitposition aus der physischen Adresse berechnet werden und anschließend das Bit an der errechneten Position auf 0 gesetzt werden.

#### Implementationsvorschläge

- Wenn man sich die Bitposition der zuletzt allozierten/freigegebenen Speicherseite merkt, kann man zumindest im Normalfall das Allozieren von Speicherseiten beschleunigen.
- Wenn man beim Allozieren gleich 32 bzw 64 Bit mit dem Wert 0xFFFFFFFF bzw. 0xFFFFFFFFFFFFFFFF vergleicht, kann man mit einem Vergleich gleich 32 bzw. 64 Speicherseiten ausschließen.

#### Eigenschaften

\+ Das Allozieren physisch kontinuierlicher Speicherseiten ist möglich. (lineare Komplexität)  
o Die Bitmap ist relativ klein.  
o Das Freigeben einer Speicherseite ist in konstanter Zeit möglich. (konstante Komplexität)  
- Zum Allozieren einer Speicherseite muss im schlechtesten Fall die gesamte Bitmap durchsucht werden. (lineare Komplexität)  

### Stack

Die Adressen der Speicherseiten werden hierbei auf einen Stack gelegt.

#### Allokation & Freigabe von Speicherseiten

Zum Allozieren einer Speicherseite wird einfach die Adresse, die ganz oben auf dem Stack liegt, genommen. Anschließend wird der Zeiger auf das Stackende angepasst.  
Das Freigeben einer Speicherseite exakt umgekehrt zur Allokation.

#### Implementationsvorschlag

Der Speicher, der für den Stack benutzt wird, wird aus den Speicherseiten, die auf den Stack gelegt werden sollen, erstellt. Dies kann folgendermaßen implementiert werden: Beim Start des Kernels ist der Stack erstmal leer. Desweiteren ist nur ein virtueller und kein physikalischer Speicherbereich für den Stack reserviert. Anschließend geht man die freien Speicherbereiche durch und legt jede freie Speicherseite auf den Stack. Da der Stack bei der ersten Speicherseite noch keinen Speicherbereich hat, nimmt man einfach diese Seite und blendet in den virtuellen Adressraum an der Adresse des Stacks ein. Anschließend können die Adressen einiger Speicherseiten auf den Stack gelegt werden, solange bis wieder kein Speicher vorhanden ist. Dann wird einfach die nächste Speicherseite, die auf den Stack gelegt werden soll, in den virtuellen Adressraum ein. Das kann man beim Freigeben natürlich analog implementieren und Speicherseiten, die in den virtuellen Adressraum engeblendet waren, wieder freigeben, falls dieser Speicherbereich nicht mehr vom Stack selbst benötigt wird. Somit verbraucht der Stack im Prinzip "keinen" Speicher.

#### Eigenschaften

\+ Das Allozieren einer Speicherseite ist in konstanter Zeit möglich. (konstante Komplexität)  
+ Der Stack verbraucht keinen Speicher.  
o Das Freigeben einer Speicherseite ist in konstanter Zeit möglich. (konstante Komplexität)  
- Das Allozieren physisch kontinuierlicher Speicherseiten ist unmöglich.  

### Fazit

Zusammenfassend lässt sich festhalten, dass eine Kombination aus den oben erklärten Datenstrukturen das Beste sein wird. Die Bitmap hat den Vorteil, dass man physisch kontinuierlichen Speicher allozieren kann. Dies benötigt man vor allem für [DMA](https://github.com/lowlevel-eu/wiki/wiki/Direct-Memory-Access "DMA"). Das heißt es macht Sinn bei der [x86](https://github.com/lowlevel-eu/wiki/wiki/X86 "X86")- bzw. [x86-64](https://github.com/lowlevel-eu/wiki/wiki/X86-64 "X86-64")-Architektur die unteren 1/16MB mit einer Bitmap zu verwalten. Der Stack hingegen hat einen unschlagbaren Geschwindigkeits- und Speichervorteil und kann für den Rest des Speichers verwendet werden.

## virtuelle Speicherverwaltung

Die **virtuelle Speicherverwaltung** befindet sich eine Schicht über der [physischen Speicherverwaltung](https://github.com/lowlevel-eu/wiki/wiki/Speicherverwaltung "Speicherverwaltung") und ist für die Organisation der Speicherbereiche im virtuellen Adressraum eines Prozesses zuständig. Unter [x86](https://github.com/lowlevel-eu/wiki/wiki/X86 "X86") und [x86-64](https://github.com/lowlevel-eu/wiki/wiki/X86-64 "X86-64") beispielsweise wird ein virtueller Adressraum über den [Paging-Mechanismus](https://github.com/lowlevel-eu/wiki/wiki/Paging "Paging") (siehe dort für eine genauere Erklärung) realisiert. Dieser virtuelle Adressraum hat erstmal nichts mit dem physischen Adressraum gemeinsam. Erst die virtuelle Speicherverwaltung stellt durch Ein- und Ausblenden von physischen Speicherseiten in den virtuellen Adressraum diese Verbindung her und blendet die Segmente des Prozessimage (Code, Daten, nicht initialisierte Daten, ...), den Heap, den Stack, benötigte shared-libraries, [shared-memory](https://github.com/lowlevel-eu/wiki/wiki/Interprozesskommunikation#shared-memory "IPC"), auch den Kernel, etc. in den virtuellen Adressraum ein oder aus. Die dafür benötigten physischen Speicherseiten werden der physischen Speicherverwaltung entnommen.

Die virtuelle Speicherverwaltung übernimmt in einem Multiprozessorsystem auch die Aufgabe die virtuellen Adressräume über mehrere Prozessoren hinweg konsistent zu halten (siehe auch [SMP](https://github.com/lowlevel-eu/wiki/wiki/Symmetrisches-Multiprozessorsystem "SMP")).

## Weblinks

- [Memory Management 1](http://www.osdever.net/tutorials/pdf/memory1.pdf) und [Memory Management 2](http://www.osdever.net/tutorials/pdf/memory2.pdf) by Tim Robinson

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/2509/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1591/index.html)

<!-- MediaWiki page 1591; revision 2509; parent 2493; 2007-12-26T20:46:51Z -->
