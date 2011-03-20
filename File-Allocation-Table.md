# File Allocation Table

| FAT12/FAT16/FAT32 |  |
| ---------------------------- | ---------------------------------------------------------------- |
| Entwickler: | Microsoft |
| Vollständige Bezeichnung: | File Allocation Table 12/16/32 |
| Maximalgröße einer Datei: | 4 GiB |
| Maximale Dateianzahl: |  |
| Länge des Dateinames: | 255 Zeichen |
| Maximale Dateisystemgröße: | • 32 MiB (FAT12)<br>• 2 – 4 GiB (FAT16)<br>• 8 TiB (FAT32)<br> |

FAT ist ein [Dateisystem](https://github.com/lowlevel-eu/wiki/wiki/Dateisystem "Dateisystem"), das mit [MS-DOS](https://github.com/lowlevel-eu/wiki/wiki/Microsoft-Disk-Operating-System "MS-DOS") eingeführt wurde. Da PCs Ende der 70er Jahre meist noch keine Festplatten sondern nur Diskettenlaufwerke hatten, war dieses Dateisystem zunächst nur für die Kapazitäten von Disketten ausgelegt.

Es gibt drei Varianten, die sich vor allem hinsichtlich der unterstützten Datenträgergröße unterscheiden:

- FAT12
- FAT16
- FAT32

FAT steht dabei für **F**ile **A**llocation **T**able und die Zahl gibt an wie groß die Einträge in dieser Tabelle sind. Mit FAT12 sind somit nur 2<sup>12</sup> Cluster adressierbar, mit FAT16 2<sup>16</sup> und mit FAT32 2<sup>28</sup>.

## Aufbau von FAT

FAT wird in fünf Bereiche unterteilt:

- [Bootsektor](#bootsektor)
- [Reservierte Sektoren](#reservierte-sektoren)
- [File Allocation Table](#file-allocation-table-1)
- [Wurzelverzeichnis](#) (bei FAT32 in der Datenregion enthalten)
- [Datei- und Verzeichnis-Datenregion](#datei--und-verzeichnis-datenregion)

### Bootsektor

Der Bootsektor enthält den BIOS Parameter Block, den Bootloader und die Bootsignatur. Damit der BIOS Parameter Block nicht ausgeführt wird, sind seine ersten 2 Bytes eine JMP-Anweisung. Hinter dem BIOS Parameter Block folgt der Bootloader. Dieser ist unter FAT **zwingend** notwendig. Der Bootloader der von Windows für FAT benutzt wird, zeigt meistens nur eine Nachricht an, dass man die Diskette entfernen und den Computer neustarten solle.

In MS-DOS 1.0 war kein BPB vorhanden. Stattdessen gab es zwei Typen von FAT:

- Single-Sided: Dieser Typ war für einseitige Disketten da
- Double-Sided: Dieser Typ war dagegen für doppelseitige Disketten da.

Ab MS-DOS 2.0 gab es den BPB, womit jetzt jedes FAT-System diesen braucht. (Die Verbreitung von MS-DOS 1.0 ist sehr gering. Deswegen wird nicht empfohlen, auf diese MS-DOS Version acht zu nehmen)

| Offset | Größe | Beschreibung |
| -------- | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0x00 | 3 | Instruktion die den BIOS Parameter Block überspringt |
| 0x03 | 8 | OEM-Name. Der Name, der Software, die das FAT erstellt hat. Dieses Feld hat keinen Einfluss auf das eigentliche Dateisystem. |
| 0x0B | 2 | Sektor-Größe in Bytes. Gültig: 512, 1024, 2048 und 4096. Normal wird 512 verwendet. |
| 0x0D | 1 | Cluster-Größe in Sektoren. Gültig: Zweierpotenz zwischen 1 und 64. |
| 0x0E | 2 | Anzahl reservierter Sektoren inkl. Bootsektor. |
| 0x10 | 1 | Anzahl an File Allocation Tables. Normal gibt es immer 2 FATs |
| 0x11 | 2 | Maximale Anzahl an Einträgen im Wurzelverzeichnis (nur gültig für FAT12 und FAT16) |
| 0x13 | 2 | Anzahl an Sektoren. Wenn hier 0 steht (nötig für FAT32 und bei größeren FAT16-Laufwerken) wird das Feld bei Offset 0x20 benutzt. |
| 0x15 | 1 | Media-Descriptor: • 0xF0: Double sided, 80 Spuren, 18/36 Sektoren pro Spur<br>• 0xF8: Festplatte (dieser Wert wird auch für andere Datenträger benutzt für die kein Media-Descriptor-Byte vergeben wurde wie z.B. ZIP-Disketten oder MO-Disks)<br>• 0xF9: Double sided, 80 Spuren, 9/15 Sektoren pro Spur<br>• 0xFA: Single sided, 80 Spuren, 8 Sektoren pro Spur (eventuell auch Ramdisk)<br>• 0xFB: Double sided, 80 Spuren, 8 Sektoren pro Spur<br>• 0xFC: Single sided, 40 Spuren, 9 Sektoren pro Spur<br>• 0xFD: Double sided, 40 Spuren, 9 Sektoren pro Spur oder Double Sided, 77 Spuren, 26 Sektoren pro Spur<br>• 0xFE: Single sided, 40 Spuren, 8 Sektoren pro Spur, Single Sided, 77 Spuren, 26 Sektoren pro Spur oder Double Sided, 77 Spuren, 8 Sektoren pro Spur<br>• 0xFF: Double sided, 40 Spuren, 8 Sektoren pro Spur<br>Dieses Byte gilt als veraltet und man sollte es daher ignorieren.<br> |
| 0x16 | 2 | FAT-Größe in Sektoren. Bei FAT32 steht hier 0 und es wird das Feld bei Offset 0x24 benutzt. |
| 0x18 | 2 | Spur-Größe in Sektoren. |
| 0x1A | 2 | Anzahl der Schreib-Lese-Köpfe. |
| 0x1C | 4 | Anzahl an Sektoren vor dem Bootsektor (z.B. wenn das FAT auf einer Partition liegt) |
| 0x20 | 4 | Anzahl an Sektoren. (0, wenn das Feld bei 0x13 verwendet wird) |

Die folgenden Daten unterscheiden sich zwischen FAT12/FAT16 und FAT32.

**FAT12 und FAT16**

| Offset | Größe | Beschreibung |
| -------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0x24 | 1 | Nummer des BIOS-Laufwerks |
| 0x25 | 1 | Reserviert |
| 0x26 | 1 | Erweiterte Bootsignatur. Indiziert, ob die folgenden Felder vorhanden sind. (Wert: 0x29) |
| 0x27 | 4 | Dateisystem-ID |
| 0x2B | 11 | Dateisystem-Name (mit Leerzeichen auf 11 Zeichen gefüllt). Wird nicht mehr verwendet. |
| 0x36 | 8 | FAT-Variante (mit Leerzeichen gefüllt), d.h. "FAT12 " oder "FAT16 ". **Achtung**: Dieses Feld ist **nicht** zuverlässig und daher maßgeblich für die Feststellung des Dateisystems. Stattdessen muss die FAT-Variante anhand der Anzahl der Cluster bestimmt werden! |
| 0x3E | 448 | Bootloader |
| 0x1FE | 2 | Bootsignatur: 0xAA55 |

**FAT32**

**Offset**

**Größe**

**Beschreibung**

0x244FAT-Größe in Sektoren 0x282FAT-Flags

| Bits | Bedeutung |
| ------ | ------------------------------------------------------------------------------------------------------------------- |
| 1-3 | Nummer der aktiven FAT. Nur valide, wenn Bit 7 gesetzt ist |
| 7 | Zeigt, ob die FAT von allen FATs gespiegelt wird (0) oder ob lediglich die in Bits 1-3 genannte FAT aktiv ist (1) |

Alle anderen Bits sind reserviert.

0x2A2FAT32-Version. Üblicherweise 0 - andernfalls kann es sein, dass die Partition von Windows nicht gemounted wird. 0x2C4Erster Cluster des Wurzelverzeichnis 0x302Info-Sektor. Sektor der Informationen über das Dateisystem enthält. 0x322Sektor der Bootsektorkopie. (Microsoft empfiehlt, nur 6 zu verwenden) 0x3412Reserviert 0x401Nummer des BIOS-Laufwerks 0x411Reserviert 0x421Erweiterte Bootsignatur. Indiziert, ob die folgenden Felder vorhanden sind. (Wert: 0x29) 0x434Dateisystem-ID 0x4711Dateisystem-Name (mit Leerzeichen auf 11 Zeichen gefüllt). Wird nicht mehr verwendet. 0x528FAT-Variante (mit Leerzeichen gefüllt). Immer "FAT32 ". 0x5A420Bootloader 0x1FE2Bootsignatur: 0xAA55

### Reservierte Sektoren

Nach dem Bootsektor folgen optionale reservierte Sektoren. In diesen Sektoren kann z.B. ein Bootloader untergebracht werden, wenn der Platz im Bootsektor nicht reicht. Der Bootsektor wird von FAT zu den reservierten Sektoren dazugezählt.

### File Allocation Table

In der File Allocation Table (kurz FAT) wird festgehalten, welche Cluster zu welcher Datei gehören. Wenn man den ersten Cluster einer Datei hat, kann man ihn in der FAT nachschlagen und somit den nächsten Cluster herausfinden. Außerdem kann man in der FAT leere Cluster finden, wenn man z.B. eine neue Datei anlegen will. Bei einer Beschädigung eines Clusters kann dieser in der FAT auch als defekt markiert werden. Er wird dann nicht mehr zum Speichern von Daten verwendet.

Normalerweise gibt es zwei FAT-Kopien um durch die Redundanz etwas Fehlertoleranz zu ermöglichen.

| Bedeutung | FAT12 | FAT16 | FAT32 |
| ------------------------------------- | ------------- | --------------- | ------------------------------------ |
| Freier Cluster | 0x000 | 0x0000 | 0x00000000 |
| Verbotene Cluster-Nummern | 0x001 | 0x0001 | 0x00000001 , 0x10000000-0xFFFFFFFF |
| Normaler Cluster einer Clusterkette | 0x002-0xFF6 | 0x0002-0xFFF6 | 0x00000002-0x0FFFFFF6 |
| Defekter Cluster | 0xFF7 | 0xFFF7 | 0x0FFFFFF7 |
| Letzter Cluster einer Clusterkette | 0xFF8-0xFFF | 0xFFF8-0xFFFF | 0x0FFFFFF8-0x0FFFFFFF |

Bei einem normalen Cluster in einer Clusterkette gibt der Wert in der FAT die Nummer des nächsten Clusters an. Man muss also den Wert aus der FAT nehmen und ihn als neuen Index für die FAT benutzen. Wenn man auf die eigentlichen Daten zugreifen will, muss man vorher 2 subtrahieren, weil die Cluster 0 und 1 nicht im Datenbereich existieren (der Datenbereich ist quasi ein Array aus Clustern das mit Index 2 anfängt wogegen die FAT ein Array aus Cluster-Nummern ist das mit Index 0 anfängt).

Die verbotenen Cluster-Nummern dürfen weder in der FAT selber noch in den Verzeichniseinträgen benutzt werden. Die Cluster-Nummer 0 darf in Verzeichiseinträgen nur verwendet werden wenn die betreffende Datei eine Größe von 0 hat (also keine Cluster für Nutzdaten benötigt) und in der FAT kennzeichnet die Cluster-Nummer 0 freie Cluster. Die Einträge 0 und 1 in der FAT werden für unbekannte Zwecke benutzt (die Tools von Microsoft verlangen die aber) und sollten daher nicht verändert werden.

### Wurzelverzeichnis

Bei FAT12 und FAT16 ist das Wurzelverzeichnis ein festgelegter zusammenhängender Bereich auf dem Volume. Es bildet, wie andere Verzeichnisse auch, eine Tabelle aus Verzeichnis-Einträgen. Allerdings wird seine Größe statisch beim Erstellen des Dateisystems festgelegt, so dass die Anzahl möglicher Dateien im Wurzelverzeichnis beschränkt ist.

Bei FAT32 liegt das Wurzelverzeichnis im Datenbereich und wird wie jedes andere Verzeichnis auch behandelt. Es hat deshalb keinen festen Platz auf dem Volume. Sein erster Cluster wird im Boot-Sektor gespeichert, die weiteren Cluster werden in der FAT gespeichert. Die Größe des Wurzelverzeichnisses ist dadurch dynamisch.

### Datei- und Verzeichnis-Datenregion

In der Datei- und Verzeichnis-Datenregion liegen die Datei- und Verzeichnis-Daten. Diese sind in Cluster verteilt. Um eine Datei Clustern zuzuordnen benutzt man die FAT.

## Verzeichnis-Eintrag

Ein Verzeichnis-Eintrag enthält Meta-Daten zu einer Datei (bzw. einem Unterverzeichnis). Ein Verzeichnis-Eintrag enthält außerdem die Nummer des ersten Clusters der Datei.

**Offset**

**Größe**

**Beschreibung**

0x008Dateiname ohne Erweiterung (mit Leerzeichen aufgefüllt). Der Dateiname darf nur aus Großbuchstaben bestehen und darf folgende Zeichen nicht enthalten: 0x22, 0x2A, 0x2B, 0x2C, 0x2E, 0x2F, 0x3A, 0x3B, 0x3C, 0x3D, 0x3E, 0x3F, 0x5B, 0x5C, 0x5D, 0x7C. 0x083Dateierweiterung (mit Leerzeichen aufgefüllt). Erlaubte Zeichen siehe Dateiname. 0x0B1Dateiattribute

| Bit | Bedeutung |
| ----- | --------------- |
| 0 | Schreibschutz |
| 1 | Versteckt |
| 2 | Systemdatei |
| 3 | Volume-Label |
| 4 | Verzeichnis |
| 5 | Archiv |
| 6/7 | Ungenutzt |

Wenn die ersten 4 Bits (Bitmaske: 0x0F) gesetzt sind, handelt es sich um einen VFAT-Eintrag

0x0C1Reserviert 0x0D5Erstellungsdatum

| Bit | Bedeutung |
| -------- | -------------------------------------------------------------------------------------- |
| 0..7 | Dekasekunde (1 Dekasekunde entspricht 10 Millisekunden, gültige Werte von 0 bis 199) |
| 8..12 | Stunde |
| 13..18 | Minute |
| 19..23 | 2 Sekunden |
| 24..30 | Jahr seit 1980 |
| 31..34 | Monat |
| 35..39 | Tag des Monats |

0x122Datum des letzten Zugriffs

| Bit | Bedeutung |
| -------- | ---------------- |
| 0..6 | Jahr seit 1980 |
| 7..10 | Monat |
| 11..15 | Tag des Monats |

0x142Obere 16 Bit des ersten Clusters (nur für FAT32, ansonsten immer 0) 0x164Datum des letzten Schreibzugriffs

| Bit | Bedeutung |
| -------- | ---------------- |
| 0..4 | Stunde |
| 5..10 | Minute |
| 11..15 | 2 Sekunden |
| 16..22 | Jahr seit 1980 |
| 23..26 | Monat |
| 27..31 | Tag des Monats |

0x1A2Erster Cluster  
(Beim Zugriff auf die eigentlichen Daten muss man vorher 2 subtrahieren, da es im Datenbereich die Cluster 0 und 1 nicht gibt. In der FAT gibt es aber die Einträge 0 und 1, so dass dort diese Nummer unverändert benutzt werden muss um zu erfahren welches der nächste Cluster ist.  
Gültige Werte sind 0 wenn die Datei keine Daten enthält also keine Clusterkette benötigt wird und ≥2 wenn doch eine Clusterkette benötigt wird.) 0x1C4Dateigröße in Bytes

## Cluster

Ein Cluster ist auf jedem Datenträger die kleinste von FAT verwaltete Einheit und besteht aus einem oder mehreren (immer eine Zweierpotenz) Sektoren. Bei Disketten, die mit FAT12 formatiert sind, ist ein Cluster immer ein Sektor (also für gewöhnlich 512 Byte) groß. Somit nimmt auf der Diskette jede Datei mindestens 512 Byte in Anspruch, auch wenn sie tatsächlich nur ein Byte groß ist. Eine 2312 Byte große Datei würde dort fünf Cluster belegen und fast einen halben Cluster ungenutzt lassen. Größere Massenspeicher wie heutige Festplatten sind natürlich nicht mit FAT12 formatiert, sondern meistens mit FAT32 oder NTFS. Bei FAT32 kann man 2^28 Cluster adressieren. Meistens sind bei FAT32 acht Sektoren (also für gewöhnlich 4096 Bytes) zu einem Cluster zusammengefasst, somit nimmt dort jede noch so kleine Datei mindestens 4096 Byte in Anspruch. Dateien mit einer Größe von 0 Bytes, also ohne Inhalt, belegen aber nie irgendwelche Cluster.

Um von der Cluster-Nummer auf die Sektor-Nummer zu kommen, in dem die eigentlichen Daten liegen, muss man folgende Gleichung benutzen:

    Sektor_Nummer = ( ( Cluster_Nummer - 2 ) * Cluster_Größe_in_Sektoren ) + Position_des_ersten_Datensektors;

Da es keine Daten-Cluster 0 und 1 gibt wird die Cluster-Nummer um 2 verringert (im Verzeichniseintrag dürfen auch nur Cluster-Nummern größer gleich 2 drin sein wenn eine Datei Daten enthält). Die Multiplikation mit der Cluster-Größe sollte logisch sein. Die Addition mit der Position des ersten Datensektors ist wichtig, weil vor den Nutzdaten ja noch mindestens der Boot-Sektor und die FAT(s) kommen, bei FAT12 und FAT16 kommt da auch noch das Stammverzeichnis. Die Position des ersten Datensektors ist üblicherweise konstant und muss daher nur ein mal beim Mounten ausrechnet werden. Die hier ausgerechnete Sektor-Nummer bezieht sich nur auf das FAT-Dateisystem als solches, wenn dieses Dateisystem als Partition auf einer Festplatte liegt muss dann noch die Start-Position der betreffenden Partition dazu addiert werden um eine absolute Sektor-Nummer zu erhalten. Wenn das Dateisystem ohne Partitionierung auf einer Diskette liegt, dann ist keine weitere Rechnung erforderlich.

Die Position des ersten Datensektors rechnet man folgendermaßen aus:

    Position_des_ersten_Datensektors = Anzahl_reservierter_Sektoren + ( Anzahl_der_FAT_Sektoren * Anzahl_der_FAT_Kopien ) + Anzahl_der_Stammverzeichnissektoren;

Alle diese Informationen sind dem Boot-Sektor zu entnehmen. Die Anzahl der reservierten Sektoren ist mindestens 1, da dazu auch der Boot-Sektor selber zählt. Die Anzahl der FAT-Sektoren und die Anzahl der FAT-Kopien sollten klar sein. Die Anzahl der Stammverzeichnissektoren ist bei FAT32 immer 0, weil dort das Stammverzeichnis ganz normal im Datenbereich liegt.  
Bei FAT12 und FAT16 muss man sich die Größe des Stammverzeichnis in Sektoren erst ausrechnen:

    Anzahl_der_Stammverzeichnissektoren = Anzahl_der_Stammverzeichniseinträge / ( Größe_der_Sektoren_in_Byte / 32 );

Auch diese Informationen sind dem Boot-Sektor zu entnehmen (zumindest bei FAT12 und FAT16). Diese Gleichung sollte ohne Rest aufgehen, wenn dem nicht so ist ist das ein Fehler. Die 32 ist die Größe eines Verzeichniseintrages und die ist bei FAT immer gleich.

Die Informationen die dem Boot-Sektor zu entnehmen sind können je nach FAT-Version in verschiedenen Einträgen drin sein, da muss entsprechend aufgepasst werden.

## VFAT

VFAT (**V**irtual **F**ile **A**llocation **T**able) ist eine Erweiterung für FAT. Sie kommt seit [Windows](https://github.com/lowlevel-eu/wiki/wiki/Windows "Windows") 95 zum Einsatz und wurde entwickelt, um lange Dateinamen nutzen zu können. Beim normalen FAT wird der Dateiname und die Erweiterung in der 8.3-Form angegeben. Bei längeren Namen benutzt VFAT einen Aliasnamen (z.B.: xxxxxx~1.xxx), dessen Nummer hochgezählt wird. Der eigentliche Name wird über mehrere zusätzliche Verzeichniseinträge verteilt. Ältere Systeme sehen diese als ungültig an und ignorieren sie. Der Dateiname kann so bis zu 255 UTF-16 Zeichen enthalten.

Außerdem werden auch das Erstelldatum und das Datum des letzten Zugriffs durch VFAT gespeichert, aber das ist nicht an die Benutzung der langen Dateinamen gebunden.

## Dateikonventionen

Dateinamen bestehen in FAT aus acht Zeichen plus drei Zeichen Dateierweiterung. Die folgenden Zeichen sind reserviert und in Dateinamen nicht erlaubt:

    < > ? " : | \ / *   sind in kurzen und langen Dateinamen verboten
    + , . ; = [ ]       sind nur in kurzen Dateinamen verboten

Leerzeichen am Ende von Name oder Erweiterung werden ignoriert, denn sie werden in Verzeichniseinträgen als Padding für kürzere Dateinamen benutzt.

Mit VFAT erweitert sich die maximale Länge des Dateinamens auf 255 Zeichen, die sowohl Name als auch ggf. Erweiterung und auch den Punkt enthalten. Unter Windows ist außerdem zu beachten, dass weiterhin keine Dateinamen mit einem Leerzeichen am Ende erstellt werden können.

## Siehe auch

- [Ausgabe_4#Das_FAT12-Dateisystem](https://github.com/lowlevel-eu/wiki/wiki/Ausgabe-4#das-fat12-dateisystem "Ausgabe 4")

## Weblinks

- [FAT32 File System Specification](http://www.microsoft.com/whdc/system/platform/firmware/fatgen.mspx) - direkt von Microsoft (im DOC-Format)
- [FAT32 File System Specification](http://www.osdever.net/downloads/docs/fatgen103.zip) - aus der "Cottontail OS Development Library" (als geziptes PDF)
- [Wikipedia-Artikel zu FAT](http://de.wikipedia.org/wiki/File_Allocation_Table)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/9628/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1643/index.html)

<!-- MediaWiki page 1643; revision 9628; parent 9595; 2011-03-20T00:40:24Z -->
