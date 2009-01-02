# QEMU

| Allgemeines |  |
| ------------------------ | -------------------------------------------------------------- |
| Name: | QEMU |
| Entwickler: | Fabrice Bellard u. a. |
| Akt. Version: | 0.9.1<br>(Stand 02.01.2009) |
| Lizenz: | GPL |
| Betriebssystem(e): | Linux, Windows, OS X, \*BSD und andere |
| Virtualisiertes System |  |
| Plattform: | x86, x86-64, PowerPC, Sparc32/64 |
| SMP: | bis zu 255 Prozessoren |
| Mechanismus: | dynamische Übersetzung, KVM (nur Linux), Kernelunterstützung |
| Homepage |  |

[http://bellard.org/qemu/](http://bellard.org/qemu/index.html)

QEMU ist ein Emulator unter anderem für die Systeme [Linux](https://github.com/lowlevel-eu/wiki/wiki/Linux "Linux"), [Windows](https://github.com/lowlevel-eu/wiki/wiki/Windows "Windows"), MacOS, FreeBSD, OpenBsd und NetBSD.

  
QEMU emuliert x86-, x86-64 bzw. AMD64-, PowerPC- und Sparc32/64-Hardware.

  
Auf einem x86 Prozessor werden neben dem Hauptprozessor folgende Komponenten emuliert:

- CD-ROM/DVD-Laufwerk über ISO-Abbild oder reales Laufwerk
- Diskettenlaufwerk
- Grafikkarte (Cirrus CLGD 5446 PCI VGA-Karte oder Standard-VGA-Grafikkarte mit Bochs-VESA-BIOS-Extensions (Hardware Level, inklusive aller Nichtstandardmodi, über einen experimentellen Patch auch mit einer vereinfachten 3D-Beschleunigung per OpenGL)
- Netzwerkkarte (NE2000-PCI-Netzwerkadapter) und ein DHCP-Server
- Parallelele Schnittstelle
- Systemlautsprecher
- zwei PCI-ATA-Schnittstellen mit Unterstützung für maximal vier Festplatten-Images im eigenen Format oder im Format von VMware, VirtualPC, Bochs, Knoppix (cloop) und dd
- PCI und ISA-System (i440FX host PCI bridge und PIIX3 PCI to ISA bridge)
- PS/2-Maus und -Tastatur
- Serielle Schnittstelle
- Soundkarte (Soundblaster 16, ES1370 PCI)
- USB-Controller (Intel SB82371, UHCI)

# Siehe Auch

- GNU Project Debugger und QEMU

# Links

- [QEMU Homepage](http://www.qemu.org)
- [QEMU unter Windows](http://www.h7.dion.ne.jp/~qemu-win)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/3816/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1505/index.html)

<!-- MediaWiki page 1505; revision 3816; parent 2871; 2009-01-02T20:14:03Z -->
