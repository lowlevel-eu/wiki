# PrettyOS

| PrettyOS |  |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
|  |  |
| Entwickler: | [ehenkes](https://lowlevel-eu.github.io/wiki/pages/2274/index.html "Benutzer:Ehenkes") |
| Akt. Version: |  |
| [Lizenz](https://github.com/lowlevel-eu/wiki/wiki/Lizenzen "Lizenzen"): | 2-Klausel-BSD |
| OS-Eigenschaften |  |
| Plattform: | [i386](https://github.com/lowlevel-eu/wiki/wiki/X86 "X86") |
| [Kernelart](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel"): | [Monolith](https://github.com/lowlevel-eu/wiki/wiki/Kernel#monolithischer-kernel "Monolithischer Kernel") |
| [Sprache](https://lowlevel-eu.github.io/wiki/pages/1648/index.html "Kategorie:Programmiersprache"): | C, Assembler |
| API: | Nativ |
| Binärformat: | [ELF](https://github.com/lowlevel-eu/wiki/wiki/Executable-and-Linking-Format "ELF") (Userprogramme) |
| [IPC-Methode](https://github.com/lowlevel-eu/wiki/wiki/Interprozesskommunikation "IPC"): | \- |
| Homepage |  |

[\[1\]](http://www.c-plusplus.de/forum/viewforum-var-f-is-62.html)

PrettyOS ist das Betriebssystem der Projektgruppe OS-Development bei [\[2\]](http://www.c-plusplus.de/forum/viewforum-var-f-is-62.html). Es entstand als Idee im März 2009, führte zu einem dreiteiligen Tutorial, das für Einstieger in die Materie beginnend beim ersten Boot-Vorgang gedacht war, und wird seit Mitte Oktober 2009 von interessierten Leuten diskutiert, umgebaut, gepflegt und erweitert. Zielsetzung ist es, verständlich zum Lernen und zum Experimentieren verwendbar zu sein. Als Arbeitsbasis ist PrettyOS bisher noch nicht ausgelegt, kann sich aber vielleicht noch in diese Richtung entwickeln.

## Ziel

PrettyOS soll Einsteiger in die Betriebssystementwicklung dabei unterstützen, den gesamten Prozess des Bootens, Startens eines C-Kernels und einer Shell (C oder C++) an einem einfachen praktischen Beispiel zu verstehen. Als Entwicklungsumgebung soll sowohl Linux als auch MS Windows einsetzbar sein. Das Starten mittels GRUB soll ebenfalls möglich sein. Inzwischen wird ein USB-Stick mit FAT16 oder FAT32 als Datenträger unterstützt. Die Grundlagen für eine Datenübertragung mittels Netzwerk (RTL8139) sind gelegt.

## Genereller Aufbau

PrettyOS besteht momentan aus den Bereichen Bootloader Stage 1, Bootloader Stage 2, Kernel und User-Space. Die beiden Bootloader sind in Assembler (NASM) geschrieben und verwenden bisher FAT12. BL1 (in Sektor 1) lädt BL2 (Datei boot2.bin). Dieser wiederum startet den bisher binären Kernel (kernel.bin). Der monolithische Kernel ist in der Programmiersprache C mit wenigen Teilen Assembler (Intel und AT&T Syntax) gehalten. Der User-Space dient bisher nur als Demonstration für die API (syscalls) und wurde ebenfalls in C geschrieben. Bisher ist nur eine einfache Shell vorhanden.

### Elemente des Kernels

Der Kernel bietet bisher grundlegende Fähigkeiten wie Interrupt-Handling, Paging, Kernel- und User-Heap, Multitasking, Multithreading, syscalls, virtual mode 86 und einige einfache Treiber. EHCI, Vesa Bios Extensions und FAT12/16/32 laufen ebenfalls. Er kann durch die beiden eigenen Bootloader aufgerufen werden (später evtl. auch mittels GRUB).

### Elemente des Userspace

Man verwendet die shell (program.elf) aus dem User-Space zum Testen der syscalls. Directory: ...\Source\user\user_program_c\\. program.elf wird nach ...\Source\user\init_rd_img\\. kopiert und in initrd.dat eingebunden. Diese Datei kopiert man nach ...\Source\kernel\\. Auf diese Weise wird program.elf letztendlich mittels incbin "initrd.dat" (im Assembler-Programm data.asm) im ELF-Format in den Kernel eingebunden. In ckernel.c wird diese Datei gefunden, ausgelesen und im User Mode gestartet.

### Weitere Entwicklung

PrettyOS ist als Experimentier-Basis für Ideen der OS-Projektgruppe bei c-plusplus.de gedacht und kann daher beeinflusst und weitgehend umgebaut werden. Weitere Details und Links findet man hier: [\[3\]](http://www.c-plusplus.de/forum/viewforum-var-f-is-62.html). Inzwischen entwickeln bis zu 10 Personen an PrettyOS.

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/8133/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2096/index.html)

<!-- MediaWiki page 2096; revision 8133; parent 8132; 2010-09-01T22:06:31Z -->
