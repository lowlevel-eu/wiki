# NerdyKernel

| NerdyKernel |  |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
|  |  |
| Entwickler: | rizor |
| Akt. Version: | 2012-01 Build 1 |
| [Lizenz](Lizenzen "Lizenzen"): | GPLv3 |
| OS-Eigenschaften |  |
| Plattform: | [i386](X86 "X86") |
| [Kernelart](Kernel "Kernel"): | Microkernel |
| [Sprache](https://lowlevel-eu.github.io/wiki/pages/1648/index.html "Kategorie:Programmiersprache"): | [C](C "C") & [Assembler](Assembler "Assembler") |
| API: | Noch nicht näher geplant |
| Binärformat: |  |
| [IPC-Methode](Interprozesskommunikation "IPC"): | Message-Passing, Message-Queues, RPC |
| Homepage |  |

<http://rizor.dyndns-home.com/git/?p=NerdyKernel.git;a=summary> <http://rizor.dyndns-home.com/git/?p=NerdyTestbot.git;a=summary>

  

## Buildsystem

Der Kernel und der Testbot werden durch CMake definiert. Es soll beides unter UNIX und Cygwin gebaut werden können. Für den Kernel selber wird es u.U. auch die Möglichkeit geben ihn mit dem MSVC zu bauen.

## Testverfahren

Für das Projekt wird derzeit ein Testbot entworfen, der verschiedene Builds durchführen kann und diese in Logdateien speichert. Damit auch die Funktionalitäten getestet werden können, wird es ein eigens entwickeltes Testframework geben, dass durch den Testbot in regelmäßigen Abständen gestartet wird. Dieses Framework soll auch die Möglichkeit zu Performance-Messungen geben, damit Bottle-Necks frühzeitig erkannt werden können.

Des weiteren wird es ein Debugging-Modul geben, das über die serielle Schnittstelle konfiguriert werden kann und dort auch Informationen ausgeben kann. Das Modul soll die Auslastung des Kernels anzeigen und die Performance genauer analysieren können.

Als letztes soll es später noch einen Fuzzer geben, der über eine generische Abbildungsvorschrift den Kernel und seine Module testet und verifiziert. Dabei kommt ein Mutation-Based-Fuzzer zum Einsatz, der Schwachstellen aufzeigen soll.

## Design

Der Kernel selbst ist modular aufgebaut und verschiedene Teile des Kernels sind voneinander getrennt. Ziel dieses Designs ist eine effektive ASLR (AddressSpace Layout Randomization), die sowohl im Kernel als auch Userspace arbeiten soll. Durch dieses Verfahren sollen Angriffe auf das System erschwert werden.

Derzeit wird geplant, wie man zur Laufzeit Updates von Modulen verwenden kann, ohne das System zu deaktivieren. Dadurch sollen die Down-Times des Systems minimiert werden. Das ist natürlich nur möglich, wenn sich die API und die internen Datenstrukturen nicht ändern.

## Fortschritt

Momentan befindet sich der Kernel weitestgehend in der Planungsphase, da die Kernel-Konfiguration und das Test-Framework entwickelt werden. Nachdem das abgeschlossen ist, wir der Kernel in die Entwicklunsphase treten.

## Entwicklungsstand

Testbot:

- Konfigurationsframework
  - Eigener Konfigurationsstandard, der auf einfaches Parsing ausgelegt ist
- Loggingframework
  - Automatische Organisation der Logs und Erstellung mehrere Log-Instanzen
- Framework für verschiedene Bots
  - Build-Bot implementierung (Eigenständige Build-Generierung mit Zusammenfassung des Builds)
  - Unit-Test-Bot (Eigenständige Builds und Ausführung der Tests)

Kernel:

- Einfache System-Bibliothek, die eine Teilmenge des C-Standards implementiert

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/10506/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1816/index.html)

<!-- MediaWiki page 1816; revision 10506; parent 10503; 2012-03-14T18:43:50Z -->
