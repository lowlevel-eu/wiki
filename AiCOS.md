# AiCOS

| AiCOS |  |
| ----------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|  |  |
| Entwickler: | [ScollPi](https://lowlevel-eu.github.io/wiki/pages/1765/index.html "Benutzer:ScollPi") |
| Akt. Version: | n/a |
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

  
AiCOS ist als ein [Betriebssystem](https://github.com/lowlevel-eu/wiki/wiki/Betriebssystem "Betriebssystem") geplant, welches Anfangs für Aufgaben im Netzwerkbereich fungieren soll, unter anderem auch als Storage-System. AiCOS soll frisches Blut (über eine genauere Definition werde ich noch grübeln) in der Computertechnik bringen, unter anderem ein eigenes [FS](https://github.com/lowlevel-eu/wiki/wiki/Dateisystem "Dateisystem"), eigenes Netzwerkprotokoll und eine eigene Programmiersprache ... wenn es klappt.

  

# Entwicklungsumgebung

- Intel Core 2 Quad mit 4 GiB RAM
- Microsoft [Windows](https://github.com/lowlevel-eu/wiki/wiki/Windows "Windows") XP Pro
- Microsoft Visual Studio 2008 Express
- Mircosoft .NET Framework v3.5
- Microsoft Windows-Debugger x86/x64 für Kernel-Debug
- Microsoft Virtual PC 2007

  

# Konzept

### Bootsektor

- Sollte die gängigsten [FS](https://github.com/lowlevel-eu/wiki/wiki/Dateisystem "Dateisystem") unterstützen, meist FAT für FDD, FAT32 für HDD und ISO9660 für CD.
- Kann an jeder Adresse ausgeführt werden, akzeptiert aber zum Laden des Bootloader nur 0x00007C00.

### Bootloader

- Kernel-Debug muss möglich sein.
- Einrichten des MKS und laden bedingter Treiber.
- Startup des MKS.

### Kernel

- MKS = Modulares Kernel System, unterteilt in:
  - Managemant-Kernel, verwaltet RAM und koordiniert die anderen Kernels für CPU, IO und Subsysteme.
  - CPU-Kernel, jeder Kern hat seinen eigenen.
  - IO-Kernel.
  - Subsystem-Kernel, für weitere Treiber, Filter und und und ...

  

# Stand der Dinge

### Fertig:

- Bootsector für Floppy (Raw)

  

### In Arbeit:

- Bootloader
- Kernel-Debug-Unterstützung

  

### Geplant:

- Bootsektor für CD

  

# Meine OpenSource-Ecke

- Verschiedenes zur Bootsektor-Programmierung (demnächst)

  

# Ziele

Ein vollwertiges OS auf die Beine zu stellen, welches sich auch im Netzwerkbereich behaupten kann.

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/3619/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1766/index.html)

<!-- MediaWiki page 1766; revision 3619; parent 3599; 2008-12-08T19:02:53Z -->
