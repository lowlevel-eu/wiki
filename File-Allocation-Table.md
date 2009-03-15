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

In MS-DOS 1.0 war kein BPB vorhanden. Stattdessen gab es zwei Typen von FAT:

- Single-Sided: Dieser Typ war für einseitige Disketten da
- Double-Sided: Dieser Typ war dagegen für doppelseitige Disketten da.

Ab MS-DOS gab es den BPB, womit jetzt jedes FAT-System diesen braucht. (Die Verbreitung von MS-DOS 1.0 ist sehr gering. Deswegen wird nicht empfohlen, auf diese MS-DOS Version acht zu nehmen) Ursprünglich waren im BPB weniger als 65.536 Sektoren, womit insgesamt 32 MB bei 512-Byte Sektoren benutzt werden konnten. Ab Windows 95 mit den OEM Service Pack 2 wurde FAT32 verwendet. Während FAT16 nur 2 GB adressieren konnte, galt dies für FAT32 nicht.

| Bezeichnung | Offset | Bytes | Erklärung |
| ------------- | -------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| JmpBoot | 0 | 3 | Hier steht ein JMP-Befehl zum Ende der Tabelle. |
| OSName | 3 | 8 | Hier steht ein 8-Buchstaben-String, der angibt, unter welchen Betriebssystem die Diskette formatiert wurde. Unter Windows sollte dort "MSWIN4.1" stehen. Man kann hier aber eigentlich schreiben, was man möchte. Es hat auf das Dateisystem keinen Einfluss. |
| BytesPerSec | 11 | 2 | Die Anzahl Bytes, die in einem Sektor vorhanden sind. Bei einer Diskette entspricht dies 512. Dieser Wert ist fest und kann ohne weiteres auch nicht geändert werden und sollte daher auch immer hier eingetragen werden. |
| SecPerClus | 13 | 1 | Die Anzahl Sektoren, die zu einem Cluster zusammengefasst werden. Was ein Cluster ist, erkläre ich weiter unten. Hier sei vorerst nur wichtig, das auf einer Diskette exakt EIN Sektor in einem Cluster ist. Also hier den Wert 1 eintragen. |
| RsvdSecCnt | 14 | 2 | Die Anzahl der Reservierten Sektoren. Der Boot Sector, in dem wir uns gerade befinden, ist ein reservierter Sektor. Da man in der Regel nur diesen reservierten Sektor benötigt, trägt man hier 1 ein. |
| NumFATs | 16 | 1 | Die Anzahl der FAT-Tabellen. Aus Redundanzgründen speichert man meistens 2 FAT-Tabellen auf der Diskette, im Falle, dass eine davon beschädigt sein sollte. Daher hier den Wert 2 eintragen. |
| RootEntCnt | 17 | 2 | Die Anzahl der möglichen Einträge ins Root-Directory. Wozu dieser Wert genau dient, erkläre ich im Abschnitt über das Root-Directory. Der Standartwert hier ist 224. |
| TotSec | 19 | 2 | Die Anzahl aller Sektoren, die auf der Diskette vorhanden sind. Bei einer 3,5" 1,44 MB-Diskette sind das 2880 Sektoren. 1,44 MB sind 1440 KB (die Hersteller multiplizieren immer mit 1000 und nicht 1024). 1440 KB sind 1474560 Bytes (diesmal mal 1024). 147560 Bytes geteilt durch 512 Bytes (1 Sektor) ergibt 2880 Sektoren. |
| MediaType | 21 | 1 | Hier wird der Wert eingetragen, anhand dem erkannt wird, um was für einen Typ es sich bei diesem Datenträger handelt. 0xF0 ist der Wert für Diskette. |
| FATSize | 22 | 2 | Hier steht die Anzahl der Sektoren, die eine FAT-Tabelle belegt (man erinnere, es gibt meistens ZWEI). Der Wert bei einer 1,44 MB-Diskette ist 9. Wie man auf den Wert kommt, erläutere ich im Abschnitt über die FAT-Tabelle.<br> |
| SecPerTrack | 24 | 2 | Die Anzahl der Sektoren pro Track. Track wird auch als Cylinder bezeichnet. Dieser Wert ist für den Interrupt 13h wichtig, da dieser die Sektoren über CHS adressiert. Der Wert für eine 1,44 MB Diskette ist 18. |
| NumHeads | 26 | 2 | Die Anzahl der Köpfe. Auch diese Angabe wird vom Interrupt 13h benötigt, um die Sektoren nach CHS adressieren zu können. Bei einer 1,44 MB-Diskette ist der Wert 2. |
| HiddenSec | 28 | 4 | Die Anzahl der versteckten Sektoren. Wozu es nützlich wäre, versteckte Sektoren zu haben, weiß ich im Moment nicht, weshalb man hier den Wert 0 eintragen sollte. |
| TotSec32 | 32 | 4 | Dieser Eintrag ist nur für einen FAT32-formatierten Datenträger wichtig. Da wir uns aber auf FAT12 konzentrieren, tragen wir hier 0 ein. |
| DrvNum | 36 | 1 | Dieser Wert wird ebenfalls von Interrupt 13h benötigt und gibt Auskunft darüber um welches Laufwerk es sich handelt. Für Diskette tragen wir hier 0x00 ein. |
| Reserved | 37 | 1 | Dieser Eintrag ist für Windows NT reserviert und sollte mit dem Wert 0 beschrieben werden (auch wenn man WindowsNT/2000/XP benutzt). |
| VolumeID | 39 | 4 | Hier kann man eine Seriennummer angeben anhand deren man die Diskette beim Einlesen erkennen kann. Dieser Wert wird meistens aus der Zusammenfassung der beiden 16-BIT-Werte von Datum und Zeit gemacht. Wie man Datum und Zeit in 16 BIT speichert, erkläre ich weiter unten. |
| FileSysType | 54 | 8 | Dämlicherweise soll man hier angeben, welches FAT-Dateisystem man auf dem Datenträger verwendet. Dämlicherweise deshalb, weil dieser Eintrag nicht dazu verwendet wird, um festzustellen welches FAT-System man nun benutzt hat. Aus Gründen der Kompatibilität sollte man hier einfach "FAT12" eintragen und die restlichen Bytes mit 0x20 (Leerzeichen) füllen. Wie man exakt bestimmt, welches FAT-System denn nun auf dem Datenträger verwendet wird erläutere ich weiter unten. |

#### FAT-Tabelle

(*Wird noch erweitert*)

## Siehe auch

- FAT12

## Links

- [FAT32 File System Specification](http://www.microsoft.com/whdc/system/platform/firmware/fatgen.mspx)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/4128/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1643/index.html)

<!-- MediaWiki page 1643; revision 4128; parent 4127; 2009-03-15T14:15:56Z -->
