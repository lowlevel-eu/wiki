# NerdyKernel

| NerdyKernel |  |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
|  |  |
| Entwickler: | rizor |
| Akt. Version: | 2012-01 Build 1 |
| [Lizenz](https://github.com/lowlevel-eu/wiki/wiki/Lizenzen "Lizenzen"): | GPLv3 |
| OS-Eigenschaften |  |
| Plattform: | [i386](https://github.com/lowlevel-eu/wiki/wiki/X86 "X86") |
| [Kernelart](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel"): | Microkernel |
| [Sprache](https://lowlevel-eu.github.io/wiki/pages/1648/index.html "Kategorie:Programmiersprache"): | [C](https://github.com/lowlevel-eu/wiki/wiki/C "C") & [Assembler](https://github.com/lowlevel-eu/wiki/wiki/Assembler "Assembler") |
| API: | Noch nicht näher geplant |
| Binärformat: |  |
| [IPC-Methode](https://github.com/lowlevel-eu/wiki/wiki/Interprozesskommunikation "IPC"): | Message-Passing, Message-Queues, RPC |
| Homepage |  |

<http://rizor.dyndns-home.com/git/?p=NerdyKernel.git;a=summary>

  

## Testverfahren

Das Projekt enthält einen eigens entwickelten Testbot, der den Kompiliervorgang überwacht und verschiedene Testszenarien durchspielt. Einzelne Komponenten des Kernels werden durch Testcases und Emulierung bestimmter Komponenten im Userspace getestet und verifiziert. Dadurch sollen einfache Möglichkeiten geschaffen werden die einzelnen Kernel-Komponenten zu überprüfen. Es eignet sich nicht zum Test von Treibern. Für Treibertests wird ein Debug-Interface definiert, das es ermöglicht die Treiber auf ihre Korrektheit zu prüfen.

## Design

Der Kernel selbst ist modular aufgebaut und verschiedene Teile des Kernels sind voneinander getrennt. Ziel dieses Designs ist eine effektive ASLR (AddressSpace Layout Randomization), die sowohl im Kernel als auch Userspace arbeiten soll. Durch dieses Verfahren sollen Angriffe auf das System erschwert werden.

Derzeit wird geplant, wie man zur Laufzeit Updates von Modulen verwenden kann, ohne das System zu deaktivieren. Dadurch sollen die Down-Times des Systems minimiert werden. Das ist natürlich nur möglich, wenn sich die API und die internen Datenstrukturen nicht ändern.

## Fortschritt

Momentan befindet sich der Kernel weitestgehend in der Planungsphase, da die Kernel-Konfiguration und das Test-Framework entwickelt werden. Nachdem das abgeschlossen ist, wir der Kernel in die Entwicklunsphase treten.

## Features

    * Kernel-Konfigurator
    * Automatisiertes Testframework

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/10493/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1816/index.html)

<!-- MediaWiki page 1816; revision 10493; parent 10492; 2012-03-07T22:51:50Z -->
