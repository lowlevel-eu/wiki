# QEMU

| Allgemeines |  |
| ------------------------ | ---------------------------------------------------------------------------- |
| Name: | QEMU |
| Entwickler: | Fabrice Bellard u. a. |
| Akt. Version: | 0.12.2<br>(Stand 12.02.2009) |
| Lizenz: | GPL (tw. LGPL, BSD) |
| Betriebssystem(e): | Linux, Windows, OS X, \*BSD und andere |
| Virtualisiertes System |  |
| Plattform: | x86, x86-64, ARM, CRIS, MIPS(64)(el), M68000, PowerPC(64), SH4, Sparc32/64 |
| SMP: | bis zu 255 Prozessoren |
| Mechanismus: | dynamische Übersetzung, KVM (nur Linux), Kernelunterstützung |
| Homepage |  |

<http://www.nongnu.org/qemu/>

QEMU ist ein Emulator unter anderem für die Systeme [Linux](https://github.com/lowlevel-eu/wiki/wiki/Linux "Linux"), [Windows](https://github.com/lowlevel-eu/wiki/wiki/Windows "Windows"), MacOS, FreeBSD, OpenBsd und NetBSD.

  
QEMU emuliert eine Vielzahl von Architekturen.

  

## Emulierte Hardware

### x86

Auf einem x86-Prozessor werden neben dem Hauptprozessor folgende Komponenten emuliert:

- PCI und ISA-System (i440FX host PCI bridge und PIIX3 PCI to ISA bridge)
- PS/2-Maus und -Tastatur
- Serielle Schnittstelle
- Parallelele Schnittstelle

#### Massenspeicher

- Zwei PCI-ATA-Schnittstellen mit Unterstützung für maximal vier Festplatten-Images
- CD-ROM/DVD-Laufwerk über ISO-Abbild oder reales Laufwerk
- Diskettenlaufwerk
- Unterstützte Dateiformate für Images: Raw, das qemu-eigene Format qcow/qcow2, die Formate von VMware, Parallels, VirtualPC, Bochs, Knoppix (cloop). Außerdem das Pseudoformat vvfat, das ein Verzeichnis auf dem Hostsystem als FAT-Image im Gast abbildet.

#### Grafikkarte

- Cirrus CLGD 5446 PCI VGA-Karte
- Standard-VGA-Grafikkarte mit Bochs-VESA-BIOS-Extensions (Hardware Level, inklusive aller Nichtstandardmodi, über einen experimentellen Patch auch mit einer vereinfachten 3D-Beschleunigung per OpenGL)

#### Netzwerkkarte und ein DHCP-Server

- NE2000-Netzwerkadapter sowohl für ISA als auch PCI
- [Realtek 8139](https://github.com/lowlevel-eu/wiki/wiki/RTL8139 "RTL8139")
- Intel eepro100 und e1000
- AMD PCnet
- virtio (Paravirtualisiertes Netzwerk)

#### Sound

- Systemlautsprecher
- Soundblaster 16
- ES1370 PCI
- [AC97](https://github.com/lowlevel-eu/wiki/wiki/AC97 "AC97")

#### USB

- UHCI- und OHCI-Controller
- HID-Geräte: Tastatur, Maus und Grafiktablett
- USB-Massenspeicher
- Durchleitung von USB-Geräten des Hosts

## Aktueller Windows-Build

Die letzten zumindest halboffiziellen Builds für Windows stammen aus 0.9.x-Zeiten. Aus diesem Grund werden unter Windows oft deutlich veraltete qemu-Versionen verwendet, deren Fehler gerade bei der Betriebssystementwicklung gelegentlich auffallen. Eine einigermaßen aktuelle Version für Windows (git-Version von Anfang November 2009) liegt auf unserem Server: [\[1\]](http://lowlevel.brainsware.org/download/qemu-0.11.50-c988bfa.tar.bz2)

## Siehe Auch

- GNU Project Debugger und QEMU

## Weblinks

- [QEMU Homepage](http://www.qemu.org)
- [QEMU unter Windows](http://www.h7.dion.ne.jp/~qemu-win)
- [Einführung in QEMU](http://qemu-buch.de/de/index.php/Hauptseite)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/7062/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1505/index.html)

<!-- MediaWiki page 1505; revision 7062; parent 6583; 2010-02-11T23:31:19Z -->
