# Dateisystem

Unter Dateisystemen versteht man eine logische Strukturierung verschiedener Dateien auf einem Speichermedium. Die Art der Strukturierung kann dabei unterschiedlich sein, z.B. in Form eines AVL-Baumes. Moderne Dateisysteme speichern dazu noch weitere Informationen zu Dateien als den bloßen Namen ab, es werden auch Lese/Schreibzugriffe und Berechtigungen gespeichert. Ersteres ist vor allem bei Journaling-Dateisystemen wichtig.

  

## Liste bekannter Dateisysteme

### Dateisysteme für Disketten / sehr kleine bzw. veraltete Festplatten

- [FAT](https://github.com/lowlevel-eu/wiki/wiki/File-Allocation-Table "FAT")
  - [FAT12](https://github.com/lowlevel-eu/wiki/wiki/Ausgabe-4#das-fat12-dateisystem "Ausgabe 4")
  - FAT16
- minix
- [SFS](https://github.com/lowlevel-eu/wiki/wiki/SFS "SFS")

### Dateisysteme für Festplatten

- [FAT](https://github.com/lowlevel-eu/wiki/wiki/File-Allocation-Table "FAT")
  - FAT32
  - VFAT (Erweiterung für lange Dateinamen aller FAT-Dateisysteme)
- [NTFS](https://github.com/lowlevel-eu/wiki/wiki/NTFS "NTFS") (und nicht fertig gewordener Aufsatz WinFS)
- Ext
  - [Ext2](https://github.com/lowlevel-eu/wiki/wiki/Ext2 "Ext2")
  - [Ext3](https://github.com/lowlevel-eu/wiki/wiki/Ext3 "Ext3")
  - [Ext4](https://github.com/lowlevel-eu/wiki/wiki/Ext4 "Ext4")
- ReiserFS
- Reiser4
- UFS
- XFS

### Dateisysteme für CD/DVD

- [ISO9660](https://github.com/lowlevel-eu/wiki/wiki/ISO9660 "ISO9660") (Erweiterungen: [Joliet](https://github.com/lowlevel-eu/wiki/wiki/ISO9660 "ISO9660") von Microsoft und [Rockridge](https://github.com/lowlevel-eu/wiki/wiki/ISO9660#rockridge "ISO9660") für UNIX)
- UDF (Für DVDs)

### Dateisysteme im Netzwerk

- NFS
- SMB/CIFS

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/10540/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1548/index.html)

<!-- MediaWiki page 1548; revision 10540; parent 9464; 2012-03-26T15:10:22Z -->
