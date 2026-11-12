# Subversion

Diese Seite oder Abschnitt ist zwar komplett, es wird aber folgende Verbesserungen gewünscht:  

*Kontrolllesen, außerdem meine TODOs im Text abarbeiten bitte :)*

Hilf Lowlevel, den Artikel zu verbessern.

  
**Subversion** (oft abgekürzt als **SVN**) ist ein zentrales [Versionskontrollsystem](Versionsverwaltung "Versionsverwaltung").

## Entwicklungsziel

Die Arbeiten am Subversionprojekt wurden 2000 begonnen. Das Ziel war es, Probleme bei [CVS](Concurrent-Versions-System "CVS") zu umgehen: Ein Beispiel dafür ist das Branching, welches jetzt in konstanter Laufzeit vonstatten geht. Dieser Ansatz brachte dem Projekt schnell den Slogan "CVS done right" ein. Darum wird [CVS](Concurrent-Versions-System "CVS") heutzutage auch meistens nur noch genutzt, wenn die Entwickler Subversion nicht kennen, oder die Umstellung auf ein neues System scheuen.

## Installation

### Linux

Subversion lässt sich bei jeder größeren Distribution aus den Paketquellen installieren. Meist heißt das Paket *subversion*.

Es gibt jedoch, wie unter Windows, einen grafischen SVN Clienten namens kdesvn, der sehr komfortabel ist.

### Windows

Unter Windows ist die Arbeit mit der Shell oft weniger bequem als unter Linux, darum empfiehlt sich die Installation von TortoiseSVN, welches sich sehr gut in den Windows Explorer integiert.

Dazu lädt man zunächst das aktuelle Paket von [dieser Seite](http://tortoisesvn.net/downloads) herunter, und installiert es. Nach der Installation stehen im Kontextmenü des Windows Explorers die unten genannten Befehle für SVN zur Verfügung.

## Schnellstart

Für einen reibungslosen Einsteig in Subversion gibt es hier eine Auflistung der wichtigsten Befehle. Jedoch empfiehlt sich auf jedem Fall ein genaues Studium der [Dokumentation](http://svnbook.red-bean.com/nightly/en/index.html), da hier nur die wirklich grundlegendsten Befehle aufgelistet werden.

Bei Windows ist das Prinzip genau gleich, nur muss man die Befehle im Kontextmenü auswählen, und erhält für die Befehlsparameter praktische Eingabefenster.

### Archiv herunterladen (checkout)

Um an der Entwicklung eines bestehenden Projektes teilzunehmen muss man oft erst die Entwicklerversion herunterladen. Subversion bietet dafür den Befehl `checkout`, den man oft auch `co` abkürzt.

Beispiel (Kopie des Tyndur-Archives):

    # Archiv herunterladen
    svn co svn://overgames.de/lost 

### Archiv aktualisieren (update)

Wenn sich das Archiv auf dem Server verändert hat, weil ein anderer Entwickler einen Commit gemacht hat, dann ist es nötig, seine Arbeitskopie auf den selben Stand zu bringen. Das geschieht durch den Befehl `update` (oder kurz `up`).

Bei einem Update kann es passieren, dass Konflikte entstehen. Diese korrigiert man einfach, indem man die diff-ähnlichen Kommentare in den Dateien, welche in Konflikt stehen, von Hand auflöst.

    # Alle Änderungen herunterladen
    svn up

### Änderungen übertragen (commit)

Irgendwann kommt der Zeitpunkt, an dem man seine Änderungen öffentlich machen will. Das geschieht mit dem Befehl `commit` (kurz `ci`).

Im Gegensatz zu [Git](Git "Git") werden alle Änderungen an getrackten Dateien standardmäßig automatisch übertragen, ohne dass man sie explizit zu einem Commit hinzufügen muss, also Vorsicht.

    # Alle Änderungen hochladen
    svn ci

### Ausblick

*TODO: Ein svn-affiner Mensch bitte die anderen wichtigen Befehle hier erwähnen, danke*

## Kostenloses Subversion-Hosting

Hier eine Liste von Anbietern, bei denen man sein Subversion-Archiv kostenlos hosten kann, um es für die Öffentlichkeit zugängig zu machen.

- [SourceForge](http://sourceforge.net): Bietet auch Hosting für Git und CVS

## Weblinks

- [Subversion bei Wikipedia](http://de.wikipedia.org/wiki/Apache_Subversion)
- [Subversion Homepage](http://subversion.tigris.org/)
- [Subversion-Dokumentation](http://svnbook.red-bean.com/nightly/de/index.html)
- [Aktuellere Dokumentation (englisch)](http://svnbook.red-bean.com/nightly/en/index.html)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/8324/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2036/index.html)

<!-- MediaWiki page 2036; revision 8324; parent 7534; 2010-09-20T18:29:10Z -->
