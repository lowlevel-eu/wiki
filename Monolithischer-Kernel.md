# Monolithischer Kernel

Als monolithischen Kernel bezeichnet man eine Art von Betriebssystemkernel, wo die Treiber in den Kernel mitgelinkt sind und nicht als seperate Module vorliegen, die erst noch vom Kernel geladen werden müssten (vergleiche hierzu [Microkernel](https://github.com/lowlevel-eu/wiki/wiki/Kernel#mikrokernel "Microkernel")).

Der Vorteil eines monolithischen Kernels ist die erhöhte Performance, da z.B. ein Nachladen der Treiber von einem Speichermedium wegfällt. Der entscheidene Nachteil ist, dass wenn ein Treiber Probleme macht, dies den ganzen Kernel mit in die Miesere zieht.

Windows und Linux sind bekannte Monolithen, obwohl diese eher in die Kategorie [Makrokernel](https://github.com/lowlevel-eu/wiki/wiki/Kernel#makrokernel "Makrokernel") fallen, da hier zur Laufzeit Module eingebunden werden können.

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/5790/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1825/index.html)

<!-- MediaWiki page 1825; revision 5790; parent 4887; 2009-08-31T06:16:16Z -->
