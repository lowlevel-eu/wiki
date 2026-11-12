# ARM-OS-Dev Teil 7 – Physische Speicherverwaltung

|  |  |  |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| « [ARM-OS-Dev Teil 6 – Multitasking](ARM-OS-Dev-Teil-6-%E2%80%93-Multitasking.md "ARM-OS-Dev Teil 6 – Multitasking") | **Navigation** | [ARM-OS-Dev Teil 8 – Ein erstes Programm](ARM-OS-Dev-Teil-8-%E2%80%93-Ein-erstes-Programm.md "ARM-OS-Dev Teil 8 – Ein erstes Programm") » |

Die Verwaltung des physischen Speichers ist im Grunde genommen plattformunabhängig, daher kann im Großen und Ganzen für dieses Thema auf die [x86-Reihe](Teil-7-Physische-Speicherverwaltung.md "Teil 7 - Physische Speicherverwaltung") verwiesen werden. Unterschiede gibt es lediglich bei der Initialisierung der Speicherverwaltung.

## Initialisierung

Zunächst einmal kann man zwar wieder eine Bitmap mit 1M Bits erstellen, muss es aber nicht. Denn im Unterschied zur x86-Plattform ist die Speicheraufteilung auf I/CP-Boards ziemlich genau festgelegt: Es gibt 128 MB Speicher, von denen das erste Megabyte Mappings des Flashspeichers enthält. Somit brauchen wir keine Bitmap, die 4 GB verwalten kann, sondern nur eine für ein Zweiunddreißigstel (128 MB), also können wir BITMAP_SIZE hier als 1024 definieren.

Im Unterschied zu x86 haben wir auch keinen Bootloader, der uns eine Art Karte des physischen Speichers übergibt. Dafür kennen wir die Aufteilung auch so ganz genau – wie gerade beschrieben können wir den gesamten Speicher nach dem ersten Megabyte frei nutzen. Die *pmm_init*-Funktion braucht also nichts zu tun, als alle Einträge ab 0x00100000 als frei zu kennzeichnen.

## Weitere Quellen

Der fertige Code für diesen Teil des Tutorials befindet sich [hier](https://gitorious.org/arm-os-dev/kernel/trees/4998e6d9f4b8a60489fc4fd69820aa071f6ba52a).

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/9788/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2426/index.html)

<!-- MediaWiki page 2426; revision 9788; parent 0; 2011-05-14T14:11:26Z -->
