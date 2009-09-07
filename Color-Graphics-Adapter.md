# Color Graphics Adapter

Der **Color Graphics Adapter** (**CGA**) ist die ursprüngliche Grafikkarte, die den 80x25 Textmodus eingeführt hat. In diesem Modus können ausschließlich Zeichen, die auf einem Raster vom Format 80x25 angeordnet sind, dargestellt werden. Jedes Zeichen kann in einer von 16 Farben dargestellt werden, sowie mit einer von 8 Hintergrundfarben hinterlegt werden und optional blinken. Die Anzahl der Hintergrundfarben kann auch auf 16 erweitert werden, allerdings können dann die Zeichen nicht mehr blinken.

## Videospeicher

Im 80x25 Textmodus (16 Farben) wird der Speicher ab Adresse 0xB8000 als Puffer verwendet. In diesem Speicher liegen für jedes Zeichen abwechselnd jeweils ein Byte mit dem Index in die Font Table (in der Regel der ASCII-Code des Zeichens) und ein Attribut-Byte. Das heißt jedes Zeichen belegt zwei Bytes im Videospeicher.

### Aufbau das Attribut-Bytes

<table>
<tbody><tr>
<th><b>Bit</b>
</th>
<th>7
</th>
<th>6
</th>
<th>5
</th>
<th>4
</th>
<th>3
</th>
<th>2
</th>
<th>1
</th>
<th>0
</th></tr>
<tr>
<td><b>Bedeutung</b></td>
<td>Blinken</td>
<td colspan="3">Hintergrundfarbe</td>
<td colspan="4">Vordergrundfarbe
</td></tr></tbody></table>

- Ist das Bit 7 gesetzt, so blinkt das Zeichen.
- Die Hintergrundfarbe setzt den Hintergrund des Zeichens auf eine der ersten 8 CGA-Farben. (Siehe unten für 16 Hintergrundfarben.)
- Die Vordergrundfarbe setzt die Farbe des Zeichens auf eine der 16 CGA-Farben.

