# SFS

**Warnung**

Achtung, alles was hier steht ist von extrem eingeschränkter Nützlichkeit und man sollte sich gut überlegen ob man das wirklich implementieren will!  
Selbst das simple FAT ist dem SFS um Längen überlegen, u.a. weil SFS keine fragmentierten Dateien unterstützt und sich daher echter Schreibzugriff nur äußerst schwer und langsam implementieren lässt!

  

## Einführung

SFS (simple file system) verfolgt das Ziel sehr einfach implementierbar zu sein. Es kann auf Floppys und Festplatten verwendet werden.

Vorteile des SFS:

- Einfacher Aufbau
- Lange Dateinamen

Nachteile des SFS:

- Keine Unterstützung für Linux
- Dateien müssen zusammenhängend sein, d.h. Schreibzugriff erfordert aufwändige und langsame Online-Defragmentierung

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

Das SFS ist extrem simpel aufgebaut und erlaubt daher einfache Datei-Operationen mit recht wenig Code zu realisieren, leider gehören du diesen einfachen Datei-Operationen nicht das Vergrößern oder Verkleinern von Dateien dazu. Als Vorteil kann man die durchgängige Unicode-Unterstützung für die recht langen Dateinamen ansehen und das Fehlen von komplexen Block-Verkettungen ermöglicht zwar einen leichten Einstig stellt aber eben auch die größte Schwäche von SFS dar. Ansonsten bleiben gegenüber anderen ähnlich simplen Dateisystemen, wie z.B. FAT, keine Vorteile übrig. FAT kann recht flexibel mit fragmentierten Dateien umgehen und erlaubt daher einigermaßen simple Schreiboperationen. Dafür hat FAT mit seiner namensgebenden File-Alocation-Table einen etwas komplexeren Mechanismus, gegenüber SFS, mit dem die Positionen der Datenblöcke auf dem Datenträger verwaltet werden, man ist bei FAT selbst schon für das lineare Einlesen von Dateien gezwungen einer Cluster-Kette zu folgen, was aber auch nicht so schwierig ist.

## Weblinks

- [<img src="https://raw.githubusercontent.com/wiki/lowlevel-eu/wiki/assets/38adc39e49df427364bd.png" title="englisch" width="20" height="12" alt="englisch" /> Spezifikation](http://dimensionalrift.homelinux.net/combuster/vdisk/sfs.html)
- [<img src="https://raw.githubusercontent.com/wiki/lowlevel-eu/wiki/assets/38adc39e49df427364bd.png" title="englisch" width="20" height="12" alt="englisch" /> Tool zum Erstellen und Manipulieren von SFS-Images (für Windows)](http://dimensionalrift.homelinux.net/combuster/vdisk/)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/8406/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2301/index.html)

<!-- MediaWiki page 2301; revision 8406; parent 8402; 2010-09-28T18:10:59Z -->
