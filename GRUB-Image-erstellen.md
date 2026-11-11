# GRUB-Image erstellen

### menu.lst

Mit der Zeit dürfte es lästig werden, bei jedem Testboot die Befehle von Hand in [GRUB](Grand-Unified-Bootloader "GRUB") einzugeben. Ein schönes Bootmenü mit genau einem Eintrag, der nach einer Sekunde automatisch gebootet wird, erhält man, wenn man eine neue Datei namens grub/menu.lst mit folgendem Inhalt auf dem Image anlegt:

    timeout 1

    title LOST
    kernel /lost.krn

### Ein Update-Skript

Ich persönlich benutze ein Shellskript, um den jeweils neuesten [Kernel](Kernel "Kernel") bequem auf das Image zu kopieren. Damit spare ich mir das Eintippen eines langen mount-Befehls, eines ebenso langen cp-Befehls und die Eingabe des Root-Passworts.

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

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/11237/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1449/index.html)

<!-- MediaWiki page 1449; revision 11237; parent 8467; 2014-12-17T07:49:55Z -->
