# Hauptseite

****Herzlich willkommen im Wiki der Lowlevel-Community!****

Hier können angehende und fortgeschrittene Betriebssystementwickler Informationen finden, die sie unterstützen. Die Artikelserie [OS-Dev für Einsteiger](https://github.com/lowlevel-eu/wiki/wiki/OS-Dev-f%C3%BCr-Einsteiger "OS-Dev für Einsteiger") ist speziell an Neulinge gerichtet und gibt einen kleinen Einblick über die steinige Welt der Betriebssystementwicklung. Ansonsten ist hier vom ersten [Bootsektor](https://github.com/lowlevel-eu/wiki/wiki/Bootsektor "Bootsektor") über [C](https://github.com/lowlevel-eu/wiki/wiki/C "C")/[C++](https://github.com/lowlevel-eu/wiki/wiki/C%2B%2B "C++") im [Kernel](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel") bis zum [Kernel](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel")/[OS](https://github.com/lowlevel-eu/wiki/wiki/Betriebssystem "OS")-Design alles zu finden.

Hilf mit, indem du dich registrierst, deine Meinung und deine Fragen der Community im [Forum](https://lowlevel-eu.github.io/forum/index.html) / [IRC](https://github.com/lowlevel-eu/wiki/wiki/IRC "IRC") oder auf der Diskussionsseite zu den Wikiartikeln kundtust, neue Artikel erstellst oder bereits existierende Artikel verbesserst. Einen kleinen Überblick darüber, was noch zu tun ist, bietet die [TODO-Liste](https://github.com/lowlevel-eu/wiki/wiki/TODO "TODO"). Sie bietet darüber hinaus die Möglichkeit, Wünsche und Anregungen für Artikel los zu werden. Wenn du keine Erfahrung im Umgang mit Wikis hast, lies dir doch unseren kleinen [Wiki-Crashkurs](https://github.com/lowlevel-eu/wiki/wiki/Wiki-Crashkurs "Wiki-Crashkurs") durch. **Beachte**: Um die registrieren zu können ist es aktuell vonnöten, dass du dich im IRC oder im Forum bei [DemHartmut](https://lowlevel-eu.github.io/wiki/pages/1865/index.html "Benutzer:Hartmut") oder DesL meldest, damit diese dir einen Account anlegen können. Dieses Wiki enthält momentan 348 Artikel.

Sämtliche Artikel des Lowlevel-Wiki (abgesehen vom ehemaligen [Lowlevel-Magazin](https://lowlevel-eu.github.io/wiki/pages/1411/index.html "Kategorie:Magazin")) stehen unter der [by-nc-sa 3.0](http://creativecommons.org/licenses/by-nc-sa/3.0/de/)-Lizenz der [Creative Commons](http://creativecommons.org/).

Tipp: Wenn ihr mal nicht online sein könnt, und trotzdem im Wiki stöbern wollt, sei euch die [Offline-Variante](https://github.com/lowlevel-eu/wiki/wiki/Lowlevel-offline "Lowlevel-Offline") des Wikis ans Herz gelegt.

****News**\[[Bearbeiten](https://lowlevel-eu.github.io/wiki/pages/1406/index.html "Vorlage:News")\]**

|  |  |
| ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Wiki tot?** | Nix los hier? Keine Sorge - wir sind noch da, aktuell aber meist nur im [IRC](https://github.com/lowlevel-eu/wiki/wiki/IRC "IRC") aktiv (Achtung: IRC ist asynchron: rein kommen, schreiben und 'ne Weile Online bleiben und warten). Komm im IRC vorbei, stell Fragen, lerne Dinge und erweitere das Wiki! :) |
| **01.04.2014 :** | Nach langer Zeit regt sich endlich wieder etwas bei [týndur](https://github.com/lowlevel-eu/wiki/wiki/T%C3%BDndur "Tyndur"). Es wurde in einem gemeinsamen IRC-Treffen beschlossen týndur komplett neu zu entwickeln - diesmal als Nanokernel auf Basis der Google-Programmiersprache [Go](http://golang.org/) und einem vollkommen reimplementierten IPC-Mechanismus ([XML-RPC](http://de.wikipedia.org/wiki/XML-RPC)). Ziel ist nicht nur ein Neuanfang (Zitat taljeth: "Den Driss sollten wir neu machen") sondern auch die Auslegung auf "moderne" Beduerfnisse; dies schliesst insbesondere die Nutzung von týndur als Host-OS fuer etwaige Web-Services ein (darum auch die Implementierung von XML-RPC; RPC von Web-Clients mit OS-Prozessen). Angestrebt wird auch eine Zusammenarbeit mit [Pedigree](http://www.pedigree-project.org/), hier wurde schon Kontakt aufgenommen. Fuer weitere Infos koennt ihr den [IRC](https://github.com/lowlevel-eu/wiki/wiki/IRC "IRC")-Channel \#tyndurofthefuture im euIRC joinen. |
| **23.05.2013 :** | Der Sommer kommt (mancherorts) in die Städte - allerdings nicht gerade zuverlässig. Zuverlässig dagegen ist das Team rund um [QEMU](https://github.com/lowlevel-eu/wiki/wiki/QEMU "QEMU") - erst kürzlich wurde die Version [1.5 freigegeben](http://article.gmane.org/gmane.comp.emulators.qemu/212062). Die neue Version unterstützt die Virtualisierung mit KVM auf ARM-Kernen. Mit dem Linux-Kernel 3.6 lassen sich ohne viel Overhead nun SCSI-Geräte an KVM-Gäste durchreichen, mit dem neuen QMP-Kommando *cpu-add* lässt sich die Anzahl der CPU-Kerne im Gast zur Laufzeit erhöhen. Diese und viele weitere Änderungen lassen sich dem [ChangeLog](http://wiki.qemu.org/ChangeLog/1.5#ARM) entnehmen. |
| **26.03.2013 :** | Der Frühling lässt noch ein wenig auf sich warten, der [GCC](https://github.com/lowlevel-eu/wiki/wiki/GNU-Compiler-Collection "GCC") in der nun erhältlichen Version 4.8.0 nicht. Einer der größten Änderungen sind infrastrukturell, GCC ist nun vollständig in C++ implementiert und man benötigt fortan nun einen C++-Compiler, um GCC selbst zu bauen. Diese und viele weitere wichtige Änderungen lassen sich im [Changelog](http://gcc.gnu.org/gcc-4.8/changes.html) einsehen. |
| **05.09.2012 :** | [QEMU](https://github.com/lowlevel-eu/wiki/wiki/QEMU "QEMU") 1.2 ist fertig. In dieser Version unterstützt AHCI auch CD-ROM-Laufwerke, und einige neue SCSI-Hostadapter sowieso USB-Attached SCSI wurden hinzugefügt. Die Grafikkarten mit *-vga std/qxl* haben jetzt 16 MB statt 8 MB Grafikspeicher. Außerdem speichert der neue Monitorbefehl *dump-guest-memory* den kompletten Arbeitsspeicher in einen ELF-Dump. Wie immer ist eine Aufzählung weiterer Neuerungen im [Changelog](http://wiki.qemu.org/ChangeLog/1.2) zu finden. |
| **29.06.2012 :** | Nach gefühlten 50 und tatsächlichen knapp zehn Jahren haben die Entwickler des [Grand Unified Bootloader](https://github.com/lowlevel-eu/wiki/wiki/Grand-Unified-Bootloader "GRUB"), besser bekannt als GRUB, die Version 2.00 herausgegeben. Neben Spielereien wie einem neuen Standard-Theme bringt GRUB 2 nun einen EHCI-Treiber mit und ist als Itanium- und SGI-Port vorhanden. Alle Änderungen lassen sich in der [Ankündigung](https://lists.gnu.org/archive/html/grub-devel/2012-06/msg00093.html) nachlesen. |
| **01.06.2012 :** | Der Emulator [QEMU](https://github.com/lowlevel-eu/wiki/wiki/QEMU "QEMU") ist am 1. Juni in der Version 1.1 freigegeben worden. Für die OS-Entwicklung am interessantesten dürfte die experimentelle Unterstützung für xHCI-Controller (USB 3.0) sein. Es sind außerdem einige Fehlerkorrekturen für das emulierte Diskettenlaufwerk enthalten, vor allem in Bezug auf Medienwechsel. Eine Aufzählung weiterer Neuerungen ist wie gewohnt im [Changelog](http://wiki.qemu.org/ChangeLog/1.1) zu finden. |
| **22.03.2012 :** | Genau 25 Jahre nach dem ersten Release ist die neue Version 4.7.0 der [GNU Compiler Collection](https://github.com/lowlevel-eu/wiki/wiki/GNU-Compiler-Collection "GCC") erschienen ([Ankündigung](http://gcc.gnu.org/ml/gcc/2012-03/msg00347.html)). Wichtige Neuerungen sind eine nochmals verbesserte Unterstützung der beiden neuen Standards C11 und C++11 (bei letzterem unter anderen die Möglichkeit der Benutzung des atomic-Konstrukts und des neuen Speichermodells). Auf einigen Architekturen wurde die Unterstützung für Software Transactional Memory (STM) eingeführt. Alle Änderungen lassen sich [hier](http://gcc.gnu.org/gcc-4.7/changes.html) nachlesen. Happy Birthday GCC! |
| **01.03.2012 :** | Das von Andrew S. Tanenbaum als Lehrsystem gestartete Betriebssystem [Minix](https://github.com/lowlevel-eu/wiki/wiki/Minix "Minix") ist in der Version 3.2 erschienen. Wichtige Neuerungen sind experimenteller [SMP](https://github.com/lowlevel-eu/wiki/wiki/Symmetrisches-Multiprozessorsystem "SMP")-Support sowie die Portierung von [FUSE](http://de.wikipedia.org/wiki/Filesystem_in_Userspace) (Filesystem in Userspace) und weiteren Werkzeugen. [Hier](http://wiki.minix3.org/en/MinixReleases) findet sich ein Überblick über alle Neuerungen, Download des ISOs ist von [hier](http://www.minix3.org/download/) möglich. |
| **23.02.2012 :** | Schon etwas länger her ist der Release der Version 9.0 von [FreeBSD](http://www.freebsd.org/releases/9.0R/announce.html). Neuerungen sind unter anderem ein neuer Installer und AHCI-Support für ATA/SATA-Laufwerke. Jüngst erschienen ist auch die Version 3.0 des FreeBSD-Derivats [DragonFlyBSD](http://www.dragonflybsd.org/). Hier sind die Neuerungen verbesserter Multiprozessor-Support sowie die Unterstützung von verschlüsselten Dateisystemen. |
| **02.01.2012 :** | Version 1.1 des DOS-kompatiblen Betriebssystems [FreeDOS](https://github.com/lowlevel-eu/wiki/wiki/FreeDOS "FreeDOS") wurde [heute veröffentlicht](http://sourceforge.net/news/?group_id=5109&id=305444). Gegenüber dem letzten Release wird nun standardmäßig ein TCP/IP-Stack mitgeliefert. Außerdem wird nun USB dank eines UHCI-Treibers unterstützt. Weitere Änderungen können der [Ankündigung](http://www.ibiblio.org/pub/micro/pc-stuff/freedos/files/distributions/1.1/announce.txt) entnommen werden. |
| **01.12.2011 :** | Nach 8 Jahren Entwicklung hat sich [QEMU](https://github.com/lowlevel-eu/wiki/wiki/QEMU "QEMU") von der führenden Null in der Version getrennt und wurde heute als Version 1.0 freigegeben. Einen Überblick über die Änderungen kann man sich im [Changelog](http://wiki.qemu.org/ChangeLog/1.0) verschaffen. |
| **30.08.2011 :** | Mittlerweile ist die Version 4.6.1 der beliebten und im OS-Dev-Bereich vorherrschenden [GNU Compiler Collection](http://gcc.gnu.org/gcc-4.6/) erschienen. Diese bietet neben üblichen Optimierungen auch experimentelle Unterstützung für den zukünftigen neuen C-Standard *C1X*. Eine Liste aller Änderungen ist [hier](http://gcc.gnu.org/gcc-4.6/changes.html) einsehbar. |
| **09.08.2011 :** | Es ist zwar Dienstag, aber jetzt ist die Version 0.15.0 von [QEMU](https://github.com/lowlevel-eu/wiki/wiki/QEMU "QEMU") erschienen. Sie enthält Untstützung für [EHCI](https://github.com/lowlevel-eu/wiki/wiki/Enhanced-Host-Controller-Interface "EHCI")-USB-Hostcontroller und etliche andere USB-bezogene Verbesserungen. Ab Linux 3.0 funktionieren jetzt auch Ping-Pakete mit dem Usermode-Netzwerkstack. Weitere Details sind im [Changelog](http://wiki.qemu.org/ChangeLog/0.15) nachzulesen. |
| **05.08.2011 :** | Jidder hat eine OS-Dev-technisch hochinteressante Frage in den Raum gestellt, nämlich was man mal in die News schreiben könnte, damit am Montag nicht zweimal QEMU oben steht. |
| **22.03.2011 :** | [ReactOS](https://github.com/lowlevel-eu/wiki/wiki/ReactOS "ReactOS") wurde in der Version 0.3.13 veröffentlicht. Im ReactOS Wiki gibt es wie üblich den [Changelog](http://www.reactos.org/wiki/ChangeLog-0.3.13). |
| **18.02.2011 :** | [QEMU](https://github.com/lowlevel-eu/wiki/wiki/QEMU "QEMU") wurde in der Version 0.14.0 veröffentlicht. Unter anderem sind eine Emulation für AHCI- und HD-Audio-Geräte dazugekommen. Verbessert wurde die Implementierung von PCI (Express), neu ist hier z. B. Unterstützung für [MSI](https://github.com/lowlevel-eu/wiki/wiki/Message-Signaled-Interrupt "MSI"). Weitere Details sind im [Changelog](http://wiki.qemu.org/Changelog/0.14) nachzulesen. |
| **20.10.2010 :** | [ReactOS](https://github.com/lowlevel-eu/wiki/wiki/ReactOS "ReactOS") wurde in der Version 0.3.12 veröffentlicht. Im ReactOS Wiki gibt es wie üblich den [Changelog](http://www.reactos.org/wiki/index.php/ChangeLog-0.3.12). |
| **18.10.2010 :** | [QEMU](https://github.com/lowlevel-eu/wiki/wiki/QEMU "QEMU") hat die Version 0.13.0 erreicht. Aus Sicht eines OS-Entwicklers für x86 enthält das Release vor allem viele kleinere Verbesserungen und Fehlerkorrekturen in der Hardwareemulation. Das neue Gerät *isa-debugcon* unterstützt jetzt den von bochs bekannten Debugport 0xe9. Der OHCI-Controller *pci-ohci* wird jetzt standardmäßig gebaut und ist damit zukünftig auch in Binärpaketen enthalten. |
| **25.04.2010 :** | [bochs](https://github.com/lowlevel-eu/wiki/wiki/Bochs "Bochs") ist in Version 2.4.5 erschienen. Die Änderungen – die es [hier](http://bochs.cvs.sourceforge.net/bochs/bochs/CHANGES?view=markup&content-type=text/vnd.viewcvs-markup&revision=REL_2_4_5_FINAL) gibt – sind abgesehen von der Implementierung der x2APIC, des Intel-VMXx2-Instruktionensatzes und einer Geräteemulation für einen USB-HP-DeskJet-920C-Drucker nur Bugfixes. |
| **14.04.2010 :** | Die Version 4.5 der [GNU Compiler Collection](https://github.com/lowlevel-eu/wiki/wiki/GNU-Compiler-Collection "GCC") wurde freigegeben. In dieser Version sind erstmals Optimierungen zur Linkzeit (LTO, über die Kommandozeilenoption -flto) enthalten. Außerdem wurde die Unterstützung für Features aus dem nächsten C++-Standard erweitert. Eine detaillierte Übersicht über die Änderungen findet sich [hier](http://gcc.gnu.org/gcc-4.5/changes.html). |
| **06.03.2010 :** | GRUB 1.98 ist erschienen. [Hier](http://grub.enbug.org/FrontPage?action=show&redirect=StartSeite) gibt es den Sourcecode und mehr Informationen zu GRUB2. |

*Ältere Nachrichten sind im [Archiv](https://github.com/lowlevel-eu/wiki/wiki/Newsarchiv "Newsarchiv") zu finden*

****Übersicht****

**[OS-Dev für Einsteiger](https://lowlevel-eu.github.io/wiki/pages/1895/index.html "Kategorie:OS-Dev für Einsteiger")**

- [Grobüberblick](https://github.com/lowlevel-eu/wiki/wiki/OS-Dev-f%C3%BCr-Einsteiger "OS-Dev für Einsteiger")
- [Teil 1 - Entwicklungsumgebung](https://github.com/lowlevel-eu/wiki/wiki/Teil-1-Entwicklungsumgebung "Teil 1 - Entwicklungsumgebung")
- [Teil 2 - Assembler 101](https://github.com/lowlevel-eu/wiki/wiki/Teil-2-Assembler-101 "Teil 2 - Assembler 101")
- [Teil 3 - Trockenübungen](https://github.com/lowlevel-eu/wiki/wiki/Teil-3-Trocken%C3%BCbungen "Teil 3 - Trockenübungen")
- [Teil 4 - Hello World](https://github.com/lowlevel-eu/wiki/wiki/Teil-4-Hello-World "Teil 4 - Hello World")
- [Teil 5 - Interrupts](https://github.com/lowlevel-eu/wiki/wiki/Teil-5-Interrupts "Teil 5 - Interrupts")
- [Teil 6 - Multitasking](https://github.com/lowlevel-eu/wiki/wiki/Teil-6-Multitasking "Teil 6 - Multitasking")
- [Teil 7 - Physische Speicherverwaltung](https://github.com/lowlevel-eu/wiki/wiki/Teil-7-Physische-Speicherverwaltung "Teil 7 - Physische Speicherverwaltung")
- [Teil 8 - Ein erstes Programm](https://github.com/lowlevel-eu/wiki/wiki/Teil-8-Ein-erstes-Programm "Teil 8 - Ein erstes Programm")
- [Teil 9 - Paging](https://github.com/lowlevel-eu/wiki/wiki/Teil-9-Paging "Teil 9 - Paging")

**Prozessor**

- [Interrupt](https://github.com/lowlevel-eu/wiki/wiki/Interrupt "Interrupt")
- [Multithreading](https://github.com/lowlevel-eu/wiki/wiki/Multithreading "Multithreading")
- [x86](https://github.com/lowlevel-eu/wiki/wiki/X86 "X86")
  - [FPU](https://github.com/lowlevel-eu/wiki/wiki/Mathematischer-Koprozessor "FPU")
  - [Real Mode](https://github.com/lowlevel-eu/wiki/wiki/Real-Mode "Real Mode")
    - [IVT](https://github.com/lowlevel-eu/wiki/wiki/Interrupt-Vector-Table "IVT")
    - [BIOS](https://github.com/lowlevel-eu/wiki/wiki/Basic-Input-Output-System "BIOS")
  - [Protected Mode](https://github.com/lowlevel-eu/wiki/wiki/Protected-Mode "Protected Mode")
    - [GDT](https://github.com/lowlevel-eu/wiki/wiki/Global-Descriptor-Table "GDT")
    - [IDT](https://github.com/lowlevel-eu/wiki/wiki/Interrupt-Descriptor-Table "IDT")
    - [Multitasking](https://github.com/lowlevel-eu/wiki/wiki/Multitasking "Multitasking") & [TSS](https://github.com/lowlevel-eu/wiki/wiki/Task-State-Segment "TSS")
    - [Paging](https://github.com/lowlevel-eu/wiki/wiki/Paging "Paging")
    - [Virtual 8086 Mode](https://github.com/lowlevel-eu/wiki/wiki/Virtual-8086-Mode "Virtual 8086 Mode")
  - [System Management Mode](https://github.com/lowlevel-eu/wiki/wiki/System-Management-Mode "System Management Mode")
- [x86-64](https://github.com/lowlevel-eu/wiki/wiki/X86-64 "X86-64")
  - [Long Mode](https://github.com/lowlevel-eu/wiki/wiki/Long-Mode "Long Mode")
- [ARM](https://github.com/lowlevel-eu/wiki/wiki/ARM "ARM")

**[Kernel](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel")**

- [Hardwareabstraktionsschicht](https://github.com/lowlevel-eu/wiki/wiki/Hardware-Abstraction-Layer "Hardware Abstraction Layer")
- [Speicherverwaltung](https://github.com/lowlevel-eu/wiki/wiki/Speicherverwaltung "Speicherverwaltung")
- [Prozessverwaltung](https://github.com/lowlevel-eu/wiki/wiki/Prozessverwaltung "Prozessverwaltung")
- [Scheduler](https://github.com/lowlevel-eu/wiki/wiki/Scheduler "Scheduler")

**Für Spaß im Userspace**

- [Interprozesskommunikation](https://github.com/lowlevel-eu/wiki/wiki/Interprozesskommunikation "Interprozesskommunikation")
- [Heapverwaltung](https://github.com/lowlevel-eu/wiki/wiki/Heapverwaltung "Heapverwaltung")
- [Systemaufrufe (Syscalls)](https://github.com/lowlevel-eu/wiki/wiki/Syscall "Systemaufruf")
- [Virtuelles Dateisystem](https://github.com/lowlevel-eu/wiki/wiki/Virtuelles-Dateisystem "Virtuelles Dateisystem")
- [Standardbibliothek](https://github.com/lowlevel-eu/wiki/wiki/Standardbibliothek "Standardbibliothek")
- [Threads](https://github.com/lowlevel-eu/wiki/wiki/Prozess#threads "Thread") (auch: [pthreads](https://github.com/lowlevel-eu/wiki/wiki/POSIX-Threads "Pthread"))
- [Shell](https://github.com/lowlevel-eu/wiki/wiki/Shell "Shell")
- [Software portieren](https://github.com/lowlevel-eu/wiki/wiki/Portieren-von-Programmen-und-Bibliotheken "Portieren von Programmen und Bibliotheken")

**[Hardware](https://lowlevel-eu.github.io/wiki/pages/1447/index.html "Kategorie:Hardware")**

- [ATA](https://github.com/lowlevel-eu/wiki/wiki/AT-Attachment "ATA")
- [DMA](https://github.com/lowlevel-eu/wiki/wiki/Direct-Memory-Access "DMA")
- [serielle Schnittstelle](https://github.com/lowlevel-eu/wiki/wiki/Serielle-Schnittstelle "Serielle Schnittstelle")
- [parallele Schnittstelle](https://github.com/lowlevel-eu/wiki/wiki/Parallele-Schnittstelle "Parallele Schnittstelle")
- [Textausgabe](https://github.com/lowlevel-eu/wiki/wiki/Textausgabe "Textausgabe")
- [Netzwerkkarten](https://lowlevel-eu.github.io/wiki/pages/1826/index.html "Kategorie:Netzwerkkarte")
  - [Realtek RTL8139](https://github.com/lowlevel-eu/wiki/wiki/RTL8139 "RTL8139")
  - [AMD PCnet-FAST III](https://github.com/lowlevel-eu/wiki/wiki/AMD-PCnet "AMD PCnet")
- Grafikkarten
  - [VGA](https://github.com/lowlevel-eu/wiki/wiki/Video-Graphics-Array "VGA")
  - [Cirrus Logic](https://github.com/lowlevel-eu/wiki/wiki/Cirrus-Logic "Cirrus Logic")
- [Soundkarten](https://lowlevel-eu.github.io/wiki/pages/1827/index.html "Kategorie:Soundkarte")
  - [Gameport](https://github.com/lowlevel-eu/wiki/wiki/Gameport "Gameport")
- IBM PC-spezifisch
  - [APIC](https://github.com/lowlevel-eu/wiki/wiki/Advanced-Programmable-Interrupt-Controller "APIC")
  - [CMOS](https://github.com/lowlevel-eu/wiki/wiki/CMOS "CMOS")
  - [Diskettenlaufwerk](https://github.com/lowlevel-eu/wiki/wiki/Floppy-Disk-Controller "FDC")
  - [PS/2 Tastatur](https://github.com/lowlevel-eu/wiki/wiki/Keyboard-Controller "KBC")
  - [PS/2 Maus](https://github.com/lowlevel-eu/wiki/wiki/PS-2-Maus "Programmierung der PS/2-Maus")
  - [PIC](https://github.com/lowlevel-eu/wiki/wiki/Programmable-Interrupt-Controller "PIC")
  - [PIT](https://github.com/lowlevel-eu/wiki/wiki/Programmable-Interval-Timer "PIT")
  - [Systemlautsprecher](https://github.com/lowlevel-eu/wiki/wiki/Systemlautsprecher "Systemlautsprecher")

**[Bussysteme](https://lowlevel-eu.github.io/wiki/pages/1769/index.html "Kategorie:Bus")**

- [ISA](https://github.com/lowlevel-eu/wiki/wiki/Industry-Standard-Architecture "ISA")
- [EISA](https://github.com/lowlevel-eu/wiki/wiki/Industry-Standard-Architecture#extended-industry-standard-architecture "EISA")
- [PCI](https://github.com/lowlevel-eu/wiki/wiki/Peripheral-Component-Interconnect "PCI")
- [USB](https://github.com/lowlevel-eu/wiki/wiki/Universal-Serial-Bus "USB")

**Hobby-[OS](https://lowlevel-eu.github.io/wiki/pages/1649/index.html "Kategorie:Betriebssystem")**

- [MyXomycota](https://github.com/lowlevel-eu/wiki/wiki/MyXomycota "MyXomycota")
- [týndur](https://github.com/lowlevel-eu/wiki/wiki/T%C3%BDndur "Týndur")
- [Xantorix](https://github.com/lowlevel-eu/wiki/wiki/Xantorix "Xantorix")
- [LF OS](https://github.com/lowlevel-eu/wiki/wiki/LF-OS "LF OS")
- Weitere: [Kategorie Betriebssysteme](https://lowlevel-eu.github.io/wiki/pages/1649/index.html "Kategorie:Betriebssystem")

**[Dateisysteme](https://github.com/lowlevel-eu/wiki/wiki/Dateisystem "Dateisystem")**

- [Ext2](https://github.com/lowlevel-eu/wiki/wiki/Ext2 "Ext2")
- [Ext3](https://github.com/lowlevel-eu/wiki/wiki/Ext3 "Ext3")
- [FAT](https://github.com/lowlevel-eu/wiki/wiki/File-Allocation-Table "FAT")
- [ISO9660](https://github.com/lowlevel-eu/wiki/wiki/ISO9660 "ISO9660")
- [NTFS](https://github.com/lowlevel-eu/wiki/wiki/NTFS "NTFS")
- weitere: [Kategorie:Dateisystem](https://lowlevel-eu.github.io/wiki/pages/1659/index.html "Kategorie:Dateisystem")

**[Sprachen](https://lowlevel-eu.github.io/wiki/pages/1648/index.html "Kategorie:Programmiersprache")**

- [Assembler](https://github.com/lowlevel-eu/wiki/wiki/Assembler "Assembler")
- [C](https://github.com/lowlevel-eu/wiki/wiki/C "C")
- [C++](https://github.com/lowlevel-eu/wiki/wiki/C%2B%2B "C++")
- [D](https://github.com/lowlevel-eu/wiki/wiki/D "D")
- [FreeBASIC](https://github.com/lowlevel-eu/wiki/wiki/FreeBASIC "FreeBASIC")
- [Pascal](https://github.com/lowlevel-eu/wiki/wiki/Pascal "Pascal")
- weitere: [Kategorie:Programmiersprache](https://lowlevel-eu.github.io/wiki/pages/1648/index.html "Kategorie:Programmiersprache")

**Verschiedenes**

- [Glossar](https://lowlevel-eu.github.io/wiki/pages/1461/index.html "Kategorie:Glossar")
- [Linkliste](https://github.com/lowlevel-eu/wiki/wiki/Linkliste "Linkliste")
- [TODO](https://github.com/lowlevel-eu/wiki/wiki/TODO "TODO")
- [Zitate](https://github.com/lowlevel-eu/wiki/wiki/Zitate "Zitate")
- [Tutorials](https://lowlevel-eu.github.io/wiki/pages/1423/index.html "Kategorie:Tutorials")
- [Literatur](https://github.com/lowlevel-eu/wiki/wiki/Literatur "Literatur")
- Alle Kategorien

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/11001/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1712/index.html)

<!-- MediaWiki page 1712; revision 11001; parent 10345; 2013-02-12T14:44:54Z -->
