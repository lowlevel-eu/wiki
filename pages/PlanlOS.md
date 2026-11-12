# PlanlOS

| planlOS |  |
| ----------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
|  |  |
| Entwickler: | Phoenix |
| Akt. Version: | \- |
| [Lizenz](Lizenzen.md "Lizenzen"): | MIT |
| OS-Eigenschaften |  |
| Plattform: | [x86](X86.md "X86") |
| [Kernelart](Kernel.md "Kernel"): | Monolithisch |
| [Sprache](Kategorie-Programmiersprache.md "Kategorie:Programmiersprache"): | [Assembler](Assembler.md "Assembler"), [C](C.md "C") |
| API: | Unix |
| Binärformat: | ELF |
| [IPC-Methode](Interprozesskommunikation.md "IPC"): | Signals |
| Homepage |  |

[\[1\]](http://repo.or.cz/w/planlOS.git) (git)

  
planlOS ist mein erster größerer Versuch, mal etwas lauffähiges zu produzieren. Dabei beschränke ich mich auf ein recht "traditionelles" Setup (monolithisch, Unix-API).

# Build-Environment

- CMake 2.6
- Dependencies:
  - mtools
  - grub legacy
  - GCC/GAS/LD (mit Unterstützung für ELF)
  - mkisofs

# Features

- Partielle (noch recht rudimentäre) Unix-API
- Partieller TCP-Support durch lwip (Lightweight IP stack)
- SMP-Support (buggy)
- Virtuelle Terminals (Strg+F1 - Strg+F8)
- Kernelmodule als ELF-Shared-Objects
- Kleine Testsuite für die Unix-API ([\[2\]](http://repo.or.cz/w/incOS.git?a=shortlog;h=refs/heads/testsuite), funktioniert auch unter meinos)
- Treiber:
  - CDI:
    - ATA
    - Floppy
    - rtl8139
    - iso9660
    - ramdisk
  - CDROM
  - CD-Speaker (noch ohne Interface)

# Known Bugs

- SMP: Shell hängt nach sehr kurzer Zeit
- Netzwerkstack stürzt regelmäßig ab

# Roadmap

0.0.1:

- Bessere Shell
- Stabilerer Netzwerksupport
- Booten von Floppy

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/3729/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1788/index.html)

<!-- MediaWiki page 1788; revision 3729; parent 0; 2008-12-25T12:03:01Z -->
