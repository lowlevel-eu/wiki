# File Allocation Table

Diese Seite ist ein Artikel, welcher **mehr** haben könnte..  

Wenn du mehr darüber weißt oder recherchieren willst, bist **du** aufgerufen, dies zu tun. Wenn du dir in einer Sache nicht sicher bist, dann stell es auf die Diskussionsseite.

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

| Offset | Name | Boot Sector oder BPB? | Funktion | Größe |
| -------- | --------- | ----------------------- | ------------------------------------------------------- | ------- |
| 0 | jmpBoot | Boot Sector | Enthält Instruktion zum Überspringen des Bootsektors. | 2 |

(*Wird noch erweitert*)

## Siehe auch

- FAT12

## Links

- [FAT32 File System Specification](http://www.microsoft.com/whdc/system/platform/firmware/fatgen.mspx)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/4066/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1643/index.html)

<!-- MediaWiki page 1643; revision 4066; parent 3883; 2009-02-26T18:54:12Z -->
