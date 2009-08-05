# Singularity

| Singularity |  |
| ----------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
|  |  |
| Entwickler: | Microsoft Research |
| Akt. Version: | 2.0 |
| [Lizenz](https://github.com/lowlevel-eu/wiki/wiki/Lizenzen "Lizenzen"): | Microsoft Research Lizenz (OpenSource) |
| OS-Eigenschaften |  |
| Plattform: | i386, x86_64, |
| [Kernelart](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel"): | [Microkernel](https://github.com/lowlevel-eu/wiki/wiki/Kernel#mikrokernel "Microkernel") |
| [Sprache](https://lowlevel-eu.github.io/wiki/pages/1648/index.html "Kategorie:Programmiersprache"): | Sing# (C#-Dialekt) |
| API: | [POSIX](https://github.com/lowlevel-eu/wiki/wiki/POSIX "POSIX") |
| Binärformat: | PE |
| [IPC-Methode](https://github.com/lowlevel-eu/wiki/wiki/Interprozesskommunikation "IPC"): | spezielles Shared Memory/Message Passing |
| Homepage |  |

<http://research.microsoft.com/os/singularity/>

  
**Singularity** ist ein Betriebssystem von Microsoft Research, das fast ausschließlich in C# bzw. einem eigens entwickelten C# Dialekt namens Sing# bzw. Spec# geschrieben. Durch die Verwendung dieser auf .NET basierenden Sprachen ist es möglich, preemptives Multitasking und Speicherschutz in einem einzigen Adressraum zu verwirklichen, da parallel laufenden Programmen einfach keine Pointer auf Objekte besitzen, die ihnen nicht gehören. Microsoft Research möchte durch den Zwang, alle Anwendungen in dieser Sprache zu schreiben ein Sicherheitsplus erreichen, welches nicht nur für den Kernel, sondern auch für die Applikationen gilt, da diese aufgrund der Sprache in der sie entstanden sind gar nicht abstürzen können. Außerdem behauptet Microsoft, einen enormen Performancegewinn gegenüber [Windows XP](https://github.com/lowlevel-eu/wiki/wiki/Windows "Windows") und [Linux](https://github.com/lowlevel-eu/wiki/wiki/Linux "Linux") zu erreichen. Der Quellcode ist frei verfügbar und veränderbar, verbietet jedoch die kommerziele Nutzung.

## Links

- [Microsoft Research: Singularity Homepage](http://research.microsoft.com/os/singularity/)
- [Singularity Quellcode](http://www.codeplex.com/singularity)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/5073/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1492/index.html)

<!-- MediaWiki page 1492; revision 5073; parent 4916; 2009-08-05T16:24:33Z -->
