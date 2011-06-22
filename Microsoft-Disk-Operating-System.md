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

## Treiber und TSR-Programme

DOS ist zwar ein Single-Tasking-System, aber dennoch muss neben den aktuell laufenden Programm weiterer Code im Speicher liegen - neben dem [Kernel](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel") selbst sind das vor allem zusätzliche Treiber. DOS kennt dazu das Konzept TSR, *Terminate and Stay Resident*. Ein TSR-Programm beendet sich anders als ein normales Programm über einen besonderen [Systemaufruf](https://github.com/lowlevel-eu/wiki/wiki/Syscall "Systemaufruf"), der einen Teil des Programms auch nach dem Programmende im Speicher belässt.

Der residente Teil des Programms bleibt anschließend solange inaktiv, bis er von anderer Stelle aufgerufen wird. In der Regel geschieht das dadurch, dass das TSR-Programm einen [IVT](https://github.com/lowlevel-eu/wiki/wiki/Interrupt-Vector-Table "IVT")-Eintrag auf seinen residenten Teil umbiegt, so dass es bei einem bestimmten Interruptaufruf zum Zug kommt. Das kann ein Hardwareinterrupt sein oder aber auch ein Softwareinterrupt, der die API des TSR-Programms anderen Anwendungen zur Verfügung stellt - Hardwaretreiber benötigen oft beides.

Es ist auch nicht unüblich, BIOS- oder DOS-Funktionen zu "überladen", indem der passende IVT-Eintrag auf eine Funktion des TSR-Programms geändert wird. Besonders in diesen Fällen wird das TSR-Programm sich den alten IVT-Eintrag merken und den ursprünglichen Interrupthandler aufrufen, sobald es seine Aufgabe erledigt hat (oder wenn es nur eine Unterfunktion des Interrupts ändert). Auf diese Weise können ganze Ketten von Interrupthandlern zu einem einzigen Interrupt entstehen.

## Speicherverwaltung

Der konventionellen Speicher (also die untersten 640 kB die mal für alles reichen sollten) werden als einfach verkettete Liste verwaltet. DOS verwaltet diesen Speicher mit einer Granularität von 16 Bytes, dort Paragraph genannt, und auch mit einem Alignment von 16 Bytes. Vor jedem Speicherblock, egal ob ein belegter oder ein unbelegter, liegt immer ein 16 Byte großer Header der MCB (Memory Control Block). In diesem MCB ist neben einer Markierung vermerkt ob der folgende Block belegt oder frei ist, wem er gehört und wie groß er ist. Über die Größe erkennt man dann wo der nächste MCB liegt. Der letzte Block, dessen Ende normalerweise bei 0x9FFFF ist, wird mit einem Z markiert wogegen alle anderen MCBs mit einem M markiert werden. Die DOS-Speicherverwaltung ist in der Lage freie Blöcke zu teilen um einen neuen Block mit einer bestimmten Größe zu bekommen aber auch nebeneinander liegende freie Blöcke zusammenzufassen. Die Adresse des ersten MCB, der Start der verketteten Liste, bekommt man mit einen undokumentierten Trick über eine Int-21h-Funktion (dieser Trick funktioniert aber unter allen DOS-Versionen und weil er von so vielen Programmen benutzt wird konnte Microsoft ihn auch nicht mehr ändern, er gehört quasi zur offiziellen API dazu). Diese Liste ist in keinster Weise geschützt so das viele DOS-Programme da nach eigenem Gutdünken frei dran rum fummeln.

## Zugriff auf hohen Speicher

Da DOS ein [Real-Mode](https://github.com/lowlevel-eu/wiki/wiki/Real-Mode "Real Mode")-Betriebssystem ist, ist der direkt adressierbare Speicher auf etwa ein Megabyte beschränkt. Da der Bereich zwischen 640 kB und 1 MB für das BIOS und zum Einblenden von Hardware reserviert ist (die *Upper Memory Area*), bleiben für Treiber und Anwendungen 640 kB an *konventionellem Speicher* übrig. Weil das auf Dauer etwas zu wenig war, wurden Methoden eingesetzt, um auch auf die höheren Speicherbereiche zugreifen zu können.

Der Treiber himem.sys stellt gemäß der *Extended Memory Specification* (XMS) den Zugriff auf verschiedene Arten von hohen Speicherbereichen zur Verfügung:

- Die *High Memory Area* (HMA) bezeichnet den 65520 Bytes großen Bereich ab 1 MB (von 0x00100000 bis 0x0010FFEF). Der Zugriff darauf wird ermöglicht, indem das [A20-Gate](https://github.com/lowlevel-eu/wiki/wiki/A20-Gate "A20-Gate") aktiviert wird, so dass der Bereich innerhalb des im Real Mode adressierbaren Bereichs liegt.
- Je nach Hardware freie Speicherbereiche in der *Upper Memory Area* zwischen 640 kB und 1 MB. Die Adressierung im Real Mode stellt hier kein Problem dar. Dieser Service wird aber nicht von himem.sys selber angeboten. Zusätzliche Speichermanager, wie emm386.exe oder umbpci.sys, stellen diesen Service zur Verfügung.
- *Extended Memory Blocks* beginnen nach dem Ende der HMA. Die API erlaubt es, im erweiterten Speicher Blöcke zu reservieren, freizugeben und Daten hinein/heraus zu kopieren (die Speicherverwaltung schaltet dazu kurzzeitig in den [Protected Mode](https://github.com/lowlevel-eu/wiki/wiki/Protected-Mode "Protected Mode")). Eine direkte Adressierung des Speichers ist im Real Mode nicht möglich, so dass die API-Funktion zum Kopieren der Daten in den konventionellen Speicher benutzt werden muss bevor mit dem Inhalt gearbeitet werden kann. Darüber hinaus kann so ein Extended Memory Block auch gelockt werden was ihn in seiner Größe unveränderlich macht aber dafür auch als nicht verschiebbar deklariert. Von einem gelockten EMB bekommt man auch die physische 32Bit-Adresse und kann ihn so für eigene Protected Mode Spielchen benutzen (alle DOS-Extender machen das so wenn sie auf einem DOS-System gestartet werden in dem nur himem.sys aber nicht emm386.exe läuft).

Mit dem *Expanded Memory Specification* (EMS) stellt emm386.exe einen anderen Mechanismus zur Verfügung, um auf Speicher außerhalb der 1 MB-Grenze zuzugreifen. Dazu wird mindestens ein 386er benötigt, denn der Prozessor wird dazu dauerhaft in den 32-Bit-Protected-Mode geschaltet, so dass [Paging](https://github.com/lowlevel-eu/wiki/wiki/Paging "Paging") verfügbar ist und hoher Speicher pageweise in das erste Megabyte des virtuellen Adressraums eingeblendet werden kann. Dadurch wird das bei XMS nötige Kopieren vermieden. Das eigentliche System und alle Programme laufen mit emm386.exe im [VM86](https://github.com/lowlevel-eu/wiki/wiki/Virtual-8086-Mode "VM86")-Modus.  
EMS kann aber auch mit Hilfe spezieller Erweiterungskarten angeboten werden welche einen kleinen Teil ihres eigenen Speichers (der nicht direkt für die CPU erreichbar ist) in den Speicher unterhalb der 1 MB-Grenze einblenden. Diese Erweiterungskarten benötigen dafür einen eigenen Treiber (der das EMS-SW-Interface zur Verfügung stellt) der auf jeder 8086 CPU läuft (also keinen Protected Mode und kein Paging erfordert).

## Weblinks

- [Extended Memory Specification (XMS)](http://www.phatcode.net/res/219/files/xms30.txt)
- [Expanded Memory Specification (EMS)](http://www.phatcode.net/res/218/files/limems40.txt)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/9868/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1829/index.html)

<!-- MediaWiki page 1829; revision 9868; parent 9864; 2011-06-22T10:52:49Z -->
