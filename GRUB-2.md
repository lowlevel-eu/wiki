# GRUB 2

| Allgemeines |  |
| --------------- | ---------------------------- |
| Name: | GRand Unified Bootloader 2 |
| Entwickler: | \- |
| Akt. Version: | 1.98 |
| Lizenz: | GNU GPL Version 3 |
| Plattform: | Unix |
| Homepage |  |

<http://www.gnu.org/software/grub/grub.html>

  
Der **GR**and **U**nified **B**ootloader2 (**GRUB2**) ist ein kompletter rewrite von GRUB legacy und ist wie sein vorgänger ein [Multiboot](https://github.com/lowlevel-eu/wiki/wiki/Multiboot "Multiboot")-konformer [Bootloader](https://github.com/lowlevel-eu/wiki/wiki/Bootloader "Bootloader").

  

### Funktionen

- Liest [ext2](https://github.com/lowlevel-eu/wiki/wiki/Ext2 "Ext2"), [ext3](https://github.com/lowlevel-eu/wiki/wiki/Ext3 "Ext3"), UFS, UFS2, ReiserFS, [FAT](https://github.com/lowlevel-eu/wiki/wiki/File-Allocation-Table "FAT"), NTFS, [ISO9660](https://github.com/lowlevel-eu/wiki/wiki/ISO9660 "ISO9660"), JFS, Minix, FFS, XFS, ext4
- Auswahlmenü um verschiedene Betriebssysteme zu laden.
- Bootet von Disketten, Festplatten, CDs, DVDs und Flashdisks.
- Beinhaltet eine Shell
- Kann mit einem Passwort gesichert werden
- Kann von einem TFTP-Server booten
- Scripting-Support mit Lua
- Grafische Benutzerschittstelle (nicht mit einer klassischen GUI bzw. einem Desktop zu verwechseln!)
- Dynamisches Laden von Module auch während der Laufzeit
- Unterstützung neuer Architekturen
- Internationalisierung
- Modulares und objektorientiertes Framework für Dateisysteme etc.
- Cross-Plattform-Installation

## CD-Image erstellen

### Linux

wenn du GRUB2 installiert hast, dann must du nur folgendes auf der komandozeile eingeben: ` grub-mkrescue --output=GRUB2.iso /boot/grub ` Danach sollte in dem Ordner, von dem du aus diesen Befehl ausgeführt hat eine GRUB2.iso liegen. Diese must du nur noch mit deinem Kernel, modulen und der GRUB.cfg(die neue konfigurationsdatei änlich der grub.lst)

### Windows

Unter Windows gibt es noch keine möglichkeit ein CD-Image von GRUB2 zu erstellen. am besten nimmst du ein fertiges. Dafür ist das ändern sehr leicht. Lade dir [UltraISO](http://www.chip.de/downloads/UltraISO_14293961.html) herunter(ist Shareware und bis 300MB begrenzt aber das dauert wohl ne Zeit bis euer OS so groß ist)Wenn UltraISO heruntergeladen und installiert ist solltest du die in einem Ordner alle nötigen Dateien sammeln. Das GRUB2.iso image, die grub.cfg und deinen kernel bzw. zusätzliche module. Das sollte dann so ausehen: [<img src="https://raw.githubusercontent.com/wiki/lowlevel-eu/wiki/assets/fa4203217911f828a9bd.png" width="597" height="130" alt="GRUB2-1.PNG" />](https://raw.githubusercontent.com/wiki/lowlevel-eu/wiki/assets/fa4203217911f828a9bd.png)

Die grub.cfg sollte folgenden inhalt haben: ` set timeout=15 set default=0 `

`menuentry "_OS_" { `

      multiboot /boot/kernel.elf   
      boot                         

`} ` Wenn das der Fall ist. dann starte UltraISO und klicke auf den button :Weiterhin testen... Klicke oben link auf Datei-\>Öffnen navigiere in deinen Ordner wo die GRUB2.iso liegt und öffne diese dann. Dann sollte dein Fenster so ausehen: Navigire unten links in der Verzeichnissstruktur zu deinem Ordner mit der grub.cfg und deiner Kernel.elf. rechts unten sollte dannn der Inhalt angezeigt werden.

[<img src="https://raw.githubusercontent.com/wiki/lowlevel-eu/wiki/assets/5a96869af9be98ac5a13.png" width="839" height="489" alt="GRUB2-2.PNG" />](https://raw.githubusercontent.com/wiki/lowlevel-eu/wiki/assets/5a96869af9be98ac5a13.png)

Kernel ins Image bringen: klicke oben links auf den ordner boot und klicke unten rechts auf die Kernel.elf. Klicke auf den makierten Button.

[<img src="https://raw.githubusercontent.com/wiki/lowlevel-eu/wiki/assets/76ee07abdaa0ca50ba98.png" width="838" height="490" alt="GRUB2-3.PNG" />](https://raw.githubusercontent.com/wiki/lowlevel-eu/wiki/assets/76ee07abdaa0ca50ba98.png)

grub.cfg ins Image bringen: klicke oben links auf das Plus neben dem Rrdner boot und klicke auf den Ordner Grub. Klicke unten rechts auf die grub.cfg. Klicke auf den makierten Button.

[<img src="https://raw.githubusercontent.com/wiki/lowlevel-eu/wiki/assets/76ee07abdaa0ca50ba98.png" width="838" height="490" alt="GRUB2-3.PNG" />](https://raw.githubusercontent.com/wiki/lowlevel-eu/wiki/assets/76ee07abdaa0ca50ba98.png)

Nun klicke auf Datei-\>speichern

Jetzt kannst du dieses image benutzen um im Emulator oder auf echter Hardware zu booten. Achtung: bitte beachte das du jedesmal deinen kernel neu ins ISO intigrieren must, wenn du etwas daran verändert hast.

## grub.cfg

Die grub.cfg Datei ist die neue konfigurationsdatei von GRUB2 sie ist das äquivalent zur grublst von GRUB legacy. Hir ein Beispiel. ` set timeout=15 set default=0 # Set the default menu entry `

`menuentry "_OS_" { `

      multiboot /boot/kernel.elf   
      boot                         

`} ` Diese konfigurationsdatei würde die Kerneldatei Kernel.elf aus dem order boot laden und danach ausführen.

# == wichtige Befehle

| Befehl | Beschreibung |
| ---------------------------------------------- | --------------------------------------------------------------- |
| multiboot /pfad/zum/kernel/dein-kernel.datei | Lädt deinen Kernel in den Speicher. um in danach auszuführen. |
| boot | Startet dein zuvor mit dem Befehl multiboot geladenen Kernel. |

## Siehe auch

- \[GRUB\]

  

## Weblinks

- [Wikipedia:GRUB](http://de.wikipedia.org/wiki/GRUB)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/7777/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2087/index.html)

<!-- MediaWiki page 2087; revision 7777; parent 7430; 2010-06-29T12:42:48Z -->
