# FruityOrange

| FruityOrange |  |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| Datei:FruityOrangeLogo.png |  |
| Entwickler: | [Micha](https://lowlevel-eu.github.io/wiki/pages/2560/index.html "Benutzer:Micha.linuxfreak") |
| Akt. Version: | 0.04 |
| [Lizenz](https://github.com/lowlevel-eu/wiki/wiki/Lizenzen "Lizenzen"): | [GNU General Public License](https://github.com/lowlevel-eu/wiki/wiki/Lizenzen#gnu-general-public-license "Lizenz") |
| OS-Eigenschaften |  |
| Plattform: | [i386](https://github.com/lowlevel-eu/wiki/wiki/X86 "X86") |
| [Kernelart](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel"): | [Monolithisch](https://github.com/lowlevel-eu/wiki/wiki/Kernel#monolithischer-kernel "Kernel") |
| [Sprache](https://lowlevel-eu.github.io/wiki/pages/1648/index.html "Kategorie:Programmiersprache"): | [C](https://github.com/lowlevel-eu/wiki/wiki/C "C") ([Assembler](https://github.com/lowlevel-eu/wiki/wiki/Assembler "Assembler")) |
| API: | nativ |
| Binärformat: | [ELF](https://github.com/lowlevel-eu/wiki/wiki/Executable-and-Linking-Format "ELF") |
| [IPC-Methode](https://github.com/lowlevel-eu/wiki/wiki/Interprozesskommunikation "IPC"): | --- |
| Homepage |  |

<https://github.com/micha-/FruityOrange>  
<https://code.google.com/p/fruityorange/>

FruityOrange ist ein Betriebssystem für den [i386](https://github.com/lowlevel-eu/wiki/wiki/X86 "X86"), welches [GRUB](https://github.com/lowlevel-eu/wiki/wiki/Grand-Unified-Bootloader "GRUB") als Bootloader benutzt.  
  

## Features

- printf, panic, debug
- [GDT](https://github.com/lowlevel-eu/wiki/wiki/Global-Descriptor-Table "GDT"), [Interrupts](https://github.com/lowlevel-eu/wiki/wiki/Interrupt "Interrupt")
- [Physische Speicherverwaltung](https://github.com/lowlevel-eu/wiki/wiki/Physische-Speicherverwaltung "Physische Speicherverwaltung"), [Paging](https://github.com/lowlevel-eu/wiki/wiki/Paging "Paging"), [Heap](https://github.com/lowlevel-eu/wiki/wiki/Heapverwaltung "Heap")
- [Multitasking](https://github.com/lowlevel-eu/wiki/wiki/Multitasking "Multitasking"), Elf32-loader

### Treiber

- [CGA Grafik](https://github.com/lowlevel-eu/wiki/wiki/Textausgabe "Textausgabe") ;)
- [Tastatur (KBC)](https://github.com/lowlevel-eu/wiki/wiki/Keyboard-Controller "Keyboard Controller")
- [PIT](https://github.com/lowlevel-eu/wiki/wiki/Programmable-Interval-Timer "PIT")
- [CMOS / RTC](https://github.com/lowlevel-eu/wiki/wiki/CMOS "CMOS")

## Syscalls

| Nummer (in %eax) | Name | Beschreibung | ebx | ecx | edx |
| ------------------ | -------- | --------------------------------------------------- | ------------------------------------------------------------------ | ------------------------------------------------------------ | ----- |
| 0 | exit | Beendet das aktuelle programm | exit-status |  |  |
| 1 | putc | Gibt ein Zeichen auf dem Bildschirm aus | zeichen |  |  |
| 2 | puts | Gibt ein String auf dem Bildschirm aus | pointer zum string | länge des Strings |  |
| 3 | getch | Wartet auf einen Tastendruck | hier wird der ASCII-code des gedrückten Zeichens reingeschrieben |  |  |
| 4 | gets | Liest einen String über die Tastatur ein. | pointer zum string (muss vorher abgespeichert werden) | länge des eingegebenen Strings (wird hier reingeschrieben) |  |
| 5 | usleep | Legt das programm für %ebx microsekunden schlafen | anzahl der microsekunden, die zu warten sind |  |  |

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/11036/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2594/index.html)

<!-- MediaWiki page 2594; revision 11036; parent 11006; 2013-03-17T17:27:00Z -->
