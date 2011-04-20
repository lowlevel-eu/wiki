# Master Boot Record

Der **Master Boot Record** (MBR) ist der erste Sektor einer Festplatte. Die Aufgabe des MBR ist es, die Partitionen zu definieren und den [Bootsektor](https://github.com/lowlevel-eu/wiki/wiki/Bootsektor "Bootsektor") einer bootbaren Partition zu laden und zu starten.

Die Sektorennummer des MBR anhand der zwei Addressierungsmöglichkeiten:

    LBA : 0x00000000
    CHS : Cylinder: 0, Head: 0, Sector: 1

## Aufbau

| Offset | Bedeutung |
| --------------- | -------------------------------- |
| 0x0000-0x01BD | Code zum Laden einer Partition |
| 0x01BE-0x01FD | Partitionstabelle |
| 0x01FE-0x01FF | Bootsignatur 0xAA55 |

## Partitionstabelle

Die Partitionstabelle besteht aus 4 Einträgen à 16 Byte in folgendem Format:

| Offset | Größe | Bedeutung |
| -------- | ------- | --------------------------------------------------------------------------------- |
| 0x0 | DB | Bootflag<br>• 0x00 nicht bootbar<br>• 0x80 bootbare Partition<br> |
| 0x1 | DB | Kopf an dem die Partition anfängt |
| 0x2 | DB | • Bit 0-5 -\> Anfangs Sektor<br>• Bit 6-7 -\> Bit 8-9 des Anfangs-Zylinders<br> |
| 0x3 | DB | Bit 0-7 des Anfangs-Zylinders |
| 0x4 | DB | Gibt den Partitions Typ an |
| 0x5 | DB | Kopf an dem die Partition endet |
| 0x6 | DB | • Bit 0-5 -\> Letzter Sektor<br>• Bit 6-7 -\> Bit 8-9 des letzten Zylinders<br> |
| 0x7 | DB | Bit 0-7 des letzten Zylinders |
| 0x8 | DD | LBA (Logical Block Addressing) Nummer des Ersten Sektors |
| 0xC | DD | Länge der Partition in Sektoren |

## Übereinkünfte

Bei dem MBR muss man beachten, das er 'über' den Betriebssystemen steht, da ja eine Partitionierte Festplatte durchaus mehrere verschiedene Betriebssystem auf den Partitionen enthalten kann. Beim Anlegen eines MBRs muss darauf Rücksicht genommen werden, dass gewisse Übereinkünfte eingehalten werden, um die Partitionstabelle für andere Betriebssysteme lesbar zu halten ihre Partitionen nicht zu beschädigen, reservierte Sektoren frei zu Halten und Partitionsgranzen korrekt zu setzten.

Es ist zu beachten, das die ATA-Übereinkünfte variieren je nachdem ob die Festplatte (nativ) durch LBA oder CHS adressiert wird.

### Versteckte (reservierte Sektoren)

Vor der ersten Partition müssen sich versteckte Sektoren befinden, die zu keiner Partition gehören. Der erste davon enthält den MBR selbst, die anderen sind für erweiterungen reserviert. ( eine Erweiterung, die gerade im kommen ist, ist das *Extendet Firmware Interface*([EFI](https://github.com/lowlevel-eu/wiki/wiki/Unified-Extensible-Firmware-Interface "EFI")), eine erweiterung zum MBR, die langsam nötig wird, da für neue Festplatten, die 48bit LBA nutzen, das 32bit Feld des Normalen LBA nicht ausreicht. Weiterhin könnten auch Bootmanager oder Präboot-Treiber in den Verteckten Sektoren sein.

Die Anzahl der verstecketen Sektoren beträgt:

- bei **CHS**-Adressierung **eine Spur**
- bei **LBA**-Adressierung **64 (40h) Sektoren** (was übrigens auch der virtuellen Spur der durch int 13h emulierten CHS-adressierung entspricht)

### Partitionsgrenzen

Partitionen dürfen nicht an beliebigen Sektoren beginnen. Diese Übereinkunft hängt bei der CHS-Adressierung damit zu sammen, dass immer ganze Spuren formatiert werden müssen, und bei der LBA-Adresseirung, sorgt sie für bessere Übersicht, und bessere Nutzung des Festplattencaches.

Die Partitionsgrenzen sollten ...

- bei **CHS**-Adressierung auf ganzzahligen **ganze Spuren** liegen
- bei **LBA**-Adressierung **auf** ganzzahligen Megabytes n\*100000h **liegen**

### Nur eine Bootfähige Partition

Der Standart MBR prüft alle Partitionen auf Bootfähigkeit. Wenn mehrere Partitionen Bootfähig sind, bricht er mit der Meldung "Ungültige Partitionstabelle" ab. Es darf also nur eine Bootfähig sein. Es ist durchaus möglich einfach einen anderen Code einzufügen, der sich anders verhält, doch dann muss man bedenken, das ein anderes Betriebssystem den MBR-Code möglicherweise wieder durch einen Standartkonformen ersetzt, und dann die Tabelle als ungültig erkannt wird.

### Verhalten des MBRcodes

- Stack setzten
- sich selbst nach 0000h:0600h kopieren, und dort weitermachen (jmp far)
- die ersten Bytes der Partitionen auf 80h prüfen.
- wenn keine Bootfähig, dann int 18h aufrufen (Das BIOS wird dann entweder das nächste Laufwerk booten, eine Fehlermeldung ausgeben oder den ROM-BASIC-Interpreter Starten)
- wenn mehrere Bootfähig, Abbruch mit Fehlermeldung
- wenn eine Bootfähig den ersten Sektor der Partition laden.
  - Wenn er per CHS erreichbar ist CHS verwenden.
  - Wenn nicht LBA verwenden
- wenn Fehler Laufwerk justieren und nochmal versuchen
- 0000h:7DFEh auf Signatur 55h,0AAh prüfen
- wenn nicht vorhanden Laufwerk justieren und nochmal versuchen
- wenn immer noch nicht vorhanden Abbruch mit Fehlermeldung, (oder ggf. eigene Erweiterung verwenden (z.b. hohe bits der LBA in obsolete CHS Felder))
- ES:DI auf den Partitionseintrag der Partition setzten
- DL wieder auf BIOS-Nummer des physischen Laufwerks setzten
- den geladenen Sektor anspringen (jmp 0000h:7C00h)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/9695/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1431/index.html)

<!-- MediaWiki page 1431; revision 9695; parent 6317; 2011-04-20T21:14:28Z -->
