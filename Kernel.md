# Kernel

Der **Kernel**, auch **Betriebssystemkernel** genannt, ist der zentrale Bestandteil und die Grundlage eines jeden [Betriebssystems](Betriebssystem "Betriebssystem"). Auf ihn bauen alle anderen Bestandteile des Betriebssystems wie Module, [Treiber](Treiber "Treiber") oder Anwendungen auf. Je nach Anwendungszweck wurden verschiedene Kernelarten mit individuellen Vor- und Nachteilen entwickelt.

  

## Aufgaben eines Kernels

Ein Kernel hat grundsätzlich folgende Basisaufgaben:

- [Speicherverwaltung](Speicherverwaltung "Speicherverwaltung")
- [Prozessverwaltung](Prozessverwaltung "Prozessverwaltung")
- [Interprozesskommunikation](Interprozesskommunikation "Interprozesskommunikation")
- Geräte- und Hardwareverwaltung
- Schnittstelle für [Treiber](Treiber "Treiber")
- [Syscalls](Syscall "Syscall") für Anwendungsprogramme
- [Scheduling](Scheduler "Scheduler")

Architekturabhängige Teile dieser Aufgaben werden normalerweise in einem [Hardware Abstraction Layer](Hardware-Abstraction-Layer "Hardware Abstraction Layer") mit einer klar definierten Schnittstelle gekapselt, um die Wiederverwendbarkeit anderer Komponenten zu erhöhen. Dazu zählen teilweise schon (kleine) Treiber, wie z. B. bei [x86](X86 "X86") bzw. [x64](X86-64 "X64") für die [PIT](Programmable-Interval-Timer "PIT"), [PIC](Programmable-Interrupt-Controller "PIC"), [Local APIC](Local-Advanced-Programmable-Interrupt-Controller "Local APIC") oder ähnlichem.

Je nach Kernelart kommt diesen Aufgaben mehr oder weniger Gewicht zu. Außerdem können z. B. folgende Aufgaben hinzukommen:

- [Dateisystemverwaltung](Dateisystem "Dateisystem")
- ausgewählte weitere Treiber (z. B. Treiber zum Erkennen und Konfigurieren von [PCI](Peripheral-Component-Interconnect "PCI")-Geräten) oder alle Treiber

## Kernelarten

Folgende Kernelarten existieren:

### Monolithischer Kernel

