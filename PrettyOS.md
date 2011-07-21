# PrettyOS

| PrettyOS |  |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
|  |  |
| Entwickler: | [ehenkes](https://lowlevel-eu.github.io/wiki/pages/2274/index.html "Benutzer:Ehenkes") et. al. |
| Akt. Version: | 0.0.2.0 |
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

PrettyOS ist das Betriebssystem der Projektgruppe OS-Development bei <http://www.c-plusplus.de/forum/>. Es entstand als Idee im März 2009, führte zu einem vierteiligen Tutorial, das für Einsteiger in die Materie beginnend beim ersten Boot-Vorgang gedacht war, und wird seit Mitte Oktober 2009 von interessierten Entwicklern diskutiert, umgebaut, gepflegt und erweitert. Zielsetzung ist, verständlich zum Lernen und zum Experimentieren verwendbar zu sein.

## Ziel

PrettyOS soll Einsteiger in die Betriebssystementwicklung dabei unterstützen, den gesamten Prozess des Bootens, Startens eines C-Kernels und einer Shell (C oder C++) an einem einfachen praktischen Beispiel zu verstehen. Als Entwicklungsumgebung soll sowohl Linux als auch MS Windows einsetzbar sein.

## Genereller Aufbau

PrettyOS besteht momentan aus den Bereichen Bootloader (Stage 1 und 2), Kernel und User-Space.

### Bootloader

Der Bootloader ist in Assembler (NASM) geschrieben und besteht aus zwei Stufen. BL1 (in Sektor 1) lädt BL2 (Datei boot2.bin). Dieser wiederum startet den Kernel (kernel.bin). Als Dateisystem für das Bootlaufwerk wird FAT12 vorausgesetzt. Der Bootloader soll [Multiboot](https://github.com/lowlevel-eu/wiki/wiki/Multiboot "Multiboot")-konform werden. Als Alternative zum nativen Bootloader wird an der Unterstützung von GRUB gearbeitet.

### Kernel

Der monolithische Kernel ist in der Programmiersprache C mit wenigen Teilen Assembler (NASM und GCCs Inline-Assembler) gehalten. Er verfügt über grundlegende Fähigkeiten wie Interrupt-Handling, Paging, Kernel- und User-Heap, Multitasking, Multithreading, syscalls, VM86 und enthält unter anderem Treiber für PCspeaker, Serielle Schnittstelle, Diskettenlaufwerke, EHCI, VESA BIOS Extensions und die Netzwerkkarten [RTL8139](https://github.com/lowlevel-eu/wiki/wiki/RTL8139 "RTL8139") und [AMD PCnet](https://github.com/lowlevel-eu/wiki/wiki/AMD-PCnet "AMD PCnet"). Als Dateisysteme werden gegenwärtig FAT12, FAT16 und FAT32 unterstützt. Betriebsbereite Netzwerkprotokolle sind: ethernet, ip, arp, icmp, udp, dhcp, tcp.

### Userprogramme

Der User-Space dient bisher nur als Demonstration für die API (syscalls). Bisher sind nur eine einfache Shell sowie ein paar simple Programme vorhanden, die u.a. zum Test neuer Features dienen. Programme für den Userspace können in diversen Sprachen geschrieben werden. Als Hilfe stehen die Dummy-makefiles, eine C-Userlib (Syscalls sowie einige wenige Funktionen der Standardlib) und eine C++-Userlib, die die C-Userlib als Untermenge hat und zudem ein paar C++-spezifische Funktionen bietet (new, delete) zur Verfügung.

Userprogramme können auf drei verschiedenen Wegen eingebunden werden: Mittels incbin direkt in den kernel, von wo es dann über die vom Linker generierte Adresse gestartet werden kann (derzeit für das VM86-Programm für VBE genutzt), über die Ramdisk (so wie es derzeit mit der Shell gemacht wird), oder auf dem herkömmlichen Weg als Executable im ELF- oder PE-Format auf einem von PrettyOS unterstützten Speichermedium, wodurch das Programm für den Nutzer von der Shell aus aufrufbar wird.

## Entwicklung

PrettyOS ist als freie Experimentier-Basis für Ideen der OS-Projektgruppe bei c-plusplus.de gedacht und wird von einer aktiven Community gepflegt und erweitert. Inzwischen entwickeln bis zu 10 Personen (allerdings nur zwei bis drei wirklich aktiv) an PrettyOS. IRC Channel: \#PrettyOS auf euirc.net und im Forum (siehe Links). Tester und Entwickler sind immer gerne gesehen.

## Links

- SVN-Repository: <https://prettyos.svn.sourceforge.net/svnroot/prettyos/trunk/Source>
- Forum: <http://www.c-plusplus.de/forum/viewforum-var-f-is-62.html>
- Tutorial: <http://www.henkessoft.de/OS_Dev/OS_Dev1.htm>

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/9964/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2096/index.html)

<!-- MediaWiki page 2096; revision 9964; parent 9961; 2011-07-21T16:47:55Z -->
