# Maschinensprache

Maschinensprache sind die Befehle, die direkt vom Prozessor ausgefuehrt werden. Der Intel x86 Befehlssatz hat eine variable Laenge, z.B. bedeutet das Byte 90h "NOP" in [assembler](https://github.com/lowlevel-eu/wiki/wiki/Assembler "Assembler") und steht fuer "no operation". Es ist also moeglich, mit einem Hexeditor ausfuehrbaren Code zu schreiben.

Maschinensprache kann mehr als Assembler, z.B. springt der Befehl

    eb ff

Zum *zweiten* Byte, also zum *Parameter* des Kommandos. Das bedeutet, nach dem Byte "eb" wird das Byte "ff" ausgefuehrt, das "eigentlich" als Parameter gedacht war. Ein solches Konstrukt ist in assembler unmoeglich. Diese Konstrukte wurden jedoch zum Sparen von Speicherplatz eingesetzt.

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/11225/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2654/index.html)

<!-- MediaWiki page 2654; revision 11225; parent 0; 2014-12-06T11:18:43Z -->
