# MultiMedia Extension

Diese Seite ist ein Artikel, welcher **mehr** haben könnte..  

Wenn du mehr darüber weißt oder recherchieren willst, bist **du** aufgerufen, dies zu tun. Wenn du dir in einer Sache nicht sicher bist, dann stell es auf die Diskussionsseite.

Die **MultiMedia Extension** oder kurz **MMX** umfasst neue Befehle zur Bearbeitung mehrerer gleichartiger Datenpakete mit nur einem Befehl (Single Instruction Multiple Data, SIMD-Verfahren gennant) bearbeiten. Somit bekommen z.B. Bildbearbeitungsprogramme durch die MMX-Befehle einen deutlichen Performanceschub.

  

## MMX-Befehle

Die MMX-Befehle lassen sich in drei Gruppen einteilen:

- Bearbeitungsbefehle
- Typumwandlungsbefehle
- Steuerungs des MMX-Zustandes (EMMX)

  
Nachfolgend eine Tabelle mit allen neuen Instruktionen und der Funktionsweise

| Befehl | Bezeichnung | Bedeutung | Funktion |
| -------------- | -------------------------- | ------------------------------ | --------------------------------------------------------------------------------------------- |
| EMMS | Empty MMX State | MMX-Zutand zurücksetzen | Der Befehl setzt die MMX-Einheit zurück und gibt alle FPU-Register frei |
| MOVD<br>MOVQ | Move DWord<br>Move QWord | DWord bzw. QWord verschieben | Verschiebt ein DWord bzw. QWord von einem Allzweckregister in in MMX-Register und umgekehrt |

## Weblinks

- [MMX Tutorial der FH-Zwickau](http://www.fh-zwickau.de/doc/prmo/mmxtutor/text/index.htm)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/11473/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2003/index.html)

<!-- MediaWiki page 2003; revision 11473; parent 5902; 2020-08-02T23:42:21Z -->
