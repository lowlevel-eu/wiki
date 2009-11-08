# X86-64 Cross-Compiler

Wer ein 64-Bit-Betriebssystem entwickeln möchte, allerdings kein 64-Bit-Linux installiert hat, muss sich einen Cross-Compiler bauen, damit dieser 64-Bit-Dateien erstellen kann.

Im Folgenden wird erklärt, wie man einen Cross-Compiler für die x86-64-Plattform unter einem 32-Bit-Linux erstellt.

  

## Vorbereitung

Es gibt zwei verschiedene Wege, einen Cross-Compiler für x86-64 zu erstellen, wir bedienen uns hier der einfachsten Variante: Wir bauen die Binutils und den [GCC](https://github.com/lowlevel-eu/wiki/wiki/GNU-Compiler-Collection "GCC") neu, sodass wir einen funktionierenden gcc haben, mit dessen Hilfe wir x86-64-ELF-Dateien erstellen können.

Als erstes müssen dazu die Binutils und der gcc heruntergeladen werden. Wir benutzen dazu die neueste (Stand: 28. August 2009) Version beider Toolchains, einmal die [binutils 2.19.9](http://ftp.gnu.org/gnu/binutils/binutils-2.19.tar.bz2) und das Core-Package des [gcc 4.4.1](http://ftp.gnu.org/gnu/gcc/gcc-4.4.1/gcc-core-4.4.1.tar.bz2). Wenn allerdings auch Support für mehr Sprachen als C gewünscht ist, müssen dementsprechend zusätzliche Pakete unter [ftp.gnu.org/gnu/gcc](http://ftp.gnu.org/gnu/gcc) heruntergeladen werden.

Diese werden nun in ein beliebiges Verzeichnis entpackt, wir verwenden hier die Verzeichnisse **/usr/src/cross-gcc** und **/usr/src/cross-binutils**. Desweiteren sollte auch ein Verzeichnis für die Cross-Tools angelegt werden, in unserem Beispiel landen die fertigen Tools unter **/usr/cross**.

Falls man sich noch nicht auf der Shell befindet, sollte man **jetzt** zu selbiger wechseln.

Anschließend werden ein paar Variablen gesetzt:

    export PREFIX=/usr/cross
    export TARGET=x86_64-elf

  
PREFIX kann mit dem Verzeichnis ersetzt werden, wo die Tools später landen sollen.

Nun kann es schon losgehen!

## binutils erstellen

Wir erstellen nun die binutils. Das ist einfacher als gedacht, handelt es sich doch auch hier um den typischen Dreisatz:

configure make all make install

Ins binutils-Verzeichnis gewechselt, geben wir configure ein paar Parameter mit auf dem Weg:

    $ ./configure --target=$TARGET --prefix=$PREFIX

Wie man sieht, konfigurieren wir die Binutils für unser Zielsystem. Nach erfolgreichem configure kann nun gebaut werden:

    $ make all
    # make install

Die binutils wurden dann erfolgreich gebaut. Jetzt geht's weiter zum gcc.

  

## gcc bauen

### Halt, da fehlt noch was

Um den gcc zu bauen, benötigt es zwei (sofern nicht bereits installiert) Bibliotheken: Die GMP und MPFR-Libraries. Diese müssen ebenfalls runtergeladen und per ./configure, make, make install gebaut und installiert werden. Hier allerdings **erst** GMP **dann** MPFR bauen und installieren.

gcc wird beim configure schon meckern, wenn eines der Librarys fehlt.

TODO: Links dazu einfügen, find' ich grad' nicht \>.\<

  

### Jetzt aber

Nun bauen wir also den gcc. Dazu sind erst kurze Vorbereitungen nötig:

    $ export PATH=$PATH:$PREFIX/bin

Damit wird der Ort der Cross-binutils zum PATH hinzugefügt.

Jetzt wird gcc konfiguriert:

    $ ./configure --target=$TARGET --prefix=$PREFIX --enable-languages=c --without-headers

Sollte einer der benötigten Tools oder Librarys (bison, flex, GMP, MPFR) fehlen, meckert configure entsprechend. Nach erfolgreichem configure kann nun der gcc per

    make all-gcc
    make install-gcc

gebaut und installiert werden. Das Bauen des gcc dauert unter Umständen sehr lange (sind halt ein paar MB Sourcecode).

  

## Fertig!

Gratulation, ein Cross-Compiler für die x86-64-Plattform wurde erstellt! Die Tools befinden sich nun unter /usr/cross/ (in diesem Beispiel) und haben x86_64-elf- als Prefix, Beispiel: x86_64-elf-gcc, x86_64-elf-ld usw.

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/6195/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2060/index.html)

<!-- MediaWiki page 2060; revision 6195; parent 5781; 2009-11-08T23:49:04Z -->
