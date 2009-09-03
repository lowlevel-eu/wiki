# Týndur/Wunschliste

Hier bitte alle Wünsche für týndur (nach Möglichkeit sortiert nach Zielgebiet) eintragen.

## Kernel

- Syscall damit Prozess für jeden abgestorbenen Prozess einen RPC erhält (Wichtig u.a. um bei unsauber beendeten Programmen aufräumen zu können - alternativ folgt irgendwann ein OOM)

  

## Allgemeines

- Entfernen der COM1-Ausgabe aus putc, stattdessen wäre ein komplettes Modul für serielle Ausgänge (inkl. Eingabe, nicht nur Ausgabe) wünschenswert.

  

## Module

- Tastaturtreiber
  - Ladbare Tastaturbelegungen
  - Deadkeys

## Anwendungen

- FTP-Client
- Mail-Client
- Setup (Installation & Konfiguration)

## LostIO

- Berechtigungen setzen und abfragen
- ioctl/fcntl um kompatibler zu bestehenden Systemen und Anwendungen zu werden (und um alternativ weitere Files im vfs einzusparen)
- Dokumentation/SDK

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/5829/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1513/index.html)

<!-- MediaWiki page 1513; revision 5829; parent 5604; 2009-09-03T08:15:06Z -->
