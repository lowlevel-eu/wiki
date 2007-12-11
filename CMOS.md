# CMOS

Ein **Complementary Metal Oxide Semiconductor** (= **CMOS**) ist eigentlich ein elektronischer Baustein, aber im Bereich der Betriebssystemprogrammierung ist damit meistens der Batterie-gepufferte SRAM eines [x86](https://github.com/lowlevel-eu/wiki/wiki/X86 "X86")- bzw. [x86-64](https://github.com/lowlevel-eu/wiki/wiki/X86-64 "X86-64")-Computers gemeint. In diesem speichert das [BIOS](https://github.com/lowlevel-eu/wiki/wiki/Basic-Input-Output-System "BIOS") Informationen beispielsweise über die angeschlossene Hardware. Außerdem wird darin die momentane Uhrzeit und das Datum gespeichert und von einer Echtzeituhr aktualisiert.

## Aufbau

Im CMOS werden folgende jeweils 1Byte große Felder gespeichert:

  

| Offset | Beschreibung |
| -------- | ----------------------------------------------------------------------------------------------------- |
| 0x00 | Sekunde |
| 0x01 | Alarmsekunde |
| 0x02 | Minute |
| 0x03 | Alarmminute |
| 0x04 | Stunde |
| 0x05 | Alarmstunde |
| 0x06 | Wochentag |
| 0x07 | Tag des Monats |
| 0x08 | Monat |
| 0x09 | Jahr (letzten zwei Stellen) |
| 0x0A | Statusregister A |
| 0x0B | Statusregister B |
| 0x0C | Statusregister C |
| 0x0D | Statusregister D |
| 0x0E | [POST](https://github.com/lowlevel-eu/wiki/wiki/Power-On-Self-Test "POST")-Diagnosestatusbyte |
| 0x0F | Shutdown-Statusbyte |
| 0x10 | Typ der [Diskettenlaufwerke](https://github.com/lowlevel-eu/wiki/wiki/Floppy-Disk-Controller "FDC") |
| 0x12 | Typ der Festplattenlaufwerke |
| 0x13 | reserviert |
| 0x14 | Gerätebyte |
| 0x15 | Größe des Basisspeichers in kB (niederwertiges Byte) |
| 0x16 | Größe des Basisspeichers in kB (höherwertiges Byte) |
| 0x17 | Größe des Erweiterungsspeichers in kB (niederwertiges Byte) |
| 0x18 | Größe des Erweiterungsspeichers in kB (höherwertiges Byte) |
| 0x2E | CMOS-Prüfsumme (niederwertiges Byte) |
| 0x2F | CMOS-Prüfsumme (höherwertiges Byte) |
| 0x32 | Jahrhundert |

  

## Programmierung

Die Programmierung des CMOS ist denkbar einfach: Die fünf niederwertigen Bits des I/O Ports 0x70 dienen als Offset (siehe Tabelle). Durch Lesen bzw. Schreiben des I/O Ports 0x71 kann dann der Wert an diesem Offset gelesen bzw. geschrieben werden.

## Weblinks

- [Wikipedia: CMOS](http://de.wikipedia.org/wiki/Complementary_Metal_Oxide_Semiconductor) (*deutsch*)
- [Real Time Clock / CMOS Setup Reference](http://www.nondot.org/sabre/os/files/MiscHW/RealtimeClockFAQ.txt) (*englisch*)
- [CMOS-Aufbau](http://www.bioscentral.com/misc/cmosmap.htm) (*englisch*)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/2373/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1562/index.html)

<!-- MediaWiki page 1562; revision 2373; parent 2372; 2007-12-11T20:33:49Z -->
