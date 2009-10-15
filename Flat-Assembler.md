# Flat Assembler

Diese Seite ist ein Artikel, welcher **mehr** haben könnte..  

Wenn du mehr darüber weißt oder recherchieren willst, bist **du** aufgerufen, dies zu tun. Wenn du dir in einer Sache nicht sicher bist, dann stell es auf die Diskussionsseite.

Der Flat Assembler ist ein [Assembler](https://github.com/lowlevel-eu/wiki/wiki/Assembler "Assembler"), der die Intelsyntax verwendet. Er wurde für 80x86-Prozessoren entworfen und kann 16-, 32- und 64-Bit-Code erstellen. Weiterhin unterstützt er [FPU](https://github.com/lowlevel-eu/wiki/wiki/Mathematischer-Koprozessor "FPU")-, [MMX](https://github.com/lowlevel-eu/wiki/wiki/MultiMedia-Extension "MMX")-, SSE-, SSE2-, SSE3- und 3DNow!-Befehle.  
Mit ihm kann man sowohl Flat Binaries als auch Dateien in den Formaten [ELF](https://github.com/lowlevel-eu/wiki/wiki/Executable-and-Linking-Format "ELF") und [PE](https://github.com/lowlevel-eu/wiki/wiki/Microsoft-Portable-Executable-and-Common-Object-File-Format "PE") (MZ und COFF) erstellen.

## Versionen

Ein großer Vorteil des Flat Assemblers ist wohl seine Portabilität. Es gibt Versionen für [DOS](https://github.com/lowlevel-eu/wiki/wiki/Microsoft-Disk-Operating-System "DOS"), [Linux](https://github.com/lowlevel-eu/wiki/wiki/Linux "Linux"), [Windows](https://github.com/lowlevel-eu/wiki/wiki/Windows "Windows") und für alle Systeme mit einer minimalen C-Standardbibliothek (benötigte Befehle: fopen, fclose, fread, fwrite, fssek, ftell, malloc, free, getenv (für ein eventuelles \$INCLUDE-Verzeichnis als Standardpfad für "include"), time (wohl für die Anzeige der benötigten Zeit) und exit). Letztere Version besteht aus einer Objektdatei, die gegen die libc gelinkt werden kann. Alternativ kann man sich den Flatassembler auch aus dem Quellcode selbst kompilieren (der Quellcode von FASM ist Quellcode für FASM) und sich seine eigene "system.inc"-Datei erstellen, die die benötigten Funktionen bereitstellt. Daher kann man FASM als eines der Programme bezeichnen, die sich wohl als erstes auf das eigene Betriebssystem portieren lassen.

## Weblinks

- [Homepage des Flatassemblers](http://flatassembler.net/)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/6069/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2091/index.html)

<!-- MediaWiki page 2091; revision 6069; parent 0; 2009-10-15T17:00:20Z -->
