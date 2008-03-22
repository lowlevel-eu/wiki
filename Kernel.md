# Kernel

Der **Kernel**, auch **Betriebssystemkernel** genannt, ist der zentraler Bestandteil und die Grundlage eines jeden [Betriebssystems](https://github.com/lowlevel-eu/wiki/wiki/Betriebssystem "Betriebssystem"). Auf ihn bauen alle anderen Bestandteile des Betriebssystems wie Module, Treiber oder Anwendungen auf. Je nach Anwendungszweck wurden verschiedene Kernelarten mit individuellen Vor- und Nachteilen entwickelt. Bekannte Betriebssystemkernel sind u.a. der Linux-Kernel oder NTOSKRNL (Windows NT Kernel).

## Aufgaben eines Kernels

Ein Kernel hat meist folgenden Aufgaben:

- Speicherverwaltung
- Prozessverwaltung
- Geräte- und Hardwareverwaltung (evt. mit Hilfe einer [HAL](https://github.com/lowlevel-eu/wiki/wiki/Hardware-Abstraction-Layer "HAL"))
- Schnittstelle für Treiber oder Anwendungsprogramme
- Dateisystemverwaltung

## Kernelarten

Folgenden Kernelarten treten am häufigsten auf:

- **Monolithischer Kernel:**

Als monolithischen Kernel bezeichnet man einen Betriebssystemkernel, der nicht nur die typischen Aufgaben eines solchen durchführt, sondern auch gleich Treiber für Hardware und andere Funktionen mit sich bringt. Dadurch müssen nicht erst Treiber oder Module nachgeladen werden und auch eine Schnittstelle ist nicht erforderlich, was einen deutlichen Geschwindigkeitsvorteil mit sich bringt. Jedoch ist ein solcher Kernel nicht nur unflexibler, sondern auch deutlich fehleranfälliger und abgestürzte Module können nicht ohne weiteres neu gestartet werden.

- **Mikrokernel:**

Der Mikrokernel hat meist deutlich weniger Funktionen als ein monolithischer Kernel, da er nur die wesentlichen Funktionen bereitstellt. Treiber und weitere Funktionen werden über zusätzliche Module hinzugefügt, welche auch als eigenständige Prozesse laufen können und gegenüber dem Kernel sicher abgeschottet sind. Somit kann ein fehlerhafter Treiber nicht das ganze [Betriebssystem](https://github.com/lowlevel-eu/wiki/wiki/Betriebssystem "Betriebssystem") zum Absturz bringen und einfach neu gestartet werden.

- **Makrokernel:**

Der Makrokernel, auch Hybridkernel genannt, ist eine Verschmelzung zwischen einem monolithischem Kernel und Mikrokernel, die jedoch nicht genau definiert ist. Damit will man die Geschwindigkeitsvorteile eines monolithischen Kernels und die Stabilität und Flexibilität eines Mikrokernels kombinieren.

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/2649/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1478/index.html)

<!-- MediaWiki page 1478; revision 2649; parent 2136; 2008-03-22T11:02:15Z -->
