# Heapverwaltung

Die **Heapverwaltung** ist ein Teil der [Speicherverwaltung](Speicherverwaltung.md "Speicherverwaltung"), der aufbauend auf der virtuellen Speicherverwaltung Funktionen zur Verwaltung dynamisch allozierten Speichers beliebiger Größe – dieser Speicher zusammengenommen wird dann auch als [Heap](Heapverwaltung.md "Heap") bezeichnet – bereitstellt. In der C-Standardbibliothek sind damit die Funktionen malloc/free (und Konsorten) bzw. in der C++-Laufzeitumgebung new/delete gemeint. Gelegentlich werden die beiden Funktionen auch als Bestandteil der virtuellen Speicherverwaltung bezeichnet, da sie ebenfalls mit virtuellen Adressen arbeiten. Sie sind aber nicht mit [Paging](Paging.md "Paging") – d. h. dem, was in diesem Wiki als [virtuelle Speicherverwaltung](Speicherverwaltung.md#virtuelle-speicherverwaltung "Speicherverwaltung") beschrieben wird – zu verwechseln.

## Überblick

Die oben genannten Funktionen werden sowohl im Userspace – als Teil der Standardbibliothek oder Laufzeitumgebung der verwendeten Programmiersprache – als auch im [Kernel](Kernel.md "Kernel") benötigt. Bei der Implementierung im Userspace werden dabei über [Systemaufrufe](Syscall.md "Systemaufruf") die benötigten Funktionen der virtuellen Speicherverwaltung des Kernels – **nicht** der Heapverwaltung des Kernels, da der (Userspace-)Heap (normalerweise) vom Userspace selbst verwaltet wird – aufgerufen. Im Kernel wird direkt auf die virtuelle Speicherverwaltung zugegriffen.

## Freispeicherliste

Die einfachste Möglichkeit malloc() und free() zu implementieren ist eine (meist einfach verkettete) Liste **nur** aus **freien** Speicherbereichen zu verwalten. In malloc() wird dann diese Liste durchlaufen, um nach einem Speicherstück ausreichender Größe zu suchen. Diese Suche kann nach mehreren Strategien erfolgen:

- Exact fit: Ein Speicherstück mit exakt der geforderten Größe wird gesucht
- First fit: Das erstbeste, ausreichend große Speicherstück wird gesucht
- Best fit: Das kleinste, gerade noch ausreichend große Speicherstück wird gesucht

Falls eines gefunden wird, wird dieses aus der Liste entfernt und ein Zeiger auf den Speicherbereich zurückgegeben, ansonsten wird die virtuelle bzw. physische Speicherverwaltung aufgerufen, um neue Speicherseiten zu allozieren. Um Speicher zu sparen, ist es sinnvoll einen Speicherbereich, falls er viel zu groß – d. h. es muss noch Platz für eine weitere Header (siehe unten) und zumindest ein bisschen Speicher danach sein – ist, in zwei Teile zu splitten, wobei der erste zurückgegeben wird und der zweite der Freispeicherliste hinzugefügt wird.

Bei einem free() wird der freizugebende Speicherbereich der Liste der freien Speicherbereiche einfach vorne hinzugefügt.

Damit man für die Liste keinen eigenen Speicher allozieren muss, werden beim malloc bewusst einige Bytes mehr Speicher reserviert (**vor** dem anschließend benutzten Speicherbereich (genannt Header)), um die Größe (und je nach Bedarf weitere Werte, wie z. B. Flags oder einen previous-Pointer) zu speichern. Für den next-Zeiger kann man den eigentlich Speicherbereich verwenden, da der next-Zeiger nur dann gültig sein muss, wenn der Speicherbereich unbenutzt ist.

*Beispielimplementierung:* [Public-Domain C Library](https://svn.lcube.de/dev34/pdclib/trunk/functions/stdlib/malloc.c)

Alternativ kann man auch eine Liste aus **freiem und belegtem** Speicher machen. Dabei reicht es dann aus für jeden Speicherbereich zu speichern, ob er frei oder belegt ist und wie groß er ist. Der next-Zeiger ergibt sich dann implizit aus der Adresse dieses Speicherblocks + Größe dieses Speicherblocks. In dieser Variante ist das malloc wahrscheinlich langsamer, da zusätzlich zu allen freien Speicherbereichen auch die belegten durchlaufen werden (im Worstcase), aber man kann ein Verschmelzen von zwei zusammenhängenden, freien Speicherbereichen sehr einfach durchführen (falls man zusätzlich noch die Größe des vorhergehenden Speicherbereichs oder einen Zeiger auf selbigen speichert).

## Buddy-Speicherverwaltung

Die Buddy-Speicherverwaltung ist sehr einfach zu implementieren: der freie Speicher wird zu Beginn in Blöcke der Größe 2<sup>n</sup> aufgeteilt.  
Bei einer Anfrage nach Speicher wird die angeforderte Größe auf die nächste Zweierpotenz 2<sup>n</sup>aufgerundet. Ist kein Block dieser Größe vorhanden, wird nach einem Block der Größe 2<sup>n+1</sup> gesucht, der dann halbiert wird; wenn kein Block der Größe 2<sup>n+1</sup> vorhanden ist, wird nach 2<sup>n+2</sup> gesucht, usw.  
Bei der Freigabe eines Blocks wird geprüft, ob er direkt mit einem freien Block gleicher Größe benachbart ist, mit welchem er dann zu einem Block von 2<sup>n+1</sup> Bytes zusammen gefügt werden kann.  
Nachteile sind u.U. eine große Platzverschwendung, bspw. wenn die angeforderte Größe 2<sup>n+1</sup>+1 beträgt, und eine mögliche starke Fragmentierung des Speichers.

## Andere Implementierung portieren

Anstatt die benötigten Funktionen selbst zu implementieren, ist es natürlich auch möglich, bestehende Implementierungen zu portieren. Z. B. stehen folgende Implementierungen unter einer freien Lizenz:

- [Doug Lea's Malloc (dlmalloc)](http://g.oswego.edu/dl/html/malloc.html) ([Public Domain](Lizenzen.md "Lizenzen"))
- [The HOARD Memory Allocator](http://www.hoard.org/) ([GPL](Lizenzen.md "Lizenzen"))

## Weblinks

- [Memory Management 2](http://www.osdever.net/tutorials/pdf/memory2.pdf) von Tim Robinson

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/11452/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2229/index.html)

<!-- MediaWiki page 2229; revision 11452; parent 8650; 2020-08-02T22:11:12Z -->
