# MultiMedia Extension

**Achtung!**

Dieser Artikel wird gerade bearbeitet, bitte **keine** Änderungen vornehmen! ~[Hartmut](https://lowlevel-eu.github.io/wiki/pages/1865/index.html "Benutzer:Hartmut") 21:15, 6. Aug. 2009 (CEST)

  
Die **MultiMedia Extension** oder kurz **MMX** umfasst neue Befehle zur bearbeitung mehrerer gleichartiger Datenpakete mit nur einem Befehl (Single Instruction Multiple Data, SIMD-Verfahren gennant) bearbeiten. Somit bekommen z.B. Bildbearbeitungsprogramme durch die MMX-Befehle einen deutlichen Prformanceschub.

  

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

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/5377/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2003/index.html)

<!-- MediaWiki page 2003; revision 5377; parent 0; 2009-08-06T19:15:30Z -->
