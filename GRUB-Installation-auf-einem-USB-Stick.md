# GRUB Installation auf einem USB-Stick

# Vorbemerkung

Nun da ich mich seit einiger Zeit damit beschäftige, auf meinem USB-Stick GRUB zu installieren möchte ich hier eine Schrit für Schritt Anleitung geben, wie man GRUB installiert.  

# Der USB-Stick

**ACHTUNG: Sichert vorher alle Daten von dem Stick, denn spätestens nach dem überschreiben des Stick-Inhalts mit Null-Bytes werden diese nicht wiederherstellbar sein!**

## Löschen der Dateien

In diesem Abschnitt werden der Inhalt des USB-Sticks mit Null-Bytes überschrieben, damit überhaupt nichts mehr darauf vorhanden ist.

### Löschen der Daten unter Linux/Unix

Zuerst sollte man nachschauen, wo der USB-Stick hin gemountet wurde, falls das automatisch geschehen ist. Dies kann man mit dem Befehl mount machen:

    mount
    /dev/sda1 on /mnt type vfat (rw)

Zumeist liegt der Stick an der Stelle /dev/sda1 o.ä. zumindest war es bei mir so. Bevor der Inhalt des Sticks allerdings überschrieben werden kann, sollte er ausgehängt werden, damit kein Programm auf diesen zugreifen kann. Dies geschieht wie folgt:

    umount /dev/sda1

Nun wird der komplette Stick mit Null-Bytes überschrieben. Dies wird wie folgt gemacht:

    cat /dev/zero > /dev/sda1
    cat: write error: No space left on device

Wird die untere Fehlermeldung ausgegeben, so heißt das, dass der USB-Stick komplett überschrieben wurde. Ab hier gibt es denke ich mal keine Möglichkeit mehr noch eventuelle Daten zu sichern, da alles überschrieben wurde.  
Ein anderer Weg, den Stick von den Daten zu befreien, wäre der folgende:

    dd if=/dev/zero of=/dev/sda1
    cat: write error: No space left on device

### Löschen der Daten unter Windows

dd wurde nach Windows portiert und ist hier erhältlich: <http://www.chrysocome.net/dd>  
Um zu schauen, welches Laufwerk der USB-Stick ist, muss dd mit dem Parameter --list aufgerufen werden. Dieser existiert allerdings nur in der Version für Windows

    dd --list

In der Auflistung muss man nun nach dem Laufwerksbuchstabe schauen, an dem der Stick von Windows abgelegt wurde. Bei mir war das G! Als nächstes müssen nun die kompletten Daten gelöscht werden:

    dd if=/dev/zero of=\\.\g: -count=1G -bs=1M --progress

*Anmerkung: Diese Aktion kann je nach größe des USB-Sticks einige Zeit in Anspruch nehmen.*  

## Partitionieren des Sticks

Um auf dem Stick den Bootloader GRUB zu installieren, muss vor dem Formatieren des Sticks eine Partition angelegt werden. Dies ist möglich, da es sich bei dem USB-Stick um eine kleine externe Festplatte handelt.

### Partitionieren unter Linux/Unix

Um den USB-Stick zu partitionieren, muss einfach nur cfdisk oder fdisk mit der Stelle angeben, unter der der Stick von der jeweiligen Maschine verwaltet wird, was in dieser Anleitung /dev/sda1 ist. Also lautet der Aufruf wie folgt:

    cfdisk /dev/sda
    .... oder ....
    fdisk /dev/sda

**Anmerkung:** /dev/sda stellt den Stick dar, /dev/sda1 die erste Partition.  
Nun muss mit dem jeweiligen Programm eine Partition erstellt werden. Nach dem Schreiben der Partitions-Tabelle, wird eben jene neu eingelesen. Beim neuen Einlesen der Partitions-Tabelle kann unter umständen der Fehler auftreten, das der Stick nicht wieder eingelesen werden konnte, was allerdings vernachlässigt werden kann.

### Partitionieren unter Windows

*ToDo*

## Formatieren des Sticks

In diesem zweiten Abschnitt bekommt der USB-Stick ein neues Dateisystem. Das Dateisystem meiner Wahl ist ext2, kann aber durchaus auch ein anderes, wie FAT32 oder so sein.

### Formatieren des Sticks unter Linux/Unix

Im nächsten Schritt muss der Stick nun mit einem Dateisystem "formatiert" werden.

    mkfs.ext2 /dev/sda1

Hier wird der Stick, nach drücken der Return-Taste, mit dem Ext2 Dateisystem formatiert.  

### Formatieren des Sticks unter Windows

*ToDo*

## Installieren von GRUB

### Installation unter Linux

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

### Installation unter Linux

*ToDo*

## Testen des USB-Sticks

*ToDo*

### Testen mit Bochs

*ToDo*

#### Testen unter Linux

*ToDo*

#### Testen unter Windows

*ToDo*

### Testen mit qemu

*ToDo*

#### Testen unter Linux

*ToDo*

#### Testen unter Windows

Um unter qemu von dem USB-Stick booten zu lassen, muss der Stick als Festplatte angegeben werden. Dazu wird jedoch allerdings der Name des Geräts benötigt. Dieser ist wie folgt zu finden:

    Start->Ausführen

Hier wird dann "diskmgmt.msc" eingegeben und mittels Klick auf "OK" geöffnet. Hier muss nun der USB-Stick gesucht werden. Dieser sollte als Wechselmedium eingetragen sein. Dieser hat den Titel "Datenträger" und dann noch eine Nummer, in meinem Falle die 5. Diese Nummer wird für qemu gebraucht, damit das richtige Gerät angesprochen werden kann. Der Aufruf von qemu könnte dann so aussehen:

    qemu -L . -m 32 -localtime -boot c -hda \\\\.\\PhysicalDrive5

**Anmerkung:** Der Stick wird mit "PhysicalDrive" und der entsprechenden Nummer dahinter angesprochen. Die vielen \\ sind aus dem Grund, da eben jenes Zeichen für die Verwendung mit qemu escaped werden muss.  
Wird dies so ausgeführt, sollte, falls nichts schief gelaufen ist, GRUB geladen werden.

### Testen auf einer realen Maschine

*ToDo*

  
***Dieser Artikel ist unvollständig, wird noch erweitert und muss nochmals korrekturgelesen werden***

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/3356/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1737/index.html)

<!-- MediaWiki page 1737; revision 3356; parent 3355; 2008-09-16T14:08:02Z -->
