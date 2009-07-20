# Mercurial

Mercurial ist ein in Python entwickeltes Version Control System, das wie die meisten in erster Line über die Shell gesteuert wird. Wobei alle Kommandos mit hg, dem Elementsymbol für Quecksilber(engl. Mercury), beginnen. Es gibt aber auch eine Explorer Erweiterung(TortoiseHg) mit Hilfe derer Mercurial über das Kontext-Menu gesteuert werden kann und IDEs wie zum Beispiel NetBeans und KDevelop die Mercurial unterstützen.

# Eigenschaften

Mercurial gehört zu der Gruppe der dezentral organisierten [VCS](https://github.com/lowlevel-eu/wiki/wiki/Versionsverwaltung "Versionsverwaltung"), d.h. es benötigt keinen zentralen Server um die Repositories vieler Entwickler miteinander zu synchronisieren.

## Besonderheiten

Eine Besonderheit an Mercurial ist, dass alle Befehle sich auf das Wurzelverzeichnis des Repositories beziehen, wenn nicht anders angegeben, und nicht wie bei den meisten anderen Systemen nur auf das aktuelle Verzeichnis.

# hg - Shell Kommandos

Dies ist eine kurze Einführung in ein paar nützliche Befehle. Für weitere Informationen ist der *help*-Befehl recht hilfreich.

    $ hg help [topic]

Er liefert sowohl nützliche Informationen zur Benutzung als auch mögliche Alias-Namen für die Befehle. So lässt sich der *update*-Befehl beispielsweise auch durch *up*, *checkout* und *co* ansprechen.

## Repository erstellen

Ein neues hg-Repository zu erstellen ist ganz einfach. Mittels *init*-Befehl lässt sich das aktuelle Verzeichnis oder optional ein beliebiges anderes Verzeichnis in ein Repository verwandeln.

    $ hg init [dir]

Dabei ist es egal ob sich in dem betreffenden Verzeichnis bereits Quellcodes befinden oder nicht. Das Repository wird zunächst noch kein der möglicherweise vorhandenen Dateien unter Versionkontrolle haben.

## Repository Clonen

Wenn bereits ein Repository für das gewünschte Projekt existiert, muss kein neues Repository erstellt werden. Es reicht das existierende für die eigenen Arbeit zu Clonen.

    $ hg clone <URI>

Dabei wird der *default-path* automatisch auf die angegebene URI gesetzt, so dass alle *push*- und *pull*-Befehle ohne URI auf diese Adresse zugreifen.

## Dateien hinzufügen/entferen

Um Dateien in die Obhut des Repositories zu geben. Müssen sie zunächst einmal hinzugefügt werden.

    $ hg add <file>

Wenn alle Dateien bislang nicht unter Versionkontrolle stehen dem Repository hinzugefügt werden sollen kann das auch mit dem *addremove*-Befehl geschehen.

    $ hg addremove

Zusätzlich werden dabei alle Dateien, die manuell aus der Verzeichnisstruktur gelöscht wurden, als aus dem Repository gelöscht markiert. Um einzelne Dateien aus dem Repository zu entfernen existiert der *remove*-Befehl

    $ hg remove <file>

Damit diese Änderungen wirksam werden müssen sie commited werden.

## Änderungen übernehmen

Wurden Änderungen gemacht müssen sie mit *commit*-Befehl übernommen werden.

    $ hg commit

Mercurial erstellt jetzt eine neue Revision des Projekts und gibt die Möglichkeit die Änderungen mit einer Commit-Message zu kommentieren.

## Arbeitsverzeichnis aktualisieren

Mit dem *update*-Befehl lässt sich das Arbeitsverzeichnis auf den stand jeder beliebigen Revision des Repositories bringen.

    $ hg update [REV]

Wird keine keine Revision angegeben aktualisiert Mercurial automatisch auf die letzte.

## Änderungen holen/importieren

Um Änderungen aus anderen Repositories zu übernehmen gibt es verschiedene Möglichkeiten. Eine davon ist der *pull*-Befehl. Er übernimmt alle Änderungen aus dem Quellrepository die im aktuellen noch Fehlen.

    $ hg pull [<URI>]

Anders als beispielsweise [git](https://github.com/lowlevel-eu/wiki/wiki/Git "Git") wird dabei aber das Arbeitsverzeichnis nicht aktualisiert. Dem Entwickler wird also die Möglichkeit gegeben die seine Arbeit ungestört fortzusetzen bevor er sich entscheidet die fremden Änderungen zu inspizieren oder mit den eigenen zu vereinen *(merge)*.

Weitere Möglichkeiten fremde Änderungen zu übernehmen sind das importieren von Patches oder Änderungs-Bündeln mit den Befehlen *import* bzw. *unbundle*.

## Änderungen übertragen/exportieren

Natürlich können die eigenen Änderungen auf verschieden Arten anderen zugänglich gemacht werden. Äquivalent zum *pull*-Befehl existiert ein *push*

    $ hg push [<URI>]

Damit lassen sich Änderungen (entsprechende Rechte vorausgesetzt) direkt in fremde Repositories übertragen. Es lassen sich aber auch Patches exportieren *(export)* oder Änderungen in Bündel zusammen fassen *(bundle)*.

## Weiter nützliche Befehle

- *tag(s)* - Zum Benennen von Revisionen
- *branch(s)* - Zum Benennen von Entwicklungszweigen
- *status*, *diff*, *log* und *help*

# Kostenlose Repository Hoster

Auch wenn Mercurial ohne zentralen Server auskommt, kann ein solcher für zum Beispiel die Veröffentlichung nützlich sein. Kostenlose Hoster sind unter anderem [SourceForge](http://sourceforge.net) und [Google Code](http://mercurial.selenic.com/wiki/MercurialHosting).

Eine liste mit weitern Hostern gibt es [hier](http://mercurial.selenic.com/wiki/MercurialHosting).

# Weblinks

- [Mercurial Buch](http://hgbook.red-bean.com/read/) *(english)*
- [Deutschsprachiges Tutorial auf der offiziellen Mercurial Website](http://mercurial.selenic.com/wiki/GermanTutorial)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/4678/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1891/index.html)

<!-- MediaWiki page 1891; revision 4678; parent 4677; 2009-07-20T14:40:21Z -->
