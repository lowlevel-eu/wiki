# MeinOS

| meinOS |  |
| ----------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|  |  |
| Entwickler: | [Janosch Gräf](https://lowlevel-eu.github.io/wiki/pages/1550/index.html "Benutzer:Jgraef") |
| Akt. Version: | noch keine |
| [Lizenz](Lizenzen "Lizenzen"): | GPL, LGPL, BSD |
| OS-Eigenschaften |  |
| Plattform: | [x86](X86 "X86") |
| [Kernelart](Kernel "Kernel"): | Microkernel |
| [Sprache](https://lowlevel-eu.github.io/wiki/pages/1648/index.html "Kategorie:Programmiersprache"): | [C](C "C") |
| API: | [POSIX](POSIX "POSIX"), Nativ |
| Binärformat: | [ELF](Executable-and-Linking-Format "ELF") |
| [IPC-Methode](Interprozesskommunikation "IPC"): | [RPC](Interprozesskommunikation#rpc-remote-procedure-call "RPC") (synchron), [Message Queues](Interprozesskommunikation#message-queues "Message Queue") (SysV), [Semaphores](Interprozesskommunikation#semaphore "Semaphore") (SysV), [Shared Memory](Interprozesskommunikation#shared-memory "Shared Memory") (SysV), [Signale](Interprozesskommunikation "Signale") |
| Homepage |  |

<http://jgraef.dyndns.org/meinos/>

  
meinOS ist ein [Microkernel](Ausgabe-2#der-microkernel "Ausgabe 2")-Betriebssystem für x86-Systeme. Es wird von [jgraef](https://lowlevel-eu.github.io/wiki/pages/1550/index.html "Benutzer:Jgraef") entwickelt.

## Entwicklung

Dank zweier 12h-Programmier-Sessions ist meinOS ein ganzes Stück weiter. Fork() und execute() funktionieren. Init startet alle Treiber und sonstige Programme (/etc/init.d). Stdin, stdout ud stderr werden nicht mehr zum Kernel geleitet, sondern über Unnamed Pipes zum Elternprozess. Außerdem läuft jetzt eine Shell. Leider funktionieren die Unnamed Pipes aber noch nicht so gut und der Keyboard-Treiber macht auch Probleme. Deswegen kann ich niemanden empfehlen andere Programme als "true" und "false" in der Shell zu starten.

### Komplett

- [Kernel](Kernel "Kernel")
  - [Speicherverwaltung](Speicherverwaltung "Speicherverwaltung")
  - [Prozessverwaltung](Prozessverwaltung "Prozessverwaltung")
  - IPC
    - [Message Queues](Interprozesskommunikation#message-queues "Message Queue") (SysV)
    - [Shared Memory](Interprozesskommunikation#shared-memory "Shared Memory") (SysV)
    - [Semaphores](Interprozesskommunikation#semaphore "Semaphore") (SysV)
    - [Remote Procedure Call](Interprozesskommunikation#rpc-remote-procedure-call "Remote Procedure Call")
    - [Signale](Interprozesskommunikation "Signale")
  - [Multiboot](Multiboot "Multiboot")-Kompatibilität

<!-- -->

- Server (Treiber)
  - Console-Server (umfasst Keyboard-Treiber und Screen-Treiber)
  - [ATA](AT-Attachment "ATA") (mit ATAPI)
  - CDROM
  - [Cirrus Logic](Cirrus-Logic "Cirrus Logic")
  - [COM](Serielle-Schnittstelle "COM")
  - Console ( [Tastatur](Keyboard-Controller "Keyboard Controller")
  - DevFS
  - [DMA](Direct-Memory-Access "DMA")
  - [FAT](File-Allocation-Table "FAT")
  - [Floppy](Floppy-Disk-Controller "Floppy")
  - [ISO9660](ISO9660 "ISO9660")
  - [PCI](Peripheral-Component-Interconnect "PCI")
  - Pseudo-Geräte (/dev/null, /dev/zero/ und /dev/urandom)
  - Ramdisk
  - VFS

<!-- -->

- Bibliotheken
  - libmeinos
    - [CMOS](CMOS "CMOS")
    - DevFS
    - [DMA](Direct-Memory-Access "DMA")
    - [RPC](Interprozesskommunikation#rpc-remote-procedure-call "RPC")
    - Linked List
    - Lock (Spinlock)
    - Path (zum parsen von Dateipfaden)
    - [PCI](Peripheral-Component-Interconnect "PCI")
    - Process (Kontrolle über Prozesse)
  - stdlibc (großer Teil schon portiert)
  - [libcdi](Common-Driver-Interface "CDI")
    - [BIOS](Basic-Input-Output-System "BIOS")
    - Cache
    - [DMA](Direct-Memory-Access "DMA")
    - FS
    - Generic (noch kein Standard)
    - Net
    - [PCI](Peripheral-Component-Interconnect "PCI")
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

- [Website von meinOS](http://jgraef.dyndns.org/meinos)
- [GIT-Repository](http://repo.or.cz/w/meinos.git)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/5546/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1551/index.html)

<!-- MediaWiki page 1551; revision 5546; parent 5281; 2009-08-10T15:38:52Z -->
