# Týndur/Entwicklung

**týndur** ist ein Community-Betriebssystem von der Community für die Community. Das heißt, jeder kann mitmachen. Ob man nun ein Programm für týndur schreiben oder portieren will, auf die Suche nach Bugs gehen möchte und selbige fixen will oder ob man Treiber entwickeln will: Jeder ist herzlich eingeladen.

Dieser Artikel soll die Entwicklung für týndur erklären und führt in die Benutzung von git ein, erläutert, wie man Patches an die Mailingliste sendet und wie man mit lbuilds umgeht.

  

## Überblick

Generell sieht der Entwicklungsvorgang so aus:

- Repository clonen/updaten
- Bug fixen/Programm schreiben/Programm portieren/Treiber schreiben
- Testen
- Commit erstellen
- Patch erstellen
- An die Mailingliste schicken

An die Mailingliste geschickt wird nun vom Projektleiter taljeth bzw. [FreakyPenguin](https://lowlevel-eu.github.io/wiki/pages/1460/index.html "Benutzer:FreakyPenguin") entschieden, ob der Patch in das Repository kommt oder nicht.

Ob ein Patch ins Repository kommt hängt davon ab, ob er sinnvoll ist und letzenendes funktioniert.

  

## Vorbereitungen

### Quellen beziehen

Um für týndur zu entwickeln braucht man die aktuellsten Quellen. Diese bezieht man am besten direkt per [git](https://github.com/lowlevel-eu/wiki/wiki/Git "Git") aus dem [týndur-Repository](http://git.tyndur.org):

` git clone ``git://git.tyndur.org/tyndur.git`` `

Je nach Internetverbindung dauert es ein paar Minuten, bis die ~5 MiB Quellcode heruntergeladen sind.

Für lbuilds läuft es fast ähnlich:

` git clone ``git://git.tyndur.org/lbuilds.git`` `

### Auf der Mailingliste anmelden

Die Mailingliste ist ein sehr wichtiges Informationsmedium in der tyńdur-Entwicklung. Dorthin werden alle Patches geschickt. Die Anmeldung ist natürlich kostenlos und die E-Mail-Adresse wird keiner Werbefirma o.ä. weitergegeben, auch bekommt man keine Mails über Potenz-steigernde Mittel.

Einfach [hier](http://list.tyndur.org) auf der Mailingliste mit einer vorhandenen E-Mail-Adresse eintragen (**Nicht vergessen** in der Bestätigungs-Email den Bestätigungs-Link anzuklicken!)

### Den IRC-Channel besuchen

Fast noch wichtiger als die Mailingliste selbst und die Anlaufstelle Nummer 1 ist der Channel zu týndur im euIRC. Dort sind viele aus der Community aktiv sowie die Projektleiter. Einfach mal in den Channel \#lost reinschauen und ruhig Fragen stellen, sie werden sicher gern beantwortet.

  

## Mit der Entwicklung beginnen

### Programme schreiben

Alle nativen týndur-Programme befinden sich im Verzeichnis src/modules/c (Windows-User denken sich die Slashes weg und ersetzen selbige druch Backslashes). Die Anzahl der Programme ist aktuell recht überschaubar. Ob man nun ein Programm extra für týndur entwickeln möchte oder ob portieren sinnvoller ist, hängt von der Art des Programms ab:

Es ist sicherlich sehr sinnvoll, ein Programm zur Festplattenpartionierung (siehe fdisk im c-Verzeichnis) selber zu schreiben, aber vielleicht nicht so sinnvoll, einen C-Compiler selber zu schreiben. Letzteres portiert man dann lieber.

Man kann ruhig im Forum oder im IRC nachfragen, welche Anwendungen denn gewünscht sind. Man kann auch z.B. die Komandozeilentools (in sh/cmds) erweitern oder neue schreiben.

Wenn man also ein neues Programm entwickelt, erstellt man einfach ein neues Verzeichnis in src/modules/c, am besten nach dem Namen des Programms (bsp. meinprog). In das Verzeichnis kopiert man sich eine Makefile.all aus einem anderen Programmverzeichnis und passt die Namen entsprechend an.

  

### Programme portieren

Wenn es sich nicht lohnt, ein Programm selbst zu schreiben, so wird ein vorhandenes portiert. Es wurden schon wichtige Tools wie die binutils, der gcc und der fpc nach týndur portiert, weitere Anwendungen wie mutt (Mail-Client), Python etc. sind in Arbeit. Wenn man ins lbuild-Repo schaut, sieht man schon angefangene/portierte Anwendungen. Wenn hier eine fehlt oder man eine Anwendung portieren möchte, ist hier wieder die beste Anlaufstelle der IRC-Channel.

Generell ist die Portierung eines Programms nicht so aufwändig wie das Neuschreiben, allerdings dennoch mit einem gewissen Aufwand verbunden.

  

### Treiber entwickeln

týndur hat schon einige Treiber, darunter für die Tastatur, Maus, Diskettenlaufwerk, Festplatte und einige Dateisystemtreiber sowie auch zwei Netzwerkkartentreiber. Neue Treiber werden mithilfe vom **Common Driver Interface**, kurz [CDI](https://github.com/lowlevel-eu/wiki/wiki/Common-Driver-Interface "CDI"), entwickelt, einer Schnittstelle, die das Programmieren von plattform-unabhänigen Treibern ermöglicht. So viele unterschiedliche Hardware es gibt, so viele unterschiedliche Treiber muss es geben. Hier wird allerdings dringend empfohlen, im IRC-Channel nachzufragen, ob nicht schon ein Community-Mitglied an einem Treiber arbeitet.

Wer also einen neuen Treiber entwickeln möchte, erstellt ein Verzeichnis in src/modules/cdi.

  

### Bugs fixen

Nobody's perfect, auch nicht die týndur-Entwickler. Deshalb schleichen sich Fehler ein und Bugs entstehen. Wer einen Bug findet, kann, nein, sollte ihn sogar fixen. Hier sei allerdings auf ausgiebiges Testen hingewiesen, denn allzuoft wird aus dem Bugfix ein zweiter Bug.

Auch sollte man überprüfen, ob der Bug nicht vielleicht doch eine Programmfunktion ist ;)

  

## Entwicklungsstand veröffentlichen

Hat man nun ein Programm geschrieben oder portiert, einen Treiber entwickelt oder einen Bug gefixt, so möchte man natürlich, dass die Welt und speziell die anderen Entwickler etwas davon mitbekommen.

### Commit erstellen

Nun muss erstmal ein Commit erstellt werden. Dazu nutzt man git add:

` git add src/modules/c/meinprog/* `

Obiger Befehl fügt zum Beispiel ein entwickeltes Programm namens "meinprog" ins lokale Repository ein. Hat man alle geänderten Dateien ins lokale Repo gespeist, wird nun ein Commit erstellt:

` git commit -s `

Nun öffnet sich der Standard-Editor (in der Regel vim). Nun kann man seinen Commit beschreiben. Dies sollte nach folgenden Regeln geschehen:

- 1\. Zeile ist der E-Mail-Betreff
- 2\. Zeile leer lassen
- 3\. Zeile Kurze Erläuterung zum Patch
- Neuer Absatz
- Änderung angeben

Die Änderung wird nach folgendem Schema angegeben:

- \+ Für neue Funktion
- \* Für Änderung
-  ! Für Bugfix

Nun eine neue Zeile einfügen und speichern. Der Commit wurde nun erstellt.

  

### Patch senden

Nun muss der Patch an die Mailingliste ankommen. Dazu wird der Patch per format-patch erstellt:

` git format-patch -1 `

Das -1 gibt an, der wie vielte Patch einer Patch-Reihe das ist, also in dem Fall 1.

Jetzt wird der Patch an die Mailingliste gesendet:

` git send-email 000x-name-des-patches.patch --smtp-server smtp.emailprovider.td --smtp-user username --smtp-pass password --to tyndur-devel@tyndur.org `

Zur Erläuterung:

- 000x-name-des-patches.patch ist der per git format-patch erstelle Patch. x steht dabei für den wievielten Patch, in unserem Fall 1, name-des-patches ist bei git commit angegebene Betreffzeile (Leerstellen wurden durch Bindestriche ersetzt)
- Bei --smtp-server musst der SMTP-Server des EMail-Providers angegeben werden
- Bei --smtp-user der Username
- Bei --smtp-pass das Passwort

Im nun folgendem Dialog wird gefragt, von woher die EMail kommen soll, sofern keine Änderung gewünscht ist einfach Enter drücken, dann wird nach der ID der Mail gefragt, hier eine 1 eintragen. Wenn alles geklappt hat ist der Patch nun auf der Mailingliste angekommen (sofern man nicht die Anmeldung auf selbiger vergessen hat).

Wenn nun von taljeth oder [FreakyPenguin](https://lowlevel-eu.github.io/wiki/pages/1460/index.html "Benutzer:FreakyPenguin") ein sogenanntes "Acked-by" an die Mailingliste gesendet wird, wurde der Patch akzeptiert und ladent im Repository.

  

## Siehe auch

- [Týndur/Bochs](https://github.com/lowlevel-eu/wiki/wiki/T%C3%BDndur-Bochs "Týndur/Bochs")
- [Týndur/Wunschliste](https://github.com/lowlevel-eu/wiki/wiki/T%C3%BDndur-Wunschliste "Týndur/Wunschliste")
- [Týndur/Ressourcen](https://github.com/lowlevel-eu/wiki/wiki/T%C3%BDndur-Ressourcen "Týndur/Ressourcen")

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/5583/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2035/index.html)

<!-- MediaWiki page 2035; revision 5583; parent 5582; 2009-08-12T08:12:04Z -->
