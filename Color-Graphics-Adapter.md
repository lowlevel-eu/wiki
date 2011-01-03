# Color Graphics Adapter

Der **Color Graphics Adapter** (**CGA**) ist die Grafikkarte, die den 80x25 Textmodus eingeführt hat. In diesem Modus können ausschließlich Zeichen auf einem Raster vom Format 80x25 dargestellt werden. Jedes Zeichen kann in einer von 16 Farben dargestellt werden, sowie mit einer von 8 Hintergrundfarben hinterlegt werden und optional blinken. Die Anzahl der Hintergrundfarben kann auch auf 16 erweitert werden, allerdings können dann die Zeichen nicht mehr blinken.

## Videospeicher

Im 80x25 Textmodus (16 Farben) wird der Speicher ab Adresse 0xB8000 als Puffer verwendet. In diesem Speicher liegen für jedes Zeichen abwechselnd jeweils ein Byte mit dem Index in die Font Table (in der Regel der ASCII-Code des Zeichens) und ein Attribut-Byte. Das heißt jedes Zeichen belegt zwei Bytes im Videospeicher.

### Aufbau des Attribut-Bytes

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

Aus dem Regen Buffer liest die Grafikkarte die Zeichencodes sowie die Attribute aus, und erstellt daraus die Signale für den Monitor. Die Bezeichnung *regenerate* zeigt an, dass die Grafikkarte nicht direkt die Buchstaben an den Monitor sendet, sondern das Videosignal anhand des Regen Buffers und der Font Table generiert.

