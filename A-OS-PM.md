# A / OS PM

A / OS PM ist ein Betriebsystem, das von Blitzmaster entwickelt wird. Zurzeit befindet es sich noch in einem nicht testbaren Stadium, weshalb ich mir hier noch nicht festlegen möchte, wann es getestet werden kann.

## Geplante Feautures

### Übsersicht

- Protected Mode
- Flat Memory Model
- Paging
- Umfangreiches Treibersystem
- Multi User
- Multi Tasking
- Microkernel
- Notkonsole
- GUI komplett vom System getrennt
- Eigenes File System (A / FS)
- Support von FAT 16/32

### Protected Mode / Flat Memory Model / Paging

Das Betriebsystem wird den Protected Mode in seinem vollen Umfang unterstützen. Angewandt wird das Flat Memory Model, das heißt es gibt nur wenige Deskriptoren für den Gesamten Hauptspeicher. Die Unterteilung wird mit Paging realisiert. Jedes Programm hat zur Laufzeit 3GB Speicher zur Verfügung.

### Multi Tasking

Es werden mehrere Programme gleichzeitig ausgeführt werden können, um genau zu sein laut jetzigem Stand 65335. Das ganze wird reines Software-Multitasking, und ist somit für die Zukunft (Long Mode) gerüstet.

### Notkonsole

Sie wird per Ctrl + Alt + Del aufgerufen und dient dazu, das System während der Laufzeit zu reparieren. Sollte z.B. der Kernel oder bestimmte Programme abstürzen, können sie hier beendet werden. Während sie aktiv ist, läuft nur sie, das heißt sie hat einen eigenen Treiber, und auch Signale von der Hardware werden vollkommen ignoriert. Sie wird auch Möglichkeiten zur Sicherung des Hauptspeichers bieten, auch einzelne Teile werden gesichert werden können.

### GUI

Die GUI wird komplett vom Rest des Systems getrennt sein, die Kommunikation mit den Programmen verläuft über s.g. Terminals. Sie werden vom Kernel verwaltet. Die GUI bietet zusätzlich noch ein paar Call Gates, die jedoch beim Start über API Funktionen registriert werden müssen.

## Derzeitiger Stand

Zurzeit sind folgende Feautures integriert:

- Protected Mode / Paging / Flat Memory Model - 40%
- Umfangreiches Treibersystem - 10%
- Multi User - 0%
- Multi Tasking - 0%
- Microkernel - 100% (der Kernel ist zurzeit zu 30% fertig)
- Notkonsole - 30% (sie existiert bereits, jedoch nur wenige Befehle)
- GUI - 10% (eine provisorische Text - Konsole)

## Road Map

Hier eine Vorsichtig gestaltete Road Map, die sich jedoch sicherlich noch änder wird, hoffentlich zum guten ^^

1\. Halbjahr 2007: 1. Alpha Release (Build 1000) mit der integration von allem ein bisschen ;)

2\. Halbjahr 2007: 2. Alpha Release (Build 1500) mit der erweiterten Integration von allem

1\. Halbjahr 2008: 1. Beta Release (Build 2000) mit der Integration von allem ausser GUI

2\. Halbjahr 2008: 2. Beta Release (Build 2500) mit der ent-buggten Integration von allem ausser GUI

1\. Halbjahr 2009: 1. Release Candidat (Build 3000)

2\. Halbjahr 2009: Final Release

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/1631/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1451/index.html)

<!-- MediaWiki page 1451; revision 1631; parent 1630; 2007-01-13T20:25:57Z -->
