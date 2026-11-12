# TAR

Diese Seite oder Abschnitt ist zwar komplett, es wird aber folgende Verbesserungen gewünscht:  

*Tutorial fertigschreiben*

Hilf Lowlevel, den Artikel zu verbessern.

  

## Allgemeines

Zuerst einmal ein paar allgemeine Informationen zu TAR und diesem Artikel.

### Worum geht es in diesem Artikel?

Da ich selbst als InitRD-Image das TAR-Format erwählt habe, möchte ich dieses nun hier beschreiben. Währenddessen werden noch ein paar Code-Abschnitte eingebaut, um zu zeigen, wie man alle Dateien in einem solchen Archiv durchläuft oder nur bestimmte Dateien innerhalb eines Ordners im Archiv.

### Was ist TAR und welche Vorteile habe ich damit?

*ToDo: Allgemeine Beschreibung von TAR*  
Der Vorteil von TAR ist, dass hierfür unter bestehenden System wie [Windows](Windows.md "Windows") oder \*nix bereits Tools vorhanden sind, die Archive in diesem Format erstellen können. Das heißt, dass dadurch zum einen der Aufwand minimiert wird, da das Programm an sich bereits vorhanden ist und zum anderen dadurch die Fehlerquellen minimiert werden, da die bereits vorhandenen Programme wie „tar“ oder „7-zip“ Fehlerfrei laufen *sollten*.

  

## Aufbau eines TAR-Archivs

*ToDo: Text schreiben*

### Allgemeines

TAR legt alle Dateien hintereinander mit einem Header voran ab. Möchte man das Archiv komprimieren, so kann man z. B. gzip oder bzip2 nehmen. Allerdings wird dies dann auch im Kernel gebraucht, falls es ausführbare Programme oder Module für den Kernel beinhaltet. Hinweis: Alle Daten im TAR-Header werden als ASCII-Zeichen abgelegt. Wenn man also z. B. die Größe einer Datei ermitteln möchte, so muss man in diesem Fall das Feld „size“ erst einmal in eine Zahl umwandeln und diese dann, da sie oktal vorliegt, ins gewünschte Zahlensystem umrechnen.

### Unterschied TAR-USTAR

*ToDo: Text schreiben*

### TAR

#### Header

Dieser Header ist vor jeder Datei/jedem Verzeichnis/jedem Link und gibt uns Informationen z. B. über die Größe der Datei oder darüber, ob es sich um einen symbolischen Link handelt.

| Byte | Länge | Name |
| ------ | ------- | ----------------------- |
| 0 | 100 | [name](#name) |
| 100 | 8 | [mode](#mode) |
| 108 | 8 | [uid](#uid) |
| 116 | 8 | [gid](#gid) |
| 124 | 12 | [size](#size) |
| 136 | 12 | [mtime](#mtime) |
| 148 | 8 | [chksum](#chksum) |
| 156 | 1 | [link](#link) |
| 157 | 100 | [linkname](#linkname) |

##### name

Hier liegt der Name der archivierten Datei. Dieser String kann nullterminiert sein, muss es aber nicht. Sollten tatsächlich alle 100 Zeichen des Feldes für den Name gebraucht werden, muss daran gedacht werden, die Nullterminierung anzuhängen, wenn man diesen ausgeben möchte.

##### mode

##### uid

##### gid

##### size

Dieses Feld enthält die Größe der eigentlichen Datei. Allerdings werden alle Zahlen in einem TAR-Archiv zum einen als String abgelegt und zum anderen oktal. Möchte man also die Größe der Datei z. B. dezimal ausgeben, so muss man die Oktalzahl zuerst in eine Dezimalzahl umwandeln.

##### mtime

##### chksum

##### link

| Wert |  |
| ------ | ------------------- |
| 0 | normale Datei |
| 1 | verlinkte Datei |
| 2 | symbolischer Link |

##### linkname

Handelt es sich bei der Datei um einen Link, so befindet sich der Name der verlinkten Datei in diesem Feld. Wie auch beim Attribut „name“ kann es sein, dass die Nullterminierung vorhanden ist, es muss aber nicht.

### USTAR-Header

#### Header

| Byte | Länge | Name |
| ------ | ------- | ----------------------- |
| 0 | 100 | [name](#name) |
| 100 | 8 | [mode](#mode) |
| 108 | 8 | [uid](#uid) |
| 116 | 8 | [gid](#gid) |
| 124 | 12 | [size](#size) |
| 136 | 12 | [mtime](#mtime) |
| 148 | 8 | [chksum](#chksum) |
| 156 | 1 | [link](#link) |
| 157 | 100 | [linkname](#linkname) |
| 257 | 6 | [magic](#magic) |
| 263 | 2 | [version](#version) |
| 266 | 32 | [uname](#uname) |
| 298 | 32 | [gname](#gname) |
| 330 | 8 | [devmajor](#devmajor) |
| 338 | 8 | [devminor](#devminor) |
| 346 | 155 | [prefix](#prefix) |

##### name

##### mode

##### uid

##### gid

##### size

##### mtime

##### chksum

##### link

##### linkaname

##### magic

##### version

##### uname

##### gname

##### devmajor

##### devminor

##### prefix

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/10836/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2073/index.html)

<!-- MediaWiki page 2073; revision 10836; parent 7936; 2012-09-16T14:13:36Z -->
