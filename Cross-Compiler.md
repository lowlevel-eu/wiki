# Cross-Compiler

Ein Cross-Compiler ist ein [Compiler](https://lowlevel-eu.github.io/wiki/pages/1923/index.html "Kategorie:Compiler"), der Objektdateien für eine andere Plattform (Zielplattform oder target) als die verwendete (Hostsystem, kurz host) erzeugt. Die Zielplattform kann sich dabei sowohl bezüglich des Betriebssystems als auch des verwendeten Prozessors unterscheiden.

  

## Allgemeines

Ein Cross-Compiler wird immer dann benötigt, wenn man Programme oder generell Code für eine andere Architektur als die eigene entwickeln und in den entsprechenden Maschinencode übersetzen will. Aber auch, wenn das Host-Betriebssystem bzw. die für dieses System verfügbaren Compiler nativ bestimmte Dateiformate nicht unterstützen, muss ein Cross-Compiler genutzt werden.

Typische Fälle, in denen man einen Cross-Compiler benötigt:

- Man hat einen 32-Bit-Prozessor und möchte Code für einen 64-Bit-Prozessor übersetzen (und vice versa)
- Man hat einen x86-Prozessor und möchte Code für die ARM- oder PPC-Architektur entwickeln
- Man nutzt MS Windows und möchte [ELF](https://github.com/lowlevel-eu/wiki/wiki/Executable-and-Linking-Format "ELF")-Binaries erstellen

In diesen Fällen muss man einen Cross-Compiler erstellen bzw. verwenden.

  

## Bau eines Cross-Compilers

Der Bau eines Cross-Compilers gestaltet sich recht einfach. Meistens gilt es, sich die aktuellen binutils und den gcc herunterzuladen. Die Befehle zum Übersetzen gleichen sich unter Linux und Windows (Cygwin, MinGW).

### Linux

Unter Linux kann es passieren, dass spätestens beim Konfigurieren vom gcc selbiges mit der Fehlermeldung abbricht, dass zwei Libraries nicht installiert seien: GMP und MPFR. Diese sind dann aus der Paketverwaltung der Distribution zu beziehen oder können hier und [hier](http://www.mpfr.org/mpfr-current/mpfr-2.4.1.tar.bz2) heruntergeladen werden. Diese müssen nur entpackt und mit dem in Linux bekannten Dreisatz *./configure, make, make install* gebaut und installiert werden.

  

### MS Windows

Unter MS Windows gibt es zwei Möglichkeiten zum Bau eines Cross-Compilers:

#### Cygwin

Cygwin kann als „emulierte Linux-Umgebung“ unter MS Windows angesehen werden. Cygwin lässt sich leicht installieren: [diese](http://www.cygwin.com/setup.exe) Setup-Datei reicht, den Rest erledigt der Installer. Es können dann alle benötigten Pakete heruntergeladen und ebenfalls installiert werden. Besonders wichtig sind folgende Pakete:

- Devel → gcc4
- Devel → make
- Libs → libgmp-devel
- Libs → libmpfr-devel
- Web → wget

optional:

- Devel → [nasm](https://github.com/lowlevel-eu/wiki/wiki/Netwide-Assembler "Netwide Assembler")

Ist Cygwin erfolgreich eingerichtet, können die binutils sowie der gcc entsprechend der Vorgehensweise unter Ablauf gebaut werden.

#### MinGW

MinGW ist ein auf MS Windows portierter GCC. Die neueste Version des Installers für MinGW kann man auf der Projektseite unter [Automated MinGW Installer / mingw-get-inst](http://sourceforge.net/projects/mingw/files/Automated%20MinGW%20Installer/mingw-get-inst/) herunterladen. Bei der Installation sollte man das MSYS Base System noch auswählen. Um GCC zu kompilieren, muss man außerdem GMP, MPFR und MPC nachinstallieren, indem man nach der Installation mingw-get in der MinGW Shell aufruft:

    mingw-get install gmp mpfr mpc

### Ablauf

Der Ablauf ist immer der gleiche. Folgende Pakete müssen heruntergeladen werden: [Binutils](http://ftp.gnu.org/gnu/binutils/binutils-2.20.tar.bz2) und [gcc](http://ftp.gnu.org/gnu/gcc/gcc-4.4.2/gcc-core-4.4.2.tar.bz2) und anschließend mittels

    $ tar -xjf binutils-2.20.tar.bz2
    $ tar -xjf gcc-core-4.4.2.tar.bz2

entpackt werden. Wenn noch weitere Sprachen zusätzlich zu C unterstützt werden sollen, müssen weitere Pakete heruntergeladen werden. Für C++ benötigt man zum Beispiel [dieses](http://ftp.gnu.org/gnu/gcc/gcc-4.4.2/gcc-g++-4.4.2.tar.bz2) Paket. Die komplette Liste befindet sich im Verzeichnis der jeweiligen GCC-Version auf dem FTP-Server. Danach müssen sie mit speziellen Parametern konfiguriert werden. Der Einfachheit halber sollte man dabei folgende Variablen setzen:

    $ export TARGET=ziel-plattform
    $ export PREFIX=wo-die-crossutils-landen-sollen

Dann reicht es, beim configure --target=\$TARGET und --prefix=\$PREFIX anzugeben. Auch ist es sinnvoll, die binutils und den gcc außerhalb ihrer entpackten Verzeichnisse zu bauen, also immer separate Verzeichnisse zu erstellen (gcc-ARCHITEKTUR und binutils-ARCHITEKTUR eignen sich beispielsweise hierfür ). Jetzt konfigureren wir die Pakete mit folgendne Befehlen (jeweils im entsprechenden separaten Verzeichnis (gcc-ARCHITEKTUR und binutils-ARCHITEKTUR) ausführen):

binutils:

    $ Pfad/zum/Code/configure  --prefix=$PREFIX --with-sysroot=$PREFIX --target=$TARGET --disable-nls

gcc:

    $ Pfad/zum/Code/configure --prefix=$PREFIX --target=$TARGET --disable-nls --enable-languages=c --disable-shared --disable-libssp

für welche CPU-Architektur der Cross-Compiler gebaut wird, wird mit dem *target*-Parameter angegeben. Hier eine nicht vollständige Liste der wichtigsten Targets:

- *x86_64-elf* (um auf einem 32-Bit-Prozessor/-OS für ein(en) 64-Bit-Prozessor/-OS zu kompilieren. Kann auch verwendet werden, um sich einen Cross-Compiler für Windows zu bauen.)
- *arm-unknown-linux-gnu* (um für ARM-Systeme Code zu kompilieren.)

Wenn weitere Sprachen unterstützt werden sollen und die entsprechenden Pakete heruntergeladen und entpackt wurden, dann müssen die Sprachen bei *--enable-languages=* durch Kommata getrennt aufgezählt werden. Nachdem die Pakete nun konfiguriert wurden, müssen diese jeweils noch mit

    $ make
    $ make install

gebaut und installiert werden.

## Siehe auch

- [Cross-Compiler für x86-64-Systeme](https://github.com/lowlevel-eu/wiki/wiki/X86-64-Cross-Compiler "X86-64 Cross-Compiler")
- [Cross-Compiler für ARM-Systeme](https://github.com/lowlevel-eu/wiki/wiki/ARM-Cross-Compiler "ARM Cross-Compiler")
- [Cross-Compiler für Windows (erzeugt ELF-Dateien)](https://github.com/lowlevel-eu/wiki/wiki/Crosscompiler-f%C3%BCr-Windows "Crosscompiler für Windows")

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/9796/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1628/index.html)

<!-- MediaWiki page 1628; revision 9796; parent 9795; 2011-05-17T10:50:32Z -->
