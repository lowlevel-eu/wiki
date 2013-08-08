# FruityOrange

| FruityOrange |  |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| Datei:FruityOrangeLogo.png |  |
| Entwickler: | [Micha](https://lowlevel-eu.github.io/wiki/pages/2560/index.html "Benutzer:Micha.linuxfreak") |
| Akt. Version: | 0.07 |
| [Lizenz](https://github.com/lowlevel-eu/wiki/wiki/Lizenzen "Lizenzen"): | [GNU General Public License](https://github.com/lowlevel-eu/wiki/wiki/Lizenzen#gnu-general-public-license "Lizenz") |
| OS-Eigenschaften |  |
| Plattform: | [i386](https://github.com/lowlevel-eu/wiki/wiki/X86 "X86") |
| [Kernelart](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel"): | [Monolithisch](https://github.com/lowlevel-eu/wiki/wiki/Kernel#monolithischer-kernel "Kernel") |
| [Sprache](https://lowlevel-eu.github.io/wiki/pages/1648/index.html "Kategorie:Programmiersprache"): | [C](https://github.com/lowlevel-eu/wiki/wiki/C "C") ([Assembler](https://github.com/lowlevel-eu/wiki/wiki/Assembler "Assembler")) |
| API: | nativ |
| Binärformat: | [ELF](https://github.com/lowlevel-eu/wiki/wiki/Executable-and-Linking-Format "ELF") |
| [IPC-Methode](https://github.com/lowlevel-eu/wiki/wiki/Interprozesskommunikation "IPC"): | --- |
| Homepage |  |

<https://github.com/michamimosa/FruityOrange>  
<https://code.google.com/p/fruityorange/>  
<https://sourceforge.net/projects/fruityorange/>

FruityOrange ist ein Betriebssystem für den [i386](https://github.com/lowlevel-eu/wiki/wiki/X86 "X86"), welches [GRUB](https://github.com/lowlevel-eu/wiki/wiki/Grand-Unified-Bootloader "GRUB") als Bootloader benutzt.  
Ein fertiges Images gibts hier: [\[1\]](http://fruityorange.googlecode.com/files/FruityOrange_v0-07.iso) (googlecode) oder hier: [\[2\]](https://sourceforge.net/projects/fruityorange/files/latest/download) (sourceforge)  
  

## Features

- Higherhalf-Kernel
- printf, panic, debug
- [GDT](https://github.com/lowlevel-eu/wiki/wiki/Global-Descriptor-Table "GDT"), [Interrupts](https://github.com/lowlevel-eu/wiki/wiki/Interrupt "Interrupt"), Dynamisches [Syscall](https://github.com/lowlevel-eu/wiki/wiki/Syscall "Syscall")-interface
- [Physische Speicherverwaltung](https://github.com/lowlevel-eu/wiki/wiki/Physische-Speicherverwaltung "Physische Speicherverwaltung"), [Paging](https://github.com/lowlevel-eu/wiki/wiki/Paging "Paging"), [Heap](https://github.com/lowlevel-eu/wiki/wiki/Heapverwaltung "Heap")
- [Multitasking](https://github.com/lowlevel-eu/wiki/wiki/Multitasking "Multitasking"), [ELF](https://github.com/lowlevel-eu/wiki/wiki/Executable-and-Linking-Format "ELF")32-loader
- [VFS](https://github.com/lowlevel-eu/wiki/wiki/Virtuelles-Dateisystem "VFS"), Initiale Ramdisk

### Treiber

- [CGA Grafik](https://github.com/lowlevel-eu/wiki/wiki/Textausgabe "Textausgabe") ;)
- [Tastatur (KBC)](https://github.com/lowlevel-eu/wiki/wiki/Keyboard-Controller "Keyboard Controller")
- [PIT](https://github.com/lowlevel-eu/wiki/wiki/Programmable-Interval-Timer "PIT")
- [CMOS / RTC](https://github.com/lowlevel-eu/wiki/wiki/CMOS "CMOS")

### Programme

- Concha - eine ganz kleine Shell
- utils: ls, cat, cp

## Screenshot

![fruityorange007_1.png](https://sourceforge.net/p/fruityorange/screenshot/fruityorange007_1.png)  
Die shell "concha"  
  
![fruityorange007_2.png](https://sourceforge.net/p/fruityorange/screenshot/fruityorange007_2.png)  
Der Text-Editor "tractius"

## Syscalls

Die Syscalls werden über den Interrupt 0x30 aufgerufen. [\[3\]](https://github.com/michamimosa/FruityOrange/blob/master/include/sys/syscalls.h)

| Nummer (in %eax) | Name |
| ------------------ | -------- |
| 0 | exit |
| 1 | putc |
| 2 | puts |
| 3 | getch |
| 4 | gets |
| 5 | time |
| 6 | usleep |
| 7 | alloc |
| 8 | free |
| 9 | open |

| Nummer (in %eax) | Name |
| ------------------ | --------- |
| 10 | close |
| 11 | read |
| 12 | write |
| 13 | seek |
| 14 | chdir |
| 15 | getcwd |
| 16 | fork |
| 17 | waitpid |
| 18 | exec |
| 19 | readdir |

| Nummer (in %eax) | Name |
| ------------------ | ------------- |
| 20 | exec_extern |
| 21 | fstat |

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/11135/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2594/index.html)

<!-- MediaWiki page 2594; revision 11135; parent 11134; 2013-08-08T10:42:28Z -->
