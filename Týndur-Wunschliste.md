# Týndur/Wunschliste

Hier bitte alle Wünsche für LOST (nach Möglichkeit sortiert nach Zielgebiet) eintragen.

## Kernel

- Syscall damit Prozess für jeden abgestorbenen Prozess einen RPC erhält (Wichtig u.a. um bei unsauber beendeten Programmen aufräumen zu können - alternativ folgt irgendwann ein OOM)

  

## Allgemeines

- Entfernen der COM1-Ausgabe aus putc, stattdessen wäre ein komplettes Modul für serielle Ausgänge (inkl. Eingabe, nicht nur Ausgabe) wünschenswert.

  

## Module

- serial (ttyS\* / COM\*), schreiben/lesen von den Ports, Konfiguration, ggf. auch Handshaking hierher verlegen.

  

## Anwendungen

- Texteditor
- fdisk-äquivalent (Partitionsverwaltung)
- FTP-Client
- Hilfesystem
- Setup (Installation & Konfiguration)

  

## LostIO

- Berechtigungen setzen und abfragen
- ioctl um kompatibler zu bestehenden Systemen und Anwendungen zu werden (und um alternativ weitere files im vfs einzusparen)
- Dokumentation/SDK

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/2930/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1513/index.html)

<!-- MediaWiki page 1513; revision 2930; parent 2722; 2008-05-07T13:19:17Z -->
