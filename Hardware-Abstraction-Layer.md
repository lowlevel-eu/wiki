# Hardware Abstraction Layer

Die **HAL** (**H**ardware **A**bstraction **L**ayer) bezeichnet eine Softwareschicht, die zwischen der Hardware und dem [Betriebssystemkernel](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel") liegt. Sie hat die Aufgabe, hardwarespezifische Funktionen auszulagern, um eine spätere Portierung zu erleichtern, da im besten Fall nur die HAL angepasst werden muss. Die verbreitesten Betriebsysteme haben eine HAL.

## Aufgaben

Die HAL beinhaltet somit folgende Aufgaben, wobei zu beachten ist, dass das nur mögliche Teile einer HAL sind. Was genau der HAL macht hängt sehr von der Struktur des OS ab. In gewissen Grenzen ist es auch eine Sache der persönlichen/subjektiven Definition ob bestimmte Code-Fragmente vom OS Teil des HAL sind oder einer anderen Komponente zugeordnet werden.

### I/O-Ports

Um I/O-Ports zu verwalten könnten Funktionen zum Allozieren und Freigeben von [I/O-Ports](https://github.com/lowlevel-eu/wiki/wiki/I-O-Ports "I/O-Port") zur Verfügung gestellt werden, falls die Architektur (wie z. B. [x86](https://github.com/lowlevel-eu/wiki/wiki/X86 "X86") und [x86-64](https://github.com/lowlevel-eu/wiki/wiki/X86-64 "X86-64")) I/O-Ports zur Verfügung stellt. Außerdem werden Funktionen benötigt um auf die I/O-Ports zuzugreifen.

### Memory-mapped I/O

Zusätzlich zu den I/O-Ports &#150; oft auch anstelle der I/O-Ports &#150; wird von der Architektur an bestimmmten Speicherbereichen nicht normaler RAM eingeblendet, sondern Register von Hardwarekomponenten. Es kann deshalb sinnvoll sein, Funktionen zum Allozieren, Freigeben und zum Zugriff auf solche Speicherbereiche vorzusehen. Dabei ist zu beachten, dass in [C](https://github.com/lowlevel-eu/wiki/wiki/C "C") und [C++](https://github.com/lowlevel-eu/wiki/wiki/C%2B%2B "C++") der type-qualifier *volatile* verwendet werden sollte, um auf solche Speicherbereiche zuzugreifen.

### Interruptverwaltung

Damit die angeschlossene Hardware einem Treiber irgendwelche Ereignisse signalisieren kann, stellt die Architektur meist [Interrupts](https://github.com/lowlevel-eu/wiki/wiki/Interrupt "Interrupt") bzw. genauer [IRQs](https://github.com/lowlevel-eu/wiki/wiki/Programmable-Interrupt-Controller#irq-tabelle "IRQ") zur Verfügung. Um Interrupts zu verwenden ist zum einen meist eine Tabelle mit den Adressen von [ISRs](https://github.com/lowlevel-eu/wiki/wiki/Interrupt-Service-Routine "ISR") (*Interrupt Service Routines*; bei [x86](https://github.com/lowlevel-eu/wiki/wiki/X86 "X86")/[x86-64](https://github.com/lowlevel-eu/wiki/wiki/X86-64 "X86-64") ist diese Tabelle die [IDT](https://github.com/lowlevel-eu/wiki/wiki/Interrupt-Descriptor-Table "IDT") im [Protected-](https://github.com/lowlevel-eu/wiki/wiki/Protected-Mode "Protected Mode") und [Long-Mode](https://github.com/lowlevel-eu/wiki/wiki/Long-Mode "Long Mode")) notwendig. Zum anderen werden die ISR-Stubs von der HAL bereitgestellt, da diese meist in Assembler geschrieben und damit sehr architekturspezifisch sind. IRQs werden meist über eine spezielle Hardwarekomponente &#150; bei [x86](https://github.com/lowlevel-eu/wiki/wiki/X86 "X86") bzw. [x86-64](https://github.com/lowlevel-eu/wiki/wiki/X86-64 "X86-64") ist das die [PIC](https://github.com/lowlevel-eu/wiki/wiki/Programmable-Interrupt-Controller "PIC") oder in neueren Systemen auch die [I/O APIC](https://github.com/lowlevel-eu/wiki/wiki/I-O-Advanced-Programmable-Interrupt-Controller "I/O APIC") (im Zusammenspiel mit der [Local APIC](https://github.com/lowlevel-eu/wiki/wiki/Local-Advanced-Programmable-Interrupt-Controller "Local APIC") dann) &#150; auf Interrupts abgebildet. Daher ist ein Treiber für diese Hardwarekomponente auch Teil der HAL.

Nach außen werden dann Funktionen zum Registrieren von Handlern für Interrupts bzw. IRQs bereitgestellt. Beim Auftreten des entsprechenden Interrupts werden diese Handler dann von den ISR-Stubs der HAL aufgerufen.

### Syscallverwaltung

Damit Anwendungen Kernelfunktionalität nutzen können werden vom Kernel [Syscalls](https://github.com/lowlevel-eu/wiki/wiki/Syscall "Syscall") zur Verfügung gestellt. Da die Art, wie diese Syscalls vom Usermode aus aufgerufen werden, architekturspezifisch ist &#150; meist über Interrupts oder Spezialinstruktionen wie *[sysenter](https://github.com/lowlevel-eu/wiki/wiki/Sysenter "Sysenter")* oder *syscall* &#150; sind Stubs, welche die Implementierung der Syscalls aufrufen, meist Teil der HAL.

### Speicherverwaltung

Auch Teile der [physischen Speicherverwaltung](https://github.com/lowlevel-eu/wiki/wiki/Physische-Speicherverwaltung "Physische Speicherverwaltung") (z. B. die Größe der Pages) und die komplette [virtuellen Speicherverwaltung](https://github.com/lowlevel-eu/wiki/wiki/Speicherverwaltung#virtuelle-speicherverwaltung "Speicherverwaltung") sind architekturspezifisch und damit Teil der HAL.

Bei [x86](https://github.com/lowlevel-eu/wiki/wiki/X86 "X86") bzw. [x86-64](https://github.com/lowlevel-eu/wiki/wiki/X86-64 "X86-64") fällt hierunter auch die [GDT](https://github.com/lowlevel-eu/wiki/wiki/Global-Descriptor-Table "GDT").

### Scheduling

Der [Scheduler](https://github.com/lowlevel-eu/wiki/wiki/Scheduler "Scheduler") hat unter anderem die Aufgabe den Kontext zu wechseln. Dabei müssen Register gesichert und wiederhergestellt werden und außerdem der virtuelle Adressraum gewechselt werden, d. h. dieser Teil des Schedulers ist extrem abhängig von der Architektur und gehört somit auch zur HAL. Außerdem muss der Scheduler von einem Timer &#150; bei [x86](https://github.com/lowlevel-eu/wiki/wiki/X86 "X86")/[x86-64](https://github.com/lowlevel-eu/wiki/wiki/X86-64 "X86-64") die [PIT](https://github.com/lowlevel-eu/wiki/wiki/Programmable-Interval-Timer "PIT"), der [RTC](https://github.com/lowlevel-eu/wiki/wiki/Real-Time-Clock "RTC"), die [Local APIC](https://github.com/lowlevel-eu/wiki/wiki/Local-Advanced-Programmable-Interrupt-Controller "Local APIC")-Timer oder der HPET &#150; aufgerufen werden, d. h. der Treiber für diesen Timer könnte auch Teil der HAL sein.

### Plug-and-Play

Das OS muss oft erst die im System vorhandenen Geräte alle finden und die benutzten (Speicher-/IO-/Interupt-)Ressourcen ermitteln oder selber vergeben. Dazu werden für moderne Hardware-Komponenten üblicherweise die Plug-and-Play-Mechanismen des betreffenden Busses (über den das Gerät dem System zugänglich ist) benutzt. Bei z.B. [PCI](https://github.com/lowlevel-eu/wiki/wiki/Peripheral-Component-Interconnect "PCI")-Geräten wird dazu der PCI-Config-Space benutzt und damit nicht alle Treiber selber direkt darauf zugreifen müssen bietet der OS-Kernel üblicherweise passende Funktionen an welche wiederum als Teil des HAL gezählt werden können.

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/9837/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1480/index.html)

<!-- MediaWiki page 1480; revision 9837; parent 9546; 2011-06-11T20:46:51Z -->
