# Textausgabe

Die Textausgabe ist für so gut wie jedes Programm eine wichtige Möglichkeit, dem User oder Programmierer Informationen über sich mitzuteilen bzw. generell Output auszugeben. Auch und gerade für ein Betriebssystem ist es auch schon in einer sehr frühen Phase wichtig, dass es Informationen per Textausgabe ausgeben kann um z. B. anzuzeigen, ob diverse Aufgaben gelungen sind oder nicht.

## Realmode

Im Realmode macht das BIOS diese Arbeit. Um ein Zeichen zu schreiben reicht folgender ASM-Code (für NASM): \<asm\> mov ah, 0x0E  ;Wir wollen schreiben mov bh, 0x00  ;Auf den Bildschirm mov al, "T"  ;Das zu schreibende Zeichen int 0x10  ;Ausführen \</asm\> Um einen ganzen Text zu schreiben gibt es folgenden Trick: \<asm\> Schreibe:  ;Hier fängt die Funktion Schreibe an lodsb  ;Zeichen laden nach al cmp al, 0x00  ;Wenn 0-Byte ... je Schreibeende;... dann beende Schreibefunktion

Wenn nicht, dann

mov ah, 0x0E  ;Wir wollen schreiben mov bh, 0x00  ;Auf den Bildschirm int 0x10  ;Jetzt jmp Schreibe  ;Mache nächstes Zeichen Schreibeende:  ;Bei Stringende wird hierher gesprungen: ret  ;Die Funktion beenden \</asm\>

Dann kann man einfach einen Text schreiben: \<asm\> mov si, Text  ;Den Text unten call Schreibe  ;schreiben

Der Text  

Text db "Text im Realmode schreiben geht!",13,10,0

,13,10 macht eine Neue Zeile

,0 sagt das es hier aufhört (sonst würde zuviel geschrieben werden)

\</asm\>

Die Funktion INT 10/AH=0Eh erlaubt es nicht im Textmodus eine Farbe anzugeben.

## Protected Mode

Zur Ausgabe von Text gibt es einen 4 kB großen Speicher an der Adresse 0xB8000. Dieser Speicher kann linear angesprochen werden und benutzt 2 Byte pro Zeichen auf dem Bildschirm. Es ergeben sich also 80 Spalten (Zeichen pro Zeile) und 25 Zeilen, insgesamt also 2000 gleichzeitig darstellbare Zeichen.

### Zeichenausgabe

Um nun auf dem Bildschirm ein Zeichen auszugeben, muss erstmal das Offset ausgerechnet werden, an dem das Zeichen steht. Da der Speicher linear ist geht das auch mit einer linearen Gleichung: o = z\*80+s, wobei o für das Offset, z für die Zeile und s für die Spalte steht

