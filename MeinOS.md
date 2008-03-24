# MeinOS

| meinOS |  |
| ----------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
|  |  |
| Entwickler: | [Janosch Gräf](https://lowlevel-eu.github.io/wiki/pages/1550/index.html "Benutzer:Jgraef") |
| Akt. Version: | noch keine |
| [Lizenz](https://github.com/lowlevel-eu/wiki/wiki/Lizenzen "Lizenzen"): | GNU GPL |
| OS-Eigenschaften |  |
| Plattform: | x86 |
| [Kernelart](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel"): | Microkernel |
| [Sprache](https://lowlevel-eu.github.io/wiki/pages/1648/index.html "Kategorie:Programmiersprache"): | [C](https://github.com/lowlevel-eu/wiki/wiki/C "C") |
| API: | [POSIX](https://github.com/lowlevel-eu/wiki/wiki/POSIX "POSIX") |
| Binärformat: | Elf |
| [IPC-Methode](https://github.com/lowlevel-eu/wiki/wiki/Interprozesskommunikation "IPC"): | Message Passing |
| Homepage |  |

<http://jgraef.bplaced.net/meinos/>

  
meinOS ist ein [Microkernel](https://github.com/lowlevel-eu/wiki/wiki/Ausgabe-2#der-microkernel "Ausgabe 2")-Betriebssystem für x86-Systeme. Außerdem unterstützt meinOS Mehrprozessor-Systeme. Es wird von [jgraef](https://lowlevel-eu.github.io/wiki/pages/1550/index.html "Benutzer:Jgraef") entwickelt.

## Entwicklung

Im Moment werden einige Kernel-Funktionen noch vollendet und es müssen noch viele Treiber geschrieben werden. Einige Programme/Bibliotheken müssen auch noch getestet werden

### Komplett (oder noch in Arbeit)

- Kernel
  - Memorymanagement (todo: noch nicht ganz fertig)
  - Multiprocessor-Kompatibilität (todo: noch nicht vollständig)
  - Taskmanagement
  - IPC (Message Passing)
  - [Multiboot](https://github.com/lowlevel-eu/wiki/wiki/Multiboot "Multiboot")-Kompatibilität
  - Signals (todo: Kernel-Schnittstelle)
  - Timer-Schnittstelle

<!-- -->

- Server
  - Keyboard-Server
  - Console-Server
  - COM-Server
  - Floppy-Server (mit CDI ist das ja kein Problem mehr)
  - Filesystem-Server (noch in Arbeit)

<!-- -->

- Bibliotheken
  - libmeinos (enthält cmos, devfs, DMA, IPC, PCI
  - stdlibc (natürlich noch nicht komplett)
  - libcdi (cdi.net noch nicht implementiert; testen wäre angebracht)

### Planung

- Init-Task (Initialisierung aller Treiber und des Login-Programms)
- Shell (eventuell Portierung einer vorhandenen Shell)
- devfs (FS-Treiber für /dev)
- Ext2-Treiber
- eventuell pipefs (Für Named Pipes ohne "richtiges" FS, dass Named Pipes unterstützt)
- Einige kleine Programme (cp, mv, rm, mkfile, cat, echo, usw.)

Wie man sieht, ist noch eine Menge zu tun.

## Download

- Unoffizielles Release vom 14.03.08 (Build 1872):
  - Floppy-Image: [floppy.img.gz](http://jgraef.bplaced.net/meinos/downloads/floppy_build1872.img.gz) (406,1kB)  
    Note: VFS oder DevFS pagefaultet manchmal, der Fehler wird natürlich noch behoben. Diese Version soll nur das virtuelle Dateisystem demonstrieren.
- Unoffizielles Release vom 12.02.08 (Build 415):
  - Floppy-Image: [floppy.img.gz](http://jgraef.bplaced.net/meinos/downloads/floppy_build415.img.gz) (335,4kB)
- Unoffizielles Release vom 20.12.07:
  - Floppy-Image: [floppy.img.gz](http://jgraef.bplaced.net/meinos/downloads/floppy.img.gz) (195,4kB)
  - Sourcecode: [meinos.tar.gz](http://jgraef.bplaced.net/meinos/downloads/meinos.tar.gz) (460kB)

## Screenshot (Unoffizielles Release vom 14.03.08 - Build 1781)

![screen.gif](http://jgraef.bplaced.net/meinos/screenshots/screen.gif)

## Weblinks

- [Website von meinOS](http://jgraef.bplaced.net/meinos/index.php)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/2813/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1551/index.html)

<!-- MediaWiki page 1551; revision 2813; parent 2628; 2008-03-24T21:28:50Z -->
