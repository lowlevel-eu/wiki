# Kernel

Der **Kernel**, auch **Betriebssystemkernel** genannt, ist der zentraler Bestandteil und die Grundlage eines jeden [Betriebssystems](https://github.com/lowlevel-eu/wiki/wiki/Betriebssystem "Betriebssystem"). Auf ihn bauen alle anderen Bestandteile des Betriebssystems wie Module, [Treiber](https://github.com/lowlevel-eu/wiki/wiki/Treiber "Treiber") oder Anwendungen auf. Je nach Anwendungszweck wurden verschiedene Kernelarten mit individuellen Vor- und Nachteilen entwickelt. Ein bekannter Betriebssystemkernel ist der [Linuxkernel](https://github.com/lowlevel-eu/wiki/wiki/Linux "Linux").

## Aufgaben eines Kernels

Ein Kernel hat meist folgenden Aufgaben:

- Speicherverwaltung
- Prozessverwaltung
- Geräte- und Hardwareverwaltung (evt. mit Hilfe einer [HAL](https://github.com/lowlevel-eu/wiki/wiki/Hardware-Abstraction-Layer "HAL"))
- Schnittstelle für [Treiber](https://github.com/lowlevel-eu/wiki/wiki/Treiber "Treiber") oder Anwendungsprogramme
- [Dateisystemverwaltung](https://github.com/lowlevel-eu/wiki/wiki/Dateisystem "Dateisystem")

## Kernelarten

Folgenden Kernelarten exirstieren:

### Monolithischer Kernel

Als monolithischen Kernel bezeichnet man einen Betriebssystemkernel, der nicht nur die typischen Aufgaben eines solchen durchführt, sondern auch gleich [Treiber](https://github.com/lowlevel-eu/wiki/wiki/Treiber "Treiber") für und andere Funktionen mit sich bringt. Dadurch müssen nicht erst [Treiber](https://github.com/lowlevel-eu/wiki/wiki/Treiber "Treiber") oder Module nachgeladen werden und auch eine Schnittstelle ist nicht erforderlich, was einen deutlichen Geschwindigkeitsvorteil mit sich bringt. Jedoch ist ein solcher Kernel nicht nur unflexibler, sondern auch deutlich fehleranfälliger und abgestürzte Module können nicht ohne weiteres neu gestartet werden. Der [Linuxkernel](https://github.com/lowlevel-eu/wiki/wiki/Linux "Linux") ist ein Monolithischer Kernel.

#### Diagramm zum Veranschaulichen

Dieses Diagramm zeigt den groben Aufbau eines monolitschen Kernels.  
![makro_kelin.png](http://be59.be.funpic.de/Lowlevel/makro_kelin.png)

### Mikrokernel

Der Mikrokernel steht im Gegensatz zum monolithischen Kernel, da bei ihm nur ein sehr kleiner Teil der Funktionalität wirklich im Kernelspace liegt. [Treiber](https://github.com/lowlevel-eu/wiki/wiki/Treiber "Treiber"), I/O und ähnliche Komponenten liegen als gesonderte Prozesse im Userspace und kommunizieren mit dem Kernel. Somit kann ein fehlerhafter [Treiber](https://github.com/lowlevel-eu/wiki/wiki/Treiber "Treiber") nicht das ganze [Betriebssystem](https://github.com/lowlevel-eu/wiki/wiki/Betriebssystem "Betriebssystem") zum Absturz bringen und einfach neu gestartet werden. Prominenter Verfechter dieser Kernelart ist u.a. Andrew S. Tanenbaum.

#### Diagramm zum Veranschaulichen

Dieses Diagramm zeigt den groben Aufbau eines Mikrokernels.  
![mikrokernel_klein.png](http://be59.be.funpic.de/Lowlevel/mikrokernel_klein.png)

### [Exokernel](https://github.com/lowlevel-eu/wiki/wiki/Kernel#exokernel "Exokernel")

Der Exokernel ist eine Unterart des Mikrokernel. Bei ein Exokernel kann jedes Programm auf die Hardware zugreifen, da es keine [HAL](https://github.com/lowlevel-eu/wiki/wiki/Hardware-Abstraction-Layer "HAL") gibt. Da nicht jedes Programm Hardwarezugriff braucht, sind auch Bibliotheken da, die die Hardware abstraktieren.

### [Makrokernel](https://github.com/lowlevel-eu/wiki/wiki/Kernel#makrokernel "Makrokernel")

Der Makrokernel, auch Hybridkernel genannt, ist eine Verschmelzung zwischen einem monolithischem Kernel und Mikrokernel, die jedoch nicht genau definiert ist. Damit will man die Geschwindigkeitsvorteile eines monolithischen Kernels und die Stabilität und Flexibilität eines Mikrokernels kombinieren. Ab NT 3.1 bezeichnet man [Windows](https://github.com/lowlevel-eu/wiki/wiki/Windows "Windows") als Hybridkernel.

## Links

[Erklärung zum Mikro- und L4Kernel](http://www.weihenstephan.org/~michaste/down/steil-l4.pdf)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/5143/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1478/index.html)

<!-- MediaWiki page 1478; revision 5143; parent 5142; 2009-08-06T10:08:55Z -->
