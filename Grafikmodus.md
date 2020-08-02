# Grafikmodus

Diese Seite oder Abschnitt ist zwar komplett, es wird aber folgende Verbesserungen gewünscht:  

*Bitte generische Infos über Grafikmodus und mehr Algorithmen dazu. [GUI](https://github.com/lowlevel-eu/wiki/wiki/Graphical-User-Interface "GUI") und diesen hier splitten, dieser hier allgemeines zum Pixel schubsen*

Hilf Lowlevel, den Artikel zu verbessern.

  
Auch wenn die meisten Hobby-[Betriebssysteme](https://github.com/lowlevel-eu/wiki/wiki/Betriebssystem "Betriebssystem") "nur" über eine [Kommandozeile](https://github.com/lowlevel-eu/wiki/wiki/Shell "Command Line Interface") verfügen, ist die Entwicklung einer [grafischen Benutzeroberfläche](https://github.com/lowlevel-eu/wiki/wiki/Graphical-User-Interface "GUI") ab einem gewissen Entwicklungsstand des Kernels auch ein interessantes Projekt.

Allerdings kann man dem Bildschirm nicht einfach sagen, dass er einen Kreis oder eine Linie zeichnen soll. Man kann nur einzelne Pixel setzen, deshalb muss man sich um die Darstellung komplexerer - da zweidimensionaler - Formen selbst kümmern (Lowlevel-Zeichnen eben).

  

## Voraussetzungen

Dieses Tutorial soll nicht erklären, wie man den Bildschirm ansteuert oder arithmetische Berechnungen durchführt. Aus diesem Grund werden auch Funktionen wie putpixel() (s.u.) oder sin() nicht genau erläutert, sondern nur die hier verwendete Signatur kurz erklärt. Die Funktionen sind auf das Nötigste beschränkt, weshalb die Beispiele für den praktischen Einsatz durchaus noch erweitert werden können (z.B. Farben bei `putpixel()` o.ä.).

Im Folgenden wird eine Funktion `putpixel()` verwendet, die folgendermaßen definiert ist:

``` c
void putpixel(int x, int y);
```

Diese Funktion stellt nur das absolut notwendigste dar, und zwar geht sie von einem schwarzen Bildschirm aus und setzt beim Aufruf das Pixel an der angegebenen Koordinate auf weiß. Die Koordinaten sind, wie üblich, in Pixeln gezählt, wobei das Pixel in der linken oberen Ecke die Koordinaten (0\|0) hat.

Eine weitere Funktion heißt round():

``` c
unsigned int round(unsigned double number); // Rundet die Zahl, z.B. round(4.2) = 4 und round(5.7) = 6
```

  

## Linien

Wir beginnen mit dem Zeichnen von einfachen Linien. Gerade Linien zu zeichnen, ist nicht das Problem - bei schiefen wird es dagegen schwieriger. Wir beschränken uns auf den letzteren Fall, da der Algorithmus universell einsetzbar sein soll.

Für das Zeichnen von Linien benötigt man das Wissen über lineare Funktionen aus der Schule. Der Bresenham-Algorithmus basiert auf genau diesem Prinzip. Und zwar: Es gibt zwei Punkte `P(x1|y1)` und `Q(x2|y2)`, zwischen denen die Linie verlaufen soll. Dazu denken wir uns ein Koordinatensystem, bei dem die x-Achse nach rechts und die y-Achse nach unten verläuft (Ursprung links oben).

Zur Erinnerung hier noch einmal die Grundform einer linearen Funktion: ` f(x) = mx + t ` Hier ist `m` die Steigung und `t` der y-Achsenabschnitt oder Offset.

`t` ist sehr einfach zu "berechnen": `t = y1`, da die Linie hier anfängt.

`m` bekommt man mit der Formel `m = (x2 - x1) / (y2 - y1)`.

Nun kann man das ganze zu einer Funktion zusammensetzen:

``` c
void linie(unsigned int x1, unsigned int y1, unsigned int x2, unsigned int y2)
{
    unsigned double m = (x2 - x1) / (y2 - y1);

    for(int x = x1; x <= x2; ++x)
        putpixel(x, y1 + round(m * (double) x));
}
```

## Siehe auch

- [Double Buffering](https://github.com/lowlevel-eu/wiki/wiki/Double-Buffering "Double Buffering")
- [VGA](https://github.com/lowlevel-eu/wiki/wiki/Video-Graphics-Array "VGA")
- [Cirrus Logic](https://github.com/lowlevel-eu/wiki/wiki/Cirrus-Logic "Cirrus Logic")
- [UEFI](https://github.com/lowlevel-eu/wiki/wiki/Unified-Extensible-Firmware-Interface "UEFI")
- [VBE](https://github.com/lowlevel-eu/wiki/wiki/VESA-BIOS-Extensions "VBE")

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/11463/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2639/index.html)

<!-- MediaWiki page 2639; revision 11463; parent 11462; 2020-08-02T22:32:18Z -->
