# Heapverwaltung

Die **Heapverwaltung** ist ein Teil der [Speicherverwaltung](https://github.com/lowlevel-eu/wiki/wiki/Speicherverwaltung "Speicherverwaltung"), der aufbauend auf der virtuellen Speicherverwaltung Funktionen zur Verwaltung dynamisch allozierten Speichers beliebiger Größe- dieser Speicher zusammengenommen wird dann auch als [Heap](https://github.com/lowlevel-eu/wiki/wiki/Heapverwaltung "Heap") bezeichnet - bereitstellt. In der C-Standardbibliothek sind damit die Funktionen malloc/free (und Konsorten) bzw. in der C++-Laufzeitumgebung new/delete gemeint. Gelegentlich werden die beiden Funktionen auch als Bestandteil der virtuellen Speicherverwaltung bezeichnet, da sie ebenfalls mit virtuellen Adressen arbeiten. Sie sind aber nicht mit [Paging](https://github.com/lowlevel-eu/wiki/wiki/Paging "Paging") - d.h. dem was in diesem Wiki als [virtuelle Speicherverwaltung](https://github.com/lowlevel-eu/wiki/wiki/Speicherverwaltung#virtuelle-speicherverwaltung "Speicherverwaltung") beschrieben wird - zu verwechseln.

  

## Überblick

Die oben genannten Funktionen werden sowohl im Userspace - als Teil der Standardbibliothek oder Laufzeitumgebung der verwendeten Programmiersprache - als auch im [Kernel](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel") benötigt. Bei der Implementierung im Userspace werden dabei über [Systemaufrufe](https://github.com/lowlevel-eu/wiki/wiki/Syscall "Systemaufruf") die benötigten Funktionen der virtuellen Speicherverwaltung des Kernels - **nicht** der Heapverwaltung des Kernels, da der (Userspace-)Heap (normalerweise) vom Userspace selbst verwaltet wird - aufgerufen. Im Kernel wird direkt auf die virtuelle Speicherverwaltung zugegriffen.

## Freispeicherliste

**TODO: Überarbeiten**

Es gibt verschiedene Möglichkeiten malloc() bzw. free() zu implementieren. Eine Möglichkeit ist es, vor den Speicherblöcken Header anzulegen, die die Länge, Flags (wie z.B ob der Block frei ist) und gegenfalls einen Pointer auf den nächsten freien Block beinhalten. Zum Anfang sind keine freien Blöcke vorhanden. Es wird vom Kernel eine Page angefordert. Nun wird ein Header an den Anfang der Page gesetzt. Wenn nun malloc() aufgerufen wird, wird der Block aufgeteilt und ein Teilblock als benutzt markiert. Bei einem Aufruf von free() wird der Block als frei markiert und in die Liste der freien Blöcke eingefügt. Wenn benachbarte Blöcke auch frei sind, werden diese zusammengefügt. Wenn man nun eine ganze Page hat, die als frei markiert ist, kann sie vom Kernel freigegeben werden oder aufgehoben werden, bis sie wieder gebraucht wird.

## Andere Implementierung portieren

Anstatt die benötigten Funktionen selbst zu implementieren ist es natürlich auch möglich bestehende Implementierungen zu portieren. Z. B. stehen folgende Implementierungen unter einer freien Lizenz:

- [Doug Lea's Malloc (dlmalloc)](http://g.oswego.edu/dl/html/malloc.html) ([Public Domain](https://github.com/lowlevel-eu/wiki/wiki/Lizenzen "Lizenzen"))
- [The HOARD Memory Allocator](http://www.hoard.org/) ([GPL](https://github.com/lowlevel-eu/wiki/wiki/Lizenzen "Lizenzen"))

## Weblinks

- [Memory Management 2](http://www.osdever.net/tutorials/pdf/memory2.pdf) von Tim Robinson

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/7578/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2229/index.html)

<!-- MediaWiki page 2229; revision 7578; parent 0; 2010-04-15T15:08:15Z -->
