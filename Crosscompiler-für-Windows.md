# Crosscompiler für Windows

Für Windows wird ein [Cross-Compiler](https://github.com/lowlevel-eu/wiki/wiki/Cross-Compiler "Cross-Compiler") benötigt, um [ELF](https://github.com/lowlevel-eu/wiki/wiki/Executable-and-Linking-Format "ELF")-Dateien zu erstellen, denn die MinGW- und cygwin-Compiler unterstützen dieses Format nicht. Das ELF-Format bietet gegenüber dem PE-Format von Windows den Vorteil, dass es weniger Sonderbehandlung und Workarounds bei der Entwicklung eines Betriebssystems benötigt. Die Verwendung eines Cross-Compilers bietet darüber hinaus mehr Kontrolle über den Ablauf des Kompiliervorgangs.

Dieser Artikel soll eine kleine Anleitung sein, wie man einen vorkompilierten [GCC](https://github.com/lowlevel-eu/wiki/wiki/GNU-Compiler-Collection "GCC") unter Windows so installiert, dass man damit [týndur](https://github.com/lowlevel-eu/wiki/wiki/T%C3%BDndur "Týndur") kompilieren kann. Allerdings ist der verwendete Compiler nicht auf ein bestimmtes System beschränkt, sondern erzeugt Dateien für das allgemeine Target *i586-elf*. Es sollte also kein Problem sein, diesen Compiler für ein anderes OS einzusetzen.

## Download

Der Compiler ist verfügbar unter <http://jidder.de/lost/files/crosstools-complete.rar>. Darin enthalten sind

- GCC 4.4.0 (C- und C++-Compiler)
- binutils 2.19.1
- newlib 1.17.0 und libstdc++ (C- bzw. C++-Standardbibliothek)

Ein neuerer Compiler Build ist [hier](http://pnoob.bplaced.net/downloads/i586-elf.rar) zu finden, funktioniert nur in einer cygwin umgebung. Darin enthalten sind

- GCC 4.5.1 (C -C++-Compiler)
- Binutils 2.20

## Installation

Im Prinzip reicht es, das Archiv zu entpacken (z.B. nach C:\crosstools), und in die PATH-Variable das Verzeichnis C:\crosstools\bin einzutragen. Alle Programme haben dann das Präfix "i586-elf-". Zum Beispiel kann der C-Compiler mit *i586-elf-gcc* aufgerufen werden.

týndur erwartet, dass dieses Präfix in der *config.sh* eingetragen wird, damit die Makefiles den Compiler finden. Dazu muss die Variable *COMPILER_PREFIX_I386* in Zeile 3 mittels *COMPILER_PREFIX_I386=i586-elf-* entsprechend gesetzt werden.

Alternativ kann man statt C:\crosstools\bin auch C:\crosstools\i586-elf\bin in die PATH-Variable eintragen. Dann haben die Programme kein Präfix und heißen einfach *gcc*, *ld*, etc. Das kann allerdings unter Umständen zu Problemen führen, wenn noch mehr Compiler in der PATH-Variable eingetragen sind.

### MSYS einrichten

Für weitere Werkzeuge wie make, bash usw. wird wie bei MinGW die MSYS-Umgebung benötigt. Wenn MSYS bereits installiert ist, kann es problemlos weiter verwendet werden. In der Regel bedeutet das, dass das MSYS-Verzeichnis (Standard C:\msys\bin) ebenfalls in die PATH-Variable eingetragen werden muss.

Wenn bisher noch kein MinGW installiert war, ist vermutlich auch MSYS noch nicht eingerichtet. MSYS kann auf der [SourceForge-Seite von MinGW](http://sourceforge.net/projects/mingw/files/MSYS/) heruntergeladen werden. Um MSYS zu verwenden, muss dann das bin-Verzeichnis ebenfalls in die PATH-Umgebungsvariable eingetragen werden.

### NASM

Für týndur wird als Assembler außerdem NASM benötigt, den es auch auf SourceForge zum [Download](http://sourceforge.net/projects/nasm/files/) gibt. Diesen auch einfach installieren.

## Cross-Compiler Kommandozeile

Ich verwende für týndur eine Batch-Datei, die mir die Umgebung einrichtet. Sie richtet die PATH-Variable ein, und startet die Kommandozeile. Zum Beispiel kann sie so aussehen:

    SET PATH=C:\msys\bin;C:\crosstools\bin;C:\Programme\NASM;%PATH%
    cmd /k cls

Diese Datei kopiere ich mir in das Wurzelverzeichnis des Quelltextbaums von týndur und starte sie. Durch die Eingabe von *make* sollte dann týndur vollständig kompilieren.

## týndur-Disketten-Images

Das Buildsystem von týndur ist nicht darauf ausgelegt unter Windows ein GRUB-Image zu erstellen, deswegen ist dort eine alternative Lösung gefragt. Dieses Thema gehört zwar nicht mehr direkt zum Cross-Compiler, aber da dieses mehr oder wenige eine Anleitung ist, wie man týndur unter Windows baut, schreibe ich das vorerst mal hierhin.

Um die GRUB-Problematik zu umgehen, ist es am einfachsten einfach ein fertiges Image (z.B. von den [Releases](http://download.tyndur.org/releases/)) nehmen, und darauf die Dateien von Hand zu kopieren. Diese Images kann man zum Beispiel mit [Virtual Floppy Drive](https://github.com/lowlevel-eu/wiki/wiki/Virtual-Floppy-Drive "Virtual Floppy Drive") als virtuelles Laufwerk einbinden, um sie zu verändern.

Nachdem du týndur mit *make* kompiliert hast, kannst du mit *make updateroot* die erstellten Programme in der passenden Verzeichnisstruktur zusammenstellen lassen. Das Ergebnis landet im Verzeichnis *build\root* und den Inhalt davon kannst du dann einfach auf das Disketten-Image kopieren und ggf. boot/grub/menu.lst anpassen.

## Feedback

Feedback im Forum, im IRC oder auf der Diskussionsseite ist erwünscht. Besonders, wenn irgendwas nicht funktioniert.

## Probleme

### gcc: CreateProcess: No such file or directory

- Die beste Lösung dafür ist, nicht gcc.exe und die anderen Programme im Verzeichnis i586-elf\bin zu benutzen, sondern die i586-elf-gcc.exe und so weiter im Verzeichnis bin.
- Alternative: Dieser Fehler tritt auf, weil der gcc die Datei cc1.exe nicht finden kann. Man könnte diese (und cc1plus.exe und collect2.exe) als Workaround einfach von libexec\gcc\i586-elf\4.4.0 nach i586-elf\bin kopieren. Das sorgt allerdings unter Umständen für weitere Probleme, wenn man die mitgelieferte Bibliotheken nutzen will, siehe z.B. nächstes Problem.
- Ein Auftreten dieser Meldung bei i586-elf-gcc (der eigentlich nicht das Problem haben sollte) wurde im Forum durch den selben Workaround gelöst. [\[1\]](https://lowlevel-eu.github.io/forum/topics/2345/index.html#msg26522)

### error: no include path in which to search for stdio.h (oder andere .h)

Eins vorweg: Die Verwendung der mitgelieferten Bibliotheken ist etwas tricky, weil dieser Compiler für das generische target i586-elf und nicht für ein bestimmtes Betriebssystem kompiliert wurde. Für alle Funktionen fehlen deswegen die Systemaufrufe, die die eigentliche Arbeit machen. Das heißt die meisten Standardfunktionen machen entweder nichts, oder bringen den Kernel/das Programm zum Absturz.

- Die Lösung dafür ist, nicht gcc.exe und die anderen Programme im Verzeichnis i586-elf\bin zu benutzen, sondern die i586-elf-gcc.exe und so weiter im Verzeichnis bin.

### crt0.o: No such file or directory

Dieser Compiler wurde für das generische Target i586-elf und nicht für ein bestimmtes Betriebssystem kompiliert. Weil crt0.o für jedes Betriebssystem anders ist, ist diese nicht mitgeliefert.

- Lösung: crt0.o im Linkerskript nicht erwähnen, oder selbst etwas gleichwertiges bereitstellen.

  

## Siehe auch

- [Cross-Compiler](https://github.com/lowlevel-eu/wiki/wiki/Cross-Compiler "Cross-Compiler")
- [Cross-Compiler für x86-64-Systeme](https://github.com/lowlevel-eu/wiki/wiki/X86-64-Cross-Compiler "X86-64 Cross-Compiler")
- [Cross-Compiler für ARM-Systeme](https://github.com/lowlevel-eu/wiki/wiki/ARM-Cross-Compiler "ARM Cross-Compiler")

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/8723/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1450/index.html)

<!-- MediaWiki page 1450; revision 8723; parent 8722; 2010-10-27T15:45:44Z -->
