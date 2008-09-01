# MeinOS

| meinOS |  |
| ----------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
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
| [IPC-Methode](https://github.com/lowlevel-eu/wiki/wiki/Interprozesskommunikation "IPC"): | [RPC](https://github.com/lowlevel-eu/wiki/wiki/Interprozesskommunikation#rpc-remote-procedure-call "RPC") (synchron), Message Queues (SysV), [Semaphores](https://github.com/lowlevel-eu/wiki/wiki/Interprozesskommunikation#semaphore "Semaphore") (SysV), [Shared Memory](https://github.com/lowlevel-eu/wiki/wiki/Interprozesskommunikation#shared-memory "Shared Memory") (SysV), [Signale](https://github.com/lowlevel-eu/wiki/wiki/Interprozesskommunikation "Signale") |
| Homepage |  |

<http://jgraef.bplaced.net/meinos/>

  
meinOS ist ein [Microkernel](https://github.com/lowlevel-eu/wiki/wiki/Ausgabe-2#der-microkernel "Ausgabe 2")-Betriebssystem für x86-Systeme. Es wird von [jgraef](https://lowlevel-eu.github.io/wiki/pages/1550/index.html "Benutzer:Jgraef") entwickelt.

## Entwicklung

Der neue Kernel ist soweit fertig. Die größten Verbesserungen waren in den Bereichen Speicherverwaltung (u.a. dynamischerer Speicherallokator für den Kernel, wodurch nun Linked Lists im Kernel benutzt werden können), Prozessverwaltung und IPC. Kernel2 unterstützt nun die SysV-IPC-Methoden, RPC und Signale. Außerdem wurde FUSE auf das VFS von meinOS portiert. Im Moment wird das DevFS auf Fuse portiert.

### Komplett

- [Kernel](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel")
  - [Speicherverwaltung](https://github.com/lowlevel-eu/wiki/wiki/Speicherverwaltung "Speicherverwaltung")
  - [Prozessverwaltung](https://github.com/lowlevel-eu/wiki/wiki/Prozessverwaltung "Prozessverwaltung")
  - IPC
    - [Message Queues](https://github.com/lowlevel-eu/wiki/wiki/Interprozesskommunikation#message-queues "Message Queue") (SysV)
    - [Shared Memory](https://github.com/lowlevel-eu/wiki/wiki/Interprozesskommunikation#shared-memory "Shared Memory") (SysV)
    - [Semaphores](https://github.com/lowlevel-eu/wiki/wiki/Interprozesskommunikation#semaphore "Semaphore") (SysV)
    - [Remote Procedure Call](https://github.com/lowlevel-eu/wiki/wiki/Interprozesskommunikation#rpc-remote-procedure-call "Remote Procedure Call")
    - [Signale](https://github.com/lowlevel-eu/wiki/wiki/Interprozesskommunikation "Signale")
  - [Multiboot](https://github.com/lowlevel-eu/wiki/wiki/Multiboot "Multiboot")-Kompatibilität

<!-- -->

- Server (Treiber)
  - Console-Server (umfasst Keyboard-Treiber und Screen-Treiber)
  - [COM](https://github.com/lowlevel-eu/wiki/wiki/Serielle-Schnittstelle "COM")-Server
  - [Floppy](https://github.com/lowlevel-eu/wiki/wiki/Floppy-Disk-Controller "Floppy")-Server ([CDI](https://github.com/lowlevel-eu/wiki/wiki/Common-Driver-Interface "CDI"))
  - [VFS](https://github.com/lowlevel-eu/wiki/wiki/Virtuelles-Dateisystem "VFS")-Server
  - DevFS

<!-- -->

- Bibliotheken
  - libmeinos
    - [CMOS](https://github.com/lowlevel-eu/wiki/wiki/CMOS "CMOS")
    - DevFS
    - [DMA](https://github.com/lowlevel-eu/wiki/wiki/Direct-Memory-Access "DMA")
    - [RPC](https://github.com/lowlevel-eu/wiki/wiki/Interprozesskommunikation#rpc-remote-procedure-call "RPC")
    - Linked List
    - [PCI](https://github.com/lowlevel-eu/wiki/wiki/Peripheral-Component-Interconnect "PCI")
  - stdlibc (großer Teil schon portiert)
  - [libcdi](https://github.com/lowlevel-eu/wiki/wiki/Common-Driver-Interface "CDI") (ohne cdi.net)
  - libfuse

### Planung

- Init-Task (Initialisierung aller Treiber und des Login-Programms)
- [Shell](https://github.com/lowlevel-eu/wiki/wiki/Shell "Shell") (eventuell Portierung einer vorhandenen Shell)
- [Ext2](https://github.com/lowlevel-eu/wiki/wiki/Ext2 "Ext2")-Treiber (Fuse)
- VFAT-Treiber (Fuse)
- [NTFS](https://github.com/lowlevel-eu/wiki/wiki/NTFS "NTFS")-Treiber (Fuse)
- Standard-Unix-Toolchain: echo,cat,mv,cp,... und GCC-Toolchain

Wie man sieht, ist noch eine Menge zu tun.

## Crosscompiler

Im Moment wird für meinOS noch ein Crosscompiler plus Toolchain gebaut, um das Portieren größerer Applikationen zu vereinfachen.

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

![meinos.gif](http://jgraef.bplaced.net/meinos/screenshots/meinos.gif)

## Weblinks

- [Website von meinOS](http://jgraef.bplaced.net/meinos/index.php)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/3282/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1551/index.html)

<!-- MediaWiki page 1551; revision 3282; parent 3222; 2008-09-01T08:56:04Z -->
