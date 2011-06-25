# VirtualBox

| Allgemeines |  |
| ------------------------ | ----------------------------------------------- |
| Name: | VirtualBox |
| Entwickler: | Oracle (ehemals Innotek & Sun) |
| Akt. Version: | 4.0.8<br>(Stand 26.06.2011) |
| Lizenz: | Proprietär, GPL 2 (2 Versionen) |
| Betriebssystem(e): | Linux, Windows, OS X, Solaris |
| Virtualisiertes System |  |
| Plattform: | x86, x86-64 |
| SMP: | bis zu 255 Prozessoren |
| Mechanismus: | dynamische Übersetzung, Hardwareunterstützung |
| Homepage |  |

<http://www.virtualbox.org/>

**VirtualBox**, auch bekannt als **VirtuaBox** ist ein x86-Emulator für x86-Systeme. Ursprünglich entwickelt von innotek, kaufte Sun das Programm auf, stellte zugleich aber eine der beiden Versionen als OpenSource-Software frei zur Verfügung. Diese Duale Lizenzierung wurde auch nach der Übernahme durch Oracle weitergeführt. Das Besondere an VirtualBox ist sicherlich die ausgereifte grafische Benutzerschnittstelle, die die Bedienung weitaus einfacher macht.

## Besondere Features

- iSCSI für Blockgeräte
- Fernsteuerung der VM via RDP, inklusive Support für USB über RDP
- Gastunsterstützung um unter offiziell unterstützen Betriebssystemen Geschwindigkeitsvorteile und weitere Features anbieten zu können.
- OpenGL-Unterstützung (derzeit nur für die 32-Bit-Versionen von Windows XP und Windows Vista sowie Linux und Solaris)
- Experimenteller Support für [EFI (Extensible Firmware Interface)](https://github.com/lowlevel-eu/wiki/wiki/Unified-Extensible-Firmware-Interface "Extensible Firmware Interface")

Befehlssatzerweiterungen für Gäste:

- PAE/NX (falls vom Host unterstützt)

## Emulierte Hardware

- ACPI, inklusive ACPI Power Status (mit Anbindung an Host)
- I/O APIC
- [Floppy](https://github.com/lowlevel-eu/wiki/wiki/Floppy-Disk-Controller "Floppy Disk Controller")
- IDE Controller:
  - PIIX3
  - PIIX4
- SATA AHCI Controller Intel ICH8M/ICH8M-E
- [AC'97](https://github.com/lowlevel-eu/wiki/wiki/AC97 "AC97") Audio (Intel)
- [Netzwerkkarten](https://lowlevel-eu.github.io/wiki/pages/1826/index.html "Kategorie:Netzwerkkarte"):
  - PCnet FAST III
  - PCnet-PCI II
  - Intel PRO/1000 MT Desktop
  - Intel PRO/1000 T Server
- [USB](https://github.com/lowlevel-eu/wiki/wiki/Universal-Serial-Bus "Universal Serial Bus")-Controller:
  - [EHCI](https://github.com/lowlevel-eu/wiki/wiki/Enhanced-Host-Controller-Interface "Enhanced Host Controller Interface") (USB 2.0)
- Serielle Schnittstellen (max. 2)

## Links

- [VirtualBox Homepage](http://www.virtualbox.org/)
- [Changelog](http://www.virtualbox.org/wiki/Changelog)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/9874/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1553/index.html)

<!-- MediaWiki page 1553; revision 9874; parent 8696; 2011-06-25T22:58:08Z -->
