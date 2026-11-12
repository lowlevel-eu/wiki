# Bootloader

Der **Bootloader** wird vom [BIOS](Basic-Input-Output-System.md "BIOS") aus dem ersten Sektor (dem sogenannten [Bootsektor](Bootsektor.md "Bootsektor")) eines Massenspeichermediums, wie z.B. einer Diskette oder einer Festplattenpartition, in den Hauptspeicher geladen und dort zur Ausführung gebracht. Seine Hauptaufgabe besteht darin, das [Betriebssystem](Betriebssystem.md "Betriebssystem") zu starten, indem er den Kernel und ggf. weitere Module lädt und ausführt.

Handelt es sich bei dem Massenspeicher, von dem gebootet wird, um eine Festplatte, so wird der **Bootloader** nicht direkt von dem [BIOS](Basic-Input-Output-System.md "BIOS") geladen, sondern über den Umweg über den [Master Boot Record](Master-Boot-Record.md "Master Boot Record") (MBR), d.h., das [BIOS](Basic-Input-Output-System.md "BIOS") lädt den MBR, welcher wiederum den **Bootloader** aus dem ersten Sektor einer Festplattenpartition lädt und zur Ausführung bringt.

  

## Probleme

Im Bootsektor ist meist nicht genügend Platz vorhanden, deshalb teilt man den Bootprozess in mehrere Stufen auf: In der ersten Stufe wird der Bootsektor vom BIOS ausgeführt. Dieser lädt wiederum den eigentlichen Bootloader, welcher dann den Rest des Bootprozesses übernimmt und den [Kernel](Kernel.md "Kernel") des Betriebssystems (und evtl. Treiber) lädt und ausführt.

## Ausgangssituation nach dem Laden

Wenn das BIOS die Kontrolle an den Bootloader übergeben hat, gibt es einige Dinge, die jedes BIOS standardmäßig sicherstellen muss:

- das Register dl enthält die Nummer des Bootlaufwerks
- der Prozessor befindet sich im [Real Mode](Real-Mode.md "Real Mode")
- Interrupts sind aktiviert
- CS:IP ist entweder 0x7C0:0x00 oder 0x00:0x7C00

Andere Dinge sind allerdings nicht standardisiert:

- die Position des Stacks
- der Inhalt der Register (außer dl, siehe oben)

## Bekannte Bootloader

- [GRUB](Grand-Unified-Bootloader.md "GRUB") (vielseitiger OpenSource Loader)
- [LILO](LILO.md "LILO") ([Linux](Linux.md "Linux") Loader)
- NTLDR ([Windows](Windows.md "Windows") NT Loader)
- BOOTMGR (Windows Vista Loader)
- [SYSLINUX](SYSLINUX.md "SYSLINUX")

## Weiterführende Artikel

Obwohl davon abgeraten wird, kann man seinen Bootloader natürlich auch selbst programmieren: [Eigener Bootloader](Eigener-Bootloader.md "Eigener Bootloader")

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/10134/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1477/index.html)

<!-- MediaWiki page 1477; revision 10134; parent 9460; 2011-09-09T15:21:26Z -->
