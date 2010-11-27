# Grand Unified Bootloader

| Allgemeines |  |
| --------------- | -------------------------------------------------- |
| Name: | **GR**and **U**nified **B**ootloader |
| Entwickler: | \- |
| Akt. Version: | 0.97 (GRUB legacy)<br>1.98 (GRUB2) |
| Lizenz: | GNU GPL V 2 (GRUB legacy)<br>GNU GPL V 3 (GRUB2) |
| Plattform: | Unix |
| Homepage |  |

<http://www.gnu.org/software/grub/grub.html>

Der **GR**and **U**nified **B**ootloader (**GRUB**) ist ein [Multiboot](https://github.com/lowlevel-eu/wiki/wiki/Multiboot "Multiboot")-konformer [Bootloader](https://github.com/lowlevel-eu/wiki/wiki/Bootloader "Bootloader") der ursprünglich aus dem GNU-Hurd-Projekt entstammt, aber inzwischen bei allen gängigen Linux-Distributionen als Bootloader eingesetzt wird. Im Falle der Betriebssystementwicklung ist es empfehlenswert GRUB den Kernel booten zu lassen, da GRUB sehr flexibel ist und einen großen Funktionsumfang bietet (siehe Abschnitt [Warum GRUB?](https://github.com/lowlevel-eu/wiki/wiki/Grand-Unified-Bootloader#warum-grub "Grand Unified Bootloader")).

## Warum GRUB?

Im Forum und hier im Wiki wird von den meisten GRUB empfohlen und selbst verwendet. Außerdem benutzen die Tutorials im Wiki (größtenteils) GRUB. Dies geschieht aus folgenden Gründen:

- Einen Bootloader zu schreiben setzt **tiefergehende Assemblerkenntnisse** voraus. Falls man diese noch nicht hat, dann wird man sehr wahrscheinlich am Bootloader scheitern oder aber einen Teil/den größten Teil aus anderem Quellcode zusammenkopieren.
- Dabei kommen dann **fehleranfällige** Bootloader heraus, von denen der jeweilige Programmierer meist nicht weiß, was sie genau machen (z. B. in welchem Dateiformat der Kernel sein muss, an welche Adresse der Kernel geladen wird oder wie viel vom Kernel überhaupt geladen wird) und im Forum werden dann Threads mit 500 Zeilen zusammengefrickelten Assemblercode und der Frage *„Warum funktioniert denn das nicht so, wie ich das will!?“* erstellt. Der Punkt hier ist nicht, dass wir zu faul wären Fragen zu beantworten, sondern, dass es einfach nichts bringt einen eigenen Bootloader zu schreiben, wenn derjenige nicht einmal im Ansatz verstanden hat, was er denn da überhaupt tut. Das ist dann für uns primär frustrierend.
- Diese Fehleranfälligkeit kann auch dazu führen, dass das ganze eine Weile funktioniert, aber irgendwann tauchen plötzlich seltsame Fehler auf. Dies kann unter anderem den Grund haben, dass nicht der komplette Kernel geladen wird, sondern z. B. nur die ersten paar Kilobyte. Solche Fehler sind meist extrem **schwer zu debuggen**.
- Eventuell tauchen später auch **neue Anforderungen** an den Bootloader auf, z. B. könnte man bei einem [Mikrokernel](https://github.com/lowlevel-eu/wiki/wiki/Kernel#mikrokernel "Mikrokernel") durch den Bootloader Module (meistens Treiber) laden wollen. Dann wird entweder versucht das schnell *hinzufrickeln* oder aber man entscheidet sich dann doch gegen einen Mikrokernel, d. h. es kann **Auswirkungen auf das Design** des Kernels haben.
- Falls man allerdings von Anfang an intensiv seinen Bootloader plant – was einem Anfänger aufgrund mangelnder Erfahrung verwehrt bleibt – und diesen sehr gewissenhaft programmiert, dann ist das ein Projekt für sich, d. h. es wird **Unmengen an Zeit verschlucken** (wir reden hier nicht von Tagen oder Wochen).
- Der **[Bootvorgang](https://github.com/lowlevel-eu/wiki/wiki/Bootprozess-auf-x86 "Bootvorgang") auf x86-Prozessoren** hat so manches Hindernis, welches von Intel und Konsorten gerne aufgrund von Abwärtskompatibilität aufgestellt wurde. Beispiele hierfür sind der [Real Mode](https://github.com/lowlevel-eu/wiki/wiki/Real-Mode "Real Mode") (der Bootloader startet im Realmode) und das [A20-Gate](https://github.com/lowlevel-eu/wiki/wiki/A20-Gate "A20-Gate"), welches aktiviert werden muss.

Wir möchten natürlich dem geneigten Leser nicht vorenthalten, was genau er denn verpasst, wenn er GRUB benutzt:

- Eine eingehende Beschäftigung mit dem [Real Mode](https://github.com/lowlevel-eu/wiki/wiki/Real-Mode "Real Mode") bleibt wahrscheinlich aus (oder kommt erst, wenn man sich mit dem [Virtual 8086 Mode](https://github.com/lowlevel-eu/wiki/wiki/Virtual-8086-Mode "Virtual 8086 Mode") beschäftigt).
- Assemblerkenntnisse zu erlangen auch für den Kernel bzw. darüber hinaus fürs Debuggen wichtig, da z. B. im Kernel an einigen kleinen Stellen [Inlineassembler](https://github.com/lowlevel-eu/wiki/wiki/Inline-Assembler-mit-GCC "Inline-Assembler mit GCC") verwendet werden muss.

## GRUB legacy

GRUB legacy ist die ursprüngliche Version von GRUB und wird unter der [GNU General Public License](https://github.com/lowlevel-eu/wiki/wiki/Lizenzen "Lizenzen") vertrieben. Wie man einen Multiboot-Kernel erstellt, der mit GRUB gebootet werden kann, wird im Artikel [OS-Dev für Einsteiger - Teil 4](https://github.com/lowlevel-eu/wiki/wiki/Teil-4-Hello-World "Teil 4 - Hello World") beschrieben.

### Funktionen

- Liest [ext2](https://github.com/lowlevel-eu/wiki/wiki/Ext2 "Ext2"), [ext3](https://github.com/lowlevel-eu/wiki/wiki/Ext3 "Ext3"), UFS, UFS2, ReiserFS, [FAT](https://github.com/lowlevel-eu/wiki/wiki/File-Allocation-Table "FAT"), NTFS, [ISO9660](https://github.com/lowlevel-eu/wiki/wiki/ISO9660 "ISO9660"), JFS, Minix, FFS, XFS
- Auswahlmenü um verschiedene Betriebssysteme zu laden.
- Bootet von Disketten, Festplatten, CDs, DVDs und Flashdisks.
- Beinhaltet eine Shell
- Kann mit einem Passwort gesichert werden
- Kann von einem TFTP-Server booten

### Diskettenimage erstellen

#### Linux

**Achtung!**

Funktioniert nur wenn GRUB legacy auf dem Hostsystem installiert ist.

Wir brauchen also zunächst einmal ein mit [FAT](https://github.com/lowlevel-eu/wiki/wiki/File-Allocation-Table "FAT")-formatiertes Diskettenimage:

    # dd of=test.img bs=1024 seek=1440 count=0
    # mkdosfs test.img

Anstelle von *mkdosfs test.img* kann auch *mke2fs -F test.img* verwendet werden, was ein [Ext2](https://github.com/lowlevel-eu/wiki/wiki/Ext2 "Ext2")-formatiertes Diskettenimage erstellt. Danach muss dieses Image gemountet und alle nötigen Dateien auf das Image kopiert werden werden:

    # sudo mount -oloop test.img /mnt
    # sudo mkdir /mnt/grub
    # sudo cp /boot/grub/stage* /mnt/grub
    # sudo cp kernel /mnt
    # sudo umount /mnt

Anschließend das Image noch bootbar machen:

    # grub

    grub> device (fd0) test.img
    grub> root (fd0)
    grub> setup (fd0)
    grub> quit

#### Windows 32-Bit

**Achtung!**

Funktioniert nur mit GRUB4DOS, nicht aber mit GRUB/GRUB2!

Es sind folgende Tools vonnöten:

- [BFI](http://www.nu2.nu/bfi/) (*Build Floppy Image*)
- [GRUB4DOS](https://gna.org/projects/grub4dos)

Wir brauchen also zunächst einmal einen Ordner. In desen Ordner kommen die Dateien *grldr* (GRUB4DOS Stage2), *menu.lst* (Die GRUB Konfigurationsdatei) und der kernel. Aus diesem Ordner machen wir jetzt ein Image.

    bfi -t=144 -f=floppy.img floppy

Erstellt die Datei floppy.img mit dem Inhalt des Ordners *floppy*.

Nun muss GRUB nur noch auf dem Image installiert werden und das Image bootfähig gemacht werden. Das geschieht mit folgendem Befehl:

    bootlace.com --fat12 --floppy floppy.img

Installiert GRUB-stage1 in den Bootsektor des Floppy Images

Den ganzen Prozess kann man in einer .bat Datei zusammenfassen.

### Windows 64-Bit

Da Windows 64-Bit Systeme die direkte Ausführung von .com Dateien, die 16-Bit sind, verweigern, muss man hier einen kleinen Umweg nehmen:

    bfi.exe -t=144 -f=floppy.img floppy -b=mbr.bin

Erstellt die Datei floppy.img mit dem Inhalt der Ordnes *floppy* und dem MBR aus *mbr.bin*.

Der Ordner *floppy* hat exakt den gleichen Inhalt wie bei oben. Die *mbr.bin* kann erstellt werden indem man den [MBR](https://github.com/lowlevel-eu/wiki/wiki/Master-Boot-Record "MBR") bspw. von einem existierenden Image mittels [dd for Windows](http://www.chrysocome.net/dd) extrahiert. Wer kein zur der GRUB Version kompatibles Image hat, kann sich mittels der Bootlace.com einmalig eines auf einem anderen PC oder in der [DosBox](http://www.dosbox.com/) erstellen.

### CD-Image herstellen

#### Linux

Es sind folgende Tools vonnöten:

- stage2_eltorito von GRUB (Sollte bei deinem Linux dabei sein.)
- mkisofs

Als Erstes sollte man die Dateien, die nachher auf der CD landen sollen, in einen Ordner kopieren. Dazu gehören auch die von GRUB benötigten Dateien und zwar *menu.lst* und *stage2_eltorito*. Diese gehören in den Ordner (relativ von der CD aus) */boot/grub/*. Man kann sie auch in einen beliebigen anderen Ordner packen, dann muss man allerdings mit den Hexeditor an *stage2_eltorito*. Anschließend erstellt man das CD-Image folgendermaßen:

    mkisofs -R -b boot/grub/stage2_eltorito -no-emul-boot -boot-load-size 4 -boot-info-table -o cdrom.iso cdrom_files/

Dies erzeugt ein CD-Image namens *cdrom.iso* aus den Dateien des Ordners *cdrom_files*. *boot/grub/stage2_eltorito* ist dabei ein relativer Pfad von der CD aus auf den Bootloader.

  
*Mögliche Probleme*:

- Die menu.lst kann nicht geladen werden, d.h. es erscheint nur der GRUB-Prompt. Schuld an diesem Fehler ist ein falscher Pfad in stage2 (der Pfad ist Lowercase, aber ISO-Level-1 speichert nur Uppercase). Abhilfe schafft entweder GRUB gepatcht neu bauen, oder einfach den Pfad im Binary zu ändern:`sed -i "s/boot\/grub\/menu.lst/BOOT\/GRUB\/MENU.LST/g" stage2_eltorito`
- Es gibt Systeme die nicht von ElTorito-CDs booten können. Abhilfe schafft hier manchmal, statt ElTorito die Floppyemulation zum Booten zu verwenden. Einfach ein Floppyimage mit allen benötigten Treibern erstellen, welches dann von CD weiterlädt. Das CD-Image hierfür wird dann via`mkisofs -b floppy.img -o cdrom.iso cdrom_files/`  
  erstellt. **ACHTUNG**: Man braucht wenn man nicht alles im Speicher hat wirklich eigene Treiber, das Floppy-Image ist ab Protected Mode verloren (es werden Interrupts umgeleitet).

### Konfigurationsdatei

#### Wichtige Befehle

| Befehl | Beschreibung |
| ----------------------------------- | --------------------------------------------------------------------------------------- |
| title \<NAME\> | Der name wird im Auswahlmenu beim Booten angezeigt. |
| kernel \</pfad/zum/kernel/datei\> | Läd den angegebenen Kernel |
| mudule \</pfad/zum/modul/datei\> | Läd das angegebene Modul in den Speicher und trägt es in die Multiboot modulliste ein |
| boot | Sagt Grub das er jetzt in den Kernel springen soll. |

#### Beispielkonnfigurationsdatei

` title OS_Name kernel /kernel module /modul.mod boot ` Diese Beispielkonfigurationsdatei lädt die Datei `kernel` aus dem Wurzelverzeichnis als Kernel in den Speicher, lädt die Datei `modul.mod` als Modul in den Speicher und führt den Kernel danach aus.

## GRUB 2

GRUB 2 ist der Nachfolger von GRUB legacy und wurde von Grund auf neu geschrieben. Er ist genauso wie GRUB legacy [multibootfähig](https://github.com/lowlevel-eu/wiki/wiki/Multiboot "Multiboot"). Außerdem wird mit GRUB 2 der Multiboot-2-Standard, der sich momentan noch in Entwicklung befindet, unterstützt.

### Neuerungen gegenüber GRUB Legacy

GRUB 2 weist eine Vielzahl an Neuerungen auf:

- Scripting-Support mit Lua
- Grafische Benutzerschnittstelle (nicht mit einer klassischen GUI bzw. einem Desktop zu verwechseln!)
- Dynamisches Laden von Module auch während der Laufzeit
- Unterstützung neuer Architekturen
- Internationalisierung
- Modulares und objektorientiertes Framework für Dateisysteme etc.
- Cross-Plattform-Installation

### Disketten-Image erstellen

#### Linux

Du benötigst ein Disketten Image mit GRUB Legacy drauf, wie man das erstellt, wird oben beschrieben.

    mkdir mnt
    sudo mount -oloop floppy.img mnt
    cd mnt

Jetzt müssen alle Dateien und Ordner außer /boot/grub und seinem Inhalt gelöscht werden. Danach verändert man den Inhalt der Datei menu.lst folgendermaßen:

    timeout=0

    title GRUB 2
    kernel /boot/grub2/core.img
    boot

Als nächstes legt man unter boot ein Verzeichnis grub2 an und führt dann folgende Befehle aus, um die core.img für GRUB 2 zu erhalten:

    cd /usr/lib/grub/i386-pc
    grub-mkimage -p /boot/grub2 -o /tmp/grubimage/mnt/boot/grub2 *.mod

Erklärung:

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

Anschließend kopiert man den Kernel und die dazugehörigen Dateien auf das Image und unmountet es: \<bash\>sudo umount mnt\</bash\> Das Image ist danach fertig.

#### Windows

// Todo kann man sich die GRUB2 Binary irgendwo runterladen?

### CD-Image erstellen

#### Linux

Wenn GRUB2 installiert ist, dann muss folgendes auf der Kommandozeile eingegeben werden:

    grub-mkrescue --output=GRUB2.iso /boot/grub

Diese muss dann noch mit dem eigenen Kernel und ggf. Modulen sowie der grub.cfg zusammengeführt werden.

#### Windows

Unter Windows gibt es noch keine Möglichkeit, ein CD-Image von GRUB2 zu erstellen. Am besten nimmt man ein Fertiges. Dafür ist das Ändern des Images sehr einfach. Man lädt [UltraISO](http://www.chip.de/downloads/UltraISO_14293961.html) herunter, falls man Windows-User ist (das Programm ist Shareware und bis 300MB begrenzt). Wenn UltraISO heruntergeladen und installiert ist, sollte man folgende Dateien in einem Ordner haben: Das GRUB2.iso-Image, die grub.cfg und alle für das eigene OS nötigen Dateien (Kernel, Module, Programe etc.). Das sollte dann so ausehen: [<img src="https://raw.githubusercontent.com/wiki/lowlevel-eu/wiki/assets/fa4203217911f828a9bd.png" width="597" height="130" alt="GRUB2-1.PNG" />](https://raw.githubusercontent.com/wiki/lowlevel-eu/wiki/assets/fa4203217911f828a9bd.png)

Die grub.cfg sollte folgenden inhalt haben:

    set timeout=15
    set default=0
     
    menuentry "_OS_"
    {
       multiboot /boot/kernel.elf   
       boot                         
    }

Wenn das der Fall ist, UltraISO starten, den "Weiterhin testen..."-Button betätigen, auf Datei-\>Öffnen klicken und dann das GRUB2-Image auswählen und öffnen. Das Fenster sollte dan wie folgt aussehen: In der Verzeichnisstruktur zu dem Ordner mit der grub.cfg und den eigenen OS-Dateien wechseln. Das Fenster sollte dann den Inhalt des Ordners beinhalten.

[<img src="https://raw.githubusercontent.com/wiki/lowlevel-eu/wiki/assets/5a96869af9be98ac5a13.png" width="839" height="489" alt="GRUB2-2.PNG" />](https://raw.githubusercontent.com/wiki/lowlevel-eu/wiki/assets/5a96869af9be98ac5a13.png)

Kernel ins Image bringen: Obenb Links auf den Ordner "boot" und unten rechts auf die eigene Kernel-Datei klicken. Klicke auf den makierten Button.

[<img src="https://raw.githubusercontent.com/wiki/lowlevel-eu/wiki/assets/76ee07abdaa0ca50ba98.png" width="838" height="490" alt="GRUB2-3.PNG" />](https://raw.githubusercontent.com/wiki/lowlevel-eu/wiki/assets/76ee07abdaa0ca50ba98.png)

grub.cfg ins Image bringen: Oben links auf das Plus neben dem Ordner "boot" klicken und dann auf den Ordner "Grub". Die grub.cfg auswählen und auf den markierten Button klicken.

[<img src="https://raw.githubusercontent.com/wiki/lowlevel-eu/wiki/assets/76ee07abdaa0ca50ba98.png" width="838" height="490" alt="GRUB2-3.PNG" />](https://raw.githubusercontent.com/wiki/lowlevel-eu/wiki/assets/76ee07abdaa0ca50ba98.png)

Auf "Datei-\>Speichern" klicken.

Nun ist das Image bereit, um auf einem echten PC oder einem Emulator gebootet zu werden. Achtung: Beachten, dass immer, wenn sich etwas am Kernel oder den Modulen ändert, diese erneut dem Image hinzugefügt werden müssen.

### Beispielkonfigurationsdatei

    menuentry "OS_Name"
    {
      multiboot /kernel
      module /modul.mod
      boot
    }

Diese Beispielkonfigurationsdatei lädt die Datei `kernel` aus dem Wurzelverzeichnis als Kernel in den Speicher, lädt die Datei `modul.mod` als Modul in den Speicher und führt den Kernel danach aus.

## Siehe auch

- GRUB legacy
  - [OS-Dev für Einsteiger - Teil 4](https://github.com/lowlevel-eu/wiki/wiki/Teil-4-Hello-World "Teil 4 - Hello World"): kleiner Beispielkernel mit Multiboot
  - [GRUB Installation auf einem USB-Stick](https://github.com/lowlevel-eu/wiki/wiki/GRUB-Installation-auf-einem-USB-Stick "GRUB Installation auf einem USB-Stick")
- GRUB 2
  - [Disketten-/ISO-Images mit GRUB 2 erstellen](http://wiki.osdev.org/GRUB_2)

## Weblinks

- [Wikipedia:GRUB](http://de.wikipedia.org/wiki/GRUB)
- [GRUB für DOS](https://gna.org/projects/grub4dos)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/8990/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1567/index.html)

<!-- MediaWiki page 1567; revision 8990; parent 8989; 2010-11-27T15:44:17Z -->
