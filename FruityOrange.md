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

- Higherhalf-Kernel mit GDT Trick
- printf, panic, debug
- [GDT](https://github.com/lowlevel-eu/wiki/wiki/Global-Descriptor-Table "GDT"), [Interrupts](https://github.com/lowlevel-eu/wiki/wiki/Interrupt "Interrupt")
- [Physische Speicherverwaltung](https://github.com/lowlevel-eu/wiki/wiki/Physische-Speicherverwaltung "Physische Speicherverwaltung"), [Paging](https://github.com/lowlevel-eu/wiki/wiki/Paging "Paging"), [Heap](https://github.com/lowlevel-eu/wiki/wiki/Heapverwaltung "Heap")
- [Multitasking](https://github.com/lowlevel-eu/wiki/wiki/Multitasking "Multitasking"), Elf32-loader
- [VFS](https://github.com/lowlevel-eu/wiki/wiki/Virtuelles-Dateisystem "VFS")

### Treiber

- [CGA Grafik](https://github.com/lowlevel-eu/wiki/wiki/Textausgabe "Textausgabe") ;)
- [Tastatur (KBC)](https://github.com/lowlevel-eu/wiki/wiki/Keyboard-Controller "Keyboard Controller")
- [PIT](https://github.com/lowlevel-eu/wiki/wiki/Programmable-Interval-Timer "PIT")
- [CMOS / RTC](https://github.com/lowlevel-eu/wiki/wiki/CMOS "CMOS")

## Syscalls

Die Syscalls werden über den Interrupt 0x30 aufgerufen.

| Nummer (in %eax) | Name | Beschreibung | ebx | ecx | edx |
| ------------------ | -------- | ----------------------------------------------------- | ------------------------------------------------------------------ | ------------------------------------------------------------ | ------------------ |
| 0 | exit | Beendet das aktuelle programm | exit-Status |  |  |
| 1 | putc | Gibt ein Zeichen auf dem Bildschirm aus | Zeichen |  |  |
| 2 | puts | Gibt einen String auf dem Bildschirm aus | Pointer zum String | Länge des Strings |  |
| 3 | getch | Wartet auf einen Tastendruck | Hier wird der ASCII-Code des gedrückten Zeichens reingeschrieben |  |  |
| 4 | gets | Liest einen String über die Tastatur ein. | Pointer zum String (muss vorher abgespeichert werden) | Länge des eingegebenen Strings (wird hier reingeschrieben) |  |
| 5 | time | Hier bekommt man einen aktuellen Timestamp | In ebx liegt der timestamp dann drin |  |  |
| 6 | usleep | Legt das Programm für %ebx Mikrosekunden schlafen | Anzahl der Mikrosekunden, die zu warten sind |  |  |
| 7 | alloc | Alloziert freie Speicherseiten im userspace (1-3GB) | Anzahl der pages | Adresse |  |
| 8 | free | Gibt Speicherseiten wieder frei | Adresse der pages | Anzahl der pages |  |
| 9 | open | Öffnet eine Datei | Pfad<br>Rückgabe: Filedeskriptor | flags | modus |
| 10 | close | Schließt eine Datei | Fildeskriptor |  |  |
| 11 | read | Liest den Inhalt einer Datei | Filedeskriptor<br>Rückgabe: Anzahl der gelesenen Bytes | Buffer | länge (in bytes) |
| 12 | write | Schreibt in eine Datei | Filedeskriptor<br>Rückgabe: Anzahl der geschriebenen Bytes | Buffer | länge (in bytes) |

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/11095/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2594/index.html)

<!-- MediaWiki page 2594; revision 11095; parent 11094; 2013-04-02T18:41:14Z -->
