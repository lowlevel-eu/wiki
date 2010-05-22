# Image mit Grub2 erstellen

## Vorbemerkungen

Mann benötigt zum Folgen der Anleitung nur einen Rechner auf dem Grub2 installiert ist.

## Erste Schritte

Ich gehe jetzt einfach mal von einem Linux aus. Arbeitsverzeichnis ist /tmp/grubimage/.

  

## Durchführung

Als erstes lädt man sich ein Image mit Grub 1 hier runter: <http://download.tyndur.org/releases/0.2/> ich habe tyndur-0.2.1-gothmog-floppy.img.bz2 genommen. Dann ins Arbeitsverzeichnis entpacken. Nun mounten: \<bash\> mkdir mnt sudo mount -oloop 0.2.1-gothmog-floppy.img mnt cd mnt \</bash\> und alle Dateien und Verzeichnisse außer dem /boot/grub Verzeichniss mit den Dateien stage1, stage2 und menu.lst. Nun wird die Datei menu.lst editiert, dass ihr Inhalt folgender ist:

    timeout=0

    title Grub2
    kernel /boot/grub2/core.img
    boot

als nächstes legt man unter boot ein Verzeichnis grub2 an. Nun führt man folgende Befehle aus um die core.img für Grub2 zu erhalten: \<bash\> cd /usr/lib/grub/i386-pc grub-mkimage -p /boot/grub2 -o /tmp/grubimage/mnt/boot/grub2 \*.mod\</bash\> Erklärung:

| Option | Erklärung |
| ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| -p /boot/grub2 | Der Pfad auf dem Image, wo Grub später nach der grub.cfg sucht, wenn nicht angegeben /boot/grub |
| -o ... | Die Ausgabe Datei, standardmäßig auf stdout |
| \*.mod | Die Module die eingefügt werden, es müssen minsestens vorhanden sein: fat sh multiboot ls ext2 configfile extcmd biosdisk (Zumindest hat mit diesen bei mir alles funktioniert) |

Nun fügt man noch eine grub.cfg mit folgendem Inhalt nach /boot/grub2 auf dem Image ein:

    set timeout=10
    set default=0

    menuentry "OS-Name"
    {
        multiboot /pfad/zu/kernel/kernel/datei
        boot    
    }

Man kopiert den Kernel und die dazugehörigen Dateien auf das Image. Dann unmountet man das Image: \<bash\>sudo umountmnt\</bash\> Das Image ist fertig.

## Test

Man testet das Image mit qemu einfach so: \<bash\>qemu -fda 0.2.1-gothmog-floppy.img\</bash\>

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/7711/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2235/index.html)

<!-- MediaWiki page 2235; revision 7711; parent 0; 2010-05-22T13:15:17Z -->
