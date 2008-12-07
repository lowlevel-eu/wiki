# MeinOS

| meinOS |  |
| ----------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|  |  |
| Entwickler: | [Janosch Gräf](https://lowlevel-eu.github.io/wiki/pages/1550/index.html "Benutzer:Jgraef") |
| Akt. Version: | noch keine |
| [Lizenz](https://github.com/lowlevel-eu/wiki/wiki/Lizenzen "Lizenzen"): | GPL, LGPL, BSD |
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

Dank zweier 12h-Programmier-Sessions ist meinOS ein ganzes Stück weiter. Fork() und execute() funktionieren. Init startet alle Treiber und sonstige Programme (/etc/init.d). Stdin, stdout ud stderr werden nicht mehr zum Kernel geleitet, sondern über Unnamed Pipes zum Elternprozess. Außerdem läuft jetzt eine Shell. Leider funktionieren die Unnamed Pipes aber noch nicht so gut und der Keyboard-Treiber macht auch Probleme. Deswegen kann ich niemanden empfehlen andere Programme als "true" und "false" in der Shell zu starten.

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
  - [ATA](https://github.com/lowlevel-eu/wiki/wiki/AT-Attachment "ATA") (mit ATAPI)
  - CDROM
  - [Cirrus Logic](https://github.com/lowlevel-eu/wiki/wiki/Cirrus-Logic "Cirrus Logic")
  - [COM](https://github.com/lowlevel-eu/wiki/wiki/Serielle-Schnittstelle "COM")
  - Console ( [Tastatur](https://github.com/lowlevel-eu/wiki/wiki/Keyboard-Controller "Keyboard Controller")
  - DevFS
  - [DMA](https://github.com/lowlevel-eu/wiki/wiki/Direct-Memory-Access "DMA")
  - [FAT](https://github.com/lowlevel-eu/wiki/wiki/File-Allocation-Table "FAT")
  - [Floppy](https://github.com/lowlevel-eu/wiki/wiki/Floppy-Disk-Controller "Floppy")
  - [ISO9660](https://github.com/lowlevel-eu/wiki/wiki/ISO9660 "ISO9660")
  - [PCI](https://github.com/lowlevel-eu/wiki/wiki/Peripheral-Component-Interconnect "PCI")
  - Pseudo-Geräte (/dev/null, /dev/zero/ und /dev/urandom)
  - Ramdisk
  - VFS

<!-- -->

- Bibliotheken
  - libmeinos
    - [CMOS](https://github.com/lowlevel-eu/wiki/wiki/CMOS "CMOS")
    - DevFS
    - [DMA](https://github.com/lowlevel-eu/wiki/wiki/Direct-Memory-Access "DMA")
    - [RPC](https://github.com/lowlevel-eu/wiki/wiki/Interprozesskommunikation#rpc-remote-procedure-call "RPC")
    - Linked List
    - Lock (Spinlock)
    - Path (zum parsen von Dateipfaden)
    - [PCI](https://github.com/lowlevel-eu/wiki/wiki/Peripheral-Component-Interconnect "PCI")
    - Process (Kontrolle über Prozesse)
  - stdlibc (großer Teil schon portiert)
  - [libcdi](https://github.com/lowlevel-eu/wiki/wiki/Common-Driver-Interface "CDI")
    - [BIOS](https://github.com/lowlevel-eu/wiki/wiki/Basic-Input-Output-System "BIOS")
    - Cache
    - [DMA](https://github.com/lowlevel-eu/wiki/wiki/Direct-Memory-Access "DMA")
    - FS
    - Generic (noch kein Standard)
    - Net
    - [PCI](https://github.com/lowlevel-eu/wiki/wiki/Peripheral-Component-Interconnect "PCI")
    - SCSI
    - Storage
    - Video
  - libfuse
- Nenneswerte Programme
  - init
  - login
  - shell (noch in Arbeit)
  - gzip
  - mount

### Planung

- NTFS-Treiber
- Standard-Unix-Toolchain: echo,cat,mv,cp,... und GCC-Toolchain

## Crosscompiler

Zum Bauen von meinOS wird der meinOS-Crosscompiler benötigt. Die Patches können hier gedownloadet werden:

- [gcc-4.2.2](http://repo.or.cz/w/meinos.git?a=blob;f=gcc-4.2.2-meinos.patch)
- [binutils-2.18](http://repo.or.cz/w/meinos.git?a=blob;f=binutils-2.18-meinos.patch)

## Download

Das aktuelle CD-Image kann hier gedownloadet werden: [meinos_cd_20081207.iso.gz](http://jgraef.bplaced.net/meinos/downloads/meinos_cd_20081207.iso.gz)

## Screenshot (07.12.2008)

![meinos.gif](http://jgraef.bplaced.net/meinos/screenshots/meinos.gif)

## Weblinks

- [Website von meinOS](http://jgraef.bplaced.net/meinos/)
- [GIT-Repository](http://repo.or.cz/w/meinos.git)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/3586/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1551/index.html)

<!-- MediaWiki page 1551; revision 3586; parent 3585; 2008-12-07T01:51:40Z -->
