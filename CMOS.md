# CMOS

Ein **Complementary Metal Oxide Semiconductor** (= **CMOS**) ist eigentlich ein elektronischer Baustein, aber im Bereich der Betriebssystemprogrammierung ist damit meistens der Batterie-gepufferte SRAM eines [x86](https://github.com/lowlevel-eu/wiki/wiki/X86 "X86")- bzw. [x86-64](https://github.com/lowlevel-eu/wiki/wiki/X86-64 "X86-64")-Computers gemeint. In diesem speichert das [BIOS](https://github.com/lowlevel-eu/wiki/wiki/Basic-Input-Output-System "BIOS") Informationen beispielsweise über die angeschlossene Hardware. Außerdem wird darin die momentane Uhrzeit und das Datum gespeichert und von einer [Echtzeituhr](https://github.com/lowlevel-eu/wiki/wiki/Real-Time-Clock "RTC") aktualisiert.

## Aufbau

Im CMOS werden folgende jeweils 1 Byte große Felder gespeichert. Die mit *BCD* markierten Einträge sind standardmässig im [BCD-Format](https://github.com/lowlevel-eu/wiki/wiki/Binary-Coded-Decimal "BCD") kodiert. Die Kodierung kann aber auch im [Statusregister B](https://github.com/lowlevel-eu/wiki/wiki/CMOS#0x0b---statusregister-b "CMOS") (Bit 2) geändert werden. Dabei ist allerdings zu beachten, dass die momentanen Werte im Register an die neue Kodierung angepasst werden müssen und dies nicht von selbst geschieht.

  

| Offset | Beschreibung |
| ------------- | --------------------------------------------------------------------------- |
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
| 0x0A | [Statusregister A](#0x0a---statusregister-a) |
| 0x0B | [Statusregister B](#0x0b---statusregister-b) |
| 0x0C | [Statusregister C](#0x0c---statusregister-c) (schreibgeschützt) |
| 0x0D | [Statusregister D](#0x0d---statusregister-d) (schreibgeschützt) |
| 0x0E | [POST-Diagnosestatusbyte](#) |
| 0x0F | [Shutdown-Statusbyte](#0x0f---shutdown-statusbyte) |
| 0x10 | [Typ der Diskettenlaufwerke](#0x10---typ-der-diskettenlaufwerke) |
| 0x11 | reserviert |
| 0x12 | [Typ der Festplattenlaufwerke](#0x12---typ-der-festplattenlaufwerke) |
| 0x13 | reserviert |
| 0x14 | [Gerätebyte](#0x14---ger%C3%A4tebyte) |
| 0x15 | Größe des Basisspeichers in kB (niederwertiges Byte) |
| 0x16 | Größe des Basisspeichers in kB (höherwertiges Byte) |
| 0x17 | Größe des Erweiterungsspeichers in kB (niederwertiges Byte) |
| 0x18 | Größe des Erweiterungsspeichers in kB (höherwertiges Byte) |
| 0x19 | Erweiterungsbyte 1. Festplatte |
| 0x1A | Erweiterungsbyte 2. Festplatte |
| 0x1B - 0x2D | Reserviert / vom BIOS abhängig |
| 0x2E | [CMOS-Prüfsumme](#0x2e--0x2f---cmos-pr%C3%BCfsumme) (höherwertiges Byte) |
| 0x2F | [CMOS-Prüfsumme](#0x2e--0x2f---cmos-pr%C3%BCfsumme) (niederwertiges Byte) |
| 0x30 | Erweiterter Speicher (niederwertiges Byte) |
| 0x31 | Erweiterter Speicher (höherwertiges Byte) |
| 0x32 | Jahrhundert (BCD) |
| 0x33 - 0x3F | Reserviert / vom BIOS abhängig |

  

### 0x0A - Statusregister A

**Bit**

**Beschreibung**

7Zeit-Update-Zyklus (1 = Update läuft =\> Zeitangaben undefiniert) 6-4Zeit-Basis (Standard = 010b = 32768 Hz) 3-0

**Auswahl-Bits zum Einstellen der Wiederholrate des periodischen Interrupts. Frequenz = 65536 Hz / 2<sup>Rate-Bits</sup>**

| Rate-Bits | Teiler | Frequenz | Periode | Bemerkung |
| ----------- | ---------------------- | ---------- | ------------- | ---------------- |
| 0000b | 0 | \- | \- | kein Interrupt |
| 0011b | 2<sup>3</sup>=8 | 8192 Hz | 122.070 µs | Minimum |
| 0100b | 2<sup>4</sup>=16 | 4096 Hz | 244.141 µs |  |
| 0101b | 2<sup>5</sup>=32 | 2048 Hz | 488.281 µs |  |
| 0110b | 2<sup>6</sup>=64 | 1024 Hz | 976.562 µs | Standard |
| 0111b | 2<sup>7</sup>=128 | 512 Hz | 1.953125 ms |  |
| 1000b | 2<sup>8</sup>=256 | 256 Hz | 3.90625 ms |  |
| 1001b | 2<sup>9</sup>=512 | 128 Hz | 7.8125 ms |  |
| 1010b | 2<sup>10</sup>=1024 | 64 Hz | 15.625 ms |  |
| 1011b | 2<sup>11</sup>=2048 | 32 Hz | 31.25 ms |  |
| 1100b | 2<sup>12</sup>=4096 | 16 Hz | 62.5 ms |  |
| 1101b | 2<sup>13</sup>=8192 | 8 Hz | 125 ms |  |
| 1110b | 2<sup>14</sup>=16384 | 4 Hz | 250 ms |  |
| 1111b | 2<sup>15</sup>=32768 | 2 Hz | 500 ms |  |

  

### 0x0B - Statusregister B

| Bit | Beschreibung |
| ----- | ------------------------------------------------------------------------------------------------------- |
| 7 | Zeit-Update (0 = Zeit aktualisieren, 1 = Zeit-update anhalten) |
| 6 | Periodischer Interrupt mit Rate aus Statusregister A (0 = deaktiviert (Standard), 1 = aktiviert) |
| 5 | Alarm Interrupt wenn Uhrzeit = Alarmzeit (0 = deaktiviert (Standard), 1 = aktiviert) |
| 4 | Update-Interrupt (0 = deaktiviert (Standard), 1 = aktiviert) |
| 3 | Rechtecks-Frequenz mit Rate aus Statusregister A erzeugen (0 = deaktiviert (Standard), 1 = aktiviert) |
| 2 | Daten Modus (0 = BCD, 1 = Binär) |
| 1 | 24 Stundenformat (0 = 12 Stunden, 1 = 24 Stunden (Standard)) |
| 0 | Sommerzeit (0 = deaktiviert (Standard), 1 = aktiviert) |

  

  

### 0x0C - Statusregister C

| Bit | Beschreibung |
| ----- | ---------------------------------------------------------- |
| 7 | Interrupt-Request (1 = RTC hat Interrupt angefordert) |
| 6 | IRQ-Quelle ist periodischer Interrupt (0 = nein, 1 = ja) |
| 5 | IRQ-Quelle ist Alarm-Interrupt (0 = nein, 1 = ja) |
| 4 | IRQ-Interrupt ist Update-Interrupt (0 = nein, 1 = ja) |
| 3-0 | Reserviert |

  

  

### 0x0D - Statusregister D

| Bit | Beschreibung |
| ----- | -------------------------------------------------------------------- |
| 7 | Gültigkeit der Daten im CMOS (0 = ungültig, 1 = Daten sind gültig) |
| 6-0 | Reserviert |

  

  

### 0x0E - [POST](https://github.com/lowlevel-eu/wiki/wiki/Power-On-Self-Test "POST")-Diagnosestatusbyte

| Bit | Beschreibung |
| ----- | -------------------------------------------------------------------------------- |
| 7 | Stromversorgung (0 = OK, 1 = Stromversorgung war unterbrochen) |
| 6 | CMOS-Prüfsumme (0 = OK, 1 = Prüfsumme falsch) |
| 5 | Konfiguration im CMOS stimmt mit ermittelten Werten überein (0 = OK, 1 = nein) |
| 4 | Speichergröße im CMOS == ermittelte Speichergröße (0 = ja, 1 = nein) |
| 3 | Laufwerk bzw Controllerfehler (0 = OK, 1 = Fehler) |
| 2 | Uhrzeit gültig (0 = OK, 1 = Fehler) |
| 1 | Fehler bei Adapterinitialisierung (0 = OK, 1 = Fehler) |
| 0 | Timeout beim Adapter-ID lesen |

  

  

### 0x0F - Shutdown-Statusbyte

80286-Prozessoren konnten nicht vom [Protected Mode](https://github.com/lowlevel-eu/wiki/wiki/Protected-Mode "Protected Mode") in den Realmode zurückgeschaltet werden. Zu diesem Zweck war ein Prozessor-Reset nötig. Das Shutdown-Statusbyte dient dazu dem BIOS anzuzeigen, ob der PC neu gebootet oder der Prozessor nur im Realmode neu gestartet werden soll.

| Wert | Beschreibung |
| ------ | ------------------------------------------------------------------------------- |
| 0x00 | Normale Ausführung des POST |
| 0x01 | Chip Satz Initialisierung für Real Mode |
| 0x02 | Power-On Reset durchführen |
| 0x03 | Power-On Reset durchführen |
| 0x04 | int 0x19-reboot |
| 0x05 | EOI an PIC ausgeben, Tastatur resetten, Sprung zur Addresse \[0x0040:0x0067\] |
| 0x06 | Sprung zur Addresse \[0x0040:0x0067\] ohne EOI |
| 0x07 | zurück zu Int 0x15, Funktion 0x87 (Block im Extenden Memory verschieben) |
| 0x08 | zurück zum POST Speicher Test |
| 0x09 | zurück zu Int 0x15, Funktion 0x87 (Block im Extenden Memory verschieben) |
| 0x0A | JMP zu \[0x0040:0x0067\] |
| 0x0B | IRET zu \[0x0040:0x0067\] |
| 0x0C | RET zu \[0x0040:0x0067\] |

  

### 0x10 - Typ der [Diskettenlaufwerke](https://github.com/lowlevel-eu/wiki/wiki/Floppy-Disk-Controller "FDC")

In diesem Byte wird der Typ der [Diskettenlaufwerke](https://github.com/lowlevel-eu/wiki/wiki/Floppy-Disk-Controller "FDC") gespeichert, wobei in den Bits 4-7 der Typ des ersten Laufwerks gespeichert ist und in den Bits 0-3 der Typ des zweiten Laufwerks. Die Typen sind wie folgt kodiert:

    0000b = Laufwerk nicht vorhanden
    0001b = 5 1/4 - 360 kB
    0010b = 5 1/4 - 1.2 MB
    0011b = 3 1/2 - 720 kB
    0100b = 3 1/2 - 1.44 MB (sollte eigentlich heutzutage der Standard sein)
    0101b - 1111b sind unbenutzt

  

  

### 0x12 - Typ der Festplattenlaufwerke

In diesem Byte wird der Typ der Festplattenlaufwerke gespeichert, wobei in den Bits 4-7 der Typ des ersten Laufwerks gespeichert ist und in den Bits 0-3 der Typ des zweiten Laufwerks. Die Typen sind wie folgt kodiert:

    0000b = Laufwerk nicht vorhanden
    0001b - 1110b = Typen 1-14
    1111b = Typ laut Erweiterungsbyte der Festplatte

  

### 0x14 - Gerätebyte

Hier werden Informationen über die allgemeine Hardwarekonfiguration des PCs gespeichert.

| Bits | 7-6 | 5-4 | 3 | 2 | 1 | 0 |
| ------ | ---------------- | ------------- | -------------------- | --------------------- | --------------------------------------- | -------- |
|  | Anzahl Floppys | Display-Typ | Display vorhanden? | Keyboard vorhanden? | Mathematischer Koprozessor vorhanden? | Floppy |

**Anzahl Floppys**  
Auf diesen Wert nur verlassen wenn Floppy=1  

    00b  1 Floppy-Laufwerk
    01b  2 Floppy-Laufwerke

**Display-Typ**

    00b  BIOS-Display-Adapter
    01b  CGA (40 Spalten)
    10b  CGA (80 Spalten)
    11b  Monochrom

  

### 0x2E & 0x2F - CMOS-Prüfsumme

Die CMOS-Prüfsumme ist eine 16 Bit grosse, byteweise Summe der Werte der Bytes von 0x10 bis 0x2D.

## Programmierung

Die Programmierung des CMOS ist denkbar einfach: Die sieben niederwertigen Bits des I/O Ports 0x70 dienen als Offset (siehe Tabelle). Das höchste Bit sollte nicht verändert werden, es dient als [NMI](https://github.com/lowlevel-eu/wiki/wiki/Non-Maskable-Interrupt "Non Maskable Interrupt")-Maskierungsregister. Durch Lesen bzw. Schreiben des I/O Ports 0x71 kann dann der Wert an diesem Offset gelesen bzw. geschrieben werden.

### Assembler Beispielcode

\<asm\>

Ein Makro um ein Byte aus dem CMOS auszulesen

Der einzige Parameter ist das Offset des Bytes welches gelesen werden soll

Rückgabe ist das gelesene Byte in AL

%macro read_byte 1

     in al, 0x70         ;Bit 7 des Ports sichern
     and al, 10000000b
     or al, %1           ;Offset (Parameter 1) dazumixen
     out 0x70, al        ;Offset setzen
     in al, 0x71         ;Byte lesen

%endmacro \</asm\>

### C/C++ Beispielcode

\<c\>

1.  define CMOS_PORT_ADDRESS 0x70
2.  define CMOS_PORT_DATA 0x71

/\*\*

    * Liest ein Byte aus den CMOS
    *  @param offset Offset im CMOS
    *  @return Gelesener Wert
    */

uint8_t cmos_read(uint8_t offset) {

     uint8_t tmp = inb(CMOS_PORT_ADDRESS);
     outb(CMOS_PORT_ADDRESS, (tmp & 0x80) | (offset & 0x7F));
     return inb(CMOS_PORT_DATA);

}

/\*\*

    * Schreibt ein Byte in das CMOS
    *  @param offset Offset im CMOS
    *  @param val Zu schreibender Wert
    */

void cmos_write(uint8_t offset,uint8_t val) {

     uint8_t tmp = inb(CMOS_PORT_ADDRESS);
     outb(CMOS_PORT_ADDRESS, (tmp & 0x80) | (offset & 0x7F));
     outb(CMOS_PORT_DATA,val);

} \</c\>

## Weblinks

- [Real Time Clock / CMOS Setup Reference](http://www.nondot.org/sabre/os/files/MiscHW/RealtimeClockFAQ.txt) (*englisch*)
- [CMOS-Aufbau](http://www.bioscentral.com/misc/cmosmap.htm) (*englisch*)
- [Bochs's CMOS map](http://bochs.sourceforge.net/doc/docbook/development/cmos-map.html) (*englisch*)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/9461/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1562/index.html)

<!-- MediaWiki page 1562; revision 9461; parent 9061; 2011-02-05T23:40:24Z -->
