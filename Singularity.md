# Singularity

| Singularity |  |
| ----------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
|  |  |
| Entwickler: | Microsoft Research |
| Akt. Version: | 2.0 |
| [Lizenz](Lizenzen "Lizenzen"): | Microsoft Research Lizenz |
| OS-Eigenschaften |  |
| Plattform: | [i386](X86 "X86"), [x86_64](X86-64 "X64"), |
| [Kernelart](Kernel "Kernel"): | [Microkernel](Kernel#mikrokernel "Microkernel") |
| [Sprache](https://lowlevel-eu.github.io/wiki/pages/1648/index.html "Kategorie:Programmiersprache"): | Sing# (Spec#-Derivat → C#-Dialekt) |
| API: | [POSIX](POSIX "POSIX") |
| Binärformat: | [PE](Microsoft-Portable-Executable-and-Common-Object-File-Format "PE") |
| [IPC-Methode](Interprozesskommunikation "IPC"): | spezielles Shared Memory/Message Passing |
| Homepage |  |

<http://research.microsoft.com/os/singularity/>

**Singularity** ist ein Betriebssystem von Microsoft Research, das fast ausschließlich in C# bzw. einem eigens entwickelten C#-Dialekt namens Sing# bzw. Spec# geschrieben ist. Durch die Verwendung dieser auf .NET basierenden Sprachen ist es möglich, präemptives Multitasking und Speicherschutz in einem einzigen Adressraum zu verwirklichen, da parallel laufenden Programmen einfach keine Pointer auf Objekte besitzen, die ihnen nicht gehören. Microsoft Research möchte durch den Zwang, alle Anwendungen in dieser Sprache zu schreiben ein Sicherheitsplus erreichen, welches nicht nur für den Kernel, sondern auch für die Applikationen gilt, da diese aufgrund der Sprache in der sie entstanden sind gar nicht abstürzen können. Außerdem behauptet Microsoft, einen enormen Performancegewinn gegenüber [Windows XP](Windows "Windows") und [Linux](Linux "Linux") zu erreichen.

Der Quellcode ist frei verfügbar und veränderbar, jedoch verbietet die Lizenz kommerzielle Nutzung, wodurch Singularity nicht komplett freie Software ist.

## Links

- [Microsoft Research – Singularity Homepage](http://research.microsoft.com/os/singularity/)
- [Singularity Quellcode](http://www.codeplex.com/singularity)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/6637/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1492/index.html)

<!-- MediaWiki page 1492; revision 6637; parent 6246; 2009-12-28T01:11:07Z -->
