# Textausgabe

## Vorwort

In diesem Artikel geht es nur darum wie im Textmode Schrift (und nur Schrift, keine Grafiken) auf dem Bildschirm ausgegeben werden kann. Normalerweise geht das über einen BIOS-Interrupt, aber man will ja auch im Protected Mode Text auf dem Bildschirm schreiben können.

## Textspeicher

Zur Ausgabe von Text gibt es einen 4kB großen Speicher an der Adresse 0xB8000. Dieser Speicher kann linear angesprochen werden und benutzt 2 Byte pro Zeichen auf dem Bildschirm. Es gibt also 80 Spalten (Zeichen pro Zeile) und 25 Zeilen.

## Schreiben in den Textspeicher

Um nun auf dem Bildschirm ein Zeichen zu haben, muss man erstmal das Offset ausrechnen, an dem das Zeichen steht. Da der Speicher linear ist geht das auch mit einer linearen Gleichung: o = z\*80+s Wobei hier o das Offset ist, z die Zeile und s die Spalte. Wenn man in Mathe aufgepasst hat, sollte das kein Problem sein.

Nun war die Rede, dass 2 Bytes pro Zeichen verwendet werden. Also woher kommt das 2. Byte? Ganz einfach: In dem 2. Byte wird das Attribut, also eigentlich nur die Farbe gespeichert. Im ersten wird einfach nur das Zeichen gespeichert. Als Code wird [Codepage 437](http://de.wikipedia.org/wiki/Codepage_437) verwendet, welche nichts anderes als [7bit-ASCII](http://de.wikipedia.org/wiki/ASCII) plus noch ein paar Zeichen Erweiterung, ist.

## Attribut-Byte

Das Attribute-Byte ist wie folgt gestaltet:

0xXY, Hierbei ist X die Hintergrundfarbe und Y die Vordergrundfarbe. Hier ist eine Tabelle aller Farben:

|  |  |  |  |
| ------ | ---------- | ------ | ------------- |
| Wert | Farbe | Wert | Farbe |
| 0x0 | Schwarz | 0x8 | Dunkelgrau |
| 0x1 | Blau | 0x9 | Hellblau |
| 0x2 | Grün | 0xA | Hellgrün |
| 0x3 | Cyan | 0xB | Hellcyan |
| 0x4 | Rot | 0xC | Hellrot |
| 0x5 | Magenta | 0xD | Hellmagenta |
| 0x6 | Braun | 0xE | Hellbraun |
| 0x7 | Hellgrau | 0xF | Weiß |

Nebenbei bemerkt: Die Standardfarbe ist 0x07. Also Hellgrau auf Schwarz.

## Beispiel

Hier ein kleines Beispiel einer Funktion, die ein Zeichen (chr), in der Farbe color auf den Bildschirm, an die Position x,y schreiben soll. Hierbei werden Steuerzeichen nicht beachtet, bzw. als normales Zeichen auch ausgegeben (siehe [Codepage 437](http://de.wikipedia.org/wiki/Codepage_437)).

\<c\>

    void printchar(u8 chr,u8 color,u8 x,u8 y) {
      u16 *off = (u16*)0xB8000;
      // berechnen der Adresse
      off += y*80+x;
      // setzen des zeichens + attributebyte
      *off = (((u16)color)<<8)|chr;
    }

\</c\>

Nun folgt die Erklärung: Mit der 1. Zeile wird ein Pointer auf den Textspeicher erzeugt. Der Dateityp ist u16, also 2byte, damit wir das Zeichen und das Attributebyte gleichzeitig schreiben können (geht einfach schneller). Nun wird die Adresse ausgerechnet, mit der oben genannten Formel. Hätten wird vorhin u8 benutzt müssten wir jetzt noch mit 2 multiplizieren, da ja jedes Zeichen 2 Byte benutzt. Das Setzen des Zeichens machen wir, indem wir einfach das Attribute auf 16 Bit erweitern, dann eine Linksverschiebung von 8 Bit vornehmen und per logischen Oder mit dem Zeichenbyte verknüpfen.

Achtung: Das Attributebyte kommt zwar immer nach dem Zeichenbyte, aber wir benutzen hier ein Word und arbeiten ja auf einem [Little-Endian](http://de.wikipedia.org/wiki/Byte-Reihenfolge)-System)

Nochmal eine Veranschaulichung der Oder-Verknüpfung:

    attr     char
    0x07     0x41
    <<8       "
    0x0700 | 0x41 = 0x0741

## Bildschirm scrollen

Um den Bildschirm zu scrollen muss man einfach den ganzen Textspeicher ab der 2. Zeile zur 1. Zeile kopieren und die letzte Zeile löschen, also auf 0 oder irgendwas setzen. Wenn man eine memcpy- und eine memset-Funktion hat, geht das in ein paar Zeilen.

## Cursor

Manchen wird schon aufgefallen sein, dass auf dem Bildschirm ein Unterstrich ist, wo keiner sein sollte. Also zumindestens wo keiner im Textspeicher ist. Das ist der Bildschirmcursor, der von BIOS zur Verfügung gestellt wird. Ich will nicht lange darauf eingehen, ich stelle nur eine Funktion zum Verschieben und zum "Löschen" des Cursors zur Verfügung. Ich selber benutze ihn nicht, da das Verschieben des Cursors wirklich lahm geht (["Keep in mind that in/out to VGA Hardware is a slow operation"](http://www.osdev.org/wiki/Text_Mode_Cursor)), es ist aber jeden seine eigene Entscheidung.

Hier eine Funktion zum Verschieben des Cursors (dies kann auch mit Int 0x10,0x02 gemacht werden)

\<c\>

    void displaycursor(u8 col,u8 row) {
      u16 tmp;
      tmp = row*VIDEOTEXT_WIDTH+col;
      outb(0x3D4,14);
      outb(0x3D5,tmp>>8);
      outb(0x3D4,15);
      outb(0x3D5,tmp);
    }

\</c\>

Wenn man den Cursor vom Bildschirm weg haben möchte, muss man ihn z.B einfach in die 26. Zeile setzen (diese gibt es nämlich nicht). Das geht natürlich genau so wie in der eben genannten Funktion, aber dies hier ist die direkte Variante:

\<c\>

    void removecursor() {
      outb(0x3D4,14);
      outb(0x3D5,0x07);
      outb(0x3D4,15);
      outb(0x3D5,0xD0);
    }

\</c\>

## Weblinks

- [Artikel aus der OSDevWiki](http://www.osdev.org/wiki/Text_UI)
- ["Printing to the Screen" Bran's Kernel Development Tutorial](http://osdever.net/bkerndev/Docs/printing.htm)
- [ASCII-Tabelle](http://de.wikipedia.org/wiki/ASCII-Tabelle)
- [Codepage 437](http://de.wikipedia.org/wiki/Codepage_437)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/2195/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1549/index.html)

<!-- MediaWiki page 1549; revision 2195; parent 2194; 2007-10-20T21:23:02Z -->
