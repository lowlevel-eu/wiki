# NTFS

| NTFS |  |
| ---------------------------- | -------------------------------------------------------------------------------------------------------- |
| Entwickler: | Microsoft |
| Vollständige Bezeichnung: | New Technology File System |
| Maximalgröße einer Datei: | Theoretisch 16 EiB, praktisch auf Limitierungen des Betriebssystem beschränkt (XP z.B. maximal 16 TiB) |
| Maximale Dateianzahl: | 4.294.967.295 |
| Länge des Dateinames: | 255 Zeichen |
| Maximale Dateisystemgröße: |  |

**NTFS** steht für **N**ew **T**echnology **F**ile **S**ystem. Das Dateisystem wurde zusammen mit Windows NT eingeführt. Es wird für Festplatten, große USB-Sticks und externe Festplatten benutzt und ist seit Windows XP Service Pack 2 das Standarddateisystem.

## Aufbau von NTFS

### Bootsektor

Der [Bootsektor](https://github.com/lowlevel-eu/wiki/wiki/Bootsektor "Bootsektor") von NTFS sieht ähnlich aus wie der von [FAT](https://github.com/lowlevel-eu/wiki/wiki/File-Allocation-Table "FAT"):

| Offset | Größe | Beschreibung |
| -------- | ------- | ----------------------------------------------------------- |
| 0x000 | 3 | Sprung zum Bootloader \<asm\> EB 52 90 JMP + NOP \</asm\> |
| 0x003 | 8 | Filesystem-ID bei immer "NTFS" |
| 0x00B | 2 | Anzahl Bytes pro Sektor |
| 0x00D | 1 | Anzahl Sektoren pro Cluster |
| 0x00E | 7 | Reserviert immer 00 00 00 00 00 00 00 |
| 0x015 | 1 | Media Descriptor Byte 0xF8 bei Hard Disk |
| 0x016 | 2 | Reserviert immer 00 00 |
| 0x018 | 2 | Anzahl Sektoren pro Spur |
| 0x01A | 2 | Anzahl Lese-/Schreibköpfe (Oberflächen) |
| 0x01C | 8 | Reserviert immer 00 00 00 00 00 00 00 00 |
| 0x024 | 4 | Reserviert 80 00 80 00 (Ausnahme?) |
| 0x028 | 8 | Gesamtzahl Sektoren im Logischen Laufwerk |
| 0x030 | 8 | Logische Clusternummer des ersten MFT-Clusters |
| 0x038 | 8 | Logische Clusternummer des ersten MFTBackup-Clusters |
| 0x040 | 4 | Anzahl Cluster pro MFT (0xF6 = 1/4) |
| 0x044 | 4 | Anzahl Cluster pro Index record |
| 0x048 | 8 | Seriennummer des Logischen Laufwerks |
| 0x050 | 4 | Reserviert immer 00 00 00 00 |
| 0x054 | 426 | Bootloader oder 1.Stagebootloader |
| 0x1FE | 2 | Kennung für Bootsektoren immer \<asm\>55 AA \</asm\> |

## Weblinks

[ntfs-g3-Projekt, bietet Lese- und Schreibmöglichkeiten unter Linux für NTFS](http://www.ntfs-3g.org/)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/9901/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2437/index.html)

<!-- MediaWiki page 2437; revision 9901; parent 9900; 2011-07-03T10:48:35Z -->
