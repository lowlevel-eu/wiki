# LightOS

lightOS ist ein weiteres Betriebssystem für x86 und x86-64. Es basiert auf einem Microkernel.

# Entwickler

- [bluecode](https://lowlevel-eu.github.io/wiki/pages/1489/index.html "Benutzer:Bluecode")

# Features

Im Moment sind die folgenden Features implementiert:

- Microkernel
- x86 und x86-64
- Multitasking/-threading
- [IPC](https://github.com/lowlevel-eu/wiki/wiki/Interprozesskommunikation "IPC"): Messages, Shared-Memory
- [SMP](https://github.com/lowlevel-eu/wiki/wiki/Symmetrisches-Multiprozessorsystem "SMP")-kompatibles System wird erkannt und alle Prozessoren gestartet
- kleine Shell

# Ziele

Das Hauptziel ist es einen möglichst performanten Mikrokernel mit Unterstützung für [SMP](https://github.com/lowlevel-eu/wiki/wiki/Symmetrisches-Multiprozessorsystem "SMP")- und evtl. auch [NUMA](https://github.com/lowlevel-eu/wiki/wiki/Non-Uniform-Memory-Architecture "NUMA")-Systemen zu entwickeln. Außerdem soll die [IPC](https://github.com/lowlevel-eu/wiki/wiki/Interprozesskommunikation "IPC") so gestaltet werden, dass Prozesse, welche auf verschiedenen Computer laufen, ohne zusätzlichen Aufwand miteinander kommunizieren können.

# Links

- [lightOS Projektseite](https://lightos.bountysource.com/)
- [lightOS Subversion Repository](https://lightos.bountysource.com/svn)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/2038/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1454/index.html)

<!-- MediaWiki page 1454; revision 2038; parent 1955; 2007-06-28T09:43:39Z -->
