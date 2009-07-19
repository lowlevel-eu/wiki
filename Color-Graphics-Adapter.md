# Color Graphics Adapter

Der **Color Graphics Adapter** (**CGA**) ist die ursprüngliche Grafikkarte, die den 80x25 Textmodus eingeführt hat. In diesem Modus können ausschließlich Zeichen, die auf einem Raster vom Format 80x25 angeordnet sind, dargestellt werden. Die Zeichen können in 16 Farben dargestellt werden, und mit 8 verschiedenen Hintergrundfarben hinterlegt werden und blinken. Die Zeichen können auch mit verschiedenen 16 Hintergrundfarben dargestellt werden, aber dann nicht mehr blinken.

## Videospeicher

Im 80x25 Textmodus (16 Farben) wird der Speicher ab Adresse 0xB8000 als Puffer verwendet. In diesem Speicher liegen für jedes Zeichen abwechselnd jeweils ein Byte mit dem Index in die Font Table (in der Regel der ASCII-Code des Zeichens) und ein Attribut-Byte.

### Aufbau das Attribut-Bytes

<table>
<tbody><tr>
<td><b>Bit</b></td>
<td>7</td>
<td>6</td>
<td>5</td>
<td>4</td>
<td>3</td>
<td>2</td>
<td>1</td>
<td>0
</td></tr>
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

## I/O Ports

Die I/O Ports 0x3D0 bis 0x3DC sind für den CGA reserviert. Die Ports sind jeweils ein Byte groß.

### Bewegen des Cursors

Der Cursor wird über 2 der Register des Motorola 6845 CRT Controllers, der im ursprünglichen CGA verbaut war, angesteuert. Diese Register Befinden werden über die Ports 0x3D4 und 0x3D5 angesprochen. Dies ist im Artikel [Textausgabe](https://github.com/lowlevel-eu/wiki/wiki/Textausgabe#cursor "Textausgabe") genauer beschrieben.

### 16 Hintergrundfarben

Um 16 Hintergrundfarben zu nutzen, muss das Bit 5 im Mode-Select Register (Port 0x3D8) gelöscht werden. Dadurch bedeutet das Bit 7 im Attribut-Feld nicht mehr, dass das Zeichen blinken soll. Das Feld für die Hintergrundfarbe erweitert sich dann auf die Bits 4 bis 7, und es können somit 16 Hintergrundfarben dargestellt werden. Diese Farben stammen aus der selben Palette wie die Vordergrundfarben.

### Vertical Sync

Bit 3 des Status Registers (Port 0x3DA) wird von der Grafikkarte genau dann gesetzt, wenn der Monitor sich im Vertical Retrace Mode befindet. Das heißt dann ist der Elektronenstrahl gerade deaktiviert und wird vom unten wieder nach oben bewegt, um ein weiteres Bild darzustellen. Dieses Bit ist besonders bei der Darstellung von Grafikmodi z.B. in Spielen oder graphischen Oberflächen interessant. Wenn man darauf wartet, dass dieses Bit gesetzt ist, bevor man beginnt in den Grafikspeicher zu schreiben, verhindert man, dass der Monitor mitten in der Darstellung eines Bildes andere Daten vorgesetzt bekommt. Dadurch lässt sich verhindern, dass das Bild in der Mitte des Monitor zerissen erscheint. Der Code dafür könnte z.B. so aussehen: \<c\>// Direkt vor dem Zeichnen aufrufen // (besser: direkt vor dem Kopieren des Double Buffers) void vsync() {

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

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/4674/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1890/index.html)

<!-- MediaWiki page 1890; revision 4674; parent 0; 2009-07-19T01:10:39Z -->
