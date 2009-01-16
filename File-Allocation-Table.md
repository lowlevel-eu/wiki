# File Allocation Table

FAT ist das Filesystem, welches MS-DOS benutzt. Ursprünglich war es für Disketten entwickelt worden. Es gibt drei Varianten:

- FAT12
- FAT16
- FAT32

Der einzige Unterschied zwischen diesen Dateisystemen ist die aufnehmbare Größe.

## Aufbau von FAT

FAT wird in 4 Bereiche unterteilt:

- Reserved Region
- FAT Region
- Root Directory Region (Exirstiert nicht unter FAT32)
- File and Directory Data Region

### Reserved Region

#### Boot Sector und der BIOS Parameter Block(BPB)

In MS-DOS war kein BPB vorhanden. Stattdessen gab es zwei Typen von FAT:

- Single-Sided: Dieser Typ war für einseitige Disketten da
- Double-Sided: Dieser Typ war dagegen für doppelseitige Disketten da.

Ab MS-DOS gab es den BPB, womit jetzt jedes FAT-System diesen braucht. (Die Verbreitung von MS-DOS 1.0 ist sehr gering. Deswegen wird nicht empfohlen, auf diese MS-DOS Version acht zu nehmen) Ursprünglich waren im BPB weniger als 65.536 Sektoren, womit insgesamt 32 MB bei 512-Byte Sektoren benutzt werden konnten. Ab Windows 95 mit den OEM Service Pack 2 wurde FAT32 verwendet. Während FAT16 nur 2 GB adressieren konnte, galt dies für FAT32 nicht.

## siehe auch

- FAT12

## Links

- [FAT32 File System Specification](http://www.microsoft.com/whdc/system/platform/firmware/fatgen.mspx)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/3881/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1643/index.html)

<!-- MediaWiki page 1643; revision 3881; parent 3880; 2009-01-16T18:35:34Z -->
