# CMOS

Ein **Complementary Metal Oxide Semiconductor** (= **CMOS**) ist eigentlich ein elektronischer Baustein, aber im Bereich der Betriebssystemprogrammierung ist damit meistens der Batterie-gepufferte SRAM eines [x86](https://github.com/lowlevel-eu/wiki/wiki/X86 "X86")- bzw. [x86-64](https://github.com/lowlevel-eu/wiki/wiki/X86-64 "X86-64")-Computers gemeint. In diesem speichert das [BIOS](https://github.com/lowlevel-eu/wiki/wiki/Basic-Input-Output-System "BIOS") Informationen beispielsweise über die angeschlossene Hardware. Außerdem wird darin die momentane Uhrzeit und das Datum gespeichert und von einer Echtzeituhr aktualisiert.

## Aufbau

Im CMOS werden folgende jeweils 1Byte große Felder gespeichert:

  

| Offset | Beschreibung |
| -------- | ----------------------------------------------------------------------------------------------------- |
| 0x00 | Sekunde (BCD) |
| 0x01 | Alarmsekunde (BCD) |
| 0x02 | Minute (BCD) |
| 0x03 | Alarmminute (BCD) |
| 0x04 | Stunde (BCD) |
| 0x05 | Alarmstunde (BCD) |
| 0x06 | Wochentag (BCD) |
| 0x07 | Tag des Monats (BCD) |
| 0x08 | Monat (BCD) |
| 0x09 | Jahr (letzten zwei Stellen) (BCD) |
| 0x0A | Statusregister A |
| 0x0B | Statusregister B |
| 0x0C | Statusregister C (schreibgeschützt) |
| 0x0D | Statusregister D (schreibgeschützt) |
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
| 0x32 | Jahrhundert (BCD) |

  

## 0x0A - Statusregister A

**Bit:**

7

**Beschreibung:**

Zeit-Update-Zyklus (1 = Update läuft, Zeitangaben undefiniert)

------------------------------------------------------------------------

**Bit:**

6-4

**Beschreibung:**

Zeit-teiler (Standard = 010b = 32.768 kHz)

------------------------------------------------------------------------

**Bit:**

3-0

**Beschreibung:**

Auswahl-Bits für Interrupts

                0000b = kein Interrupt
                0011b = alle 122 Mikrosekunden (minimum)
                0110b = 976.562 Mikrosekunden (Standard)
                1111b = 500 Millisekunden

  

  

## 0x0B - Statusregister B

| Bit | Beschreibung |
| ----- | -------------------------------------------------------------------- |
| 7 | Zeit-Update (0 = normales Update, 1 = Update läuft) |
| 6 | Periodischer Interrupt (0 = deaktiviert (Standard), 1 = aktiviert) |
| 5 | Alarm Interrupt (0 = deaktiviert (Standard), 1 = aktiviert) |
| 4 | Update-Ende-Interrupt (0 = deaktiviert (Standard), 1 = aktiviert) |
| 3 | Rechtecks-Frequenz (0 = deaktiviert (Standard), 1 = aktiviert) |
| 2 | Daten Modus (0 = BCD, 1 = Binary) |
| 1 | 24/12 Stunden Wahl (0 = 24 Stunden (Standard), 1 = 12 Stunden) |
| 0 | Sommerzeit (0 = deaktiviert (Standard), 1 = aktiviert) |

  

## Programmierung

Die Programmierung des CMOS ist denkbar einfach: Die fünf niederwertigen Bits des I/O Ports 0x70 dienen als Offset (siehe Tabelle). Durch Lesen bzw. Schreiben des I/O Ports 0x71 kann dann der Wert an diesem Offset gelesen bzw. geschrieben werden.

## Weblinks

- [Wikipedia: CMOS](http://de.wikipedia.org/wiki/Complementary_Metal_Oxide_Semiconductor) (*deutsch*)
- [Real Time Clock / CMOS Setup Reference](http://www.nondot.org/sabre/os/files/MiscHW/RealtimeClockFAQ.txt) (*englisch*)
- [CMOS-Aufbau](http://www.bioscentral.com/misc/cmosmap.htm) (*englisch*)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/2374/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1562/index.html)

<!-- MediaWiki page 1562; revision 2374; parent 2373; 2007-12-11T21:22:28Z -->
