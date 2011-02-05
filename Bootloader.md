# Bootloader

Der **Bootloader** wird vom [BIOS](https://github.com/lowlevel-eu/wiki/wiki/Basic-Input-Output-System "BIOS") aus dem ersten Sektor (dem sogenannten [Bootsektor](https://github.com/lowlevel-eu/wiki/wiki/Bootsektor "Bootsektor")) eines Massenspeichermediums, wie z.B. einer Diskette oder einer Festplattenpartition, in den Hauptspeicher geladen und dort zur Ausführung gebracht. Seine Hauptaufgabe besteht darin, das [Betriebssystem](https://github.com/lowlevel-eu/wiki/wiki/Betriebssystem "Betriebssystem") zu starten, indem er den Kernel und ggf. weitere Module lädt und ausführt.

Handelt es sich bei dem Massenspeicher, von dem gebootet wird, um eine Festplatte, so wird der **Bootloader** nicht direkt von dem [BIOS](https://github.com/lowlevel-eu/wiki/wiki/Basic-Input-Output-System "BIOS") geladen, sondern über den Umweg über den [Master Boot Record](https://github.com/lowlevel-eu/wiki/wiki/Master-Boot-Record "Master Boot Record") (MBR), d.h., das [BIOS](https://github.com/lowlevel-eu/wiki/wiki/Basic-Input-Output-System "BIOS") lädt den MBR, welcher wiederum den **Bootloader** aus dem ersten Sektor einer Festplattenpartition lädt und zur Ausführung bringt.

  

## Probleme

Im Bootsektor ist meist nicht genügend Platz vorhanden, deshalb teilt man den Bootprozess in mehrere Stufen auf: In der ersten Stufe wird der Bootsektor vom BIOS ausgeführt. Dieser lädt wiederum den eigentlichen Bootloader, welcher dann den Rest des Bootprozesses übernimmt und den [Kernel](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel") des Betriebssystems (und evtl. Treiber) lädt und ausführt.

## Ausgangssituation nach dem Laden

Wenn das BIOS die Kontrolle an den Bootloader übergeben hat, gibt es einige Dinge, die jedes BIOS standardmäßig sicherstellen muss:

- das Register dl enthält die Nummer des Bootlaufwerks
- der Prozessor befindet sich im [Real Mode](https://github.com/lowlevel-eu/wiki/wiki/Real-Mode "Real Mode")
- Interrupts sind aktiviert
- CS:IP ist entweder 0x7C0:0x00 oder 0x00:0x7C00

Andere Dinge sind allerdings nicht standardisiert:

- die Position des Stacks
- der Inhalt der Register (außer dl, siehe oben)

## Bekannte Bootloader

- [GRUB](https://github.com/lowlevel-eu/wiki/wiki/Grand-Unified-Bootloader "GRUB") (vielseitiger OpenSource Loader)
- [LILO](https://github.com/lowlevel-eu/wiki/wiki/LILO "LILO") ([Linux](https://github.com/lowlevel-eu/wiki/wiki/Linux "Linux") Loader)
- NTLDR ([Windows](https://github.com/lowlevel-eu/wiki/wiki/Windows "Windows") NT Loader)
- BOOTMGR (Windows Vista Loader)

## Weiterführende Artikel

Obwohl davon abgeraten wird, kann man seinen Bootloader natürlich auch selbst programmieren: [Eigener Bootloader](https://github.com/lowlevel-eu/wiki/wiki/Eigener-Bootloader "Eigener Bootloader")

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/9460/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1477/index.html)

<!-- MediaWiki page 1477; revision 9460; parent 7719; 2011-02-05T23:36:19Z -->
