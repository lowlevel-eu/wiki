# Concurrent Versions System

Das **Concurrent Versions System** oder kurz **CVS** ist ein bekanntes zentrales [Version Control System](Versionsverwaltung "Versionsverwaltung") unter der GPL, welches bereits 1989 als Weiterentwicklung des RCS (Revision Control System) entwickelt wurde. Es wird seit 2008 nicht mehr aktiv weiterentwickelt (letzter Stand der aktuellen Version: 8. März 2008). Es wurde mittlerweile von [Subversion](Subversion "Subversion") und [git](Git "Git") abgelöst.

## Geschichtliches

CVS wurde als Ableger des Revision Control System weiterentwickelt und sollte dessen Limitierungen, wie das gleichzeitige Speichern von mehreren Dateien, aufheben. Um abwärtskompatibel zu sein benutze es das gleiche Dateiformat wie RCS. CVS war lange Zeit Platzhirsch unter den Versionskontrollsystemen, viele der heutigen kommerziellen „Configuration-Management-Systeme“ beruhen auf CVS. Doch aufgrund der Limitierungen von CVS hinsichtlich Verzeichnissen und Binärdateien und aufgrund einiger Sicherheitslecks wurde im Jahr 2000 dessen Nachfolgen [Subversion](Subversion "Subversion") entwickelt. Subversion hat CVS bei Projekten so gut wie komplett abgelöst, und die meisten Projekte, die CVS nutzen (z. B. FreeBSD), sind älter, und ein Wechsel auf ein anderes SCM wäre alles andere als trivial. SourceForge bietet darum auch noch Unterstützung für dieses System.

## Funktionsweise

CVS als Vorreiter moderner Versionskontrollsysteme funktioniert ebenso wie diese: Es werden Repositories erstellt und bei jeder Änderung einer Datei wird der vorherige Zustand erhalten, sodass man bis bei Änderung bis auf einen beliebigen Stand der Entwicklung zurückschrauben kann. Um dies zu ermöglichen speichert CVS jeweils das *Delta*, also nur den Unterschied zwischen den einzelnen Dateien anstatt der gesamten Datei selbst. Dadurch wird vor allem Platz gespart. Gearbeitet wird mit CVS fast wie mit allen anderen System, man holt sich den aktuellen Entwicklungsstand vom Server via *check-out* und kann via *check-in* seine Änderungen wieder zum Server übertragen. Wenn mehrere Leute gleichzeitig an einer Datei arbeiten kann dieser Misstand durch einen *merge*, also dem Zusammenführen zweier Entwicklungslinien, behoben werden.

## Mit CVS arbeiten

CVS ist ein veraltetes und fehleranfälliges System, weshalb dringendst geraten wird, [Subversion](Subversion "Subversion") (sozusagen der Nachfolger von CVS) oder sogar [git](Git "Git") zu nutzen. Diese heben die Limitierungen von CVS auf und sind zudem sicherer und werden aktiv weiterentwickelt. Dennoch hier eine kurze Übersicht über die Arbeit mit einem CVS-Repository.

CVS nutzt ein spezielles Login-System, was bedeutet, das man anders als bei git oder Subversion sich erst auf einem CVS-Server einloggen muss, auf welchem das Repository liegt. Wenn man kein Entwickler des Projektes oder lediglich den Entwicklungsstand herunterladen will benutzt man den *Anonymouis CVS Access*.

Um sich auf einem Server einzuloggen nutzt man folgenden Befehl:

    $ CVSROOT=:pserver:cvs-username@einedomain.tld:/Pfad/zum/CVS/Root/Verzeichnis cvs login

Somit kann man sich zu einem Server verbinden und, je nach Rechten, verschiedene Aktionen durchführen. Um den aktuellen Entwicklungsstand herunterzuladen nutzt man den Befehl

    $ cvs checkout repositoryname

Um einen Patch zu commiten nutzt man

    $ cvs import -m "Ein Import, heutzutage nennt man das Commit ;-)" repositoryname default

Um den lokalen Entwicklungsstand zu updaten nutzt man

    $ cvs update repositoryname

Weitere Befehle:

- log zeigt sämtliche getane Vorgänge an wie Importieren und Updaten
- diff zeigt Unterschiede zwischen Dateien an
- add fügt neue Dateien zum Repository hinzu

## Weblinks

- [Offizielle Homepage](http://www.nongnu.org/cvs/) (wird nicht mehr gepflegt)
- [OpenSource-Development with CVS](http://cvsbook.red-bean.com/) - Buch über die Entwicklung mit CVS
- [CVS-Cheatsheet](http://kj.uue.org/papers/cvs-handout.pdf)

## Siehe auch

- [Subversion](Subversion "Subversion") - Eine Weiterentwicklung von CVS
- [git](Git "Git") - populäres dezentrales VCS, wird auch für [týndur](T%C3%BDndur "Týndur") benutzt

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/10814/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2104/index.html)

<!-- MediaWiki page 2104; revision 10814; parent 10813; 2012-09-12T21:43:51Z -->
