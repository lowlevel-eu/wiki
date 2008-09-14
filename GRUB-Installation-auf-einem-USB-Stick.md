# GRUB Installation auf einem USB-Stick

# GRUB Installation auf einem USB-Stick

## Vorbemerkung

Nun da ich mich seit einiger Zeit damit beschäftige, auf meinem USB-Stick GRUB zu installieren möchte ich hier eine Schrit für Schritt Anleitung geben, wie man GRUB installiert.  

## Der USB-Stick

**ACHTUNG: Sichert vorher alle Daten von dem Stick, denn spätestens nach dem überschreiben des Stick-Inhalts mit Null-Bytes werden diese nicht wiederherstellbar sein!**

### Löschen der Dateien

In diesem Abschnitt werden der Inhalt des USB-Sticks mit Null-Bytes überschrieben, damit überhaupt nichts mehr darauf vorhanden ist.

#### Löschen der Daten unter Linux/Unix

Zuerst sollte man nachschauen, wo der USB-Stick hin gemountet wurde, falls das automatisch geschehen ist. Dies kann man mit dem Befehl mount machen:

    mount

    ''Beispielausgabe einfügen''

Zumeist liegt der Stick an der Stelle /dev/sda1 o.ä. zumindest war es bei mir so. Nun wird der komplette Stick mit Null-Bytes überschrieben. Dies wird wie folgt gemacht:

    cat /dev/zero > /dev/sda1
    cat: write error: No space left on device

Wird die untere Fehlermeldung ausgegeben, so heißt das, dass der USB-Stick komplett überschrieben wurde. Ab hier gibt es denke ich mal keine Möglichkeit mehr noch eventuelle Daten zu sichern, da alles überschrieben wurde.  
Ein anderer Weg, den Stick von den Daten zu befreien, wäre der folgende:

    dd if=/dev/zero of=/dev/sda1
    cat: write error: No space left on device

#### Löschen der Daten unter Windows

dd wurde nach Windows portiert und ist hier erhältlich: <http://www.chrysocome.net/dd>  
Um zu schauen, welches Laufwerk der USB-Stick ist, muss dd mit dem Parameter --list aufgerufen werden. Dieser existiert allerdings nur in der Version für Windows

    dd --list

In der Auflistung muss man nun nach dem Laufwerksbuchstabe schauen, an dem der Stick von Windows abgelegt wurde. Bei mir war das G! Als nächstes müssen nun die kompletten Daten gelöscht werden:

    dd if=/dev/zero of=\\.\g: -count=1G -bs=1M --progress

*Anmerkung: Diese Aktion kann je nach größe des USB-Sticks einige Zeit in Anspruch nehmen.*  

### Formatieren des Sticks

In diesem zweiten Abschnitt bekommt der USB-Stick ein neues Dateisystem. Das Dateisystem meiner Wahl ist ext2, kann aber durchaus auch ein anderes, wie FAT32 oder so sein.

#### Formatieren des Sticks unter Linux/Unix

Im nächsten Schritt muss der Stick nun mit einem Dateisystem "formatiert" werden.

    mkfs.ext2 /dev/sda1

Hier wird der Stick, nach drücken der Return-Taste, mit dem Ext2 Dateisystem formatiert.  

#### Formatieren des Sticks unter Windows

*ToDo*

### Installieren von GRUB

Nun muss der Formatierte Stick wieder gemountet werden:

    mount /dev/sda1 /media/usb

Im nächsten Schritt sollten nun die nötigen Ordner für GRUB erstellt werden:

    mkdir -p /media/usb/boot/grub

Nun müssen die Bootdateien von GRUB in den erstellten Ordner /media/usb/boot/grub kopiert werden.

    cp /usr/lib/grub/i386-pc/* /media/usb/boot/grub/

Sollte obige Anweisung nicht funktionieren, weil das Verzeichnis nicht existiert, so ist ein anderer möglicher Pfad in der nun folgenden Anweisung. Man muss eigentlich nur das /usr entfernen.

    cp /lib/grub/i386-pc/* /media/usb/boot/grub/

Nun werden alle Dateien, die von GRUB benötigt werden auf den USB-Stick kopiert. Im letzten Schritt muss nun eine Datei mit dem Namen device.map erstellt werden, damit GRUB weiß, welche Laufwerksangabe für den USB-Stick gilt. Dies geschieht wie folgt:

    echo '(hd0)     /dev/sda1' > /media/usb/boot/grub/device.map

Als letzter Schritt muss nun nur noch GRUB auf dem Stick installiert werden, was wie folgt gemacht wird:

    /sbin/grub-install --root-directory=/media/usb/ /dev/sda1

Nun ist GRUB auf dem USB-Stick installiert und es kann von diesem gebootet werden.  
**Anmerkung:** Jeder USB-Stick kann bootbar gemacht werden. Im Internet herrscht der irrglaube, dass nur einige wenige Sticks bootbar sind, und zwar diese, wo das draufsteht. Das ist jedoch einfach gesagt Schwachsinn, da ein USB-Stick ein Speichermedium ist und solange das BIOS mit dem booten von USB-Sticks klar kommt wird das funktionieren.

  
***Dieser Artikel ist unvollständig, wird noch erweitert und muss nochmals korrekturgelesen werden***

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/3341/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1737/index.html)

<!-- MediaWiki page 1737; revision 3341; parent 0; 2008-09-14T18:57:15Z -->
