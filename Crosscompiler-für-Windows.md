# Crosscompiler für Windows

Für Windows wird ein [Cross-Compiler](https://github.com/lowlevel-eu/wiki/wiki/Cross-Compiler "Cross-Compiler") benötigt, um [ELF](https://github.com/lowlevel-eu/wiki/wiki/Executable-and-Linking-Format "ELF")-Dateien zu erstellen, denn die MinGW- und cygwin-Compiler unterstützen dieses Format nicht. Das ELF-Format bietet gegenüber dem PE-Format von Windows den Vorteil, dass es weniger Sonderbehandlung und Workarounds für bei der Entwicklung eines Betriebssystems benötigt. Die Verwendung eines Cross-Compilers bietet darüberhinaus mehr Kontrolle über den Ablauf des Kompiliervorgangs.

Dieser Artikel soll eine kleine Anleitung sein, wie man einen vorkompilierten [GCC](https://github.com/lowlevel-eu/wiki/wiki/GNU-Compiler-Collection "GCC") unter Windows so installiert, dass man damit [týndur](https://github.com/lowlevel-eu/wiki/wiki/T%C3%BDndur "Týndur") kompilieren kann. Allerdings ist der verwendete Compiler nicht auf ein bestimmtes System beschränkt, sondern erzeugt Dateien für das allgemeine Target *i586-elf*. Es sollte also kein Problem sein, diesen Compiler für ein anderes OS einzusetzen.

## Download

Der Compiler ist verfügbar unter <http://jidder.de/lost/files/crosstools-complete.rar>. Darin enthalten sind

- GCC 4.4.0 (C- und C++-Compiler)
- binutils 2.19.1
- newlib 1.17.0 und libstdc++ (C- bzw. C++-Standardbibliothek)

## Installation

Im Prinzip reicht es das Archiv zu entpacken (z.B. nach C:\crosstools), und in die PATH-Variable das Verzeichnis C:\crosstools\bin einzutragen. Alle Programme haben dann das Präfix "i586-elf-". Zum Beispiel der C-Compiler kann mit *i586-elf-gcc* aufgerufen werden.

týndur erwartet, dass dieses Präfix in der *config.sh* eingetragen wird, damit die Makefiles den Compiler finden. Dazu muss die Variable *COMPILER_PREFIX_I386* in Zeile 3 mittels *COMPILER_PREFIX_I386=i586-elf-* entsprechend gesetzt werden.

Alternativ kann man statt C:\crosstools\bin auch C:\crosstools\i586-elf\bin in die PATH-Variable eintragen. Dann haben die Programme kein Präfix und heißen einfach *gcc*, *ld*, etc. Das kann allerdings unter Umständen zu Problemen führen, wenn noch mehr Compiler in der PATH-Variable eingetragen sind.

### MSYS einrichten

Für weitere Werkzeuge wie make, bash, und so weiter, wird wie bei MinGW die MSYS-Umgebung benötigt. Wenn MSYS bereits installiert ist, kann es problemlos weiter verwendet werden. In der Regel bedeutet das, dass das MSYS-Verzeichnis (Standard C:\msys\bin) ebenfalls in die PATH-Variable eingetragen werden muss.

Wenn bisher noch kein MinGW installiert war, ist vermutlich auch MSYS noch nicht eingerichtet. MSYS kann auf der [SourceForge-Seite von MinGW](http://sourceforge.net/project/showfiles.php?group_id=2435&package_id=24963) heruntergeladen werden. Die Setup-Datei hat einen Namen in der Form MSYS-1.0.xx.exe, und muss nach dem Download einfach abgearbeitet werden. Um MSYS zu verwenden, muss dann das bin-Verzeichnis ebenfalls in die PATH-Umgebungsvariable eingetragen werden.

### NASM

Für týndur wird als Assembler außerdem NASM benötigt, den es auch auf SourceForge zum [Download](http://sourceforge.net/project/showfiles.php?group_id=6208&package_id=47034) gibt. Diesen auch einfach installieren.

## Cross-Compiler Kommandozeile

Ich verwende für týndur eine Batch-Datei, die mir Umgebung einrichtet. Sie richtet die PATH-Variable ein, und startet die Kommandozeile. Zum Beispiel kann sie so aussehen:

    SET PATH=C:\msys\bin;C:\crosstools\i586-elf\bin;C:\Programme\NASM;%PATH%
    cmd /k cls

Diese Datei kopiere ich mir in das Wurzelverzeichnis des Quelltextbaums von týndur und starte sie. Durch die Eingabe von make sollte dann týndur vollständig kompilieren.

## Feedback

Feedback im Forum, im IRC oder auf der Diskussionsseite ist erwünscht. Besonders, wenn irgendwas nicht funktioniert.

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/4414/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1450/index.html)

<!-- MediaWiki page 1450; revision 4414; parent 3942; 2009-05-27T21:12:13Z -->
