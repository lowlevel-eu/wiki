# Ext3

Diese Seite ist ein Artikel, welcher **mehr** haben könnte..  

Wenn du mehr darüber weißt oder recherchieren willst, bist **du** aufgerufen, dies zu tun. Wenn du dir in einer Sache nicht sicher bist, dann stell es auf die Diskussionsseite.

| ext3 |  |
| ---------------------------- | ---------------------------- |
| Entwickler: | Verschiedene |
| Vollständige Bezeichnung: | Third extended file system |
| Maximalgröße einer Datei: | 2 TiB |
| Maximale Dateianzahl: | Variabel |
| Länge des Dateinames: | 255 Byte |
| Maximale Dateisystemgröße: | 32 TiB |

Das ext3-Dateisystem ist die Weiterentwicklung des ext2-Dateisystems. Im Gegensatz zu ext2 hat ext3 ein Journal. Der Dateisystemtreiber speichert dann vor einer Änderung am Dateisystem je nach Konfiguration mehr oder weniger viele Informationen dazu im Journal. Wenn nun ein Absturz stattfindet, so muss danach das Dateisystem nicht vollständig geprüft werden, außerdem ist somit die Konsistenz des Dateisystems garantiert.

Das [ext4](https://github.com/lowlevel-eu/wiki/wiki/Ext4 "Ext4")-Dateisystem ist die Weiterentwicklung von ext3.

## Erkennen eines ext3 Dateisystems

Ein ext3-Dateisystem ist eigentlich ein ext2-Dateisystem mit einer Erweiterung. Deshalb kann ein ext2-Treiber theoretisch auch ein ext3-Dateisystem benutzen. Deshalb ist sowohl die Kennung in der [Partitionstabelle](https://github.com/lowlevel-eu/wiki/wiki/Master-Boot-Record#partitionstabelle "MBR") (0x83) als auch die Magic number (0xEF53) im Superblock identisch. Man kann ein ext3-Dateisystem allerdings an den Compatible Features Flags (Bytes 92-95 im Superblock) erkennen. 0x0004 bedeutet dort, dass es sich um ein ext3-Dateisystem handelt.

## Siehe auch

- [Dateisystem](https://github.com/lowlevel-eu/wiki/wiki/Dateisystem "Dateisystem")
- [ext2](https://github.com/lowlevel-eu/wiki/wiki/Ext2 "Ext2")

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/11043/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1660/index.html)

<!-- MediaWiki page 1660; revision 11043; parent 9913; 2013-03-18T16:56:15Z -->
