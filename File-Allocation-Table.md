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

## siehe auch

- FAT12

## Links

- [FAT32 File System Specification](http://www.microsoft.com/whdc/system/platform/firmware/fatgen.mspx)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/3880/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1643/index.html)

<!-- MediaWiki page 1643; revision 3880; parent 3879; 2009-01-16T18:24:30Z -->
