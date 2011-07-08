# Ext2

Diese Seite ist ein Artikel, welcher **mehr** haben könnte..  

Wenn du mehr darüber weißt oder recherchieren willst, bist **du** aufgerufen, dies zu tun. Wenn du dir in einer Sache nicht sicher bist, dann stell es auf die Diskussionsseite.

| ext2 |  |
| ---------------------------- | ----------------------------- |
| Entwickler: | Rémy Card |
| Vollständige Bezeichnung: | Second extended file system |
| Maximalgröße einer Datei: | 2 TiB |
| Maximale Dateianzahl: | 10<sup>18</sup> |
| Länge des Dateinames: | 255 Byte |
| Maximale Dateisystemgröße: | 16 TiB |

Das ext2-Dateisystem (ext steht für extended) war bis vor ein paar Jahren das Standarddateisystem unter Linux und anderen Unix-Derivaten, bis es durch [ext3](https://github.com/lowlevel-eu/wiki/wiki/Ext3 "Ext3") oder andere Journaling-Dateisysteme ersetzt wurde.

## Aufbau

### Superblock

An einem Offset von 1024 Bytes vom Anfang des Mediums. Er beinhaltet alle Informationen, die das ganze Dateisystem betreffen, wie zum Beispiel die Anzahl der Blocks die verfügbar und reserviert sind. Weiter ist auch ein Feld für eine Magic-Number um festzustellen, ob es sich wirklich um ein ext2-Dateisystem und wenn ja, um welche Version es sich handelt.

# Links

- [Design and Implementation of the Second Extended Filesystem](http://web.mit.edu/tytso/www/linux/ext2intro.html)
- [The Second Extended File System](http://www.nongnu.org/ext2-doc/ext2.html)
- [libext2 aus týndur](http://git.tyndur.org/?p=libext2.git;a=summary)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/9912/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1617/index.html)

<!-- MediaWiki page 1617; revision 9912; parent 9904; 2011-07-08T21:45:54Z -->
