# Video Graphics Array

Diese Seite ist ein Artikel, welcher **mehr** haben könnte..  

Wenn du mehr darüber weißt oder recherchieren willst, bist **du** aufgerufen, dies zu tun. Wenn du dir in einer Sache nicht sicher bist, dann stell es auf die Diskussionsseite.

## Einleitung

Irgendwann ist man an einem Punkt angelangt, an dem man nicht nur den voreingestellten Textmodus des BIOS benutzen möchte. Man möchte in den Grafikmodus wechseln, die Auflösung anpassen und vielleicht auch die Farbtiefe anpassen. Oder auch einfach nur die Schriftart (den Font) ändern. Der erste Station auf diesem Weg (anfangs besser die erste Hürde) nennt sich VGA (Video Graphics Array).

Man könnte für jede Grafikkarte einen eigenen Treiber schreiben. Dann hätte man natürlich die volle Kontrolle über alles. Allerdings hat wahrscheinlich keiner weder die Zeit dazu, noch den Zugriff auf die Dokumentationen, die die Hersteller wie einen Schatz hüten, aus Angst man konnte daraus Rückschlüsse auf das Design des Grafikchips schließen. Und die wenigsten könnten auch alle Treiber testen, da man dazu ja jede Grafikkarte bräuchte. ;)

Die zweite Möglichkeit wären die [VESA BIOS Extensions](https://github.com/lowlevel-eu/wiki/wiki/VESA-BIOS-Extensions "VESA BIOS Extensions") (VBE). Diese unterstützen viel höhere Auflösungen und Farbtiefen als VGA mit seinen popeligen 640 mal 480 Pixeln bei 4 Bit (16 Farben) als Maximum. Der Nachteil dabei ist, dass man auf die Video-BIOS Routinen angewiesen ist, und damit den 16 Bit Real Mode benötigt. Die meisten von Euch haben wahrscheinlich schon den Protected Mode initialisiert (oder von Grub initialisieren lassen), Interrupts zum arbeiten gebracht und vielleicht sogar einen Speichermanager geschrieben. Der Wechsel in den Real Mode würde da vieles durcheinander bringen und viel einfacher sind die VBEs auch nicht zu benutzen, sodass man erst mal mit VGA anfangen kann.

VGA wird von fast allen Grafikkarten unterstützt (Mir ist keine bekannt die VGA nicht unterstützt, aber ich denke Grafikkarten vor der Einführung von VGA dürften da Probleme haben... ;) ), bietet 256 KByte Speicher auf der Karte (kein direkter Zugriff, nur Memory Mapped IO (MMIO), später mehr dazu) und kann im Textmodus und dem Grafikmodus betrieben werden. Folgende Modi sind vom Standard vorgeschrieben: 720x400 Textmodus (80x25 Zeichen, ein Zeichen 9x16), 640x480 Textmodi (80x30 Zeichen, ein Zeichen 8x16), 320x200 bei 8 Bit Farbtiefe (palettenbasiert), 640x480 mit 4 Bit Farbtiefe.

## Warnung!

Wenn Du die Timings des CRTC (später mehr dazu) änderst und Dein Monitor diese Frequenzen nicht unterstützt, besteht die Chance auf einen Defekt an ihm. Teste am besten alle Änderungen vorher auf einem Emulator deiner Wahl (Bochs, QEmu, ...) und rechne besser zweimal nach. Normalerweise haben heute die meisten Monitore einen Schutzmechanismus intus und zeigen bei fehlerhaften Timings "Modus wird nicht unterstützt" oder so ähnlich an. Versprechen kann ich aber nichts. Die Benutzung des Wissens und der Codebeispiele geschieht auf eigene Gefahr. Weder der Autor noch die Lowlevel-Community und auch nicht die Betreiber dieser Webseite haften für entstandene Schäden.

## Voraussetzungen

Generell wird nur je eine Routine zum Lesen und Schreiben von einem Byte auf IO-Ports benötigt. Diese Routinen sollten auch noch eine Verzögerung beinhalten, damit die Hardware auf Änderungen reagieren kann. Bevor man sich aber ernsthaft mit VGA beschäftigt wäre es hilfreich, in den Protected Mode zu wechseln. Sämtliche Speicheradressen, die ich hier aufzähle, sind sofern nichts anderes dabei steht physisch.

