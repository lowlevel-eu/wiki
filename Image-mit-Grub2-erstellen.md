# Image mit Grub2 erstellen

## Vorbemerkungen

Man benötigt zum Folgen der Anleitung nur einen Rechner, auf dem [GRUB 2](Grand-Unified-Bootloader#grub-2 "GRUB 2") installiert ist.

## Erste Schritte

Im Folgenden gehe ich davon aus, dass ihr Linux verwendet, das Arbeitsverzeichnis ist /tmp/grubimage/.

  

## Durchführung

Zuerst lädt man sich ein Image mit [GRUB Legacy](Grand-Unified-Bootloader "GRUB") herunter, z. B. hier: <https://github.com/lowlevel-eu/tyndur/releases>. Ich habe tyndur-0.2.1-gothmog-floppy.img.bz2 genommen. Dieses Image entpackt man nun ins Arbeitsverzeichnis und mountet es anschließend: \<bash\>mkdir mnt sudo mount -oloop 0.2.1-gothmog-floppy.img mnt cd mnt\</bash\> Jetzt müssen alle Dateien und Ordner außer /boot/grub und seinem Inhalt gelöscht werden. Danach verändert man den Inhalt der Datei menu.lst folgendermaßen:

    timeout=0

    title GRUB 2
    kernel /boot/grub2/core.img
    boot

Als nächstes legt man unter boot ein Verzeichnis grub2 an und führt dann folgende Befehle aus, um die core.img für GRUB 2 zu erhalten: \<bash\>cd /usr/lib/grub/i386-pc grub-mkimage -p /boot/grub2 -o /tmp/grubimage/mnt/boot/grub2 \*.mod\</bash\> Erklärung:

| Option | Erklärung |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| -p /boot/grub2 | Der Pfad auf dem Image, in welchem GRUB später nach der grub.cfg sucht, wenn dieser nicht angegeben wird /boot/grub |
| -o ... | Die Ausgabedatei, standardmäßig stdout |
| \*.mod | Die Module, die eingefügt werden, folgende müssen mindestens vorhanden sein: fat sh multiboot ls ext2 configfile extcmd biosdisk (Zumindest hat mit diesen bei mir alles funktioniert) |

Nun erstellt man noch eine grub.cfg mit folgendem Inhalt unter /boot/grub2 auf dem Image ein:

    set timeout=10
    set default=0

    menuentry "OS-Name"
    {
        multiboot /pfad/zu/kernel/kernel/datei
        boot    
    }

Anschließend kopiert man den [Kernel](Kernel "Kernel") und die dazugehörigen Dateien auf das Image und unmountet es: \<bash\>sudo umount mnt\</bash\> Das Image ist danach fertig.

## Test

Testen kann man das Image z. B. mit [QEMU](QEMU "QEMU"): \<bash\>qemu -fda 0.2.1-gothmog-floppy.img\</bash\>

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/11236/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2235/index.html)

<!-- MediaWiki page 2235; revision 11236; parent 7718; 2014-12-17T07:46:53Z -->
