# AiCOS

| ![AiCOS-Logo-small.png](http://aicos.amazing-fx.de/images/AiCOS-Logo-small.png) |  |
| ----------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|  |  |
| Entwickler: | [ScollPi](https://lowlevel-eu.github.io/wiki/pages/1765/index.html "Benutzer:ScollPi") |
| Akt. Version: | Research Phase (0.00.21.6) |
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

  
AiCOS ist als ein [Betriebssystem](https://github.com/lowlevel-eu/wiki/wiki/Betriebssystem "Betriebssystem") geplant, welches Anfangs für Aufgaben im Netzwerkbereich fungieren soll, unter anderem auch als Storage-System. Dabei wird es gezielt auf Multiprozessor bzw. Multicore-System operieren. Ob es auch den Sprung in ein Cluster schafft, wird sich dann zeigen. Aber erst einmal alles Schritt für Schritt, begonnen mit einem Singlecore-System.

AiCOS soll frisches Blut (über eine genauere Definition werde ich noch grübeln) in die Computertechnik bringen, unter anderem ein eigenes [FS](https://github.com/lowlevel-eu/wiki/wiki/Dateisystem "Dateisystem"), eigenes Netzwerkprotokoll und eine eigene Programmiersprache ... wenn es klappt.

  

# Entwicklungsumgebung

- Intel Core 2 Quad mit 4 GiB RAM
- Microsoft [Windows](https://github.com/lowlevel-eu/wiki/wiki/Windows "Windows") XP Pro
- Microsoft Visual Studio 2008 Express
- Mircosoft .NET Framework v3.5
- Microsoft Windows-Debugger x86/x64 für Kernel-Debug
- Microsoft Virtual PC 2007

**Testumgebung:** Es wird immer zuerst in der VM auf dem Entwicklungssystem getestet und erst wenn da alles ohne Probleme läuft, wird auf der realen Maschine getestet. Als Test-PC dient da einmal ein P2 mit müden 400 MHz als Single-Core, um vor allem die Boot-Phasen zu testen. Versehentlich auch mal Tests auf meinem Quad-Core, wenn ich vergessen habe die Diskette nach dem Testen rauszunehmen. Aber da zeigt sich schon, dass auf der realen Maschine alles genauso läuft wie bisher in der VM.

  

# Konzept

### Bootsektor

- Der Bootsektor wird so geschrieben, dass es im Prinzip egal ist, an welcher Adresse dieser geladen und ausgeführt wird. Derzeit wird noch ein Fehlercode ausgeben und die Ausführung angehalten, wenn sich der Bootcode nicht an der Adresse 0x00007C00 befindet.
- Für jedes [FS](https://github.com/lowlevel-eu/wiki/wiki/Dateisystem "Dateisystem") (RAW, FAT, FAT32 und ISO9660) auf dem AiCOS zum Einsatz kommen wird, wird es einen entsprechenden Bootcode geben.
- Die Aufgabe des Bootsektors sollte wohl ja klar sein, nämlich unabhängig vom Medium den Bootloader zu laden und auszuführen.

### Bootloader

- Soll erste Möglichkeiten des Kernel-Debugging ermöglichen.
- Einrichten des MKS und laden bedingter Treiber.
  - Kernel für BSP (Boot Strap Processor).
  - Kernel für APs (Application Processors) ... nur bei MultiCore-Systemen.
  - Management-Kernel.
  - I/O-Kernel.
- Startup des MKS und Channel-System.
  - Den BSP in den 32-Bit PM schalten und die Kontrolle über den Management-Kernel geben.

### Kernel

- MKS = Modulares Kernel System, unterteilt in:
  - Managemant-Kernel, verwaltet RAM und koordiniert die anderen Kernels für CPU, IO und Subsysteme.
  - CPU-Kernel, jeder Kern hat seinen eigenen.
  - IO-Kernel.
  - Subsystem-Kernel, für weitere Treiber, Filter und und und ...
- Soll insich redundant werden, erfordert aber mind. 2 CPUs bzw. 2 CPU-Kerne.

**Notiz:** Zum besseren Verständnis meines Konzept ist eine visuelle Darstellung meines OS in Planung. Sie beinhaltet den Bootprozess und den Aufbau des MKS. Diese Visualisierungen werden überwiegend auf der Homepage von AiCOS zu finden sein, die sich derzeit noch im Aufbau befindet.

  

# History

- 01.01.2009 Fehler beim Sprung in den PM behoben, FDD-Motor wird nun auch abgeschaltet. (0.00.21.6)
- 31.12.2008 Bootsektor: Umadressierung, da Probleme mit dem PM. (0.00.20.5)
- 15.15.2008 Bootsektor für ROFS ((simple) Read-Only-File-System) FDD-Version fertig. (0.00.11)
- 07.12.2008 Bootsektor für Raw-Floppy fertig.
- 06.12.2008 Bootsektor-Programm, das den Inhalt der Register der CPU beim Einsprung in den Bootcode anzeigt.

  

# Stand der Dinge

**Fertig:**

- Bootsector für ROFS, FDD-Version. (0.00.21.6)
- Bootloader
  - Entry16: 16-Bit-Einsprung

  
**In Arbeit:**

- Bootloader
  - Entry32: 32-Bit-PM-Einsprung
- Homepage für AiCOS

  
**Geplant:**

- Bootloader
  - COM-Treiber: für Kernel-Debug benötigt
  - Kernel-Debug
- Bootsektor für CD

  

# Meine OpenSource-Ecke

- **Bootsektor-Programmierung**
  - [ShowReg_32.asm](http://aicos.amazing-fx.de/opensource/ShowReg_32.asm) :: Zeigt den Inhalt der CPU-Register beim Einprung in den Bootcode. [Screenshot hier!](http://aicos.amazing-fx.de/images/screenshots/ShowReg_32.asm.gif)
  - [Floppy_Raw.asm](http://aicos.amazing-fx.de/opensource/Floppy_Raw.asm) :: Floppy-Raw-Bootsektor, Research-Version.
  - [All_Bootsector_Images.zip](http://aicos.amazing-fx.de/downloads/All_Bootsector_Images.zip) :: Alle Bootsektor-Beispiele als Raw-Image für die Floppy.

  

# Ziele

Ein vollwertiges OS auf die Beine zu stellen, welches sich auch im Netzwerkbereich behaupten kann. Dabei wird keinerlei Code von anderen OS verwendet, vorallem keine Bootloader wie z.B. Grub!

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/3762/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1766/index.html)

<!-- MediaWiki page 1766; revision 3762; parent 3761; 2008-12-31T23:25:14Z -->
