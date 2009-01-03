# AiCOS

| ![AiCOS-Logo-small.png](http://aicos.amazing-fx.de/images/AiCOS-Logo-small.png) |  |
| ----------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|  |  |
| Entwickler: | [ScollPi](https://lowlevel-eu.github.io/wiki/pages/1765/index.html "Benutzer:ScollPi") |
| Akt. Version: | Research Phase 0 (0.00.31.40) |
| [Lizenz](https://github.com/lowlevel-eu/wiki/wiki/Lizenzen "Lizenzen"): | n/a |
| OS-Eigenschaften |  |
| Plattform: | [x86](https://github.com/lowlevel-eu/wiki/wiki/X86 "X86") (später auch x64) |
| [Kernelart](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel"): | Modulares Kernel System (MKS) |
| [Sprache](https://lowlevel-eu.github.io/wiki/pages/1648/index.html "Kategorie:Programmiersprache"): | [Assembler](https://github.com/lowlevel-eu/wiki/wiki/Assembler "Assembler"), [C](https://github.com/lowlevel-eu/wiki/wiki/C "C")/[C++](https://github.com/lowlevel-eu/wiki/wiki/C%2B%2B "C++") |
| API: | n/a |
| Binärformat: | BIN, (event. EXE) |
| [IPC-Methode](https://github.com/lowlevel-eu/wiki/wiki/Interprozesskommunikation "IPC"): | Channels |
| Homepage |  |

In Planung

  
AiCOS ist als ein [Betriebssystem](https://github.com/lowlevel-eu/wiki/wiki/Betriebssystem "Betriebssystem") geplant, welches Anfangs für Aufgaben im Netzwerkbereich fungieren soll, unter anderem auch als Storage-System. Dabei wird es gezielt auf Multiprozessor bzw. Multicore-System operieren. Ob es auch den Sprung in ein Cluster schafft, wird sich dann zeigen. Aber erst einmal alles Schritt für Schritt, begonnen mit einem Singlecore-System.

AiCOS soll frisches Blut (über eine genauere Definition werde ich noch grübeln) in die Computertechnik bringen, unter anderem ein eigenes [FS](https://github.com/lowlevel-eu/wiki/wiki/Dateisystem "Dateisystem"), eigenes Netzwerkprotokoll und eine eigene Programmiersprache ... wenn es klappt.

  

# Entwicklungsumgebung

- **Hardware**
  - Intel Core 2 Quad mit 8 GiB RAM
- **Software**
  - [Microsoft XP Pro](http://www.microsoft.com/germany/windows/windows-xp/) \>\>\> [Windows](https://github.com/lowlevel-eu/wiki/wiki/Windows "Windows")
  - [Microsoft Visual Studio 2008 Express](http://www.microsoft.com/germany/express/)
  - [Mircosoft .NET Framework v3.5](http://www.microsoft.com/downloads/details.aspx?FamilyID=333325fd-ae52-4e35-b531-508d977d32a6&DisplayLang=de)
  - [Microsoft Windows-Debugger x86/x64 für Kernel-Debug](http://www.microsoft.com/whdc/devtools/debugging/default.mspx)
  - [Microsoft Virtual PC 2007 inkl. SP 1](http://www.microsoft.com/downloads/details.aspx?FamilyID=28c97d22-6eb8-4a09-a7f7-f6c7a1f000b5&DisplayLang=de)
- **Referenzmaterial**
  - [Microsoft Singularity RDK 2.0](http://www.codeplex.com/singularity)
  - [Protected Mode Tutorials](http://www.fh-zwickau.de/doc/prmo/start.htm)
  - [Paging verschiedener CPUs](http://ra.ziti.uni-heidelberg.de/pages/student_work/seminar/ws0304/frank_lemke/praesentation.pdf)

  
**Testumgebung:**

Es wird immer zuerst in der VM auf dem Entwicklungssystem getestet und erst wenn da alles ohne Probleme läuft, wird auf der realen Maschine getestet. Als Test-PC dient da einmal ein P2 mit müden 400 MHz als Single-Core, um vor allem die Boot-Phasen zu testen. OK, derzeit benutze ich einen Laptop mit P3 mit 1 GHz und satten 256 MiB RAM. Versehentlich auch mal Tests auf meinem Quad-Core, wenn ich vergessen habe die Diskette nach dem Testen rauszunehmen. Aber da zeigt sich schon, dass auf der realen Maschine alles genauso läuft wie bisher in der VM.

  

# Konzept

### Bootsektor

- Der Bootsektor wird so geschrieben, dass es im Prinzip egal ist, an welcher Adresse dieser geladen und ausgeführt wird. Derzeit wird noch ein Fehlercode ausgeben und die Ausführung angehalten, wenn sich der Bootcode nicht an der Adresse 0x00007C00 befindet.
- Für jedes [FS](https://github.com/lowlevel-eu/wiki/wiki/Dateisystem "Dateisystem") (RAW, FAT, FAT32 und ISO9660) auf dem AiCOS zum Einsatz kommen wird, wird es einen entsprechenden Bootcode geben.
- Die Aufgabe des Bootsektors sollte wohl ja klar sein, nämlich unabhängig vom Medium den Bootloader zu laden und auszuführen.

### Bootloader

- Protected-Mode
- Paging mit Physical-Address-Extension (PAE), max. 64 GiByte
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

- 03.01.2009 C++ Testdummy, um Einsprung zu testen; Test OK (0.00.31.40)
- 02.01.2009 Paging mit PAE implementiert. (0.00.24.23)
- 01.01.2009 Bootloader prüft die CPU, da mindestens ein 586er benötigt wird. (0.00.23.20)
- 01.01.2009 Bug im Bootcode behoben; Bootloader gibt Meldung aus. (0.00.22.16)
- 01.01.2009 Fehler beim Sprung in den PM behoben, FDD-Motor wird nun auch abgeschaltet. (0.00.21.6)
- 31.12.2008 Bootsektor: Umadressierung, da Probleme mit dem PM. (0.00.20.5)
- 15.15.2008 Bootsektor für ROFS ((simple) Read-Only-File-System) FDD-Version fertig. (0.00.11)
- 07.12.2008 Bootsektor für Raw-Floppy fertig.
- 06.12.2008 Bootsektor-Programm, das den Inhalt der Register der CPU beim Einsprung in den Bootcode anzeigt.

  

# Stand der Dinge

**Fertig:**

- Bootsector für ROFS, FDD-Version. (0.00.31.40)
- Bootloader (0.00.31.40)
  - Entry16: 16-Bit-Einsprung in Assembler (0.00.23.20)
  - Entry32: 32-Bit-PM-Einsprung in Assembler (0.00.31.40)
  - Entry: C++ Part (0.00.31.40)

  
**In Arbeit:**

- Bootloader
  - Paging mit PAE (bisher nur 2 MiB gemappt, sollte erstmal für Bootloader-Spielereien reichen)
  - Routinen für Textausgabe, darunter auch mit printf()
- Homepage für AiCOS

  
**Geplant:**

- Bootloader
  - COM-Treiber: für Kernel-Debug benötigt
  - Kernel-Debug
- Bootsektor für CD

  

# Roadmap

**Research Phase 0 (Version 0.00)**

- Single-CPU
- Funtionierender Bootsektor für Floppy
- Funktionierender Bootloader
- Kernel-Debug-Interface für [Microsoft Windows-Debugger x86/x64](http://www.microsoft.com/whdc/devtools/debugging/default.mspx)

  
**Research Phase 1 (Version 0.01)**

- Differenzierung des Kernelgrundsystem in Management-Kernel, CPU-Kernel & I/O-Kernel
- Channel-System als IPC implementieren
- Hello-World-Prozess

  

# Aktueller Screenshot

**Version: 0.00.31.40**

![bootloader_003.gif](http://aicos.amazing-fx.de/images/screenshots/bootloader_003.gif)

  

# Böse Falle

- Ständig kackte meine VM ab, als mein Bootloader ins den PM-Segment prang. Man kann sich echt todsuchen, wenn man Hexzahlen und Dezimalzahlen nicht unterscheiden kann. 20d != 20h
- Und wieder einmal stellte meine VM ihren Dienst beim Sprung ins PM-Segment ein und wieder suchte ich mich blöd. War letztenendes auch logisch, wenn der Bootsektor nur ein Sektor (512 Bytes) des Bootloaders lädt, aber der Sprung in PM-Segment aber an Offset 0x0200 sich befinden. **Böse Falle**

  

# Meine OpenSource-Ecke

- **Bootsektor-Programmierung**
  - [ShowReg_32.asm](http://aicos.amazing-fx.de/opensource/ShowReg_32.asm) :: Zeigt den Inhalt der CPU-Register beim Einprung in den Bootcode. [Screenshot hier!](http://aicos.amazing-fx.de/images/screenshots/ShowReg_32.asm.gif)
  - [Floppy_Raw.asm](http://aicos.amazing-fx.de/opensource/Floppy_Raw.asm) :: Floppy-Raw-Bootsektor, Research-Version.
  - [All_Bootsector_Images.zip](http://aicos.amazing-fx.de/downloads/All_Bootsector_Images.zip) :: Alle Bootsektor-Beispiele als Raw-Image für die Floppy.

  

# Ziele

Ein vollwertiges OS auf die Beine zu stellen, welches sich auch im Netzwerkbereich behaupten kann. Dabei wird keinerlei Code von anderen OS verwendet, vorallem keine Bootloader wie z.B. Grub!

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/3819/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1766/index.html)

<!-- MediaWiki page 1766; revision 3819; parent 3798; 2009-01-03T00:51:26Z -->
