# Universe

Universe ist als benutzerfreundliches universelles Desktop-Betriebssystem geplant. Es soll später möglich sein auf Universe Linux Applikationen auszuführen. Dieses Ziel liegt jedoch noch in weiter Ferne.

| Universe |  |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
|  |  |
| Entwickler: | InfinityCoding |
| Akt. Version: | (in Entwicklung) |
| [Lizenz](https://github.com/lowlevel-eu/wiki/wiki/Lizenzen "Lizenzen"): | GNU GPL |
| OS-Eigenschaften |  |
| Plattform: | [x86](https://github.com/lowlevel-eu/wiki/wiki/X86 "X86"), [ARM](https://github.com/lowlevel-eu/wiki/wiki/ARM "ARM")(In Arbeit), PowerPC(In Arbeit) |
| [Kernelart](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel"): | Hybrid |
| [Sprache](https://lowlevel-eu.github.io/wiki/pages/1648/index.html "Kategorie:Programmiersprache"): | Assembler/C/C++ |
| API: | nativ, [POSIX](https://github.com/lowlevel-eu/wiki/wiki/POSIX "POSIX") |
| Binärformat: | [ELF](https://github.com/lowlevel-eu/wiki/wiki/Executable-and-Linking-Format "ELF") |
| [IPC-Methode](https://github.com/lowlevel-eu/wiki/wiki/Interprozesskommunikation "IPC"): | [Pipes](https://github.com/lowlevel-eu/wiki/wiki/Pipe "Pipe") |
| Homepage |  |

(In Arbeit)

  

## Universe aktuell

Aktuell handelt es sich um einen einfachen Hybrid-Kernel mit einem kleinen Treibersatz. Es wird seit 2009 entwickelt.

  

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

- Pipes

**Portierungen:**

- stdlibc (In Arbeit)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/11151/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2498/index.html)

<!-- MediaWiki page 2498; revision 11151; parent 11150; 2013-10-15T20:17:53Z -->
