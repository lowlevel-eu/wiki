# SFS

## Einführung

SFS (simple file system) verfolgt das Ziel sehr einfach implementierbar zu sein. Es kann auf Floppys und Festplatten verwendet werden.

Vorteile des SFS:

- Einfacher Aufbau
- Lange Dateinamen

Nachteile des SFS:

- Keine Unterstützung für Linux

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

Dieser Bereich enthält Daten, die der SFS Treiber laut Spezifikation ignorieren muss und die der Programmierer frei verwenden kann, zum Beispiel für den Bootloader.

### Data Area

Der Datenbereich enthält alle Dateien, die das Dateisystem enthält.

### Free Area

Die Free Area trennt die Data Area und die Index Area, d.h. wenn Dateien erstellt werden vergrößert sich der Datenbereich und die Free Area wird kleiner.

### Index Area

Die Index Area enthält die Informationen über die Dateien.

## weiterführende Links

[Spezifikation(Englisch)](http://dimensionalrift.homelinux.net/combuster/vdisk/sfs.html) [\[1\]](http://wiki.osdev.org/SFS)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/8377/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2301/index.html)

<!-- MediaWiki page 2301; revision 8377; parent 8376; 2010-09-26T14:23:01Z -->
