# C

C ist eine bekannte, ältere Programmiersprache. Sie verfolgt das Ziel, bei vergleichbarer Ausführungsgeschwindigkeit plattformunabhängiger und abstrakter als [Assembler](https://github.com/lowlevel-eu/wiki/wiki/Assembler "Assembler") zu sein. Direkte Weiterentwicklung von C ist [C++](https://github.com/lowlevel-eu/wiki/wiki/C%2B%2B "C++").

| Allgemeines |  |
| -------------------------------- | ----------------------------------------------------------------------------------------------------- |
| Name: | C |
| Inlineassembler: | Ja |
| Compiler: | [gcc](https://github.com/lowlevel-eu/wiki/wiki/GNU-Compiler-Collection "Gcc") |
| Spracheneigenschaften |  |
| Plattformen: | Alle |
| Beispielkernel in der Sprache: | [C-Kernel mit GRUB](https://github.com/lowlevel-eu/wiki/wiki/C-Kernel-mit-GRUB "C-Kernel mit GRUB") |
| Homepage |  |

  

## Kernelprogrammierung mit C

Da man mit C sehr hardwarenah programmieren kann, eignet sich die Sprache zur Programmierung eines Kernels. Es ist sogar die überwiegende Anzahl der Betriebssystemkernel in C geschrieben. Für andere Bereiche ist C jedoch nicht sonderlich geeignet, um Beispiel für einen Bootsektor. Empfehlenswert ist – wie bei jeder anderen Sprache, die im Bereich der Kernelprogrammierung verwendet werden soll – ein Compiler, der Inlineassembler unterstützt. Hierfür eignet sich der [gcc](https://github.com/lowlevel-eu/wiki/wiki/GNU-Compiler-Collection "Gcc"). Für Einsteiger gibt es ein [Tutorial](http://www.cheebi.de/c-kernel-tutorial.pdf), welches beschreibt, wie man in den [Protected Mode](https://github.com/lowlevel-eu/wiki/wiki/Protected-Mode "Protected Mode") schaltet und in C geschriebenen Code ausführt.

## Eigenschaften von C

### Assemblercode in C

Während es möglich ist, den allergrößten Teil des Kernels in C zu schreiben, sind für einige wenige Aufgaben nach wie vor einige Zeilen Assemblercode notwendig. Es gibt dabei im Wesentlichen zwei Ansätze:

- **Inline-Assembler**: Assemblercode wird direkt in den C-Code eingebettet. Die konkrete Syntax dafür unterscheidet sich von Compiler zu Compiler, im Allgemeinen wird der Assemblercode durch das Schlüsselwort *asm* eingeleitet. Ein Vorteil dieser Methode ist, dass ein direkter Zugriff auch auf lokale C-Variablen möglich ist. Sie eignet sich daher für sehr kleine Codestücke besonders gut.

  Siehe auch [Inline-Assembler mit GCC](https://github.com/lowlevel-eu/wiki/wiki/Inline-Assembler-mit-GCC "Inline-Assembler mit GCC")

- **Externe Assemblerdatei**: Der Assemblercode wird in eine eigene Datei ausgelagert und vom C-Code als eigenständige Funktion aufgerufen. Die Übergabe von Parametern und des Rückgabewerts wird im Artikel [Aufrufkonventionen](https://github.com/lowlevel-eu/wiki/wiki/Aufrufkonventionen "Aufrufkonventionen") beschrieben.

### Zeiger in C

Zeiger sind einzigartig in C. Mit Zeigern kann man wie bei Assembler direkt auf den Arbeitsspeicher zugreifen. (Allerdings nicht auf Register) Folgender Beispielcode verdeutlicht dies:

    /* Standardfunktionen für die Shell */
    /***********************************************************************************
    * Funktion Oneletter: Zeigt ein Buchstaben an einer bestimmten Position
    * Groundcolour: Vordergrundfarbe
    * Backcolour: Hintergrundfarbe
    * Letter: Der Buchstabe
    * Zeile: Die Zeile des Buchstaben
    * Position: Welche Position der Buchstabe in der Zeile hat
    ***********************************************************************************
    */
    void OneLetter(unsigned char Groundcolour, unsigned char Backcolour, unsigned char Letter, unsigned char Zeile, unsigned char   Position)
    {
        char Colour;
        unsigned short int Atribut;
        unsigned short int *Text = 0xB8000;
        /* Prüfen ob überhaupt Farben möglich sind */
        if(Groundcolour > 16)
        {
            End();
        }
        if(Backcolour > 16)
        {
            End();
        }
        /* Zusammlegen der Farbe */
        Colour = Groundcolour * 16 + Backcolour;
        Atrribut = Colour <<8;
        Atrribut = Atrribut | Letter;
        /* Adress für die richtige Positionierung finden */
        Text += y * 80 + x;
        *Text = Atrribut;
    }

Es handelt sich um den Code für die Textausgabe aus [FiKe](https://github.com/lowlevel-eu/wiki/wiki/FiKe "FiKe"). Die Zeile 3 beinhaltet einen Zeiger, der für die Textausgabe essentiell ist. Dieser Zeiger kann erhöht werden(Zeile 18) oder auf dem zeigende Wert verändert werden(Zeile 19).  
Bei **sehr** fortgeschrittenen Betriebsystemen sollte jedoch auch ein Aspekt auf die Sicherheit getan werden. (Nur nötig bei Netzwerkfähigkeit)

## Bekannte C-Compiler

- gcc aus der [GNU Compiler Collection](http://gcc.gnu.org/)
- [tcc](http://bellard.org/tcc/) (Tiny C Compiler)
- Borland [Turbo C](http://dn.codegear.com/article/20841) für DOS (16 Bit/Real Mode)

## Weblinks

- [Allgemeines C-Tutorial](http://openbook.galileocomputing.de/c_von_a_bis_z/c_000Vorwort_000.htm#Xxx999266)
- [Draft des C Standards](http://www.open-std.org/JTC1/SC22/WG14/www/docs/n1124.pdf)
- [C-Tutorial](http://www.c-howto.de/)
- [C-Kernel-Tutorial](http://www.cheebi.de/c-kernel-tutorial.pdf)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/4777/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1526/index.html)

<!-- MediaWiki page 1526; revision 4777; parent 4269; 2009-07-29T22:19:52Z -->
