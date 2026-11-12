# Ausgabe 9

|  |  |
| ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| © | Dieser Artikel ist urheberrechtlich geschützt.<br>Bitte beachte, dass die üblichen [Lizenzbestimmungen](https://lowlevel-eu.github.io/wiki/pages/1637/index.html "Lowlevel:Urheberrecht") des Wikis für diesen Artikel nicht gelten. |

  

|  |  |  |
| ------------------------------------------------------------------------------- | ---------------- | ----- |
| « [Ausgabe 8](Ausgabe-8 "Ausgabe 8") | **Navigation** |  |

## Einleitung

Hi,

wie ihr sicher auch schon gemerkt habt, ist das Weiterführen vom Magazin nicht immer unproblematisch. Deshalb haben N00B und ich vor, einige Änderungen durchzuführen. Im Wesentlichen betrifft das das Kategoriesystem. Es wird keine 10 Kategorien mehr geben, die in allen Ausgaben vorhanden sind. Stattdessen hat jede Ausgabe einen Thmenschwepunkt. Das könnten z.B. Protected Mode Features sein, mit Tutorials über Paging, Hardware MT, usw. Natürlich gibt es trotzdem noch einige Standard Kategorien, nämlich die News, das OS-Showcase, usw. In dieser Ausgabe wird der Schwerpunkt bei Speichergeräten liegen, wir haben dazu eine IDE-Übersicht, ein ext2-Tutorial, und noch einiges mehr.

Dies wird außerdem die erste Ausgabe sein, die nicht nur als PDF File sondern auch im Wiki erscheint. Das hat natürlich den Vorteil, dass Fehler schnell verbessert werden können.

Wir wünschen euch viel Spaß mit der neuen Ausgabe!

## News

Viel neues ist passiert seit der letzten Ausgabe - auch nicht weiter verwunderlich, wenn man bedenkt wieviel Zeit ins Land gegangen ist ;) . Vor wenigen Wochen, am 22.7 ist QEMU 0.8.2 herausgekommen. Als einer der wenigen Emulatoren verfügt er über ein Kernelmodul um die Ausführung der ganzen VM erheblich zu beschleunigen - mir fällt sonst nur VMWare ein, dass diese Möglichkeit nutzt. Neu in der aktuellen Version sind u.a. ACPI Support und einige Verbesserungen der USB-Fähigkeiten.

Auch beim längst totgeglaubten Community-OS LOST gibt es Fortschritte. Seitdem taljeth die Projektleitung übernommen hat, sind einige Fortschritte zu beobachten. Mittlerweile funktioniert sogar eine erste Form des Multitasking, welche Jidder/PorkChicken zusammen mit dem Phys. Speichermanagment entwickelt hat. Es fehlt also nicht mehr viel bis die ersten Treiberprogramme (Für die die es nicht wissen, LOST ist ein Microkernel) geschrieben werden können.

## Ein OS auf einer CD-ROM

### Index

- Einleitung
- Praxis: Ahead Nero
- Theorie: Das ISO El-Torito Format
- Nachwort

### Einleitung

Irgendwie ist es halb drei Uhr in der Früh und ich kann nicht mehr schlafen, darum will ich jetzt mal was sinnvolles machen und anderen versuchen zu erklären, wie man ein Betriebssystem auf eine CD-ROM bekommt, und wie das BIOS dieses ISO El-Torito Format ließt. Nun gut, auf gehts...

### Praxis: Ahead Nero

Wenn wir unser Betriebssystem geschrieben haben und in einer .IMG Datei compiliert haben, schreiben wir es normalerweise mit RaWrite (oder einem ähnlichen Programm) 1 zu 1 auf eine Diskette. Da aber in unserer 'modernen' Welt selbst PCs existieren, die keine Diskettenlaufwerke mehr haben (tja, scheisse :D) haben wir Pech gehabt. Oder? Anstatt das Betriebssystem auf einer Diskette anzubieten, können wir es auch auf eine CD-ROM schreiben (ein CD-ROM Laufwerk hat beinahe jeder PC/Laptop), und wir sind dieses Problem los. Doch wie schreibt man nun ein Betriebssystem auf eine CD-ROM? Ich werde das nun versuchen Schritt für Schritt zu erklären:

