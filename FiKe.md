# FiKe

FiKe ist ein monolithischer Kernel mit integrierter Shell. FiKe steht dabei für First Kernel und meint damit meinem ersten Kernel.

| FiKe |  |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------- |
|  |  |
| Entwickler: | Be59 |
| Akt. Version: | Build 1 |
| [Lizenz](https://github.com/lowlevel-eu/wiki/wiki/Lizenzen "Lizenzen"): | BSD |
| OS-Eigenschaften |  |
| Plattform: | x86 |
| [Kernelart](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel"): | Monolithischer Kernel |
| [Sprache](https://lowlevel-eu.github.io/wiki/pages/1648/index.html "Kategorie:Programmiersprache"): | [C](https://github.com/lowlevel-eu/wiki/wiki/C "C") |
| API: | In Planung |
| Binärformat: | In Planung |
| [IPC-Methode](https://github.com/lowlevel-eu/wiki/wiki/Interprozesskommunikation "IPC"): | Keine, da Monolith |
| Homepage |  |

<https://fike.bountysource.com/>  
Subversion: <https://svn.bountysource.com/fike>

## Aufbau

FiKe kann keine Module laden und besitzt nur einen einzigen Treiber, der des KeyBoardControllers.(KeyBoardController.h) Die Shell ist zwar noch nicht fertig, aber die Grundlagen für einzelne Programme sind weitesgehent vorhanden (GDT.h) Ein Weiterkommen verhindert das Modul CPUID.h. Die Shell wird ihren eigenen Befehle haben.

## Zyklus

**0.0.0.0.1** Vollständige Shell wird intrigiert.

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/3961/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1762/index.html)

<!-- MediaWiki page 1762; revision 3961; parent 3885; 2009-01-24T19:44:16Z -->
