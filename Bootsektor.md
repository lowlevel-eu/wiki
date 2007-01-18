# Bootsektor

Als Bootsektor bezeichnet man den Sektor von einem Datenträger oder Laufwerk, der vom [BIOS](https://github.com/lowlevel-eu/wiki/wiki/Basic-Input-Output-System "BIOS") während des Bootprozesses eingelesen und ausgeführt wird. Aufgabe des Bootsektors ist es, das Betriebsystem oder einen [Bootloader](https://github.com/lowlevel-eu/wiki/wiki/Bootloader "Bootloader") zu laden.

Der Bootsektor ist in der Regel 512 Byte groß und endet mit der Magic Number 0xAA55, anhand der das [BIOS](https://github.com/lowlevel-eu/wiki/wiki/Basic-Input-Output-System "BIOS") den Sektor als gültigen Bootsektor erkennt. Bei Disketten befindet sich der Bootsektor im erste Sektor des Datenträgers. Bei Festplatten im erste Sektor der bootfähigen Partition des Datenträgers. Der erste Sektor einer Festplatte hingegen heißt [Master Boot Record](https://github.com/lowlevel-eu/wiki/wiki/Master-Boot-Record "Master Boot Record").

Der Bootsektor wird oft auch **Boot Record** genannt.

## Bootsektor Tutorials

Eigener Boot Record

[Ausgabe 1](https://github.com/lowlevel-eu/wiki/wiki/Ausgabe-1 "Ausgabe 1") OS Dev-Tutorial, Teil 1

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/1733/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1475/index.html)

<!-- MediaWiki page 1475; revision 1733; parent 1729; 2007-01-18T19:46:44Z -->
