# NerdyKernel

| rizor-OS |  |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
|  |  |
| Entwickler: | rizor |
| Akt. Version: | 0.1-Alpha Build 0002 |
| [Lizenz](https://github.com/lowlevel-eu/wiki/wiki/Lizenzen "Lizenzen"): | Closed-Source |
| OS-Eigenschaften |  |
| Plattform: | i386 |
| [Kernelart](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel"): | Microkernel |
| [Sprache](https://lowlevel-eu.github.io/wiki/pages/1648/index.html "Kategorie:Programmiersprache"): | [C](https://github.com/lowlevel-eu/wiki/wiki/C "C") & [Assembler](https://github.com/lowlevel-eu/wiki/wiki/Assembler "Assembler") |
| API: | Noch nicht näher geplant |
| Binärformat: | [ELF](https://github.com/lowlevel-eu/wiki/wiki/Executable-and-Linking-Format "ELF") |
| [IPC-Methode](https://github.com/lowlevel-eu/wiki/wiki/Interprozesskommunikation "IPC"): | Noch nicht näher geplant |
| Homepage |  |

In Planung

  
rizor-OS ist ein kleines Hobby-OS bei dem ich viel über die LowLevel-Programmierung lernen möchte. Das OS soll später als Projektarbeit und Referenzen für und nach dem Studium gelten. Unter Umständen wechsele ich das Projekt zu einem OpenSource-Projekt, das dann unter der GPL-Lizenz laufen würde.

## Entwickler

- rizor

## Entwicklungsstatus

- Kernel
  - rizor-0.3.0.0003-Alpha
    - Treiber für den PIC einbauen
    - Entwickeln der IRQ
    - Planung zum Multitasking

## Features

Folgende Features sind implementiert

- x86
- nicht-kommunikationsfähiger Microkernel
  - GDT
  - IDT
  - CPUID
  - ISR
  - teile der libc

## Roadmap

- rizor-OS-0.1 (Release: März/April 2009):
  - Multitasking (einfaches Round-Robin kein Thread-Support)
  - einfachste Shell (Starten/Stoppen von Prozessen)
  - Speicherverwaltung mit einfachem First-Fit
  - libc (fast komplette Implementierung)
  - Treiber für das Display und die Tastatur im Userspace
- rizor-OS-0.2 (Release: August-Oktober 2009):
  - Speicherverwaltung optimieren
  - Multitasking erweitern
    - Threads implementieren
    - Round-Robin mit Prioritäten
    - Multi-Level-Feedback
  - Shell-Integration
  - Dateisystem
  - vollständige libc
- rizor-OS-0.3 (Release: 2010):
  - Netzwerktreiber
  - kleiner konsolenbasierter Browser
  - kleinen Dateimanager
- Entfernte Planung:
  - Teile der Treiber sollen in den Kernel verlagert werden um ein optimales Leistungs-Stabilitätsverhältnis zu gewährleisten
  - Portierung auf x86-64
  - guter Treibersupport (unter Umständen ein Einbau der CDI)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/4034/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1816/index.html)

<!-- MediaWiki page 1816; revision 4034; parent 4033; 2009-02-17T23:22:06Z -->
