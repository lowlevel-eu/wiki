# LightOS

lightOS ist ein weiteres Betriebssystem, welches auf einem Mikrokernel basiert. Die entwicklung der 32-Bit Version wurde im Dezember 2006 gestoppt, da wir uns nun auf 64-Bit Platformen konzentrieren möchten, da wir das für zukunftssicherer halten.

# Überblick

## Entwickler

- [bluecode](https://lowlevel-eu.github.io/wiki/pages/1489/index.html "Benutzer:Bluecode") (Projektleiter)
- [FreakyPenguin](https://lowlevel-eu.github.io/wiki/pages/1460/index.html "Benutzer:FreakyPenguin")
- \_seeker\_ (aka Damian)

## Features

In der 64-Bit version sind wir noch im Anfangsstaduim. Im Moment sind die folgenden Features implementiert:

- Longmode-Switch
- Speicherverwaltung
- [SMP](https://github.com/lowlevel-eu/wiki/wiki/Symmetrisches-Multiprozessorsystem "SMP")-Initialisierung (noch nicht vollständig)

## Ziele

Das Hauptziel ist es einen möglichst performanten Mikrokernel mit Unterstützung für [SMP](https://github.com/lowlevel-eu/wiki/wiki/Symmetrisches-Multiprozessorsystem "SMP")- und evtl. auch [NUMA](https://github.com/lowlevel-eu/wiki/wiki/Non-Uniform-Memory-Architecture "NUMA")-Systemen zu entwickeln. Außerdem soll die [IPC](https://github.com/lowlevel-eu/wiki/wiki/Interprozesskommunikation "IPC") so gestaltet werden, dass Prozesse, welche auf verschiedenen Computer laufen, ohne zusätzlichen Aufwand miteinander kommunizieren können.

# Links

- [lightOS Trac-Projektseite](http://62.141.55.81/trac/trac.cgi)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/1773/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1454/index.html)

<!-- MediaWiki page 1454; revision 1773; parent 1643; 2007-01-21T23:24:19Z -->
