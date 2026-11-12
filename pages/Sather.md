# Sather

Diese Seite ist ein Artikel, welcher **mehr** haben könnte..  

Wenn du mehr darüber weißt oder recherchieren willst, bist **du** aufgerufen, dies zu tun. Wenn du dir in einer Sache nicht sicher bist, dann stell es auf die Diskussionsseite.

| Allgemeines |  |
| -------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| Name: | Sather |
| Inlineassembler: | Nein, aber Inline-C und Inline-Fortran |
| Compiler: | GNU Sather, Sather-K, Sather-W |
| Spracheneigenschaften |  |
| Plattformen: | Frei aus dem Quellcode kompilierbar |
| Beispielkernel in der Sprache: | [Sather-Kernel mit GRUB](Sather-Kernel-mit-GRUB.md "Sather-Kernel mit GRUB") |
| Homepage |  |

<http://www.icsi.berkeley.edu/~sather/>

  
Sather ist eine eher unbekannte Programmiersprache, deren Wurzeln in der Sprache Eiffel liegen. Ihr Ziel bestand darin, ähnliche Möglichkeiten (Design by contract, etc.) zu bieten, aber um einiges weniger komplex zu sein. So waren Satherprogramme der ersten Version noch gültige Eiffelprogramme. Inzwischen hat Sather aber auch Konzepte aus anderen Programmiersprachen übernommen und ist somit keine Untermenge von Eiffel mehr.

## Kernelprogrammierung mit Sather

Obwohl es einen Beispielkernel mit Sather gibt ([Sather-Kernel mit GRUB](Sather-Kernel-mit-GRUB.md "Sather-Kernel mit GRUB")), ist im Großen und Ganzen (vor allem für Anfänger) von der Verwendung dieser Sprache in Kerneln abzuraten. Sie erfordert eine ziemlich große Runtime-Lib und ist im Gegensatz zu z. B. [C](C.md "C") alles andere als hardwarenah. Einziger Pluspunkt hier mag die Möglichkeit der Verwendung von Inline-C (wie auch bei Eiffel) sein.

Außerdem erstellt ein Sathercompiler keinen Maschinen- oder Objektcode, sondern C-Code. Hier muss also auch die Makefile noch entsprechend angepasst werden, damit nicht automatisch externe Bibliotheken des Hostbetriebssystems eingebunden werden.

## Eigenschaften von Sather

### Inline-C

Sather bietet mehrere Möglichkeiten, C-Code einzubinden.

- Inline: Über die Klasse SYS und die Methode inlined_C kann C-Code direkt eingebunden werden. Lokale Variablen aus dem Sathercode können hierbei per Voranstellen eines \# verwendet werden.
- Extern: Es gibt auch die Möglichkeit, ganze „Klassen“ aus C einzubinden (natürlich werden hierbei keine echten C-Klassen verwendet, da es solche nicht gibt, sondern nur einzelne Methoden).

## Beispielprogramm

Bei C mag das Beispielprogramm wohl fast dem Beispielkernel entsprechen, hier ist das jedoch aufgrund der RTL keineswegs der Fall. Darum hier ein kleines Hallo-Welt-Programm:

    class MAIN is
        main is 
            #OUT + "Hallo Welt!\n"; 
        end;
    end;

Erstellt wird die Klasse „MAIN“ mit der Routine „main“. Beim Kompilieren wird diese als Einstiegspunkt in das Programm verwendet (kann jedoch verändert werden). „#OUT“ ist ein Alias für OUT::create, „erstellt“ also die Klasse OUT (die zur Systembibliothek gehört) &#150; hier muss dies nicht allzu ernst genommen werden, da die create-Routine von OUT meist einfach nur die Klasse selbst zurückgibt. Das „+“ führt zum Aufruf von (OUT::create).plus("Hallo Welt!\n"), es wird also die Routine namens „plus“ in der Klasse „OUT“ ausgeführt, ihr wird der String „Hallo Welt!\n“ übergeben. Diese Routine gibt den String letztlich aus.

Hinweis: Im Gegensatz zu Eiffel sind die Semikola *nicht* optional!

## Weblinks

- [Homepage](http://www.icsi.berkeley.edu/~sather/)
- [Tutorial](http://www.icsi.berkeley.edu/~sather/Documentation/LanguageDescription/contents.html)
- [GNU Sather](http://www.gnu.org/software/sather/)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/6998/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2173/index.html)

<!-- MediaWiki page 2173; revision 6998; parent 0; 2010-02-01T16:18:04Z -->
