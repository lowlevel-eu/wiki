# Xantorix

**HomixOS** (Homix Operating System) ist ein kostenloses [Betriebssystem](https://github.com/lowlevel-eu/wiki/wiki/Betriebssystem "Betriebssystem"), das vollständig in [Assembler](https://github.com/lowlevel-eu/wiki/wiki/Assembler "Assembler") ([Bootloader](https://github.com/lowlevel-eu/wiki/wiki/Bootloader "Bootloader")) und [Pascal](https://github.com/lowlevel-eu/wiki/wiki/Pascal "Pascal") ([Kernel](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel"), Anwendungen) programmiert wird. Das Betriebssystem ist modular aufgebaut, daher ist es möglich einfach und bequem verschiedene Module oder Treiber zur Laufzeit hinzuzufügen oder zu entfernen. Der Kernel unterstützt alle modernen Technologien wie Protected-Mode, [Multitasking](https://github.com/lowlevel-eu/wiki/wiki/Multitasking "Multitasking") und [Paging](https://github.com/lowlevel-eu/wiki/wiki/Paging "Paging"). Das Betriebssystem steht derzeit noch am Anfang der Entwicklung und ist daher noch nicht für die dauerhafte Verwendung geeignet. Neben der 32-Bit Variante existiert seit neuestem auch eine noch nicht ausführlich getestete 64-Bit Version.

In unregelmäßigen Zeitabständen, meistens jedoch ungefähr alle 2 bis 3 Wochen, wird neben dem finalen Release auch eine Alpha-/Beta-/RC-Variante der sich derzeit in Entwicklung befindlichen Version veröffentlicht. Hierbei handelt es sich um keine stabile Version, sondern nur um den derzeitigen Entwicklungsstand. Den Verlauf und Fortschritt der Entwicklung und die Roadmap kann man auf der offiziellen Webseite betrachten. Dort findet man auch Screenshots aktueller Versionen.

## Features

Einen Überblick über die bereits integrierten, der sich in Entwicklung befindlichen oder erst geplanten Features finden sie auf der [offiziellen Webseite](http://www.homix-online.de/homixos/features.php).

## Versionen

Überblick der verschiedenen Versionen:

    26.12.2007 : HomixOS 0.1.1
    09.09.2007 : HomixOS 0.1.0

Die Veränderungen bei den verschiedenen Versionen:

**HomixOS 0.1.1:**

- Bugfixes
- kleine Benutzerverwaltung
- verbesserte Prozessverwaltung
- Exception-Handling
- erweiterte Shell
- Konsole verbessert

**HomixOS 0.1.0:**

- Multiboot-kompatibler Kernel
- 32-Bit ProtectedMode Kernel
- 64-Bit LongMode Kernel
- Multitasking (Prozesse und Threads)
- moderne Speicherverwaltung (Paging)
- Diskettenlaufwerkstreiber
- FAT-Dateisystemtreiber
- Tastaturtreiber
- PE-Unterstützung

## Roadmap

Folgende Versionen sind geplant:

    Anfang 2008 : HomixOS 0.1.2
    2. Quartal 2008 : HomixOS 0.2.0

Die geplanten Neuheiten in den zukünftigen Versionen:

**HomixOS 0.1.2:**

- SMP / Multiprocessor-Support
- Optimierter Binary-Loader
- vollständige Benutzerverwaltung
- Festplattentreiber (P-ATA)
- Texteditor

**HomixOS 0.2.0:**

- Viele Kernelverbesserungen
- 100%-ige Stabilität
- Netzwerkunterstützung
- ARP, IPv4, UDP, TCP, DNS Netzwerkprotokolle
- RTL8139 Netzwerkkartentreiber
- AMD PCnet Netzwerkkartentreiber

## Offizielle Webseite

[HomixOS Projekt-Webseite](http://www.homix-online.de/homixos/)  
[Homix-Online](http://www.homix-online.de/)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/2708/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1453/index.html)

<!-- MediaWiki page 1453; revision 2708; parent 2500; 2008-03-22T16:48:09Z -->
