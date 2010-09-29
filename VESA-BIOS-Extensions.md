# VESA BIOS Extensions

Diese Seite ist ein Artikel, welcher **mehr** haben könnte..  

Wenn du mehr darüber weißt oder recherchieren willst, bist **du** aufgerufen, dies zu tun. Wenn du dir in einer Sache nicht sicher bist, dann stell es auf die Diskussionsseite.

Die VESA BIOS Extensions (kurz: VBE) sind ein Standard der [VESA](https://github.com/lowlevel-eu/wiki/wiki/Video-Electronics-Standards-Association "VESA"). Er vereinheitlicht den Zugriff auf eine Grafikkarte, bietet dabei allerdings deutlich mehr Möglichkeiten als [VGA](https://github.com/lowlevel-eu/wiki/wiki/Video-Graphics-Array "VGA"). Der Standard wird von nahezu allen Grafikkarten in Version 2.0 oder der letzten Version, 3.0, unterstützt.

## VBE Funktionen

### Allgemein

Alle Funktionen der VBE sind im Grunde nur im [Real Mode](https://github.com/lowlevel-eu/wiki/wiki/Real-Mode "Real Mode") verfügbar. Die Funktionsnummer wird in AX übergeben, weitere Informationen in den anderen 16 Bit Registern. Jede VBE Funktion liefert einen Wert in AX zurück, der Fehlerinformationen darstellt:

- 004Fh: Aufruf erfolgreich
- 014Fh: Fehler bei der Ausführung
- 024Fh: Funktion nicht unterstützt
- 034Fh: Funktion im aktuellen Grafikmodus nicht unterstützt

Der Funktionaufruf erfolgt über den Interrupt 0x10.

### Linear Frame Buffer

Grundsätzlich stellt VBE zwei Speichermodelle zur Verfügung, um auf den Grafikkartenspeicher zuzugreifen:

- **paged**: Der Speicher wird in mehrere sogenannte "Windows" unterteilt, von denen immer nur eines in den Adressraum der CPU einblendet wird. Um den gesamten Grafikkartenspeicher zu adressieren, muss man zwischen den einzelnen Windows wechseln. Dieser Vorgang wird "Bank Switching" genannt.
- **flat**: Der gesamte Grafikkartenspeicher wird als sogenannter "Linear Frame Buffer" in den Adressraum der CPU eingeblendet.

Der LFB ist wohl eine der wichtigsten Neuerungen mit VBE 2.0. Mithilfe dieser Funktionalität kann man direkt auf den Grafikspeicher der Grafikkarte zugreifen und so viel schneller und einfacher Pixel zeichnen. Außerdem entfällt das lästige "Bank Switching". Daher sollte man (und wird auch) einen Grafikmodus wählen, der den LFB unterstützt.

### Auf VBE-Unterstützung testen: 4F00h

Diese Funktion überprüft, ob die Grafikkarte VBE unterstützt und wenn ja, welche Version.

- AX = 4F00h
- ES:DI = Zeiger auf freien Speicher für den VBE Info Block.

//TODO: VBE Info Block beschreiben

### Unterstützte Grafikmodi suchen

In VBE 1.0 waren die Nummern der verschiedenen Grafikmodi noch vordefiniert:

//TODO: Standart Grafikmodi

Mit VBE 2.0 hat man sich allerdings dafür entschieden, dass die Grafikkartenherrsteller einfach nur eine Funktion bereitstellen, die alle von der Grafikkarte unterstützten Modi auflistet. Den Zeiger auf diese Liste erhält man mit dem VBE Info Block (4F00h). Diese Liste ist eigentlich nur ein WORD-Array, also eine Hintereinaderreihung von 16Bit Nummern. Diese repräsentieren die von der Grafikkarte unterstützten Grafikmodi. Die Liste wird terminiert durch den Eintrag 0xFFFF.

### Einen bestimmten Grafikmodus suchen: 4F01h

Man durchläuft also die obige Liste und prüft dann mit folgender Funktion, welche Eigenschaften der entsprechende Grafikmodus bestitzt:

- AX = 4F01h
- CX = Nummer des Grafikmodus
- ES:DI = Zeiger auf freien Speicher für den ModeInfoBlock

//TODO: ModeInfoBlock beschreiben

So kann man die Nummer desjenigen Grafikmodus herausfinden, den man benötigt.

### In einen Grafikmodus umschalten: 4F02h

Nachdem man nun die gewünschte Grafikmodusnummer hat, muss man nur noch in diesen umschalten:

- AX = 4F02h
- BX = Nummer des VBE Grafikmodus:
  - Bit 15: Löscht den Grafikspeicher, wenn gelöscht
  - Bit 14: Speichermodell: 0=Windowed (paged); 1=Linear (flat)
  - Bits 13-9: reserviert, Null setzen

## VBE im Protected Mode

Vorweg: Es ist nicht möglich, mit VBE einen Grafiktreiber komplett im [Protected Mode](https://github.com/lowlevel-eu/wiki/wiki/Protected-Mode "Protected Mode") zu entwickeln. Wenigstens das Umschalten in den gewünschten Grafikmodus muss im Real Mode erfolgen!

//TODO: Funktion 4f0Ah beschreiben //TODO:VESA V3?? Protected Mode Interface??

## Weblinks

- [\[1\]](http://www.petesqbsite.com/sections/tutorials/tuts/vbe3.pdf) - VBE Spezifikation Version 3.0

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/8424/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2303/index.html)

<!-- MediaWiki page 2303; revision 8424; parent 8423; 2010-09-29T20:45:33Z -->
