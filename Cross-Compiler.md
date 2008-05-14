# Cross-Compiler

Ein Cross-Compiler ist ein Compiler, der Objektdateien für eine andere Plattform (Zielplattform oder target) als die Verwendete (host) erzeugt. Die Zielplattform kann sich dabei sowohl beim Betriebssystem, als auch beim verwendeten Prozessor unterscheiden.

# Anforderungen

Um einen Cross-Compiler zu bauen, werden die üblichen GNU-Tools benötigt. Dazu gehören binutils, gcc und make.

## Linux

Auf vielen Linux-Distributionen sind diese Programme standardmässig dabei. Wer eine Binärdistribution, wie zum Beispiel Ubuntu oder andere debian-Derivate, einsetzt und noch keine Programme kompiliert hat, muss unter Umständen noch Entwicklungspakete installieren (bei Ubuntu/Debian libc6-dev und texinfo).

## Windows

Wer Windows einsetzt hat grundsätzlich zwei Möglichkeiten an diese Tools zu kommen. Entweder [cygwin](http://www.cygwin.com/) oder [mingw](http://www.mingw.org/)

### Cygwin

Die Installation von Cygwin gestaltet sich recht einfach. Bei der Installation müssen jedoch ein paar Dinge beachtet werden, das betrifft vor allem die Auswahl der richtigen Pakete. Für das Kompilieren eines Cross-gcc müssen die folgenden Pakete unbedingt installiert werden:

- Devel -\> gcc
- Devel -\> make
- Web -\> wget

  

### mingw

TODO

  

# binutils

Die GNU-binutils beinhalten unter anderem den Linker ld, den Assembler as und viele weitere kleine Helfer wie ar, objdump oder objcopy. Da gcc auf diesen basiert, müssen diese vor dem gcc kompiliert werden. Diese sind streng genommen auch Bestandteil des Cross-Compilers, da sie auch für eine bestimmte Target- und Host-Plattform konfiguriert werden müssen. Jetzt aber zur eigentlichen Arbeit. Um die binutils zu kompilieren, muss zuerst der Quellcode heruntergeladen werden. Dieser kann von <http://ftp.gnu.org/gnu/binutils/> bezogen werden. In diesem Artikel wird von der Version 2.18 ausgegangen:

    $ wget http://ftp.gnu.org/gnu/binutils/binutils-2.18.tar.bz2

Er müsste aber auch für jüngere und ältere Versionen funktionieren. Nach dem Herunterladen muss das Archiv entpackt werden:

    $ tar -xjf binutils-2.18.tar.bz2

## Konfigurieren

Der nächste Schritt ist das Konfigurieren. Die Dokumentation empfiehlt binutils ausserhalb des Quellverzeichnisses zu konfigurieren und zu kompilieren:

    $ mkdir binutils-build
    $ cd binutils-build

Beim Konfigurieren muss auch das Verzeichnis festgelegt werden, in das die binutils installiert werden sollen. Hier wird jetzt `/usr/local/crosstools` benutzt. Folgender Befehl wird zum Konfigurieren beunutzt:

    $ ../binutils-2.18/configure --prefix=/usr/local/crosstools --target=i386-elf --disable-nls

Als Zielplattform wird hier i386-elf benutzt, da dies wohl die Meistbenutzte im Zusammenhang mit Betriebssystementwicklung ist. Der letzte Schalter `--disable-nls` dient dazu, sämtliche Übersetzungen zu deaktivieren, da die meist mehr verwirren als nützen.

## Kompilieren

Nach dem Konfigurieren ist der nächste Schritt das Kompilieren:

    $ make all

Wer eine CPU mit mehreren Kernen benutzt, kann diesen vorgang etwas beschleunigen, wenn er den Parameter -j3 benutzt. Dieser Signalisiert make, dass maximal 3 Instanzen des Compilers zur selben Zeit laufen dürfen. Standardmässig wird hier 1 benutzt. Als Daumenregel wird oft Anzahl der Kerne + 1 empfohlen.

## Installieren

Sobald das Kompilieren abgeschlossen ist, können die binutils installiert werden:

    $ make install
    $ cd ..

# gcc

Nachdem nun die binutils kompiliert und installiert wurden, kann mit gcc weitergefahren werden. Für das Konfigurieren von gcc müssen die Binutils in \$PATH also der Umgebungsvariable, die die Verzeichnisse enthält, in denen nach ausführbaren Dateien gesucht werden soll, enthält, sein. Erreicht wird das durch:

    $ export PATH="/usr/local/crosstools/bin:$PATH"

Wichtig ist hier, dass der eigene Pfad vor den originalen Pfaden steht, damit sicher die vorhin kompilierten binutils benutzt werden. Der Pfad /usr/local/crosstools muss auch hier wieder angepasst werden, wenn für den Präfix bei Binutils ein anderer benutzt wurde. Als nächstes muss der Quellcode von gcc heruntergeladen werden. Dieser kann von <http://ftp.gnu.org/gnu/gcc> bezogen werden. Während dem Schreiben dieses Artikels wurde die Version 4.2.3 benutzt. Aber auch hier gilt wieder, dass das auf andere Versionen übertragen werden kann. Das Archiv mit Namen gcc-core-\<VERSION\>.tar.bz2 muss auf jeden Fall heruntergeladen werden. Falls auch ein C++ Compiler gewünscht wird, ist auch gcc-g++-\<VERSION\>.tar.bz2 notwendig. Nach dem Download des einen oder der beiden Archive müssen diese wieder entpackt werden:

    $ tar -xjf gcc-core-4.2.3.tar.bz2
    $ tar -xjf gcc-g++-4.2.3.tar.bz2

## Konfigurieren

Auch für gcc wird empfohlen, ihn ausserhalb des Quellverzeichnisses zu bauen:

    $ mkdir gcc-build
    $ cd gcc-build
    $ ../gcc-4.2.3/configure --prefix=/usr/local/crosstools --target=i386-elf --disable-nls --without-headers --enable-languages=c,c++

Beim Konfigurieren von gcc muss unbedingt darauf geachtet werden, dass der selbe Präfix wie bei binutils benutzt wird. Sonst benutzt gcc später den falschen Assembler. Die drei ersten Konfigurationsoptionen haben wieder die selbe Bedeutung wie bei gcc und werden hier deshalb nicht noch mal erläutert. Der Schalter --without-headers teilt gcc mit, dass keine Libc Header installiert sind und er sie somit nicht benutzen darf, und die letzte Option --enable-languages legt die Sprachen fest, die der Compiler beherrschen soll. Wie vorhin schon gesagt, muss für den C++ Compiler das 2. Archiv auch heruntergeladen werden. Wenn der Compiler nur C kompilieren soll muss auch nur --enable-languages=c angegeben werden.

## Kompilieren

Auch hier ist der nächste Schritt nach dem Konfigurieren wieder das Kompilieren. Dieser Prozess dauert je nach Prozessorleistung recht lange. Gestartet wird das Kompilieren folgendermassen:

    $ make all-gcc

## Installieren

Nachdem gcc fertig kompiliert ist, kann er installiert werden. Das geschieht mit diesem Befehl:

    $ make install-gcc

## Benutzung

Beim Kompilieren von Programmen mit dem neuen Crosscompiler muss daran gedacht werden, dass dieser nur zum Kompilieren und nicht zum Linken benutzt werden kann, denn dafür fehlt eine installierte Libc. Deshalb muss der gcc mit dem -c Flag aufgerufen wird, damit er nur den Präprozessor aufruft und den Quellcode kompiliert aber nicht linkt.

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/2937/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1628/index.html)

<!-- MediaWiki page 1628; revision 2937; parent 2597; 2008-05-14T11:24:21Z -->
