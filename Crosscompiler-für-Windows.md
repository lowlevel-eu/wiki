# Crosscompiler für Windows

Im Folgenden werde ich (Jidder) erklären wie man LOST unter Windows kompiliert.

## Benötigte Werkzeuge

Die Anforderungen von LOST sind relativ gering und auf allen unterstützten Plattformen gleich:

- Eine POSIX-Umgebung (wir brauchen unter anderem Bash, sed und make)
- NASM
- GCC

## MinGW-basierte Umgebung

MinGW ist ein Port des GCC nach Windows. Der mitgelieferte Compiler von MinGW kann keine ELF-Dateien erzeugen und ist deswegen nicht geeignet, um LOST zu kompilieren. Darum muss ein Cross-Compiler benutzt werden.

Einen Cross-Compiler, den ich selbst aus den ungeänderten Sourcen für mein eigenes Frickel-OS namens IncOS kompiliert habe, gibt es unter [\[1\]](http://jidder.de/lost/files/incoscc-with-cpp-and-with-without-i18n.rar). Darin enthalten ist der GCC 4.2.0 mit dem Target ELF und die Binutils 2.17. Außerdem benötigen wir die POSIX-Umgebung für MinGW [MSYS](http://mingw.org/download.shtml) (aktuelle Version: MSYS-1.0.10.exe) und [NASM](http://sourceforge.net/project/showfiles.php?group_id=6208&package_id=47034) (aktuelle Version: nasm-0.98.39-win32.zip).

Wenn iht die drei Dateien runtergeladen habt, erstellt ein Verzeichnis namens C:\lostdev. (Wer seine Werkzeuge woanders platzieren möchte, kann das natürlich auch tun. Im folgenden werde ich dennoch von diesem Pfad ausgehen.) Startet den Setup von MSYS und klickt euch bis zur Angabe des Pfads durch. Gebt da C:\lostdev\msys an. Dann weiter bis zum Ende durchklicken. Wenn eine Eingabeaufforderung auftaucht, die etwas von "This is a post install process" erzählt, brecht das durch die Eingabe von "n" ab.

Entpacke danach NASM in das Verzeichnis C:\lostdev\nasm. Achte dabei darauf, dass die Datei nasmw.exe direkt in dem Verzeichnis C:\lostdev\nasm liegt und nicht in irgendwelchen Unterverzeichnissen. Benenne außerdem die Datei nasmw.exe in nasm.exe um, damit NASM von dem build-Skript erkannt wird.

Entpacke dann die Datei incoscc-with-cpp-and-with-without-i18n.rar in dem lostdev Verzeichnis, so dass z.B. in c:\lostdev\bin die Datei i586-elf-addr2line.exe liegt.

Damit der Compiler und der Assembler auch gefunden werden, muss die PATH-Variable entsprechend geändert werden. Ich bevorzuge für jede Compilerumgebung auf meinem Computer eine Batch-Datei, die die Umgebung einrichtet. Für LOST sieht sie so aus:

    set path=C:\lostdev\msys\bin;C:\lostdev\lostcc\i586-elf\bin;C:\lostdev\nasm;%path%
    cmd /k cls

Diese Datei kopiere ich mir dann in immer das Wurzelverzeichnis des Quelltextbaums von LOST und starte sie. Durch die Eingabe von make sollte dann LOST vollständig kompilieren.

Wer lieber den Compiler tiefer in das System verankern will, kann die Pfade in die globale PATH-Variable schreiben. Diese Pfade sind dann überall verfügbar und können unter Umständen Konflikte mit anderen Compilern und Umgebungen verursachen. Unter Windows geht das in der Systemsteuerung (klassische Ansicht) -\> System -\> Erweitert -\> Umgebungsvariablen und dort eine PATH-Variable editieren.

## Cygwin

(todo)

## Erstellung eines eigenen Cross Compilers

Wer nicht meinen Cross Compiler nutzen möchte, kann sich selbst einen bauen. Weil das zur Zeit den Rahmen dieses Artikels sprengen würde, verweise ich auf die [Anleitung](http://www.osdev.org/osfaq2/index.php/GCC%20Cross-Compiler) im OS-FAQ Wiki auf Mega-Tokyo. Mein Cross Compiler ist auch in etwa nach dieser Anleitung entstanden.

## Probleme

### gcc.exe: \_spawnvp: No such file or directory

Die genaue Ursache kenne ich auch nicht, aber es könnte helfen, die Datei libexec\gcc\i586-elf\4.1.1\cc1.exe nach i586-elf\bin zu kopieren.

### Keine Unterstützung für C++

Als ich den Crosscompiler erstellt habe, enthielt LOST noch keinen C++-Code, deswegen gibt es mit den neueren Versionen Abbrüche beim Kompilieren. Die einfachste Lösung ist das Verzeichnis src/modules/cpp zu löschen und gegebenenfalls make clean auszuführen. Alternativ kann man sich einen Crosscompiler mit C++-Unterstützung bauen.

## Ältere Crosscompiler

Aus sentimentalen Gründen hab ich mal einen älteren GCC 4.1.1 mit Binutils 2.17 online gelassen. Den gibt es unter [\[2\]](http://jidder.de/lost/files/lostcc.rar). (Workaround: Einfach betroffene Verzeichnisse löschen.) Dieser Crosscompiler hat keinen C++ Support, weil zu dessen Zeiten kein C++ unter LOST verwendet wurde. Originalanleitung dazu findet man unter [\[3\]](http://lowlevel.brainsware.org/wiki/index.php?title=Crosscompiler_f%C3%BCr_Windows&oldid=1957), der einzige unterschied ist allerdings das Entpacken des RAR-Archivs. ;)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/2011/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1450/index.html)

<!-- MediaWiki page 1450; revision 2011; parent 1957; 2007-06-04T23:49:24Z -->
