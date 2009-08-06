# Shell

**An diesem Artikel wird im Laufe des 06.08.2009 gearbeitet! --[Benutzer:Hartmut](https://lowlevel-eu.github.io/wiki/pages/1865/index.html "Benutzer:Hartmut")**

Eine **Shell** (deutsch wörtlich: Muschel, hier: Schale, Aufsatz) ist ein Programm, welches eine direkte Schnittstelle zwischen den Funktionen des Betriebssystems (Syscalls) und dem User darstellt und/oder als Kommandozeileninterpreter zum Ausführen von Programmen und der Navigation durch das Dateisystem dient.

## Geschichte

Die frühen Hardwaremonitore, wo noch jedes Bit einzeln gecodet werden musste, können schon als eine Art "Shell" angesehen werden. Shells an sich sind ein altes Konzept, um im direktem Kontakt mit dem Betriebssystem zu stehen. Die wohl älteste Shell ist die 'osh', auch 'Thompson Shell' für das Betriebssystem [Unix](https://github.com/lowlevel-eu/wiki/wiki/Unix "Unix") . Sie war von 1971 bis 1979 die Standard-Shell unter Unix und führte u.a. das mächtige Konzept der [Pipes](https://github.com/lowlevel-eu/wiki/wiki/Pipe "Pipe") ein. Danach entwickelte Stephen R. Bourne die Bourne-Shell, sh, auf die fast alle heutigen Shell mehr oder weniger aufsetzen.

## Funktionsweise einer Shell

### Linux/Unix

Unter Linux und Unix war und ist das wohl essentiellste Werkzeug eines Linux-User und vor allem Administrators die Shell. Sie wird direkt nach dem Login gestartet und kann unter Desktop-Umgebungen wie Gnome oder KDE mit den Programmen Terminal bzw. Konsole gestartet werden. Die Shell unter Linux/Unix ist meistens auch Kommandozeileninterpreter und Interpreter für eine simple Scriptsprache, dem Shell-Script. Wobei simpel hier nicht ganz zutrifft, denn die Sprache ist doch recht mächtig.

Die wohl mit Abstand meist genutzte Shell unter Linux ist die bash, die Bourne Again Shell. Sie ist ein GNU-Projekt und wird von der FDL auch als Standard-Shell empfohlen. Unter Linux/Unix greift die Shell allerdings (heutzutage) nicht mehr direkt auf die Funktionen des Betriebssystems zu. Dafür gibt es Programme wie rm, mv, cp usw.. Es wird beispielsweise

    Hartmut@linux:/tmp:$ mv -r EineDatei /home/Hartmut

eingegeben, von gefolgtem ENTER. Die Shell ermittelt nun:

- Welcher Befehl eingegeben wurde (mv)
- Ob der Befehl als Programm auf dem System vorhanden ist (sollte eigentlich)
- Ermittelt evtl. Optionen (-r, EineDatei, /home/Hartmut)
- Ruft das Programm auf und übergibt dabei die Optionen
- Wartet, bis das Programm beendet wurde
- Kehrt wieder zur Eingabe zurück

Bei manchen Shells kann durch heranstellen eines '&' auch ein neuer Prozess gestartet werden, in dem das Programm dann abläuft und somit die Shell weiterbenutzen.

### bash

Die **Bourne-again Shell**, oder kurz **bash** ist die Standard-Shell für GNU-Systeme und die mit Abstand am meistgenutzte Shell unter Linux. Sie ist eine Weiterentwicklung der sh, die lange Zeit Standard war.

## Windows

Die Shell unter Windows wurde seit MS-DOS-Zeiten Befehlsinterpreter, bzw. Kommandozeileninterpreter genannt. Während der Windows-9x-Zeit hieß sie dann 'Eingabeaufforderung' oder auch "DOS-Box", wurde dann unter Windows 2000/XP nur "Eingabeaufforderung" genannt.

Allerdings war seit jeher die "Windows-Shell" nicht halb so mächtig wie deren \*nix-Pendants. Die Scriptsprache, "Batch" bestand mehr oder weniger aus einer Einananderreihung von Befehlen mit simpelsten Kontrollstrukturen.

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/5344/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1864/index.html)

<!-- MediaWiki page 1864; revision 5344; parent 5099; 2009-08-06T17:00:05Z -->