1.  Man compiliert sein Betriebssystem ganz normal, und erstellt eine .IMG Datei - wie es auch für Disketten-Betriebssysteme gemacht wird
2.  Man öffnet 'Ahead Nero Burning ROM' (btw: ich finde den Namen sehr gelungen :D)
3.  Neue Zusammenstellung -\> 'CD-ROM (Boot)'
4.  Das Options-Feld 'Image-Datei' anklicken und den Pfad zum Image des Betriebssystems eingeben. 'Neu' klicken
5.  Dann, schlussendlich, das Dialogfeld 'CD Brennen' klicken und die CD-ROM brennen

Wenn wir nun den Computer neu starten, und im BIOS die Option "von CD-ROM Booten" auswählen, startet unser Betriebssystem als wäre es eine Diskette. OK, wir wissen nun, wie es gemacht wird, aber nicht, warum es das macht.

### Theorie: Das ISO El-Torito Format

Eine bootfähige CD-ROM hat in den meisten Fällen ein Dateisystem namens "ISO El-Torito". Das ist der gängige Standard für bootfähige CD-ROMs, die fast alle BIOS-Systeme erkennen.

Zuerst ist wichtig: Ein Sektor auf einem ISO-Datenträger ist 0x800 Byte groß (im Gegensatz zu Sektoren auf FAT Systemen, die grundsätzlich 0x200 Byte groß sind).

Bei El-Torito CD-ROM wird im Grunde nichts anderes gemacht als eine Diskette emuliert, die das bootfähige Image beinhaltet. Das ISO-El-Torito Format ist grundsätzlich so aufgebaut:

                   +-------------------------+
        Sector 0:  |          SYSTEM         |
                   |         (UNUSED)        |
                   |-------------------------|
        Sector 16: |      Primary Volume     |
                   |-------------------------|
        Sector 17: |    Boot Record Volume   |-------+
                   |-------------------------|       |
                   |                         |       |
                   |-------------------------|       |
                   |                         |       |
                   |-------------------------|       |
                   |                         |       |
                   |-------------------------|       |
                   | Set Termination Volume  |       |
                   |-------------------------|       |
                   |     Boot Catalog        | <-----+ 
                   |                         |-------+
                   |-------------------------|       |
                   |  Bootable Disk Image    | <-----+
                   |-------------------------|
                   |      CD-ROM Image       |
                   +-------------------------+

Das bedeutet, im Sektor 17 (an der Adresse 17 \* 0x800) ist das Boot-Record Volume. Dieses hat einen Zeiger auf den Boot-Catalog, und sieht folgendermaßen aus:

  

| Offset | Type | Description |
| ------------ | ------- | ----------------------------------------------------------------------------------------------------------------------- |
| 0x0 | Byte | Boot Record Indicator |
| 0x1-0x5 | Byte | ISO-9660 Identifier, muss 'CD001' sein |
| 0x6 | Byte | Version des Descriptor, muss '1' sein |
| 0x7-0x26 | Byte | Boot System Identifier, immer 'EL TORITO SPECIFICATION", wird mit Nullen aufgefüllt um die Korrekte Größe zu erhalten |
| 0x27-0x46 | Byte | Unbenutzt, immer 0 |
| 0x47-0x4A | DWord | Absolute pointer to first sector of Boot Catalog |
| 0x4A-0x7FF | Byte | Unbenutzt, 0 |

Wie wir hier deutlich erkennen können, ist an der Adresse 0x47-0x4A im 17. CD-ROM Sektor der Pointer zum Boot-Catalog. Wir folgen nun diesem Pointer und sehen uns den Boot Catalog an:

| Offset | Type | Description |
| ----------- | ------ | ------------------------ |
| 0x0 | Byte | Header ID, immer 01 |
| 0x1 | Byte | Platform ID |
| 0x2-0x3 | Word | Reserviert, immer 0 |
| 0x 4-0x1B | Char | ID-String |
| 0x1C-0x1D | Int | Checksum Word |
| 0x1E | Byte | Key Byte, muss 55 sein |
| 0x1F | Byte | Key Byte, muss AA sein |

Hier sehen wir zuerst einige Standard-Strings und Zeichen ("0x55, 0xAA" sollten wir schon kennen). 0x20 Byte weiter (also 32 Bytes weiter) im selben Sektor befindet sich dann der "Initial/Default Entry", der auch den Pointer zu unserem Boot-Image beinhaltet:

