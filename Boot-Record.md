# Boot Record

Als Boot Record bezeichnet man den Sektor der vom [BIOS](https://github.com/lowlevel-eu/wiki/wiki/Basic-Input-Output-System "BIOS") während des Bootprocesses eingelesen und ausgeführt wird. Aufgabe des Boot Record ist es das Betriebsystem oder einen Boot Loader zu laden.

Der Boot Record ist in der Regel 512 Byte groß. Und endet mit der Magic Number 0x55AA, anhand der das [BIOS](https://github.com/lowlevel-eu/wiki/wiki/Basic-Input-Output-System "BIOS") den Sektor als gültigen Boot Record erkennt. Bei Disketten befindet sich der Boot Record im erste Sektor des Datenträgers. Bei Festplatten im erste Sektor der bootfähigen Partition des Datenträgers.

Der erste Sektor einer Festplatte hingegen heißt [Master Boot Record](https://github.com/lowlevel-eu/wiki/wiki/Master-Boot-Record "Master Boot Record").

  

## Boot Record Tutorials

Boot Record I

[Ausgabe 1](https://github.com/lowlevel-eu/wiki/wiki/Ausgabe-1 "Ausgabe 1") OS Dev-Tutorial, Teil 1

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/1495/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1426/index.html)

<!-- MediaWiki page 1426; revision 1495; parent 1494; 2006-09-16T18:22:24Z -->
