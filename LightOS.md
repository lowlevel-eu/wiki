# LightOS

lightOS ist ein weiteres Betriebssystem, welches auf einem Mikrokernel basiert. Die Entwicklung der 32-Bit Version wurde im Dezember 2006 gestoppt, da wir uns nun auf 64-Bit Plattformen konzentrieren möchten, die wir für zukunftssicherer halten.

# Überblick

## Entwickler

- [bluecode](https://lowlevel-eu.github.io/wiki/pages/1489/index.html "Benutzer:Bluecode") (Projektleiter)
- [FreakyPenguin](https://lowlevel-eu.github.io/wiki/pages/1460/index.html "Benutzer:FreakyPenguin")
- \_seeker\_ (aka Damian)

## Features

In der 64-Bit Version sind wir noch im Anfangsstadium. Im Moment sind die folgenden Features implementiert:

- Longmode-Switch
- Speicherverwaltung
- [SMP](https://github.com/lowlevel-eu/wiki/wiki/Symmetrisches-Multiprozessorsystem "SMP")-Initialisierung (noch nicht vollständig)

## Ziele

Das Hauptziel ist es einen möglichst performanten Mikrokernel mit Unterstützung für [SMP](https://github.com/lowlevel-eu/wiki/wiki/Symmetrisches-Multiprozessorsystem "SMP")- und evtl. auch [NUMA](https://github.com/lowlevel-eu/wiki/wiki/Non-Uniform-Memory-Architecture "NUMA")-Systemen zu entwickeln. Außerdem soll die [IPC](https://github.com/lowlevel-eu/wiki/wiki/Interprozesskommunikation "IPC") so gestaltet werden, dass Prozesse, welche auf verschiedenen Computer laufen, ohne zusätzlichen Aufwand miteinander kommunizieren können.

# Links

- [lightOS Trac-Projektseite](http://62.141.55.81/trac/trac.cgi)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/1955/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1454/index.html)

<!-- MediaWiki page 1454; revision 1955; parent 1954; 2007-04-25T11:53:13Z -->
