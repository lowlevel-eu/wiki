# NerdyKernel

|  |  |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
|  |  |
| Entwickler: | rizor |
| Akt. Version: |  |
| [Lizenz](https://github.com/lowlevel-eu/wiki/wiki/Lizenzen "Lizenzen"): |  |
| OS-Eigenschaften |  |
| Plattform: | i386 |
| [Kernelart](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel"): | Microkernel |
| [Sprache](https://lowlevel-eu.github.io/wiki/pages/1648/index.html "Kategorie:Programmiersprache"): | [C](https://github.com/lowlevel-eu/wiki/wiki/C "C") & [Assembler](https://github.com/lowlevel-eu/wiki/wiki/Assembler "Assembler") |
| API: | Noch nicht näher geplant |
| Binärformat: | [ELF](https://github.com/lowlevel-eu/wiki/wiki/Executable-and-Linking-Format "ELF") |
| [IPC-Methode](https://github.com/lowlevel-eu/wiki/wiki/Interprozesskommunikation "IPC"): | Noch nicht näher geplant |
| Homepage |  |

In Planung

  
rizor-OS ist ein kleines Hobby-OS bei dem ich viel über die LowLevel-Programmierung lernen möchte.

## Entwickler

- rizor

## Features

Folgende Features sind implementiert

- Microkernel
- x86
- GDT
- IDT
- CPUID
- teile der libc

## Roadmap

- rizor-OS-0.1:
  - Multitasking
  - libc (fast komplette Implementierung)
  - Treiber für das Display und die Tastatur im Userspace
- rizor-OS-0.2:
  - Shell-Integration
  - Dateisystem
  - vollständige libc
- rizor-OS-0.3:
  - Netzwerktreiber
  - kleiner konsolenbasierter Browser
  - kleinen Dateimanager
- Entfernte Planung:
  - Teile der Treiber sollen in den Kernel verlagert werden um ein optimales Leistungs-Stabilitätsverhältnis zu gewährleisten
  - Portierung auf x86-64
  - guter Treibersupport (unter Umständen ein Einbau der CDI)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/4021/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1816/index.html)

<!-- MediaWiki page 1816; revision 4021; parent 4020; 2009-02-17T20:43:47Z -->
