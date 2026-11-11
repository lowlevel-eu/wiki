# AiCOS

| ![AiCOS-Logo-small.png](http://aicos.amazing-fx.de/images/AiCOS-Logo-small.png) |  |
| ----------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|  |  |
| Entwickler: | [ScollPi](https://lowlevel-eu.github.io/wiki/pages/1765/index.html "Benutzer:ScollPi") |
| Akt. Version: | Research Phase 1 (0.01.x) |
| [Lizenz](Lizenzen "Lizenzen"): | n/a |
| OS-Eigenschaften |  |
| Plattform: | [x86](X86 "X86") (später auch [x64](X86-64 "X64")) |
| [Kernelart](Kernel "Kernel"): | Modulares Kernel System (MKS) |
| [Sprache](Kategorie-Programmiersprache "Kategorie:Programmiersprache"): | [Assembler](Assembler "Assembler"), [C](C "C")/[C++](C%2B%2B "C++") |
| API: | n/a |
| Binärformat: | BIN, (event. EXE) |
| [IPC-Methode](Interprozesskommunikation "IPC"): | Channels |
| Homepage |  |

In Planung

  
AiCOS ist ein [Betriebssystem](Betriebssystem "Betriebssystem"), welches ganz neue Wege gehen wird, vor allem im Kerneldesign. Warum also aus einer blöden und verrückten Idee nicht ein vollwertiges OS machen?

AiCOS Einsatzbereich wird anfangs im Netzwerkbereich liegen, unter anderem aber auch als Storage-System. Auch wenn AiCOS auf Single-Core-Plattformen laufen wird, wird es seine Stärken wohl eher auf Multiprozessor bzw. Multicore-System zeigen können. Wichtigstes Ziel ist dabei zum Einem die Performance (ideal sogar Echtzeit) und zum Anderem die Stabilität (Redundanz bis auf CPU-Ebene).

Dieses ehrgeizige Ziel von AiCOS soll frischen Wind in die Computertechnik bringen und hoffentlich auch andere zu einem solchen OS-Design motivieren und gegebenenfalls auch animieren. Denn noch ist AiCOS ein ClosedSource-Projekt.

Wen wundert es also, dass die Wurzeln von AiCOS weder in der Linux/Unix-Welt noch in der Windows-Welt liegen, sondern viel eher in Microsofts [Singularity](Singularity "Singularity"). Ein zweites Singularity soll es aber nicht werden, versprochen.

  

# Über AiCOS

### Namensgebung

Ist der Name des OS nur ein fantasievolle Bezeichnung oder steht **AiCOS** für eine Abkürzung? Wenn ja, was verbirgt sich dahinter?

AiCOS ist in der Tat eine Abkürzung und steht für ***A**syncronous **i**nter**C**onnected **O**perating **S**ystem*. Sollte sich die Entwicklung dieses OS meinen Erwartungen entsprechen, könnte AiCOS in einigen Jahren auch für ***A**rtificial **i**ntelligence **C**ontrolled **O**perating **S**ystem* stehen. Klingt nach **SKYNET**, könnte man denken, wird aber keinesfalls beabsichtig.

### Entwickler & Lizenz

Derzeit unterliegt die komplette Entwicklung von AiCOS einer einzigen Persion, nämlich mein Wenigkeit, [ScollPi](https://lowlevel-eu.github.io/wiki/pages/1765/index.html "Benutzer:ScollPi"). Dies soll aber nicht für immer so bleiben. Wenn die wichtigsten Konzepte des OS (überwiegend Kernel) erstellt und ggf. auch schon umgesetzt wurden, werde ich meine Türe öffnen und andere Begeisterte mit in dieses Boot nehmen.

### Plattform

Erstmal nur aus x86-Reihe für 32/64-Bit Plattformen ab 586 voraussichtlich.

### Kernel

Beim Kernel werden ganz neue Wege gegangen. Der monolithischer Kernel als auch die Mikrokernel mögen ihre Vor- und Nachteile haben. Klar, es gäbe noch die Hybriden. Aber die Entwicklung der Prozessoren geht ja auch weiter, Multicores und Co's gehört die Zukunft. Ideal sind Multicore-CPUs, bei denen auf jedem Kern ein andere Kernel laufen könnte. Tile-Gx (100 Kerne) von Tileras geht da schon in diese Richtung. Doch selbst auf heutigen PC, in erster Linie Gaming-PC, gibs schon verschiedene Prozessoren, CPU, GPU und auch schon PPU.

### Sprachen

Hardware nahe Programmteile wie Bootloader (später mehr dazu) oder Treiber werden in Assembler (Intel-Syntax) vorliegen. Der Kernel selbst wird überwiegend in C geschrieben sein, bis auf den CPU-Kernel. Ob C++ auch verwendet wird, wird jedoch nicht ausgeschlossen. Programme im Userspace werden überwiegend in C++ geschrieben. Ob andere Sprachen Einzug erhalten, hängt davon ab, ob entsprechende Compiler portiert werden.

### API

*Noch nicht Bestandteil der Entwicklung.*

### Binärformat

Vorerst BIN, ggf. auch EXE. Ob ELF unterstützt wird, ist eine Frage der Implementierung. Ein ganz anderes Format wäre natürlich auch denkbar.

### IPC-Methode

Den einzigen gemeinsamer Nenner, den ich finden konnte und den ich auch bei der derzeitigen CPU-Entwicklung für zukunftsicher halte, sind Channels. Channels sollen später auch die Grundlage eines eigenen Netzwerkprotokolls werden, welches anfangs eher über IP zu einer anderen Maschine mit AiCOS getunnelt wird.

  

# Entwicklungsumgebung

- **Hardware**
  - Intel Core 2 Quad mit 8 GiB RAM
- **Software**
  - [Microsoft Windows 7 (64-bit)](http://www.microsoft.com/germany/windows/windows-7/) \>\>\> [Windows](Windows "Windows")
  - [Microsoft Visual Studio 2008 Express](http://www.microsoft.com/germany/express/)
  - [Mircosoft .NET Framework v3.5](http://www.microsoft.com/downloads/details.aspx?FamilyID=333325fd-ae52-4e35-b531-508d977d32a6&DisplayLang=de)
  - [Microsoft Windows-Debugger x86/x64 für Kernel-Debug](http://www.microsoft.com/whdc/devtools/debugging/default.mspx)
  - [Microsoft Virtual PC 2007 inkl. SP 1](http://www.microsoft.com/downloads/details.aspx?FamilyID=28c97d22-6eb8-4a09-a7f7-f6c7a1f000b5&DisplayLang=de) \>\>\> [Microsoft Virtual PC](Microsoft-Virtual-PC "Microsoft Virtual PC")
  - Sun VirtualBox
  - Bochs
- **Referenzmaterial**
  - [Microsoft Singularity RDK 2.0](http://www.codeplex.com/singularity)
  - [Protected Mode Tutorials](http://www.fh-zwickau.de/doc/prmo/start.htm)
  - [Paging verschiedener CPUs](http://ra.ziti.uni-heidelberg.de/pages/student_work/seminar/ws0304/frank_lemke/praesentation.pdf)

  

# Konzept

Ich wurde gefragt, warum ich zum Booten meines OS denn nicht GRUB nehme. Nun, erstens brauche ich nur einen Bootloader und keinen ganzen Bootmanager. Zudem muss der Bootloader in der Lage sein, ein Modulares-Kernel-System laden und initialisieren zu können. Wie anfangs schon gesagt, AiCOS geht ganz neue Wege. Und zweitens geht es mir bei der Entwicklung auch darum den Bootvorgang zu verstehen. Dazu schaue ich mir den Bootcode an, den Windows XP verwendet (also NT-Bootsektor und NTLDR).

### Bootsektor

- Universeller Aufbau, sodass nur die Routinen für das jeweiliges Dateisystem ausgetauscht werden müssen.
- Es wird anfangs nicht versucht, den gesamten Code zum vollständigen Laden des Bootloaders in den Bootsektor zu quetschen. Entsprechende Optimierungen folgen erst später.
- Bootcode wird es anfangs für folgende Dateisysteme geben: FAT12, FAT16, FAT32, ROSF, ISO9660 und eventuell auch NTFS.
- Zukünftige Festplatten mit 4k-Sektoren werden ebenfalls berücksichtigt.

### Bootloader

- Protected-Mode
- Paging mit Physical-Address-Extension (PAE), max. 64 GiByte
- Soll erste Möglichkeiten des Kernel-Debugging ermöglichen.
- Einrichten des MKS und laden bedingter Treiber.
  - Mikrokernel für den BSP (Boot Strap Processor).
  - Mikrokernel für jeden APs (Application Processors) ... nur bei MultiCore-Systemen.
  - Management-Kernel.
  - I/O-Kernel.
- Startup des MKS und Channel-System.
  - Den BSP in den 32-Bit PM schalten und die Kontrolle über den Management-Kernel geben.

### Kernel

- MKS = Modulares Kernel System, unterteilt in:
  - Managemant-Kernel, verwaltet RAM und koordiniert die anderen Kernels für CPU, IO und Subsysteme.
  - CPU-Kernel, jeder Kern hat seinen eigenen Mikrokernel. Der für den BSP ist bereits im Bootloader enthalten.
  - IO-Kernel.
  - Subsystem-Kernel, für weitere Treiber, Filter und und und ...
- Soll in sich redundant werden, erfordert aber mind. 2 CPUs bzw. 2 CPU-Kerne.

  
**Notiz:** Zum besseren Verständnis meines Konzept ist eine visuelle Darstellung meines OS in Planung. Sie beinhaltet den Bootprozess und den Aufbau des MKS. Diese Visualisierungen werden überwiegend auf der Homepage von AiCOS zu finden sein, die sich derzeit noch im Aufbau befindet.

  

# History

**Die letzten 10 Änderungen:**

- 18.03.2010: Entwicklungsinfo
  - Lange war es ruhig um AiCOS, doch wirklich ruhte die Entwicklung nicht. Es wurde vor allem in der Theorie gefeilt. Zur Zeit wird an der Überarbeitung des Bootsektors gearbeitet, da dieser universal aufgebaut sein soll und sich nur in den Bestandteilen des jeweiligen Dateisystem unterscheidet. Zeitgleich wird auch am Bootloader gearbeitet, vor allem am Assebler-Part.
- 15.01.2009: Version 0.00.??.??
  - ROFS-Bootsektor-Code finalisiert, es kann nun auch eine Datei grö´ßer 64KiB geladen werden. Der Bootloader selbst wurde wegen seiner PM-Funktionalität auf 256 KiB beschränkt.
  - Suchen und Auslesen von MPS (FPS).
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

- Bootsektor für FAT12
- Bootsektor für FAT16

  
**In Arbeit:**

- Bootloader (Assembler-Part)
- "Tutorial: Eigener Bootloader" für Lowlevel

  
**Geplant:**

- Bootsektor für FAT32
- Bootsektor für ROFS (Read Only File System - Eigenentwicklung
- Bootsektor für CD
- Bootsektor für NTFS
- Bootloader (CPU-Kernel)

  

# Roadmap

**Folgt in Kürze**

  

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

Ein vollwertiges OS auf die Beine zu stellen, welches sich auch im Netzwerkbereich behaupten kann. Dabei wird in keinster Weise direkt Code von anderen OS verwendet, vorallem keine Bootloader wie z.B. Grub! Vielmehr wird deren Funktionsweise analysiert. Der Kernel, besser gesagt das Kernel-System von AiCOS wird keines im Sinnes der Definition eines Kernels sein, sondern vielmehr ein Systemkern aus einer modularen Ansammlung mehrere Mikrokernels.

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/7681/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1766/index.html)

<!-- MediaWiki page 1766; revision 7681; parent 7456; 2010-05-10T16:04:06Z -->
