# AiCOS

| ![AiCOS-Logo-small.png](http://aicos.amazing-fx.de/images/AiCOS-Logo-small.png) |  |
| ----------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|  |  |
| Entwickler: | [ScollPi](https://lowlevel-eu.github.io/wiki/pages/1765/index.html "Benutzer:ScollPi") |
| Akt. Version: | Research Phase 0 (0.00.38.57) |
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

AiCOS Wurzel liegen weder in der Linux/Unix-Welt, weder in der Windows-Welt, sondern in Microsofts [Singularity](https://github.com/lowlevel-eu/wiki/wiki/Singularity "Singularity").

**Dieses Projekt ist zur Zeit wegen eines anderen höher priorisierten Projekt angehalten. Dieses Projekt wird jedoch später fortgesetzt.**

  

# Entwicklungsumgebung

- **Hardware**
  - Intel Core 2 Quad mit 8 GiB RAM
- **Software**
  - [Microsoft XP Pro](http://www.microsoft.com/germany/windows/windows-xp/) \>\>\> [Windows](https://github.com/lowlevel-eu/wiki/wiki/Windows "Windows")
  - [Microsoft Visual Studio 2008 Express](http://www.microsoft.com/germany/express/)
  - [Mircosoft .NET Framework v3.5](http://www.microsoft.com/downloads/details.aspx?FamilyID=333325fd-ae52-4e35-b531-508d977d32a6&DisplayLang=de)
  - [Microsoft Windows-Debugger x86/x64 für Kernel-Debug](http://www.microsoft.com/whdc/devtools/debugging/default.mspx)
  - [Microsoft Virtual PC 2007 inkl. SP 1](http://www.microsoft.com/downloads/details.aspx?FamilyID=28c97d22-6eb8-4a09-a7f7-f6c7a1f000b5&DisplayLang=de) \>\>\> [Microsoft Virtual PC](https://github.com/lowlevel-eu/wiki/wiki/Microsoft-Virtual-PC "Microsoft Virtual PC")
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

**Die letzten 10 Änderungen:**

- 14.01.2009: Version 0.00.38.57
  - Grundfunktionen des Memory-Management
  - Suchen und auslesen des PCI-BIOS.
  - Suchen und auslesen des PnP-BIOS.
  - Suchen und auslesen von ACPI.
  - Problematische unerklärbarer Bug im Bootsektor-Code (ROFS) behoben.
- 11.01.2009 SMAP hinzugefügt.
- 04.01.2009 Bug im Bootcode behoben; Kernel-Debug implementiert (0.00.35.47)
- 03.01.2009 Printf implementiert (0.00.34.45)
- 03.01.2009 C++ Testdummy, um Einsprung zu testen; Test OK (0.00.31.40)
- 02.01.2009 Paging mit PAE implementiert. (0.00.24.23)
- 01.01.2009 Bootloader prüft die CPU, da mindestens ein 586er benötigt wird. (0.00.23.20)
- 01.01.2009 Bug im Bootcode behoben; Bootloader gibt Meldung aus. (0.00.22.16)
- 01.01.2009 Fehler beim Sprung in den PM behoben, FDD-Motor wird nun auch abgeschaltet. (0.00.21.6)
- 31.12.2008 Bootsektor: Umadressierung, da Probleme mit dem PM. (0.00.20.5)

**Komplette History:** <http://aicos.amazing-fx.de/history.txt>

  

# Statistik

**Die folgende Statistik zählte folgende Datei-Typen:**

- Build-System-Dateien *(.cmd, .vbs)*
- MSBuild-Projekt-Dateien *(.proj, .targets)*
- Assembler-Dateien *(.asm, .inc)*
- C/C++ Dateien *(.cpp, .h)*

  

- **Gesamtzeilen:** 10022  
    
- **Codezeilen:** 5504 *(55%)*
- **Leerzeilen:** 1985 *(20%)*
- **Kommentar:** 2533 *(25%)*

  
Gezählt wurde mit dem Java-Programm: **[Lines Of Code Wichtel](http://www.andreas-berl.de/linesofcodewichtel/)**

  

# Stand der Dinge

**Fertig:**

- Bootsector für ROFS, FDD-Version.
- Bootloader
  - Entry16: 16-Bit-Einsprung in Assembler
  - Entry32: 32-Bit-PM-Einsprung in Assembler
  - Entry: C++ Part
  - Routinen für Textausgabe, darunter auch mit printf()
  - COM-Treiber: für Kernel-Debug benötigt
  - Kernel-Debug
  - SMAP (System Memory Map)

  
**In Arbeit:**

- Bootloader
  - Paging mit PAE (bisher nur 2 MiB gemappt, sollte erstmal für Bootloader-Spielereien reichen).
  - Memory Management.
  - PCI Suuport.
  - PnP Support.
  - ACPI Support.
  - ACPI (Um Anzahl der Cores zu ermitteln).
- Homepage für AiCOS.

  
**Geplant:**

- Bootloader
  - System-Shell (Kernel-Ersatz, dient zum Anzeigen wichtiger System-Informationen und wird als CLI \[Command Line Interface\] aufgesetzt.
- Bootsektor für CD

  

# Roadmap

**Ziele für Sprung in Research Phase 1 (Version 0.01)**

- Single-CPU
- Funtionierender Bootsektor für Floppy (ROFS) und CD (ISO9660) - (Einheitlicher Code, bis auf die unterschiedliche Sektorgröße).
- Funktionierender Bootloader, der System-Vorab-Checks durchführt, bevor gewissen Funktionen wie Protected Mode oder Paging benutzt werden.
- Ausführliche Comments in Bootsektoren und Bootloader.
- AiCOS-Source-Tree, Hardwarebedingter Code wird von System-Code getrennt, damit soll später eine bessere Portierbarkeit erreicht werden, wodurch nur der Hardwarebedingte Code (überwiegend Assembler) ausgetauscht werden muss.
- AiCOS-Startup-Dummy.

  
**Ziele für Sprung in Research Phase 2 (Version 0.02)**

- Differenzierung des Kernelgrundsystem in Management-Kernel, CPU-Kernel & I/O-Kernel
- Channel-System als IPC implementieren
- Hello-World-Prozess

  

# Aktueller Screenshot

**Version: 0.00.38.57**

![bootloader_008.gif](http://aicos.amazing-fx.de/images/screenshots/bootloader_008.gif)

[Screenshot mit Windows-Debug](http://aicos.amazing-fx.de/images/screenshots/Dev_20090104_0730.png)

  

# Böse Falle

- Ständig kackte meine VM ab, als mein Bootloader ins den PM-Segment prang. Man kann sich echt todsuchen, wenn man Hexzahlen und Dezimalzahlen nicht unterscheiden kann. 20d != 20h
- Und wieder einmal stellte meine VM ihren Dienst beim Sprung ins PM-Segment ein und wieder suchte ich mich blöd. War letztenendes auch logisch, wenn der Bootsektor nur ein Sektor (512 Bytes) des Bootloaders lädt, aber der Sprung in PM-Segment aber an Offset 0x0200 sich befinden. **Böse Falle**

  

# Meine SourceCode-Ecke

- **Bootsektor-Programmierung**
  - [ShowReg_32.asm](http://aicos.amazing-fx.de/opensource/ShowReg_32.asm) :: Zeigt den Inhalt der CPU-Register beim Einprung in den Bootcode. [Screenshot hier!](http://aicos.amazing-fx.de/images/screenshots/ShowReg_32.asm.gif)
  - [Floppy_Raw.asm](http://aicos.amazing-fx.de/opensource/Floppy_Raw.asm) :: Floppy-Raw-Bootsektor, Research-Version.
  - [All_Bootsector_Images.zip](http://aicos.amazing-fx.de/downloads/All_Bootsector_Images.zip) :: Alle Bootsektor-Beispiele als Raw-Image für die Floppy.

  

# Ziele

Ein vollwertiges OS auf die Beine zu stellen, welches sich auch im Netzwerkbereich behaupten kann. Dabei wird keinerlei Code von anderen OS verwendet, vorallem keine Bootloader wie z.B. Grub!

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/4284/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1766/index.html)

<!-- MediaWiki page 1766; revision 4284; parent 3873; 2009-04-11T13:09:15Z -->
