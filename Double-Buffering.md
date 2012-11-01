# Double Buffering

Diese Seite ist ein Artikel, welcher **mehr** haben könnte..  

Wenn du mehr darüber weißt oder recherchieren willst, bist **du** aufgerufen, dies zu tun. Wenn du dir in einer Sache nicht sicher bist, dann stell es auf die Diskussionsseite.

Double Buffering bezeichnet eine Methode zur Darstellung von Grafiken, bei der neben dem Bildschirmspeicher auch noch ein zweiter Puffer genutzt wird.

Bei Röhrenbildschirmen wird das Bild durch einen Elektronenstrahl, der auf eine spezielle Oberfläche trifft, die dadurch zum Leuchten angeregt wird, dargestellt. Wenn sich nun das Bild schneller ändert, als sich der Strahl bewegt, entsteht ein unerwünschtes Flimmern. Das kann verhindert werden, indem Veränderungen der dargestellten Grafik erst in einem zweiten Puffer erfolgen, der dann als ganzes in den Videospeicher kopiert wird. Dadurch entsteht ein deutlich flüssigerer Bildlauf.

Das Flimmern tritt übrigens auch bei neueren Bildschirmen auf, wenn man die Pixel einzeln setzt. Das dauert, und während dieser Zeit kann man teilweise sogar den zeilenweisen Aufbau des Bildes beobachten. Das kann man verhindern, indem man das Bild erst in den Puffer zeichnet und dann den kompletten Puffer auf einmal auf den Bildschirm bringt.

## Beispiel

Für dieses Beispiel wird die Allegro-Bibliothek verwendet. Man findet sie \[alleg.sourceforge.net auf Sourceforge\]. Hier wird die Version 4 verwendet, da sie eine übersichtlichere API bietet als die aktuelle Version 5.

\<c\>

1.  include \<allegro.h\>

int main(int argc, char \*\*argv) {

       allegro_init();
       install_keyboard();

       set_color_depth(32);
       set_gfx_mode(GFX_AUTODETECT_WINDOWED, 256, 256, 0, 0);

       clear_to_color(screen, makecol(0, 0, 0));

} \</c\>

Keine Angst, das war nur die Initialisierung der Allegro-Bibliothek und des Fensters, das wir verwenden wollen. Danach wird es einfacher.

*Zur Information: Wir haben jetzt die Allegro-Bibliothek initialisiert (allegro_init()), die Tastatur für unser Programm aktiviert (install_keyboard()), die Farbtiefe auf 32 Bit gesetzt (set_color_depth(32)), ein Fenster mit der Größe 256\*256 Pixel kreiert und den Standart-Grafiktreiber als Treiber festgelegt (set_gfx_mode(GFX_AUTODETECT_WINDOWED, 256, 256, 0, 0)) und schließlich das Fenster schwarz gefärbt (clear_to_color(screen, makecol(0, 0, 0))).*

Nun kommen wir zum eigentlichen Zeichnen. Wir werden einen einfachen Farblauf erstellen. Dazu verwenden wir die Funktion putpixel():

\<c\>

1.  include \<allegro.h\>

int main(int argc, char \*\*argv) {

       allegro_init();
       install_keyboard();

       set_color_depth(32);
       set_gfx_mode(GFX_AUTODETECT_WINDOWED, 256, 256, 0, 0);

       clear_to_color(screen, makecol(0, 0, 0));

       int i = 0,k = 0;

       for(i = 0; i < 256; ++i)
       {
           for(k = 0; k < 256; ++k)
           {
               putpixel(screen, i, k, makecol(i, k, i));
           }
       }

} \</c\>

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/10914/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2600/index.html)

<!-- MediaWiki page 2600; revision 10914; parent 10819; 2012-11-01T12:11:18Z -->
