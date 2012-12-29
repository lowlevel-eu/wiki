# Git

**Git** ist ein dezentrales [Source-Code-Managementsystem](https://github.com/lowlevel-eu/wiki/wiki/Versionsverwaltung "Versionsverwaltung"). Git wurde ursprünglich für die Entwicklung des [Linux](https://github.com/lowlevel-eu/wiki/wiki/Linux "Linux")-Kernels entwickelt und steht unter der GPL.

## Geschichte

Nachdem das alte Versionsverwaltungssystem des Linux-Kernels seine Lizenz änderte, und es dadurch für einige Entwickler nicht mehr möglich war, dieses System zu nutzen, beschloss Linus Torvalds, ein eigenes SCM zu entwickeln, da andere SCMs nicht die Anforderungen der Kernelentwickler erfüllten.

Designziel von git war es insbesondere, ein sehr schnelles Zusammenführen von Entwicklungszweigen (Merging) zu ermöglichen. Des Weiteren musste das System eine Korruption der Versionsgeschichte, zum Beispiel durch einen Festplattenschaden oder bösartigen Angriff, selbstständig erkennen. Außerdem musste es möglich sein, dass Entwickler unabhängig voneinander arbeiten. Alle diese Ziele wurden durch git verwirklicht.

## Installation

Die meisten Linuxdistributoren bieten git bereits in ihren Software-Archiven an. Bei einigen Distributoren steht "git" jedoch als Abkürzung für die bereits länger existierenden GNU Interactive Tools, daher kann es sein, dass das Paket "git" nicht das Versionsverwaltungssystem installiert.

- Benutzer von Ubuntu oder Debian installieren das Paket *git-core*.
- Fedora-User können einfach das Paket *git* nehmen.

### Windows

Für Windowsbenutzer existiert ein Port von git, der sich msysgit nennt und unter [\[1\]](http://code.google.com/p/msysgit/) heruntergeladen werden kann. Msysgit kommt komplett mit einer Konsole (GitBash), die sich auch in Kontextmenüs integriert, und ermöglicht so auch dem Windowsnutzer komfortables Arbeiten mit git.

## Aufbau von git

*TODO: Eventuell näher auf das Architekturdesign eingehen.*

Grundsätzlich ist git ein verteiltes SCM. Das heißt, dass zu einem Projekt jeder Entwickler ein eigenes lokales Projektarchiv (Repository) hat. Normalerweise werden die Archive nur lokal genutzt, aber den Entwickler hindert nichts daran, sein lokales Repository auch öffentlich einsehbar zu machen.

Git behandelt jedes Archiv unabhängig. Verbindungen zu einem Server werden nicht hergestellt, bis der Benutzer es explizit wünscht (z.B. durch die Befehle `push` und `pull`). Ein Archiv besteht aus einer Ansammlung von Patches (diffs/Deltas), die die einzelnen commits darstellen und durch eine Baumstruktur miteinander in Verhältnis stehen. Durch Hinabwandern des Baumes und Anwendung der Patches auf dem Weg kann somit der Status zum Zeitpunkt jedes einzelnen commits hergestellt werden. Verzweigungsstellen zu verschiedenen Branches sind in dieser Baumstruktur Punkte, an denen ein commit mehr als ein Kind hat, und Merges sind solche commits, die mehr als einen Vater haben.

Die einzelnen Branches sind jeweils durch einen sogenannten *head* markiert, der sozusagen einen Zeiger auf den letzten commit dieses Zweiges darstellt.

## Schnellstart

Um schnell in git einsteigen zu können, sind hier die allerwichtigsten Befehle dargestellt. Dies ist jedoch keine Anleitung, und spricht branching und merging zum Beispiel gar nicht an. Ein einfaches Tutorial gibt es (auf Englisch) auf der Git Homepage. (siehe [Weblinks](https://github.com/lowlevel-eu/wiki/wiki/Git#weblinks "Git"))

### Archiv herunterladen (clone)

Um mit der Entwicklung zu beginnen, muss man zunächst natürlich seine eigene Kopie des Repositorys haben. Diese bekommt man mit dem `clone`-Befehl. Der Befehl ist das git-Äquivalent zum Subversion-Befehl `checkout`. (Achtung: Dieser Befehl existiert zwar auch in git, hat aber eine andere Aufgabe)

Da die gesamte Versionsgeschichte des Projektes heruntergeladen wird, kann dieser Befehl je nach Verbindungsgeschwindigkeit sehr lange dauern.

Beispiel (Kopie des offiziellen týndur-Archives anfordern):

    git clone git://git.tyndur.org/tyndur.git

### Archiv aktualisieren (pull)

Der Befehl `pull` berechnet die Änderungen zwischen dem eigenen Archiv und dem Remote-Archiv und fordert die Änderungen vom Server an. `pull` bezieht die Änderungen standardmäßig von dem origin-Archiv, das ist normalerweise das Archiv von dem ursprünglich geclonet wurde. Unter Subversion funktioniert der `update`-Befehl ähnlich.

Wenn eigene commits vorliegen, die nicht auf dem Server ist (wie es bei git eigentlich typisch ist), dann kann `pull` angewiesen werden, versuchen, die Änderungen in den eigenen Tree zu übernehmen, sodass nachher sowohl die lokalen, als auch die remote-commits vorliegen. Dies geht mit dem `--rebase`-Parameter.

Beispiel:

    # Falls der lokale Tree frei von eigenen commits ist
    git pull

    # Falls der Tree eigene commits enthält, die dem Server unbekannt sind
    git pull --rebase

### Änderungen anwenden (add/commit)

Will man seine Änderungen am Code in einen commit packen, so muss man git zunächst mitteilen, welche Dateiänderungen wichtig sind. Das macht man mit dem `add`-Befehl.

Sobald man alle Dateien hinzugefügt hat, ruft man `git commit` auf. Es öffnet sich ein Editor, in dem man die commit-Nachricht eingibt. Man kann jedoch auch mit dem Parameter `-m` direkt eine Nachricht angeben.

Im Gegensatz zu den gleichbenannten Subversion-Befehlen laufen beide Befehle bei git nur lokal ab.

Beispiel:

    # Geänderte Dateien hinzufügen
    git add foo.c bar.c

    # Änderungen eintragen
    git commit
    # Oder auch so
    git commit -m "Fixes bug #31415"

### Änderungen übertragen (push)

Sobald commits vorliegen, möchte man diese sicherlich an den Hauptserver übertragen und öffentlich machen. Dies macht man mit dem `push`-Befehl, vorausgesetzt, man hat auch Schreibzugriff. In anderen Fällen muss man meistens Patches an die Entwickler schicken (z.B. bei týndur). Git bietet dafür ebenfalls komfortable Mechanismen, die in der git-Dokumentation zu finden sind.

Zum erfolgreichen push muss der tree jedoch ein wenig mit dem auf dem Hauptserver abgestimmt sein. Vorher ist also ein `git pull --rebase` zu empfehlen, um Konflikte zu vermeiden.

Da bei Subversion alle Commits direkt auf den Server kommen, gibt es hier keinen vergleichbaren Befehl. Der SVN-Befehl `commit` vereint sozusagen die Funktionalität von Gits `commit` und `push`

Beispiel:

    # Änderungen des Servers übertragen
    git pull --rebase

    # Eigene Änderungen auf den Server übertragen
    git push

### Ausblick

Oben werden nur sehr grundlegende Befehle genannt, die nur ein sehr begrenztes Arbeiten ermöglichen. Hier werden auch solche genannt, die oben aus Platzgründen nicht erwähnt werden, aber trotzdem sehr wichtig sind. Dieser Absatz soll ein Anreiz sein, die Befehle in der Git-Dokumentation oder mit Hilfe von `man` nachzuschlagen. Bei `man` findet man diese Befehle unter dem Namen `git-<BEFEHL>`.

Um erstmal ein eigenes Archiv anzulegen, sollte man den Befehl `init` kennen. Außerdem wird man sicherlich oft die Git-Befehle `diff`, `log` und `status` brauchen. Um Fehler in der History zu korrigieren muss man sicher auch einmal die Befehle `reset` oder `revert` anwenden.

Sehr wichtig sind die Branching-Mechanismen. Mit den oben genannten Befehlen wäre es nur möglich auf einem Branch zu arbeiten. Davon ist grundsätzlich abzuraten; viele Projekte verbieten sogar das Arbeiten im Hauptzweig (*master*). Wichtige Branching-Befehle sind `branch`, `merge`, `rebase` und `checkout`.

Äußerst wichtig für das Aktualisieren des Trees während der täglichen Arbeit ist `stash`, das es ermöglicht, die Änderungen an seiner Arbeitskopie zwischenzuspeichern und einen saubere Arbeitskopie zum `pull`en zu bekommen.

Aber auch die bereits oben erklärten Befehle sollte man in der Dokumentation nachschauen, da alle noch interessante Parameter haben, die sicherlich zur Anwendung kommen.

## Beispiel-Konfigurationsdatei

git bietet die Möglichkeit, in Konfigurationsdateien einige Einstellungen dauerhaft vorzunehmen, die man sonst jedes Mal über Kommandozeilenparameter angeben müsste. Es gibt dabei zwei verschiedene Konfigurationsdateien: ~/.gitconfig gilt für alle Repositories, .git/config liegt im Verzeichnis jedes einzelnen Repositorys und gilt nur für dieses. Für die globalen Einstellungen empfiehlt sich zumindest die folgenden Optionen anzugeben (die Werte natürlich anpassen, wo nötig):

    [user]
       name = Dein Name
       email = mail@dres.se
    [color]
       branch = auto
       diff = auto
       status = auto
    [color "branch"]
       current = yellow reverse
       local = yellow
       remote = green
    [color "diff"]
       meta = yellow bold
       frag = magenta bold
       old = red bold
       new = green bold
    [color "status"]
       added = yellow
       changed = green
       untracked = cyan
    [sendemail]
        chainreplyto = false
        smtpserver = smtp.mail-provider.de
        smtpuser = smtpuser
    [format]
        numbered = auto
    [merge]
        tool = vimdiff

In der projektspezifischen Konfigurationsdatei kann man z.B. die Mailadresse einstellen, an die git-send-email seine Mails schicken soll:

    [sendemail]
        to = tyndur-devel@tyndur.org

Weitere Einstellungsmöglichkeiten werden in den Manpages der einzelnen git-Befehle beschrieben.

## Tipps & Tricks

### Branch im Remote-Archiv löschen

Über

    git push <Remote-Archiv> :heads/<Branch>

kann der Branch \<Branch\> im Remote-Archiv \<Remote-Archiv\> (typischerweise *origin*) gelöscht werden.

## Vergleich zu Subversion

Wie bei so vielen konkurrierenden Projekten gibt es auch viele Meinungen, Diskussionen und Flamewars bei der Frage, welches SCM das beste sei. Git und [Subversion](https://github.com/lowlevel-eu/wiki/wiki/Subversion "Subversion") werden oft direkt miteinander verglichen, was einerseits mit der Popularität beider Systeme zusammenhängt, aber vielleicht auch mit den starken Meinungen von Linus Torvalds gegenüber Subversion (und insbesondere [CVS](https://github.com/lowlevel-eu/wiki/wiki/Concurrent-Versions-System "CVS")). Dieser Abschnitt nimmt sich der wichtigsten Argumente an, und soll als Entscheidungshilfe dienen.

### Vorteile von git

Das dezentrale System von git bietet viel Komfort für Programmierer. Anders als bei Subversion kann auch jeder, der nicht zum Kernentwicklerteam gehört, und keinen Schreibzugriff auf das Archiv hat, jederzeit alle Möglichkeiten, die das SCM bietet, ausnutzen. Niemand hindert den Entwickler daran, in seinem Archiv commits zu machen. So wird ein Programmierer viel eher ordentliche, atomare commits machen, auch wenn diese instabil und ungetestet sind, als bei zentralen Systemen, wo ein ungetesteter commit bedeuten würde, dass jeder Entwickler nun eine instabile Version zum arbeiten bekommt. Außerdem wird so den Entwicklern das Erstellen von Patches, die früher oder später zur Mailingliste müssen, komfortabler gemacht.

### Nachteile von git

*TODO: Lass sich hier mal einer was einfallen \*g\**

## Kostenloses Git-Hosting

Für den Hobby-Betriebssystementwickler ist es sicherlich irgendwann wichtig, dass das Projekt veröffentlicht wird, und jeder einfachen Zugriff auf den Sourcecode hat. Daher gibt es hier eine Liste von kostenlosen git-Hostern.

Falls ihr ebenfalls empfehlenswerte, kostenlose Hoster kennt, oder Kommentare zu den hier aufgelisteten habt, dann zögert nicht, diese hier hinzuzufügen

- [repo.or.cz](http://repo.or.cz): Nur grundlegende Funktionen.

<!-- -->

- [Github](http://github.com): Kostenlos für Open-Source-Projekte. Bietet weitere Features, zum Beispiel Beobachtungslisten für die Aktivitäten anderer Entwickler und Projekte.

<!-- -->

- [Gitorious](http://gitorious.org): Viele Features wie Wikis, mehrere Repos pro Projekt möglich

<!-- -->

- [SourceForge](http://sourceforge.net): Bietet noch Support für andere SCMs.

<!-- -->

- [Bitbucket](http://bitbucket.org): Bietet u. a. kostenlose private Repos für bis zu 5 bzw. für Studenten für unbegrenzt viele Benutzer an.

## Weblinks

- [Git bei Wikipedia](http://de.wikipedia.org/wiki/Git)

<!-- -->

- [Git Homepage](http://git-scm.com/) (englisch)

<!-- -->

- [Git Dokumentation, Anfängertutorial und Crashkurs für SVN-Umsteiger](http://git-scm.com/documentation) (englisch)

<!-- -->

- [Rede von Linus Torvalds über git](http://www.youtube.com/watch?v=4XpnKHJAok8) (englisch)

<!-- -->

- [Transskription dieser Rede](http://git.or.cz/gitwiki/LinusTalk200705Transcript) (englisch)

<!-- -->

- [Eine FAQ zu Git, die fast alle geläufigen Probleme lösen kann](http://git.wiki.kernel.org/index.php/GitFaq) (englisch)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/10976/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1889/index.html)

<!-- MediaWiki page 1889; revision 10976; parent 8366; 2012-12-29T00:23:18Z -->
