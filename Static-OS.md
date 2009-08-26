# Static OS

**Static Operating System** (Static OS) ist ein 32 Bit Betriebssystem, welches von Stefan Mayer entwickelt wird. Das Betriebssystem wird derzeit noch als Closed Source entwickelt. Ein Video welches den Betrieb des OS zeigt, kann auf Youtube angesehen werden:

[Static Operating System RUN](http://www.youtube.com/watch?v=fF-6pyQtDJQ)

| Static Operating System |  |
| ----------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
|  |  |
| Entwickler: | [Stefan Mayer](https://lowlevel-eu.github.io/wiki/pages/2055/index.html "Benutzer:Hunter") |
| Akt. Version: | 1.8 |
| [Lizenz](https://github.com/lowlevel-eu/wiki/wiki/Lizenzen "Lizenzen"): | \- |
| OS-Eigenschaften |  |
| Plattform: | [i386](https://github.com/lowlevel-eu/wiki/wiki/X86 "X86") |
| [Kernelart](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel"): | Microkernel |
| [Sprache](https://lowlevel-eu.github.io/wiki/pages/1648/index.html "Kategorie:Programmiersprache"): | [C](https://github.com/lowlevel-eu/wiki/wiki/C "C"), ASM |
| API: | SOS_API |
| Binärformat: | [ELF](https://github.com/lowlevel-eu/wiki/wiki/Executable-and-Linking-Format "ELF") |
| [IPC-Methode](https://github.com/lowlevel-eu/wiki/wiki/Interprozesskommunikation "IPC"): |  |
| Homepage |  |

<http://www.staticos.at.tf/>

![Staticos1.JPG](http://lowlevel.brainsware.org/wiki/images/8/8d/Staticos1.JPG)

  

## Features

**Version 1.8**

- 32 Bit
- Intel x86 Architektur
- GRUB als Bootloader (Multiboot fähig)
- Protected Mode
- Paging / Phys-Virt-Memorymanagement (malloc/realloc/free)
- IDT / GDT / TSS
- PIC / PIT
- Multitasking (Ring 0 / Ring 3)
- Elf-Support
- ATAPI / ATA (derzeit noch im Kernel implementiert)
- FDC (z.z. keien Verwendung)
- Virtual 8086 Modus (ermöglicht das Ausführen von 16 Bit Code im Protected Mode)
- Maus / Tastatur - Treiber (Treibermanagement -\> völlig eigenständige Treiber)
- VESA (Verschiedene Auflösung durch V8086 Task möglich / Standart: 800x600x24bpp )
- Grafische Benutzeroberfläche
  - Fenster (verschiebbar, Größe veränderbar)
  - Labels (Zur einfachen Textausgabe in Fenstern)
  - Buttons
  - Textbox
  - Listbox (beliebig Einträge abfragen/hinufügen/editieren/entfernen)
  - Pictures (SBF, SCU, BMP, RAW)
  - Font-Support (Verdana, Courier New, Comic Sans, Impact, ...)
- API
  - Taskhandling
  - User Speicherzugriffe (umalloc)
  - Funktions/Handler-Registrierung
  - IPC (Inter Process Communication)
  - ...

  

## Screenshots

Static Operating System Ladevorgang

![Staticos1.JPG](http://lowlevel.brainsware.org/wiki/images/8/8d/Staticos1.JPG)

Static Operating System GUI Test

![Staticos2.JPG](http://lowlevel.brainsware.org/wiki/images/4/4f/Staticos2.JPG)

Static Operating System Fenster vergrößern

![Staticos3.JPG](http://lowlevel.brainsware.org/wiki/images/e/e2/Staticos3.JPG)

  

## Download

Zur Zeit steht leider noch keine Aktuelle Version zum Download bereit.

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/5741/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2050/index.html)

<!-- MediaWiki page 2050; revision 5741; parent 5740; 2009-08-26T12:39:42Z -->
