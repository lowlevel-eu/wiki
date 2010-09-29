# SFS

**Achtung!**

Achtung, alles was hier steht ist von extrem eingeschränkter Nützlichkeit und man sollte sich gut überlegen ob man das wirklich implementieren will!  
Selbst das simple FAT ist dem SFS um Längen überlegen, u.a. weil SFS keine fragmentierten Dateien unterstützt und sich daher echter Schreibzugriff nur äußerst schwer und langsam implementieren lässt!  
Siehe dazu auf die [Diskussionsseite](https://lowlevel-eu.github.io/wiki/pages/2302/index.html "Diskussion:SFS") und in den Abschnitt [Vergleich mit anderen Dateisystemen](https://github.com/lowlevel-eu/wiki/wiki/SFS#vergleich-mit-anderen-dateisystemen "SFS")

  

## Einführung

SFS (simple file system) verfolgt das Ziel sehr einfach implementierbar zu sein. Es kann auf Floppys und Festplatten verwendet werden.

Vorteile des SFS:

- Einfacher Aufbau

Nachteile des SFS:

- Keine native Unterstützung unter Linux, Windows oder anderen relevanten Betriebssystemen
  - Unter Windows existiert ein unvollständiges Tool, um auf SFS-Images zuzugreifen
- Dateien müssen zusammenhängend sein, d.h. Schreibzugriff erfordert aufwändige und langsame Online-Defragmentierung
- Die Defragmentierung kann nicht sicher implementiert werden (d.h. ein Absturz/Stromausfall während der Defragmentierung zieht zwangsläufig Datenverlust oder -korruption nach sich)
- Flash-basierte Datenträger (USB-Sticks oder SSDs) könnten aufgrund des häufigen Defragmentierens schneller altern.

## Aufbau

Das SFS teilt das Medium in fünf Bereiche auf.

1.  Superblock
2.  Reserved Area
3.  Data Area
4.  Free Area
5.  Index Area

### Superblock

Der Superblock enthält wichtige Daten für den SFS Treiber.

### Reserved Area

Dieser Bereich enthält Daten, die der SFS Treiber laut Spezifikation ignorieren muss und die der Programmierer frei verwenden kann, zum Beispiel für die Bootloader Stage 2.

### Data Area

Der Datenbereich enthält alle Dateien, die das Dateisystem enthält.

### Free Area

Die Free Area trennt die Data Area und die Index Area, d.h. wenn Dateien erstellt werden vergrößert sich der Datenbereich und die Free Area wird kleiner.

### Index Area

Die Index Area enthält die Informationen über die Dateien.

## Vergleich mit anderen Dateisystemen

Das SFS ist extrem simpel aufgebaut und erlaubt daher einfache Datei-Operationen wie das Lesen von Dateien mit recht wenig Code zu realisieren. Das Fehlen von komplexen Block-Verkettungen ermöglicht zwar einen leichten Einsteig, stellt aber gleichzeitig auch die größte Schwäche von SFS dar. Als weiteren Vorteil kann man die durchgängige Unicode-Unterstützung für die recht langen Dateinamen ansehen.

Für die Implementierung einer Schreibunterstützung sind bereits einige grundlegende Operationen nötig, die mit SFS sehr mühsam und nur unsicher (Gefahr von Datenverlust und Korruption!) zu erreichen sind, z.B. das Erstellen, Vergrößern oder Verkleinern von Dateien.

Auch ansonsten bietet SFS gegenüber anderen ähnlich simplen Dateisystemen, wie z.B. [FAT](https://github.com/lowlevel-eu/wiki/wiki/File-Allocation-Table "FAT"), keine Vorteile. FAT kann recht flexibel mit fragmentierten Dateien umgehen und erlaubt daher einigermaßen simple Schreiboperationen. Dafür hat FAT mit seiner namensgebenden File-Alocation-Table gegenüber SFS einen etwas komplexeren Mechanismus, mit dem die Positionen der Datenblöcke auf dem Datenträger verwaltet werden. Man ist bei FAT selbst schon für das lineare Einlesen von Dateien gezwungen, einer Cluster-Kette zu folgen (was aber auch nicht so schwierig ist, zumindest einfach genug damit man das in einem 512 Byte-FAT-Boot-Sektor realisieren kann).

## Weblinks

- [<img src="https://raw.githubusercontent.com/wiki/lowlevel-eu/wiki/assets/38adc39e49df427364bd.png" title="englisch" width="20" height="12" alt="englisch" /> Spezifikation](http://dimensionalrift.homelinux.net/combuster/vdisk/sfs.html)
- [<img src="https://raw.githubusercontent.com/wiki/lowlevel-eu/wiki/assets/38adc39e49df427364bd.png" title="englisch" width="20" height="12" alt="englisch" /> Tool zum Erstellen und Manipulieren von SFS-Images (für Windows)](http://dimensionalrift.homelinux.net/combuster/vdisk/)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/8411/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2301/index.html)

<!-- MediaWiki page 2301; revision 8411; parent 8410; 2010-09-29T13:07:54Z -->
