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

Die folgenden Abschnitten beziehen sich primär auf Linux oder ähnliche Systeme. Dieser Artikel enthält weiter unten einen gesonderten Abschnitt, wie týndur [unter Windows](T%C3%BDndur-Entwicklung.md#entwicklung-unter-windows "Týndur/Entwicklung") gebaut und ausgeführt werden kann.

### Quellen beziehen

Um für týndur zu entwickeln braucht man die aktuellsten Quellen. Diese bezieht man am besten direkt per [git](Git.md "Git") aus dem [týndur-Repository](https://github.com/lowlevel-eu/tyndur):

` git clone ``https://github.com/lowlevel-eu/tyndur.git`` `

Je nach Internetverbindung dauert es ein paar Minuten, bis die ~5 MiB Quellcode heruntergeladen sind.

### Auf der Mailingliste anmelden

Die Mailingliste ist ein sehr wichtiges Informationsmedium in der tyńdur-Entwicklung. Dorthin werden alle Patches geschickt. Die Anmeldung ist natürlich kostenlos und die E-Mail-Adresse wird keiner Werbefirma o.ä. weitergegeben, auch bekommt man keine Mails über Potenz-steigernde Mittel.

Einfach [hier](http://list.tyndur.org) auf der Mailingliste mit einer vorhandenen E-Mail-Adresse eintragen (**Nicht vergessen** in der Bestätigungs-E-Mail den Bestätigungs-Link anzuklicken!)

### Den IRC-Channel besuchen

Fast noch wichtiger als die Mailingliste selbst und die Anlaufstelle Nummer 1 ist der Channel zu týndur im euIRC. Dort sind viele aus der Community aktiv sowie die Projektleiter. Einfach mal in den Channel \#lost reinschauen und ruhig Fragen stellen, sie werden sicher gern beantwortet.

## Mit der Entwicklung beginnen

### Umgebung aufsetzen

Wer einen 64-Bit-gcc hat, muss sich eine 32-Bit-libgcc installieren, da týndur diese benötigt.  
Unter Debian und Ubuntu heißt das nötige Paket ia32-libs, unter openSUSE libgcc\<Version\>-32bit (z. B. libgcc45-32bit) und unter Arch gcc-multilib aus dem multilib-Repository (*TODO*: Weitere Distributionen und Betriebssysteme ergänzen).

  
Wer nicht vorhat, portierte Programme (lbuilds) zu kompilieren und auch keinen Pascal-Code übersetzen möchte, kann diesen Abschnitt überspringen. Alle anderen müssen zunächst die lbuilds einrichten und dabei einen FPC-Crosscompiler erstellen. Im Idealfall muss man dazu einfach nur den Maketarget lbuilds-env ausführen:

    make lbuilds-env

Dadurch wird das lbuilds-Repository ausgecheckt und binutils, gcc, fpc udn fasm heruntergeladen und kompiliert (manchmal passen die Patches nicht mehr ganz auf die aktuelle FPC-Version, in diesem Fall melde man sich im Forum oder im IRC). Außerdem wird die libc von tyndur in das Verzeichnis lbuilds Unterverzeichnis kopiert. Achtung: Wenn man später Änderungen an der libc vornimmt, muss also **make lbuilds-env** erneut aufgerufen werden und alle lbuilds neu entpackt werden, damit die neue Version benutzt wird! Beim nächsten Bauen im tyndur-Verzeichnis werden nun auch die Pascal-Programme (z. B. lpt und kirc) erstellt. Ein lbuild kann nun über

    cd lbuilds && ./lbuild.sh <Pfad zur *.lbuild Datei irgendwo in lbuilds/<programm>/>

erstellt werden.

### Programme schreiben

Alle nativen týndur-Programme befinden sich im Verzeichnis src/modules/c (Windows-User denken sich die Slashes weg und ersetzen selbige durch Backslashes). Die Anzahl der Programme ist aktuell recht überschaubar. Ob man nun ein Programm extra für týndur entwickeln möchte oder ob portieren sinnvoller ist, hängt von der Art des Programms ab:

Es ist sicherlich sehr sinnvoll, ein Programm zur Festplattenpartionierung (siehe fdisk im c-Verzeichnis) selber zu schreiben, aber vielleicht nicht so sinnvoll, einen C-Compiler selber zu schreiben. Letzteres portiert man dann lieber.

Man kann ruhig im Forum oder im IRC nachfragen, welche Anwendungen denn gewünscht sind. Man kann auch z.B. die Komandozeilentools (in sh/cmds) erweitern oder neue schreiben.

Wenn man also ein neues Programm entwickelt, erstellt man einfach ein neues Verzeichnis in src/modules/c, am besten nach dem Namen des Programms (bsp. meinprog). In das Verzeichnis kopiert man sich eine Makefile.all aus einem anderen Programmverzeichnis und passt die Namen entsprechend an.

### Programme portieren

Wenn es sich nicht lohnt, ein Programm selbst zu schreiben, so wird ein vorhandenes portiert. Es wurden schon wichtige Tools wie die binutils, der gcc und der fpc nach týndur portiert, weitere Anwendungen wie mutt (Mail-Client), Python etc. sind in Arbeit. Wenn man ins lbuild-Repo schaut, sieht man schon angefangene/portierte Anwendungen. Wenn hier eine fehlt oder man eine Anwendung portieren möchte, ist hier wieder die beste Anlaufstelle der IRC-Channel.

Generell ist die Portierung eines Programms nicht so aufwändig wie das Neuschreiben, allerdings dennoch mit einem gewissen Aufwand verbunden.

  

### Treiber entwickeln

týndur hat schon einige Treiber, darunter für die Tastatur, Maus, Diskettenlaufwerk, Festplatte und einige Dateisystemtreiber sowie auch zwei Netzwerkkartentreiber. Neue Treiber werden mithilfe vom **Common Driver Interface**, kurz [CDI](Common-Driver-Interface.md "CDI"), entwickelt, einer Schnittstelle, die das Programmieren von plattform-unabhänigen Treibern ermöglicht. So viele unterschiedliche Hardware es gibt, so viele unterschiedliche Treiber muss es geben. Hier wird allerdings dringend empfohlen, im IRC-Channel nachzufragen, ob nicht schon ein Community-Mitglied an einem Treiber arbeitet.

Wer also einen neuen Treiber entwickeln möchte, erstellt ein Verzeichnis in src/modules/cdi.

  

### Bugs fixen

Nobody's perfect, auch nicht die týndur-Entwickler. Deshalb schleichen sich Fehler ein und Bugs entstehen. Wer einen Bug findet, kann, nein, sollte ihn sogar fixen. Hier sei allerdings auf ausgiebiges Testen hingewiesen, denn allzuoft wird aus dem Bugfix ein zweiter Bug.

Auch sollte man überprüfen, ob der Bug nicht vielleicht doch eine Programmfunktion ist. ;)

## Entwicklungsstand veröffentlichen

Hat man schließlich ein Programm geschrieben oder portiert, einen Treiber entwickelt oder einen Bug gefixt, so möchte man natürlich, dass die Welt und speziell die anderen Entwickler etwas davon mitbekommen.

### Commit erstellen

Nun muss erstmal ein Commit erstellt werden. Dazu nutzt man git add:

` git add src/modules/c/meinprog/* `

Obiger Befehl fügt zum Beispiel ein entwickeltes Programm namens "meinprog" ins lokale Repository ein. Hat man alle geänderten Dateien ins lokale Repo gespeist, wird nun ein Commit erstellt:

` git commit -s `

Danach öffnet sich der Standard-Editor (in der Regel vim). Dort kann man seinen Commit beschreiben. Dies sollte nach folgenden Regeln geschehen:

- 1\. Zeile ist der E-Mail-Betreff
- 2\. Zeile leer lassen
- Änderungen angeben

Die Änderung wird nach folgendem Schema angegeben:

- \+ Für neue Funktion
- \* Für Änderung
-  ! Für Bugfix

Nun eine neue Zeile einfügen und speichern. Der Commit wurde jetzt erstellt.

Beim Committen bitte darauf achten, dass aus einer logischen Änderung genau ein Commit (und damit später genau ein Patch) wird. Wenn Du also an zwei verschiedenen Baustellen gearbeitet hast, füg zunächst alle Änderungen, die zur ersten gehören, mit git add hinzu, mache einen Commit und wiederhole das ganze für den zweiten Teil.

### Patch senden

Nun muss der Patch an die Mailingliste ankommen. Dazu wird der Patch per format-patch erstellt:

` git format-patch -1 `

Das -1 gibt an, wie viele Patches zu der Patchserie gehören sollten, die exportiert werden soll. Das ist also in diesem Fall genau einer. Wenn es mehrere sind, kann man noch --cover-letter angeben, die einen \[PATCH 0/n\] erstellt, in dem üblicherweise der grobe Überblick über die ganze Serie gegeben wird.

Jetzt wird der Patch an die Mailingliste gesendet:

` git send-email 000x-name-des-patches.patch --smtp-server smtp.example.com --smtp-user username --to tyndur-devel@tyndur.org `

Zur Erläuterung:

- 000x-name-des-patches.patch ist der per git format-patch erstelle Patch. x steht dabei für den wievielten Patch, in unserem Fall 1, name-des-patches ist bei git commit angegebene Betreffzeile (Leerstellen wurden durch Bindestriche ersetzt). Bei einer Patchserie werden alle Patches auf einmal angegeben, am einfachsten über 00\*.patch.
- Bei --smtp-server muss der SMTP-Server des E-Mail-Providers angegeben werden
- Bei --smtp-user der Username
- Mit smtp-pass kann das Passwort angegeben werden - das ist aber im Allgemeinen eine schlechte Idee, weil das Passwort damit im Klartext in der History der Shell landet. Wenn man den Parameter weglässt, fragt git selber nach dem Passwort.
- Die Einstellungen können auch in der [git-Konfigurationsdatei](Git.md#beispiel-konfigurationsdatei "Git") gemacht werden, siehe git-send-email --help

Sollte dies nicht funktionieren, dann kann man den Mailserver auch weglassen. Git versendet die E-Mail dann über einen eigenen Mailserver und trägt nur die Adresse des Entwicklers als Absender ein:

` git send-email 000x-name-des-patches.patch --to tyndur-devel@tyndur.org `

Im nun folgendem Dialog wird gefragt, von woher die E-Mail kommen soll, sofern keine Änderung gewünscht ist einfach Enter drücken, dann wird nach der ID der Mail gefragt, auf die geantwortet werden soll - im Normalfall auch hier einfach Enter drücken. Wenn alles geklappt hat ist der Patch nun auf der Mailingliste angekommen (sofern man nicht die Anmeldung auf selbiger vergessen hat).

Der Patch muss dann zunächst auf der Mailingliste korrekturgelesen ("gereviewt") werden, bevor er von Leuten mit Commitrechten in das Repository eingepflegt wird. Wenn Du beim Korrekturlesen helfen willst, kannst Du auf einen Patch entweder mit einer Zeile wie *Acked-by: Max Mustermann \<max@mustermann.de\>* antworten und ihn so als korrekt bestätigen oder aber Deine Kritikpunkte zitieren und kommentieren.

## Entwicklung unter Windows

### Quellcode auschecken

- Falls kein git-Client vorhanden ist, msysgit herunterladen und installieren (<http://code.google.com/p/msysgit/downloads/list>)
  - Im Installationsprogramm eine der Optionen wählen, mit denen git in PATH eingetragen wird
- In cmd.exe *git clone https://github.com/lowlevel-eu/tyndur.git* ausführen (oder alternativ die Git-GUI benutzen)

### Buildumgebung aufbauen

Ein Crosscompiler, der ELF-Dateien erzeugen kann, nasm und MSYS werden benötigt. Für Details siehe [Crosscompiler für Windows](Crosscompiler-f%C3%BCr-Windows.md "Crosscompiler für Windows"). Durch Aufruf von *make* tyndur kompilieren. Später reicht in der Regel ein *make subdirs*, das das unter Windows zeitaufwendige Erzeugen der Makefiles weglässt.

### Ausführen

Wir brauchen hier einen [QEMU](QEMU.md "QEMU"), mindestens in Version 0.11.0, gern auch was neueres. Auf der Wikiseite ist eine Version verlinkt, die auf unserem Server liegt, falls das Internet nichts aktuelleres hergibt. Das Verzeichnis, in dem qemu liegt, am besten auch in PATH aufnehmen.

Unter Windows sind mir keine Möglichkeiten bekannt, ext2-Festplattenimages mit GRUB zu erstellen. Wir werden daher erst einmal einen etwas anderen Weg gehen: qemu kann Multiboot direkt booten und es kann Verzeichnisse als FAT-Festplatten zur Verfügung stellen.

Zunächst brauchen wir also ein Verzeichnis (*build/root*), das alle Dateien enthält, die tyndur zum Booten braucht. Ich habe dafür eine Batchdatei *buildroot.bat* mit folgendem Inhalt angelegt:

    sh build\scripts\updateroot
    xcopy /s /y build\root-common\*.* build\root\
    xcopy /s /y build\root-hd\*.* build\root\
    xcopy /s /y build\root-local\*.* build\root\

Anschließend muss qemu mit den passenden Parametern aufgerufen werden. Das macht bei mir eine *run.bat*:

    cd build\output\modules
    qemu-system-x86_64 -kernel ..\kernel\tyndur -initrd "init,pci,ata,fat,console servmgr:/term servmgr:/term,servmgr ata:/ata00_p0|fat:/ vterm:/vterm8/out ata fat console pci" -hda fat:../../root %*
    cd ..\..\..

Nach jeder Änderung muss *buildroot.bat* ausgeführt werden, danach kann tyndur über *run.bat* beliebig oft ausgeführt werden. Beachte, dass alle Änderungen am Dateisystem verloren gehen, wenn qemu beendet wird. Um das zu lösen, kann man entweder versuchen, die rw-Unterstützung von qemu zu benutzen (die aber als instabil bekannt ist), oder ein zusätzliches Image anlegen und das als zweite Festplatte einbinden.

## Siehe auch

- [Týndur/Bochs](T%C3%BDndur-Bochs.md "Týndur/Bochs")
- [Týndur/Wunschliste](T%C3%BDndur-Wunschliste.md "Týndur/Wunschliste")
- [Týndur/Ressourcen](T%C3%BDndur-Ressourcen.md "Týndur/Ressourcen")

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/9715/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2035/index.html)

<!-- MediaWiki page 2035; revision 9715; parent 9714; 2011-04-23T00:06:03Z -->
