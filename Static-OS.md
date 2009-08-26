# Static OS

**Static Operating System** (Static OS) ist ein 32 Bit Betriebssystem, welches von Stefan Mayer entwickelt wird. Das Betriebssystem wird derzeit noch als Closed Source entwickelt.

Vorlage:Infobox Programme

## Features

**Version 1.8**

     •  32 Bit
     •  Intel x86 Architektur
     •  GRUB als Bootloader (Multiboot fähig)
     •  Protected Mode
     •  Paging / Phys-Virt-Memorymanagement (malloc/realloc/free)
     •  IDT / GDT / TSS
     •  PIC / PIT
     •  Multitasking (Ring 0 / Ring 3)
     •  Elf-Support
     •  ATAPI / ATA (derzeit noch im Kernel implementiert)
     •  FDC (z.z. keien Verwendung)
     •  Virtual 8086 Modus (ermöglicht das Ausführen von 16 Bit Code im Protected Mode)
     •  Maus / Tastatur - Treiber (Treibermanagement -> völlig eigenständige Treiber)
     •  Grafische Benutzeroberfläche
          -  Fenster (verschiebbar, Größe veränderbar)
          -  Labels (Zur einfachen Textausgabe in Fenstern)
          -  Buttons
          -  Textbox
          -  Listbox (beliebig Einträge abfragen/hinufügen/editieren/entfernen)
          -  Pictures (SBF, SCU, BMP, RAW)
          -  Font-Support (Verdana, Courier New, Comic Sans, Impact, ...)
     •  API
          -  Taskhandling
          -  User Speicherzugriffe (umalloc)
          -  Funktions/Handler-Registrierung
          -  IPC (Inter Process Communication)
          -  ...

  

## Download

Zur Zeit steht leider noch keine Aktuelle Version zum Download bereit.

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/5718/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2050/index.html)

<!-- MediaWiki page 2050; revision 5718; parent 5717; 2009-08-26T09:01:57Z -->
