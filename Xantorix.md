# Xantorix

**HomixOS** (Homix Operating System) ist ein kostenloses [Betriebssystem](https://github.com/lowlevel-eu/wiki/wiki/Betriebssystem "Betriebssystem"), das vollständig mit Assembler (Bootloader) und Pascal ([Kernel](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel"), Programme) programmiert wird. Das Betriebssystem ist modular aufgebaut, was bedeutet, dass man einfach und bequem verschiedene Module oder Treiber hinzufügen oder entfernen kann. Der Kernel unterstützt außerdem 32-Bit Protected-Mode, [Multitasking](https://github.com/lowlevel-eu/wiki/wiki/Multitasking "Multitasking") und [Paging](https://github.com/lowlevel-eu/wiki/wiki/Paging "Paging").

Das Betriebssystem ist derzeit noch in Entwicklung und befindet sich in der Alpha-Phase. Es ist im Laufe des Jahres geplant, den Alpha-Status abzuschließen und eine 64-Bit Version für HomixOS zu veröffentlichen. Den Verlauf und Fortschritt der Entwicklung und die Roadmap kann man auf der offiziellen Webseite betrachten. Dort findet man auch Screenshots aktueller Versionen.

HomixOS wird als Install-Disk, mit der HomixOS auf einem PC installiert werden kann, und als Live-Disk, mit der HomixOS problemlos direkt von Diskette gestartet werden kann, zur Verfügung gestellt. Die Alpha- und Beta-Versionen stehen nur als Live-Disk zur Verfügung. Bei speziellen Bochs-Paketen wird ein Emulator inkl. Konfiguration mitgeliefert. Dadurch kann das Betriebssystem einfach per Doppelklick auf die Start-BAT-Datei mit dem Emulator getestet werden, ohne [Windows](https://github.com/lowlevel-eu/wiki/wiki/Windows "Windows") beenden zu müssen.

## Features

Einen Überblick über die bereits integrierten, der sich in Entwicklung befindlichen oder erst geplanten Features finden sie auf der [offiziellen Webseite](http://www.homix-online.de/HomixOS/Features.php).

## Versionen

Überblick der verschiedenen Versionen:

    05.01.2007 : HomixOS 0.0.6 Alpha
    28.09.2006 : HomixOS 0.0.5 Alpha

Die Veränderungen bei den derzeitigen Versionen:

**HomixOS 0.0.6 Alpha:**

- FAT-Dateisystemtreiber integriert
- Erweiterte Shell (u.a. mit Dateibefehlen)
- Textmodus und Grafikmodus
- Ändern der Bildschirmauflösung
- Herunterfahren und Neustarten von HomixOS möglich

**HomixOS 0.0.5 Alpha:**

- Kleine Shell
- Lauffähiger 32-Bit Kernel
- Textmodus

## Roadmap

Folgende Versionen sind geplant:

    30.01.2007 : HomixOS 0.0.7 Alpha
    24.02.2007 : HomixOS 0.0.8 Alpha
    14.04.2007 : HomixOS 0.1.0 Beta

Die geplanten Neuheiten in den zukünftigen Versionen:

**HomixOS 0.0.7 Alpha:**

- Multitasking und Multithreading integriert
- Kernel komplett Multitasking-fähig
- Neues verbessertes Nachrichtensystem
- Erweiterte GUI (Bugfixes, mehr Controls, ...)

**HomixOS 0.0.8 Alpha:**

- Festplattentreiber (ATA)
- CD-ROM/DVD-ROM Laufwerkstreiber (ATAPI)
- VGA-Grafiktreiber
- VFAT Unterstützung
- ISO9660 Dateisystemtreiber
- UDF Dateisystemtreiber

**HomixOS 0.1.0 Beta:**

- Kernel-Protection
- Stabilitätssicherungen
- Multiprozessor (SMP) Unterstützung
- Netzwerk/Internet Unterstützung
- Netzwerkprotokolle: ARP,IPv4,UDP,TCP/IP
- RTL8139 Netzwerkkartentreiber

## Offizielle Webseite

[HomixOS Projekt-Webseite](http://www.homix-online.de/HomixOS/)  
[Homix-Online](http://www.homix-online.de/)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/1767/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1453/index.html)

<!-- MediaWiki page 1453; revision 1767; parent 1766; 2007-01-20T23:30:40Z -->
