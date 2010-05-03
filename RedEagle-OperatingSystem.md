# RedEagle-OperatingSystem

| RedEagle-OperatingSystem |  |
| ----------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
|  |  |
| Entwickler: | [Benutzer:RedEagle](https://lowlevel-eu.github.io/wiki/pages/1491/index.html "Benutzer:RedEagle") |
| Akt. Version: | 0.8.0 |
| [Lizenz](https://github.com/lowlevel-eu/wiki/wiki/Lizenzen "Lizenzen"): | [CC by-nc-sa 2.0](http://creativecommons.org/licenses/by-nc-sa/2.0/de/) (GPL geplant) |
| OS-Eigenschaften |  |
| Plattform: | [i586](https://github.com/lowlevel-eu/wiki/wiki/X86 "X86") |
| [Kernelart](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel"): | Monolithisch |
| [Sprache](https://lowlevel-eu.github.io/wiki/pages/1648/index.html "Kategorie:Programmiersprache"): | [C](https://github.com/lowlevel-eu/wiki/wiki/C "C"), [C++](https://github.com/lowlevel-eu/wiki/wiki/C%2B%2B "C++"), ASM |
| API: | Nativ |
| Binärformat: | Kernel: raw; Apps: [ELF](https://github.com/lowlevel-eu/wiki/wiki/Executable-and-Linking-Format "ELF") |
| [IPC-Methode](https://github.com/lowlevel-eu/wiki/wiki/Interprozesskommunikation "IPC"): | [Pipe](https://github.com/lowlevel-eu/wiki/wiki/Pipe "Pipe") |
| Homepage |  |

[www.redeagle-operatingsystem.de.vu](http://www.redeagle-operatingsystem.de.vu/)

RedEagle-OperatingSystem ist ein 32Bit OS dessen Hauptziel darin besteht einfach und unkompliziert auf lowlevel-ebene Programmieren zu können. Das System dient quasi nur als Unterstützung für den Programmierer und soll ihn nicht bevormunden.

Ziel ist es **nicht** ein sicheres und stabiles System zu schreiben. Diese Punkte werden frühstens in der Nächsten Generation berücksichtigt :)

## Allgemeine Features

- Arbeitet im PM
- Paging
- Multitasking
- Singeluser-system
- Pipes
- alle Programme laufen in ring0

## Nennenswerte Besonderheiten

Ich lege viel wert darauf wirklich alles selber zu schreiben. Ich möchte nicht nur ein Kernel schreiben sondern ein Betriebssystem :)  
Ich werde wohl bei einigen Tools wie einem Assembler ausnahmen machen, aber die Basis soll von Grund auf neu sein.  

### Der Bootloader

Bei dem Bootloader *reosboot* liegt der Fokus darauf den Kernel zu unterstützen und **niemals** im Weg zu stehen. Der bootloader ist quasi der Knecht der dem Kernel den weg bereitet.

Zu den besonderen Features von reosboot gehören die Folgenden Punkte

- Bietet eine kleine API
- Stellt eine Verbindung zu einem entfernten PC per RS232 her
- Ist scripting-fähig
- Führt verschiedene kleine Tools aus (boot-app's)
- Arbeitet mit dem FT3fs-Dateisystem (mehr dazu weiter unten)
- 3 Wege das A20-Gate zu enablen

Zu den Tools gehört unter anderem ein ramdisk-manager der folgende Features bietet:

- laden einer Diskette in den RAM
- eine ramdisk auf Diskette schreiben
- Eine ramdisk per RS232 herunterladen und in den RAM schreiben

### Das FT3fs - Dateisystem

Das Dateisystem basiert auf einem Graph der in einer Datei gespeichert ist.  
Das Dateisystem ist also in Dateien gespeichert.

Die 1. Datei die geladen wird ist der Bootsektor (lässt sich nicht vermeiden :D)  
In dem Bootsektor ist neben einem äußerst minimalistischem FT3fs-Treiber ein Graph der die Dateien (Nodes) des eigentlichen Dateisystem enthält.  
Das Dateisystem ist in die folgenden Nodes zerlegt:

- bootsector.bin: Der Bootsektor.
- reosboot.bin: Der Bootloader. (Optional, anderer Nodename möglich)
- secmap.dat: Enthält eine bytemap in der beschrieben ist, welche Sektoren belegt sind, und welche frei sind.
- nodes.dat: Hier liegt der Graph, der den Rest des Dateisystem's beschreibt.

Die Verteilung der Dateien auf dem Datenträger wird durch eine Liste von Sektor-nummern in der Datei-spezifischen Datenstruktur der Nodes beschrieben.  
Da das Dateisystem speziell auf mein Betriebssystem zugeschnitten ist werden keine unix-permissions unterstützt.

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/7649/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2232/index.html)

<!-- MediaWiki page 2232; revision 7649; parent 7647; 2010-05-03T14:54:12Z -->