Als monolithischen Kernel bezeichnet man einen Betriebssystemkernel, der nicht nur die typischen Aufgaben eines solchen durchführt, sondern auch gleich Treiber für alle [Hardware](https://lowlevel-eu.github.io/wiki/pages/1447/index.html "Kategorie:Hardware"), das virtuelle Dateisystem, Dateisystemtreiber und vieles mehr enthält. Diese Treiber können entweder fest in den Kernel einkompiliert sein oder zur Laufzeit ladbar sein, laufen aber immer im Kernelmode. Das Treiberinterface besteht somit aus normalen Funktionsaufrufen, was zu einem deutlichen Geschwindigkeitsvorteil führt. Jedoch ist ein solcher Kernel nicht nur unflexibler, sondern auch deutlich fehleranfälliger, und abgestürzte Module führen meist zu einem Absturz des gesamten Systems. Interprozesskommunikation spielt in einem solchen Kernel anfangs sicherlich erstmal eine untergeordnete Rolle, da die gesamte Funktionalität direkt über den Kernel erreichbar ist.

Das folgende Diagramm zeigt den groben Aufbau eines monolithischen Kernels:

  

|  |  |
| ---------------------------------------------------------------------------------- | --------- |
| Hardware |  |
| [HAL](Hardware-Abstraction-Layer "HAL") |  |
| Kernel | Treiber |
| Syscallinterface |  |

Anwendungen, Bibliotheken

blau: Kernelmode

grau: Usermode

  

### Mikrokernel

Bei einem Mikrokernel liegt im Gegensatz zum monolithischen Kernel nur die Implementierung der oben genannten Basisaufgaben im Kernelspace. [Treiber](Treiber "Treiber"), Dateisystemverwaltung (eventuell inklusive virtuellem Dateisystem) und ähnliche Komponenten liegen als gesonderte Prozesse im Userspace und kommunizieren mit dem Kernel über [Syscalls](Syscall "Syscall") bzw. mit anderen Prozessen über [Interprozesskommunikation](Interprozesskommunikation "Interprozesskommunikation"). Der Kernel verwaltet und verteilt also nur die Ressourcen, während die Userspaceprozesse sich um die konkrete Nutzung selbst kümmern. Somit kann ein fehlerhafter [Treiber](Treiber "Treiber") nicht das ganze [Betriebssystem](Betriebssystem "Betriebssystem") zum Absturz bringen und eventuell neu gestartet werden. Letzteres funktioniert allerdings nur bei einem entsprechenden Design des Kernels, der Interprozesskommunikation und anderer Komponenten, da z. B. ein abstürzender Festplattentreiber, der die Betriebssystempartition verwaltet, nicht so ohne weiteres nachgeladen werden kann, sondern permanent im Speicher vorgehalten werden muss.

Da die Treiber nicht im Kernel sind, ist es wesentlich, dass der Bootloader auch die Treiber laden kann und diesen dem Kernel übergibt. Dies ist von Haus aus z. B. über [GRUB](Grand-Unified-Bootloader "GRUB") möglich.

Prominenter Verfechter dieser Kernelart ist u.a. Andrew S. Tanenbaum, der dieses Prinip in [Minix](Minix "Minix") verwendet.

Das folgende Diagramm zeigt den groben Aufbau eines Mikrokernels:

  

|  |  |
| ---------------------------------------------------------------------------------- | ------------------------------------ |
| Hardware |  |
| [HAL](Hardware-Abstraction-Layer "HAL") |  |
| Kernel |  |
| Syscallinterface | Syscallinterface (Hardwarezugriff) |
| Anwendungen, Bibliotheken | Treiber |

### Exokernel

Im Unterschied zu einem Mikrokernel liegt beim Exokernel der Fokus darauf, das Verwalten (z. B. das Layout des Adressraums, abgesehen vom Kernel) und das Schützen (z. B. sollen zwei Anwendungen nicht unkontrolliert die gleichen Pages verwenden) von Ressourcen voneinander zu trennen. Das Schützen der Ressourcen soll weiterhin im Kernel verbleiben, aber die Verwaltung soll in einer Bibliothek (meist als libOS bezeichnet) im Userspace erfolgen. Jede Anwendung wird dann gegen eine solche libOS, die z. B. die Verwaltung des Adressraums übernimmt oder auch wie ein Treiber direkt auf die Hardware zugreifen kann (wobei durch den Kernel sichergestellt wird, dass dieser Zugriff nicht in Konflikt mit anderen Zugriffen anderer Anwendungen steht), gelinkt, d. h. im Gegensatz zum Mikrokernel, bei dem es genau einen Treiber in einem eigenen Prozess gibt, kann beim Exokernel (für bestimmte Hardware) in jeder libOS ein Treiber existieren. Dadurch hat jede Anwendung größtmögliche Freiheit – ohne dabei in Konflikt mit anderen Anwendungen zu stehen – was die Nutzung von Ressourcen angeht. Eine Spezialanwendung kann dann auch eine eigene libOS, die auf diese spezielle Anwendung hin optimiert ist, implementieren.

Es ist allerdings nicht sonderlich fruchtbar sich einen Exokernel als einen Mikrokernel ins Extrem getrieben vorzustellen, sondern vom ursprünglich monolithischen Kerneldesign her gesehen sind Mikro- bzw. Exokernel zwei orthogonale Designentscheidungen: Beim Mikrokernel werden Treiber in **einen** separaten Prozess ausgelagert, beim Exokernel in **jede** Anwendung. Auch abstrahiert ein Exokernel nicht immer weniger als ein Mikrokernel, z. B. findet sich meist ein Festplattentreiber im Exokernel und die Anwendungen können Sektoren allozieren: Der Schutz ist gewährleistet, aber die Verwaltung wird der konkreten Anwendung/libOS überlassen. In einem Mikrokernel hingegen befindet sich der Festplattentreiber typischerweise in einem separaten Prozess im Userspace. Nur wenn man den Mikrokernel und die umgebenden Serverprozesse betrachtet, die, um in dem Beispiel zu bleiben, sehr wahrscheinlich als Abstraktion am Ende eine Datei anbieten (ohne dass man überhaupt auf Sektoren Zugriff hätte), kommt man zu dem Schluss, dass der Exokernel weniger Abstraktion vorwegnimmt.

### Makrokernel

Der Makrokernel, manchmal auch Hybridkernel genannt, befindet sich auf einer Skala von Mikrokernel zum monolithischen Kernel irgendwo dazwischen und es ist somit nicht näher definiert, was genau ein Makrokernel ist. Man will dabei die Geschwindigkeitsvorteile eines monolithischen Kernels und die Stabilität und Flexibilität eines Mikrokernels kombinieren. Ab NT 3.1 bezeichnet man [Windows](Windows "Windows") als Hybridkernel.

## Links

- [Erklärung zum Mikro- und L4-Kernel](assets/904ad80cc1c81c6b6e5d.pdf "Die L4-Mikrokernel-Familie.pdf")
- [The Exokernel Operating System Architecture](http://pdos.csail.mit.edu/exo/theses/engler/thesis.ps)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/9840/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1478/index.html)

<!-- MediaWiki page 1478; revision 9840; parent 8651; 2011-06-11T20:50:18Z -->
