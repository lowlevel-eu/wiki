# VESA BIOS Extensions

Die VESA BIOS Extensions (kurz: VBE) sind ein Standard der [VESA](Video-Electronics-Standards-Association.md "VESA"). Er vereinheitlicht den Zugriff auf eine Grafikkarte und bietet dabei deutlich mehr Möglichkeiten als [VGA](Video-Graphics-Array.md "VGA"). Der Standard wird von nahezu allen Grafikkarten in Version 2.0 oder der letzten Version, 3.0, unterstützt. **Daher bezieht sich dieser Artikel, wenn nicht anders vermerkt, auf Version 2.0.**

## VBE Funktionen

### Allgemein

Alle Funktionen der VBE sind im Grunde nur im [Real Mode](Real-Mode.md "Real Mode") verfügbar (es gibt ein Protected-Mode-Interface, welches allerdings nur sehr spärlich unterstützt wird). Die Funktionsnummer wird in AX übergeben, weitere Informationen in den anderen 16-Bit-Registern. Jede VBE Funktion liefert einen Wert in AX zurück, der Fehlerinformationen darstellt:

- 004Fh: Aufruf erfolgreich
- 014Fh: Fehler bei der Ausführung
- 024Fh: Funktion nicht unterstützt
- 034Fh: Funktion im aktuellen Grafikmodus nicht unterstützt

Der Funktionaufruf erfolgt über den Interrupt 0x10. Wenn durch irgendwelche Funktionen „FARPTR“ zurückgegeben werden, sind dies für den Real Mode immer DWORDs, im Segment:Offset-Format, im Protected Mode (nur bei der Verwendung des Protected-Mode-Interface) DWORDs im Selektor:Offset-Format (wobei ein 16-Bit-Selektor verwendet wird).

### Linear Frame Buffer

Grundsätzlich stellt VBE zwei Speichermodelle zur Verfügung, um auf den Grafikkartenspeicher zuzugreifen:

- **paged**: Der Speicher wird in mehrere sogenannte Fenster unterteilt, von denen immer nur eines in den Adressraum der CPU einblendet wird. Um den gesamten Grafikkartenspeicher zu adressieren, muss man zwischen den einzelnen Windows wechseln. Dieser Vorgang wird „Bank Switching“ genannt.
- **flat**: Der gesamte Grafikkartenspeicher wird als sogenannter „Linear Frame Buffer“ in den Adressraum der CPU eingeblendet.

Der LFB ist wohl eine der wichtigsten Neuerungen mit VBE 2.0. Mithilfe dieser Funktionalität kann man direkt auf den Grafikspeicher der Grafikkarte zugreifen und so viel schneller und einfacher Pixel zeichnen. Außerdem entfällt das lästige „Bank Switching“. Daher sollte man (und wird auch) einen Grafikmodus wählen, der den LFB unterstützt.

### Auf VBE-Unterstützung testen: 4F00h

Diese Funktion überprüft, ob die Grafikkarte VBE unterstützt und wenn ja, welche Version.

- AX = 4F00h
- ES:DI = Zeiger auf freien Speicher für den VBE Info Block (512 Bytes)

| Offset | Eintrag | Größe in Byte | Beschreibung |
| -------- | ---------------------------------------------------- | --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0 | Signatur | 4 | Hier sollte "VESA" stehen (=0x56455341) |
| 4 | Version | 2 | BCD-kodiert: 0x0100 für 1.0, 0x0200 für 2.0, 0x0300 für 3.0 |
| 6 | Zeiger auf OEMString | 4 (FARPTR) |  |
| 10 | Eigenschaften des Grafikcontrollers | 4 | • Bit 2: RAMDAC-Operation: 0=Normal; 1=Leeres Bit benutzen bei großen Blöcken<br>• Bit 1: 0=Controller ist VGA-kompatibel<br>• Bit 0: DAC-Breite: 0=6 Bits; 1=6 oder 8 Bits<br> |
| 14 | Zeiger auf eine Liste mit unterstützten Grafikmodi | 4 (FARPTR) | Diese Liste ist ein Array aus 16 Bit großen Einträgen, die jeweils die Nummer eines unterstützten Modus sind. Der letzte Eintrag ist 0xFFFF. |
| 18 | Größe des Grafikspeichers | 2 | Die Größe des Grafikspeichers in 64-kB-Blöcken |
| 20 | OEMSoftwareRevision | 2 |  |
| 22 | Zeiger auf OEMVendorNameString | 4 (FARPTR) |  |
| 26 | Zeiger auf OEMProductNameString | 4 (FARPTR) |  |
| 30 | Zeiger auf OEMProductRevision | 4 (FARPTR) |  |
| 34 | *reserviert* | 222 |  |
| 256 | Datenbereich für OEMStrings | 256 |  |

