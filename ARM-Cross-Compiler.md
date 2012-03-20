# ARM Cross-Compiler

Wer ein Betriebssystem (oder generell Applikationen) für auf ARM-Prozessoren basierenden Architekturen erstellen will, aber selber nicht auf einer solchen entwickelt, muss sich einen Cross-Compiler erstellen bzw. verwenden. In diesem Artikel wird erklärt, wie ein Cross-Compiler unter Linux für die ARM-Architektur erstellt wird.

  

## Vorbereitungen

Die Erstellung eines Cross-Compilers für ARM-Architekturen erfolgt anfangs analog zu der Erstellung eines [Cross-Compilers](https://github.com/lowlevel-eu/wiki/wiki/X86-64-Cross-Compiler "X86-64 Cross-Compiler") für [x86-64 Prozessoren](https://github.com/lowlevel-eu/wiki/wiki/X86-64 "X86-64"): Es müssen die [binutils](http://ftp.gnu.org/gnu/binutils/binutils-2.21.1a.tar.bz2) und der [gcc](http://ftp.gnu.org/gnu/gcc/gcc-4.6.0/gcc-core-4.6.0.tar.bz2) in ihrer jeweils aktuellen Version (Stand: 11. Mai 2011) heruntergeladen werden. Sollen mehr Sprachen als C unterstützt werden, so müssen die entsprechenden Pakete unter [\[1\]](http://ftp.gnu.org/gnu/gcc) heruntergeladen werden.

Es werden nun ein paar Variablen erstellt:

    $ export PREFIX=/usr/cross/arm
    $ export TARGET=arm-unknown-linux-gnu

Der Pfad unter PREFIX kann geändert werden, wenn die Cross-Tools an anderer Stelle compilliert werden sollen.

## binutils bauen

Sofern nicht schon geschehen, sollte man jetzt das binutils-Paket entpacken, in diesem Beispiel werden die binutils nach */usr/src/cross-arm-binutils* entpackt. Nun sollte ein separates Verzeichnis erstellt werden, in welchem die binutils gebaut werden, in unserem Beispiel ist das */usr/src/binutils-arm*. Nun wechselt man in eben dieses Verzeichnis und ruft configure wie folgt auf:

    $ ../cross-arm-binutils/configure --target=$TARGET --prefix=$PREFIX

Nach erfolgreichem configure können die binutils nun gebaut werden mittels

    $ make all
    $ make install

## gcc bauen

Nun geht's an den gcc: Hier gilt auch wieder, sofern nicht schon geschehen, den gcc zu entpacken, in diesem Beispiel nach */usr/src/cross-arm-gcc*. Nun sollte, genau wie bei den binutils, ein separates Verzeichnis erstellt werden, in welchem der gcc gebaut wird, in unserem Beispiel ist das */usr/src/gcc-arm*. Nun wechselt man in eben dieses Verzeichnis und setzt erst den neuen Pfad zu den ARM-binutils:

    $ export PATH=$PATH:$PREFIX/bin

Dann ruft man configure wie folgt auf:

    $ ../cross-arm-gcc/gcc-4.6.0/configure --target=$TARGET 
                  --prefix=$PREFIX --enable-languages=c --without-headers

Nach erfolgreichem configure kann der gcc mittels

    $ make all-gcc
    $ make install-gcc

gebaut und installiert werden.

### LibGCC bauen

Für bestimmte Operationen, z.B. Stack Unwinding, Ganzzahl- und Fließkommaarithmetik und andere Unterstützungsfunktionen benötigt man zusätzlich die LibGCC. Diese kann man zusätzlich erstellen:

    $ make all-target-libgcc
    $ make install-target-libgcc

### Fehler beim configure

Eventuell kann es sein, dass configure mit der Fehlermeldung abbricht, dass die Libraries **GMP** und/oder **MPFR** sowie **MCP** nicht installiert seien. Diese müssen dann per Paketverwaltung oder von Hand installiert werden. Hier kann GMP und [hier](http://www.mpfr.org/mpfr-current/mpfr-3.0.1.tar.gz) MPFR und [hier](http://www.multiprecision.org/mpc/download/mpc-0.9.tar.gz) MCP heruntergeladen werden, falls selbige nicht über die Paketverwaltung der Distribution erhältlich sind. Gebaut werden beide mit dem in Linux bekannten Dreisatz *./configure, make, make install*.

## Fertig!

Wenn alles geklappt hat, wurde nun ein Cross-Compiler für ARM-Architekturen erstellt. Die Tools befinden sich (im Beispiel dieses Artikels) unter */usr/cross/arm*.

  

## Siehe auch

- [Cross-Compiler](https://github.com/lowlevel-eu/wiki/wiki/Cross-Compiler "Cross-Compiler")
- [Cross-Compiler für x86-64-Systeme](https://github.com/lowlevel-eu/wiki/wiki/X86-64-Cross-Compiler "X86-64 Cross-Compiler")
- [Cross-Compiler für Windows (erzeugt ELF-Dateien)](https://github.com/lowlevel-eu/wiki/wiki/Crosscompiler-f%C3%BCr-Windows "Crosscompiler für Windows")

## Weblinks

- [summon-arm-toolchain](https://github.com/esden/summon-arm-toolchain/blob/master/summon-arm-toolchain) – Ein Script zum erstellen eines ARM-Cross-Compilers unter Linux

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/10534/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2099/index.html)

<!-- MediaWiki page 2099; revision 10534; parent 10533; 2012-03-20T14:31:24Z -->
