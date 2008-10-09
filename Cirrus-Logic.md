# Cirrus Logic

Qemu emuliert primär eine Cirrus Logic GD5446. Mit dieser Grafikkarte ist es sehr einfach, mit einem eigenen OS in den Genuss hardwarebeschleunigter¹ 2D-Grafik zu kommen.

¹So weit ich es gesehen habe, werden die Grundoperationen hardwarebeschleunigt dargestellt. Alle Angaben ohne Gewähr.

## Resourcen

Die Grafikkarte ist eine PCI-Karte, Vendor-ID 0x1013, Chip-ID 0x00B8. Sie wird größtenteils über MMIO angesteuert, dabei werden zwei Speicherbereiche als MMIO-Interface zur Karte benutzt, die über die PCI-Schnittstelle abgefragt werden können: Der erste fängt im Falle Qemus an der Adresse 0xF0000000 an und ist 2 Megabytes groß und dient als Framebufferschnittstelle, der zweite (kleinere) Bereich (für die Steuerung der Karte) fängt bei 0xF2000000 an und ist 0x1000 Bytes lang.

In diesen zweiten Bereich sind sämtliche VGA-Ports gemappt, wobei man von der Adresse 0x3C0 abziehen muss, um den Offset in den MMIO-Bereich zu erhalten. So befindet sich das Register VGA_MISC_OUT_W (0x3C2) an der Speicheradresse 0xF2000002.

VGA besitzt an einigen Stellen hinter einem Port mehrere Register, zwischen denen über einen zweiten Indexport gewechselt werden kann. An diesen Stellen besitzt die Grafikkarte oft Zusatzports, vor allem die Register 0x3CE und 0x3CF werden in diesem Zusammenhang für die Hardwarebeschleunigung verwendet.

## Initialisierung

Es gibt zwei Möglichkeiten, die Grafikkarte zu initialisieren: Entweder über die VGA-Register, oder über VESA.

Die Programmierung über die VGA-Register ist recht kompliziert, ich habe es nicht geschafft, wer es versuchen will, viel Spaß, als Lektüre empfehle ich den Xorg-Treiber (siehe Anhang).

Über VESA lässt sich die Karte dagegen sehr einfach einrichten, es reicht aus, über den int10 (entweder mit vm86, einem Emulator oder im Realmode bei Betriebssystemstart) eine größere Auflösung zu wählen.

Ist die Karte einmal in dem Videomodus, muss noch die Beschleunigung aktiviert werden. Dies geschieht durch Schreiben in das Graph-Register 33:

\<c\>

1.  define VGA_GRAPH_INDEX 0x3CE
2.  define VGA_GRAPH_DATA 0x3CF

outb(VGA_GRAPH_INDEX, 0x33); outb(VGA_GRAPH_DATA, 0x04); // Oder outw(VGA_GRAPH_INDEX, 0x0433); \</c\>

Ich habe diese Methode jedoch nur in Qemu getestet. Ich bin mir ziemlich sicher, dass das in der echten Welt da draußen nicht so einfach tut, aber wer hat schon eine Cirrus Logic. :)

## Beschleunigung

TODO

## Links

<http://www.koders.com/c/fidC2D0E7B95D33763B17521DF3EA7B68C81D500CAD.aspx> Code aus Qemu <http://cgit.freedesktop.org/xorg/driver/xf86-video-cirrus/> Xorg-Treiber

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/3393/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1743/index.html)

<!-- MediaWiki page 1743; revision 3393; parent 0; 2008-10-09T00:48:34Z -->
