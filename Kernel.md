# Kernel

Der **Kernel**, auch **Betriebssystemkernel** genannt, ist der zentraler Bestandteil und die Grundlage eines jeden [Betriebssystems](https://github.com/lowlevel-eu/wiki/wiki/Betriebssystem "Betriebssystem"). Auf ihn bauen alle anderen Bestandteile des Betriebssystems wie Module, [Treiber](https://github.com/lowlevel-eu/wiki/wiki/Treiber "Treiber") oder Anwendungen auf. Je nach Anwendungszweck wurden verschiedene Kernelarten mit individuellen Vor- und Nachteilen entwickelt. Bekannte Betriebssystemkernel sind u.a. der [Linux-Kernel](https://github.com/lowlevel-eu/wiki/wiki/Linux "Linux") oder NTOSKRNL ([Windows](https://github.com/lowlevel-eu/wiki/wiki/Windows "Windows") NT Kernel).

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

Als monolithischen Kernel bezeichnet man einen Betriebssystemkernel, der nicht nur die typischen Aufgaben eines solchen durchführt, sondern auch gleich [Treiber](https://github.com/lowlevel-eu/wiki/wiki/Treiber "Treiber") für [Hardware](https://lowlevel-eu.github.io/wiki/pages/1953/index.html "Hardware") und andere Funktionen mit sich bringt. Dadurch müssen nicht erst [Treiber](https://github.com/lowlevel-eu/wiki/wiki/Treiber "Treiber") oder Module nachgeladen werden und auch eine Schnittstelle ist nicht erforderlich, was einen deutlichen Geschwindigkeitsvorteil mit sich bringt. Jedoch ist ein solcher Kernel nicht nur unflexibler, sondern auch deutlich fehleranfälliger und abgestürzte Module können nicht ohne weiteres neu gestartet werden. Der [Linuxkernel](https://github.com/lowlevel-eu/wiki/wiki/Linux "Linux") ist ein Monolithischer Kernel.

### Mikrokernel

Der Mikrokernel hat meist deutlich weniger Funktionen als ein monolithischer Kernel, da er nur die wesentlichen Funktionen bereitstellt. [Treiber](https://github.com/lowlevel-eu/wiki/wiki/Treiber "Treiber") und weitere Funktionen werden über zusätzliche Module hinzugefügt, welche auch als eigenständige Prozesse laufen können und gegenüber dem Kernel sicher abgeschottet sind. Somit kann ein fehlerhafter [Treiber](https://github.com/lowlevel-eu/wiki/wiki/Treiber "Treiber") nicht das ganze [Betriebssystem](https://github.com/lowlevel-eu/wiki/wiki/Betriebssystem "Betriebssystem") zum Absturz bringen und einfach neu gestartet werden. Prominenter Verfechter dieser Kernelart ist u.a. Andrew S. Tanenbaum.

#### [Exokernel](https://github.com/lowlevel-eu/wiki/wiki/Kernel#exokernel "Exokernel")

Der Exokernel ist eine Unterart des Mikrokernel. Bei ein Exokernel kann jedes Programm auf die Hardware zugreifen, da es keine [HAL](https://github.com/lowlevel-eu/wiki/wiki/Hardware-Abstraction-Layer "HAL") gibt. Da nicht jedes Programm Hardwarezugriff braucht, sind auch Bibliotheken da, die die Hardware abstraktieren.

### Makrokernel

Der Makrokernel, auch Hybridkernel genannt, ist eine Verschmelzung zwischen einem monolithischem Kernel und Mikrokernel, die jedoch nicht genau definiert ist. Damit will man die Geschwindigkeitsvorteile eines monolithischen Kernels und die Stabilität und Flexibilität eines Mikrokernels kombinieren. Ab NT4 bezeichnet man [Windows](https://github.com/lowlevel-eu/wiki/wiki/Windows "Windows") als Hybridkernel.

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/3500/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1478/index.html)

<!-- MediaWiki page 1478; revision 3500; parent 3239; 2008-11-09T12:34:52Z -->
