# QEMU

| Allgemeines |  |
| ------------------------ | ---------------------------------------------------------------------------- |
| Name: | QEMU |
| Entwickler: | Fabrice Bellard u. a. |
| Akt. Version: | 1.5.0<br>(Stand 20.5.2013) |
| Lizenz: | GPL (tw. LGPL, BSD) |
| Betriebssystem(e): | Linux, Windows, OS X, \*BSD und andere |
| Virtualisiertes System |  |
| Plattform: | x86, x86-64, ARM, CRIS, MIPS(64)(el), M68000, PowerPC(64), SH4, Sparc32/64 |
| SMP: | bis zu 255 Prozessoren |
| Mechanismus: | dynamische Übersetzung, KVM (nur Linux), Kernelunterstützung |
| Homepage |  |

<http://wiki.qemu.org/Main_Page>

QEMU ist ein Emulator unter anderem für die Systeme [Linux](Linux.md "Linux"), [Windows](Windows.md "Windows"), MacOS, FreeBSD, OpenBSD und NetBSD. Er emuliert eine Vielzahl von Architekturen.

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
- [Realtek 8139](RTL8139.md "RTL8139")
- Intel eepro100 und e1000
- [AMD PCnet](AMD-PCnet.md "AMD PCnet")
- virtio (Paravirtualisiertes Netzwerk)

#### Sound

- Systemlautsprecher
- Soundblaster 16
- ES1370 PCI
- [AC97](AC97.md "AC97")
- Intel HD Audio

#### USB

- UHCI-/OHCI-/EHCI- und experimentell auch xHCI-Controller
- HID-Geräte: Tastatur, Maus und Grafiktablett
- USB-Massenspeicher
- USB-Soundkarte
- Durchleitung von USB-Geräten des Hosts

## Aktueller Windows-Build

Bereits seit einiger Zeit gibt es keine offiziellen Binärpakete von QEMU mehr, auch nicht für Windows. Aus diesem Grund werden unter Windows oft deutlich veraltete qemu-Versionen verwendet, deren Fehler gerade bei der Betriebssystementwicklung gelegentlich auffallen. Einigermaßen aktuelle inoffizielle Builds für Windows sind zum Beispiel auf <http://qemu.weilnetz.de/> zu finden.

Ein Build von QEMU 1.2.0 ist ebenfalls auf <http://improved-madness.de/venom/qemu_1.2.0.7z> zu finden.

## QEMU unter Windows kompilieren

Um QEMU unter Windows zu kompilieren, werden MinGW und eine Reihe Bibliotheken, die man sich selbst zusammensuchen muss, benötigt:

- MinGW über den Installer *mingw-get-inst* von <http://sourceforge.net/projects/mingw/> installieren.
- zlib kann anschließend mittels `mingw-get install libz` installiert werden.
- Die aktuelle Version von Python 2.7.x kann von <http://www.python.org/download/> heruntergeladen werden. Für das Kompilieren von QEMU sollte Python zumindest vorübergehend mittels z. B. `SET PATH=C:\Python27;%PATH%` in den Suchpfad eingetragen werden.
- Von <http://www.gtk.org/download/win32.php> die Pakete für GLib und Abhängigkeiten herunterladen und im MinGW-Ordner entpacken:
  1.  pkg-config ("Tool")
  2.  gettext-runtime ("Run-time")
  3.  GLib ("Run-time" und "Dev")
  4.  pixman ("Dev") ab 1.3.0. Wer das Paket selbst bauen will, kann den Quelltext von <http://pixman.org/> herunterladen. Das Kompilieren sollte ausnahmsweise in `sh` erfolgen, damit der korrekte Pfad zum Installationsverzeichnis von MinGW automatisch bestimmt werden kann:

  `` ./configure --prefix=`cd /mingw; pwd -W` && make && make install ``
- Die SDL Development Libraries (SDL-devel-1.2.\*-mingw32.tar.gz) von <http://www.libsdl.org/download-1.2.php> herunterladen und in einem beliebigen Verzeichnis entpacken. In diesem Ordner `make native` ausführen, um SDL im MinGW-Ordner zu installieren.

Anschließend kann QEMU wie üblich konfiguriert und gebaut werden, indem die folgenden Befehle im Quelltextverzeichnis von QEMU ausgeführt werden:

    sh configure --target-list=x86_64-softmmu --prefix=D:/installations/pfad/fuer/qemu
    make
    make install

Das baut ein QEMU, das für die Emulation von x86-PCs (32-/64-Bit) verwendet werden kann. Wenn der Parameter `--target-list` weggelassen wird, wird QEMU für alle Architekturen gebaut, was unter Umständen relativ lange dauert. Für eine Auflistung der unterstützten Architekturen `sh configure --help` ausführen.

Hinweise:

- Wenn man `--prefix` beim `configure` weglässt, wird QEMU in den Programmordner (z. B. C:\Program Files\Qemu) installiert. Dann sind für `make install` Administratorrechte erforderlich, das heißt die Eingabeaufforderung muss für diesen Vorgang als Administrator gestartet werden.
- QEMU gibt unter Windows nur dann etwas auf der Konsole aus, wenn die Umgebungsvariable `SDL_STDIO_REDIRECT` auf `0` gesetzt ist. Deswegen könnte es sinnvoll sein eine Batch-Datei anzulegen, die `SET SDL_STDIO_REDIRECT=0` ausführt.

## Siehe auch

- [Debugging](Debugging.md "Debugging")

## Weblinks

- [QEMU Homepage](http://www.qemu.org)
- [QEMU-Binaries für Windows](http://qemu.weilnetz.de/)
- [QEMU unter Windows](http://www.h7.dion.ne.jp/~qemu-win)
- [Einführung in QEMU](http://qemu-buch.de/de/index.php/Hauptseite)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/11182/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1505/index.html)

<!-- MediaWiki page 1505; revision 11182; parent 11115; 2014-01-02T22:00:34Z -->
