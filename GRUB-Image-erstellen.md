# GRUB-Image erstellen

## Vorbemerkungen

Da die Frage immer wieder aufkommt, möchte ich hier kurz eine Methode vorstellen, ein Floppy-Image mit GRUB und LOST zu erstellen. Außer einer Linux-Installation mit GRUB dürfte nichts besonderes nötig sein, auch kein echtes Diskettenlaufwerk. (Windows-Benutzer werden unter GRUB-Image erstellen (Windows) fündig)

In meinen Beispielen werde ich alles in /tmp machen, erstens weil ich es da zum Ausprobieren wirklich gemacht habe, und zweitens, weil es so schön kurz ist. Außerdem gehe ich davon aus, daß alle Schritte als root ausgeführt werden. Nötig ist es eigentlich nur, um das Image mounten zu können. Wer weiß, was er tut, kann davon abweichen, alle anderen nehmen einfach root für den gesamten Prozess.

## Die Minimal-Floppy

Wir brauchen also zunächst einmal ein Image:

    # dd if=/dev/zero of=/tmp/testimg bs=1024 count=1440
    # mkdosfs /tmp/testimg

Danach muß dieses Image gemountet und alle nötigen Dateien draufkopiert werden:

    # mount -oloop /tmp/testimg /mnt
    # mkdir /mnt/grub
    # cp /boot/grub/stage* /mnt/grub
    # cp lost.krn /mnt
    # umount /mnt

Anschließend das Image noch bootbar machen:

    # grub

    grub> device (fd0) /tmp/testimg
    grub> root (fd0)
    grub> setup (fd0)
    grub> quit

Das war's im Prinzip. Jetzt den Lieblingsemulator auf das Image loslassen und LOST booten:

    grub> kernel /lost.krn
    grub> boot

## Sinnvolle Ergänzungen

### menu.lst

Mit der Zeit dürfte es lästig werden, bei jedem Testboot die Befehle von Hand einzugeben. Ein schönes Bootmenü mit genau einem Eintrag, der nach einer Sekunde automatisch gebootet wird, erhält man, wenn man eine neue Datei namens grub/menu.lst mit folgendem Inhalt auf dem Image anlegt:

    timeout 1

    title LOST
    kernel /lost.krn

### Ein Update-Skript

Ich persönlich benutze ein Shellskript, um den jeweils neuesten Kernel bequem auf das Image zu kopieren. Damit spare ich mir das Eintippen eines langen mount-Befehls, eines ebenso langen cp-Befehls und die Eingabe des Root-Passworts.

Zunächst muß das Image in die /etc/fstab eingetragen sein. Dazu ist eine Zeile wie die folgende einzutragen:

    /tmp/testimg   /mnt       auto    user,noauto,loop        0       0

Spätestens hier sollte man natürlich sinnvollerweise nicht mehr in /tmp arbeiten... Ich bleibe mal dabei, denn hier hat sowieso jeder andere Pfade. Weiterhin /mnt zu benutzen, ist ebenso natürlich auch eine schlechte Idee, stattdessen einfach ein leeres Verzeichnis erstellen und dieses dafür eintragen.

Anschließend ein Skript update_lost.sh (oder so ähnlich) mit sinngemäß folgendem, aber an die eigenen Verzeichnisse angepaßtem Inhalt anlegen:

    #!/bin/bash

    mount /mnt
    cp /home/lost/trunk/build/*.krn /home/lost/trunk/build/*.mod /mnt
    umount /mnt

Ausführbar machen und ausprobieren:

    chmod 755 update_lost.sh
    ./update_lost.sh

## Siehe auch

- GRUB auf CD

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/4927/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1449/index.html)

<!-- MediaWiki page 1449; revision 4927; parent 4271; 2009-07-31T13:33:59Z -->
