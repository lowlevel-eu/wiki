# Graphical User Interface

Ein GUI (**G**raphical **U**ser **I**nterface) ist eine grafische Oberfläche, die zumeist mit der Maus bedienbar ist. Ein [Windowsdesktop](https://github.com/lowlevel-eu/wiki/wiki/Windows "Windows") ist ein typisches Beispiel für eine grafische Oberfläche. [Linux](https://github.com/lowlevel-eu/wiki/wiki/Linux "Linux") z.B. bietet zwar grafische Oberflächen an, das Grundsystem ist jedoch eine Kommandozeile, und ein GUI ist nur optional (aber für viele Nutzer unentbehrlich).

## Vorteile eines GUI

- Für die meisten [Windows](https://github.com/lowlevel-eu/wiki/wiki/Windows "Windows")-gewöhnten Nutzer ist ein GUI bequemer zu bedienen als eine Commandline (Kommandozeile). Man klickt einfach auf das Browsericon, anstatt irgendeinen Textbefehl einzutippen, der den Textbrowser aufruft
- Es ist bei mehreren, auf einmal laufenden Programmen übersichtlicher. In der Kommandozeile sind rein vom Aufbau her mehrere Fenster, zwischen denen man per simplem Klick wechselt, nicht möglich. Man kann in der Kommandozeile eigentlich nur ein Programm gleichzeitig laufen haben, das konkret Eingaben vom Benutzer entgegennimmt
- Die Darstellung von Bildern ist möglich

## Vorteile einer Kommandozeile

- Man hat mehr Kontrolle über das System. Im File Explorer von [Windows](https://github.com/lowlevel-eu/wiki/wiki/Windows "Windows") kann man Rechtsklick\>Löschen auswählen. Eine genauere Spezifizierung der Anweisung, zum Beispiel, ob rekursiv alle Unterordner mit gelöscht werden sollen, oder nicht, ist nicht möglich. In der Kommandozeile können an einen Befehl aber problemlos beliebige Parameter angehängt werden, und damit die gewünschte Wirkung genauer angegeben werden
- Eine Kommandozeilendarstellung verbraucht viel weniger Ressourcen. Auf Servern ist ein GUI reine Ressourcenverschwendung, da man an diesen nicht wie an gewöhnlichen Arbeitscomputern arbeitet, sondern sie fast nur zur Programmausführung verwendet, und man sich damit den Luxus eines GUIs zugunsten der Performance sparen sollte
- Ein GUI ist für Programmieranfänger im OS-Entwicklungsbereich viel anspruchsvoller (Grafiktreiber bzw. Nutzung von [VESA](https://github.com/lowlevel-eu/wiki/wiki/Video-Electronics-Standards-Association "VESA")/[VGA](https://github.com/lowlevel-eu/wiki/wiki/Video-Graphics-Array "VGA") oder Ähnlichem, Anzeigen aller Fenster in der richtigen Ordnung, Zugriff auf die Maus, etc.), und es empfiehlt sich für das Erstprojekt ein System, das erst einmal nur eine Kommandozeile bietet

## OSentwicklung

Eine GUI ist es empfelenswert, erst nach den [Kernel](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel") die GUI zu entwickeln. Dieser Fehler wird meißtens von Anfänger gemacht.

## Techniken

Hier wird erklärt, was eine GUI ausmacht

### Fenster

Meistens ist ein Fenster ein Rechteck. Dieser kann verschoben werden. Ein Fenster kann geschlossen, minimiert oder die Größe kann verändert werden. Meistens stellt ein Fenster ein Programm dar. Es können mehrere Fenster von Programm abstammen.

### Drag and Drop

Bei Drag and Drop wird ein Bild verschoben.

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/2862/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1511/index.html)

<!-- MediaWiki page 1511; revision 2862; parent 2860; 2008-03-26T12:50:01Z -->
