# NerdyKernel

| rizor-OS |  |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
|  |  |
| Entwickler: | rizor |
| Akt. Version: | 0.1-Alpha Build 0009 |
| [Lizenz](https://github.com/lowlevel-eu/wiki/wiki/Lizenzen "Lizenzen"): | Closed-Source |
| OS-Eigenschaften |  |
| Plattform: | [i386](https://github.com/lowlevel-eu/wiki/wiki/X86 "X86") |
| [Kernelart](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel"): | Hybridkernel |
| [Sprache](https://lowlevel-eu.github.io/wiki/pages/1648/index.html "Kategorie:Programmiersprache"): | [C](https://github.com/lowlevel-eu/wiki/wiki/C "C") & [Assembler](https://github.com/lowlevel-eu/wiki/wiki/Assembler "Assembler") |
| API: | Noch nicht näher geplant |
| Binärformat: | [ELF](https://github.com/lowlevel-eu/wiki/wiki/Executable-and-Linking-Format "ELF") |
| [IPC-Methode](https://github.com/lowlevel-eu/wiki/wiki/Interprozesskommunikation "IPC"): | Message-Passing, Message-Queues, RPC |
| Homepage |  |

In Planung

  
rizor-OS ist ein kleines Hobby-OS, bei dem ich viel über die LowLevel-Programmierung lernen möchte. Das OS soll später als Projektarbeit und Referenz für und nach dem Studium gelten. Unter Umständen wechsele ich das Projekt zu einem OpenSource-Projekt, das dann unter der GPL-Lizenz laufen würde.

## Entwickler

- rizor

## Userinterface

Zur Interaktion mit dem User sind einfache Terminals geplant. Später soll es dann auch ein Kernel-Terminal geben, das genau angibt, was geschieht und wie die momentane Situation im Kernelspace aussieht. Der User hat dann auch die Möglichkeit, den Kernelspace bedingt zu verändern um Probleme zu beheben. Es soll aber nur eingeschränkten Zugriff geben, damit der Kernel nicht zerstört wird.

## OS-Design

Es soll ein elementarer Hybridkernel angeboten werden. Dieser soll auch ein elementares Filesystem haben, damit er die Boot-Files lesen und die entsprechenden Module laden kann. Manche Module sollen dabei direkt in den Kernelspace geladen werden (z.B. PIC, erweiterte Speicherverwaltung). Alle anderen Module sollen dann im Userspace arbeiten. Dadurch soll eine größtmögliche Portierbarkeit auf andere Architekturen ermöglicht werden. Außerdem sind dann leichter Erweiterungen und Updates möglich. Jeder Task, der einen Syscall anbietet, muss außerdem einen Broadcast-Handler anbieten, damit der Kernel in regelmäßigen Abständen die Funktion der einzelnen Tasks gewährleisten kann. Wenn der Task nach einer bestimmten Zeit nicht reagiert, wird dieser beendet und automatisch vom Kernel neu gestartet. Falls dieser Task zur Interaktion mit anderen Tasks verwendet wurde, wird jedem Task ein Signal geschickt, das ihm sagt, dass er seine Informationen noch einmal schicken soll. Es sei denn, die Informationen befinden sich noch in einer Liste o. ä., die abgearbeitet wird.

## Modulkommunikation

Ein Modul registriert sich im Kernel als Modul an gibt eine Beschreibung ab (meistens den Namen der Hardware die es verwaltet). Außerdem muss das Modul einen Speicherbereich angeben den es für Broadcasts vorsieht. Ein Modul kann beliebig viele Methoden registrieren; es muss nur eine Beschreibung und die Anzahl an Parametern angeben. Wenn es Rückgabewerte gibt, geschieht das über das normale Message-Passing des Kernels. Es kann außerdem entschieden werden, ob der Prozess eine Benachrichtigung erhalten möchte, dass sein Auftrag erfolgreich umgesetzt wurde. Das funktioniert aber nur, wenn das Modul solch eine Möglichkeit bietet. Dadurch ist es möglich, dass die Softwareentwickler zwischen synchroner und asynchroner Kommunikation entscheiden können-

## Interprozesskommunikation

Es wird mehrere Möglichkeiten der Kommunikation geben. Zum einen gibt es Shared-Memory, Message-Passing und dann noch Message-Queues. Beim Shared-Memory, müssen sich die kooperierenden Prozesse selbst um die Synchronisation kümmern. Beim Message-Passing bekommt der Emfänger ein Signal, dass eine Nachricht für ihn bereit liegt. Diese kann er sich dann in seinen Speicher laden. Bei den Message-Queues geschieht es auch nur über Methoden. Jede Nachricht wird in einen Puffer in den Kernel geladen. Wenn der Sender eine größere Nachricht sendet, dann wird das über mehrere Puffer zwischengelagert. Außerdem werden diese großen Nachrichten nur nach und nach in den Kernel geladen. Dadurch muss der Prozess länger warten, aber der Kernel bleibt vom Speicheraufwand her gering.

## OS-Statistiken

- Version: rizor-OS-0.1 Build 0009-Alpha
  - Kernel: 3819 LOC
  - Libc: 316 LOC
  - Kernel-Library: 66 LOC
  - Collection: 7 LOC

## Entwicklungsstatus

- Kernel
  - rizor-0.3.2-Alpha
    - Fertigstellung der Elf-Loader
    - Fertigstellung des Multitaskings
  - rizor-0.3.3
    - Optimierung des Kernels
  - rizor-0.3.4 (Kernel für rizor-os-0.1)
    - letzte Optimierungen
  - rizor-0.4.0-Alpha (Kernel für rizor-os-0.2)
    - Auslagerung der Module
    - Shared-Memory-Handlers
    - Module-RPC
    - Messagepassings
    - Messagequeues
- System
  - rizor-os-0.1
    - Testmethoden
      - physikalische Speicherverwaltung
      - Paging
      - virtuelle Speicherverwaltung
      - Multitasking

## Features

Folgende Features sind implementiert

- x86
- kommunikationsfähiger Hybrid-Kernel
  - CPUID
  - Physikalische Speicherverwaltung
  - Syscalls
  - Paging mit automatischer Flagwahl
  - Speicherverwaltung für Kernel- und User-Space
  - Spinlocks
  - voller Funktionsumfang des KBC
  - kompletter Keyboardhandler mit einem eigenen Keycode
- Teile der libc
- Eine Kernel-Library
- Eine Collection an Datenstrukturen

## Roadmap

- rizor-OS-0.1 (Release: März/April 2009):
  - **Feature Freeze**: 31.03.2009
  - **Geplanter Release**: Ende April/Anfang Mai
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

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/5294/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1816/index.html)

<!-- MediaWiki page 1816; revision 5294; parent 4383; 2009-08-06T15:32:22Z -->
