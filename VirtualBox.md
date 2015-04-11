# VirtualBox

| Allgemeines |  |
| ------------------------ | ----------------------------------------------- |
| Name: | VirtualBox |
| Entwickler: | Oracle (ehemals Innotek & Sun) |
| Akt. Version: | 4.1.2<br>(Stand 19.09.2011) |
| Lizenz: | GPL 2, Proprietär (Extension Packs) |
| Betriebssystem(e): | Linux, Windows, OS X, Solaris |
| Virtualisiertes System |  |
| Plattform: | x86, x86-64 |
| SMP: | bis zu 255 Prozessoren |
| Mechanismus: | dynamische Übersetzung, Hardwareunterstützung |
| Homepage |  |

<http://www.virtualbox.org/>

**VirtualBox** ist ein x86-Emulator für x86-Systeme. Ursprünglich entwickelt von innotek, kaufte Sun das Programm auf, stellte zugleich aber eine der beiden Versionen als OpenSource-Software frei zur Verfügung. Diese Duale Lizenzierung wurde auch nach der Übernahme durch Oracle weitergeführt, zur Veröffenlichung von Version 4.0 jedoch umgestelt: Es existiert nun nur noch die Open-Source-Version, die propietären Erweiterungen werden als Extension Pack angeboten. Das Besondere an VirtualBox ist sicherlich die ausgereifte grafische Benutzerschnittstelle, die die Bedienung weitaus einfacher macht.

## Besondere Features

