# Minix

| Minix |  |
| ----------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
|  |  |
| Entwickler: | Andrew S. Tanenbaum und weitere |
| Akt. Version: | 3.2 |
| [Lizenz](Lizenzen "Lizenzen"): | 2-Klausel-BSD |
| OS-Eigenschaften |  |
| Plattform: | [i386](X86 "X86"), Motorola 68000, Sun SPARC |
| [Kernelart](Kernel "Kernel"): | Microkernel |
| [Sprache](https://lowlevel-eu.github.io/wiki/pages/1648/index.html "Kategorie:Programmiersprache"): | [C](C "C") |
| API: | [POSIX](POSIX "POSIX") ab Version 3 |
| Binärformat: | [ELF](Executable-and-Linking-Format "ELF") |
| [IPC-Methode](Interprozesskommunikation "IPC"): | Message Passing |
| Homepage |  |

<http://www.minix3.org>

**Minix** ist ein im Jahre 1987 von Andrew S. Tanenbaum zu Lehrzwecken entwickeltes Betriebssystem, welches einem Unix-System nachempfunden ist. Mittlerweile ist es in Version 3 erschienen und wurde modernisiert. Ab Version 3.2 hat [SMP](Symmetrisches-Multiprozessorsystem "SMP")-Support (vorerst als experimentell bezeichnet) in den Kernel Einzug gehalten.

  

## Minix als Lehrsystem

Ursprünglich wurde Minix als Lehrsystem konzipiert. Die erste Version umfasste 12.500 Zeilen und sollte Studenten in die Geheimnisse des x86-Prozessors einführen. Der Code von Minix wird auch in Tanenbaums eigenem Buch „Operating Systems: Design and Implementation“ benutzt, um anhand des Codes die Funktionsweise eines Betriebssystems zu erklären.

  

## Minix für Entwickler

Für engagierte Entwickler ist Minix unter Umständen auch eine interessante Plattform. Das Projekt bietet nämlich jährlich Patenschaften im Rahmen des Google Summer Of Code an, bei dem man als Student einen Sommer lang an einem bestimmten Bereich arbeiten kann, und dabei von Google bezahlt wird. Natürlich sollte man am Ende auch gute Ergebnisse vorweisen können, daher ist ein solches Projekt nur für sehr erfahrene Entwickler geeignet.

  

## „Linux is obsolete“

Minix ist bekanntlich älteren Datums als Linux (Minix 0.1.0: 1987, Linux 0.01: 1991). Linus Torvalds wollte mit Linux eigentlich einen Terminal-Emulator schreiben, fand aber immer mehr Gefallen daran, die Hardware seines x86 zu erforschen und so wurde aus einem Terminal-Emulator ein Betriebssystem, welches in Konkurrenz zu Minix stand. In einem bis dato beispiellosen Flamewar, angefangen von Andrew S. Tanenbaum persönlich, wurde jeweils gegen das andere System und mögliche Stärken/Schwächen gewettert.

Ausgangspunkt waren hierbei die herbe Kritik an dem noch jungen Projekt Linux.

Kritikpunkte waren hier der monolithische Kernel, der in Tanenbaums Augen unzeitgemäß wäre, die „Versteifung“ auf die x86-Plattform durch Inline-Assembler, das liberale Entwicklungssystem sowie „unnötige“ Features, wie das parallele Zugreifen auf das Dateisystem von mehreren Programmen aus.

Dies war Ausgangspunkt für einen Flamewar ganz besonderer Art, der die Entwicklung beider Systeme angefacht hat.

## Links

- [Artikel zu Minix bei Wikipedia](http://de.wikipedia.org/wiki/Minix_%28Betriebssystem%29)
- [minix3.org](http://minix3.org)
- [Flamewar im Usenet](http://www.educ.umu.se/~bjorn/mhonarc-files/obsolete/)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/10482/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1910/index.html)

<!-- MediaWiki page 1910; revision 10482; parent 9646; 2012-03-01T10:16:14Z -->
