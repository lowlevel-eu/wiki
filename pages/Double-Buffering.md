# Double Buffering

Double Buffering bezeichnet eine Methode zur Darstellung von Grafiken, bei der neben dem Bildschirmspeicher auch noch ein zweiter Puffer genutzt wird.

Bei komplexen Zeichenoperationen kann es vorkommen, dass der Bildschirm seinen Inhalt aktualisiert bevor die Zeichenoperationen beendet ist. Dadurch zeigt der Bildschirm einen unvollständigen Zwischenstand an, wodurch beim Benutzer der Eindruck des Flackerns entsteht. Double Buffering behebt dieses Problem, indem zunächst in einen zweiten Puffer, den sogenannten Backbuffer, gerendert wird. Erst wenn die Zeichenoperationen abgeschlossen sind und das Frame vollständig ist, wird der Backbuffer in den Frontbuffer kopiert bzw. werden die beiden Puffer getauscht.

Das Flimmern tritt übrigens auch bei neueren Bildschirmen auf, wenn man die Pixel einzeln setzt. Das dauert, und während dieser Zeit kann man teilweise sogar den zeilenweisen Aufbau des Bildes beobachten. Das kann man verhindern, indem man das Bild erst in den Puffer zeichnet und dann den kompletten Puffer auf einmal auf den Bildschirm bringt.

## Beispiel

Für dieses Beispiel wird die Allegro-Bibliothek verwendet. Man findet sie [auf Sourceforge](http://alleg.sourceforge.net). Hier wird die Version 4 verwendet, da sie eine übersichtlichere API bietet als die aktuelle Version 5.

``` c
#include <allegro.h>

int main(int argc, char **argv)
{
    allegro_init();
    install_keyboard();

    set_color_depth(32);
    set_gfx_mode(GFX_AUTODETECT_WINDOWED, 256, 256, 0, 0);

    clear_to_color(screen, makecol(0, 0, 0));

    return 0;
}
```

Keine Angst, das war nur die Initialisierung der Allegro-Bibliothek und des Fensters, das wir verwenden wollen. Danach wird es einfacher.

*Zur Information: Wir haben jetzt die Allegro-Bibliothek initialisiert (allegro_init()), die Tastatur für unser Programm aktiviert (install_keyboard()), die Farbtiefe auf 32 Bit gesetzt (set_color_depth(32)), ein Fenster mit der Größe 256\*256 Pixel kreiert und den Standard-Grafiktreiber als Treiber festgelegt (set_gfx_mode(GFX_AUTODETECT_WINDOWED, 256, 256, 0, 0)) und schließlich das Fenster schwarz gefärbt (clear_to_color(screen, makecol(0, 0, 0))).*

Nun kommen wir zum eigentlichen Zeichnen. Wir werden einen einfachen Farblauf erstellen. Dazu verwenden wir die Funktion putpixel():

``` c
#include <allegro.h>

int main(int argc, char **argv)
{
    allegro_init();
    install_keyboard();

    set_color_depth(32);
    set_gfx_mode(GFX_AUTODETECT_WINDOWED, 256, 256, 0, 0);

    clear_to_color(screen, makecol(0, 0, 0));

    int i = 0, k = 0;

    for(i = 0; i < 256; ++i)
    {
        for(k = 0; k < 256; ++k)
        {
            //screen ist der Bildschirm, makecol bildet eine Farbe aus dem angegebenen RGB-Wert
            putpixel(screen, i, k, makecol(i, k, i));
        }
    }

    //Auf einen Tastendruck warten, damit das Bild nicht gleich verschwindet
    readkey();

    return 0;
}
```

So weit, so gut. Wenn man dieses Programm ausprobiert (dazu braucht man Allegro und man muss mit dem Schalter -lalleg kompilieren), kann man sehen, wie der Farbverlauf Spalte für Spalte aufgebaut wird. Ab und zu ein ganz netter Anblick, aber für produktives Arbeiten nicht gerade hilfreich.

Nun das gleiche Beispiel mit einem zweiten Puffer (Bilder werden in Allegro als "BITMAP" gespeichert):

``` c
#include <allegro.h>

int main(int argc, char **argv)
{
    allegro_init();
    install_keyboard();

    set_color_depth(32);
    set_gfx_mode(GFX_AUTODETECT_WINDOWED, 256, 256, 0, 0);

    clear_to_color(screen, makecol(0, 0, 0));

    int i = 0, k = 0;

    //Puffer für das Bild erstellen
    BITMAP *buffer = create_bitmap(SCREEN_W, SCREEN_H);

    for(i = 0; i < 256; ++i)
    {
        for(k = 0; k < 256; ++k)
        {
            //Nun nicht mehr auf den Bildschirm, sondern in den Puffer zeichnen
            putpixel(buffer, i, k, makecol(i, k, i));
        }
    }

    //Den Puffer darstellen
    blit(buffer, screen, 0, 0, 0, 0, SCREEN_W, SCREEN_H);

    readkey();

    return 0;
}
```

Nun sollte das Bild auf einmal erscheinen.

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/11451/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2600/index.html)

<!-- MediaWiki page 2600; revision 11451; parent 11401; 2020-08-02T22:09:52Z -->