In dem ersten Byte wird der Buchstabe selbst, in dem 2. Byte wird das Attribut, also die Vorder- und Hintergrundfarbe gespeichert. Als Code wird [Codepage 437](https://github.com/lowlevel-eu/wiki/wiki/Codepage-437 "Codepage 437") verwendet, welche eine Erweiterung von [ASCII](https://github.com/lowlevel-eu/wiki/wiki/Codepage-437 "ASCII") darstellt.

Das Attribute-Byte ist wie folgt aufgebaut:

BXXXYYYYb, Hierbei ist X die Hintergrundfarbe, Y die Vordergrundfarbe und B das „Blinkbit“. Ist es gesetzt, blinkt das entsprechende Zeichen. Hier ist eine Tabelle aller Farben:

| Wert | Farbe |  | Wert | Farbe |  |
| ------ | ---------- | ----- | ------ | ------------- | ----- |
| 0x0 | Schwarz |  | 0x8 | Dunkelgrau |  |
| 0x1 | Blau |  | 0x9 | Hellblau |  |
| 0x2 | Grün |  | 0xA | Hellgrün |  |
| 0x3 | Cyan |  | 0xB | Hellcyan |  |
| 0x4 | Rot |  | 0xC | Hellrot |  |
| 0x5 | Magenta |  | 0xD | Hellmagenta |  |
| 0x6 | Braun |  | 0xE | Gelb |  |
| 0x7 | Hellgrau |  | 0xF | Weiß |  |

Häufig benutzt wird 0x07, **Hellgrau auf Schwarz.**

Man kann sich nicht darauf verlassen, dass das höchstwertige Bit des Attributbytes wirklich anzeigt, ob das Zeichen blinken soll oder nicht. Bei einigen Computern ist dieses Bit einfach das höherwertige Bit der Hintergrundfarbe, sodass man hier auch helle Farben als Hintergrund verwenden kann.

Wie man die Bedeutung dieses Bits manuell bestimmen kann, steht im Artikel [Color Graphics Adapter](https://github.com/lowlevel-eu/wiki/wiki/Color-Graphics-Adapter#16-hintergrundfarben "Color Graphics Adapter").

  
Hier ein kleines Beispiel einer Funktion, die ein Zeichen (chr), in der Farbe color auf den Bildschirm, an die Position x,y schreiben soll. Hierbei werden Steuerzeichen nicht beachtet bzw. als normales Zeichen auch ausgegeben (siehe [Codepage 437](https://github.com/lowlevel-eu/wiki/wiki/Codepage-437 "Codepage 437")).

\<c\> void printchar(uint8_t chr, uint8_t color, uint8_t x, uint8_t y) {

     uint16_t* off = (uint16_t*)0xB8000;
     // berechnen der Adresse
     off += y * 80 + x;  // eine Multiplikation mit 2 darf hier nicht erfolgen, da off vom type uint16_t ist
     // setzen des zeichens + attributebyte
     *off = (((uint16_t)color) << 8) | chr;

} \</c\>

Mit der 1. Zeile wird ein Pointer auf den Textspeicher erzeugt. Der Dateityp ist uint16_t, also 2 Byte, damit wir das Zeichen und das Attributebyte gleichzeitig schreiben können (geht einfach schneller). Nun wird mit der obengenannten Formel die Adresse ausgerechnet. Würde man uint8_t benutzen, müsste man dann mit 2 multiplizieren, denn jedes Zeichen benutzt 2 Byte. Man setzt das Zeichen, indem man das Attribute-Byte auf 16 Bit erweitern, dann eine Linksverschiebung von 8 Bit vornimmt und per logischem Oder mit dem Zeichenbyte verknüpft.

Achtung: Das Attributebyte kommt zwar immer nach dem Zeichenbyte, aber x86 ist ein [Little-Endian](http://de.wikipedia.org/wiki/Byte-Reihenfolge)-System.

Nochmal eine Veranschaulichung der Oder-Verknüpfung:

    attr     char
    0x07     0x41
    <<8       "
    0x0700 | 0x41 = 0x0741

### Bildschirm scrollen

Um den Bildschirm zu scrollen muss einfach der gesamte Textspeicher ab der 2. Zeile zur 1. Zeile kopiert werden und die letzte Zeile gelöscht werden, also auf 0 oder einen sonstigen Wert setzen. Wenn man eine memmove- und eine memset-Funktion bzw. eine memsetw-Funktion bei einem Attributbyte != 0 hat, geht das in ein paar Zeilen. Denn die Funktion memcpy muss für sich überlappende Speicherbereiche nicht das gewünschte Ergebnis erzielen.

### Cursor

Der Cursor dient dazu dem Nutzer anzuzeigen, an welcher Stelle die nächste Ausgabe erfolgt. In der Regel ist er als blinkender Unterstrich unter der Textzeile zu sehen. Das Verschieben des Cursors ist eine Operation, die *relativ* lange dauert. ([“Keep in mind that in/out to VGA Hardware is a slow operation”](http://www.osdev.org/wiki/Text_Mode_Cursor))

**Cursor verschieben**

Diese Funktion verschiebt den Cursor. \<c\> void displaycursor(uint8_t col, uint8_t row) {

     uint16_t tmp;
     tmp = row * VIDEOTEXT_WIDTH + col;
     outb(0x3D4,14);
     outb(0x3D5,tmp >> 8);
     outb(0x3D4,15);
     outb(0x3D5,tmp);

} \</c\> **Löschen des Cursors** Wenn man den Cursor vom Bildschirm weg haben möchte, muss man ihn z. B. einfach in die 26. Zeile setzen (diese gibt es nämlich nicht). Das geht natürlich genau so wie in der eben genannten Funktion, aber dies hier ist die direkte Variante:

\<c\> void removecursor() {

     outb(0x3D4,14);
     outb(0x3D5,0x07);
     outb(0x3D4,15);
     outb(0x3D5,0xD0);

} \</c\>

## Siehe auch

- [CGA](https://github.com/lowlevel-eu/wiki/wiki/Color-Graphics-Adapter "CGA")

## Weblinks

- [Artikel aus der OSDevWiki](http://www.osdev.org/wiki/Text_UI)
- [“Printing to the Screen” Bran's Kernel Development Tutorial](http://osdever.net/bkerndev/Docs/printing.htm)
- [ASCII-Tabelle](http://de.wikipedia.org/wiki/ASCII-Tabelle)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/10142/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1549/index.html)

<!-- MediaWiki page 1549; revision 10142; parent 10141; 2011-09-20T17:01:46Z -->
