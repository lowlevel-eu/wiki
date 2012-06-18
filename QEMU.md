# QEMU

| Allgemeines |  |
| ------------------------ | ---------------------------------------------------------------------------- |
| Name: | QEMU |
| Entwickler: | Fabrice Bellard u. a. |
| Akt. Version: | 1.1<br>(Stand 18.06.2012) |
| Lizenz: | GPL (tw. LGPL, BSD) |
| Betriebssystem(e): | Linux, Windows, OS X, \*BSD und andere |
| Virtualisiertes System |  |
| Plattform: | x86, x86-64, ARM, CRIS, MIPS(64)(el), M68000, PowerPC(64), SH4, Sparc32/64 |
| SMP: | bis zu 255 Prozessoren |
| Mechanismus: | dynamische Übersetzung, KVM (nur Linux), Kernelunterstützung |
| Homepage |  |

<http://wiki.qemu.org/Main_Page>

QEMU ist ein Emulator unter anderem für die Systeme [Linux](https://github.com/lowlevel-eu/wiki/wiki/Linux "Linux"), [Windows](https://github.com/lowlevel-eu/wiki/wiki/Windows "Windows"), MacOS, FreeBSD, OpenBSD und NetBSD. Er emuliert eine Vielzahl von Architekturen.

## Emulierte Hardware

### x86

Auf einem x86-Prozessor werden neben dem Hauptprozessor folgende Komponenten emuliert:

- PCI und ISA-System (i440FX host PCI bridge und PIIX3 PCI to ISA bridge)
- PS/2-Maus und -Tastatur
- Serielle Schnittstelle
- Parallele Schnittstelle

#### Massenspeicher

- Zwei PCI-ATA-Schnittstellen mit Unterstützung für maximal vier Festplatten-Images
- CD-ROM/DVD-Laufwerk über ISO-Abbild oder reales Laufwerk
- Diskettenlaufwerk
- SATA-Festplatten (AHCI)
- SCSI-Festplatten und SCSI-CD-ROM-Laufwerke
- virtio-blk (Paravirtualisierte Festplatte)
- Unterstützte Dateiformate für Images: Raw, das qemu-eigene Format qcow/qcow2, die Formate von VMware, VirtualBox, Parallels, VirtualPC, Bochs, Knoppix (cloop). Außerdem das Pseudoformat vvfat, das ein Verzeichnis auf dem Hostsystem als FAT-Image im Gast abbildet.

#### Grafikkarte

- Cirrus CLGD 5446 PCI VGA-Karte
- Standard-VGA-Grafikkarte mit Bochs-VESA-BIOS-Extensions (Hardware Level, inklusive aller Nichtstandardmodi, über einen experimentellen Patch auch mit einer vereinfachten 3D-Beschleunigung per OpenGL)

#### Netzwerkkarte und ein DHCP-Server

- NE2000-Netzwerkadapter sowohl für ISA als auch PCI
- [Realtek 8139](https://github.com/lowlevel-eu/wiki/wiki/RTL8139 "RTL8139")
- Intel eepro100 und e1000
- [AMD PCnet](https://github.com/lowlevel-eu/wiki/wiki/AMD-PCnet "AMD PCnet")
- virtio (Paravirtualisiertes Netzwerk)

#### Sound

- Systemlautsprecher
- Soundblaster 16
- ES1370 PCI
- [AC97](https://github.com/lowlevel-eu/wiki/wiki/AC97 "AC97")
- Intel HD Audio

#### USB

- UHCI-/OHCI-/EHCI- und experimentell auch xHCI-Controller
- HID-Geräte: Tastatur, Maus und Grafiktablett
- USB-Massenspeicher
- USB-Soundkarte
- Durchleitung von USB-Geräten des Hosts

## Aktueller Windows-Build

Bereits seit einiger Zeit gibt es keine offiziellen Binärpakete von QEMU mehr, auch nicht für Windows. Aus diesem Grund werden unter Windows oft deutlich veraltete qemu-Versionen verwendet, deren Fehler gerade bei der Betriebssystementwicklung gelegentlich auffallen. Einigermaßen aktuelle inoffizielle Builds für Windows sind zum Beispiel auf <http://qemu.weilnetz.de/> zu finden.

## Siehe auch

- [Debugging](https://github.com/lowlevel-eu/wiki/wiki/Debugging "Debugging")

## Weblinks

- [QEMU Homepage](http://www.qemu.org)
- [QEMU-Binaries für Windows](http://qemu.weilnetz.de/)
- [QEMU unter Windows](http://www.h7.dion.ne.jp/~qemu-win)
- [Einführung in QEMU](http://qemu-buch.de/de/index.php/Hauptseite)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/10618/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1505/index.html)

<!-- MediaWiki page 1505; revision 10618; parent 10347; 2012-06-18T12:45:54Z -->
