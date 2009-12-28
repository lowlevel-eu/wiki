# Kernel

Der **Kernel**, auch **Betriebssystemkernel** genannt, ist der zentraler Bestandteil und die Grundlage eines jeden [Betriebssystems](https://github.com/lowlevel-eu/wiki/wiki/Betriebssystem "Betriebssystem"). Auf ihn bauen alle anderen Bestandteile des Betriebssystems wie Module, [Treiber](https://github.com/lowlevel-eu/wiki/wiki/Treiber "Treiber") oder Anwendungen auf. Je nach Anwendungszweck wurden verschiedene Kernelarten mit individuellen Vor- und Nachteilen entwickelt.

  

## Aufgaben eines Kernels

Ein Kernel hat grundsätzlich folgende Basisaufgaben:

- [Speicherverwaltung](https://github.com/lowlevel-eu/wiki/wiki/Speicherverwaltung "Speicherverwaltung")
- [Prozessverwaltung](https://github.com/lowlevel-eu/wiki/wiki/Prozessverwaltung "Prozessverwaltung")
- [Interprozesskommunikation](https://github.com/lowlevel-eu/wiki/wiki/Interprozesskommunikation "Interprozesskommunikation")
- Geräte- und Hardwareverwaltung
- Schnittstelle für [Treiber](https://github.com/lowlevel-eu/wiki/wiki/Treiber "Treiber")
- [Syscalls](https://github.com/lowlevel-eu/wiki/wiki/Syscall "Syscall") für Anwendungsprogramme
- Scheduling

Architekturabhängige Teile dieser Aufgaben werden normalerweise in einem [Hardware Abstraction Layer](https://github.com/lowlevel-eu/wiki/wiki/Hardware-Abstraction-Layer "Hardware Abstraction Layer") mit einer klar definierten Schnittstelle gekapselt, um die Wiederverwendbarkeit anderer Komponenten zu erhöhen. Dazu zählen teilweise schon (kleine) Treiber, wie z. B. bei [x86](https://github.com/lowlevel-eu/wiki/wiki/X86 "X86") bzw. [x64](https://github.com/lowlevel-eu/wiki/wiki/X86-64 "X64") für die [PIT](https://github.com/lowlevel-eu/wiki/wiki/Programmable-Interval-Timer "PIT"), [PIC](https://github.com/lowlevel-eu/wiki/wiki/Programmable-Interrupt-Controller "PIC"), [Local APIC](https://github.com/lowlevel-eu/wiki/wiki/Local-Advanced-Programmable-Interrupt-Controller "Local APIC") oder ähnlichem.

Je nach Kernelart kommt diesen Aufgaben mehr oder weniger Gewicht zu. Außerdem können z. B. folgende Aufgaben hinzukommen:

- [Dateisystemverwaltung](https://github.com/lowlevel-eu/wiki/wiki/Dateisystem "Dateisystem")
- ausgewählte weitere Treiber (z. B. Treiber zum Erkennen und Konfigurieren von [PCI](https://github.com/lowlevel-eu/wiki/wiki/Peripheral-Component-Interconnect "PCI")-Geräten) oder alle Treiber

## Kernelarten

Folgende Kernelarten existieren:

### Monolithischer Kernel

Als monolithischen Kernel bezeichnet man einen Betriebssystemkernel, der nicht nur die typischen Aufgaben eines solchen durchführt, sondern auch gleich Treiber für alle [Hardware](https://lowlevel-eu.github.io/wiki/pages/1447/index.html "Kategorie:Hardware"), das virtuelle Dateisystem, Dateisystemtreiber und vieles mehr enthält. Diese Treiber können entweder fest in den Kernel einkompiliert sein oder zur Laufzeit ladbar sein, laufen aber immer im Kernelmode. Das Treiberinterface besteht somit aus normalen Funktionsaufrufen, was zu einem deutlichen Geschwindigkeitsvorteil führt. Jedoch ist ein solcher Kernel nicht nur unflexibler, sondern auch deutlich fehleranfälliger und abgestürzte Module führen meist zu einem Absturz des gesamten Systems. Interprozesskommunikation spielt in einem solchen Kernel anfangs sicherlich erstmal eine untergeordnete Rolle, da die ges. Funktionalität direkt über den Kernel erreichbar ist.

Das folgende Diagramm zeigt den groben Aufbau eines monolithischen Kernels:

  

Datei:Makro kelin corr.png

  

### Mikrokernel

Bei einem Mikrokernel liegt im Gegensatz zum monolithischen Kernel nur die Implementierung der oben genannten Basisaufgaben im Kernelspace. [Treiber](https://github.com/lowlevel-eu/wiki/wiki/Treiber "Treiber"), Dateisystemverwaltung (eventuell inklusive virtuellem Dateisystem) und ähnliche Komponenten liegen als gesonderte Prozesse im Userspace und kommunizieren mit dem Kernel über [Syscalls](https://github.com/lowlevel-eu/wiki/wiki/Syscall "Syscall") bzw. mit anderen Prozessen über [Interprozesskommunikation](https://github.com/lowlevel-eu/wiki/wiki/Interprozesskommunikation "Interprozesskommunikation"). Der Kernel verwaltet und verteilt also nur die Ressourcen, während die Userspaceprozesse sich um die konkrete Nutzung selbst kümmern. Somit kann ein fehlerhafter [Treiber](https://github.com/lowlevel-eu/wiki/wiki/Treiber "Treiber") nicht das ganze [Betriebssystem](https://github.com/lowlevel-eu/wiki/wiki/Betriebssystem "Betriebssystem") zum Absturz bringen und eventuell neu gestartet werden. Letzteres funktioniert allerdings nur bei einem entsprechenden Design des Kernels, der Interprozesskommunikation und anderer Komponenten, da z. B. ein abstürzender Festplattentreiber, der die Betriebssystempartition verwaltet, nicht so ohne weiteres nachgeladen werden kann, sondern permanent im Speicher vorgehalten werden muss.

Prominenter Verfechter dieser Kernelart ist u.a. Andrew S. Tanenbaum, der dieses Prinip in [Minix](https://github.com/lowlevel-eu/wiki/wiki/Minix "Minix") verwendet.

Das folgende Diagramm zeigt den groben Aufbau eines Mikrokernels:

  

![mikrokernel_klein.png](http://be59.be.funpic.de/Lowlevel/mikrokernel_klein.png)

  

### [Exokernel](https://github.com/lowlevel-eu/wiki/wiki/Kernel#exokernel "Exokernel")

Der Exokernel ist eine Unterart des Mikrokernel. Bei ein Exokernel liegt die HAL in Biblitoheken, die vom Programm eingebunden werden können. Jedoch kann das Programm genau so gut selbst auf die Hardware zugreifen. Der Vorteil ist damit höhere Flexibilität für den Programmierer, und die bessere Möglichkeit, ein anderes System und dessen API durch eine spezielle Bibliothek zu emulieren.

Ein Beispiel für einen Exokernel ist das [xok](http://pdos.csail.mit.edu/exo/)-System vom MIT.

### [Makrokernel](https://github.com/lowlevel-eu/wiki/wiki/Kernel#makrokernel "Makrokernel")

Der Makrokernel, auch Hybridkernel genannt, ist eine Verschmelzung zwischen einem monolithischem Kernel und Mikrokernel, die jedoch nicht genau definiert ist. Damit will man die Geschwindigkeitsvorteile eines monolithischen Kernels und die Stabilität und Flexibilität eines Mikrokernels kombinieren. Ab NT 3.1 bezeichnet man [Windows](https://github.com/lowlevel-eu/wiki/wiki/Windows "Windows") als Hybridkernel.

## Links

[Erklärung zum Mikro- und L4Kernel](http://www.weihenstephan.org/~michaste/down/steil-l4.pdf)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/6664/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1478/index.html)

<!-- MediaWiki page 1478; revision 6664; parent 6658; 2009-12-28T16:41:20Z -->
