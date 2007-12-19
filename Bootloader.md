# Bootloader

Der Bootloader wird vom [BIOS](https://github.com/lowlevel-eu/wiki/wiki/Basic-Input-Output-System "BIOS") oder einem [Bootsektor](https://github.com/lowlevel-eu/wiki/wiki/Bootsektor "Bootsektor") in den Speicher geladen und ausgeführt und hat die Aufgabe, ein [Betriebssystem](https://github.com/lowlevel-eu/wiki/wiki/Betriebssystem "Betriebssystem") zu starten. Oft sind Bootloader in mehreren Stufen aufgeteilt, wenn im Bootsektor nicht genügend Platz vorhanden ist. In diesem Fall lädt die erste Stufe (der Bootsektor) die zweite Stufe, die dann den Rest der Bootprozesses durchführt und den [Betriebssystemkernel](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel") startet.

## Bekannte Bootloader

- [GRUB](https://github.com/lowlevel-eu/wiki/wiki/Grand-Unified-Bootloader "GRUB") (vielseitiger OpenSource Loader)
- [LILO](https://github.com/lowlevel-eu/wiki/wiki/LILO "LILO") (Linux Loader)
- NTLDR (Windows NT Loader)
- BOOTMGR (Windows Vista Loader)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/2432/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1477/index.html)

<!-- MediaWiki page 1477; revision 2432; parent 1738; 2007-12-19T15:25:20Z -->
