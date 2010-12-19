# RedEagle-OperatingSystem

| RedEagle-OperatingSystem |  |
| ----------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|  |  |
| Entwickler: | [Benutzer:RedEagle](https://lowlevel-eu.github.io/wiki/pages/1491/index.html "Benutzer:RedEagle") |
| Akt. Version: | 0.9.9 |
| [Lizenz](https://github.com/lowlevel-eu/wiki/wiki/Lizenzen "Lizenzen"): | [CC by-nc-sa 2.0](http://creativecommons.org/licenses/by-nc-sa/2.0/de/) (GPL geplant) |
| OS-Eigenschaften |  |
| Plattform: | [i586](https://github.com/lowlevel-eu/wiki/wiki/X86 "X86") |
| [Kernelart](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel"): | Monolithisch |
| [Sprache](https://lowlevel-eu.github.io/wiki/pages/1648/index.html "Kategorie:Programmiersprache"): | [C](https://github.com/lowlevel-eu/wiki/wiki/C "C"), [C++](https://github.com/lowlevel-eu/wiki/wiki/C%2B%2B "C++"), [Assembler](https://github.com/lowlevel-eu/wiki/wiki/Assembler "Assembler") |
| API: | Nativ |
| Binärformat: | Kernel: [ELF](https://github.com/lowlevel-eu/wiki/wiki/Executable-and-Linking-Format "ELF"); Apps: [ELF](https://github.com/lowlevel-eu/wiki/wiki/Executable-and-Linking-Format "ELF") |
| [IPC-Methode](https://github.com/lowlevel-eu/wiki/wiki/Interprozesskommunikation "IPC"): | [pipes](https://github.com/lowlevel-eu/wiki/wiki/Pipe "Pipe") |
| Homepage |  |

[www.redeagle-operatingsystem.de.vu](http://www.redeagle-operatingsystem.de.vu/)

RedEagle-OperatingSystem ist ein 32Bit OS dessen Hauptziel darin besteht einfach und unkompliziert auf lowlevel-ebene Programmieren zu können. Das System dient quasi nur als Unterstützung für den Programmierer und soll ihn nicht bevormunden.

Ziel ist es **nicht** ein sicheres und stabiles System zu schreiben. Diese Punkte werden frühstens in der Nächsten Generation berücksichtigt :)

## Bestandteile des Betriebssystems

Das RedEagle-OperatingSystem besteht (bisher) aus den folgenden Komponenten

- **reosboot**: Der Bootloader des Systems
- **reos**: Der Kernel des Systems
- **FT3fs**: Für das Betriebssystem entwickeltes Dateisystem
- **Bifröst**: Schnittstelle zur Außenwelt per rs232

## Allgemeine Features

- Monolithisch
- Arbeitet im PM
- Paging
- Multitasking
- Singeluser-system
- Pipes
- alle Programme laufen in ring0
- [GDB](https://github.com/lowlevel-eu/wiki/wiki/GDB "GDB") interface

### GUI

**Status:** Noch in einem sehr frühen Entwicklungsstadium

Das GUI läuft im textmode. Mithilfe von ASCII-Zeichen werden Fenster gezeichnet welche wie üblich verschoben, in ihrer Größe verändert, oder maximiert werden können.  
Das GUI wird vollständig über die Tastatur bedient.

JEDES Fenster besitzt 3 GUI-Elemente:

- Eine Menüleiste
- Eine F-Tasten-Leiste (im Prinzip auch eine 2. Menüleiste)
- Ein Textfeld

Dabei soll das Textfeld verschiedene Modi bereitstellen:

- Command-Mode: Verhält sich wie eine Konsole
- Text-Mode: Verhält sich wie ein übliches edit-control
- Interactiv-Mode: Verhält sich etwa wie ein billiger webbrowser

### Pipes

**Status:** Bereits vereinzelt erfolgreich im Einsatz, aber noch nicht 100% ausgereift.

Jedes Programm, jeder Thread hat 4.294.967.294 Ports. Diese Ports können unter den folgenden Bedingungen miteinander verknüpft werden:

- Es können nur 2 Ports verknüpft werden
- Einer muss lesend sein, der andere schreibend

Werden 2 Ports verknüpft die noch nicht geöffnet wurden (wo also unklar ist, welcher lesender und welcher schreibender Natur ist) wird der 1. als schreibend, der 2. lesend geöffnet. \<c\> PID pid = CreateProcess(...); // Prozess erstellen

open(2, true); //Port 2 zum schreiben öffnen link(MyPID(), 2, pid, 1); //Port 2 mit Port 1 des neuen Prozesses verbinden \</c\>

### Programme

**Status:** Funktionsfähig, aber mangels Bibliotheken/Shell im Einsatz nicht allzu mächtig.

Programme liegen im [ELF](https://github.com/lowlevel-eu/wiki/wiki/Executable-and-Linking-Format "ELF")-format vor. Die API ist über *int 0xFF* anwendbar.  
Programme können in C und Assembly geschrieben sein. Für C-Programme gib es eine entsprechende API-Bibliothek.  
Bislang gibt es abgesehen von der API keine weiteren Bibliotheken.

Alle Programme laufen in ring0, ihnen stehen also alle Befehle der CPU zur Verfügung und können beliebig auf Hardware zugreifen. So können Programme per *cli* auch den Taskswitch unterdrücken oder ggf die gesamte Kontrolle übernehmen. (REOS könnte also auch als Bootmanager verwendet werden)  
Da es sich um ein single-user-system handelt gibt es auch keine Einschränkung im Zugriff aus Dateien (währe bei ring0-programmen auch kein wirkliches Hindernis).

Greift ein Programm schreibend auf eine schreibgeschützte Datei zu, so fragt der Kernel den User, ob dieses Programm das trotz verbot darf oder nicht. - Ein Schreibschutz ist kein Verbot, sondern vielmehr die Aufforderung sich beim User zu melden bevor etwas verändert wird.  
*(bislang noch nicht implementiert)*

## sonstige Nennenswerte Besonderheiten

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

Ein weiteres tool namens *xelf* lädt eine [ELF](https://github.com/lowlevel-eu/wiki/wiki/Executable-and-Linking-Format "ELF")-Datei und führt diesem im PM aus. (Derzeit in der Entwicklung)

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

### Bifröst

Bifröst bezeichnet einen Server und ein Übertragungsprotokoll dessen Aufgabe es ist, den Kernel zu unterstützen, bzw vom kernel stammende Informationen auszuwerten.  
Der bootloader und später der kernel verbinden sich per rs232 mit dem auf einem Linux-rechner laufenden Server.

Der Server bietet derzeit folgende Features:

- Up/Download von Dateien
- Sektor-weiser lese/schreibzugriff auf image-files
- empfangen & Anzeigen von log-informationen

#### kernel-logs

Der Kernel schickt beständig Informationen über die rs232. Dafür verwendet er 3 verschiedene Übertragungsprotokolle:

1.  Bifröst
2.  raw ascii
3.  ansi

Durch ein ping wird ermittelt ob der Bifröst-Server erreichbar ist (s.o.) - ist dies nicht der Fall werden die logs ASCII-Codiert übertragen. Das hat den Vorteil dass auf einer virtuellen Maschiene die log-daten einfach in ein Textfile geschrieben werden können um sie später auszuwerten.  
Im ANSI-Modus werden die Daten mit ANSI-Escape-Sequenzen coloriert. Somit kann man auch ohne Bifröst-Server die Daten mit einem 2. PC in Echtzeit farbig beobachten.

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/9074/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2232/index.html)

<!-- MediaWiki page 2232; revision 9074; parent 7798; 2010-12-19T12:59:55Z -->
