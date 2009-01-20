# Crosscompiler für Windows

Dieser Artikel soll eine kleine Anleitung sein, wie man einen [GCC](https://github.com/lowlevel-eu/wiki/wiki/GNU-Compiler-Collection "GCC") unter Windows so aufsetzt, dass man damit [týndur](https://github.com/lowlevel-eu/wiki/wiki/T%C3%BDndur "Týndur") kompilieren kann. Wer sein eigenes OS damit kompilieren will, kann das natürlich auch tun. Den GCC habe ich bereits kompiliert, aber wer mir nicht traut, kann sich mit der [Cross-Compiler-Anleitung](https://github.com/lowlevel-eu/wiki/wiki/Cross-Compiler "Cross-Compiler") selbst einen bauen.

## Benötigte Werkzeuge

Die Anforderungen von týndur sind relativ gering und auf allen unterstützten Plattformen gleich:

- Eine POSIX-Umgebung (wir brauchen unter anderem Bash, sed und make)
- NASM
- GCC und binutils

## MinGW-basierte Umgebung

MinGW ist ein Port des GCC nach Windows. Der mitgelieferte Compiler von MinGW kann keine ELF-Dateien erzeugen und ist deswegen nicht geeignet, um týndur zu kompilieren. Darum muss ein Cross-Compiler benutzt werden.

Einen Cross-Compiler, den ich selbst aus den ungeänderten Sourcen für mein eigenes Frickel-OS namens IncOS kompiliert habe, gibt es unter [\[1\]](http://jidder.de/lost/files/incoscc-with-cpp-and-with-without-i18n.rar). Darin enthalten ist der GCC 4.2.0 mit dem Target ELF und die Binutils 2.17. Außerdem benötigen wir die POSIX-Umgebung für MinGW [MSYS](http://mingw.org/download.shtml) und [NASM](http://sourceforge.net/project/showfiles.php?group_id=6208&package_id=47034).

Wenn ihr die drei Dateien runtergeladen habt, erstellt ein Verzeichnis namens C:\lostdev. (Wer seine Werkzeuge wo anders platzieren möchte, kann das natürlich auch tun. Im folgenden werde ich dennoch von diesem Pfad ausgehen.) Startet den Setup von MSYS und klickt euch bis zur Angabe des Pfads durch. Gebt da C:\lostdev\msys an. Dann weiter bis zum Ende durchklicken. Wenn eine Eingabeaufforderung auftaucht, die etwas von "This is a post install process" erzählt, brecht das durch die Eingabe von "n" ab.

Entpacke danach NASM in das Verzeichnis C:\lostdev\nasm. Achte dabei darauf, dass die Datei nasmw.exe direkt in dem Verzeichnis C:\lostdev\nasm liegt und nicht in irgendwelchen Unterverzeichnissen. Benenne außerdem die Datei nasmw.exe in nasm.exe um, damit NASM von dem build-Skript erkannt wird.

Entpacke dann die Datei incoscc-with-cpp-and-with-without-i18n.rar in dem lostdev-Verzeichnis, sodass z.B. in c:\lostdev\bin die Datei i586-elf-addr2line.exe liegt.

Damit der Compiler und der Assembler auch gefunden werden, muss die PATH-Variable entsprechend geändert werden. Ich bevorzuge für jede Compilerumgebung auf meinem Computer eine Batch-Datei, die die Umgebung einrichtet. Für týndur sieht sie so aus:

    set path=C:\lostdev\msys\bin;C:\lostdev\lostcc\i586-elf\bin;C:\lostdev\nasm;%path%
    cmd /k cls

Diese Datei kopiere ich mir in das Wurzelverzeichnis des Quelltextbaums von týndur und starte sie. Durch die Eingabe von make sollte dann týndur vollständig kompilieren.

Wer lieber den Compiler tiefer in das System verankern will, kann die Pfade in die globale PATH-Variable schreiben. Diese Pfade sind dann allerdings überall verfügbar und können unter Umständen Konflikte mit anderen Compilern und Umgebungen verursachen. Unter Windows geht das in der Systemsteuerung (klassische Ansicht) -\> System -\> Erweitert -\> Umgebungsvariablen und dort eine PATH-Variable editieren.

## Cygwin

(todo)

## Erstellung eines eigenen Cross Compilers

Wer nicht meinen Cross Compiler nutzen möchte, kann sich selbst einen bauen. Weil das zur Zeit den Rahmen dieses Artikels sprengen würde, verweise ich auf die [Anleitung](http://wiki.osdev.org/GCC%20Cross-Compiler) im OS-FAQ Wiki auf Mega-Tokyo. Mein Cross Compiler ist auch in etwa nach dieser Anleitung entstanden.

## Probleme

### gcc.exe: \_spawnvp: No such file or directory und CreateProcess: No such file or directory

Die genaue Ursache kenne ich auch nicht, aber es könnte helfen, die Datei libexec\gcc\i586-elf\4.2.0\cc1.exe nach i586-elf\bin zu kopieren.

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/3942/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1450/index.html)

<!-- MediaWiki page 1450; revision 3942; parent 3842; 2009-01-20T20:04:25Z -->