| Offset | Type | Description |
| ----------- | ------- | --------------------------------------------------------- |
| 0x0 | Byte | Boot Indicator ( 88 = bootable, 00 = not bootable ) |
| 0x1 | Byte | Boot media Type |
| 0x2-0x3 | Word | Load segment (standard is 0x7C0) |
| 0x4 | Byte | System Type |
| 0x5 | Byte | Unbenutzt, 0 |
| 0x6-0x7 | Word | Sector count |
| 0x8-0x0B | DWord | Load RBA. This is the start address of the virtual disk |
| 0x0C-0x1F | Byte | Unbenutzt, 0 |

An der Adresse 0x08-0x0B befindet sich schließlich der Pointer zum Image unseres Betriebssystems. Hier befindet sich also das Image - und wir wissen nun auch ein bisschen, wie unser Betriebssystem auf einer CD-ROM gespeichert ist.

Wer mehr wissen möchte, sollte folgende Dokumente lesen:

- FAT: Gerneral Overview of On-Disk Formation by Microsoft Corporation
- Volume and File Structure of CDROM for Information Interchange
- ["El Torito" Bootable CD-ROM Format Specification](http://www.phoenix.com/NR/rdonlyres/98D3219C-9CC9-4DF5-B496-A286D893E36A/0/specscdrom.pdf)

### Nachwort

Das wars auch schon wieder - ich hoffe man konnte einige nützliche Informationen im Artikel finden. Falls nicht, mir egal - ich bin endlich müde und kann vielleicht weiterschlafen ;).

Also, schön weiterprogrammieren, lernen, Ideen entwickeln und so weiter. Und: Von nichts und niemandem vom Kurs abbringen lassen ;)

SPTH

Second Part To Hell

## Dateisystemvergleiche

Bestimmt hast du auch schon das eine oder andere Dateisystem implementiert, oder planst dies in näherer Zukunft zu tun. Da nicht jeder Lust hat sein eigenes System zu entwerfen, hier mal einige Infos über verschiedene Dateisysteme, für einen schnellen Vergleich ordentlich in einer Tabelle dargestellt. Ich hoffe ich erleichtere euch eure Arbeit hiermit ein bisschen, und verkompliziere sie nicht noch eher weil es so viele interessante Systeme gibt \*g\*. Viel Spaß, stultus/N00b  
  

|  | ext2 | ReiserFS | Fat32 |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Zugriffskontrolle | chmod | ? | keine |
| Blockgröße | 2 kB - 8 kB | 4 kB | 4 kB (Standard) |
| Max. Dateigröße | Je nach Blockgröße 16 GB bis 2 TB | 2 GB – 1 Byte (Allerdings 1 Exabyte bei Version 3.6) \* | 4 GB – 1 Byte |
| Max. Dateisystemgröße | Je nach Blockgröße 2 TB bis 32 TB \* | 16 TB \* | 8 TB (unter Windows XP maximal 32 GB formatierbar, aber unbegrenzt lesbar) |
| Max. Unterverzeichnisse | 32.768 | ? | 65.553 (2^16) von Microsoft vorgesehen, theoretisch bis 2^28 = 268435456 möglich (inkl. Dateien im Verzeichniss), 2^28 da 4 Bit reserviert sind (lt. Wikipedia), evtl. also auch auf 2^32 erweiterbar. |
| Max. Dateien je Verzeichnisse | Ca. 130 Trillionen (10^18), Warnungen ab 10.000 Dateien in einem Verzeichnis | 518701895 (limitiert durch eine Hash-Funktion) | 268435456 (inkl. Unterverzeichnissen) |
| Max. Dateien gesamt | ? | 2^32 – 3 (4.294.967.293) | ? |
| Besonderheiten | Erweiterbar ohne dass das System ein bestimmtes Feature zwingend können MUSS, möglich wird dis durch die COMPAT, RO_COMPAT und INCOMAT – Felder im Superblock Journaling-Erweiterung (ext3)<br> | Erstes Journaling-Dateisystem das unter Linux komplett unterstützt wurde. | Kann von allen gängigen Systemen (Linux, Mac OS, Windows) gelesen und geschrieben werden. |

  

