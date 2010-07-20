# Grand Unified Bootloader

| Allgemeines |  |
| --------------- | -------------------------- |
| Name: | GRand Unified Bootloader |
| Entwickler: | \- |
| Akt. Version: | 1.98 |
| Lizenz: | GNU GPL Version 3 |
| Plattform: | Unix |
| Homepage |  |

<http://www.gnu.org/software/grub/grub.html>

Der **GRand Unified Bootloader** (**GRUB**) ist ein [Multiboot](https://github.com/lowlevel-eu/wiki/wiki/Multiboot "Multiboot")-konformer [Bootloader](https://github.com/lowlevel-eu/wiki/wiki/Bootloader "Bootloader") der ursprünglich aus dem GNU-Hurd-Projekt entstammt, aber inzwischen bei allen gängigen Linux-Distributionen als Bootloader eingesetzt wird. Im Falle der Betriebssystementwicklung ist es empfehlenswert GRUB den Kernel booten zu lassen, da GRUB sehr flexibel ist und einen großen Funktionsumfang bietet (siehe Abschnitt [Warum GRUB?](https://github.com/lowlevel-eu/wiki/wiki/Grand-Unified-Bootloader#warum-grub "Grand Unified Bootloader")).

## Warum GRUB?

Im Forum und hier im Wiki wird von den meisten GRUB empfohlen und selbst verwendet. Außerdem benutzen die Tutorials im Wiki (größtenteils) GRUB. Dies geschieht aus folgenden Gründen:

- Einen Bootloader zu schreiben setzt **tiefergehende Assemblerkenntnisse** voraus. Falls man diese noch nicht hat, dann wird man sehr wahrscheinlich am Bootloader scheitern oder aber einen Teil/den größten Teil aus anderem Quellcode zusammenkopieren.
- Dabei kommen dann **fehleranfällige** Bootloader heraus, von denen der jeweilige Programmierer meist nicht weiß, was sie genau machen (z. B. in welchem Dateiformat der Kernel sein muss, an welche Adresse der Kernel geladen wird oder wie viel vom Kernel überhaupt geladen wird) und im Forum werden dann Threads mit 500 Zeilen zusammengefrickelten Assemblercode und der Frage *„Warum funktioniert denn das nicht so, wie ich das will!?“* erstellt. Der Punkt hier ist nicht, dass wir zu faul wären Fragen zu beantworten, sondern, dass es einfach nichts bringt einen eigenen Bootloader zu schreiben, wenn derjenige nicht einmal im Ansatz verstanden hat, was er denn da überhaupt tut. Das ist dann für uns primär frustrierend.
- Diese Fehleranfälligkeit kann auch dazu führen, dass das ganze eine Weile funktioniert, aber irgendwann tauchen plötzlich seltsame Fehler auf. Dies kann unter anderem den Grund haben, dass nicht der komplette Kernel geladen wird, sondern z. B. nur die ersten paar Kilobyte. Solche Fehler sind meist extrem **schwer zu debuggen**.
- Eventuell tauchen später auch **neue Anforderungen** an den Bootloader auf, z. B. könnte man bei einem [Mikrokernel](https://github.com/lowlevel-eu/wiki/wiki/Kernel#mikrokernel "Mikrokernel") durch den Bootloader Module (meistens Treiber) laden wollen. Dann wird entweder versucht das schnell *hinzufrickeln* oder aber man entscheidet sich dann doch gegen einen Mikrokernel, d. h. es kann **Auswirkungen auf das Design** des Kernels haben.
- Falls man allerdings von Anfang an intensiv seinen Bootloader plant – was einem Anfänger aufgrund mangelnder Erfahrung verwehrt bleibt – und diesen sehr gewissenhaft programmiert, dann ist das ein Projekt für sich, d. h. es wird **Unmengen an Zeit verschlucken** (wir reden hier nicht von Tagen oder Wochen).
- Der **[Bootvorgang](https://github.com/lowlevel-eu/wiki/wiki/Bootprozess-auf-x86 "Bootvorgang") auf x86-Prozessoren** hat so manches Hindernis, welches von Intel und Konsorten gerne aufgrund von Abwärtskompatibilität aufgestellt wurde. Beispiele hierfür sind der [Real Mode](https://github.com/lowlevel-eu/wiki/wiki/Real-Mode "Real Mode") (der Bootloader startet im Realmode) und das [A20-Gate](https://github.com/lowlevel-eu/wiki/wiki/A20-Gate "A20-Gate"), welches aktiviert werden muss.

Wir möchten natürlich dem geneigten Leser nicht vorenthalten, was genau er denn verpasst, wenn er GRUB benutzt:

- Eine eingehende Beschäftigung mit dem [Real Mode](https://github.com/lowlevel-eu/wiki/wiki/Real-Mode "Real Mode") bleibt wahrscheinlich aus (oder kommt erst, wenn man sich mit dem [Virtual 8086 Mode](https://github.com/lowlevel-eu/wiki/wiki/Virtual-8086-Mode "Virtual 8086 Mode") beschäftigt).
- Assemblerkenntnisse zu erlangen auch für den Kernel bzw. darüber hinaus fürs Debuggen wichtig, da z. B. im Kernel an einigen kleinen Stellen [Inlineassembler](https://github.com/lowlevel-eu/wiki/wiki/Inline-Assembler-mit-GCC "Inline-Assembler mit GCC") verwendet werden muss.

## GRUB legacy

GRUB legacy ist die ursprüngliche Version von GRUB und wird unter der [GNU General Public License](https://github.com/lowlevel-eu/wiki/wiki/Lizenzen "Lizenzen") vertrieben. Wie man einen Multiboot-Kernel erstellt, der mit GRUB gebootet werden kann, wird im Artikel [OS-Dev für Einsteiger - Teil 4](https://github.com/lowlevel-eu/wiki/wiki/Teil-4-Hello-World "Teil 4 - Hello World") beschrieben.

### Funktionen

- Liest [ext2](https://github.com/lowlevel-eu/wiki/wiki/Ext2 "Ext2"), [ext3](https://github.com/lowlevel-eu/wiki/wiki/Ext3 "Ext3"), UFS, UFS2, ReiserFS, [FAT](https://github.com/lowlevel-eu/wiki/wiki/File-Allocation-Table "FAT"), NTFS, [ISO9660](https://github.com/lowlevel-eu/wiki/wiki/ISO9660 "ISO9660"), JFS, Minix, FFS, XFS
- Auswahlmenü um verschiedene Betriebssysteme zu laden.
- Bootet von Disketten, Festplatten, CDs, DVDs und Flashdisks.
- Beinhaltet eine Shell
- Kann mit einem Passwort gesichert werden
- Kann von einem TFTP-Server booten

### Beispielkonfigurationsdatei

` title OS_Name kernel /kernel modul /modul.mod boot ` Diese Beispielkonfigurationsdatei lädt die Datei `kernel` aus dem Wurzelverzeichnis als Kernel in den Speicher und lädt die Datei `modul.mod` als Modul in den Speicher und führt den Kernel danach aus.

## GRUB 2

GRUB 2 ist der Nachfolger von GRUB legacy und wurde von Grund auf neu geschrieben. Er ist genauso wie GRUB legacy [multibootfähig](https://github.com/lowlevel-eu/wiki/wiki/Multiboot "Multiboot"). Außerdem wird mit GRUB 2 der Multiboot-2-Standard, der sich momentan noch in Entwicklung befindet, unterstützt.

### Neuerungen gegenüber GRUB Legacy

GRUB 2 weist eine Vielzahl an Neuerungen auf:

- Scripting-Support mit Lua
- Grafische Benutzerschnittstelle (nicht mit einer klassischen GUI bzw. einem Desktop zu verwechseln!)
- Dynamisches Laden von Module auch während der Laufzeit
- Unterstützung neuer Architekturen
- Internationalisierung
- Modulares und objektorientiertes Framework für Dateisysteme etc.
- Cross-Plattform-Installation

## Siehe auch

- GRUB legacy
  - [OS-Dev für Einsteiger - Teil 4](https://github.com/lowlevel-eu/wiki/wiki/Teil-4-Hello-World "Teil 4 - Hello World"): kleiner Beispielkernel mit Multiboot
  - [GRUB-Image erstellen](https://github.com/lowlevel-eu/wiki/wiki/GRUB-Image-erstellen "GRUB-Image erstellen")
  - GRUB-Image erstellen (Windows)
  - GRUB auf CD
  - [GRUB Installation auf einem USB-Stick](https://github.com/lowlevel-eu/wiki/wiki/GRUB-Installation-auf-einem-USB-Stick "GRUB Installation auf einem USB-Stick")
- GRUB 2
  - [Disketten-/ISO-Images mit GRUB 2 erstellen](http://wiki.osdev.org/GRUB_2)

## Weblinks

- [Wikipedia:GRUB](http://de.wikipedia.org/wiki/GRUB)
- [GRUB für DOS](https://gna.org/projects/grub4dos)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/7939/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1567/index.html)

<!-- MediaWiki page 1567; revision 7939; parent 7938; 2010-07-20T00:28:16Z -->
