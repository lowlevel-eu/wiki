# PrettyOS

| PrettyOS |  |
| ----------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|  |  |
| Entwickler: | [ehenkes](https://lowlevel-eu.github.io/wiki/pages/2274/index.html "Benutzer:Ehenkes") et. al. |
| Akt. Version: | 0.0.5.105 (Mai 2015) |
| [Lizenz](https://github.com/lowlevel-eu/wiki/wiki/Lizenzen "Lizenzen"): | 2-Klausel-BSD |
| OS-Eigenschaften |  |
| Plattform: | [i386](https://github.com/lowlevel-eu/wiki/wiki/X86 "X86") |
| [Kernelart](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel"): | [Monolith](https://github.com/lowlevel-eu/wiki/wiki/Kernel#monolithischer-kernel "Monolithischer Kernel") |
| [Sprache](https://lowlevel-eu.github.io/wiki/pages/1648/index.html "Kategorie:Programmiersprache"): | C, Assembler |
| API: | Nativ |
| Binärformat: | [ELF](https://github.com/lowlevel-eu/wiki/wiki/Executable-and-Linking-Format "ELF"), [PE](https://github.com/lowlevel-eu/wiki/wiki/Microsoft-Portable-Executable-and-Common-Object-File-Format "PE") (Userprogramme) |
| [IPC-Methode](https://github.com/lowlevel-eu/wiki/wiki/Interprozesskommunikation "IPC"): | \- |
| Homepage |  |

[\[1\]](http://prettyos.de)

PrettyOS ist das Betriebssystem der Projektgruppe OS-Development bei <http://www.c-plusplus.de/forum/>. Es entstand als Idee im März 2009, führte zu einem vierteiligen Tutorial, das für Einsteiger in die Materie beginnend beim ersten Boot-Vorgang gedacht war, und wird seit Mitte Oktober 2009 von interessierten Entwicklern diskutiert, umgebaut, gepflegt und erweitert. Zielsetzung ist, verständlich zum Lernen und zum Experimentieren verwendbar zu sein. Das ist bisher weitgehend gelungen. Mit zunehmender Komplexität stellt sich die Frage der Didaktik immer wieder neu.

## Ziel

PrettyOS soll Einsteiger in die Betriebssystementwicklung dabei unterstützen, den gesamten Prozess des Bootens, Startens eines C-Kernels, einer Shell sowie Applikationen (C oder C++) an einem noch überschaubaren praktischen Beispiel zu verstehen. Als Entwicklungs-Plattform ist Linux, MacOS und MS Windows einsetzbar.

## Genereller Aufbau

PrettyOS besteht momentan aus den Bereichen Bootloader (Stage 1 und 2, Assembler), Kernel (C) und User-Space (C/C++).

### Bootloader

Der Bootloader ist in Assembler (NASM) geschrieben und besteht aus zwei Stufen. BL1 (in Sektor 1) lädt BL2 (Datei boot2.bin). Dieser wiederum startet den Kernel (kernel.bin). Als Dateisystem für das Bootlaufwerk wird FAT12 vorausgesetzt. Der Bootloader ist inzwischen [Multiboot](https://github.com/lowlevel-eu/wiki/wiki/Multiboot "Multiboot")-konform. Als Alternative zum nativen Bootloader können mit Einschränkungen GRUB oder iPXE verwendet werden.

### Kernel

Der monolithische Kernel ist in der Programmiersprache C mit wenigen Teilen Assembler (NASM und GCCs Inline-Assembler) gehalten. Er verfügt über grundlegende Fähigkeiten wie Interrupt-Handling, Paging, Kernel- und User-Heap, Multitasking, Multithreading, Syscalls, VM86 und enthält unter anderem Treiber für PCspeaker, Serielle Schnittstelle, Diskettenlaufwerke, [xHCI](https://github.com/lowlevel-eu/wiki/wiki/Extensible-Host-Controller-Interface "XHCI") (USB 3), [EHCI](https://github.com/lowlevel-eu/wiki/wiki/Enhanced-Host-Controller-Interface "EHCI") (USB 2), [OHCI](https://github.com/lowlevel-eu/wiki/wiki/Open-Host-Controller-Interface "OHCI") und [UHCI](https://github.com/lowlevel-eu/wiki/wiki/Universal-Host-Controller-Interface "UHCI") (USB 1.1 und USB 2.0), [VESA BIOS Extensions](https://github.com/lowlevel-eu/wiki/wiki/VESA-BIOS-Extensions "VESA BIOS Extensions") und die Netzwerkkarten [RTL8139](https://github.com/lowlevel-eu/wiki/wiki/RTL8139 "RTL8139"), RTL8168/[RTL8169](https://github.com/lowlevel-eu/wiki/wiki/RTL8169 "RTL8169") und [AMD PCnet](https://github.com/lowlevel-eu/wiki/wiki/AMD-PCnet "AMD PCnet"). Mittels [CDI](https://github.com/lowlevel-eu/wiki/wiki/Common-Driver-Interface "CDI") werden auch andere Treiber eingebunden, z.B. e1000. Die Netzwerkprotokolle ethernet, ip, arp, icmp, dhcp, udp und tcp werden unterstützt. Als Dateisysteme werden gegenwärtig FAT12, FAT16 und FAT32 auf Floppydisk und USB-Stick eingesetzt. Das System enthält ferner Treiber für USB-MSDs, USB-Diskettenlaufwerke (UFI), USB-Webcams und USB-HIDs (Maus und Tastatur).

### Userprogramme

Der User-Space dient bisher vorwiegend als Demonstration für die API (syscalls). Bisher sind nur eine einfache Shell sowie ein paar simple Programme vorhanden, die u.a. zum Test neuer Features dienen. Programme für den Userspace können in diversen Sprachen geschrieben werden. Als Hilfe stehen die Dummy-makefiles, eine C-Userlib (Syscalls sowie einige wenige Funktionen der C-Standardlib) und eine C++-Userlib, die die C-Userlib als Untermenge hat und zudem ein paar C++-spezifische Funktionen bietet (new, delete) zur Verfügung.

Userprogramme können auf zwei verschiedenen Wegen eingebunden werden: Mittels incbin direkt in den Kernel, von wo es dann über die vom Linker generierte Adresse gestartet werden kann (derzeit für die VM86-Programme für VBE und APM genutzt), ggf. mit Einbindung in die Ramdisk, oder auf dem herkömmlichen Weg als Executable im ELF- oder PE-Format auf einem von PrettyOS unterstützten Speichermedium, wodurch das Programm für den Nutzer von der Shell aus aufrufbar wird.

## Entwicklung

PrettyOS ist als freie Experimentierbasis für Ideen der OS-Projektgruppe bei c-plusplus.de gedacht und wird von einer aktiven Community gepflegt und erweitert. IRC Channel: \#PrettyOS auf euirc.net und im Forum (siehe Links). Konstruktive Tester, Beobachter und Entwickler sind immer gerne gesehen.

## Links

- Website: <http://prettyos.de/>
- SVN-Repository: svn://svn.code.sf.net/p/prettyos/code/trunk/Source und <http://svn.code.sf.net/p/prettyos/code/trunk/Source/>
- Forum: <http://www.c-plusplus.de/forum/f62>
- Tutorial: <http://www.henkessoft.de/OS_Dev/OS_Dev1.htm>
- IRC: irc.euirc.net, \#PrettyOS

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/11278/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2096/index.html)

<!-- MediaWiki page 2096; revision 11278; parent 11277; 2015-05-15T09:59:25Z -->
