# AiCOS

| AiCOS |  |
| ----------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|  |  |
| Entwickler: | [ScollPi](https://lowlevel-eu.github.io/wiki/pages/1765/index.html "Benutzer:ScollPi") |
| Akt. Version: | Research Phase |
| [Lizenz](https://github.com/lowlevel-eu/wiki/wiki/Lizenzen "Lizenzen"): | n/a |
| OS-Eigenschaften |  |
| Plattform: | [x86](https://github.com/lowlevel-eu/wiki/wiki/X86 "X86") (später auch x64) |
| [Kernelart](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel"): | Modulares Kernel System (MKS) |
| [Sprache](https://lowlevel-eu.github.io/wiki/pages/1648/index.html "Kategorie:Programmiersprache"): | [Assembler](https://github.com/lowlevel-eu/wiki/wiki/Assembler "Assembler"), [C](https://github.com/lowlevel-eu/wiki/wiki/C "C")/[C++](https://github.com/lowlevel-eu/wiki/wiki/C%2B%2B "C++") |
| API: | n/a |
| Binärformat: | bisher RAW |
| [IPC-Methode](https://github.com/lowlevel-eu/wiki/wiki/Interprozesskommunikation "IPC"): | Channels |
| Homepage |  |

In Planung

  
AiCOS ist als ein [Betriebssystem](https://github.com/lowlevel-eu/wiki/wiki/Betriebssystem "Betriebssystem") geplant, welches Anfangs für Aufgaben im Netzwerkbereich fungieren soll, unter anderem auch als Storage-System. AiCOS soll frisches Blut (über eine genauere Definition werde ich noch grübeln) in die Computertechnik bringen, unter anderem ein eigenes [FS](https://github.com/lowlevel-eu/wiki/wiki/Dateisystem "Dateisystem"), eigenes Netzwerkprotokoll und eine eigene Programmiersprache ... wenn es klappt.

  

# Entwicklungsumgebung

- Intel Core 2 Quad mit 4 GiB RAM
- Microsoft [Windows](https://github.com/lowlevel-eu/wiki/wiki/Windows "Windows") XP Pro
- Microsoft Visual Studio 2008 Express
- Mircosoft .NET Framework v3.5
- Microsoft Windows-Debugger x86/x64 für Kernel-Debug
- Microsoft Virtual PC 2007

  

# Konzept

### Bootsektor

- Der Bootsektor wird so geschrieben, dass es im Prinzip egal ist, an welcher Adresse dieser geladen und ausgeführt wird. Derzeit wird noch ein Fehlercode ausgeben und die Ausführung angehalten, wenn sich der Bootcode nicht an der Adresse 0x00007C00 befindet.
- Für jedes [FS](https://github.com/lowlevel-eu/wiki/wiki/Dateisystem "Dateisystem") (RAW, FAT, FAT32 und ISO9660) auf dem AiCOS zum Einsatz kommen wird, wird es einen entsprechenden Bootcode geben.

### Bootloader

- Soll erste Möglichkeiten des Kernel-Debugging ermöglichen.
- Einrichten des MKS und laden bedingter Treiber.
- Startup des MKS.

### Kernel

- MKS = Modulares Kernel System, unterteilt in:
  - Managemant-Kernel, verwaltet RAM und koordiniert die anderen Kernels für CPU, IO und Subsysteme.
  - CPU-Kernel, jeder Kern hat seinen eigenen.
  - IO-Kernel.
  - Subsystem-Kernel, für weitere Treiber, Filter und und und ...
- Soll insich redundant werden, erfordert aber mind. 2 CPUs bzw. 2 CPU-Kerne.

**Notiz:** Zum besseren Verständnis meines Konzept ist eine visuelle Darstellung meines OS in Planung. Sie beinhaltet den Bootprozess und den Aufbau des MKS.

  

# History

- 07.12.2008 Bootsektor für Raw-Floppy fertig.
- 06.12.2008 Bootsektor-Programm, das den Inhalt der Register der CPU beim Einsprung in den Bootcode anzeigt.

  

# Stand der Dinge

**Fertig:**

- Bootsector für Floppy (Raw)

  
**In Arbeit:**

- Bootloader
- Kernel-Debug-Unterstützung für WinDbg

  
**Geplant:**

- Bootsektor für CD

  

# Meine OpenSource-Ecke

- **Bootsektor-Programmierung**
  - [ShowReg_32.asm](http://aicos.amazing-fx.de/opensource/ShowReg_32.asm) :: Zeigt den Inhalt der CPU-Register beim Einprung in den Bootcode. [Screenshot hier!](http://aicos.amazing-fx.de/images/screenshots/ShowReg_32.asm.gif)
  - [All_Bootsector_Images.zip](http://aicos.amazing-fx.de/downloads/All_Bootsector_Images.zip) :: Alle Bootsektor-Beispiele als Raw-Image für die Floppy.

  

# Ziele

Ein vollwertiges OS auf die Beine zu stellen, welches sich auch im Netzwerkbereich behaupten kann. Dabei wird keiner Code von anderen OS verwendet, vorallem keine Bootloader wie z.B. Grub!

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/3681/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1766/index.html)

<!-- MediaWiki page 1766; revision 3681; parent 3680; 2008-12-11T20:50:30Z -->
