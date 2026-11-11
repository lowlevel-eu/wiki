# Hauptseite

****Herzlich willkommen im Wiki der Lowlevel-Community!****

Hier können angehende und fortgeschrittene Betriebssystementwickler Informationen finden, die sie unterstützen. Die Artikelserie [OS-Dev für Einsteiger](OS-Dev-f%C3%BCr-Einsteiger "OS-Dev für Einsteiger") ist speziell an Neulinge gerichtet und gibt einen kleinen Einblick über die steinige Welt der Betriebssystementwicklung. Ansonsten ist hier vom ersten [Bootsektor](Bootsektor "Bootsektor") über [C](C "C")/[C++](C%2B%2B "C++") im [Kernel](Kernel "Kernel") bis zum [Kernel](Kernel "Kernel")/[OS](Betriebssystem "OS")-Design alles zu finden.

Hilf mit, indem du dich registrierst, deine Meinung und deine Fragen der Community im [Forum](https://lowlevel-eu.github.io/forum/index.html) / [IRC](IRC "IRC") oder auf der Diskussionsseite zu den Wikiartikeln kundtust, neue Artikel erstellst oder bereits existierende Artikel verbesserst. Einen kleinen Überblick darüber, was noch zu tun ist, bietet die [TODO-Liste](TODO "TODO"). Sie bietet darüber hinaus die Möglichkeit, Wünsche und Anregungen für Artikel los zu werden. Wenn du keine Erfahrung im Umgang mit Wikis hast, lies dir doch unseren kleinen [Wiki-Crashkurs](Wiki-Crashkurs "Wiki-Crashkurs") durch. **Beachte**: Um dich registrieren zu können ist es aktuell vonnöten, dass du dich im [IRC](IRC "IRC") oder im Forum bei [DemHartmut](https://lowlevel-eu.github.io/wiki/pages/1865/index.html "Benutzer:Hartmut") oder DesL meldest, damit diese dir einen Account anlegen können. Dieses Wiki enthält momentan 348 Artikel.

Sämtliche Artikel des Lowlevel-Wiki (abgesehen vom ehemaligen [Lowlevel-Magazin](Kategorie-Magazin "Kategorie:Magazin")) stehen unter der [by-nc-sa 3.0](http://creativecommons.org/licenses/by-nc-sa/3.0/de/)-Lizenz der [Creative Commons](http://creativecommons.org/).


****News**\[[Bearbeiten](https://lowlevel-eu.github.io/wiki/pages/1406/index.html "Vorlage:News")\]**

|  |  |
| ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Wiki tot?** | Nix los hier? Keine Sorge - wir sind noch da, aktuell aber meist nur im [IRC](IRC "IRC") aktiv (Achtung: IRC ist asynchron: rein kommen, schreiben und 'ne Weile Online bleiben und warten). Komm im IRC vorbei, stell Fragen, lerne Dinge und erweitere das Wiki! :) |
| **01.04.2014 :** | Nach langer Zeit regt sich endlich wieder etwas bei [týndur](T%C3%BDndur "Tyndur"). Es wurde in einem gemeinsamen IRC-Treffen beschlossen týndur komplett neu zu entwickeln - diesmal als Nanokernel auf Basis der Google-Programmiersprache [Go](http://golang.org/) und einem vollkommen reimplementierten IPC-Mechanismus ([XML-RPC](http://de.wikipedia.org/wiki/XML-RPC)). Ziel ist nicht nur ein Neuanfang (Zitat taljeth: "Den Driss sollten wir neu machen") sondern auch die Auslegung auf "moderne" Beduerfnisse; dies schliesst insbesondere die Nutzung von týndur als Host-OS fuer etwaige Web-Services ein (darum auch die Implementierung von XML-RPC; RPC von Web-Clients mit OS-Prozessen). Angestrebt wird auch eine Zusammenarbeit mit [Pedigree](http://www.pedigree-project.org/), hier wurde schon Kontakt aufgenommen. Fuer weitere Infos koennt ihr den [IRC](IRC "IRC")-Channel \#tyndurofthefuture im euIRC joinen. |
| **23.05.2013 :** | Der Sommer kommt (mancherorts) in die Städte - allerdings nicht gerade zuverlässig. Zuverlässig dagegen ist das Team rund um [QEMU](QEMU "QEMU") - erst kürzlich wurde die Version [1.5 freigegeben](http://article.gmane.org/gmane.comp.emulators.qemu/212062). Die neue Version unterstützt die Virtualisierung mit KVM auf ARM-Kernen. Mit dem Linux-Kernel 3.6 lassen sich ohne viel Overhead nun SCSI-Geräte an KVM-Gäste durchreichen, mit dem neuen QMP-Kommando *cpu-add* lässt sich die Anzahl der CPU-Kerne im Gast zur Laufzeit erhöhen. Diese und viele weitere Änderungen lassen sich dem [ChangeLog](http://wiki.qemu.org/ChangeLog/1.5#ARM) entnehmen. |
| **26.03.2013 :** | Der Frühling lässt noch ein wenig auf sich warten, der [GCC](GNU-Compiler-Collection "GCC") in der nun erhältlichen Version 4.8.0 nicht. Einer der größten Änderungen sind infrastrukturell, GCC ist nun vollständig in C++ implementiert und man benötigt fortan nun einen C++-Compiler, um GCC selbst zu bauen. Diese und viele weitere wichtige Änderungen lassen sich im [Changelog](http://gcc.gnu.org/gcc-4.8/changes.html) einsehen. |
| **05.09.2012 :** | [QEMU](QEMU "QEMU") 1.2 ist fertig. In dieser Version unterstützt AHCI auch CD-ROM-Laufwerke, und einige neue SCSI-Hostadapter sowieso USB-Attached SCSI wurden hinzugefügt. Die Grafikkarten mit *-vga std/qxl* haben jetzt 16 MB statt 8 MB Grafikspeicher. Außerdem speichert der neue Monitorbefehl *dump-guest-memory* den kompletten Arbeitsspeicher in einen ELF-Dump. Wie immer ist eine Aufzählung weiterer Neuerungen im [Changelog](http://wiki.qemu.org/ChangeLog/1.2) zu finden. |
| **29.06.2012 :** | Nach gefühlten 50 und tatsächlichen knapp zehn Jahren haben die Entwickler des [Grand Unified Bootloader](Grand-Unified-Bootloader "GRUB"), besser bekannt als GRUB, die Version 2.00 herausgegeben. Neben Spielereien wie einem neuen Standard-Theme bringt GRUB 2 nun einen EHCI-Treiber mit und ist als Itanium- und SGI-Port vorhanden. Alle Änderungen lassen sich in der [Ankündigung](https://lists.gnu.org/archive/html/grub-devel/2012-06/msg00093.html) nachlesen. |
| **01.06.2012 :** | Der Emulator [QEMU](QEMU "QEMU") ist am 1. Juni in der Version 1.1 freigegeben worden. Für die OS-Entwicklung am interessantesten dürfte die experimentelle Unterstützung für xHCI-Controller (USB 3.0) sein. Es sind außerdem einige Fehlerkorrekturen für das emulierte Diskettenlaufwerk enthalten, vor allem in Bezug auf Medienwechsel. Eine Aufzählung weiterer Neuerungen ist wie gewohnt im [Changelog](http://wiki.qemu.org/ChangeLog/1.1) zu finden. |
| **22.03.2012 :** | Genau 25 Jahre nach dem ersten Release ist die neue Version 4.7.0 der [GNU Compiler Collection](GNU-Compiler-Collection "GCC") erschienen ([Ankündigung](http://gcc.gnu.org/ml/gcc/2012-03/msg00347.html)). Wichtige Neuerungen sind eine nochmals verbesserte Unterstützung der beiden neuen Standards C11 und C++11 (bei letzterem unter anderen die Möglichkeit der Benutzung des atomic-Konstrukts und des neuen Speichermodells). Auf einigen Architekturen wurde die Unterstützung für Software Transactional Memory (STM) eingeführt. Alle Änderungen lassen sich [hier](http://gcc.gnu.org/gcc-4.7/changes.html) nachlesen. Happy Birthday GCC! |
| **01.03.2012 :** | Das von Andrew S. Tanenbaum als Lehrsystem gestartete Betriebssystem [Minix](Minix "Minix") ist in der Version 3.2 erschienen. Wichtige Neuerungen sind experimenteller [SMP](Symmetrisches-Multiprozessorsystem "SMP")-Support sowie die Portierung von [FUSE](http://de.wikipedia.org/wiki/Filesystem_in_Userspace) (Filesystem in Userspace) und weiteren Werkzeugen. [Hier](http://wiki.minix3.org/en/MinixReleases) findet sich ein Überblick über alle Neuerungen, Download des ISOs ist von [hier](http://www.minix3.org/download/) möglich. |
| **23.02.2012 :** | Schon etwas länger her ist der Release der Version 9.0 von [FreeBSD](http://www.freebsd.org/releases/9.0R/announce.html). Neuerungen sind unter anderem ein neuer Installer und AHCI-Support für ATA/SATA-Laufwerke. Jüngst erschienen ist auch die Version 3.0 des FreeBSD-Derivats [DragonFlyBSD](http://www.dragonflybsd.org/). Hier sind die Neuerungen verbesserter Multiprozessor-Support sowie die Unterstützung von verschlüsselten Dateisystemen. |
| **02.01.2012 :** | Version 1.1 des DOS-kompatiblen Betriebssystems [FreeDOS](FreeDOS "FreeDOS") wurde [heute veröffentlicht](http://sourceforge.net/news/?group_id=5109&id=305444). Gegenüber dem letzten Release wird nun standardmäßig ein TCP/IP-Stack mitgeliefert. Außerdem wird nun USB dank eines UHCI-Treibers unterstützt. Weitere Änderungen können der [Ankündigung](http://www.ibiblio.org/pub/micro/pc-stuff/freedos/files/distributions/1.1/announce.txt) entnommen werden. |
| **01.12.2011 :** | Nach 8 Jahren Entwicklung hat sich [QEMU](QEMU "QEMU") von der führenden Null in der Version getrennt und wurde heute als Version 1.0 freigegeben. Einen Überblick über die Änderungen kann man sich im [Changelog](http://wiki.qemu.org/ChangeLog/1.0) verschaffen. |
| **30.08.2011 :** | Mittlerweile ist die Version 4.6.1 der beliebten und im OS-Dev-Bereich vorherrschenden [GNU Compiler Collection](http://gcc.gnu.org/gcc-4.6/) erschienen. Diese bietet neben üblichen Optimierungen auch experimentelle Unterstützung für den zukünftigen neuen C-Standard *C1X*. Eine Liste aller Änderungen ist [hier](http://gcc.gnu.org/gcc-4.6/changes.html) einsehbar. |
| **09.08.2011 :** | Es ist zwar Dienstag, aber jetzt ist die Version 0.15.0 von [QEMU](QEMU "QEMU") erschienen. Sie enthält Untstützung für [EHCI](Enhanced-Host-Controller-Interface "EHCI")-USB-Hostcontroller und etliche andere USB-bezogene Verbesserungen. Ab Linux 3.0 funktionieren jetzt auch Ping-Pakete mit dem Usermode-Netzwerkstack. Weitere Details sind im [Changelog](http://wiki.qemu.org/ChangeLog/0.15) nachzulesen. |
| **05.08.2011 :** | Jidder hat eine OS-Dev-technisch hochinteressante Frage in den Raum gestellt, nämlich was man mal in die News schreiben könnte, damit am Montag nicht zweimal QEMU oben steht. |
| **22.03.2011 :** | [ReactOS](ReactOS "ReactOS") wurde in der Version 0.3.13 veröffentlicht. Im ReactOS Wiki gibt es wie üblich den [Changelog](http://www.reactos.org/wiki/ChangeLog-0.3.13). |
| **18.02.2011 :** | [QEMU](QEMU "QEMU") wurde in der Version 0.14.0 veröffentlicht. Unter anderem sind eine Emulation für AHCI- und HD-Audio-Geräte dazugekommen. Verbessert wurde die Implementierung von PCI (Express), neu ist hier z. B. Unterstützung für [MSI](Message-Signaled-Interrupt "MSI"). Weitere Details sind im [Changelog](http://wiki.qemu.org/Changelog/0.14) nachzulesen. |
| **20.10.2010 :** | [ReactOS](ReactOS "ReactOS") wurde in der Version 0.3.12 veröffentlicht. Im ReactOS Wiki gibt es wie üblich den [Changelog](http://www.reactos.org/wiki/index.php/ChangeLog-0.3.12). |
| **18.10.2010 :** | [QEMU](QEMU "QEMU") hat die Version 0.13.0 erreicht. Aus Sicht eines OS-Entwicklers für x86 enthält das Release vor allem viele kleinere Verbesserungen und Fehlerkorrekturen in der Hardwareemulation. Das neue Gerät *isa-debugcon* unterstützt jetzt den von bochs bekannten Debugport 0xe9. Der OHCI-Controller *pci-ohci* wird jetzt standardmäßig gebaut und ist damit zukünftig auch in Binärpaketen enthalten. |
| **25.04.2010 :** | [bochs](Bochs "Bochs") ist in Version 2.4.5 erschienen. Die Änderungen – die es [hier](http://bochs.cvs.sourceforge.net/bochs/bochs/CHANGES?view=markup&content-type=text/vnd.viewcvs-markup&revision=REL_2_4_5_FINAL) gibt – sind abgesehen von der Implementierung der x2APIC, des Intel-VMXx2-Instruktionensatzes und einer Geräteemulation für einen USB-HP-DeskJet-920C-Drucker nur Bugfixes. |
| **14.04.2010 :** | Die Version 4.5 der [GNU Compiler Collection](GNU-Compiler-Collection "GCC") wurde freigegeben. In dieser Version sind erstmals Optimierungen zur Linkzeit (LTO, über die Kommandozeilenoption -flto) enthalten. Außerdem wurde die Unterstützung für Features aus dem nächsten C++-Standard erweitert. Eine detaillierte Übersicht über die Änderungen findet sich [hier](http://gcc.gnu.org/gcc-4.5/changes.html). |
| **06.03.2010 :** | GRUB 1.98 ist erschienen. [Hier](http://grub.enbug.org/FrontPage?action=show&redirect=StartSeite) gibt es den Sourcecode und mehr Informationen zu GRUB2. |

*Ältere Nachrichten sind im [Archiv](Newsarchiv "Newsarchiv") zu finden*

****Übersicht****

**[OS-Dev für Einsteiger](Kategorie-OS-Dev-f%C3%BCr-Einsteiger "Kategorie:OS-Dev für Einsteiger")**

- [Grobüberblick](OS-Dev-f%C3%BCr-Einsteiger "OS-Dev für Einsteiger")
- [Teil 1 - Entwicklungsumgebung](Teil-1-Entwicklungsumgebung "Teil 1 - Entwicklungsumgebung")
- [Teil 2 - Assembler 101](Teil-2-Assembler-101 "Teil 2 - Assembler 101")
- [Teil 3 - Trockenübungen](Teil-3-Trocken%C3%BCbungen "Teil 3 - Trockenübungen")
- [Teil 4 - Hello World](Teil-4-Hello-World "Teil 4 - Hello World")
- [Teil 5 - Interrupts](Teil-5-Interrupts "Teil 5 - Interrupts")
- [Teil 6 - Multitasking](Teil-6-Multitasking "Teil 6 - Multitasking")
- [Teil 7 - Physische Speicherverwaltung](Teil-7-Physische-Speicherverwaltung "Teil 7 - Physische Speicherverwaltung")
- [Teil 8 - Ein erstes Programm](Teil-8-Ein-erstes-Programm "Teil 8 - Ein erstes Programm")
- [Teil 9 - Paging](Teil-9-Paging "Teil 9 - Paging")

**Prozessor**

- [Interrupt](Interrupt "Interrupt")
- [Multithreading](Multithreading "Multithreading")
- [x86](X86 "X86")
  - [FPU](Mathematischer-Koprozessor "FPU")
  - [Real Mode](Real-Mode "Real Mode")
    - [IVT](Interrupt-Vector-Table "IVT")
    - [BIOS](Basic-Input-Output-System "BIOS")
  - [Protected Mode](Protected-Mode "Protected Mode")
    - [GDT](Global-Descriptor-Table "GDT")
    - [IDT](Interrupt-Descriptor-Table "IDT")
    - [Multitasking](Multitasking "Multitasking") & [TSS](Task-State-Segment "TSS")
    - [Paging](Paging "Paging")
    - [Virtual 8086 Mode](Virtual-8086-Mode "Virtual 8086 Mode")
  - [System Management Mode](System-Management-Mode "System Management Mode")
- [x86-64](X86-64 "X86-64")
  - [Long Mode](Long-Mode "Long Mode")
- [ARM](ARM "ARM")

**[Kernel](Kernel "Kernel")**

- [Hardwareabstraktionsschicht](Hardware-Abstraction-Layer "Hardware Abstraction Layer")
- [Speicherverwaltung](Speicherverwaltung "Speicherverwaltung")
- [Prozessverwaltung](Prozessverwaltung "Prozessverwaltung")
- [Scheduler](Scheduler "Scheduler")

**Für Spaß im Userspace**

- [Interprozesskommunikation](Interprozesskommunikation "Interprozesskommunikation")
- [Heapverwaltung](Heapverwaltung "Heapverwaltung")
- [Systemaufrufe (Syscalls)](Syscall "Systemaufruf")
- [Virtuelles Dateisystem](Virtuelles-Dateisystem "Virtuelles Dateisystem")
- [Standardbibliothek](Standardbibliothek "Standardbibliothek")
- [Threads](Prozess#threads "Thread") (auch: [pthreads](POSIX-Threads "Pthread"))
- [Shell](Shell "Shell")
- [Software portieren](Portieren-von-Programmen-und-Bibliotheken "Portieren von Programmen und Bibliotheken")

**[Hardware](Kategorie-Hardware "Kategorie:Hardware")**

- [ATA](AT-Attachment "ATA")
- [DMA](Direct-Memory-Access "DMA")
- [serielle Schnittstelle](Serielle-Schnittstelle "Serielle Schnittstelle")
- [parallele Schnittstelle](Parallele-Schnittstelle "Parallele Schnittstelle")
- [Textausgabe](Textausgabe "Textausgabe")
- [Netzwerkkarten](Kategorie-Netzwerkkarte "Kategorie:Netzwerkkarte")
  - [Realtek RTL8139](RTL8139 "RTL8139")
  - [AMD PCnet-FAST III](AMD-PCnet "AMD PCnet")
- Grafikkarten
  - [VGA](Video-Graphics-Array "VGA")
  - [Cirrus Logic](Cirrus-Logic "Cirrus Logic")
- [Soundkarten](Kategorie-Soundkarte "Kategorie:Soundkarte")
  - [Gameport](Gameport "Gameport")
- IBM PC-spezifisch
  - [APIC](Advanced-Programmable-Interrupt-Controller "APIC")
  - [CMOS](CMOS "CMOS")
  - [Diskettenlaufwerk](Floppy-Disk-Controller "FDC")
  - [PS/2 Tastatur](Keyboard-Controller "KBC")
  - [PS/2 Maus](PS-2-Maus "Programmierung der PS/2-Maus")
  - [PIC](Programmable-Interrupt-Controller "PIC")
  - [PIT](Programmable-Interval-Timer "PIT")
  - [Systemlautsprecher](Systemlautsprecher "Systemlautsprecher")

**[Bussysteme](Kategorie-Bus "Kategorie:Bus")**

- [ISA](Industry-Standard-Architecture "ISA")
- [EISA](Industry-Standard-Architecture#extended-industry-standard-architecture "EISA")
- [PCI](Peripheral-Component-Interconnect "PCI")
- [USB](Universal-Serial-Bus "USB")

**Hobby-[OS](Kategorie-Betriebssystem "Kategorie:Betriebssystem")**

- [MyXomycota](MyXomycota "MyXomycota")
- [týndur](T%C3%BDndur "Týndur")
- [Xantorix](Xantorix "Xantorix")
- [LF OS](LF-OS "LF OS")
- Weitere: [Kategorie Betriebssysteme](Kategorie-Betriebssystem "Kategorie:Betriebssystem")

**[Dateisysteme](Dateisystem "Dateisystem")**

- [Ext2](Ext2 "Ext2")
- [Ext3](Ext3 "Ext3")
- [FAT](File-Allocation-Table "FAT")
- [ISO9660](ISO9660 "ISO9660")
- [NTFS](NTFS "NTFS")
- weitere: [Kategorie:Dateisystem](Kategorie-Dateisystem "Kategorie:Dateisystem")

**[Sprachen](Kategorie-Programmiersprache "Kategorie:Programmiersprache")**

- [Assembler](Assembler "Assembler")
- [C](C "C")
- [C++](C%2B%2B "C++")
- [D](D "D")
- [FreeBASIC](FreeBASIC "FreeBASIC")
- [Pascal](Pascal "Pascal")
- weitere: [Kategorie:Programmiersprache](Kategorie-Programmiersprache "Kategorie:Programmiersprache")

**Verschiedenes**

- [Glossar](Kategorie-Glossar "Kategorie:Glossar")
- [Linkliste](Linkliste "Linkliste")
- [TODO](TODO "TODO")
- [Zitate](Zitate "Zitate")
- [Tutorials](Kategorie-Tutorials "Kategorie:Tutorials")
- [Literatur](Literatur "Literatur")
- Alle Kategorien

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/11520/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1712/index.html)

<!-- MediaWiki page 1712; revision 11520; parent 11440; 2020-09-18T13:55:33Z -->
