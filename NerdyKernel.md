# NerdyKernel

| rizor-kernel |  |
| ----------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|  |  |
| Entwickler: | rizor |
| Akt. Version: | 0.0.0.0 |
| [Lizenz](https://github.com/lowlevel-eu/wiki/wiki/Lizenzen "Lizenzen"): | Closed-Source |
| OS-Eigenschaften |  |
| Plattform: | [i386](https://github.com/lowlevel-eu/wiki/wiki/X86 "X86"),[amd64](https://github.com/lowlevel-eu/wiki/wiki/X86-64 "X86-64"),[ARM](https://github.com/lowlevel-eu/wiki/wiki/ARM "ARM") |
| [Kernelart](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel"): | Microkernel |
| [Sprache](https://lowlevel-eu.github.io/wiki/pages/1648/index.html "Kategorie:Programmiersprache"): | [C](https://github.com/lowlevel-eu/wiki/wiki/C "C") & [Assembler](https://github.com/lowlevel-eu/wiki/wiki/Assembler "Assembler") |
| API: | Noch nicht näher geplant |
| Binärformat: | [ELF](https://github.com/lowlevel-eu/wiki/wiki/Executable-and-Linking-Format "ELF") |
| [IPC-Methode](https://github.com/lowlevel-eu/wiki/wiki/Interprozesskommunikation "IPC"): | Message-Passing, Message-Queues, RPC, Shared-Memory |
| Homepage |  |

In Planung

  
rizor-OS ist ein Projekt, dass eine möglichst generische API bieten soll. Dadurch soll erreicht werden, dass man den Kernel möglichst schnell auf beliebige Plattformen portieren kann. Außerdem soll der Kernel die Möglichkeit bieten ein reiner Hypervisor zu sein. Das soll eine Virtualisierung mit möglichst wenig Aufwand ermöglichen, wodurch die VMs schneller werden.

## Entwickler

- rizor

## Kernel-Design

### normaler Kernel

Der Kernel soll verschiedene Möglichkeiten der Kommunikation, der Speicherverwaltung und des Schedulings bieten.

#### Kommunikation

##### x86

Die einzelnen Elemente (Syscalls, IPC, Module-Communication) bekommen ihre eigenen Trap-Gates. Dadurch wird dem Kernel das Verwalten der einzelenen Elemente abgenommen. Bei der Initialisierung wird den Syscalls standardmäßig die 0x80 als Interrupt-Nummer zugewiesen. Die einzelnen IPC-Komponenten beantragen beim IDT-Manager eigene Interrupt-Gates an und registrieren eigene Handler. Das gleiche mach auch die Module-Communication. Wenn nun ein Task eine Nachricht abschicken möchte, fragt er über Syscalls die Interrupt-Nummer ab und löst dann den Interrupt aus. Somit muss der Kernel nur einmal bemüht werden und der IPC-Request kann schneller abgearbeitet werden. Außerdem kommunizieren die Tasks über ein extra Interface mit den Modules. Dadurch wird der Overhead der normalen IPC minimiert.

##### ARM

Bei dieser Architektur läuft alles über Syscalls ab und dadurch wird der Aufwand des Kernels größer, was sich allerdings nicht vermeiden lässt. Damit der Aufwand geringer ausfällt, werden die einzelnen Syscall-Handler in Hash-Tables gespeichert. Dadurch kann der zutreffende Handler schneller aufgerufen werden.

#### Speicherverwaltung

##### physische Speicherverwaltung

Hierbei gibt es mehrere Wahlmöglichkeiten zur Verwaltung. Zum einen kann zwischen 4KiB- und 4MiB-Blöcken gewählt werden, dann kann man auch noch zwischen Bitmaps, Stacks und einer Mischung aus beiden wählen. Bei der Mischung soll Performanz mit Minimierung des Speicheraufwands kombiniert werden.

##### virtuelle Speicherverwaltung

###### i386

Hierbei kann zwischen dem normalen Paging, PSE und PAE gewählt werden. Welche Version benutzt werden soll, wird beim Compile-Vorgang definiert.

###### amd64

Bei dieser Version wird natürlich automatisch PAE benutzt.

###### ARM

Die Speicherverwaltung wird je nach MMU definiert.

### Hypervisor

Der Hypervisor soll nur die CPUs bzw. Prozessoren verwalten und am Ende nur dafür zuständig sein soll, welche VM welchen Interrupt behandelt. Dadurch liegt die Hauptaufgabe bei den VMs und der Hypervisor hat nur einen geringen Verwaltungsaufwand. Außerdem soll er die Möglichkeit bieten, dass man der VM bestimmte Hardware ein- bzw. ausblenden kann. Dadurch soll erreicht werden, dass die VMs nur die Hardware sehen, die sie auch benutzen dürfen. Der Hypervisor läuft standard-mäßig im amd64-Mode.

#### Speicherverwaltung

Abgesehen davon, dass Paging im PAE-Modus betrieben wird, bietet der Hypervisor Shadow- und Nested-Paging

## Code-Statistik

Momentan gibt es noch keine Statistiken zu dem Kernel

## Kernel-Features

Da der Kernel noch in der Version 0.0.0.0 liegt, gibt es auch keine Features

## Roadmap

Wird gerade genauer definiert

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/9555/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1816/index.html)

<!-- MediaWiki page 1816; revision 9555; parent 7620; 2011-02-16T16:18:52Z -->
