# VESA BIOS Extensions

Diese Seite ist ein Artikel, welcher **mehr** haben könnte..  

Wenn du mehr darüber weißt oder recherchieren willst, bist **du** aufgerufen, dies zu tun. Wenn du dir in einer Sache nicht sicher bist, dann stell es auf die Diskussionsseite.

Die VESA BIOS Extensions (kurz: VBE) sind ein Standard der [VESA](https://github.com/lowlevel-eu/wiki/wiki/Video-Electronics-Standards-Association "VESA"). Er vereinheitlicht den Zugriff auf eine Grafikkarte, bietet dabei allerdings deutlich mehr Möglichkeiten als [VGA](https://github.com/lowlevel-eu/wiki/wiki/Video-Graphics-Array "VGA"). Der Standard wird von nahezu allen Grafikkarten in Version 2.0 oder der letzten Version, 3.0, unterstützt.

## VBE Funktionen

### Allgemein

Alle Funktionen der VBE sind im Grunde nur im [Real Mode](https://github.com/lowlevel-eu/wiki/wiki/Real-Mode "Real Mode") verfügbar. Die Funktionsnummer wird in AX übergeben, weitere Informationen in den anderen 16 Bit Registern. Jede VBE Funktion liefert einen Wert in AX zurück, der Fehlerinformationen darstellt:

- 004Fh: Aufruf erfolgreich
- 014Fh: Fehler bei der Ausführung
- 024Fh: Funktion nicht unterstützt
- 034Fh: Funktion im aktuellen Grafikmodus nicht unterstützt

Der Funktionaufruf erfolgt über den Interrupt 0x10. Wenn durch irgendwelche Funktionen "FARPTR" zurückgegeben werden, sind dies für den Real Mode immer DWORDs, im Segment:Offset Format, im Protected Mode DWORDs im Selector:Offset Format.

### Linear Frame Buffer

Grundsätzlich stellt VBE zwei Speichermodelle zur Verfügung, um auf den Grafikkartenspeicher zuzugreifen:

- **paged**: Der Speicher wird in mehrere sogenannte "Windows" unterteilt, von denen immer nur eines in den Adressraum der CPU einblendet wird. Um den gesamten Grafikkartenspeicher zu adressieren, muss man zwischen den einzelnen Windows wechseln. Dieser Vorgang wird "Bank Switching" genannt.
- **flat**: Der gesamte Grafikkartenspeicher wird als sogenannter "Linear Frame Buffer" in den Adressraum der CPU eingeblendet.

Der LFB ist wohl eine der wichtigsten Neuerungen mit VBE 2.0. Mithilfe dieser Funktionalität kann man direkt auf den Grafikspeicher der Grafikkarte zugreifen und so viel schneller und einfacher Pixel zeichnen. Außerdem entfällt das lästige "Bank Switching". Daher sollte man (und wird auch) einen Grafikmodus wählen, der den LFB unterstützt.

### Auf VBE-Unterstützung testen: 4F00h

Diese Funktion überprüft, ob die Grafikkarte VBE unterstützt und wenn ja, welche Version.

- AX = 4F00h
- ES:DI = Zeiger auf freien Speicher für den VBE Info Block (512 Bytes)

| Offset | Eintrag | Größe | Beschreibung |
| -------- | ---------------------------------------------------- | ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0 | Signatur | DWORD | Hier sollte "VESA" stehen (=0x56455341) |
| 4 | Version | WORD | 0x0200 für VBE 2.0 und 0x0100 für VBE 1.0 |
| 6 | Zeiger auf OEMString | DWORD |  |
| 10 | Fähigkeiten des Grafikcontrollers | DWORD | • Bit 2: RAMDAC operation: 0=Normal; 1=Leeres Bit benutzen bei großen Blöcken<br>• Bit 1: 0=Controller ist VGA kompatibel<br>• Bit 0: DAC Breite: 0=6 Bits; 1=6 oder 8 Bits<br> |
| 14 | Zeiger auf eine Liste mit unterstützten Grafikmodi | DWORD | Diese Liste ist ein Array aus 16 Bit großen Einträgen, die für die unterstützten Grafikmodi stehen. Der letzte Eintrag ist 0xFFFF. |
| 18 | Größe des Grafikspeichers | WORD | Die Größe des Grafikspeichers in 64KB Blöcken |
| 20 | OEMSoftwareRevision | WORD |  |
| 22 | Zeiger auf OEMVendorNameString | DWORD |  |
| 26 | Zeiger auf OEMProductNameString | DWORD |  |
| 30 | Zeiger auf OEMProductRevision | DWORD |  |
| 34 | *reserviert* | 222 Bytes |  |
| 256 | Datenbereich für OEMStrings | 256 Bytes |  |

Vor dem Aufruf sollte das Feld "Signatur" mit dem Wert "VBE2" gefüllt werden.

### Unterstützte Grafikmodi suchen

In VBE 1.0 waren die Nummern der verschiedenen Grafikmodi noch vordefiniert:

| Modus | Auflösung (Pixel×Pixel) | Farbtiefe (Bit) |
| ------- | ------------------------- | ----------------- |
| 0x100 | 640×400 | 8 |
| 0x101 | 640×480 | 8 |
| 0x102 | 800×600 | 4 |
| 0x103 | 800×600 | 8 |
| 0x104 | 1024×768 | 4 |
| 0x105 | 1024×768 | 8 |
| 0x106 | 1280×1024 | 4 |
| 0x107 | 1280×1024 | 8 |
| 0x108 | 80×60 (Text) | 4 |
| 0x109 | 132×25 (Text) | 4 |
| 0x10A | 132×43 (Text) | 4 |
| 0x10B | 132×50 (Text) | 4 |
| 0x10C | 132×60 (Text) | 4 |
| 0x10D | 320×200 | 15 |
| 0x10E | 320×200 | 16 |
| 0x10F | 320×200 | 24 |

| Modus | Auflösung (Pixel×Pixel) | Farbtiefe (Bit) |
| ------- | ------------------------- | ----------------- |
| 0x110 | 640×480 | 15 |
| 0x111 | 640×480 | 16 |
| 0x112 | 640×480 | 24 |
| 0x113 | 800×600 | 15 |
| 0x114 | 800×600 | 16 |
| 0x115 | 800×600 | 24 |
| 0x116 | 1024×768 | 15 |
| 0x117 | 1024×768 | 16 |
| 0x118 | 1024×768 | 24 |
| 0x119 | 1280×1024 | 15 |
| 0x11A | 1280×1024 | 16 |
| 0x11B | 1280×1024 | 24 |
| 0x11C | 1600×1200 | 8 |
| 0x11D | 1600×1200 | 15 |
| 0x11E | 1600×1200 | 16 |
| 0x11F | 1600×1200 | 24 |

Mit VBE 2.0 hat man sich allerdings dafür entschieden, dass die Grafikkartenherrsteller einfach nur eine Funktion bereitstellen, die alle von der Grafikkarte unterstützten Modi auflistet. Den Zeiger auf diese Liste erhält man mit dem VBE Info Block (4F00h). Diese Liste ist eigentlich nur ein WORD-Array, also eine Hintereinaderreihung von 16Bit Nummern. Diese repräsentieren die von der Grafikkarte unterstützten Grafikmodi. Die Liste wird terminiert durch den Eintrag 0xFFFF.

### Einen bestimmten Grafikmodus suchen: 4F01h

Man durchläuft also die obige Liste der unterstützten Videomodi und prüft dann mit folgender Funktion, welche Eigenschaften der entsprechende Grafikmodus bestitzt:

- AX = 4F01h
- CX = Nummer des Grafikmodus
- ES:DI = Zeiger auf freien Speicher für den ModeInfoBlock

//TODO: ModeInfoBlock beschreiben

So kann man die Nummer desjenigen Grafikmodus herausfinden, den man benötigt.

### In einen Grafikmodus umschalten: 4F02h

Nachdem man nun die gewünschte Grafikmodusnummer hat, muss man nur noch in diesen umschalten:

- AX = 4F02h
- BX = Nummer des VBE Grafikmodus:
  - Bit 15: Löscht den Grafikspeicher, wenn gelöscht
  - Bit 14: Speichermodell: 0=Windowed (paged); 1=Linear (flat)
  - Bits 13-9: reserviert, Null setzen

## VBE im Protected Mode

Vorweg: Es ist nicht möglich, mit VBE einen Grafiktreiber komplett im [Protected Mode](https://github.com/lowlevel-eu/wiki/wiki/Protected-Mode "Protected Mode") zu entwickeln. Wenigstens das Umschalten in den gewünschten Grafikmodus muss im Real Mode erfolgen! Allerdings ist man auf die VBE Funktionen im PM auch nicht mehr angewiesen, wenn man sich für das [LFB](https://github.com/lowlevel-eu/wiki/wiki/VESA-BIOS-Extensions#linear-frame-buffer "LFB") Modell entschieden hat und nachträglich nicht mehr die Auflösung wechseln möchte.

Mit VBE 2.0 wurde das sogenannte "Protected Mode Interface" eingeführt. Das sind Funktionen, die die Grafikkarte zur Verfügung stellt und die im Gegensatz zu den anderen Funktionen in 32Bit Protected Mode Code vorliegen. Die Adresse dieser Funktionen erhält man mit folgendem Auftuf, der allerdings immer noch im Real Mode stattfinden muss:

- AX = 4F0Ah
- BL = 00h

Diese Funktion liefert folgende Werte zurück:

- ES:DI=Zeiger auf eine Tabelle des unten stehenden Formats
- CX=Länge der Tabelle

| Offset | Eintrag |
| -------- | -------------------------------------------------------------------------- |
| 0 | Offset der "SetWindow" Funktion |
| 2 | Offset der "SetDisplayStart" Funktion |
| 4 | Offset der "SetPaletteData" Funktion |
| 6 | Offset auf eine Liste aller Ports und Adresse, auf die der Code zugreift |
| 8 | Code und Daten |

## Pixel zeichnen

### Im Protected Mode

Um im Protected Mode Pixel zu zeichnen, muss man in den Grafikspeicher schreiben. Hier zeigt sich auch der Vorteil des LFB: er ist im PM viel einfacher und schneller zu handhaben! Wenn man also mithilfe des LFB Zugriff auf den Grafikspeicher hat, dann zeichnet man ein Pixel folgendermaßen: \<c\> unsigned int\* lfb = (unsigned int\*) vbe_mode_info.phys_base_ptr; void draw_pixel(unsigned int x, unsigned int y, unsigned int color) {

     lfb[x + y*vbe_mode_info.bytes_per_scan_line = color;

} \</c\>

Wenn man allerdings das paged Modell verwendet, muss man erst den entsprechenden Teil des Grafikspeichers in den Adressraum blenden mithilfe des "Bank Switch".

### im Real Mode

Im Real Mode kann man die obige Variante theoretisch auch verwenden, wenn der Grafikspeicher sich nicht oberhalb der 1MB Marke im Adressraum befindet.

## VBE 3.0

//TODO

## Weblinks

- <http://www.petesqbsite.com/sections/tutorials/tuts/vbe3.pdf> - VBE Spezifikation Version 3.0
- //TODO: Link für VBE 2.0 ( und VBE 1.0?)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/8434/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2303/index.html)

<!-- MediaWiki page 2303; revision 8434; parent 8424; 2010-09-30T16:27:32Z -->
