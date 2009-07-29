# Bootloader

Der **Bootloader** wird vom [BIOS](https://github.com/lowlevel-eu/wiki/wiki/Basic-Input-Output-System "BIOS") oder einem [Bootsektor](https://github.com/lowlevel-eu/wiki/wiki/Bootsektor "Bootsektor") in den Speicher geladen und ausgeführt. Er hat die Aufgabe, ein [Betriebssystem](https://github.com/lowlevel-eu/wiki/wiki/Betriebssystem "Betriebssystem") zu starten. Im Bootsektor ist meist nicht genügend Platz vorhanden, deshalb teilt man den Bootprozess in mehrere Stufen auf: In der ersten Stufe wird der Bootsektor vom BIOS ausgeführt. Dieser lädt wiederum den eigentlichen Bootloader, welcher dann den Rest des Bootprozesses übernimmt und den [Kernel](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel") des Betriebssystems (und evtl. Treiber) lädt und ausführt.

## Bekannte Bootloader

- [GRUB](https://github.com/lowlevel-eu/wiki/wiki/Grand-Unified-Bootloader "GRUB") (vielseitiger OpenSource Loader)
- [LILO](https://github.com/lowlevel-eu/wiki/wiki/LILO "LILO") (Linux Loader)
- NTLDR (Windows NT Loader)
- BOOTMGR (Windows Vista Loader)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/4793/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1477/index.html)

<!-- MediaWiki page 1477; revision 4793; parent 4579; 2009-07-29T23:50:13Z -->
