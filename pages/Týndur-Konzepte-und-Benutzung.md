# Týndur/Konzepte und Benutzung

Die folgenden Abschnitte geben eine kurze Einführung für alle, die mit den Konzepten und der Benutzung von [týndur](T%C3%BDndur "Týndur") nicht ganz so vertraut sind.

## Der Bootvorgang

Der Bootvorgang von týndur läuft grob in zwei Phasen ab: týndur benutzt [Multiboot](Multiboot "Multiboot"), um den [Kernel](Kernel "Kernel") und einige erste Module zu laden (z. B. Platten- und Dateisystemtreiber), so dass Zugriff auf das eigentliche týndur-Dateisystem möglich ist. Diese Module werden von [GRUB](Grand-Unified-Bootloader "GRUB") geladen und ihr Aufruf kann deshalb im Bootmenü geändert werden. Anschließend lädt servmgr die Konfiguration vom [Dateisystem](Dateisystem "Dateisystem") und lädt weitere Module nach (z. B. Konsole oder Netzwerktreiber).

Damit servmgr das System booten kann, braucht er die Angabe des týndur-Dateisystems als Parameter (vergleichbar zu *root=...* für Linux). Der im Bootmenü voreingestellte Pfad beginnt mit *ata:/ata00_p0* für das Festplattenimage und *ata:/cdrom* für die Live-CD. Insbesondere bei der Live-CD kann es nötig sein, diese Einstellung zu ändern, wenn der Rechner über zwei CD-Laufwerke verfügt und das falsche als *ata:/cdrom* benutzt wird. Beispiele für mögliche Angaben:

- *ata:/ata00_p0* steht für die erste Partition auf einer Festplatte an Primary Master
- *ata:/atapi10* steht für ein CD/DVD-Laufwerk an Secondary Master
- *ata:/ata11* steht für ein Dateisystem auf einer unpartitionierten Festplatte an Secondary Slave
- *ata:/cdrom* steht für das „erstbeste“ CD/DVD-Laufwerk

Manchmal kommt es bei der Benutzung von [DMA](Direct-Memory-Access "DMA") mit dem ata-Modul zu Problemen (insbesondere mit VirtualBox). In diesem Fall kann es helfen, die ata-Kommandozeile im Bootmenü auf „module /modules/ata nodma“ zu ändern.

## Terminal und Shell

Wenn servmgr alle Module geladen hat, stehen mehrere virtuelle Terminals zur Verfügung. Standardmäßig kann auf den ersten vier Terminals eine Shell gestartet werden. Die Terminals können über Alt-F1 bis Alt-F4 ausgewählt werden. Alt-F9 wählt das Service-Terminal aus, auf dem von servmgr geladene Treiber ihre Meldungen ausgeben. In den Terminals kann mit Shift-Bild Auf/Ab gescrollt werden.

Zur grundlegenden Orientierung im Dateisystem sei gesagt, dass sich ausführbare Dateien an drei verschiedenen Stellen befinden: Zunächst ist das *file:/apps*, das alle Anwendungsprogramme des Kernsystems enthält. Das zweite ist *file:/system/lpt-bin*, das die ausführbaren Dateien per lpt installierter Pakete enthält – genauer gesagt enthält es symbolische Links auf die eigentlichen ausführbaren Dateien unter *file:/packages*. Beide bereits genannten Verzeichnisse sind in PATH, die Programme können also ohne explizite Pfadangabe gestartet werden. Schließlich existiert noch *file:/modules*, das [Treiber](Treiber "Treiber") und sonstige Services enthält.

Um ein Programm im Vordergrund zu starten, gibt man seinen Dateinamen ein (wenn es weder im aktuellen Verzeichnis noch in PATH liegt, den Pfad zur Datei). Um es im Hintergrund zu starten (empfiehlt sich für Servies aus *file:/modules*), wird der Befehl start benutzt (z. B. „start /modules/ramdisk“).

## Dateisystem und Pfade

Die Pfade, die unter týndur Verwendung finden, unterscheiden sich ein wenig von den üblichen Konzepten und sind daher auch eine kurze Erläuterung wert. Wie man bereits am Dateinamen „file:/apps/sh“ erkennt, bestehen Pfade anders als unter Unix nicht nur aus dem Verzeichnis und einem Dateinamen, sondern auch noch aus einem dritten Teil, der angibt, welcher Service die Datei zur Verfügung stellt. Soweit ist das Konzept noch ganz grob mit Laufwerksbuchstaben unter DOS vergleichbar.

