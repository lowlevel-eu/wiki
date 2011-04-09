# Graphical User Interface

Ein **Graphical User Interface** (GUI, dt.: grafische Benutzeroberfläche) zeichnet sich im Gegensatz zum [CLI](https://github.com/lowlevel-eu/wiki/wiki/Shell "Command Line Interface") dadurch aus, dass der Benutzer seine Befehle nicht durch Texteingabe, sondern durch Aktionen mit grafischen Elementen gibt. Besonders im Desktop-Bereich haben sich GUIs durchgesetzt, und daher unterstützt auch fast jedes große Betriebssystem die Bedienung über ein GUI. Es ist also verständlich, wenn sich auch beim Hobby-OS-Entwickler der Wunsch entwickelt, eine GUI anzubieten.

## Merkmale

Prägende Merkmale eines modernen GUI sind die Nutzung der [Maus](https://github.com/lowlevel-eu/wiki/wiki/Maus "Maus") als primäres Eingabegerät und die Nutzung von Fenstern, welche sich auf einer oder mehreren Arbeitsflächen befinden (Stichwort: Virtuelle Desktops). Weitere (beinah) allgegenwärtige Features von GUIs sind Drag'n'Drop und eine Zwischenablage, um zu vermeiden, dass jedes Fenster von den anderen abgeschottet ist.

## Entwickeln einer GUI für das eigene OS

Die meisten OS-Developer wollen eine GUI für ihr OS haben. Doch besonders viele Anfänger wollen quasi sofort eine GUI mit allem Drum und Dran haben. Dabei sollte jedem klar sein, dass eine GUI ein hochkomplexes Programm ist, vergleichbar mit einem aufwändigen 3D-Spiel. Und wo es gerade erwähnt wurde: Eine GUI ist ein **Programm**, soll also vom Kernel **geladen und ausgeführt** werden. Eine GUI ist **kein** Bestandteil des [Kernels](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel")! Auch die GUI von [Windows](https://github.com/lowlevel-eu/wiki/wiki/Windows "Windows") gehört nicht zum Kernel, wie oft angenommen wird (allerdings sind GUI und Kernel über die WinAPI und verschiedenste [Syscalls](https://github.com/lowlevel-eu/wiki/wiki/Syscall "Syscall") eng miteinander verzahnt).

Wer eine GUI für sein OS entwickeln möchte, benötigt mindestens folgendes in seinem Kernel:

- Vollständige [Speicherverwaltung](https://github.com/lowlevel-eu/wiki/wiki/Speicherverwaltung "Speicherverwaltung")
- [Multitasking](https://github.com/lowlevel-eu/wiki/wiki/Multitasking "Multitasking") (am besten für User-Space-Programme)

Dazu braucht man dann wahrscheinlich noch:

- Grafiktreiber
- libc
- Sonstige Libs

Multitasking vor allem, weil die GUI, wenn sie als einziger Prozess ausgeführt werden würde, sich nicht mehr bedienen lassen würde, wenn ein anderes Programm gestartet wird (und auch dieses im Grunde nicht ausgeführt werden kann, weil es sich der Elemente der GUI bedient).

### Portieren oder selbst schreiben?

KDE, Gnome, IceWM... Bei der Fülle an (Linux-)GUIs fragt man sich sicherlich, warum man nicht einfach eine bestehende portieren kann. Kann man, allerdings ist dazu fast immer die Portierung von Libs (Qt bei KDE, GTK bei Gnome) vonnöten, was mitunter ein ebenso großes Projekt ist. Außerdem brauchen GUIs auch Window-Manager.

Selber schreiben klingt da vernünftiger, allerdings muss man hier auf unterster Ebene (lowlevel ;)) arbeiten: Man hat keine Libs im Hintergrund, die eine Fenster mit "createWindow();" erstellen, man muss alles von Hand machen.

## Vorteile

- Auch vollkommen unerfahrene Benutzer können mithilfe eines GUI oftmals Funktionen "erraten", sei es durch das Design der Icons oder auch durch Tooltips. Die Lernkurve durch "Learning-by-doing" verläuft viel steiler als bei Einsteigern in die Konsole.
- Die Bedienung erfolgt durch konkrete, sichtbare Objekte intuitver, der Benutzer muss sich weniger Gedanken machen.

<!-- -->

- *Beispiel: Auf zwei virtuellen Konsolen laufen unterschiedliche Programme. Um zwischen diesen zu wechseln muss der Benutzer wissen, auf welchem tty das Programm läuft und dann per Tastenkombination wechseln. Bei einem GUI kann der Benutzer das zweite Programm in der Fensterleiste, oder direkt unter dem ersten, sehen, und muss es einfach nur anklicken.*

## Nachteile

- Das Hinzufügen neuer Programmfunktionen erhöht unweigerlich die Komplexität des GUI. Daher ist das Design eines komplexen GUI allein schon ein enormer Aufwand.

<!-- -->

- *Beispiel: In einem Dateimanager können alle Funktionen zu einer Datei in einem Kontextmenü untergebracht werden. Jedoch braucht jede Funktion auch einen eigenen Eintrag. Bei ausreichend vielen Einträgen wird das Menü vielleicht zu groß oder zu unübersichtlich. Bei einer Konsole ist es egal, wie viele Befehle verfügbar sind, da jeder Befehl direkt eingegeben werden kann.*

<!-- -->

- GUIs verbrauchen viele Ressourcen. Daher wird insbesondere auf Servern nur ein einfaches GUI eingesetzt oder oft auch ganz auf ein GUI verzichtet.
- Last but not least ist der Aufwand der Entwicklung oder Portierung eines GUI enorm. Desweiteren braucht eine GUI besonders viel Infrastruktur, wie z.B. Grafik- oder Maustreiber. Von der Entwicklung eines GUI ohne einen stabilen und relativ ausgereiften [Kernel](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel") ist also abzuraten.

## Nützliches für die GUI-Programmierung

Wer nicht gleich ein Library portieren will um schiefe Linien zu zeichnen kann diesen Beispielcode verwenden. **Der Beispielcode setzt voraus das es die Funktion setpixel(int x,int y, unsigned char color) gibt.(die Funktion sollte einen Pixel zeichnen)** \<c\>

1.  define sgn(x) ((x\<0)?-1:((x\>0)?1:0))

void line(int x1, int y1, int x2, int y2, unsigned char color) {

     int dx,dy,sdx,sdy,px,py,dxabs,dyabs,i;
     int slope;

     dx = x2-x1;      
     dy = y2-y1;      
     dxabs = abs(dx);
     dyabs = abs(dy);
     sdx = sgn(dx);
     sdy = sgn(dy);
     if(dxabs >= dyabs) {
       slope = dy / dx;
       for(i=0;i!=dx;i+=sdx) {
         px = i + x1;
         py = slope * i + y1;
         setpixel(px, py, color);
       }
     } else {
       slope = dx / dy;
       for(i=0;i!=dy;i+=sdy) {
         px = slope * i + x1;
         py = i + y1;
         setpixel(px, py, color);
       }
     }

} \</c\> Hat man diese Funktion ist vieles getan.  
Eine leichte Übung wäre jetzt eine Funktion um ein Rechteck zu zeichnen: \<c\> void rectangle(int x, int y, int w, int h, unsigned char color) {

     line(x, y, x + h, y, color);
     line(x, y, x, y + w, color);
     line(x, y + w, x + h, y + w, color);
     line(x + h, y, x + h, y + w, color);

} \</c\>

## Links

[Common Usability Terms](http://osnews.com/story/20287/Common_Usability_Terms_part_IX_the_Menu)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/9657/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1511/index.html)

<!-- MediaWiki page 1511; revision 9657; parent 7343; 2011-04-09T07:02:18Z -->
