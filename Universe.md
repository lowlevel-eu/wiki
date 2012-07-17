# Universe

Universe ist als benutzerfreundliches universelles Desktop-Betriebssystem geplant. Es soll später möglich sein auf Universe Linux Applikationen auszuführen. Dieses Ziel liegt jedoch noch in weiter Ferne.

| Universe |  |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|  |  |
| Entwickler: | Tdotu |
| Akt. Version: | 0.8 (in Entwicklung) |
| [Lizenz](https://github.com/lowlevel-eu/wiki/wiki/Lizenzen "Lizenzen"): | GNU GPL |
| OS-Eigenschaften |  |
| Plattform: | [x86](https://github.com/lowlevel-eu/wiki/wiki/X86 "X86"),[x64](https://github.com/lowlevel-eu/wiki/wiki/X86-64 "X64"),[ARM](https://github.com/lowlevel-eu/wiki/wiki/ARM "ARM") |
| [Kernelart](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel"): | Hybrid |
| [Sprache](https://lowlevel-eu.github.io/wiki/pages/1648/index.html "Kategorie:Programmiersprache"): | Assembler/C/C++ |
| API: | nativ, [POSIX](https://github.com/lowlevel-eu/wiki/wiki/POSIX "POSIX") |
| Binärformat: | UEF,[ELF](https://github.com/lowlevel-eu/wiki/wiki/Executable-and-Linking-Format "ELF"),UMM |
| [IPC-Methode](https://github.com/lowlevel-eu/wiki/wiki/Interprozesskommunikation "IPC"): | [Shared Memory](https://github.com/lowlevel-eu/wiki/wiki/Interprozesskommunikation#shared-memory "Shared Memory"),[RPC](https://github.com/lowlevel-eu/wiki/wiki/Interprozesskommunikation#rpc-remote-procedure-call "RPC") |
| Homepage |  |

<http://www.infinitycoding.de/index.php?inhalt=Universe>

  

## Universe aktuell

Aktuell handelt es sich um einen einfachen Hybrid-Kernel mit einem kleinen Treibersatz. Es wird seit 2009 entwickelt. Der Großteil der Universe-Versionen wurden für den [Real Mode](https://github.com/lowlevel-eu/wiki/wiki/Real-Mode "Real Mode") entwickelt. Erst ab Version 0.7 läuft das System im [Protected Mode](https://github.com/lowlevel-eu/wiki/wiki/Protected-Mode "Protected Mode"). Die Floppy Disk Variante des Systems ohne GUI heißt DDOS. Es kann sein das ich das System umbenennen werde. Das liegt vor allem daran, das man im Web vereinzelt Seiten über ein "Universe-OS" findet, die nicht von mir sind und ich Verwechselungen vermeiden möchte.

  

## Universe Kernel 1.0 (Planung/in Arbeit)

Hybrid Kernel mit folgenden integrierten Treibern:

- Blocktreiber für Bootlaufwerk (FDC + ATA)
- Dateisystemtreiber für das Bootlaufwerk ([FAT](https://github.com/lowlevel-eu/wiki/wiki/File-Allocation-Table "FAT") und EXT)
- DMA Treiber
- Standard Konsolen/Grafiktreiber

  
Diese Treiber sind in das Kernel gelinkt und sind standardmäßig verfügbar. Das System kann jedoch auch von Dateisystemen und Laufwerken gestartet werden, deren Treiber nicht direkt im Kernel verankert sind. Diese dienen lediglich dazu dem Kernel die Möglichkeit zu geben das System ohne "externe Treiber" zu nutzen und die Basisfunktionen des Kernels sicher zu gewährleisten. Die Funktionalitäten der Treiber (abgesehen der Funktionen des DMA Treibers) können auch von externen Treibern abgelöst werden. Als "extern" werden alle Treiber Bezeichnet die nicht im Kernel integriert sind und ihre Funktionen über den Treiberinterface oder direktes IPC zur Verfügung stellen.

  
**Interfaces:**

- CDI
- POSIX API (über int \$0x80, oder über einen dynamischen Syscall)
- Universe API (nur über einen dynamischen Syscall)

**IPC Systeme:**

- RPC
- Shared Memory
- Buffered RPC

**Portierungen:**

- stdlibc
- FASM

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/10650/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2498/index.html)

<!-- MediaWiki page 2498; revision 10650; parent 10632; 2012-07-17T12:54:53Z -->
