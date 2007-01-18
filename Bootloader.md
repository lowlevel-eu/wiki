# Bootloader

Der Bootloader wird vom BIOS oder einem Bootsektor in den Speicher geladen und ausgeführt und hat die Aufgabe, ein Betriebssystem zu starten. Oft sind Bootloader in mehreren Stufen aufgeteilt, wenn im Bootsektor nicht genügend Platz vorhanden ist. In diesem Fall läd die erste Stufe (der Bootsektor) die zweite Stufe, die dann den Rest der Bootprozesses durchführt und den Betriebssystemkernel startet.

## Bekannte Bootloader

- [GRUB](https://github.com/lowlevel-eu/wiki/wiki/Grand-Unified-Bootloader "GRUB") (vielseitiger OpenSource Loader)
- [LILO](https://github.com/lowlevel-eu/wiki/wiki/LILO "LILO") (Linux Loader)
- NTLDR (Windows NT Loader)
- BOOTMGR (Windows Vista Loader)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/1736/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1477/index.html)

<!-- MediaWiki page 1477; revision 1736; parent 0; 2007-01-18T20:07:11Z -->
