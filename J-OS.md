# J-OS

| J-OS |  |
| ----------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
|  |  |
| Entwickler: | [Jonebohne](https://lowlevel-eu.github.io/wiki/pages/2138/index.html "Benutzer:Jonebohne") |
| Akt. Version: | Pre-Alpha 0.0.1 |
| [Lizenz](https://github.com/lowlevel-eu/wiki/wiki/Lizenzen "Lizenzen"): | [by-nc-sa 2.0](http://creativecommons.org/licenses/by-nc-sa/2.0/de/) |
| OS-Eigenschaften |  |
| Plattform: | [x86](https://github.com/lowlevel-eu/wiki/wiki/X86 "X86") |
| [Kernelart](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel"): | [Microkernel](https://github.com/lowlevel-eu/wiki/wiki/Kernel#mikrokernel "Microkernel") |
| [Sprache](https://lowlevel-eu.github.io/wiki/pages/1648/index.html "Kategorie:Programmiersprache"): | [C](https://github.com/lowlevel-eu/wiki/wiki/C "C") |
| API: | Nativ(geplant) |
| Binärformat: | Portable Executable |
| [IPC-Methode](https://github.com/lowlevel-eu/wiki/wiki/Interprozesskommunikation "IPC"): | [RPC](https://github.com/lowlevel-eu/wiki/wiki/Interprozesskommunikation#rpc-remote-procedure-call "RPC")(geplant) |
| Homepage |  |

\[noch keine\]

J-OS ist ein (sehr) kleines [Betriebssystem](https://github.com/lowlevel-eu/wiki/wiki/Betriebssystem "Betriebssystem") von mir, welches ich hier etwas genauer beschreibe.

J-OS ist fast komplett in [C](https://github.com/lowlevel-eu/wiki/wiki/C "C") geschrieben(teilweise [Assembler](https://github.com/lowlevel-eu/wiki/wiki/Assembler "Assembler")) und bootet mit dem [GRUB](https://github.com/lowlevel-eu/wiki/wiki/Grand-Unified-Bootloader "GRUB")-Loader. Es läuft vollständig im [Protected Mode](https://github.com/lowlevel-eu/wiki/wiki/Protected-Mode "Protected Mode"). Geplant ist ein [Microkernel](https://github.com/lowlevel-eu/wiki/wiki/Kernel#mikrokernel "Microkernel"), eine native API, [Treiber](https://github.com/lowlevel-eu/wiki/wiki/Treiber "Treiber") für Festplatten/Disketten/CD-Laufwerke, externe Programme, Netzwerktreiber, eine [Shell](https://github.com/lowlevel-eu/wiki/wiki/Shell "Shell") und vieles mehr. Es kann also fast nichts ;-)

  

## Changelog

#### Version 0.0.1

In Version 0.0.1 sind folgende Features implementiert:

- Textausgabe (verschiedene Farben)
- GDT und IDT
- Exceptions werden behandelt
- Multitasking in Ring 0

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/7048/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1828/index.html)

<!-- MediaWiki page 1828; revision 7048; parent 7038; 2010-02-09T14:40:39Z -->
