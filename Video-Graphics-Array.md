# Video Graphics Array

Diese Seite ist ein Artikel, welcher **mehr** haben könnte..  

Wenn du mehr darüber weißt oder recherchieren willst, bist **du** aufgerufen, dies zu tun. Wenn du dir in einer Sache nicht sicher bist, dann stell es auf die Diskussionsseite.

**Video Graphics Array** (**VGA**) ist ein Grafikstandard der seit 1987 benutzt wird. Heutige PC-Grafikkarten sind noch immer zum VGA Standard kompatibel.

## Modi

Die Grafikdarstellung von VGA kann grob in Text- und Grafikmodus unterteilen werden.  

### Textmodus

Im Textmodus werden meistens 80\*25 Zeichen verwendet. Diese Aufösung wird z.B. fast immer beim Starten eines PCs benutzt. Eine andere oft benutzte Zeichendarstellung ist 80\*50. Speicheradresse: 0xB8000h.

### Grafikmodus

Im Grafikmodus werden die Werte der einzelnen Pixel direkt verändert. Ein Modus besteht aus vertikaler und horizontaler Pixelanzahl und der Anzahl darstellbarer Farben.

#### Modus 13h

320x200 Punkte bei 256 Farben

Speicheradresse: 0xA0000

Speichergröße: 64000 Bytes

## Einleitung

Irgendwann ist man an einem Punkt angelangt, an dem man nicht nur den voreingestellten Textmodus des BIOSes benutzen möchte. Man möchte in den Grafikmodus wechseln, die Auflösung anpassen und vielleicht auch die Farbtiefe anpassen. Oder auch einfach nur die Schriftart (Den Font) ändern. Der erste Station auf diesem Weg (Anfangs besser die erste Hürde) nennt sich VGA (Video Graphics Array).

Man könnte für jede Grafikkarte einen eigenen Treiber schreiben. Dann hätte man natürlich die volle Kontrolle über alles. Allerdings hat wahrscheinlich keiner die Zeit dazu, noch den Zugriff auf die Dokumentationen, die die Hersteller wie einen Schatz hüten, aus Angst man konnte daraus Rückschlüsse auf das Design des Grafikchips schließen. Und die wenigsten könnten auch alle Treiber testen, da man dazu ja jede Grafikkarte bräuchte. ;)

Die zweite Möglichkeit wären die VESA BIOS Extensions (VBE). Diese unterstützen viel höhere Auflösungen und Farbtiefen wie VGA mit seinen popeligen 640 mal 480 Pixeln bei 4 Bit (16 Farben) als Maximum. Der Nachteil dabei ist, dass man auf die Video-BIOS Routinen angewiesen ist, und damit deb 16 Bit Modus benötigt. Die meisten von Ihnen haben wahrscheinlich so schon den Protected Mode initialisiert (oder von Grub initialisieren lassen), Interrupts zum arbeiten gebracht und vielleicht sogar einen Speichermanager geschrieben. Der Wechsel in den Real Mode würde da vieles durcheinander bringen. Viel einfacher sind die VBE auch nicht zu benutzen, sodass man erst mal mit VGA anfangen kann.

VGA wird von fast allen Grafikkarten unterstützt (Mir ist keine bekannt die VGA nicht unterstützt, aber ich denke Grafikkarten vor der Einführung von VGA dürften da Probleme haben... ;) ), bietet 256KByte Speicher auf der Karte (Kein direkter Zugriff, Nur Memory Mapped IO (MMIO), später mehr dazu) und kann im Textmodus und dem Grafikmodus betrieben werden. Folgende Modi sind vom Standard vorgeschrieben: 720x400 Textmodus (80x25 Zeichen, ein Zeichen 9x16), 640x480 Textmodi (80x30 Zeichen, ein Zeichen 8x16), 320x200 bei 8 Bit Farbtiefe (Paletten basiert), 320x200 bei 16 Bit Farbtiefe, 640x480 mit 4 Bit Farbtiefe.

## Warnung!

Wenn Sie die Timings des CRTC (später mehr dazu) ändern und Ihr Monitor diese Frequenzen nicht unterstützt, besteht die Chance auf einen Defekt an ihm. Testen Sie am besten alle Änderungen vorher auf einem Emulator Ihrer Wahl (Bochs, QEmu, ...) und rechnen Sie besser zweimal nach. Normalerweise haben Heute die meisten Monitore einen Schutzmechanismus intus und zeigen bei Fehlerhaften Timings etwa "Modus wird nicht unterstützt" oder so ähnlich an. Versprechen kann ich Ihnen aber nichts. Die Benutzung des Wissens und der Codebeispiele geschieht auf eigene Gefahr. Weder der Autor noch die Lowlevel Community und auch nicht die Betreiber dieser Webseite Haften für entstandene Schäden.

## Siehe auch

- [Textausgabe](https://github.com/lowlevel-eu/wiki/wiki/Textausgabe "Textausgabe")

## Weblinks

- [Wikipedia: VGA](http://de.wikipedia.org/wiki/Video_Graphics_Array)

## Quellen

- [\[1\]](http://wiki.osdev.org/VGA_Hardware)
- [\[2\]](http://www.osdever.net/FreeVGA/vga/vga.htm)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/4661/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1516/index.html)

<!-- MediaWiki page 1516; revision 4661; parent 4660; 2009-07-17T08:16:32Z -->
