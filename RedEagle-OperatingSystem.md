# RedEagle-OperatingSystem

| RedEagle-OperatingSystem (Projektname) |  |
| ----------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|  |  |
| Entwickler: | [Benutzer:RedEagle](https://lowlevel-eu.github.io/wiki/pages/1491/index.html "Benutzer:RedEagle") |
| Akt. Version: | Betriebssystem: 1.00<br>Kernel: 0.10.0 |
| [Lizenz](Lizenzen "Lizenzen"): | [CC by-nc-sa 2.0](http://creativecommons.org/licenses/by-nc-sa/2.0/de/) (GPL geplant) |
| OS-Eigenschaften |  |
| Plattform: | [i586](X86 "X86") |
| [Kernelart](Kernel "Kernel"): | Monolithisch |
| [Sprache](Kategorie-Programmiersprache "Kategorie:Programmiersprache"): | [C](C "C"), [C++](C%2B%2B "C++"), [Assembler](Assembler "Assembler") |
| API: | Nativ |
| Binärformat: | Kernel: [ELF](Executable-and-Linking-Format "ELF"); Apps: [ELF](Executable-and-Linking-Format "ELF") |
| [IPC-Methode](Interprozesskommunikation "IPC"): | [pipes](Pipe "Pipe") |
| Homepage |  |

[Projektseite](http://www.redeagle-operatingsystem.de.vu/)  
[YouTube-Channel](http://www.youtube.com/1000Tode)

RedEagle-OperatingSystem ist ein 32Bit OS dessen Hauptziel darin besteht einfach und unkompliziert auf lowlevel-ebene Programmieren zu können. Das System dient quasi nur als Unterstützung für den Programmierer und soll ihn nicht bevormunden.

Ziel ist es **nicht** ein sicheres und stabiles System zu schreiben. Diese Punkte werden frühstens in der Nächsten Generation berücksichtigt :)

  
**Hinweis:** Das Projekt ist laut der [Projektwebsite](http://www.redeagle-operatingsystem.de.vu/) eingestellt worden.

## Namensänderung

Das gesamte Betriebssystem wird seit der Kernel-Version 0.10 Adversys genannt.  
Das Projekt heißt weiterhin RedEagle-OperatingSystem, und der Kernel weiterhin reos

## Bestandteile des Betriebssystems

Adversys besteht (bisher) aus den folgenden Komponenten

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
- Ausführen von [ELF](Executable-and-Linking-Format "ELF")-Dateien
- alle Programme laufen in ring0
- [GDB](GDB "GDB") interface

### Pipes

**Status:** Bereits vereinzelt erfolgreich im Einsatz, aber noch nicht 100% ausgereift.

Jedes Programm, jeder Thread hat 4.294.967.294 Ports. Diese Ports können unter den folgenden Bedingungen miteinander verknüpft werden:

- Es können nur 2 Ports verknüpft werden
- Einer muss lesend sein, der andere schreibend

Werden 2 Ports verknüpft die noch nicht geöffnet wurden (wo also unklar ist, welcher lesender und welcher schreibender Natur ist) wird der 1. als schreibend, der 2. lesend geöffnet. \<c\> PID pid = CreateProcess(...); // Prozess erstellen

open(2, true); //Port 2 zum schreiben öffnen link(MyPID(), 2, pid, 1); //Port 2 mit Port 1 des neuen Prozesses verbinden \</c\>

### Programme

**Status:** Funktionsfähig, aber mangels Bibliotheken/Shell im Einsatz nicht allzu mächtig.

Programme liegen im [ELF](Executable-and-Linking-Format "ELF")-format vor. Die API ist über *int 0xFF* anwendbar.  
Programme können in C und Assembly geschrieben sein. Für C-Programme gib es eine entsprechende API-Bibliothek.  
Bislang gibt es abgesehen von der API keine weiteren Bibliotheken.

Alle Programme laufen in ring0, ihnen stehen also alle Befehle der CPU zur Verfügung und können beliebig auf Hardware zugreifen. So können Programme per *cli* auch den Taskswitch unterdrücken oder ggf die gesamte Kontrolle übernehmen. (REOS könnte also auch als Bootmanager verwendet werden)  
Da es sich um ein single-user-system handelt gibt es auch keine Einschränkung im Zugriff aus Dateien (währe bei ring0-programmen auch kein wirkliches Hindernis).

Greift ein Programm schreibend auf eine schreibgeschützte Datei zu, so fragt der Kernel den User, ob dieses Programm das trotz verbot darf oder nicht. - Ein Schreibschutz ist kein Verbot, sondern vielmehr die Aufforderung sich beim User zu melden bevor etwas verändert wird.  
*(bislang noch nicht implementiert)*

## sonstige Nennenswerte Besonderheiten

Ich lege viel Wert darauf, wirklich alles selber zu schreiben. Ich möchte nicht nur ein Kernel schreiben sondern ein Betriebssystem :)  
Ich werde wohl bei einigen Tools wie einem Assembler ausnahmen machen, aber die Basis soll von Grund auf neu sein.  

**!! Nicht alle Ideen und Umsetzungen sind gut oder sinnvoll !!**

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

Ein weiteres tool namens *ldelf* lädt eine [ELF](Executable-and-Linking-Format "ELF")-Datei (den Kernel) in den Speicher. Diese kann dann mit einem weiteren Tool ausgeführt werden.

  
Für die Entwicklung im Realmode wurden folgende Programme eingesetzt:

- bcc - ein C-Compiler der Code für den [Real Mode](Real-Mode "Real Mode") erzeugt
- ld86 - Der Entsprechende Linker um eine [Real Mode](Real-Mode "Real Mode") - Anwendung zu erzeugen
- nasm - Ein universeller Assembler für alles :)

*bcc* und *ld86* werden vom Paketmanager (opensuse & Fedora) im Paket *dev86* bereit gestellt.

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

### Speichermanager

Ist jetzt nicht direkt eine Besonderheit des Kernels, aber ich will dennoch mal beschreiben wie ich ihn realisiert habe.

Es gibt drei Listen die in dem Speichermanager genutzt werden.

1.  Eine Liste, die freie Listenelemente enthält
2.  Eine Liste, die reservierten Speicher beschreibt
3.  und eine Liste, die freien Speicher beschreibt.

Da innerhalb des Speichermanagers nur ganze Pages reserviert werden könne um neue Listenelemente anzulegen wird direkt eine ganze reihe an Elementen gleichzeitig reserviert. Nämlich soviel, wie in einer Page platz finden. Diese Elemente werden zu einer Liste freier Elemente "verbunden".  
Wird freier Speicher angefordert wird in der Liste, die den freien Speicher beschreibt nach einem ausreichend großen Speicherbereich gesucht. Wird keiner gefunden werden entsprechend viele Pages vom Pagemanager angefordert. Der benötigte Speicher wird vom freien Speicher angezogen und durch ein neues Listenelement beschrieben welches in die Liste des Reservierten Speichers aufgenommen wird.  
Wird Speicher freigegeben wird das entsprechende Listenelement aus der Liste des reservierten Speicher in die liste des freien Speichers gegeben. Es wird geprüft ob dieser Speicherbereich an anderen freien Speicher angrenzt und verschmolzen werden kann. Falls ja, wird das überflüssige Listenelement wieder in die Liste der freien Elemente aufgenommen.

### Pagemanager

Ein Pagemanager an sich ist ebenfalls nichts besonderes in einem x86-Kernel, aber naja… auch da hat jeder seine eigenen Vorstellungen wie man so etwas angeht :)

Beim Initialisieren werden die ersten 3 4MiB-Pages reserviert und an 0x00000000, 0x00400000, 0x00800000 gemapped. Für die ersten 12MiB ist die Vvrtuelle Adresse also gleich der Physikalischen.

Werden später Pages angefordert wird zunächst geprüft ob es mehr als 1024 Pages sind. Falls ja wird der Speicher in 4MiB-Pages reserviert. Wird also 5MiB angefordert werden 8MiB reserviert.  
Werden weniger als 1024 Pages angefordert werden entsprechend viele Pages reserviert und eine Pagetable gesucht, die genügend freie Plätze für den Speicher hat. Sind nicht ausreichend viele Plätze frei wird eine neue Pagetable angelegt.

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

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/11050/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2232/index.html)

<!-- MediaWiki page 2232; revision 11050; parent 10358; 2013-03-19T15:00:23Z -->
