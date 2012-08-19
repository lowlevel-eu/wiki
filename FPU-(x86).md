# FPU (x86)

Diese Seite ist ein Artikel, welcher **mehr** haben könnte..  

Wenn du mehr darüber weißt oder recherchieren willst, bist **du** aufgerufen, dies zu tun. Wenn du dir in einer Sache nicht sicher bist, dann stell es auf die Diskussionsseite.

Die FPU des [x86](https://github.com/lowlevel-eu/wiki/wiki/X86 "X86") - Prozessors nennt sich x87 und ist heute fest im Prozessor eingebaut. In den Anfangsjahren des x86ers war die FPU noch ein externer Chip, der auf dem Mainboard aufgelötet wurde, und nicht jeder x86 - Nutzer konnte eine FPU sein Eigen nennen.

Heute ist die FPU, wie bereits erwähnt, fest im Prozessor eingebaut, weshalb man sich auch darauf verlassen kann, dass die entsprechenden FPU - Befehle auch wirklich unterstützt werden.

Neben den mathematischen Befehlen, die den ursprünglichen Zweck der FPU darstellen, kann man auf der x87 - FPU auch sog. [MultiMedia Extensions](https://github.com/lowlevel-eu/wiki/wiki/MultiMedia-Extension "MMX") ausführen. Allerdings sollte man sich vorher überlegen, ab welchem Prozessor man sein OS unterstützen will, denn Intel empfiehlt heute, anstatt der langsameren [MMX](https://github.com/lowlevel-eu/wiki/wiki/MultiMedia-Extension "MMX") - Befehle, die auf der FPU ausgeführt werden, die performanteren [SSE](https://github.com/lowlevel-eu/wiki/wiki/Streaming-SIMD-Extensions "SSE") - Befehle zu verwenden, die direkt vom Hauptprozessor abgearbeitet werden.

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/10687/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2587/index.html)

<!-- MediaWiki page 2587; revision 10687; parent 0; 2012-08-19T16:43:59Z -->
