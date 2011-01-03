# Microsoft Disk Operating System

| MS-DOS |  |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
|  |  |
| Entwickler: | Microsoft |
| Akt. Version: | 8.0 (Windows ME) |
| [Lizenz](https://github.com/lowlevel-eu/wiki/wiki/Lizenzen "Lizenzen"): | Proprietär |
| OS-Eigenschaften |  |
| Plattform: | [x86](https://github.com/lowlevel-eu/wiki/wiki/X86 "X86") |
| [Kernelart](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel"): | [Monolith](https://github.com/lowlevel-eu/wiki/wiki/Kernel#monolithischer-kernel "Monolithischer Kernel") |
| [Sprache](https://lowlevel-eu.github.io/wiki/pages/1648/index.html "Kategorie:Programmiersprache"): | Assembler, C |
| API: | u.a. int 21h |
| Binärformat: | COM, [MZ EXE](https://github.com/lowlevel-eu/wiki/wiki/MZ-EXE "MZ EXE") |
| [IPC-Methode](https://github.com/lowlevel-eu/wiki/wiki/Interprozesskommunikation "IPC"): | \- |
| Homepage |  |

  
**MS-DOS** (Microsoft Disk Operating System) ist eines der ersten Betriebssysteme für [x86](https://github.com/lowlevel-eu/wiki/wiki/X86 "X86")-PCs. DOS war in den späten 1980ern das dominierende Betriebssystem für Ein-Benutzer-Rechner. Heute ist DOS nicht mehr erhältlich. Stattdessen gibt es Betriebssysteme wie FreeDOS oder andere Abstammungen von MS-DOS.

Die ursprüngiche Codebasis von [Windows](https://github.com/lowlevel-eu/wiki/wiki/Windows "Windows") (Windows 1.x bis Windows ME) waren lediglich ein grafischer Betriebssystemaufsatz für MS-DOS, auch wenn MS-DOS seit Windows 95 (MS-DOS 7.0) nicht mehr einzeln verkauft wurde. Beim NT-Kernel, der von allen neueren Windows-Versionen benutzt wird, änderte sich das aber: Der [NT](https://github.com/lowlevel-eu/wiki/wiki/Windows "NT")-[Kernel](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel") wurde komplett neu entwickelt und konnte DOS-Anwendungen nicht mehr oder nur mit Problemen starten. Ab diesem Zeitpunkt wurden immer häufiger Emulatoren wie z.B. DOS-Box eingesetzt, um diese Programme dennoch starten zu können.

## Zugriff auf hohen Speicher

Da DOS ein [Real-Mode](https://github.com/lowlevel-eu/wiki/wiki/Real-Mode "Real Mode")-Betriebssystem ist, ist der direkt adressierbare Speicher auf etwa ein Megabyte beschränkt. Da der Bereich zwischen 640 kB und 1 MB für das BIOS und zum Einblenden von Hardware reserviert ist (die *Upper Memory Area*), bleiben für Treiber und Anwendungen 640 kB an *konventionellem Speicher* übrig. Weil das auf Dauer etwas zu wenig war, wurden Methoden eingesetzt, um auch auf die höheren Speicherbereiche zugreifen zu können.

Der Treiber himem.sys stellt gemäß der *Extended Memory Specification* den Zugriff auf verschiedene Arten von hohen Speicherbereichen zur Verfügung:

- Die *High Memory Area* (HMA) bezeichnet den 65520 Bytes großen Bereich ab 1 MB. Der Zugriff darauf wird ermöglicht, indem das [A20-Gate](https://github.com/lowlevel-eu/wiki/wiki/A20-Gate "A20-Gate") aktiviert wird, so dass der Bereich innerhalb des im Real Mode adressierbaren Bereichs liegt.
- Je nach Hardware freie Speichbereiche in der *Upper Memory Area* zwischen 640 kB und 1 MB. Die Adressierung im Real Mode stellt hier kein Problem dar.
- *Extended Memory Blocks* beginnen nach dem Ende der HMA. Die API erlaubt es, im erweiterten Speicher Blöcke zu reservieren, freizugeben und zu kopieren (die Speicherverwaltung schaltet dazu kurzzeitig in den [Protected Mode](https://github.com/lowlevel-eu/wiki/wiki/Protected-Mode "Protected Mode")). Eine direkte Adressierung des Speichers ist im Real Mode nicht möglich, so dass die API-Funktion zum Kopieren des Blocks in den konventionellen Speicher benutzt werden muss bevor mit dem Inhalt gearbeitet werden kann.

Mit dem *Expanded Memory* stellt emm386.exe einen anderen Mechanismus zur Verfügung, um auf hohen Speicher zuzugreifen. Dazu wird mindestens ein 386er benötigt, denn der Prozessor wird dazu dauerhaft in den 32-Bit-Protected-Mode geschaltet, so dass [Paging](https://github.com/lowlevel-eu/wiki/wiki/Paging "Paging") verfügbar ist und hoher Speicher in das erste Megabyte des virtuellen Adressraums eingeblendet werden kann. Dadurch wird das bei XMS nötige Kopieren vermieden. Das eigentliche System und alle Programme laufen mit emm386.exe im [VM86](https://github.com/lowlevel-eu/wiki/wiki/Virtual-8086-Mode "VM86")-Modus.

## Weblinks

- [Extended Memory Specification (XMS)](http://www.phatcode.net/res/219/files/xms30.txt)
- [Expanded Memory Specification (EMS)](http://www.phatcode.net/res/218/files/limems40.txt)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/9233/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1829/index.html)

<!-- MediaWiki page 1829; revision 9233; parent 5301; 2011-01-03T12:13:30Z -->
