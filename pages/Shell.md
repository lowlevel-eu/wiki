# Shell

Eine **Shell** (deutsch wörtlich: Muschel, hier: Schale, Aufsatz) ist ein Programm, welches eine direkte Schnittstelle zwischen den Funktionen des Betriebssystems (Syscalls) und dem User darstellt und/oder als Kommandozeileninterpreter zum Ausführen von Programmen und der Navigation durch das Dateisystem dient.

## Geschichte

Die frühen Hardwaremonitore, wo noch jedes Bit einzeln gecodet werden musste, können schon als eine Art „Shell“ angesehen werden. Shells an sich sind ein altes Konzept, um im direktem Kontakt mit dem Betriebssystem zu stehen. Die wohl älteste Shell ist die „osh“, auch „Thompson Shell“ für das Betriebssystem [Unix](Unix.md "Unix") . Sie war von 1971 bis 1979 die Standard-Shell unter Unix und führte u. a. das mächtige Konzept der [Pipes](Pipe.md "Pipe") ein. Danach entwickelte Stephen R. Bourne die Bourne-Shell, sh, auf die fast alle heutigen Shells mehr oder weniger aufsetzen.

## Funktionsweise einer Shell

### Linux/Unix

Unter Linux und Unix war und ist das wohl essentiellste Werkzeug eines Linux-Users und vor allem Administrators die Shell. Sie wird direkt nach dem Login gestartet und kann unter Desktop-Umgebungen wie Gnome oder KDE z. B. mit den Programmen Terminal bzw. Konsole gestartet werden. Die Shell unter Linux/Unix ist meistens auch Kommandozeileninterpreter und Interpreter für eine einfache Scriptsprache, dem Shell-Script, wobei „einfach“ hier nicht ganz zutrifft, denn die Sprache ist doch recht mächtig.

Die wohl mit Abstand meist genutzte Shell unter Linux ist die bash, die Bourne Again Shell. Sie ist ein GNU-Projekt und wird von der FDL auch als Standard-Shell empfohlen. Unter Linux/Unix greift die Shell allerdings (heutzutage) nicht mehr direkt auf die Funktionen des Betriebssystems zu. Dafür gibt es Programme wie rm, mv, cp usw.. Es wird beispielsweise

    Hartmut@linux:/tmp:$ cp -r EinOrdner /home/Hartmut

eingegeben, von gefolgtem ENTER. Die Shell ermittelt nun:

- Welcher Befehl eingegeben wurde (cp)
- Ob der Befehl in der Shell als Funktion eingebaut ist (sollte hier nicht)
- Wenn nicht, ob der Befehl als Programm auf dem System vorhanden ist (sollte eigentlich)
- Ermittelt evtl. Optionen (-r, EinOrdner, /home/Hartmut)
- Ruft das Programm bzw. die eingebaute Funktion auf und übergibt dabei die Optionen
- Wartet, bis das Programm beendet wurde
- Kehrt wieder zur Eingabe zurück

Bei manchen Shells kann durch Verwendung eines *&* am Ende der Zeile auch das Warten übersprungen werden, sodass die Shell sofort nach dem Befehlsaufruf wieder zur Benutzung bereit ist.

### bash

Die **Bourne-again Shell**, oder kurz **bash** ist die Standard-Shell für GNU-Systeme und die mit Abstand am meistgenutzte Shell unter Linux. Sie ist eine Weiterentwicklung der sh, die lange Zeit Standard war.

## Windows

Die Shell unter Windows wurde seit MS-DOS-Zeiten Befehlsinterpreter bzw. Kommandozeileninterpreter genannt. Während der Windows-9x-Zeit hieß sie dann „Eingabeaufforderung“ oder auch „DOS-Box“ und wurde dann unter Windows 2000/XP nur noch „Eingabeaufforderung“ genannt.

Allerdings war seit jeher die „Windows-Shell“ nicht halb so mächtig wie deren \*nix-Pendants. Die Scriptsprache, „Batch“ bestand mehr oder weniger aus einer Aneinanderreihung von Befehlen mit einfachen Kontrollstrukturen. Dies soll sich mit der ab Windows 7 vorinstallierten PowerShell ändern.

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/9993/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1864/index.html)

<!-- MediaWiki page 1864; revision 9993; parent 7669; 2011-07-28T03:50:11Z -->
