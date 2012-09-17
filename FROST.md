# FROST

| FROST |  |
| ----------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|  |  |
| Entwickler: | darkinsanity aka TheThing |
| Akt. Version: | V2 alpha |
| [Lizenz](https://github.com/lowlevel-eu/wiki/wiki/Lizenzen "Lizenzen"): | GNU GPL 3 |
| OS-Eigenschaften |  |
| Plattform: | [i386](https://github.com/lowlevel-eu/wiki/wiki/X86 "X86") |
| [Kernelart](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel"): | Microkernel |
| [Sprache](https://lowlevel-eu.github.io/wiki/pages/1648/index.html "Kategorie:Programmiersprache"): | [FreeBASIC](https://github.com/lowlevel-eu/wiki/wiki/FreeBASIC "FreeBASIC") und [Assembler](https://github.com/lowlevel-eu/wiki/wiki/Assembler "Assembler") |
| API: |  |
| Binärformat: | ELF |
| [IPC-Methode](https://github.com/lowlevel-eu/wiki/wiki/Interprozesskommunikation "IPC"): |  |
| Homepage |  |

[Sourceforge-Seite](http://sourceforge.net/projects/frostkernel)

  
FROST ist ein OS, dass auf dem gleichnamigen Microkernel beruht und zum Ziel hat, ein kleines und benutzbares System in FreeBASIC zu schreiben.

## FROST V2 0.1 (codename: river dragon)

Dinge, die bereits funktionieren:

- Multitasking (nur teilweise, wird momentan umgestellt)
- Paging (nur halb)

Features, die noch auf ihre Umsetzung warten:

- VFS
- Shell (dasuSH - dumb although somehow useful shell)
- tcp/ip
- Treiber für RTL8139
- ext2 und FAT support

## Der Kernel

FROST ist ein 32-Bit Microkernel, der in FreeBASIC und Assembler geschrieben ist. Der Kernel wurde vor kurzem neu begonnen und unterstützt Multitasking und Paging, wobei diese beiden Systeme noch einiges an Änderungen erfahren (werden). Der Kernel ist kompatibel zum Multiboot-Standard und wird momentan von GRUB 2 geladen. Die letzte Version des alten Kernels (V0.3.4a) kann noch über sourceforge heruntergeladen werden, allerdings wird empfohlen die neue Version zu beziehen, die im git-Repository liegt.

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/10857/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1754/index.html)

<!-- MediaWiki page 1754; revision 10857; parent 9799; 2012-09-17T18:47:13Z -->
