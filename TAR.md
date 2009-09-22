# TAR

Diese Seite oder Abschnitt ist zwar komplett, es wird aber folgende Verbesserungen gewünscht:  

*Tutorial fertigschreiben*

Hilf Lowlevel, den Artikel zu verbessern.

  

# Allgemeines

Zuerst einmal ein paar allgemeine Informationen zu TAR und diesem Artikel.

## Worum geht es in diesem Artikel?

Da ich selbst als InitRD-Image das TAR-Format erwählt habe, möchte ich dieses nun hier beschreiben. Zwischendrinne werden dann noch ein paar Code-Abschnitte eingebaut, um zu zeigen, wie man alle Dateien in einem solchen Archiv durchläuft oder nur bestimmte Dateien innerhalb eines Ordners im Archiv.

## Was ist TAR und welche Vorteile habe ich damit?

*ToDo: Allgemeine Beschreibung von TAR*  
Der Vorteil von TAR ist, dass hierfür unter bestehenden System wie Windows oder \*nix bereits Tools vorhanden sind, die Archive in diesem Format erstellen können. Das heißt, dass dadurch zum einen der Aufwand minimiert wird, da das Programm an sich bereits vorhanden ist und zum anderen dadurch die Fehlerquellen minimiert werden, da die bereits vorhandenen Programme wie "tar" oder "7-zip" Fehlerfrei laufen *sollten*.

  

# Aufbau eines TAR-Archivs

*ToDo: Text schreiben*

## Allgemeines

*ToDo: Text schreiben*

## Unterschied TAR-USTAR

*ToDo: Text schreiben*

## TAR

### Header

Dieser Header ist vor jeder Datei/jedem Verzeichnis/jedem Link und gibt uns Informationen wie z.B. wie Groß ist die Datei oder handelt es sich um einen symbolischen Link.

| Byte | Länge | Name |
| ------ | ------- | ---------- |
| 0 | 100 | name |
| 100 | 8 | mode |
| 108 | 8 | uid |
| 116 | 8 | gid |
| 124 | 12 | size |
| 136 | 12 | mtime |
| 148 | 8 | chksum |
| 156 | 1 | link |
| 157 | 100 | linkname |

#### name

Hier liegt der Name der archivierten Datei. Dieser String kann 0-Terminiert sein, muss es aber nicht. Sollten tatsächlich alle 100 Zeichen des Feldes für den Name gebraucht werden, muss daran gedacht werden, die 0-Terminierung anzuhängen, wenn man diesen Ausgeben möchte.

#### mode

#### uid

#### gid

#### size

Dieses Feld enthält die Größe der eigentlichen Datei. Allerdings werden alle Zahlen in einem TAR-Archiv zum einen als String abgelegt und zum anderen Oktal. Möchte man also die Größe der Datei z.B. leserlich ausgeben, so muss man die Oktalzahl zuerst in eine Dezimalzahl umwandeln.

#### mtime

#### chksum

#### link

| Wert |  |
| ------ | ------------------- |
| 0 | normale Datei |
| 1 | verlinkte Datei |
| 2 | symbolischer Link |

#### linkaname

Handelt es sich bei der Datei um einen Link, so ist der Name der verlinkten Datei in diesem Feld. Wie auch beim Attribut "name" kann es sein, dass die 0-Terminierung vorhanden ist, es muss aber nicht.

## USTAR-Header

### Header

| Byte | Länge | Name |  |
| ------ | ------- | ---------- | ----- |
| 0 | 100 | name |  |
| 100 | 8 | mode |  |
| 108 | 8 | uid |  |
| 116 | 8 | gid |  |
| 124 | 12 | size |  |
| 136 | 12 | mtime |  |
| 148 | 8 | chksum |  |
| 156 | 1 | link |  |
| 157 | 100 | linkname |  |
| 156 | 6 | magic |  |
| 156 | 2 | version |  |
| 156 | 32 | uname |  |
| 156 | 32 | gname |  |
| 156 | 8 | devmajor |  |
| 156 | 8 | devminor |  |
| 156 | 155 | prefix |  |

#### name

#### mode

#### uid

#### gid

#### size

#### mtime

#### chksum

#### link

#### linkaname

#### magic

#### version

#### uname

#### gname

#### devmajor

#### devminor

#### prefix

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/5947/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2073/index.html)

<!-- MediaWiki page 2073; revision 5947; parent 5945; 2009-09-22T10:17:30Z -->
