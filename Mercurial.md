# Mercurial

Mercurial ist eine dezentral organisierters Versionsverwaltungssystem, das wie die meisten anderen in erster Linie über die Shell gesteuert wird. Es ist nahezu vollständig in Python geschrieben (mit Ausnahme des in C implementierten diff), sodass es theoretisch problemlos auf allen Plattformen mit Python-Umgebung einsatzfähig ist. Dar Name des Kommandozeilentools lautet *hg* (chem. Elementsymbol für Quecksilber; engl. : Mercury). Für Linux und Windows gibt es das Tool \[tortoisehg.bitbucket.org/ TortoiseHg\], welches eine grafische Oberfläche für alle Operationen plus weitere Features wie das "Shelf" ("Regal", um Changes zwischen verschiedenen Commits/Merging-Vorgängen zwischenspeichern zu können) bereitstellen und sich unter Windows auch in das Kontextmenü des Explorers integrieren.

Außerdem existieren eine Reihe IDEs, wie zum Beispiel NetBeans, Eclipse und KDevelop, die Mercurial out-of-the-box oder per Plugins Unterstützen.

## Eigenschaften

Mercurial gehört wie z.B. [git](https://github.com/lowlevel-eu/wiki/wiki/Git "Git") zu der Gruppe der dezentral organisierten [VCS](https://github.com/lowlevel-eu/wiki/wiki/Versionsverwaltung "Versionsverwaltung"), d.h. es benötigt keinen zentralen Server, um die Repositories mehrerer Entwickler miteinander zu synchronisieren. Damit erreicht es einen erheblichen Geschwindigkeitsvorteil gegenüber zentral organisierten VCS, wie SVN und CVS.

### Besonderheiten

Eine Besonderheit an Mercurial ist, dass alle Befehle sich auf das Wurzelverzeichnis des Repositories beziehen, wenn nicht anders angegeben, und nicht wie bei den meisten anderen Systemen nur auf das aktuelle Verzeichnis.

## Konfiguration

Mercurial sucht Konfigurationsdateien unter anderem in *\$HOME/.hgrc* und *\$(hg root)/.hg/hgrc*. Die folgenden Konfigurationsdatei lässt unter anderem die *Pager Extension* laden, so dass die Ausgabe von ausgewählten Befehlen durch den angegeben Pager geleitet wird. Zudem wird die *diff*-Ausgabe auf das erweiterte git-Format umgestellt, was sehr empfehlenswert ist solange man nicht auf die Kompatibilität zu uralten Unix-Tools angewiesen ist.

    [ui]
      username = Max Mustermann <max.mustermann@example.com>
    [diff]
      git=true
    [extensions]
      color=
      pager=
      progress=
    [pager]
      pager=LESS='FSRX' less
      ignore=version, update
    #  attend=log, diff, annotate

Für weitere Konfigurationsmöglichkeiten siehe: `$ `[`man hgrc`](http://www.selenic.com/mercurial/hgrc.5.html)

## hg - Shell Kommandos

Dies ist eine kurze Einführung in ein paar nützliche Befehle. Für weitere Informationen ist der *help*-Befehl recht hilfreich.

    $ hg help [topic]

Er liefert sowohl nützliche Informationen zur Benutzung als auch mögliche Alias-Namen für die Befehle. So lässt sich der *update*-Befehl beispielsweise auch durch *up*, *checkout* und *co* ansprechen.

### Repository erstellen

Ein neues hg-Repository zu erstellen ist ganz einfach. Mittels *init*-Befehl lässt sich das aktuelle Verzeichnis oder optional ein beliebiges anderes Verzeichnis in ein Repository verwandeln.

    $ hg init [dir]

Dabei ist es egal ob sich in dem betreffenden Verzeichnis bereits Quellcodes befinden oder nicht. Das Repository wird zunächst noch keine der möglicherweise vorhandenen Dateien unter Versionkontrolle haben.

### Repository klonen

Wenn bereits ein Repository für das gewünschte Projekt existiert, muss kein neues Repository erstellt werden. Es reicht, das existierende für die eigene Arbeit zu klonen.

    $ hg clone <URI>

Dabei wird der *default-path* automatisch auf die angegebene URI gesetzt, so dass alle *push*- und *pull*-Befehle ohne URI auf diese Adresse zugreifen.

### Dateien hinzufügen/entferen

Um Dateien in die Obhut des Repositories zu geben müssen sie zunächst einmal hinzugefügt werden.

    $ hg add <file>

Wenn alle Dateien, die bislang nicht unter Versionkontrolle stehen, dem Repository hinzugefügt werden sollen, so kann das auch mit dem *addremove*-Befehl geschehen.

    $ hg addremove

Zusätzlich werden dabei alle Dateien, die manuell aus der Verzeichnisstruktur gelöscht wurden, als aus dem Repository gelöscht markiert. Um einzelne Dateien aus dem Repository zu entfernen existiert der *remove*-Befehl.

    $ hg remove <file>

Damit diese Änderungen wirksam werden, müssen sie commited werden.

### Änderungen übernehmen

Wurden Änderungen gemacht müssen sie mit *commit*-Befehl übernommen werden.

    $ hg commit

Mercurial erstellt jetzt eine neue Revision des Projekts, und gibt die Möglichkeit die Änderungen mit einer Commit-Message zu kommentieren.

### Arbeitsverzeichnis aktualisieren

Mit dem *update*-Befehl lässt sich das Arbeitsverzeichnis auf den Stand jeder beliebigen Revision des Repositories bringen.

    $ hg update [REV]

Wird keine keine Revision angegeben aktualisiert Mercurial automatisch auf die letzte.

### Änderungen holen/importieren

Um Änderungen aus anderen Repositories zu übernehmen gibt es verschiedene Möglichkeiten. Eine davon ist der *pull*-Befehl. Er übernimmt alle Änderungen aus dem Quellrepository, die im aktuellen noch fehlen.

    $ hg pull [<URI>]

Anders als beispielsweise bei [gits](https://github.com/lowlevel-eu/wiki/wiki/Git "Git") pull-Befehl wird dabei aber das Arbeitsverzeichnis nicht aktualisiert. Dem Entwickler wird also die Möglichkeit gegeben, seine Arbeit ungestört fortzusetzen, bevor er sich entscheidet, die fremden Änderungen zu inspizieren oder mit den eigenen zu vereinen *(merge)*.

Weitere Möglichkeiten fremde Änderungen zu übernehmen sind das importieren von Patches oder Änderungs-Bündeln mit den Befehlen *import* bzw. *unbundle*.

### Änderungen übertragen/exportieren

Natürlich können die eigenen Änderungen auf verschieden Arten anderen zugänglich gemacht werden. Äquivalent zum *pull*-Befehl existiert ein *push*

    $ hg push [<URI>]

Damit lassen sich Änderungen (entsprechende Rechte vorausgesetzt) direkt in fremde Repositories übertragen. Es lassen sich aber auch Patches exportieren *(export)* oder Änderungen in Bündel zusammen fassen *(bundle)*.

### Weitere nützliche Befehle

- *tag(s)* - Zum Benennen von Revisionen
- *branch(s)* - Zum Benennen von Entwicklungszweigen
- *status*, *diff*, *log* und *help*

## Kostenlose Repository Hoster

Auch wenn Mercurial ohne zentralen Server auskommt, kann ein solcher für zum Beispiel die Veröffentlichung nützlich sein. Kostenlose Hoster sind unter anderem [Bitbucket](http://bitbucket.org/) und [Google Code](http://code.google.com).

Eine Liste mit weiteren Hostern gibt es [hier](http://mercurial.selenic.com/wiki/MercurialHosting).

## Weblinks

- [<img src="https://raw.githubusercontent.com/wiki/lowlevel-eu/wiki/assets/38adc39e49df427364bd.png" title="englisch" width="20" height="12" alt="englisch" /> Mercurial Homepage](http://mercurial.selenic.com/)
- [<img src="https://raw.githubusercontent.com/wiki/lowlevel-eu/wiki/assets/80088a07d15fa1c1dc96.png" title="deutsch" width="20" height="12" alt="deutsch" /> Deutschsprachiges Tutorial auf der offiziellen Mercurial Website](http://mercurial.selenic.com/wiki/GermanTutorial)
- [<img src="https://raw.githubusercontent.com/wiki/lowlevel-eu/wiki/assets/38adc39e49df427364bd.png" title="englisch" width="20" height="12" alt="englisch" /> Mercurial: The Definitive Guide](http://hgbook.red-bean.com/read/) *(english)*

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/10957/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1891/index.html)

<!-- MediaWiki page 1891; revision 10957; parent 10956; 2012-12-02T18:49:40Z -->