In der 80x25 Auflösung können 80\*25 Zeichen dargestellt werden, von denen jedes 2 Bytes belegt. Das heißt es werden 80\*25\*2 = 4000 Bytes verwendet. In dem Regen Buffer wären also für insgesamt 8 Bildschirmseiten (= 32 KiB/4000) Platz. Standardmäßig werden (nach dem Systemstart) die ersten 4000 Bytes an Adresse 0xB8000 zur Darstellung verwendet. Man kann allerdings dieses Fenster verschieben indem man den Grafikadapter anweist eine andere Startadresse zu nehmen. (Siehe [Interne Register](#interne-register) weiter unten.)

Für die 8 Bildschirmseiten verwendet das BIOS Startadressen, die jeweils Vielfache von 0x1000 (4 KiB) sind. Allerdings ist man weder daran gebunden, noch muss man dieses Konzept von 8 getrennten Bildschirmseiten beibehalten (sofern man das BIOS vollständig umgeht). Man kann z.B. durch Verschieben der Startadresse in 80er-Schritten ein Hardware Scrolling realisieren.

## I/O Ports

Die [I/O Ports](https://github.com/lowlevel-eu/wiki/wiki/I-O-Ports "I/O Ports") 0x3D0 bis 0x3DC sind für den CGA reserviert. Die Ports sind jeweils ein Byte groß.

### Interne Register

Der Motorola 6845 CRT Controller hat 18 interne Register, die verschiedene Aspekte der Darstellung kontrollieren. Sie werden über die Ports 0x3D4 und 0x3D5 angesteuert. Das Laden eines Registers erfolgt, indem der Index des Registers an den Port 0x3D4 geschrieben wird, und dann die Daten nach Port 0x3D5 geschrieben werden.

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

Die ersten 10 Register (0-9) steuern das Timing des CRT-Displays, sowie weitere Details der Darstellung, die über den Zweck dieses Artikels hinausgehen. Informationen dazu gibt es im Datenblatt des 6845 z.B. unter [\[2\]](http://bbc.nvg.org/doc/datasheets/MC6845.zip).

Nur die Register 14 bis 17 können laut Spezifikation ausgelesen werden. Deswegen ist es notwendig die Werte der anderen Register in einer Variable zu speichern, wenn man ihre Werte benötigt. Das BIOS nutzt dafür zum Beispiel Teile der [BIOS Data Area](https://github.com/lowlevel-eu/wiki/wiki/BIOS-Data-Area#grafik-adapter-informationen "BIOS Data Area").

#### Cursor Format

Die Register 10 und 11 steuern die Form des Cursors. Die unteren 5 Bits dieser Register geben jeweils die Start- und End-Scanline des Cursors innerhalb eines Zeichens an. Außerdem steuern Bits 5 und 6 des Registers 10 das Blinken des Cursors.

<table>
<tbody><tr>
<th>Register
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
<td><b>Cursor Start</b></td>
<td>n/a</td>
<td>Enable</td>
<td>Timing
</td>
<td colspan="5">Scanline
</td></tr>
<tr>
<td><b>Cursor End</b>
</td>
<td colspan="3">n/a
</td>
<td colspan="5">Scanline
</td></tr></tbody></table>

Die folgende Tabelle listet alle möglichen Belegungen von Enable und Timing auf:

| Enable | Timing | Effekt |
| -------- | -------- | ------------------------------- |
| 0 | 0 | Cursor blinkt nicht |
| 0 | 1 | Cursor wird nicht dargestellt |
| 1 | 0 | Cursor blinkt normal |
| 1 | 1 | Cursor blinkt schnell |

#### Start Address

Die Register 12 und 13 geben das Offset an, an dem das erste darzustellende Zeichen auf dem Bildschirm, also das Zeichen oben links, steht. Dabei ist zu beachten, dass die Berechnung des Offsets wie die Berechnung der Cursorposition (siehe unten) verläuft. Das heißt das Offset darf nicht mit 2 multipliziert werden, um die Attribute einzubeziehen.

Beispiel, das analog zum BIOS den Speicher in 8 Seiten unterteilt: \<cpp\>/\* Unsere Auflösung \*/

1.  define ROWS 25
2.  define COLS 80

/\*

    * DISPLAY_PAGE_OFFSET gibt die Startadresse der übergebenen Seitennummer 
    * zurück. Dabei rundet es die Adresse einer Bildschirmseite auf das 
    * nächste Vielfache von 256 auf. Das Makro ist etwas komplizierter als nötig, 
    * falls es jemand mit anderen Auflösungen verwenden will. Für den 80x25-
    * Modus vereinfacht es sich zu ((page) * 2048). 
    */

1.  define DISPLAY_PAGE_OFFSET(page) ((page) \* ((ROWS \* COLS + 0xff) & 0xff00))

/\* Die Startadresse der dargestellten Seite \*/ unsigned short start_address;

void select_page(unsigned int page) {

       start_address = DISPLAY_PAGE_OFFSET(page);

       outb(0x3D4, 13);
       outb(0x3D5, start_address & 0xff); // Low Byte schreiben
       outb(0x3D4, 12);
       outb(0x3D5, (start_address >> 8) & 0xff); // High Byte schreiben

       /* 
        * Hier muss noch die Cursorposition gesetzt werden, da diese für 
        * jede Page eine andere ist. Das heißt sie muss z.B. in einem Array 
        * gespeichert werden, wenn man mehrere Pages verwalten möchte.
        *
        * Das Setzen des Cursors wird im nächsten Abschnitt erläutert.
        */

}\</cpp\>

#### Cursor Address

Die Register 14 und 15 setzen die Cursor-Adresse, die sich aus der Cursor-Position berechnet. Um den Cursor zum Beispiel in die Zeile 10 und Spalte 63 zu setzen, muss man 10 \* 80 + 63 = 863 rechnen. Dieser Wert wird dann in die High- und Low-Bytes der Register für die Cursor Adresse geschrieben.

Dabei ist zu beachten, dass wenn man wie im letzten Abschnitt beschrieben die Startadresse verändert, diese Startadresse auf die Cursor-Adresse addieren muss.

Beispiel: \<cpp\>/\* Unsere Auflösung \*/

1.  define ROWS 25
2.  define COLS 80

/\* Cursor-Position, die durch die Ausgabefunktionen gesetzt werden \*/ unsigned int cursor_x; unsigned int cursor_y;

void update_cursor() {

       unsigned short cursor_address = cursor_x + cursor_y * COLS;

       // die Startadresse dazuaddieren (nur nötig, wenn man diese auch verändert hat)
       cursor_address += start_address; 

       outb(0x3D4, 15);
       outb(0x3D5, cursor_address & 0xff);
       outb(0x3D4, 14);
       outb(0x3D5, (cursor_address >> 8) & 0xff);

}\</cpp\>

### 16 Hintergrundfarben

Um 16 Hintergrundfarben zu nutzen, muss das Bit 5 im Mode-Select Register (Port 0x3D8) gelöscht werden. Dadurch bedeutet das Bit 7 im Attribut-Feld nicht mehr, dass das Zeichen blinken soll. Das Feld für die Hintergrundfarbe erweitert sich dann auf die Bits 4 bis 7, und es können somit 16 Hintergrundfarben dargestellt werden. Diese Farben stammen aus der selben Palette wie die Vordergrundfarben.

### Vertical Sync

Bit 3 des Status Registers (Port 0x3DA) wird von der Grafikkarte genau dann gesetzt, wenn der Monitor sich im Vertical Retrace Mode befindet. Das heißt dann ist der Elektronenstrahl gerade deaktiviert und wird wieder von unten nach oben bewegt, um ein weiteres Bild darzustellen. Dieses Bit ist besonders bei der Darstellung von Grafikmodi z.B. in Spielen oder graphischen Oberflächen interessant. Wenn man darauf wartet, dass dieses Bit gesetzt ist, bevor man beginnt in den Grafikspeicher zu schreiben, verhindert man, dass der Monitor mitten in der Darstellung eines Bildes andere Daten vorgesetzt bekommt. Dadurch lässt sich verhindern, dass das Bild bei horizontalen Bewegungen zerissen erscheint. Der Code dafür könnte z.B. so aussehen: \<cpp\>// Direkt vor dem Zeichnen aufrufen // (besser: direkt vor dem Kopieren des Double Buffers) void vsync() {

       do {} while (inb(0x3DA) & 8) != 0); // warten, wenn der vsync bereits läuft
       do {} while (inb(0x3DA) & 8) == 0); // warten während der Monitor darstellt

}\</cpp\>

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

- IBM PC Technical Reference (z.B. unter [\[3\]](http://www.retroarchive.org/dos/docs/index.html))
- [Artikel in der englischen Wikipedia](http://en.wikipedia.org/wiki/Color_Graphics_Adapter)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/9241/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1890/index.html)

<!-- MediaWiki page 1890; revision 9241; parent 7692; 2011-01-03T17:26:41Z -->
