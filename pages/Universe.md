# Universe

Universe soll ein schlankes, universelles (deswegen auch der Name, wer hätte das nur gedacht ;)) und modulares Betriebssystem werden, bei dem Sicherheit besonders groß geschrieben wird.

| Universe |  |
| ----------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
|  |  |
| Entwickler: | InfinityCoding |
| Akt. Version: | 1.0 (in Entwicklung) |
| [Lizenz](Lizenzen "Lizenzen"): | GPL v3, LGPL (libc) |
| OS-Eigenschaften |  |
| Plattform: | [x86](X86 "X86"), [ARM](ARM "ARM")(In Arbeit) |
| [Kernelart](Kernel "Kernel"): | Micro-Kernel |
| [Sprache](Kategorie-Programmiersprache "Kategorie:Programmiersprache"): | Assembler/C |
| API: | nativ, [POSIX](POSIX "POSIX") |
| Binärformat: | [ELF](Executable-and-Linking-Format "ELF") |
| [IPC-Methode](Interprozesskommunikation "IPC"): | [Pipes](Pipe "Pipe") |
| Homepage |  |

(in Arbeit)

  

## Universe aktuell

Aktuell handelt es sich um einen einfachen Microkernel mit einem kleinen Treibersatz. Es wird in dieser Form seit 2012 entwickelt. Die aktuellsten Neuerungen sind die Einführung eines universellen Kommunikationsprotokolls für Treiber und die Portierung diverser Tools.

  

## Universe Kernel 1.0 (Planung/in Arbeit)

- Blocktreiber für Bootlaufwerk (CD + ATA)
- Dateisystemtreiber für das Bootlaufwerk ([FAT](File-Allocation-Table "FAT") und EXT)
- Standard Konsolen/Grafiktreiber
- vollständige Portierung der core-utils

Die Treiber sind wie für ein Microkernel üblich außerhalb des Kernels und kommunizieren mittels UDRCP-Protokolls. Dieses Protokoll erlaubt auch das dynamische verändern der Treiberpiplines.

  

**Interfaces:**

- CDI
- POSIX API (über int \$0x80, oder über einen dynamischen Syscall)
- Universe API (nur über einen dynamischen Syscall)

**IPC Systeme:**

- Pipes

**Portierungen:**

- stdlibc (In Arbeit)
- zlib
- fasm
- gcc (in Arbeit)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/11190/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2498/index.html)

<!-- MediaWiki page 2498; revision 11190; parent 11152; 2014-04-11T19:53:44Z -->
