# Monolithischer Kernel

Als monolithischen Kernel bezeichnet man eine Art von Betriebssystemkernel, bei welcher die Treiber in den Kernel mitgelinkt werden und nicht als seperate Module vorliegen, die erst noch vom Kernel geladen werden müssten (vergleiche hierzu [Mikrokernel](https://github.com/lowlevel-eu/wiki/wiki/Kernel#mikrokernel "Mikrokernel")).

Der Vorteil eines monolithischen Kernels liegt in der erhöhten Performance, da z. B. ein Nachladen der Treiber von einem Speichermedium unnötig ist. Zudem muss die Kommunikation zwischen den Treibern nicht allzu abstrakt gestaltet werden, was ebenfalls zu einer Erhöhung der Geschwindigkeit führt. Der entscheidene Nachteil ist, dass wenn ein Treiber Probleme macht, dies den ganzen Kernel zum Absturz bringen kann.

Windows und Linux sind bekannte Monolithen, obwohl diese eher in die Kategorie [Makrokernel](https://github.com/lowlevel-eu/wiki/wiki/Kernel#makrokernel "Makrokernel") fallen, da hier zur Laufzeit Module eingebunden werden können.

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/5802/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1825/index.html)

<!-- MediaWiki page 1825; revision 5802; parent 5790; 2009-08-31T14:09:19Z -->
