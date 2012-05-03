# LF OS

| LF OS (LittleFox' Operating System oder Light & Fast Operating System) |  |
| ----------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|  |  |
| Entwickler: | LittleFox |
| Akt. Version: | 1.0 Alpha 1 / Kernel4 |
| [Lizenz](https://github.com/lowlevel-eu/wiki/wiki/Lizenzen "Lizenzen"): | GPLv3+ |
| OS-Eigenschaften |  |
| Plattform: | [x86](https://github.com/lowlevel-eu/wiki/wiki/X86 "X86"), später [x86-64](https://github.com/lowlevel-eu/wiki/wiki/X86-64 "X86-64") |
| [Kernelart](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel"): | Microkernel |
| [Sprache](https://lowlevel-eu.github.io/wiki/pages/1648/index.html "Kategorie:Programmiersprache"): | [C](https://github.com/lowlevel-eu/wiki/wiki/C "C"), [C++](https://github.com/lowlevel-eu/wiki/wiki/C%2B%2B "C++"), [Assembler](https://github.com/lowlevel-eu/wiki/wiki/Assembler "Assembler") |
| API: | Nativ, evt. POSIX, und die API's anderer Hobby-OSe (damit ich weniger portieren muss :P) |
| Binärformat: | [ELF](https://github.com/lowlevel-eu/wiki/wiki/Executable-and-Linking-Format "ELF") |
| [IPC-Methode](https://github.com/lowlevel-eu/wiki/wiki/Interprozesskommunikation "IPC"): | \- |
| Homepage |  |

<http://lf-os.googlecode.com>

  
LF OS ist ein weiteres Hobbybetriebssystem das in C/C++ und Assembler programmiert wird.

Da ich momentan wiedereinmal von vorne angefangen habe (einige haben das im Forum sicherlich schon mitbekommen) ist die Featureliste momentan ziemlich kurz. Die folgenden Features sind bereits implementiert:

- Physische Speicherverwaltung
- GDT/IDT
- plattformunabhängige Verwaltung der Interrupts (werden vom Plattformstarter auf Kernel-Events gemappt)
- endlich mal ein grobes Design in menschenlesbarer Textform ;)

------------------------------------------------------------------------

hier gibt es bald noch mehr updates ...

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/10593/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2267/index.html)

<!-- MediaWiki page 2267; revision 10593; parent 10212; 2012-05-03T04:43:45Z -->
