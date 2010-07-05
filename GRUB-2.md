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

  
Der **GR**and **U**nified **B**ootloader2 (**GRUB2**) ist ein kompletter Rewrite von GRUB legacy und ist wie sein Vorgänger ein [Multiboot](https://github.com/lowlevel-eu/wiki/wiki/Multiboot "Multiboot")-konformer [Bootloader](https://github.com/lowlevel-eu/wiki/wiki/Bootloader "Bootloader").

  

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

Wenn GRUB2 installiert ist, dann muss folgendes auf der Kommandozeile eingegeben werden: ` grub-mkrescue --output=GRUB2.iso /boot/grub `

Diese muss dann noch mit dem eigenen Kernel und ggf. Modulen sowie der grub.cfg zusammengeführt werden.

### Windows

Unter Windows gibt es noch keine Möglichkeit, ein CD-Image von GRUB2 zu erstellen. Am besten nimmt man ein Fertiges. Dafür ist das Ändern des Images sehr einfach. Man lädt [UltraISO](http://www.chip.de/downloads/UltraISO_14293961.html) herunter, falls man Windows-User ist (das Programm ist Shareware und bis 300MB begrenzt). Wenn UltraISO heruntergeladen und installiert ist, sollte man folgende Dateien in einem Ordner haben: Das GRUB2.iso-Image, die grub.cfg und alle für das eigene OS nötigen Dateien (Kernel, Module, Programe etc.). Das sollte dann so ausehen: [<img src="https://raw.githubusercontent.com/wiki/lowlevel-eu/wiki/assets/fa4203217911f828a9bd.png" width="597" height="130" alt="GRUB2-1.PNG" />](https://raw.githubusercontent.com/wiki/lowlevel-eu/wiki/assets/fa4203217911f828a9bd.png)

Die grub.cfg sollte folgenden inhalt haben: ` set timeout=15 set default=0 `

`menuentry "_OS_" { `

      multiboot /boot/kernel.elf   
      boot                         

`} ` Wenn das der Fall ist, UltraISO starten, den "Weiterhin testen..."-Button betätigen, auf Datei-\>Öffnen klicken und dann das GRUB2-Image auswählen und öffnen. Das Fenster sollte dan wie folgt aussehen: In der Verzeichnisstruktur zu dem Ordner mit der grub.cfg und den eigenen OS-Dateien wechseln. Das Fenster sollte dann den Inhalt des Ordners beinhalten.

[<img src="https://raw.githubusercontent.com/wiki/lowlevel-eu/wiki/assets/5a96869af9be98ac5a13.png" width="839" height="489" alt="GRUB2-2.PNG" />](https://raw.githubusercontent.com/wiki/lowlevel-eu/wiki/assets/5a96869af9be98ac5a13.png)

Kernel ins Image bringen: Obenb Links auf den Ordner "boot" und unten rechts auf die eigene Kernel-Datei klicken. Klicke auf den makierten Button.

[<img src="https://raw.githubusercontent.com/wiki/lowlevel-eu/wiki/assets/76ee07abdaa0ca50ba98.png" width="838" height="490" alt="GRUB2-3.PNG" />](https://raw.githubusercontent.com/wiki/lowlevel-eu/wiki/assets/76ee07abdaa0ca50ba98.png)

grub.cfg ins Image bringen: Oben links auf das Plus neben dem Ordner "boot" klicken und dann auf den Ordner "Grub". Die grub.cfg auswählen und auf den markierten Button klicken.

[<img src="https://raw.githubusercontent.com/wiki/lowlevel-eu/wiki/assets/76ee07abdaa0ca50ba98.png" width="838" height="490" alt="GRUB2-3.PNG" />](https://raw.githubusercontent.com/wiki/lowlevel-eu/wiki/assets/76ee07abdaa0ca50ba98.png)

Auf "Datei-\>Speichern" klicken.

Nun ist das Image bereit, um auf einem echten PC oder einem Emulator gebootet zu werden. Achtung: Bedanken, dass immer, wenn sich etwas am Kernel oder den Modulen ändert, diese erneut dem Image hinzugefügt werden müssen.

## grub.cfg

Die grub.cfg Datei ist die neue Konfigurationsdatei von GRUB2. Sie ist das Äquivalent zur grublst von GRUB legacy. Hier ein Beispiel: ` set timeout=15 set default=0 # Set the default menu entry `

`menuentry "_OS_" { `

      multiboot /boot/kernel.elf   
      boot                         

`} ` Diese Konfigurationsdatei würde die Kerneldatei Kernel.elf aus dem Ordner "boot" laden und danach ausführen.

### wichtige Befehle

| Befehl | Beschreibung |
| ---------------------------------------------- | --------------------------------------------------------------- |
| multiboot /pfad/zum/kernel/dein-kernel.datei | Lädt deinen Kernel in den Speicher. um in danach auszuführen. |
| boot | Startet dein zuvor mit dem Befehl multiboot geladenen Kernel. |

## Siehe auch

- [GRUB](https://github.com/lowlevel-eu/wiki/wiki/Grand-Unified-Bootloader "GRUB")

  

## Weblinks

- [Wikipedia:GRUB](http://de.wikipedia.org/wiki/GRUB)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/7789/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2087/index.html)

<!-- MediaWiki page 2087; revision 7789; parent 7780; 2010-07-05T06:59:43Z -->