## Aufbau

Ein VGA-Adapter besteht aus folgenden Komponenten: Dem Grafikcontroller, Speicher (256 KByte aufgeteilt auf Ebene 0 bis Ebene 3 mit jeweils 64 KByte), dem Sequenzer, dem CRT-Controller (CRT = Cathode Ray Tube, technische Bezeichnung für Röhrenmonitor), dem Attribut-Controller und dem DAC (Palette). Der Grafikcontroller regelt wie genau in den Videospeicher geschrieben und der Sequenzer wie die Daten weiter an den CRT Controller geschickt werden. Der CRT-Controller kümmert sich um das Timing der Daten, die zum Monitor gehen, und der Attribute Controller regelt ein paar wenige Dinge wie zum Beispiel das Aktivieren oder Deaktivieren des Monitors etc. Mit dem DAC kann man die Palette anpassen, wenn man sich im 8 Bit Modus befindet.

### Externe Register

Die externen Register stellen nützliche Informationen bereit und steuern allgemeine Dinge, wie beispielsweise die Polarität (positiv oder negativ) der Synchronisationsimpulse, welche vom CRT-Controller an den Monitor gesendet werden. Das Ausgaberegister wird über Port 0x3C2 beschrieben und über 0x3CC gelesen. Das Statusregister 0 wird über Port 0x3C2 und das Statusregister 1 entweder über Port 0x3BA oder 0x3DA gelesen. (Später mehr dazu)

### Attribut-Controller

Der Attribut-Controller wird über die Ports 0x3C0 und 0x3C1 gesteuert. Ersterer übernimmt dabei den Index und die zu schreibenden Daten und letzterer enthält die zu lesenden Daten. Wie? Über nur zwei Ports hat man Zugriff auf mehrere Register? Und über ein und denselben Port werden Index und Daten geschrieben? Wie geht denn das? Nun, die Register werden durchnummeriert. Möchte man Daten ins Register 1 schreiben oder lesen, dann schreibt man zuerst die 1 das Indexregister 0x3C0 und kann anschließend über denselben Port Daten senden oder über Port 0x3C1 das Register lesen. Dabei merkt sich der Controller, ob als nächstes ein Index oder Daten anstehen. Leider ist zu Beginn nicht definiert, was erwartet wird. Glücklicherweise kann man durch Lesen eines Bytes von Port 0x3DA (das ist das externe Statusregister 1) die Logik zurücksetzen, sodass als nächstes ein Index erwartet wird. Man sollte also vor jedem Zugriff zuerst mal Port 0x3DA lesen, dann den Index schreiben und anschließend die Daten lesen/schreiben.

## Modi

### Modus 13h

- 320x200 Punkte bei 256 Farben
- Speicheradresse: 0xA0000
- Speichergröße: 64000 Bytes

#### Beispielcode

Als erstes muss man einen Pointer auf den Speicher erstellen: \<c\> unsigned char\* VGA = (unsigned char\*) 0xA0000; \</c\> Wenn man einen Pixel zeichnen möchte, muss man einfach in dem Speicher schreiben: \<c\> void setpixel(int x, int y, unsigned char color) {

     offset = 320*y + x;
     if(x <= 320) {
       if(y <= 200) {
         VGA[offset] = color;
       }
     }

} \</c\>

## Siehe auch

- [Textausgabe](https://github.com/lowlevel-eu/wiki/wiki/Textausgabe "Textausgabe")

## Weblinks

- [Wikipedia: VGA](http://de.wikipedia.org/wiki/Video_Graphics_Array)

## Quellen

- [wiki.osdev.org/VGA_Hardware](http://wiki.osdev.org/VGA_Hardware)
- [www.osdever.net/FreeVGA/vga/vga.htm](http://www.osdever.net/FreeVGA/vga/vga.htm)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/9656/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1516/index.html)

<!-- MediaWiki page 1516; revision 9656; parent 8555; 2011-04-09T06:39:07Z -->
