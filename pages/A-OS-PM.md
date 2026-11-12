# A / OS PM

**Löschhinweis:**

Dieser Artikel wurde zum Löschen vorgeschlagen.

Keine Website, letzter Edit des Autors von Mitte 2008, wird scheinbar nicht mehr weiterentwickelt --[DerHartmut](https://lowlevel-eu.github.io/wiki/pages/1865/index.html "Benutzer:Hartmut") 11:40, 30. Aug. 2011 (CEST)

A / OS PM ist ein [Betriebssystem](Betriebssystem "Betriebssystem"), das von Blitzmaster entwickelt wird. Zurzeit befindet es sich noch in einem nicht testbaren Stadium, weshalb ich mich hier noch nicht festlegen möchte, wann es getestet werden kann. Es gab einen Vorgänger (A / OS RM) der im RealMode lief und nur zu testzwecken diente.

| A / OS PM |  |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------- |
|  |  |
| Entwickler: | Blitzmaster |
| Akt. Version: | 0.0.1 (Pre Alpha I) |
| [Lizenz](Lizenzen "Lizenzen"): | (Vorerst) Proprietär |
| OS-Eigenschaften |  |
| Plattform: | [x86](X86 "X86") |
| [Kernelart](Kernel "Kernel"): | Microkernel |
| [Sprache](Kategorie-Programmiersprache "Kategorie:Programmiersprache"): | Assembly, C/C++ |
| API: | A / API |
| Binärformat: | ELF |
| [IPC-Methode](Interprozesskommunikation "IPC"): | Message passing, pipes, shared memory |
| Homepage |  |

## Geplante Features

### Übersicht

- [Protected Mode](Protected-Mode "Protected Mode")
- Flat Memory Model
- [Paging](Paging "Paging")
- Umfangreiches Treibersystem
- Multiuser
- [Multitasking](Multitasking "Multitasking")
- [Microkernel](Kernel "Kernel")
- Notkonsole
- [GUI](Graphical-User-Interface "GUI") komplett vom System getrennt
- Eigenes [Dateisystem](Dateisystem "Dateisystem") (A / FS)
- Support von FAT 16/32

### Protected Mode / Flat Memory Model / Paging

Das Betriebssystem wird den Protected Mode in seinem vollen Umfang unterstützen. Angewandt wird das Flat Memory Model, das heißt, es gibt nur wenige Deskriptoren für den gesamten Hauptspeicher. Die Unterteilung wird mit Paging realisiert. Jedes Programm hat zur Laufzeit 3 GB Speicher zur Verfügung.

### Multitasking

Es werden mehrere Programme gleichzeitig ausgeführt werden können. Das ganze wird reines Software-Multitasking, und ist somit für die Zukunft (Long Mode) gerüstet. In späteren Versionen soll auch ein Prioritätenmodell zur Verfügung stehen.

### Notkonsole

Sie wird per Ctrl + Alt + Del aufgerufen und dient dazu, das System während der Laufzeit zu reparieren. Sollte z.B. der Kernel oder bestimmte Programme abstürzen, können sie hier beendet werden. Während sie aktiv ist, läuft nur sie, das heißt sie hat einen eigenen Treiber, und auch Signale von der Hardware werden vollkommen ignoriert. Sie wird auch Möglichkeiten zur Sicherung des Hauptspeichers bieten, auch einzelne Teile werden gesichert werden können.

### GUI

Die GUI wird komplett vom Rest des Systems getrennt sein, die Kommunikation mit den Programmen verläuft über sogenannte Terminals. Sie werden vom Kernel verwaltet. Die GUI bietet zusätzlich noch ein paar Call Gates, die jedoch beim Start über API Funktionen registriert werden müssen.

## Version 0.0.2 (1. Alpha Release)

Hier einmal die geplanten Features für diese Version von A / OS PM:

- Multitasking: jedoch ohne Prioritäten
- Treibersystem
- A / IO (die [IPC](Interprozesskommunikation "IPC") Schnittstelle)
- Text - Console
- Keyboard - Treiber
- Grafik - Treiber: Textmodus

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/10101/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1451/index.html)

<!-- MediaWiki page 1451; revision 10101; parent 5271; 2011-08-30T09:40:39Z -->
