# C

| Allgemeines |  |
| -------------------------------- | ----------------------------------------------------------------------------------------------------- |
| Name: | C |
| Inlineassembler: | Ja |
| Compiler: | [gcc](https://github.com/lowlevel-eu/wiki/wiki/GNU-Compiler-Collection "Gcc"), icc, ... |
| Spracheneigenschaften |  |
| Plattformen: | Alle |
| Beispielkernel in der Sprache: | [C-Kernel mit GRUB](https://github.com/lowlevel-eu/wiki/wiki/C-Kernel-mit-GRUB "C-Kernel mit GRUB") |
| Homepage |  |

C ist eine bekannte, ältere Programmiersprache. Sie verfolgt das Ziel, bei vergleichbarer Ausführungsgeschwindigkeit plattformunabhängiger und abstrakter als [Assembler](https://github.com/lowlevel-eu/wiki/wiki/Assembler "Assembler") zu sein. Direkte Weiterentwicklung von C ist [C++](https://github.com/lowlevel-eu/wiki/wiki/C%2B%2B "C++").

## Geschichte

C wurde 1971–1973 von Dennis Ritchie in den Bell Laboratories entwickelt, er stützte sich dabei auf die Programmiersprache B, die Ken Thompson in den Jahren 1969/70 geschrieben hatte. Ritchie schrieb auch den ersten Compiler für C. 1973 war die Sprache so weit ausgereift, dass man nun den Unix-Kernel in C neu schreiben konnte.

## häufiger Verwendungszweck

C wird häufig in der Systemprogrammierung eingesetzt. z.B. Der Linuxkernel, ist bis auf Ausnahmen vollständig in C geschrieben. C wird auch sehr häufig in der Anwendungsentwicklung eingesetzt.

## Kernelprogrammierung mit C

Da man mit C sehr hardwarenah programmieren kann, eignet sich die Sprache zur Programmierung eines Kernels hervorragend. Es ist sogar die überwiegende Anzahl der Betriebssystemkernel in C geschrieben. Für andere Bereiche ist C jedoch nicht sonderlich geeignet, um Beispiel für einen Bootsektor. Empfehlenswert ist – wie bei jeder anderen Sprache, die im Bereich der Kernelprogrammierung verwendet werden soll – ein Compiler, der Inlineassembler unterstützt. Hierfür eignet sich der [gcc](https://github.com/lowlevel-eu/wiki/wiki/GNU-Compiler-Collection "Gcc"). Für Einsteiger gibt es ein [Tutorial](http://www.cheebi.de/c-kernel-tutorial.pdf), welches beschreibt, wie man in den [Protected Mode](https://github.com/lowlevel-eu/wiki/wiki/Protected-Mode "Protected Mode") schaltet und in C geschriebenen Code ausführt.

## Eigenschaften von C

### Assemblercode in C

Während es möglich ist, den allergrößten Teil des Kernels in C zu schreiben, sind für einige wenige Aufgaben nach wie vor einige Zeilen Assemblercode notwendig. Es gibt dabei im Wesentlichen zwei Ansätze:

- **Inline-Assembler**: Assemblercode wird direkt in den C-Code eingebettet. Die konkrete Syntax dafür unterscheidet sich von Compiler zu Compiler, im Allgemeinen wird der Assemblercode durch das Schlüsselwort *asm* eingeleitet. Ein Vorteil dieser Methode ist, dass ein direkter Zugriff auch auf lokale C-Variablen möglich ist. Sie eignet sich daher für sehr kleine Codestücke besonders gut.

  Siehe auch [Inline-Assembler mit GCC](https://github.com/lowlevel-eu/wiki/wiki/Inline-Assembler-mit-GCC "Inline-Assembler mit GCC")

- **Externe Assemblerdatei**: Der Assemblercode wird in eine eigene Datei ausgelagert und vom C-Code als eigenständige Funktion aufgerufen. Die Übergabe von Parametern und des Rückgabewerts wird im Artikel [Aufrufkonventionen](https://github.com/lowlevel-eu/wiki/wiki/Aufrufkonventionen "Aufrufkonventionen") beschrieben.

### Zeiger in C

Zeiger sind einzigartig in C. Mit Zeigern kann man wie bei Assembler direkt auf den Arbeitsspeicher zugreifen (allerdings nicht auf Register). Folgender Beispielcode verdeutlicht dies: \<c\>

    int console_attr = 7, console_x = 0, console_y = 0;

    void putchar(int c)
    {
        unsigned char *console = (unsigned char *)0xB8000;

        if ((c != '\n') && (c != '\r'))
        {
            console += (console_y * 80 + console_x) * 2;
            *(console++) = c;
            *console = console_attr;
            console_x++;
        }
        else if (c == '\r')
        {
            console_x = 0;
        }

        while ((console_x >= 80) || (c == '\n'))
        {
            if (console_x >= 80)
            {
                console_x -= 80;
            }
            console_y++;
            while (console_y >= 25)
            {
                console_y--;
                memmove((void *)0xB8000, (void *)0xB80A0, 3840);
                memset((void *)0xB8F00, 0, 160);
            }
            c = 0;
        }
    }

\</c\> Hierbei handelt es sich um einen Beispielcode, der zeigt, wie eine putchar()-Funktion beispielsweise aussehen könnte. Die Zeile 5 beinhaltet einen Zeiger, der für die Textausgabe essentiell ist. Dieser Zeiger kann erhöht werden (Zeile 7) oder auf dem zeigende Wert verändert werden (Zeile 9). In Zeile 8 wird zuerst der Wert, auf den console zeigt, verändert und dann der Zeiger um eins erhöht.  

## Beispielprogramm

\<c\>

    #include <stdio.h>

    int main(void)
    {
        printf("Hallo Welt!\n");
        return 0;
    } /* end main() */

\</c\>

## Bekannte C-Compiler

- gcc aus der [GNU Compiler Collection](http://gcc.gnu.org/)
- [tcc](http://bellard.org/tcc/) (Tiny C Compiler)
- [bcc](http://dir.filewatcher.com/d/FreeBSD/4.2-release/i386/bcc-1995.03.12.tgz.79915.html) ein 16Bit Compiler für Linux (im dev86-Paket enthalten)
- Borland [Turbo C](http://dn.codegear.com/article/20841) für DOS (16 Bit/Real Mode)

## Weblinks

- [Allgemeines C-Tutorial](http://openbook.galileocomputing.de/c_von_a_bis_z/c_000Vorwort_000.htm#Xxx999266)
- [Draft des C Standards](http://www.open-std.org/JTC1/SC22/WG14/www/docs/n1124.pdf)
- [C-Tutorial](http://www.c-howto.de/)
- [C-Kernel-Tutorial](http://www.cheebi.de/c-kernel-tutorial.pdf)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/6916/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1526/index.html)

<!-- MediaWiki page 1526; revision 6916; parent 6915; 2010-01-17T01:04:23Z -->