Farben der Standard-CGA-Palette in der englischen Wikipedia: [\[1\]](http://en.wikipedia.org/wiki/List_of_8-bit_computer_hardware_palettes#CGA)

### Regen Buffer

Der Videospeicher wird auch als Regen Buffer (von engl. *regenerate*) bezeichnet. Er war ursprünglich 16 KiB groß und ging von 0xB8000 bis 0xBC000, bei neueren Grafikkarten (relativ zum CGA) ist er 32 KiB groß und geht bis 0xC0000. Im Folgenden gehen wir davon aus, dass der Puffer 32 KiB groß ist, denn einen originalen IBM PC hat vermutlich keiner mehr rumstehen.

Aus dem Regen Buffer liest die Grafikkarte die Zeichencodes sowie die Attribute aus, und erstellt daraus die Signale für den Monitor. Die Bezeichnung *regenerate* zeigt an, dass die Grafikkarte nicht direkt die Buchstaben an den Monitor sendet, sondern das Videosignal bestehend aus den Farbinformationen der Pixel für jedes Bild neu generiert.

In der 80x25 Auflösung können 80\*25 Zeichen dargestellt werden, von denen jedes 2 Bytes belegt. Das heißt es werden 80\*25\*2 = 4000 Bytes verwendet. In dem Regen Buffer wären also für insgesamt 8 Bildschirmseiten (32 KiB/4000) Platz. Standardmäßig werden (nach dem Systemstart) die ersten 4000 Bytes an Adresse 0xB8000 zur Darstellung verwendet. Man kann allerdings dieses Fenster verschieben indem man den Grafikadapter anweist eine andere Startadresse zu nehmen. (Siehe [Interne Register](#interne-register) weiter unten.)

Für die 8 Bildschirmseiten verwendet das BIOS Startadressen, die jeweils Vielfache von 0x4000 (4KiB) sind. Allerdings ist man weder daran gebunden, noch muss man dieses Konzept von 8 getrennten Bildschirmseiten beibehalten (sofern man das BIOS vollständig umgeht). Man kann z.B. durch Verschieben der Startadresse in 80er-Schritten ein Scrollen ohne externen Speichern realisieren.

## I/O Ports

Die I/O Ports 0x3D0 bis 0x3DC sind für den CGA reserviert. Die Ports sind jeweils ein Byte groß.

### Interne Register

Der Motorola 6845 CRT Controllers hat interne Register, die verschiedene Aspekte der Darstellung kontrollieren. Sie werden über die Ports 0x3D4 und 0x3D5 angesteuert. Das Laden eines Registers erfolgt, indem der Index des Registers an den Port 0x3D4 geschrieben wird, und dann die Daten nach Port 0x3D5 geschrieben werden.

Die folgende Tabelle listet alle zur Verfügung stehenden Register auf:

| Index | Register Typ | Einheit |
| ------- | ---------------------------- | --------------- |
| 0 | Horizontal Total | Character |
| 1 | Horizontal Displayed | Character |
| 2 | Horizontal Sync Position | Character |
| 3 | Horizontal Sync Width | Character |
| 4 | Vertical Total | Character Row |
| 5 | Vertical Total Adjust | Scan Line |
| 6 | Vertical Displayed | Character Row |
| 7 | Vertical Sync Position | Character Row |
| 8 | Interlace Mode | \- |
| 9 | Maximum Scan Line Address | Scan Line |
| 10 | Cursor Start | Scan Line |
| 11 | Cursor End | Scan Line |
| 12 | Start Address (High Byte) | Offset |
| 13 | Start Address (Low Byte) | Offset |
| 14 | Cursor Address (High Byte) | Offset |
| 15 | Cursor Address (Low Byte) | Offset |
| 16 | Light Pen (High Byte) | ? |
| 17 | Light Pen (Low Byte) | ? |

### 16 Hintergrundfarben

Um 16 Hintergrundfarben zu nutzen, muss das Bit 5 im Mode-Select Register (Port 0x3D8) gelöscht werden. Dadurch bedeutet das Bit 7 im Attribut-Feld nicht mehr, dass das Zeichen blinken soll. Das Feld für die Hintergrundfarbe erweitert sich dann auf die Bits 4 bis 7, und es können somit 16 Hintergrundfarben dargestellt werden. Diese Farben stammen aus der selben Palette wie die Vordergrundfarben.

### Vertical Sync

Bit 3 des Status Registers (Port 0x3DA) wird von der Grafikkarte genau dann gesetzt, wenn der Monitor sich im Vertical Retrace Mode befindet. Das heißt dann ist der Elektronenstrahl gerade deaktiviert und wird wieder von unten nach oben bewegt, um ein weiteres Bild darzustellen. Dieses Bit ist besonders bei der Darstellung von Grafikmodi z.B. in Spielen oder graphischen Oberflächen interessant. Wenn man darauf wartet, dass dieses Bit gesetzt ist, bevor man beginnt in den Grafikspeicher zu schreiben, verhindert man, dass der Monitor mitten in der Darstellung eines Bildes andere Daten vorgesetzt bekommt. Dadurch lässt sich verhindern, dass das Bild bei horizontalen Bewegungen zerissen erscheint. Der Code dafür könnte z.B. so aussehen: \<c\>// Direkt vor dem Zeichnen aufrufen // (besser: direkt vor dem Kopieren des Double Buffers) void vsync() {

       do {} while (inb(0x3DA) & 8) != 0); // warten, wenn der vsync bereits läuft
       do {} while (inb(0x3DA) & 8) == 0); // warten während der Monitor darstellt

}\</c\>

## Textausgabe

Die Ausgabe von Text erfolgt entweder über die [BIOS](https://github.com/lowlevel-eu/wiki/wiki/Basic-Input-Output-System "BIOS")-Funktionen (z.B. Int 0x10/AH=0x0E), oder über das direkte Schreiben in den Videospeicher. Dies ist im Artikel [Textausgabe](https://github.com/lowlevel-eu/wiki/wiki/Textausgabe "Textausgabe") genauer beschrieben.

## Palette

Die Farben des Textmodus können mit Hilfe der Palette der [VGA](https://github.com/lowlevel-eu/wiki/wiki/Video-Graphics-Array "VGA")-Karten verändert werden. Das Setzen der RGB-Werte funktioniert wie im VGA Modus über die Register 0x3C8 und 0x3C9. Die Farben des CGA-Modus sind allerdings nicht linear im Farbraum der VGA-Modi angeordnet.

| CGA Index | VGA Paletten Index |
| ----------- | -------------------- |
| 0 | 0 |
| 1 | 1 |
| 2 | 2 |
| 3 | 3 |
| 4 | 4 |
| 5 | 5 |
| 6 | 20 |
| 7 | 7 |
| 8 | 55 |
| 9 | 56 |
| 10 | 57 |
| 11 | 58 |
| 12 | 59 |
| 13 | 60 |
| 14 | 61 |
| 15 | 62 |

## Siehe auch

- IBM PC Technical Reference (z.B. unter [\[2\]](http://www.retroarchive.org/dos/docs/index.html))
- [Artikel in der englischen Wikipedia](http://en.wikipedia.org/wiki/Color_Graphics_Adapter)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/5855/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1890/index.html)

<!-- MediaWiki page 1890; revision 5855; parent 5854; 2009-09-07T11:23:54Z -->
