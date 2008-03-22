# Ext2

Das ext2-Dateisystem (ext steht für extended) war bis vor ein paar Jahren das Standarddateisystem unter Linux und anderen Unix-Derivaten, bis es durch ext3 oder andere Journaling-Dateisysteme ersetzt wurde.

# Aufbau

## Superblock

An einem Offset von 1024 Bytes vom Anfang des Mediums. Er beinhaltet alle Informationen, die das ganze Dateisystem betreffen, wie zum Beispiel die Anzahl der Blocks die verfügbar und reserviert sind. Weiter ist auch ein Feld für eine Magic-Number um festzustellen, ob es sich wirklich um ein ext2-Dateisystem und wenn ja, um welche Version es sich handelt.

# Links

[Design and Implementation of the Second Extended Filesystem](http://web.mit.edu/tytso/www/linux/ext2intro.html) [The Second Extended File System](http://www.nongnu.org/ext2-doc/ext2.html)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/2648/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1617/index.html)

<!-- MediaWiki page 1617; revision 2648; parent 2626; 2008-03-22T11:01:21Z -->