Vor dem Aufruf sollte das Feld „Signatur“ mit dem Wert „VBE2“ gefüllt werden.

### Unterstützte Grafikmodi suchen

In VBE 1.0 waren die Nummern der verschiedenen Grafikmodi noch vordefiniert:

| Modus | Auflösung (Breite×Höhe) | Farbtiefe (Bit) |
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

| Modus | Auflösung (Breite×Höhe) | Farbtiefe (Bit) |
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

Mit VBE 2.0 hat man sich allerdings dafür entschieden, dass die Grafikkartenherrsteller einfach nur eine Funktion bereitstellen, die alle von der Grafikkarte unterstützten Modi auflistet. Den Zeiger auf diese Liste erhält man mit dem VBE Info Block (4F00h). Diese Liste ist eigentlich nur ein WORD-Array, also eine Hintereinaderreihung von 16-Bit-Nummern. Diese repräsentieren die von der Grafikkarte unterstützten Grafikmodi. Die Liste wird terminiert durch den Eintrag 0xFFFF. Es wird empfohlen, sich nicht auf die o. g. Standardmodi zu verlassen, sondern durch Abfragen des Modeinfoblocks die Auflösung und anderen Eigenschaften der Modi aus der Modeliste herauszufinden.

### Informationen zu einem Grafikmodus: 4F01h

Man durchläuft also die obige Liste der unterstützten Modi und prüft dann mit folgender Funktion, welche Eigenschaften der entsprechende Grafikmodus besitzt:

- AX = 4F01h
- CX = Nummer des Grafikmodus
- ES:DI = Zeiger auf freien Speicher für den ModeInfoBlock (256 Bytes)

So kann man die Nummer desjenigen Grafikmodus herausfinden, den man benötigt.

