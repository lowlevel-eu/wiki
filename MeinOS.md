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
| API: | [POSIX](https://github.com/lowlevel-eu/wiki/wiki/POSIX "POSIX"), Nativ |
| Binärformat: | [ELF](https://github.com/lowlevel-eu/wiki/wiki/Executable-and-Linking-Format "ELF") |
| [IPC-Methode](https://github.com/lowlevel-eu/wiki/wiki/Interprozesskommunikation "IPC"): | RPC (synchron), Message Queues (SysV), Semaphores (SysV), Shared Memory (SysV), Signale |
| Homepage |  |

<http://jgraef.bplaced.net/meinos/>

  
meinOS ist ein [Microkernel](https://github.com/lowlevel-eu/wiki/wiki/Ausgabe-2#der-microkernel "Ausgabe 2")-Betriebssystem für x86-Systeme. Außerdem unterstützt meinOS Mehrprozessor-Systeme. Es wird von [jgraef](https://lowlevel-eu.github.io/wiki/pages/1550/index.html "Benutzer:Jgraef") entwickelt.

## Entwicklung

Der neue Kernel ist soweit fertig. Die größten Verbesserungen waren in den Bereichen Speicherverwaltung (u.a. dynamischerer Speicherallokator für den Kernel, wodurch nun Linked Lists im Kernel benutzt werden können), Prozessverwaltung und IPC. Kernel2 unterstützt nun die SysV-IPC-Methoden, RPC und Signale. Außerdem wurde FUSE auf das VFS von meinOS portiert. Im Moment wird das DevFS auf Fuse portiert.

### Komplett (oder so gut wie komplett)

- Kernel
  - [Speicherverwaltung](https://github.com/lowlevel-eu/wiki/wiki/Speicherverwaltung "Speicherverwaltung")
  - [Prozessverwaltung](https://github.com/lowlevel-eu/wiki/wiki/Prozessverwaltung "Prozessverwaltung")
  - IPC
    - Message Queues (SysV)
    - [Shared Memory](https://github.com/lowlevel-eu/wiki/wiki/Interprozesskommunikation#shared-memory "Shared Memory") (SysV)
    - Semaphores (SysV)
    - [Remote Procedure Call](https://github.com/lowlevel-eu/wiki/wiki/Interprozesskommunikation#rpc-remote-procedure-call "Remote Procedure Call")
    - [Signale](https://github.com/lowlevel-eu/wiki/wiki/Interprozesskommunikation "Signale")
  - [Multiboot](https://github.com/lowlevel-eu/wiki/wiki/Multiboot "Multiboot")-Kompatibilität

<!-- -->

- Server
  - Console-Server (umfasst Keyboard-Treiber und Screen-Treiber)
  - [COM](https://github.com/lowlevel-eu/wiki/wiki/Serielle-Schnittstelle "COM")-Server
  - [Floppy](https://github.com/lowlevel-eu/wiki/wiki/Floppy-Disk-Controller "Floppy")-Server ([CDI](https://github.com/lowlevel-eu/wiki/wiki/Common-Driver-Interface "CDI"))
  - [VFS](https://github.com/lowlevel-eu/wiki/wiki/Virtuelles-Dateisystem "VFS")-Server
  - DevFS

<!-- -->

- Bibliotheken
  - libmeinos
    - CMOS
    - DevFS
    - DMA
    - RPC
    - Linked List
    - PCI
  - stdlibc (großer Teil schon portiert)
  - libcdi (ohne cdi.net)

### Planung

- Init-Task (Initialisierung aller Treiber und des Login-Programms)
- Shell (eventuell Portierung einer vorhandenen Shell)
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

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/3217/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1551/index.html)

<!-- MediaWiki page 1551; revision 3217; parent 3034; 2008-08-18T09:27:19Z -->
