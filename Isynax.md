# Isynax

| Isynax |  |
| ----------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
|  |  |
| Entwickler: | [XanClic](https://lowlevel-eu.github.io/wiki/pages/1860/index.html "Benutzer:XanClic") |
| Akt. Version: | \- |
| [Lizenz](https://github.com/lowlevel-eu/wiki/wiki/Lizenzen "Lizenzen"): | MIT |
| OS-Eigenschaften |  |
| Plattform: | [i386](https://github.com/lowlevel-eu/wiki/wiki/X86 "X86") |
| [Kernelart](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel"): | Monolith |
| [Sprache](https://lowlevel-eu.github.io/wiki/pages/1648/index.html "Kategorie:Programmiersprache"): | [Assembler](https://github.com/lowlevel-eu/wiki/wiki/Assembler "Assembler") (FASM) |
| API: | \- |
| Binärformat: | \- |
| [IPC-Methode](https://github.com/lowlevel-eu/wiki/wiki/Interprozesskommunikation "IPC"): | \- |
| Homepage |  |

[Gitorious](http://gitorious.org/isynax)

  
Isynax soll ein möglichst kleines Betriebssystem sein, dessen einzige Aufgabe die Benutzung des IRC ist.

Es gibt keine Prozesse, der gesamte Code läuft im Kernelmodus. Das Betriebssystem läuft im ProtectedMode.

## Features

Bis jetzt gibt es eine Unterstützung für die [RTL8139](https://github.com/lowlevel-eu/wiki/wiki/RTL8139 "RTL8139")-Netzwerkkarte, [ARP](https://github.com/lowlevel-eu/wiki/wiki/Address-Resolution-Protocol "ARP"), [IP](https://github.com/lowlevel-eu/wiki/wiki/Internet-Protocol "IP") und Minimalunterstützung für TCP. Mit Isynax kann man derzeit nur eine Verbindung zu einem IRC-Server außerhalb des lokalen Netzwerks herstellen.

Die eigene IP, die IP des Gateways im lokalen Netzwerks, die IP des Servers, der Zielport und der Nickname sind bis jetzt noch feste Konstanten im Code.

## Screenshot

[<img src="https://raw.githubusercontent.com/wiki/lowlevel-eu/wiki/assets/6ec97dbbcb1faeabf08c.png" width="720" height="400" alt="Isynax-screen.png" />](https://raw.githubusercontent.com/wiki/lowlevel-eu/wiki/assets/6ec97dbbcb1faeabf08c.png)  
**Für alle Intelliebhaber im normalen Modus...**  
  
[<img src="https://raw.githubusercontent.com/wiki/lowlevel-eu/wiki/assets/e792a94b4a8342e9c4d1.png" width="720" height="400" alt="Isynax-shot-falschrum.png" />](https://raw.githubusercontent.com/wiki/lowlevel-eu/wiki/assets/e792a94b4a8342e9c4d1.png)  
**...Und für AT&T-Fans auch andersrum! Aktivierbar per wrong=1 anstatt von wrong=0 im Code.**

## Weblinks

- Der Code bei [Gitorious](http://gitorious.org/isynax)
- Ein relativ aktuelles Image unter [\[1\]](http://www.xanclic.bplaced.net/isynax.img.bz2), Falschrumversion unter [\[2\]](http://www.xanclic.bplaced.net/asynax.img.bz2)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/5865/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2066/index.html)

<!-- MediaWiki page 2066; revision 5865; parent 5864; 2009-09-08T17:44:52Z -->