| Offset | Eintrag | Größe in Byte | Beschreibung |
| -------- | ----------------------- | --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0 | ModeAttributes | 2 | • Bit 7: 0=kein LFB, 1=LFB verfügbar<br>• Bit 6: 0=kein VGA kompatibles Speichermodell, 1=VGA kompatibles Speichermodell verfügbar (=paged)<br>• Bit 5: 0=VGA kompatibler Modues, 1= nicht VGA kompatibel<br>• Bit 4: 0=Textmodus, 1=Grafikmodus<br>• Bit 3: 0=Monochrom, 1=farbig<br>• Bit 2: 0=TTY Ausgabe Funktionen werden nicht unterstuützt, 1=werden unterstützt<br>• Bit 1: Reserved (1)<br>• Bit 0: 0=Modus wird nicht unterstützt, 1=wird unterstützt<br> |
| 2 | WinAAttributes | 1 | • Bit 2: 0=Fenster nicht beschreibbar, 1=Fenster beschreibbar<br>• Bit 1: 0=Fenster lesbar, 1=nicht lesbar<br>• Bit 0: 0=Reallozierung der Fenster nicht möglich, 1=ist möglich<br> |
| 3 | WinBAttributes | 1 | *siehe WinAAttributes* |
| 4 | WinGranularity | 2 | in kB |
| 6 | WinSize | 2 | Fenstergröße in kB |
| 8 | WinASegment | 2 | Startsegment des A-Fensters (Real-Mode-Segment) |
| 10 | WinBSegment | 2 | Startsegment des B-Fensters (Real-Mode-Segment) |
| 12 | WinFuncPtr | 4 (FARPTR) | Zeiger auf die „Window Function“ |
| 16 | BytesPerScanLine | 2 | Anzahl der Bytes pro Zeile |
| 18 | XResolution | 2 | Horizontale Auflösung |
| 20 | YResolution | 2 | Vertikale Auflösung |
| 22 | XCharSize | 1 | Breite eines Buchstabens (Textmodus) |
| 23 | YCharSize | 1 | Höhe eines Buchstabens (Textmodues) |
| 24 | NumberOfPlanes | 1 |  |
| 25 | BitsPerPixel | 1 | Bits pro Pixel (=Farbtiefe) |
| 26 | NumberOfBanks | 1 |  |
| 27 | Speichermodell | 1 | • 00h = Text mode<br>• 01h = CGA graphics<br>• 02h = Hercules graphics<br>• 03h = Planar<br>• 04h = Packed pixel<br>• 05h = Non-chain 4, 256 color<br>• 06h = Direct color<br>• 07h = YUV<br> |
| 28 | BankSize | 1 | in kB |
| 29 | NumberOfImagePages | 1 | Anzahl der Images - 1 |
| 30 | Reserviert | 1 | =1 |
| 31 | RedMaskSize | 1 | Anzahl der Bits, die den roten Farbanteil angeben (Speichermodell: direct color) |
| 32 | RedFieldPosition | 1 | Position des ersten Bits ([LSB](Bin%C3%A4re-Datentypen.md#msb-und-lsb "LSB")), das den roten Farbanteil angibt |
| 33 | GreenMaskSize | 1 |  |
| 34 | GreenFieldPosition | 1 |  |
| 35 | BlueMaskSize | 1 |  |
| 36 | BlueFieldPosition | 1 |  |
| 37 | RsvdMaskSize | 1 |  |
| 38 | RsvdFieldPosition | 1 |  |
| 39 | DirectColorModeInfo | 1 | • Bit 1: 0=Alle reservierten Bits in der Farbmaske dürfen *nicht* benutzt werden, 1=dürfen benutzt werden<br>• Bit 0: 0=Color-Ramp des DAC ist fest, 1=einstellbar<br> |
| 40 | PhysBasePtr | 4 | Physische Adresse des LFB |
| 44 | OffScreenMemOffset | 4 | Zeiger auf den Anfang des Teil des Grafikspeichers, der nicht auf dem Bildschirm zu sehen ist |
| 48 | OffScreenMemSize | 2 | in kB |
| 50 | LinBytesPerScanLine | 2 | Bytes pro Zeile im LFB-Modus |
| 52 | BnkNumberOfImagePages | 1 |  |
| 53 | LinNumberOfImagePages | 1 |  |
| 54 | LinRedMaskSize | 1 | Anzahl der Bits, die den roten Farbanteil im LFB-Modus angeben (Speichermodell: direct color) |
| 55 | LinRedFieldPosition | 1 | Position des ersten Bits, das den roten Farbanteil im LFB-Modus angibt |
| 56 | LinGreenMaskSize | 1 |  |
| 57 | LinGreenFieldPosition | 1 |  |
| 58 | LinBlueMaskSize | 1 |  |
| 59 | LinBlueFieldPosition | 1 |  |
| 60 | LinRsvdMaskSize | 1 |  |
| 61 | LinRsvdFieldPosition | 1 |  |
| 62 | MaxPixelClock | 4 |  |
| 66 | Reserviert | 190 |  |

Die Felder ab LinBytesPerScanLine (also Offset 50) sind erst in VBE 3.0 definiert.

Von diesen Einträgen sind einige besonders wichtig:

- In grün: Diese Einträge sind für die Verwendung des [LFB](VESA-BIOS-Extensions.md#linear-frame-buffer "LFB") wichtig.
- In rot: Diese Einträge sind zum Adressieren/Zeichnen eines Pixels wichtig.
- In blau: Diese Einträge zeigen an, wie die Farbe eines Pixels anzugeben ist. Dies ist in der Regel eine RGB-Angabe. Dafür muss das Speichermodell (27) *direct color* sein (=6h).

### In einen Grafikmodus umschalten: 4F02h

Nachdem man nun die gewünschte Grafikmodusnummer hat, muss man nur noch in diesen umschalten:

- AX = 4F02h
- BX = VBE-Grafikmodus:
  - Bits 0 – 8: Modusnummer
  - Bits 9 – 13: reserviert, Null setzen
  - Bit 14: Speichermodell: 0=Windowed (paged); 1=Linear (flat)
  - Bit 15: Löscht den Grafikspeicher, wenn gelöscht (VBE 3.0 garantiert nicht, das die Grafikkarte dies unterstützt)

## VBE im Protected Mode

Diese Seite oder Abschnitt ist zwar komplett, es wird aber folgende Verbesserungen gewünscht:  

*Tatsächlich beschreiben (wobei man es eigentlich nie braucht)*

Hilf Lowlevel, den Artikel zu verbessern.

  
Mit VBE 2.0 wurde das sogenannte „Protected-Mode-Interface“ eingeführt. Das sind Funktionen, die die Grafikkarte zur Verfügung stellt und die im Gegensatz zu den anderen Funktionen in 16/32-Bit-Protected-Mode-Code vorliegen. Die Adresse dieser Funktionen erhält man mit folgendem Aufruf, der allerdings immer noch im Real Mode stattfinden muss:

- AX = 4F0Ah
- BL = 00h

Diese Funktion liefert folgende Werte zurück:

- ES:DI=Zeiger auf eine Tabelle des unten stehenden Formats
- CX=Länge der Tabelle

| Offset | Eintrag |
| -------- | --------------------------------------------------------------------------- |
| 0 | Offset der „SetWindow“-Funktion |
| 2 | Offset der „SetDisplayStart“-Funktion |
| 4 | Offset der „SetPaletteData“-Funktion |
| 6 | Offset auf eine Liste aller Ports und Adressen, auf die der Code zugreift |
| 8 | Code und Daten |

## Pixel zeichnen

### Im Protected Mode

Um im Protected Mode Pixel zu zeichnen, muss man in den Grafikspeicher schreiben. Hier zeigt sich auch der Vorteil des LFB: er ist im PM viel einfacher und schneller zu handhaben! Wenn man also mithilfe des LFB Zugriff auf den Grafikspeicher hat, dann zeichnet man ein Pixel folgendermaßen: \<c\> uint8_t\* lfb = (uint8_t\*) (uintptr_t) vbe_mode_info.phys_base_ptr; void draw_pixel(unsigned int x, unsigned int y, unsigned int color) {

     *(uint32_t *)(lfb + y * vbe_mode_info.bytes_per_scan_line + x * 4) = color;

} \</c\>

(Funktioniert nur, wenn die Farbtiefe 32 Bits pro Pixel beträgt, bei VBE 3.0 lin_bytes_per_scan_line gleich bytes_per_scan_line ist und der LFB virtuell an der gleichen Stelle wie physisch liegt)

Wenn man allerdings das Paged-Modell verwendet, muss man erst den entsprechenden Teil des Grafikspeichers in den Adressraum blenden mithilfe des „Bank Switch“.

### im Real Mode

Im Real Mode kann man die obige Variante theoretisch auch verwenden, wenn der Grafikspeicher sich nicht oberhalb der 1-MB-Marke im Adressraum befindet (sonst wird mindestens der Unreal Mode benötigt).

## VBE 3.0

VBE 3.0 bietet nicht viele neue Funktionen an. Eine der wichtigsten ist die Unterstützung für Triple Buffering, für die zwei neue Funktionen eingeführt wurden:

ScheduleDisplayStart:

- AX=4f07h
- BL=0
- BH=2
- ECX=Offset des ersten Pixels im [LFB](VESA-BIOS-Extensions.md#linear-frame-buffer "LFB")

GetDisplayStartStatus:

- AX=4f07h
- BL=0
- BH=4
- liefert AX!=0, wenn das Bild im Buffer, der mit *ScheduleDisplayStart* gewählt wurde, auf dem Bildschirm abgebildet wurde.

  
Diese beiden Funktionen kann man natürlich auch für [Double Buffering](Double-Buffering.md "Double Buffering") verwenden:

- Den ersten Buffer rendern
- Ihn mit *ScheduleDisplayStart* auswählen
- Während der erste Buffer auf dem Bildschirm erscheint, den zweiten rendern
- Mit *GetDisplayStatus* darauf warten, dass der erste Buffer komplett auf dem Bildchirm gezeichnet wurde
- Den zweiten Buffer mit *ScheduleDisplayStart* auswählen
- Das Bild wieder im ersten Buffer rendern
- Mit *GetDisplayStatus* darauf warten, dass der zweite Buffer komplett auf dem Bildchirm gezeichnet wurde
- Den ersten Buffer mit *ScheduleDisplayStart* auswählen
- usw.

[Double Buffering](Double-Buffering.md "Double Buffering") wäre auch schon mit VBE 2.0 möglich (siehe Funktion: 4F07h, 80h – Set Display Start During Vertical Retrace). Allerdings ist müsste man hier direkt auf die Grafikkarte zugreifen, um das Timing hinzukriegen.

## Weblinks

- <http://www.phatcode.net/res/221/files/vbe20.pdf> – VBE Spezifikation 2.0
- <http://www.petesqbsite.com/sections/tutorials/tuts/vbe3.pdf> – VBE Spezifikation Version 3.0

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/11461/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2303/index.html)

<!-- MediaWiki page 2303; revision 11461; parent 10649; 2020-08-02T22:28:32Z -->