Das Besondere an týndur-Pfaden ist, dass sich diese Pfade zu längeren kombinieren lassen: Während „ext2:/“ noch unvollständig wäre, ergibt es kombiniert mit dem Pfad zu einer Festplattenpartition schon sehr viel mehr Sinn: „ata:/ata00_p0\|ext2:/“. Der Aufbau der Live-CD erzeugt dabei mehrfach kombinierte Pfade: „ata:/cdrom\|iso9660:/hd.img\|ramoverlay:/cached\|ext2:/“ bedeutet, dass sich auf dem Laufwerk *ata:/cdrom* ein ISO-9660-Dateisystem befindet, auf dem ein Image *hd.img* liegt, über das wiederum eine Ramdisk gelegt wird (damit auf das Dateisystem geschrieben werden kann, obwohl es sich um eine CD handelt), die schließlich ein ext2-Dateisystem enthält.

Um solch umständliche Pfade zu vereinfachen, existiert der Service *file*, der ein Alias für Pfade bereitstellt. Die Zuordnung der Pfade ist auch auf dem Service-Terminal sichtbar.

## Netzwerk

Beim ersten Start des Systems wird die Netzwerkkonfiguration gestartet. Falls ein passender Treiber für die Netzwerkkarte verfügbar ist ([rtl8139](RTL8139 "RTL8139"), sis900, e1000, ne2k, [pcnet](AMD-PCnet "AMD PCnet")), wird er automatisch erkannt. Die Einstellungen für die IP-Adresse und den Gateway müssen eventuell angepasst werden. Sie sind so voreingestellt, dass sie mit den Standardeinstellungen von [QEMU](QEMU "QEMU") funktionieren. Als DNS-Server wird OpenDNS verwendet (kann durch einen Parameter „ns=a.b.c.d“ beim Aufruf von tcpip geändert werden).

Wenn eine Internetverbindung besteht, ist ein schneller Weg, um das Netzwerk zu testen, eine DNS-Adresse aufzulösen: „cat tcpip:/dns/www.tyndur.org“. Es ist auch möglich eine einfache telnet-artige Verbindung zu einem anderen Rechner aufzubauen: „pipe tcpip:/192.168.1.1:1234“. Die Verbindung wird beendet, wenn „EOF.“ auf einer eigenen Zeile eingegeben wird.

## Software bauen

Um auf týndur Software zu entwickeln (oder zumindest zu kompilieren) stehen gcc für C-Programme, FPC für Pascalprogramme sowie nasm, yasm und fasm für Assembler zur Verfügung. Auf der großen Variante der Live-CD sind diese alle bereits vorinstalliert; in der kleinen Variante oder auf das Festplatten-Image können sie nachinstalliert werden. Beispielhaft die Installation von gcc und yasm:

    # lpt scan
    # lpt get gcc
    # lpt get yasm

Wenn die Compiler und Assembler installiert sind, können sie wie gewohnt benutzt werden (allerdings ist etwas Geduld nötig, die Compiler gehen sehr gemächlich zu Werke). Als Editoren stehen kedit sowie nano zur Verfügung (letzterer muss ggf. per lpt nachinstalliert werden). kedit beherrscht Syntaxhighlighting, das per F8 aktiviert werden kann. Als Versionsverwaltungssystem kann [Subversion](Subversion "Subversion") benutzt werden.

Programme, die aus mehr als einer Datei bestehen, werden am besten mit „build“ gebaut. Es sammelt Dateien aus einer Verzeichnisstruktur wie für den týndur-Code verwendet zusammen und baut daraus eine Binary, die „run“ genannt wird. Als einfaches Beispiel wollen wir die týndur-Shell neu kompilieren:

    # svn co svn://tyndur.org/tyndur/tags/0.2.2/src/modules/c/shell
    # build

Es geht mit ein wenig Geduld allerdings auch etwas umfangreicher, nämlich unter týndur einen týndur-Kernel bauen (dauert gut 5 bis 10 Minuten). Die Besonderheit dabei ist, dass nicht die normale Standardbiblithek benutzt werden darf (deswegen build -k), sondern diejenige, die auch beim Bauen unter Linux verwendet wird (deswegen checken wir sie extra aus). Insgesamt sieht das folgendermaßen aus:

    # mkdir kernel
    # cd kernel
    # svn co svn://tyndur.org/tyndur/tags/0.2.2/src/include
    # svn co svn://tyndur.org/tyndur/tags/0.2.2/src/lib
    # svn co svn://tyndur.org/tyndur/tags/0.2.2/src/kernel
    # cp kernel/src/kernel.ld .
    # build -k

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/10794/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2238/index.html)

<!-- MediaWiki page 2238; revision 10794; parent 7750; 2012-09-11T08:29:25Z -->