- iSCSI für Blockgeräte
- Fernsteuerung der VM via RDP, inklusive Support für USB über RDP
- Gastunterstützung, um unter offiziell unterstützen Betriebssystemen Geschwindigkeitsvorteile und weitere Features anbieten zu können.
- OpenGL-Unterstützung (derzeit nur für die 32-Bit-Versionen von Windows XP und Windows Vista sowie Linux und Solaris)
- Experimenteller Support für [EFI (Extensible Firmware Interface)](https://github.com/lowlevel-eu/wiki/wiki/Unified-Extensible-Firmware-Interface "Extensible Firmware Interface")
- Debugger

Befehlssatzerweiterungen für Gäste:

- PAE/NX (falls vom Host unterstützt)

## Emulierte Hardware

- ACPI, inklusive ACPI Power Status (mit Anbindung an Host)
- [I/O_APIC](https://github.com/lowlevel-eu/wiki/wiki/I-O-Advanced-Programmable-Interrupt-Controller "I/O APIC")
- VGA- und [VBE](https://github.com/lowlevel-eu/wiki/wiki/VESA-BIOS-Extensions "VBE")-kompatible Grafikkarte
- [Floppy](https://github.com/lowlevel-eu/wiki/wiki/Floppy-Disk-Controller "Floppy Disk Controller")
- IDE Controller:
  - PIIX3
  - PIIX4
  - ICH6
- SATA AHCI Controller Intel ICH8M/ICH8M-E
- Soundkarten
  - [AC'97](https://github.com/lowlevel-eu/wiki/wiki/AC97 "AC97") Audio (Intel)
  - SoundBlaster 16
  - Intel HD Audio
- [Netzwerkkarten](https://lowlevel-eu.github.io/wiki/pages/1826/index.html "Kategorie:Netzwerkkarte"):
  - [PCnet FAST III](https://github.com/lowlevel-eu/wiki/wiki/AMD-PCnet "AMD PCnet")
  - PCnet-PCI II
  - Intel PRO/1000 MT Desktop
  - Intel PRO/1000 T Server
- [USB](https://github.com/lowlevel-eu/wiki/wiki/Universal-Serial-Bus "Universal Serial Bus")-Controller:
  - [OHCI](https://github.com/lowlevel-eu/wiki/wiki/Open-Host-Controller-Interface "Open Host Controller Interface")
  - [EHCI](https://github.com/lowlevel-eu/wiki/wiki/Enhanced-Host-Controller-Interface "Enhanced Host Controller Interface") (USB 2.0, nur per Extension Pack)
  - [xHCI](https://github.com/lowlevel-eu/wiki/wiki/Extensible-Host-Controller-Interface "XHCI") (Nur per Extension Pack, ab Version 5)
- Serielle Schnittstellen (max. 2)

## Debugger

Seit einiger Zeit bietet VirtualBox einen integrierten Debugger, der Informationen zum Zustand der VM, der emulierten CPU und der emulierten Geräte ausgeben kann. Weiterhin werden Breakpoints unterstützt sowie die schrittweise Ausführung des Codes ermöglicht. Im Folgenden soll kurz dargestellt werden, wie diese (versteckte) Funktion aktiviert wird, was sie bringt und wie man sie nutzt.

### Den Debugger aktivieren und starten

Oracle hat den Debugger - mit der Begründung, er sei nur für "advanced users" geeignet - gut versteckt, denn standardmäßig ist er nicht aktiviert und seine Existenz ist über die GUI auch nicht zu erkennen. Es gibt 3 Wege, diesen zu aktivieren:

- In der Konfigurationsdatei von VirtualBox (Unter Windows zu finden unter C:/Benutzer/\<Benutzer\>/.VirtualBox/VirtualBox.xml (Windows 7) bzw. C:/Dokumente und Einstellungen/\<Benutzer\>/.VirtualBox (Windows XP)) zum Knoten "VirtualBox/Global/ExtraData" dies hinzufügen:

      <ExtraDataItem name="GUI/Dbg/Enabled" value="true"/>

  VBox muss neu gestartet werden, damit die Änderung übernommen wird.

- Die Umgebungsvariable VBOX_GUI_DBG_ENABLED oder VBOX_GUI_DBG_AUTO_SHOW auf true setzen, bevor VBox gestartet wird

- VirtualBox mit den Kommandozeilenparametern --dbg, --debug, oder --debug-command-line starten

Anschließend kann der Debugger aus der laufenden VM gestartet werden. In der laufenden Maschine sollte der Menüpunkt "Debug" hinzugekommen sein.

### Benutzung

Wenn man im Menü "Debug" den Unterpunkt "Kommandozeile" wählt, erhält man dann eine Konsole, über die die weitere Steuerung des Debuggers hauptsächlich erfolgt.

#### Informationen beschaffen

Die wichtigsten Befehle der Kommandozeile, um Infos über das System zu erhalten:

| Befehl | Wirkung |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| r | Gibt den Inhalt der Register der CPU aus |
| u | Disassembliert den Code, der als nächstes ausgeführt wird |
| k | Gibt einen Stacktrace aus |
| dg | GDT |
| di | IDT |
| dl | LDT |
| dt | TSS |
| da/db/dw/dd/dq | Gibt den Speicher an der angegebenen Addresse aus, als ASCII-Text, in Bytes/Words/Doublewords/Quadwords |
| info \<arg\> | Gibt Infos zum angegebenen Gerät aus. Übersicht über diese Geräte: info help. Beispiele: pcnet0, pit, pic, ohci, ehci, vbe, ioport, ... |

#### Log

Hinter dem Menüelement "Zeige Log" verbirgt sich ein Fenster, dessen erste Registerkarte ein Log enthält, dass dem von Bochs ähnelt. Es enthält beispielsweise Fehlermeldungen und Statusänderungen der von VirtualBox emulierten Geräte.

#### Breakpoints

Folgende Informationen fehlen dem Artikel an dieser Stelle:

- Ergänzungen zum Debugger, d.h. zum Setzen von Breakpoints und zur schrittweisen Code-Ausführung

Hilf Lowlevel, den Artikel zu verbessern.

## Links

- [VirtualBox Homepage](http://www.virtualbox.org/)
- [Changelog](http://www.virtualbox.org/wiki/Changelog)
- [VirtualBox-Dokumentation über den Debugger](http://www.virtualbox.org/manual/ch12.html#idp6083456)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/11271/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1553/index.html)

<!-- MediaWiki page 1553; revision 11271; parent 11257; 2015-04-11T08:55:58Z -->
