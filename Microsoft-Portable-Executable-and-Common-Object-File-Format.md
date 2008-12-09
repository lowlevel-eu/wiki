# Microsoft Portable Executable and Common Object File Format

## Grober Aufbau

### MS-DOS Header

Diese Header ist ein Kompabilitätsheader, womit im MS-DOS ausgedrückt werden kann, dass das Programm darunter nicht läuft.  
Für lowlevel kann dieser Bereich getrost ausgelassen werden, weil

- Programme eines Nicht-Windowssystem brauchen nicht unter MS-DOS zu laufen
- Fast niemand hat noch MS-DOS

### PE Kennzeichnung

An der Stelle 0x3c kommt das Kennzeichnen des PE-Formates. Dieser ist 4-Byte groß und sieht so aus: "PE\0\0". (Zwei Nullbytes am Ende) Das ist wiederum ein Kennzeichen von Windows und sollte verändert(nicht weggelassen) werden.

  

  

## Links

- [Microsoft Portable Executable and Common Object File Format Specification](http://www.microsoft.com/whdc/system/platform/firmware/PECOFF.mspx)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/3635/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1644/index.html)

<!-- MediaWiki page 1644; revision 3635; parent 3633; 2008-12-09T15:47:55Z -->
