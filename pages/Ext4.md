# Ext4

Diese Seite ist ein Artikel, welcher **mehr** haben könnte..  

Wenn du mehr darüber weißt oder recherchieren willst, bist **du** aufgerufen, dies zu tun. Wenn du dir in einer Sache nicht sicher bist, dann stell es auf die Diskussionsseite.

| ext4 |  |
| ---------------------------- | ------------------------------------------------------------------------------- |
| Entwickler: | Mingming Cao, Dave Kleikamp, Alex Tomas, Theodore Ts'o und weitere |
| Vollständige Bezeichnung: | Fourth extended file system |
| Maximalgröße einer Datei: | Größe des Dateisystems |
| Maximale Dateianzahl: | Variabel |
| Länge des Dateinames: | 256 Byte |
| Maximale Dateisystemgröße: | 1 EiB, aufgrund einer Beschränkung in e2fsprogs allerdings nur maximal 16 TiB |

Das Fourth extended file system oder kurz **ext4** ist die Weiterentwicklung von [ext3](Ext3 "Ext3"). Es ist seit dem Linux-Kernel 2.6.19 Bestandteil selbiges und heutzutage das Standarddateisystem unter Linux. Es hat die gleiche Partitionskennung wie ext3 (0x83 bzw. EBD0A0A2-B9E5-4433-87C0-68B6B72699C7 nach GPT).

  

## Neuerungen gegenüber ext3

Die wichtigste Neuerung von ext4 gegenüber ext3 ist, dass das Dateisystem jetzt auch Extents statt Blocktabellen benutzen kann. Das bedeutet, dass die Zuordnung nicht in Blöcken fester Größe geschieht, sondern in variablen Extents, deren Beschreibung eine Anzahl von Blöcken enthält, die auf der Platte direkt hintereinander liegen. Besonders bei großen Dateien können so die Metadaten verkleinert und damit die Performance verbessert werden.

Weitere Neuerungen sind Zeitstempel auf Nanosekunden-Basis, Journal mit Prüfsummenunterstützung (einschaltbar beim Mounten via journal_checksum), Mehrfache Preallokation von Dateiblöcken und Inodes sowie Zeitverzögerte Allokation von Dateiblöcken und Inodes.

## Weblinks

- [Dokumentation zu ext4](https://git.kernel.org/cgit/linux/kernel/git/torvalds/linux.git/tree/Documentation/filesystems/ext4.txt)
- [ext4 On-Disk-Layout](https://ext4.wiki.kernel.org/index.php/Ext4_Disk_Layout)
- [ext4-Wiki](https://ext4.wiki.kernel.org/index.php/Main_Page)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/11139/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2438/index.html)

<!-- MediaWiki page 2438; revision 11139; parent 11044; 2013-08-30T11:57:53Z -->
