# FROST

| FROST |  |
| ----------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|  |  |
| Entwickler: | TheThing aka Thrimbor |
| Akt. Version: | V2 alpha |
| [Lizenz](Lizenzen.md "Lizenzen"): | GNU GPL 3 |
| OS-Eigenschaften |  |
| Plattform: | [i486](X86.md "X86") oder höher |
| [Kernelart](Kernel.md "Kernel"): | Microkernel |
| [Sprache](Kategorie-Programmiersprache.md "Kategorie:Programmiersprache"): | [FreeBASIC](FreeBASIC.md "FreeBASIC") und [Assembler](Assembler.md "Assembler") |
| API: | nativ |
| Binärformat: | ELF |
| [IPC-Methode](Interprozesskommunikation.md "IPC"): |  |
| Homepage |  |

[github-Seite](https://github.com/thrimbor/frost)

  
FROST ist ein OS welches dem gleichnamigen Microkernel aufbaut und zum Ziel hat ein kleines, leicht verständliches und dennoch modernes System in FreeBASIC zu schreiben.

## FROST V2 0.1 (codename: river dragon)

Erledigt:

- Multitasking
- Paging
- Speicherverwaltung

Begonnen:

- VFS
- IPC
- SMP und APIC-Support

## Der Kernel

FROST ist ein 32-Bit Microkernel, der in FreeBASIC und Assembler geschrieben ist. Der Kernel wurde vor einiger Zeit neu begonnen, ist kompatibel zum Multiboot-Standard und wird momentan von GRUB 2 geladen. Die letzte Version des alten Kernels (V0.3.4a) kann noch über [sourceforge](http://sourceforge.net/projects/frostkernel/files/deprecated/FROST_V0.3.4a.zip/download) heruntergeladen werden, allerdings wird empfohlen die neue Version zu beziehen, die auf github zu finden ist.

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/11145/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1754/index.html)

<!-- MediaWiki page 1754; revision 11145; parent 11144; 2013-09-26T10:55:33Z -->
