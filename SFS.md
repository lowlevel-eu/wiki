# SFS

**Achtung!**

Achtung, alles was hier steht ist von extrem eingeschränkter Nützlichkeit und man sollte sich gut überlegen ob man das wirklich implementieren will!  
Selbst das simple FAT ist dem SFS um Längen überlegen, u.a. weil SFS keine fragmentierten Dateien unterstützt und sich daher echter Schreibzugriff nur äußerst schwer und langsam implementieren lässt!  
Siehe dazu auf die [Diskussionsseite](https://lowlevel-eu.github.io/wiki/pages/2302/index.html "Diskussion:SFS") und in den Abschnitt [Vergleich mit anderen Dateisystemen](SFS#vergleich-mit-anderen-dateisystemen "SFS")

| SFS |  |
| ---------------------------- | ----------------------------- |
| Entwickler: | Brendan Trotter |
| Vollständige Bezeichnung: | SimpleFS/Simple File System |
| Maximalgröße einer Datei: |  |
| Maximale Dateianzahl: |  |
| Länge des Dateinames: |  |
| Maximale Dateisystemgröße: |  |

  

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
2.  Reservierter Bereich
3.  Datenbereich
4.  Unbenutzer Bereich
5.  Indexbereich

### Superblock

Der Superblock enthält grundlegende Daten über das SFS-Dateisystem. Er ist 512 Bytes groß und entspricht damit dem Bootsektor.

### Reserved Area

Dieser Bereich enthält Daten, die nicht für das Dateisystem selbst benutzt werden. Der SFS-Treiber muss sie laut Spezifikation ignorieren, so dass sie frei verwendet werden können, zum Beispiel für einen Bootloader. Der Superblock ist ebenfalls Teil des reservierten Bereiches.

Die Größe des reservierten Bereichs wird im Superblock festgelegt.

### Data Area

Der Datenbereich enthält alle Nutzdaten, die das Dateisystem enthält. Er hat eine dynamische Größe und kann nach oben hin wachsen, wenn bestehende Dateien vergrößert oder neue Dateien angelegt werden.

### Free Area

Die Free Area ist ein Bereich von unbenutztem Speicher. Er trennt die Data Area und die Index Area, d.h. wenn Dateien erstellt werden vergrößert sich der Datenbereich und die Free Area wird kleiner.

### Index Area

Die Index Area enthält Informationen über die Dateien und entspricht damit in etwa den Verzeichniseinträgen und Inodes in anderen Dateisystemen. Da die Einträge im Indexbereich eine feste Länge von 64 Bytes haben und längere Pfade unterstützt werden, können die Pfade über mehrere Folgeeinträge (*Continuation Entries*) im Indexbereich verteilt werden.

Eine Besonderheit im Vergleich zu anderen Dateisystemen ist, dass es keine Verzeichnisse gibt, die ähnlich zum Indexbereich ihre eigenen Dateien verwalten. Stattdessen werden alle Dateien im Indexbereich gespeichert und enthalten den kompletten Pfad zur Datei.

## Vergleich mit anderen Dateisystemen

Das SFS ist extrem simpel aufgebaut und erlaubt daher einfache Datei-Operationen wie das Lesen von Dateien mit recht wenig Code zu realisieren. Das Fehlen von komplexen Block-Verkettungen ermöglicht zwar einen leichten Einsteig, stellt aber gleichzeitig auch die größte Schwäche von SFS dar. Als weiteren Vorteil kann man die durchgängige Unicode-Unterstützung für die recht langen Dateinamen ansehen.

Für die Implementierung einer Schreibunterstützung sind bereits einige grundlegende Operationen nötig, die mit SFS sehr mühsam und nur unsicher (Gefahr von Datenverlust und Korruption!) zu erreichen sind, z.B. das Erstellen, Vergrößern oder Verkleinern von Dateien.

Auch ansonsten bietet SFS gegenüber anderen ähnlich simplen Dateisystemen, wie z.B. [FAT](File-Allocation-Table "FAT"), keine Vorteile. FAT kann recht flexibel mit fragmentierten Dateien umgehen und erlaubt daher einigermaßen simple Schreiboperationen. Dafür hat FAT mit seiner namensgebenden File-Alocation-Table gegenüber SFS einen etwas komplexeren Mechanismus, mit dem die Positionen der Datenblöcke auf dem Datenträger verwaltet werden. Man ist bei FAT selbst schon für das lineare Einlesen von Dateien gezwungen, einer Cluster-Kette zu folgen (was aber auch nicht so schwierig ist, zumindest einfach genug damit man das in einem 512 Byte-FAT-Boot-Sektor realisieren kann).

Lange Dateinamen sind in SFS recht simpel implementiert obwohl man auch dort mehrere "Entrys" benötigt, der Name wird dann über (mehrere) "Continuation Entrys" fortgesetzt. In diesem Punkt ist FAT etwas komplexer weil es immer noch parallel den kurzen (8.3) Dateinamen gibt der nach bestimmten Regeln mit gepflegt werden muss. Dafür sind bei FAT die Fortsetzungs-Einträge als solche zu erkennen und mit einer Prüfsumme über den gesamten Dateinamen gesichert, was beides bei SFS nicht gegeben ist so das SFS hier einer höheren Gefahr von Datenfehlern ausgesetzt ist (so ein "Continuation Entry" könnte fälschlicherweise auch für was anderes gehalten werden).

In den Verzeichnis- und Datei-Namen von SFS ist auch immer der gesamte Pfad enthalten. SFS selber unterscheidet nicht zwischen verschiedenen Verzeichnissen, alle Entrys liegen (ohne besondere Ordnung) in der einen Index-Area. Das macht es sehr langwierig alle Dateien eines bestimmten Verzeichnisses aufzulisten. SFS ist eher auf kleine Datenträger mit wenigen Dateien/Verzeichnissen ausgelegt (so das der SFS-Treiber eine komplette Liste im RAM halten kann).

SFS ist sehr darauf angewiesen das der benutzte Datenträger keine defekten Sektoren bekommt, in der Index-Area gibt es absolut keine Fehlertoleranz, wenn ein Eintrag defekt ist kann es passieren das alle folgenden (noch intakten) Einträge ebenfalls unbrauchbar sind.

## Weblinks

- [<img src="assets/38adc39e49df427364bd.png" title="englisch" width="20" height="12" alt="englisch" /> Spezifikation](http://dimensionalrift.homelinux.net/combuster/vdisk/sfs.html)
- [<img src="assets/38adc39e49df427364bd.png" title="englisch" width="20" height="12" alt="englisch" /> Tool zum Erstellen und Manipulieren von SFS-Images (für Windows)](http://dimensionalrift.homelinux.net/combuster/vdisk/)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/9918/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2301/index.html)

<!-- MediaWiki page 2301; revision 9918; parent 8445; 2011-07-12T09:37:58Z -->
