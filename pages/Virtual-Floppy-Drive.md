# Virtual Floppy Drive

Das Programm **Virtual Floppy Drive** (**VFD**) ermöglicht es unter [Windows](Windows.md "Windows") ein Disketten-Image als virtuelles Laufwerk einzubinden. Das ist zum Beispiel notwendig, wenn man Dateien auf das Disketten-Image kopieren will. Es kann damit als Ersatz für das Unix-Werkzeug *mount* dienen.

VFD stellt sowohl eine graphische Oberfläche (vfdwin.exe) als auch Konsolenprogrammm (vfd.exe) zur Verfügung, die beide alle Funktionen des Programms steuern können. Beide Programme sollten als Administrator gestartet werden.

## Benutzung der GUI

Die Tabs "Drive0" und "Driver" beinhalten die wichtigsten Funktionen für die Verwendung von VFD.

### Treiber installieren

Bevor ein Diskettenimage eingebunden werden kann, muss zunächst der Treiber installiert und gestartet werden. Das geschieht im Tab "Driver". Im Eingabefeld "Driver File" muss der Pfad zur Datei vfd.sys eingetragen sein, der mit im heruntergeladenen .zip-Archiv ist. Danach kann mit den Button "Install" der Treiber installiert und danach mit dem Button "Start" gestartet werden.

### Image als virtuelles Laufwerk einbinden

Im Tab "Drive0" kann das erste virtuelle Laufwerk eingebunden werden. Zuerst muss über den Button "Change" ein Laufwerksbuchstabe ausgewählt werden. Sofern verfügbar bietet sich dafür "B:" an. Danach kann mit dem Button "Open/Create" das Diskettenimage ausgewählt werden. Als "Disk Type" sollte dabei "File" ausgewählt sein, falls Schreibzugriffe auf das virtuelle Laufwerk das Image auch verändern sollen. Das virtuelle Laufwerk sollte jetzt im Explorer bereits angezeigt werden, und benutzbar sein.

## Benutzung des Konsolenprogramms

Das Konsolenprogramm bietet sowohl die Möglichkeit über Parameter als auch über eine eigene Eingabeaufforderung die Funktionen von VFD zu verwenden. Man kann zum Beispiel über die Parameter den Vorgang des Mountens und Unmountens automatisieren, wenn man dafür nicht immer die [GUI](Graphical-User-Interface.md "GUI") bemühen möchte. Dafür bietet es sich an eine Batch-Dateien zu erstellen.

### Beispiel: Mount

Diese Batch-Datei installiert den Treiber, startet den Treiber und bindet das Image als Laufwerk B: ein. Die Variablen VFD und IMAGE sind gegebenenfalls anzupassen. Diese Datei ist dafür gedacht im Verzeichnis, in dem das Disketten-Image liegt, ausgeführt zu werden. Ist der Pfad in IMAGE absolut (also fängt mit C:\\ oder so an), dann muss das %~dp0%IMAGE% durch %IMAGE% ersetzt werden. Der Befehl %VFD% LINK 0 B wählt den Laufwerksbuchstaben aus. Lässt man das B weg, wird der erste verfügbare Buchstabe gewählt.

`@SET VFD=E:\vfd21-080206\vfd.exe @SET IMAGE=disk.img `

`%VFD% INSTALL %VFD% START %VFD% LINK 0 B %VFD% OPEN 0: %~dp0%IMAGE% `

`@PAUSE`

### Beispiel: Unmount

Diese Batch-Datei bindet das virtuelle Laufwerk wieder aus, stoppt den Treiber und deinstalliert ihn wieder. `@SET VFD=E:\vfd21-080206\vfd.exe `

`%VFD% ULINK 0 %VFD% CLOSE 0: %VFD% STOP %VFD% REMOVE `

`@PAUSE`

## Probleme

### Zugriff verweigert

Wenn eines der Programme die Fehlermeldung "Zugriff verweigert" liefert, sollte man überprüfen, ob das Programm wirklich als Administrator läuft. Unter [Vista/7](Windows.md "Windows") geht das, indem man die [.exe](Microsoft-Portable-Executable-and-Common-Object-File-Format.md "PE")- oder .bat-Datei mit Rechtsklick -\> "Als Administrator ausführen" startet.

## Alternativen

- [VDK](http://chitchat.at.infoseek.co.jp/vmware/vdk.html) ist ähnlich, funktioniert aber mit Festplatten-Images. ([64-Bit Version hier](http://oss.netfarm.it/win32/))
- [WinImage](http://www.winimage.com/) ist eine Shareware (30-Tage Testversion), die keine Möglichkeit bietet, ein Disketten-Image als virtuelles Laufwerk einzubinden, aber mit der man Images direkt bearbeiten kann.
- Das [VMware Disk Mount Utility](http://www.vmware.com/download/eula/diskmount_ws_v55.html) kann Images im VMware-Format (.vmdk) einbinden.
- Der [ImDisk Virtual Disk Driver](http://www.ltr-data.se/opencode.html#ImDisk) kann Disketten-, Festplatten-, sowie ISO-Images einbinden.

## Weblinks

- [VFD Homepage](http://chitchat.at.infoseek.co.jp/vmware/vfd.html)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/10841/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2063/index.html)

<!-- MediaWiki page 2063; revision 10841; parent 6991; 2012-09-16T14:25:37Z -->
