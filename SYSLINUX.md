# SYSLINUX

**SYSLINUX** ist ein [Bootloader](https://github.com/lowlevel-eu/wiki/wiki/Bootloader "Bootloader"), der verschiedene Betriebssysteme von einem FAT-Dateisystem laden kann.

## Installation

### FAT-Image

Unter Linux sollte das SYSLINUX aus dem Repository der Distribution verwendet werden. Für Windows gibt es Binaries in der offiziellen Source Code Distribution in den Verzeichnissen *win32\syslinux.exe* und *win64\syslinux64.exe* (für 32- bzw. 64-Bit-Windows).

Um mittels SYSLINUX ein [Multiboot](https://github.com/lowlevel-eu/wiki/wiki/Multiboot "Multiboot")-konformes Betriebssystem zu booten wird das Modul *mboot.c32* benötigt. Dieses ist in der offiziellen Source Code Distribution mitgeliefert und befindet sich im Verzeichnis *com32/mboot*.

Außerdem muss eine Konfigurationsdatei namens *syslinux.cfg* erstellt werden, die wie folgt aussehen könnte: `DEFAULT myos LABEL myos `

     SAY Booting MyOS
     KERNEL /boot/syslinux/mboot.c32
     APPEND /mykernel --- /myprog1 --- /myprog2

In der Zeile *KERNEL* muss *mboot.c32* angegeben werden, da es aus Sicht von SYSLINUX der Kernel ist. Erst dieses Modul lädt die Datei mykernel aus dem Wurzelverzeichnis sowie die Module myprog1 und myprog2. Die Module werden durch drei Bindestriche (---) voneinander getrennt. Es können nach jedem Modul Kommandozeilenparameter angegeben werden. Weitere Informationen stehen in der Dokumentation zu mboot.c32 (siehe Weblinks).

1.  Das Laufwerk/Image mit dem FAT-Dateisystem formatieren. Dazu sind die Bordmittel des Betriebssystems zu verwenden.
2.  Durch den Aufruf von *syslinux* den Bootloader installieren.
    - **Linux**: `syslinux -d boot/syslinux image_oder_dev`
      TODO: Testen.
    - **Windows**: `syslinux -m -a -d boot/syslinux H:`
      Um diesen Befehl auszuführen sind Administratorrechte erforderlich.
3.  Verzeichnis *boot/syslinux* auf dem Image erstellen.
4.  *syslinux.cfg* und *mboot.c32* in das eben erstelle Verzeichnis kopieren.
5.  Das eigene Betriebssystem auf das Image kopieren (in diesem Beispiel mykernel, myprog1 und myprog2)

Nur der letzte Schritt muss wiederholt werden, wenn das Image aktualisiert werden soll.

## Weblinks

- [SYSLINUX Website](http://www.syslinux.org)
- [Download](http://www.kernel.org/pub/linux/utils/boot/syslinux/)
- [SYSLINUX Dokumentation](http://www.syslinux.org/wiki/index.php/SYSLINUX)
- [mboot.c32 Dokumentation](http://www.syslinux.org/wiki/index.php/Mboot.c32)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/10136/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2470/index.html)

<!-- MediaWiki page 2470; revision 10136; parent 10135; 2011-09-09T17:19:31Z -->
