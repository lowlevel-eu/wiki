# IRC

Im IRC-Channel *\#lost* auf *irc.euirc.net* bekommt man einerseits schnelle Hilfe auf kleine Probleme und kann andererseits auch Diskussionen über OS-Entwicklung im allgemeinen oder natürlich [Týndur](https://lowlevel-eu.github.io/wiki/pages/1795/index.html "Kategorie:Týndur") im speziellen führen.

## Verhaltensregeln im Channel

- Es wird weder geflucht, noch irgendeine andere Person oder deren Arbeit/Projekt beleidigt.
- Codestücke usw. über 5 Zeilen werden nicht direkt per Copy+Paste übertragen sondern als Link angegeben. Dazu benutzt man einen sogenannten Nopaste-Service wie zum Beispiel <http://pastebin.com>
- Statusnicks (bspw. „PNoob\|afk“) sind unerwünscht.
- Flooden, also sinnloses Aneinanderreihen von Buchstabenfolgen ist verboten.
- Bei irgendwelchen Verstössen kann es durchaus sein, dass man von einem Admin gekickt wird.
- Sollte das passieren, ist ein automatischer Rejoin verboten.
- Wird dies auch nicht eingehalten, kann das schnell zu einem Bann führen.
- Ist man gebannt, sollte man nicht versuchen, diese Sperre irgendwie zu umgehen oder anderswertig zu nerven!! Denn dann wird aus dem technischen Bann mit ziemlich großer Wahrscheinlichkeit eine persönliche Ächtung. Und mit der ganzen Community will man es sich ja schließlich nicht verscherzen, oder?
- Bei der Codierung des Clients ist darauf zu achten, dass UTF8 benutzt wird, da nicht alle Clients sauber mit mehreren Codierungen umgehen können.

## Schnell-Zugriff per Link

Es ist durchaus möglich, dass diese Möglichkeit bei Dir nicht funktioniert, da es auf den Browser und das genutzte IRC-Client Programm ankommt. Versuch es einfach, du wirst dann sehen, ob es geht.

irc://irc.euirc.net/lost

## Schnell-Zugriff zum Channel per CGIIRC

Falls man aus irgend einem Grund keinen IRC-Client installieren will oder kann, ist der Zugang über CGIIRC eine Alternative. Dieser arbeitet nur über HTTP und funktioniert somit auch hinter Firewalls und Proxies (also zum Beispiel etwas für in der Schule ;-)). Eine CGIIRC-Installation speziell für den \#lost-Channel kann [hier](http://cgiirc.tyndur.org/) gefunden werden. Es wird aber empfohlen, wenn möglich einen normalen IRC-Client zu verwenden, da die Anzahl der möglichen CGIIRC-Verbindungen von Seiten Euirc beschränkt sind.

## Schnell-Zugriff per Mibbit

Wenn du unseren CGI-IRC schonen willst, und trotzdem keinen Client installieren willst, dann nutze am besten den Mibbit-WebIRC-Client:

- Rufe [diese Seite](http://chat.mibbit.com) auf.
- Im Feld *IRC* wählst du im Dropdownmenü den Punkt *euIRC \[webirc\]*.
- Als Channel muss natürlich *\#lost* gesetzt sein.
- Solltest du deinen Nicknamen mit mit einem Passwort geschützt haben (NickServ), klicke auf *Auth* neben dem Dropdown für den IRC Server aus und gebe dein Passwort in das entsprechende Passwort-Feld ein.
- Dann gib noch im Feld *Nick* deinen Wunschnick an, und mit einem Klick auf *Go* geht es los!

## IRC-Start mit KVirc unter Windows

- Am Anfang ist ein IRC-Client nötig. Dafür ist KVIrc geeignet. Auf [\[1\]](http://www.kvirc.net/?id=releases&platform=win32) hat man auf den Eintrag bei "Neueste Ausgabe" zu klicken. Nun nur noch einen Server auswählen und wenig später ist KVIrc auf der Platte.

<!-- -->

- Um KVIrc zu installieren auf die Programmdatei doppelklicken und einfach immer "OK", "Weiter" klicken. Am Ende das Häckchen für den automatischen Start aktivieren/aktiviert lassen um KVirc gleich zu starten und einzurichten.

<!-- -->

- Jetzt öffnet sich automatisch ein Dialog für die Einrichtung. Bei Spitznamen kann man sich einen Namen geben, welcher dann später auch im Chat verwendet wird. Die restlichen Einstellung sind von geringerer Bedeutung, sodass man sie bedenkenlos einfach bei den Standardeinstellungen belassen kann. Am Schluss klickt man auf "Abschließen" und KVIrc öffnet sich.

<!-- -->

- Im geöffneten Unterfenster "Server" sucht man den Eintrag euIRC und wählt den Unterpunkt irc.euirc.net aus. Nach einem Klick auf "Jetzt Verbinden" beginnt sich der Client mit einem Server zu verbinden. Sollte eine Sicherheitsmeldung von WinXP erscheinen, kann kann man bedenkenlos "Nicht mehr blocken" anklicken um KVIrc überhaupt auszuführen können.

<!-- -->

- Jetzt kann man das Fenster "Server" mit einem Klick auf "OK" wegmachen. Im Fenster "Kanäle betreten" gibt man unter Name "#lost" (Um in den Chat-Raum der Lowlevel-Gemeinde zu kommen) ein, das Passwort-Feld lässt man leer. Nachdem man also den Raum betreten hat, kann man auch "Kanäle betreten" mittels "Schliessen" wegmachen. Geht ebenfalls mit dem join-Befehl

      /join #lost

<!-- -->

- Das oberste Fenster in KVIrc namens "#lost" kann man maximieren. Nun kann man unten rechts eine Nachricht eingeben und mit Enter abschicken.

<!-- -->

- Um mit einem einzelnen User zu sprechen, kann man rechts oben auf den entsprechenden Namen doppelklicken. Schon öffnet sich ein Chat-Fenster für ein Gespräch unter 2 Augen.

<!-- -->

- Per Rechtsklick auf einen User-Namen bekommt man weitere interessante Funktionen, wie "/whois X" um zu erfahren wer genau diese Person "ist".

<!-- -->

- Weiter Konfigurationen usw. findet man unter "Einstellungen" / "KVIrc konfigurieren"

## IRC-Start mit KVIRC unter Linux

Ich beschreibe hier für die Distrubutionen „Debian“ und „Suse“

- Suse

Unter Suse 10.0 werdet ihr die aktuelle Version in der Paketverwaltung (z.B. über YAST) finden. Die Benutzung gestaltet sich dann gleich wie im Folgenden für Debian beschrieben.

- Debian Sarge

Wenn man Debian frisch installiert hat (mit der sources.list der Standardinstallation), wird man KVIRC im Paketmanager installieren können. Jedoch ist diese Version in Sarge ziemlich alt (Benutzer von Etch oder Sid können einfach "aptitude install kvirc" benutzen). Deshalb beschreibe ich, wie man eine neue Version kompiliert.

Zuerst gehen wir zur Website, um die Sourcen herunterzuladen: ftp://ftp.kvirc.net/pub/kvirc/3.2.0/source/kvirc-3.2.0.tar.bz2 Nachdem wir den Quellcode heruntergeladen haben, entpacken wir ihn und gehen mit der Konsole ins Verzeichnis vom KVIRC.

    fabian@fabian:~$ cd Desktop/kvirc-3.2.0/kvirc-3.2.0/

Wenn wir da sind, geben wir configure ein.

    fabian@fabian:~/Desktop/kvirc-3.2.0/kvirc-3.2.0$ ./configure

Nun wird das System überprüft, ob auch alle benötige Pakete installiert sind. Der häufigste Fehler ist, dass QT nicht installiert ist, auch die dev-Pakete müssen installiert sein.

Nachdem das Überprüfen des Systems abgeschlossen ist, müssen wir es kompilieren. Dies geschieht mit „make“

    fabian@fabian:~/Desktop/kvirc-3.2.0/kvirc-3.2.0$ make

Nun kompiliert er alles. Danach „make install“ als root. Dann wird er das Programm ausführbar machen. Einfach danach \[ALT\]+\[F2\] da denn „kvirc“ eingeben und KVIRC startet.

Alles weitere Funktioniert wie beim [KVIRC unter Windows](#irc-start-mit-kvirc-unter-windows)

## Channel-Logs und Statistiken

Aufzeichnungen der Channelgespräche sind nach Tagen unterteilt unter [\[2\]](https://log.mq32.de/%23lost/) zu finden.

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/11521/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1463/index.html)

<!-- MediaWiki page 1463; revision 11521; parent 9073; 2020-09-18T13:56:31Z -->
