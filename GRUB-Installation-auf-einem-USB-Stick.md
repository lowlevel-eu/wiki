# GRUB Installation auf einem USB-Stick

Diese Seite oder Abschnitt ist zwar komplett, es wird aber folgende Verbesserungen gewünscht:  

*Tutorial fertigschreiben*

Hilf Lowlevel, den Artikel zu verbessern.

  
Nun da ich mich seit einiger Zeit damit beschäftige, auf meinem USB-Stick [GRUB](https://github.com/lowlevel-eu/wiki/wiki/Grand-Unified-Bootloader "GRUB") zu installieren möchte ich hier eine Schrit für Schritt Anleitung geben, wie man GRUB installiert.  
Der Stick sowie das BIOS/EFI müssen allerdings einige Bedingungen erfüllen. Das heißt, es geht mit dem USB-Stick, auf dem "Bootable Device" o.ä. darauf steht. Dies steht nicht überall, weil nicht jeder Hersteller sich an die Spezifikation für das verhalten der Sticks beim booten hält. Genauere Informationen sind [hier](http://www.usb.org/developers/devclass_docs/usb_msc_boot_1.0.pdf) zu finden. Es kann aber durchaus sein, dass man von dem Stick booten kann, obwohl dieser nicht als Bootable gekennzeichnet ist.  
Des Weiteren muss im [BIOS](https://github.com/lowlevel-eu/wiki/wiki/Basic-Input-Output-System "BIOS")/EFI die Möglichkeit gegeben sein, ein USB Speichermedium in der Bootreihenfolge auszuwählen. Dies ist, falls es unterstützt wird zumeist als USB-HDD angegeben. Ist nur ein USB-FDD zu finden, so funktioniert dies nicht, da USB-FDD ein Eintrag für externe USB-Diskettenlaufwerke ist.

## Löschen der Dateien

In diesem Abschnitt werden der Inhalt des USB-Sticks mit Null-Bytes überschrieben, damit überhaupt nichts mehr darauf vorhanden ist.

**Warnung**

Sichert vorher alle Daten von dem Stick, denn spätestens nach dem überschreiben des Stick-Inhalts mit Null-Bytes werden diese **nicht wiederherstellbar** sein!

### Löschen der Daten unter Linux/Unix

Zuerst sollte man nachschauen, wo der USB-Stick hin gemountet wurde, falls das automatisch geschehen ist. Dies kann man mit dem Befehl mount machen:

    $ mount
    /dev/hda1 on / type ext3 (rw,errors=remount-ro)
    proc on /proc type proc (rw,noexec,nosuid,nodev)
    sysfs on /sys type sysfs (rw,noexec,nosuid,nodev)
    /dev/sda1 on /mnt type vfat (rw)                    <-- diese Zeile ist relevant

Zumeist liegt der Stick an der Stelle /dev/sda o.ä. zumindest war es bei mir so. Bevor der Inhalt des Sticks allerdings überschrieben werden kann, sollte er ausgehängt werden, damit kein Programm auf diesen zugreifen kann. Dies geschieht wie folgt:

    $ umount /dev/sda1

Nun wird der komplette Stick mit Null-Bytes überschrieben. Dies wird wie folgt gemacht:

    $ cat /dev/zero > /dev/sda
    cat: write error: No space left on device

**Warnung**

**/dev/sda** kann durchaus auch deine Festplatte sein. Falls du dir also nicht sicher bist: ***nicht*** einfach ausprobieren

Wird die untere Fehlermeldung ausgegeben, so heißt das, dass der USB-Stick komplett überschrieben wurde. Ab hier gibt es denke ich mal keine Möglichkeit mehr noch eventuelle Daten zu sichern, da alles überschrieben wurde.  
Ein anderer Weg, den Stick von den Daten zu befreien, wäre der folgende:

    $ dd if=/dev/zero of=/dev/sda
    dd: Schreiben in „/dev/sda“: Auf dem Gerät ist kein Speicherplatz mehr verfügbar
    2007041+0 Datensätze ein
    2007040+0 Datensätze aus
    1027604480 Bytes (1,0 GB) kopiert, 349,675 s, 2,9 MB/s

### Löschen der Daten unter Windows

dd wurde nach [Windows](https://github.com/lowlevel-eu/wiki/wiki/Windows "Windows") portiert und ist hier erhältlich: [DD für Windows](http://www.chrysocome.net/dd)  
Um zu schauen, welches Laufwerk der USB-Stick ist, muss dd mit dem Parameter --list aufgerufen werden. Dieser existiert allerdings nur in der Version für Windows

    > dd --list

In der Auflistung muss man nun nach dem Laufwerksbuchstabe schauen, an dem der Stick von Windows abgelegt wurde. Bei mir war das G! Als nächstes müssen nun die kompletten Daten gelöscht werden:

    > dd if=/dev/zero of=\\.\g: -count=1G -bs=1M --progress

*Anmerkung: Diese Aktion kann je nach größe des USB-Sticks einige Zeit in Anspruch nehmen.*  

## Formatieren des Sticks

In diesem zweiten Abschnitt bekommt der USB-Stick ein neues [Dateisystem](https://github.com/lowlevel-eu/wiki/wiki/Dateisystem "Dateisystem"). Das Dateisystem meiner Wahl ist ext2, kann aber durchaus auch ein anderes, wie FAT32 oder so sein.

### Formatieren der Partition des Sticks unter Linux/Unix

Bevor der Stick formatiert wird, sollte eben jener zuerst partitioniert werden, da die Partition ja durch Null-Bytes ersetzt wurde. Um den USB-Stick zu partitionieren, muss einfach nur cfdisk oder fdisk mit der Stelle angeben, unter der der Stick von der jeweiligen Maschine verwaltet wird, was in dieser Anleitung /dev/sda ist. Also lautet der Aufruf wie folgt:

    $ cfdisk /dev/sda
    .... oder ....
    $ fdisk /dev/sda

Nun muss mit dem jeweiligen Programm eine Partition erstellt werden, was in meinem Falle ext2 ist. Nach dem Schreiben der Partitions-Tabelle, wird eben jene neu eingelesen. Jedoch kann beim neuen Einlesen der Partitions-Tabelle unter umständen der Fehler auftreten, das der Stick nicht wieder eingelesen werden kann, was allerdings vernachlässigt werden kann. Im nächsten Schritt muss der Stick nun mit einem Dateisystem formatiert werden. Dies wird wie folgt gemacht:

    $ mkfs.ext2 /dev/sda1

Hier wird der Stick, nach drücken der Return-Taste, mit dem Ext2 Dateisystem formatiert.  

### Formatieren der Partition des Sticks unter Windows

Unter Windows reicht es, den USB-Stick einfach formatieren zu lassen, da hier gleichzeitig dann auch eine Partition angelegt wird. Formatieren kann man den Stick im Arbeitsplatz. Hierzu muss das Kontext-Menü mit einem Rechtsklick auf den Laufwerksbuchstaben geöffnet werden. In diesem Menü kann dann über den Eintrag "Formatieren..." den Stick mit dem Dateisystem FAT32 formatieren.

## Installieren von GRUB

### Installation unter Linux/Unix

Nun muss der Formatierte Stick wieder gemountet werden:

    # mount /dev/sda1 /media/usb

Im nächsten Schritt sollten nun die nötigen Ordner für GRUB erstellt werden:

    $ mkdir -p /media/usb/boot/grub

Nun müssen die Bootdateien von GRUB in den erstellten Ordner /media/usb/boot/grub kopiert werden.

    $ cp /usr/lib/grub/i386-pc/* /media/usb/boot/grub/

Sollte obige Anweisung nicht funktionieren, weil das Verzeichnis nicht existiert, so ist ein anderer möglicher Pfad in der nun folgenden Anweisung. Man muss eigentlich nur das /usr entfernen.

    $ cp /lib/grub/i386-pc/* /media/usb/boot/grub/

Nun werden alle Dateien, die von GRUB benötigt werden auf den USB-Stick kopiert. Im letzten Schritt muss nun eine Datei mit dem Namen device.map erstellt werden, damit GRUB weiß, welche Laufwerksangabe für den USB-Stick gilt. Dies geschieht wie folgt:

    $ echo '(hd0)     /dev/sda' > /media/usb/boot/grub/device.map

Als letzter Schritt muss nun nur noch GRUB auf dem Stick installiert werden, was wie folgt gemacht wird:

    $ /sbin/grub-install --root-directory=/media/usb/ /dev/sda

Nun ist GRUB auf dem USB-Stick installiert und es kann von diesem gebootet werden.  
**Anmerkung:** Jeder USB-Stick kann bootbar gemacht werden. Im Internet herrscht der irrglaube, dass nur einige wenige Sticks bootbar sind, und zwar diese, wo das draufsteht. Das ist jedoch einfach gesagt Schwachsinn, da ein USB-Stick ein Speichermedium ist und solange das BIOS mit dem booten von USB-Sticks klar kommt wird das funktionieren.

### Installation unter Windows

Wie auch bei der Installation unter [Linux](https://github.com/lowlevel-eu/wiki/wiki/Linux "Linux")/Unix werden hier die GRUB Binarys benötigt, welche auf dem ftp-Server des Projekts zu finden sind: GRUB Legacy. Zur Benutzung empfehle ich die Version 0.97! GRUB Legacy wird zwar nicht mehr weiterentwickelt, allerdings gibt es von GRUB2 noch keinen stable-Release.  
  
Für die Installation von GRUB unter Windows gibt es ein kleines Tool, das sich "grubinstall.exe" nennt. Hiermit sollte es möglich sein, GRUB auf dem USB-Stick zu installieren. Man kann dieses kleine Tool [hier](http://www.geocities.com/lode_leroy/grubinstall/) herunterladen.

## Testen des USB-Sticks

*ToDo*

### Testen mit Bochs

Leider konnte ich keine brauchbaren Informationen dazu finden, wie man Bochs dazu bringt vom Stick zu booten.

### Testen mit qemu

*ToDo*

#### Testen unter Linux/Unix

Das booten des USB-Sticks unter Linux ist im Gegensatz zu der Vorgehensweise unter Windows etwas einfacher. Es wird einfach das Devicenode, das vom Kernel vergeben wird, benötigt. In diesem Beispiel ist das /dev/sda, da /dev/sda1 die Partition auf dem USB-Stick ist! Der Aufruf von qemu würde dann also so aussehen:

**Warnung**

Um ein physikalisches Gerät nutzen zu können, braucht man root-Rechte, da man als normaler Nutzer nicht auf die Devicenodes zugreifen darf.

    $ qemu -m 32 -localtime -boot c -hda /dev/sda

#### Testen unter Windows

Um unter qemu von dem USB-Stick booten zu lassen, muss der Stick als Festplatte angegeben werden. Dazu wird jedoch allerdings der Name des Geräts benötigt. Dieser ist wie folgt zu finden:

    Start->Ausführen

Hier wird dann "diskmgmt.msc" eingegeben und mittels Klick auf "OK" geöffnet. Hier muss nun der USB-Stick herausgesucht werden. Dieser hat den Titel "Datenträger" und dann noch eine Nummer, in diesem Fall die 5. Diese Nummer wird für qemu gebraucht, damit das richtige Gerät angesprochen werden kann. Welcher Eintrag nun der USB-Stick ist, kann mit mehreren Kriterien herausgefunden werden. Zum einen wäre da der Mountpunkt, also der buchstabe, z.B. "D:", zum anderen wird der Stick von Windows als Wechselmedium gespeichert, wodurch man einige Einträge ausschließen kann, wie z.B. interne Festplatten oder CD/DVD-Laufwerke. Der Aufruf von qemu könnte dann wie folgt aussehen:

    > qemu -L . -m 32 -localtime -boot c -hda \\\\.\\PhysicalDrive5

**Anmerkung:** Der Stick wird mit "PhysicalDrive" und der entsprechenden Nummer dahinter angesprochen. PhysicalDrive ist einfach nur der Englische Name für "Datenträger". Die vielen \\ sind aus dem Grund, da eben dieses Zeichen für die Verwendung mit qemu escaped werden muss.  
Wird dies so ausgeführt, sollte, falls nichts schief gelaufen ist, unter qemu dann GRUB vom USB-Stick geladen werden.

### Testen auf einer realen Maschine

Der Test auf einer realen Maschine sollte nicht unbedingt so schwer sein.  
Die einzige Vorraussetzung ist, dass das BIOS von einer USB-Festplatte booten können muss. Das heißt, man muss um dies zu aktivieren im BIOS bei den Geräten von denen gebootet werden soll den Eintrag "USB-HDD" einfügen, insofern dieser vorhanden ist. Andere Einstellungen, wie z.B. "USB-FDD" oder "USB-CDROM" funktionieren leider nicht.  
Ist dieser Eintrag ("USB-HDD") nicht vorhanden, muss ein BIOS-Update vorgenommen werden, wo dieser dann hoffentlich vorhanden ist.  
**Anmerkung:** Dieser Part steht hier unter vorbehalt, da ich schauen muss, ob nicht eventuell irgendwo noch eine Option vorhanden ist, mit der man das bootem von USB Festplatten verbieten kann. Dieser Part sollte dem zufolge also erst einmal \_**IGNORIERT**\_ werden

  
***Dieser Artikel ist unvollständig, wird noch erweitert und korrigiert***

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/6116/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1737/index.html)

<!-- MediaWiki page 1737; revision 6116; parent 5943; 2009-10-30T15:22:22Z -->
