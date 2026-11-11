# Flat Assembler

Diese Seite ist ein Artikel, welcher **mehr** haben könnte..  

Wenn du mehr darüber weißt oder recherchieren willst, bist **du** aufgerufen, dies zu tun. Wenn du dir in einer Sache nicht sicher bist, dann stell es auf die Diskussionsseite.

| Allgemeines |  |
| --------------- | --------------------------------------------------------------------- |
| Name: | Flat Assembler |
| Entwickler: | Tomasz Grysztar |
| Akt. Version: | 1.69.31 |
| Lizenz: | Alle Rechte vorbehalten<br>(Quellcode verfügbar) |
| Plattform: | Linux, Unix (bzw. alle Systeme mit rudimentärer libc), Windows, DOS |
| Homepage |  |

[flatassembler.net](http://flatassembler.net/)

  
Der Flat Assembler ist ein [Assembler](Assembler "Assembler"), der die Intelsyntax verwendet. Er wurde für 80x86-Prozessoren entworfen und kann 16-, 32- und 64-Bit-Code erstellen. Weiterhin unterstützt er [FPU](Mathematischer-Koprozessor "FPU")-, [MMX](MultiMedia-Extension "MMX")-, SSE-, SSE2-, SSE3- und 3DNow!-Befehle.  
Mit ihm kann man sowohl Flat Binaries als auch Dateien in den Formaten [ELF](Executable-and-Linking-Format "ELF") und [PE](Microsoft-Portable-Executable-and-Common-Object-File-Format "PE") (MZ und COFF) erstellen.  
Im Zusammenhang mit der Betriebssystementwicklung ist zu erwähnen, dass der FASM zu Anfang speziell für diesen Zweck designt wurde. Seine Syntax ähnelt sehr stark der des [NASM](Netwide-Assembler "NASM"), einem ebenfalls weit verbreiteten Assembler für Hobbybetriebssysteme.

## Versionen

Ein großer Vorteil des Flat Assemblers ist wohl seine Portabilität. Es gibt Versionen für [DOS](Microsoft-Disk-Operating-System "DOS"), [Linux](Linux "Linux"), [Windows](Windows "Windows") und für alle Systeme mit einer minimalen C-Standardbibliothek (benötigte Befehle: fopen, fclose, fread, fwrite, fssek, ftell, malloc, free, getenv (für ein eventuelles \$INCLUDE-Verzeichnis als Standardpfad für "include"), time (wohl für die Anzeige der benötigten Zeit) und exit). Letztere Version besteht aus einer Objektdatei, die gegen die libc gelinkt werden kann. Alternativ kann man sich den Flatassembler auch aus dem Quellcode selbst kompilieren (der Quellcode von FASM ist Quellcode für FASM) und sich seine eigene "system.inc"-Datei erstellen, die die benötigten Funktionen bereitstellt. Daher kann man FASM als eines der Programme bezeichnen, die sich wohl als erstes auf das eigene Betriebssystem portieren lassen.

## Siehe auch

- [MenuetOS](MenuetOS "MenuetOS") - komplett in FASM geschrieben

## Weblinks

- [Homepage des Flatassemblers](http://flatassembler.net/)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/9883/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2091/index.html)

<!-- MediaWiki page 2091; revision 9883; parent 9644; 2011-06-25T23:15:26Z -->