- Anmerkung: Größen jenseits 2 Terabyte (TB) sind nicht möglich, da die maximale Länge einer Partition bei aktuellen Partitionstabellen 2 TB nicht übersteigen kann (und das Laufwerk maximal 4 TB groß sein kann).

  
  
Quellen: [Wikipedia](http://de.wikipedia.org/wiki/)

## ext2

### Worum geht es in diesem Tutorial?

Es geht hier um den Aufbau von ext2! Hier werdet ihr KEINEN Code bekommen!

### Was ist ext2?

ext2 ist das Standarddateisystem von Linux. Es gehört zu den stabilsten am Markt, wenn auch nicht zu den schnellsten. Leider bietet es noch kein Journaling-Funktion (Hierzu existiert allerdings die Erweiterung ext3, wobei jede Partition die mit ext3 verwendet wird auch ohne weiteres mit ext2-Treibern betrieben werden kann - es fehlt halt lediglich die Journaling-Funktionalität). Es ist, logischerweise, der Nachfolger von ext1 (bzw. ext).

### Wie ist ext2 aufgebaut?

Einige Daten:

|  |  |
| --------------------------- | ----------------------------------- |
| Maximale Dateigröße | Je nach Blockgröße 16 GB bis 2 TB |
| Maximale Dateinamenslänge | 255 Zeichen |

  
In ext2 besteht eine Datei aus zwei Teilen: Kopf (I-node) und Rumpf. In der I-Node-Table ist die Information über die physikalische Position einer Datei. Im Rumpf die eigentliche Datei.  
  
Sehen Sie sich folgende Abbildung an:

![Ext2_aufbau1.png](http://lowlevel.brainsware.org/wiki/images/Ext2_aufbau1.png)

Die kleinste adressierbare Einheit ist ein Block. Er ist bei ext2 immer 4096 Byte groß. Eigentlich kann man sie anpassen, aber das sollte man nicht. Jeder Block erhält eine eindeutige Nummer. Der I-node ist bei jeder Datei vorhanden, die I-Node-Table ist mit der FAT zu vergleichen.  
  

### Blöcke

Solange eine Datei nicht größer als 10 Blöcke ist, kann sie in ext2 noch mit dem I-node adressiert werden. Wenn sie größer ist, wird ein Indirektionsblock angelegt, der im I-node steht und in diesen werden wieder weitere Blocks adressiert. Man könnte also mit dem Indirektionsblock weitere Indirektionsblöcke adressieren und so weiter, bis die Datei 2 GB groß ist.  
  

### Zugriffsrechte

Wenn ihr euch in der Abbildung die I-Node-Table angesehen habt, werdet ihr euch gedacht haben, was das bedeutet. Das Beispiel oben war unvollstängig! Nehmen wir ein Richtiges mit mehreren Einträgen:

       -rwx-rw-r 1root root Jun 11 12:45 Text1
       drw-x 1root root Jun 11 12:46 Programm3
       cx 1root root Jun 11 12:46 Device5
       bx 1root root Jun 11 12:47 Device8
       l 1root root Jun 11 12:48 ..
       p 1root root Jun 11 12:59 test5

  
So: In der 1. Zeile das erste Zeichen, hier -, heißt in diesem Fall, dass es eine normale Datei ist. Das erste Zeichen gibt immer den Typ an:  

| Zeichen | Bedeutung |
| -------------------------------- | ----------- |
| Normale Datei | \- |
| Verzeichniss | d |
| Zeichenorientierte Gerätedatei | c |
| Blockorientierte Gerätedatei | b |
| Link | l |
| Pipe | p |

  
Was was ist, dürfte klar sein, wenn man diese Tutorial liest.  
Nun, die weiteren Zeichen bis zur ersten Leerstelle sind die Zugriffsrechte. Im Beispiel: rwx-rw-r = Dateibesitzer darf Lesen(r), schreiben(w) und ausführen(x), die Gruppe der der Besitzer angehört, darf lesen und schreiben und alle anderen Benutzer dürfen nur lesen. Der root darf selbstverständlich alles. Also heißt beispielsweise in Beispiel 3 wo steht: cx = Datei ist eine zeichenorientierte Gerätedatei und darf nur vom Besitzer ausgeführt werden.  
  
Zugriffsrechttabelle:  

| Zeichen | Bedeutung |
| --------- | ----------- |
| r | Lesen |
| w | Schreiben |
| x | Ausführen |

  
Der nächste String, 1root, ist der Dateibesitzer. Der nächste ist dann die Gruppe, der der Besitzer angehört. Danach kommt das Datum, hier 11. Juni und dann die Uhrzeit der Erstellung. Zum Schluss noch der Dateiname.  
  
In ext2 wird das FS in Gruppen eingeteilt. Jede Gruppe ist 8192 Blöcke groß. Jede Gruppe enthält eine Kopie das Superblocks und einen Gruppenblock. Der Superblock ist der I-Node-Table und der Gruppenblock behandelt die Gruppe wie eine eigene Partition.  
  
Beim Anbinden von Dateisystemen löscht ext2 im Superblock einen für jede verschiedene Partition die vorhanden ist angelegten valid-Flag. Wenn das FS die Partition wieder aushängt, setzt ext2 den valid-Flag wieder.  
So sollte der Kernel erkennen, dass das System nicht ordnungsgemäß heruntergefahren wurde und das Dateisystem prüfen.

## OS-Showcase: FreeBSD

### Screenshots

![FreeBSD1.jpg](http://lowlevel.brainsware.org/wiki/images/FreeBSD1.jpg)  
  
![FreeBSD2.gif](http://lowlevel.brainsware.org/wiki/images/FreeBSD2.gif)

*Anmerkung: FreeBSD ist genau wie Unix oder Linux ein textbasiertes OS. Erst nach der Installation eines Desktops, gibt es eine GUI wie man sie auf den Screenshots sieht.*

### Geschichte

Die erste Version von FreeBSD (1.0) erschien im November 1993, basierend auf den Quelltexten von 386BSD, 4.3BSD-Lite (Net/2) und dem dazu existierenden Patchkit. Die Entwicklung begann allerdings schon im Juli 1993. Im November 1994 erschien dann die Version 2.0, die jetzt auf den Quelltexten von 4.4BSD-Lite basiert. Version 3.0 erschien dann erst 1998 und Version 4.0 dann 2000. Im Jahre 2003 erschien dann die Version 5.0. Die aktuelle Version, die es seit November 2004 gibt, ist FreeBSD 5.3.  
FreeBSD ist vor allem bei Internet-Providern weit verbreitet. So setzt auch das ziemlich bekannte Internet-Portal und Suchmaschine Yahoo! auf diese Technologie.

### Features

Die Version 1.0 von FreeBSD gibt es seit November 1993. Seit November 2004 gibt es schon die Version 5.3, welche sehr viel Funktionen hat, die ich jetzt nicht alle aufzählen will. Nähere Informationen bekommt man auf der Homepage. Das OS läuft auf neun verschiedenen Plattformen:

- alpha
- amd64
- i386
- ia64
- pc98
- sparc64
- MIPS
- ppc
- ARM

FreeBSD besitzt heute schon Funktionen im Bereich Netzwerk, Leistungsfähigkeit, Sicherheit und Kompatibilität, die andere Systeme, auch kommerzielle, nicht besitzen. So kann man zum Beispiel durch Kompatibilitäts-Module Programme von anderen Systemen, wie zum Beispiel Linux, SCO UNIX und System V Release 4, auf FreeBSD laufen lassen. Aber auch für die Sicherheit im Netzwerk ist gesorgt, da IPsec und IPv6 unterstützt werden.

Da unter FreeBSD viele Anwendungen laufen, ist es eine gute Alternative zu kommerziellen UNIX® Workstations und kann sowohl für Arbeitsplätze wie auch als Server benutzt werden.

### Daten/Kontakt zum Projekt

Wer weitere Informationen über das Projekt benötigt, erhält diese auf www.freebsd.org. Die Seite ist in vielen Sprachen erhältlich und hat ein gutes Design, durch welches man sich recht schnell auf der Seite fortbewegen kann.

|  |  |  |
| ------------------------------------------------------------------------------- | ---------------- | ----- |
| « [Ausgabe 8](Ausgabe-8 "Ausgabe 8") | **Navigation** |  |

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/6648/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1409/index.html)

<!-- MediaWiki page 1409; revision 6648; parent 6304; 2009-12-28T01:23:10Z -->
