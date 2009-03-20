# NerdyKernel

| rizor-OS |  |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
|  |  |
| Entwickler: | rizor |
| Akt. Version: | 0.1-Alpha Build 0008 |
| [Lizenz](https://github.com/lowlevel-eu/wiki/wiki/Lizenzen "Lizenzen"): | Closed-Source |
| OS-Eigenschaften |  |
| Plattform: | i386 |
| [Kernelart](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel"): | Hybridkernel |
| [Sprache](https://lowlevel-eu.github.io/wiki/pages/1648/index.html "Kategorie:Programmiersprache"): | [C](https://github.com/lowlevel-eu/wiki/wiki/C "C") & [Assembler](https://github.com/lowlevel-eu/wiki/wiki/Assembler "Assembler") |
| API: | Noch nicht näher geplant |
| Binärformat: | [ELF](https://github.com/lowlevel-eu/wiki/wiki/Executable-and-Linking-Format "ELF") |
| [IPC-Methode](https://github.com/lowlevel-eu/wiki/wiki/Interprozesskommunikation "IPC"): | Noch nicht näher geplant |
| Homepage |  |

In Planung

  
rizor-OS ist ein kleines Hobby-OS bei dem ich viel über die LowLevel-Programmierung lernen möchte. Das OS soll später als Projektarbeit und Referenzen für und nach dem Studium gelten. Unter Umständen wechsele ich das Projekt zu einem OpenSource-Projekt, das dann unter der GPL-Lizenz laufen würde.

## Entwickler

- rizor

## Userinterface

Zur Interaktion mit dem User sind einfache Terminals geplant. Später soll es dann auch ein Kernel-Terminal geben, dass genau angibt, was geschieht und wie die momentante Situation im Kernelspace aussieht. Der User hat dann auch die Möglichkeit den Kernelspace bedingt zu verändern um Probleme zu beheben. Es soll aber nur eingeschränkten Zugriff geben, damit der Kernel nicht zerstört wird.

## OS-Design

Es soll ein elementarer Hybridkernel angeboten werden. Dieser soll auch ein elementares Filesystem haben, damit er die Boot-Files lesen und die entsprechenden Module laden kann. Manche Module sollen dabei direkt in den Kernelspace geladen werden (z.B. PIC, erweiterte Speicherverwaltung). Alle anderen Module sollen dann im Userspace arbeiten. Dadurch ist eine größtmögliche Portierbarkeit auf andere Architekturen ermöglicht werden. Außerdem sind dann leichter erweiterungen und Updates möglich. Jeder Task, der einen Syscall anbietet, muss außerdem einen Broadcast-Handler anbieten, damit der Kernel in regelmäßigen Abständen die Funktion der einzelnen Tasks gewährleisten kann. Wenn der Task nach einer bestimmten Zeit nicht reagiert, wird dieser beendet und wird automatisch vom Kernel neu gestartet. Falls dieser Task zur Interaktion mit anderen Tasks verwendet wurde, wird jedem Task ein Signal geschickt, dass ihm sagt, dass sie ihre Informationen noch einmal schicken sollen. Es sei denn, die Informationen befinden sich noch in einer Liste (oder ähnliches) die abgearbeitet wird.

## OS-Statistiken

- Version: rizor-OS-0.1 Build 0008-Alpha
  - Kernel: 3524 LOC
  - Libc: 316 LOC
  - Kernel-Library: 66 LOC
  - Collection: 7 LOC

## Entwicklungsstatus

- Kernel
  - rizor-0.3.1.0009-Alpha
    - Entwicklung zum Multitasking
    - Entwicklung des Shared-Memory-Handlers
    - Planung der IPC/RPC

## Features

Folgende Features sind implementiert

- x86
- kommunikationsfähiger Hybrid-Kernel
  - Physikalische Speicherverwaltung
  - Syscalls
  - Paging mit automatischer Flagwahl
  - Speicherverwaltung für Kernel- und User-Space
  - Spinlocks
  - voller Funktionsumfang des KBC
  - einfache Ausgabe des Keyboards
- Teile der libc
- Eine Kernel-Library
- Eine Collection an Datenstrukturen

## Roadmap

- rizor-OS-0.1 (Release: März/April 2009):
  - **Feature Freeze**: 31.03.2009
  - **Geplanter Release**: 15.04.2009
  - Multitasking (einfaches Round-Robin ohne Thread-Support)
  - Speicherverwaltung mit einfachem First-Fit
  - libc (nötigste Implementierung)
  - Treiber für das Display und die Tastatur im Kernelspace
- rizor-OS-0.2 (Release: August-Oktober 2009):
  - Speicherverwaltung optimieren
  - Multitasking erweitern
    - Threads implementieren
    - Round-Robin mit Prioritäten
    - Multi-Level-Feedback
  - Shell-Integration
  - Auslagerung der Treiber in den Userspace
  - Dateisystem
  - vollständige libc
  - Portierung des GCC
  - Einbau eines kleinen Texteditors
- rizor-OS-0.3 (Release: 2010):
  - Netzwerktreiber
  - kleiner konsolenbasierter Browser
  - kleinen Dateimanager
  - Multitasking erweitern
    - shortest-job-next
    - longest-job-next
    - Wechsel des Scheduling-Verfahrens zur Laufzeit
- Entfernte Planung:
  - Teile der Treiber sollen in den Kernel verlagert werden um ein optimales Leistungs-Stabilitätsverhältnis zu gewährleisten
  - Portierung auf x86-64
  - guter Treibersupport (unter Umständen ein Einbau der CDI)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/4150/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1816/index.html)

<!-- MediaWiki page 1816; revision 4150; parent 4149; 2009-03-20T00:42:13Z -->
