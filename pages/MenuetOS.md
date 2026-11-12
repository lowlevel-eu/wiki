# MenuetOS

| MenuetOS |  |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
|  |  |
| Entwickler: | Ville Turjanmaa |
| Akt. Version: | i386: 0.85B<br>x86_64: 0.97Z |
| [Lizenz](Lizenzen.md "Lizenzen"): | [M64 Lizenz](http://www.menuetos.net/m64l.txt) |
| OS-Eigenschaften |  |
| Plattform: | [i386](X86.md "X86"), [x86_64](X86-64.md "X64") |
| [Kernelart](Kernel.md "Kernel"): | Monolithisch |
| [Sprache](Kategorie-Programmiersprache.md "Kategorie:Programmiersprache"): | [Assembler](Assembler.md "Assembler") |
| API: | Nativ |
| Binärformat: | ? |
| [IPC-Methode](Interprozesskommunikation.md "IPC"): | ? |
| Homepage |  |

<http://www.menuetos.net/>

**MenuetOS** ist ein kleines 32/64-Bit [Betriebssystem](Betriebssystem.md "Betriebssystem"), das vollständig mit [FASM](Flat-Assembler.md "FASM") geschrieben. Es passt trotz einiger mitgelieferten Anwendungen immer noch auf eine einzelne Diskette. Durch die Programmierung in Assembler ist das System sehr ressourcenschonend und schnell. MenuetOS basiert nicht auf Unix oder [POSIX](POSIX.md "POSIX"), sondern hat sich das Ziel gesetzt, die Extra-Schichten zwischen den verschiedenen Teilen des Betriebssystems zu beseitigen, um Komplexität und Bugs vorzubeugen. Die 32-Bit Version von MenuetOS wird aufgrund der 64-Bit Version jedoch kaum mehr entwickelt, was zu [KolibriOS](KolibriOS.md "KolibriOS"), das eine Weiterentwicklung des letzten öffentlichen 32-Bitzweiges ist, geführt hat.

## Releases

Die derzeit aktuellen Versionen sind:

- MenuetOS 32 v0.85B
- MenuetOS 64 v0.97Z

## Features

Folgende Liste von Features kann man auf der MenuetOS-Webseite finden:

- [Multitasking](Multitasking.md "Multitasking"), Multithreading, Ring-3-Schutz
- [GUI](Graphical-User-Interface.md "GUI") (Graphical User Interface)
- IDE: Editor/Makro Assembler um Kernel und Anwendungen zu erzeugen
- TCP/[IP](Internet-Protocol.md "IP")-Stack mit Loopback, PPP & [Ethernettreibern](Ethernet.md "Ethernet")
- Netzwerkanwendungen inklusive FTP-/HTTP-/MP3-/SMTP-Server
- IRC-, HTTP-, NNTP-, E-Mail- und TFTP-Clients
- Freigestaltbare Programmfenster
- Echtzeitdatenverarbeitung
- [USB](Universal-Serial-Bus.md "USB")-2.0-Support für High-Speed-Massenspeicher, -Webcams, -Drucker und -TV (mit DVB-T)
- Multiprocessor-Unterstützung
- Passt unkomprimiert auf eine einzelne Diskette

## siehe auch

- [Ausgabe 1](Ausgabe-1.md#os-showcase-menuetos "Ausgabe 1")
- [KolibriOS](KolibriOS.md "KolibriOS")

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/10112/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1481/index.html)

<!-- MediaWiki page 1481; revision 10112; parent 9645; 2011-08-30T12:53:46Z -->
