# Bootsektor

Als **Bootsektor** oder auch **Boot Record** bezeichnet man den Sektor eines Datenträgers oder Laufwerks, der vom [BIOS](https://github.com/lowlevel-eu/wiki/wiki/Basic-Input-Output-System "BIOS") während des Bootprozesses eingelesen und ausgeführt wird. Aufgabe des Bootsektors ist es das [Betriebssystem](https://github.com/lowlevel-eu/wiki/wiki/Betriebssystem "Betriebssystem") oder einen [Bootloader](https://github.com/lowlevel-eu/wiki/wiki/Bootloader "Bootloader") zu laden.

Der Bootsektor ist in der Regel 512 Byte groß und endet mit der Magic Number 0xAA55, anhand der das [BIOS](https://github.com/lowlevel-eu/wiki/wiki/Basic-Input-Output-System "BIOS") den Sektor als gültigen Bootsektor erkennt. Bei Disketten befindet sich der Bootsektor im ersten Sektor des Datenträgers. Bei Festplatten im ersten Sektor der bootfähigen Partition des Datenträgers. Der erste Sektor einer Festplatte hingegen heißt [Master Boot Record](https://github.com/lowlevel-eu/wiki/wiki/Master-Boot-Record "Master Boot Record").

## siehe auch

- [Eigener Bootloader](https://github.com/lowlevel-eu/wiki/wiki/Eigener-Bootloader "Eigener Bootloader")
- [Ausgabe 1 (4.3 Unser Bootloader)](https://github.com/lowlevel-eu/wiki/wiki/Ausgabe-1#unser-bootloader "Ausgabe 1")

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/9011/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1475/index.html)

<!-- MediaWiki page 1475; revision 9011; parent 3448; 2010-11-28T13:32:13Z -->
