# MeinOS

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

## Download

- Unoffizielles Release vom 12.02.08 (Build 415):
  - Floppy-Image: [floppy.img.gz](http://jgraef.bplaced.net/meinos/downloads/floppy_build415.img.gz) (335,4kB)
- Unoffizielles Release vom 20.12.07:
  - Floppy-Image: [floppy.img.gz](http://jgraef.bplaced.net/meinos/downloads/floppy.img.gz) (195,4kB)
  - Sourcecode: [meinos.tar.gz](http://jgraef.bplaced.net/meinos/downloads/meinos.tar.gz) (460kB)

## Screenshot (Unoffizielles Release vom 12.02.08 (Build 415))

![screen.gif](http://jgraef.bplaced.net/meinos/screenshots/screen.gif)

## Weblinks

- [Website von meinOS](http://jgraef.bplaced.net/meinos/index.php)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/2574/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1551/index.html)

<!-- MediaWiki page 1551; revision 2574; parent 2557; 2008-02-12T19:58:27Z -->
