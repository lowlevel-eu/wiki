# Virtual Floppy Drive

Das Programm **Virtual Floppy Drive** (**VFD**) ermöglicht es unter Windows ein Disketten-Image als virtuelles Laufwerk einzubinden. Das ist zum Beispiel notwendig, wenn man Dateien auf das Disketten-Image kopieren will. Es kann damit als Ersatz für das Unix-Werkzeug *mount* dienen.

VFD stellt sowohl eine graphische Oberfläche (vfdwin.exe) als auch Konsolenprogrammm (vfd.exe) zur Verfügung, die beide alle Funktionen des Programms steuern können. Beide Programme sollten als Administrator gestartet werden.

## Benutzung der GUI

Die Tabs "Drive0" und "Driver" beinhalten die wichtigsten Funktionen für die Verwendung von VFD.

### Treiber installieren

Bevor ein Diskettenimage eingebunden werden kann, muss zunächst der Treiber installiert und gestartet werden. Das geschieht im Tab "Driver". Im Eingabefeld "Driver File" muss der Pfad zur Datei vfd.sys eingetragen sein, der mit im heruntergeladenen .zip-Archiv ist. Danach kann mit den Button "Install" der Treiber installiert und danach mit dem Button "Start" gestartet werden.

### Image als virtuelles Laufwerk einbinden

Im Tab "Drive0" kann das erste virtuelle Laufwerk eingebunden werden. Zuerst muss über den Button "Change" ein Laufwerksbuchstabe ausgewählt werden. Sofern verfügbar bietet sich dafür "B:" an. Danach kann mit dem Button "Open/Create" das Diskettenimage ausgewählt werden. Als "Disk Type" sollte dabei "File" ausgewählt sein, falls Schreibzugriffe auf das virtuelle Laufwerk das Image auch verändern sollen. Das virtuelle Laufwerk sollte jetzt im Explorer bereits angezeigt werden, und benutzbar sein.

## Benutzung des Konsolenprogramms

Das Konsolenprogramm bietet sowohl die Möglichkeit über Parameter als auch über eine eigene Eingabeaufforderung die Funktionen von VFD zu verwenden. Man kann zum Beispiel über die Parameter den Vorgang des Mountens und Unmountens automatisieren, wenn man dafür nicht immer die GUI bemühen möchte. Dafür bietet es sich an eine Batch-Dateien zu erstellen.

### Beispiel: Mount

Diese Batch-Datei installiert den Treiber, startet den Treiber und bindet das Image auf den ersten verfügbaren Laufwerksbuchstaben ein. Die Variablen VFD und IMAGE sind gegebenenfalls anzupassen. Diese Datei ist dafür gedacht im Verzeichnis, in dem das Disketten-Image liegt, ausgeführt zu werden. Ist der Pfad in IMAGE absolut (also fängt mit C:\\ oder so an), dann muss das %~dp0%IMAGE% durch %IMAGE% ersetzt werden.

`@SET VFD=E:\vfd21-080206\vfd.exe @SET IMAGE=disk.img `

`%VFD% INSTALL %VFD% START %VFD% OPEN 0: %~dp0%IMAGE% `

`@PAUSE`

### Beispiel: Unmount

Diese Batch-Datei bindet das virtuelle Laufwerk wieder aus, stoppt den Treiber und deinstalliert ihn wieder. `@SET VFD=E:\vfd21-080206\vfd.exe `

`%VFD% CLOSE 0: %VFD% STOP %VFD% REMOVE `

`@PAUSE`

## Probleme

### Zugriff verweigert

Wenn eines der Programme die Fehlermeldung "Zugriff verweigert" liefert, sollte man überprüfen, ob das Programm wirklich als Administrator läuft. Unter Vista geht das indem man die .exe- oder .bat-Datei mit Rechtsklick -\> "Als Administrator ausführen" startet.

## Weblinks

- [VFD Homepage](http://chitchat.at.infoseek.co.jp/vmware/vfd.html)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/5801/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2063/index.html)

<!-- MediaWiki page 2063; revision 5801; parent 5800; 2009-08-31T12:07:15Z -->
