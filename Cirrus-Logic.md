# Cirrus Logic

Qemu emuliert primär eine Cirrus Logic GD5446. Mit dieser Grafikkarte ist es sehr einfach, mit einem eigenen OS in den Genuss hardwarebeschleunigter¹ 2D-Grafik zu kommen.

¹So weit ich es gesehen habe, werden die Grundoperationen hardwarebeschleunigt dargestellt. Alle Angaben ohne Gewähr.

## Resourcen

Die Grafikkarte ist eine PCI-Karte, Vendor-ID 0x1013, Chip-ID 0x00B8. Sie wird größtenteils über MMIO angesteuert, dabei werden zwei Speicherbereiche als MMIO-Interface zur Karte benutzt, die über die PCI-Schnittstelle abgefragt werden können: Der erste fängt im Falle Qemus an der Adresse 0xF0000000 an und ist 2 Megabytes groß und dient als Framebufferschnittstelle, der zweite (kleinere) Bereich (für die Steuerung der Karte) fängt bei 0xF2000000 an und ist 0x1000 Bytes lang.

In diesen zweiten Bereich sind sämtliche VGA-Ports gemappt, wobei man von der Adresse 0x3C0 abziehen muss, um den Offset in den MMIO-Bereich zu erhalten. So befindet sich das Register VGA_MISC_OUT_W (0x3C2) an der Speicheradresse 0xF2000002.

VGA besitzt an einigen Stellen hinter einem Port mehrere Register, zwischen denen über einen zweiten Indexport gewechselt werden kann. An diesen Stellen besitzt die Grafikkarte oft Zusatzports, vor allem die Register 0x3CE und 0x3CF werden in diesem Zusammenhang für die Hardwarebeschleunigung verwendet.

## Initialisierung

Es gibt zwei Möglichkeiten, die Grafikkarte zu initialisieren: Entweder über die VGA-Register, oder über VESA.

Die Programmierung über die VGA-Register ist recht kompliziert, ich habe es nicht geschafft, wer es versuchen will, viel Spaß, als Lektüre empfehle ich den Xorg-Treiber (siehe Anhang).

Über VESA lässt sich die Karte dagegen sehr einfach einrichten, es reicht aus, über den int10 (entweder mit vm86, einem Emulator oder im Realmode bei Betriebssystemstart) eine größere Auflösung zu wählen.

Ist die Karte einmal in dem Videomodus, muss noch die Beschleunigung aktiviert werden. Dies geschieht durch Schreiben in das Graph-Register 33:

\<c\>

1.  define VGA_GRAPH_INDEX 0x3CE
2.  define VGA_GRAPH_DATA 0x3CF

outb(VGA_GRAPH_INDEX, 0x33); outb(VGA_GRAPH_DATA, 0x04); // Oder outw(VGA_GRAPH_INDEX, 0x0433); \</c\>

Ich habe diese Methode jedoch nur in Qemu getestet. Ich bin mir ziemlich sicher, dass das in der echten Welt da draußen nicht so einfach tut, aber wer hat schon eine Cirrus Logic. :)

## Offscreen Memory

Die von Qemu initialisierte Cirrus hat 2 Megabyte Videoram, der nicht dem Framebuffer zugeordnet ist. Es liegt in linear hinter dem Framebuffer und kann genau wie dieser für Beschleunigung benutzt werden. TODO: Das hier überprüfen. Eventuell sinds auch 4 Megabyte, dann allerdings inklusive Framebuffer.

## Beschleunigung

TODO: Zeichnen per MMIO über die Register?

Für beschleunigtes Zeichnen werden für verschiedene Zeichenarten verschiedene Raster Ops benutzt:

\<c\> const unsigned char cirrus_rop\[\] = {

       0x00, // clear
       0x05, // and
       0x09, // andreverse
       0x0D, // copy        Einfaches Setzen der Farbe
       0x50, // andinverted
       0x06, // noop
       0x59, // xor
       0x6D, // or
       0x95, // equiv
       0x0B, // invert
       0xAD, // orreverse
       0xD0, // copyinverted
       0xD6, // orinverted
       0xDA, // nand
       0x0E, // set

};

void set_rop(int rop) {

       outb(VGA_GRAPH_INDEX, 0x32);
       outb(VGA_GRAPH_DATA, cirrus_rop[rop]);

} \</c\>

Nach jeder Zeichenoperation muss zum Starten des Zeichnens entweder 0x02 in das Graph-Register 0x31 geschrieben werden oder die Karte nach der Initialisierung in den Autostart-Modus versetzt werden: \<c\> // Autostart aktivieren outw(VGA_GRAPH_INDEX, 0x8031); \</c\>

### Zeichnen von gefüllten Rechtecken

Zuerst muss das Zeichnen von Rechtecken mit der gewünschten Farbe und dem gewünschten Raster Op initialisiert werden. Für einfache gefüllte Rechtecke benutzen wir hier COPY.

\<c\> set_rop(3);

// Initialisieren outw(VGA_GRAPH_INDEX, 0x0433); // 0x04 nach GR33

// Pixelgröße einstellen outw(VGA_GRAPH_INDEX, 0xC030 \|((bitsPerPixel - 8) \<\< 9)); // Farbe einstellen outw(VGA_GRAPH_INDEX, ((b \<\< 8) & 0xff00) \| 0x01); outw(VGA_GRAPH_INDEX, ((r) & 0xff00) \| 0x11); outw(VGA_GRAPH_INDEX, ((g \>\> 8) & 0xff00) \| 0x13); outw(VGA_GRAPH_INDEX, 0x15);

// Pitch einstellen (Bytes in einer Zeile int pitch = screenwidth \* bitsPerPixel / 8; outw(VGA_GRAPH_INDEX, ((pitch \<\< 8) & 0xff00) \| 0x24); outw(VGA_GRAPH_INDEX, ((pitch) & 0x1f00) \| 0x25);

  
// Jetzt können beliebig viele Rechtecke mit diesen Einstellungen gezeichnet werden:

// Breite outw(VGA_GRAPH_INDEX, (((width \* 3 - 1) \<\< 8) & 0xff00) \| 0x20); outw(VGA_GRAPH_INDEX, (((width \* 3 - 1)) & 0x1f00) \| 0x21); // Höhe outw(VGA_GRAPH_INDEX, (((height - 1) \<\< 8) & 0xff00) \| 0x22); outw(VGA_GRAPH_INDEX, ((height - 1) & 0x0700) \| 0x23); int dest = pitch \* y + x \* bitsPerPixel / 8; outw(VGA_GRAPH_INDEX, ((dest \<\< 8) & 0xff00) \| 0x28); outw(VGA_GRAPH_INDEX, ((dest) & 0xff00) \| 0x29); outw(VGA_GRAPH_INDEX, ((dest \>\> 8) & 0x3f00) \| 0x2A); // Starte Zeichenvorgang if (!autostart)

       outw(VGA_GRAPH_INDEX, 0x0231);

\</c\>

  

## Hardware-Cursor

## Links

<http://www.koders.com/c/fidC2D0E7B95D33763B17521DF3EA7B68C81D500CAD.aspx> Code aus Qemu <http://cgit.freedesktop.org/xorg/driver/xf86-video-cirrus/> Xorg-Treiber

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/3395/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1743/index.html)

<!-- MediaWiki page 1743; revision 3395; parent 3394; 2008-10-09T14:40:58Z -->
