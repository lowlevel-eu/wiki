# Universe

Universe ist als benutzerfreundliches universelles Desktop-Betriebssystem geplant. Es soll später möglich sein auf Universe Linux und eventuell Windows Applikationen auszuführen. Dieses Ziel liegt jedoch noch in weiter Ferne. Aktuell handelt es sich um einen einfachen Hybrid-Kernel mit einem kleinen Treibersatz. Es wird seit 2009 entwickelt. Der Großteil der Universe-Versionen wurden für den [Real Mode](https://github.com/lowlevel-eu/wiki/wiki/Real-Mode "Real Mode") entwickelt erst ab Version 0.7 läuft das System im [Protected Mode](https://github.com/lowlevel-eu/wiki/wiki/Protected-Mode "Protected Mode"). Wir entschieden uns die Floppy Disk Varriante ohne GUI, DDOS zu nennen.

| Universe |  |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|  |  |
| Entwickler: | Tdotu |
| Akt. Version: | 0.8 (in Entwicklung) |
| [Lizenz](https://github.com/lowlevel-eu/wiki/wiki/Lizenzen "Lizenzen"): | UPL |
| OS-Eigenschaften |  |
| Plattform: | [x86](https://github.com/lowlevel-eu/wiki/wiki/X86 "X86"),[x64](https://github.com/lowlevel-eu/wiki/wiki/X86-64 "X64") |
| [Kernelart](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel"): | Hybrid |
| [Sprache](https://lowlevel-eu.github.io/wiki/pages/1648/index.html "Kategorie:Programmiersprache"): | Assembler/C/C++ |
| API: | nativ, [POSIX](https://github.com/lowlevel-eu/wiki/wiki/POSIX "POSIX") |
| Binärformat: | UEF,[ELF](https://github.com/lowlevel-eu/wiki/wiki/Executable-and-Linking-Format "ELF"),UMM |
| [IPC-Methode](https://github.com/lowlevel-eu/wiki/wiki/Interprozesskommunikation "IPC"): | [Shared Memory](https://github.com/lowlevel-eu/wiki/wiki/Interprozesskommunikation#shared-memory "Shared Memory"),[RPC](https://github.com/lowlevel-eu/wiki/wiki/Interprozesskommunikation#rpc-remote-procedure-call "RPC") |
| Homepage |  |

<http://universe.de.tc> (nur vorläufig)

  

  

  

## Universe 0.8 (Kernel 1.00)

**Die Entwicklung pausiert momentan, bis ein genauer Plan für Die Kernel Architektur feststeht. Es kann sein das ich das System umbenennen werde. Das liegt vor allem daran, das man im Web vereinzelt Seiten über ein "Universe-OS" findet, die nicht von mir sind und ich Verwechselungen vermeiden möchte.**

**Nachtrag: Die Richtung und der grobe Kernelaufbau stehen jetzt fest. Ich werde nun 60% des ursprünglichen Codes neu schreiben um ihn Multiprozessor-system tauglich zu machen und um ihn an den neuen Aufbau an zu passen. So bald die Sache wieder brauchbare Maße angenommen hat, werde ich diesen Artikel aktualisieren.**

## Versionen

Bisher fertiggestellte Versionen:

| Version | Änderungen/Fähigkeiten |
| --------- | ---------------------------------------------------------------------------------------------------------- |
| 0.1 | Einfaches bootbares „Hello world!“ Programm mit eigenem Bootloader(nur ASM) |
| 0.2 | Textbasiertes Logo (nur ASM) |
| 0.3 | Erster Versuch mit C-Kernel(C/ASM) |
| 0.4 | Neustart- und Herunterfahrfunktionen (C/ASM) |
| 0.5 | Funktionsmenü (nur ASM) |
| 0.6 | Graphischer Editor mit Druckfunktion + Lade und Startfunktion für binäre Programme (nur ASM) |
| 0.7 | Erste Versuche mit dem Protected Mode und Vesa (Version wegen hoher Fehlerquote als gescheitert erklärt) |

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/10596/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2498/index.html)

<!-- MediaWiki page 2498; revision 10596; parent 10589; 2012-05-07T21:06:11Z -->
