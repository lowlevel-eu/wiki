# Kernel

Der **Kernel**, auch **Betriebssystemkernel** genannt, ist der zentraler Bestandteil und die Grundlage eines jeden [Betriebssystems](https://github.com/lowlevel-eu/wiki/wiki/Betriebssystem "Betriebssystem"). Auf ihn bauen alle anderen Bestandteile des Betriebssystems wie Module, [Treiber](https://github.com/lowlevel-eu/wiki/wiki/Treiber "Treiber") oder Anwendungen auf. Je nach Anwendungszweck wurden verschiedene Kernelarten mit individuellen Vor- und Nachteilen entwickelt. Ein bekannter Betriebssystemkernel ist der [Linuxkernel](https://github.com/lowlevel-eu/wiki/wiki/Linux "Linux").

## Aufgaben eines Kernels

Ein Kernel hat meist folgenden Aufgaben:

- Speicherverwaltung
- Prozessverwaltung
- Geräte- und Hardwareverwaltung (evtl. mit Hilfe einer [HAL](https://github.com/lowlevel-eu/wiki/wiki/Hardware-Abstraction-Layer "HAL"))
- Schnittstelle für [Treiber](https://github.com/lowlevel-eu/wiki/wiki/Treiber "Treiber") oder Anwendungsprogramme
- [Dateisystemverwaltung](https://github.com/lowlevel-eu/wiki/wiki/Dateisystem "Dateisystem")

## Kernelarten

Folgenden Kernelarten existieren:

### Monolithischer Kernel

Als monolithischen Kernel bezeichnet man einen Betriebssystemkernel, der nicht nur die typischen Aufgaben eines solchen durchführt, sondern auch gleich Treiber für [Hardware](https://lowlevel-eu.github.io/wiki/pages/1447/index.html "Kategorie:Hardware") und andere Funktionen mit sich bringt. Dadurch müssen nicht erst Treiber oder Module nachgeladen werden und auch eine Schnittstelle ist nicht erforderlich, was einen deutlichen Geschwindigkeitsvorteil mit sich bringt. Jedoch ist ein solcher Kernel nicht nur unflexibler, sondern auch deutlich fehleranfälliger und abgestürzte Module können nicht ohne weiteres neu gestartet werden. Außerdem macht die fehlende Hardwareabstraktion den Kernel schwieriger zu entwickeln, wenn er nicht Mechanismen wie genormte Treiberinterfaces oder Ähnliches anbietet. Der Linuxkernel ist ein Monolithischer Kernel.

#### Diagramm zur Veranschaulichung

Dieses Diagramm zeigt den groben Aufbau eines monolitschen Kernels.  
Datei:Makro kelin corr.png

### Mikrokernel

Der Mikrokernel steht im Gegensatz zum monolithischen Kernel, da bei ihm nur ein sehr kleiner Teil der Funktionalität wirklich im Kernelspace liegt. [Treiber](https://github.com/lowlevel-eu/wiki/wiki/Treiber "Treiber"), I/O und ähnliche Komponenten liegen als gesonderte Prozesse im Userspace und kommunizieren mit dem Kernel. Der Kernel verwaltet und verteilt also die Ressourcen, während die Userspaceprozesse sich um die konkrete Nutzung selbst kümmern. Somit kann ein fehlerhafter [Treiber](https://github.com/lowlevel-eu/wiki/wiki/Treiber "Treiber") nicht das ganze [Betriebssystem](https://github.com/lowlevel-eu/wiki/wiki/Betriebssystem "Betriebssystem") zum Absturz bringen und einfach neu gestartet werden. Außerdem kann der Kernel an sich leicht für unterschiedlichste Systeme portiert werden, da die systemabhängigen Treiber nicht im Kernel sind, und der Kernel vom Aufbau des Systems idealerweise nichts wissen muss.

Prominenter Verfechter dieser Kernelart ist u.a. Andrew S. Tanenbaum, der dieses Prinip in [Minix](https://github.com/lowlevel-eu/wiki/wiki/Minix "Minix") verwendet.

#### Diagramm zur Veranschaulichung

Dieses Diagramm zeigt den groben Aufbau eines Mikrokernels.  
![mikrokernel_klein.png](http://be59.be.funpic.de/Lowlevel/mikrokernel_klein.png)

### [Exokernel](https://github.com/lowlevel-eu/wiki/wiki/Kernel#exokernel "Exokernel")

Der Exokernel ist eine Unterart des Mikrokernel. Bei ein Exokernel liegt die HAL in Biblitoheken, die vom Programm eingebunden werden können. Jedoch kann das Programm genau so gut selbst auf die Hardware zugreifen. Der Vorteil ist damit höhere Flexibilität für den Programmierer, und die bessere Möglichkeit, ein anderes System und dessen API durch eine spezielle Bibliothek zu emulieren.

Ein Beispiel für einen Exokernel ist das [xok](http://pdos.csail.mit.edu/exo/)-System vom MIT.

### [Makrokernel](https://github.com/lowlevel-eu/wiki/wiki/Kernel#makrokernel "Makrokernel")

Der Makrokernel, auch Hybridkernel genannt, ist eine Verschmelzung zwischen einem monolithischem Kernel und Mikrokernel, die jedoch nicht genau definiert ist. Damit will man die Geschwindigkeitsvorteile eines monolithischen Kernels und die Stabilität und Flexibilität eines Mikrokernels kombinieren. Ab NT 3.1 bezeichnet man [Windows](https://github.com/lowlevel-eu/wiki/wiki/Windows "Windows") als Hybridkernel.

## Links

[Erklärung zum Mikro- und L4Kernel](http://www.weihenstephan.org/~michaste/down/steil-l4.pdf)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/5792/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1478/index.html)

<!-- MediaWiki page 1478; revision 5792; parent 5791; 2009-08-31T06:19:49Z -->
