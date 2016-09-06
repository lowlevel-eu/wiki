# Cross-Compiler

Ein Cross-Compiler ist ein [Compiler](https://lowlevel-eu.github.io/wiki/pages/1923/index.html "Kategorie:Compiler"), der Objektdateien für eine andere Plattform (Zielplattform oder target) als die verwendete (Hostsystem, kurz host) erzeugt. Die Zielplattform kann sich dabei sowohl bezüglich des Betriebssystems als auch des verwendeten Prozessors unterscheiden.

  

## Allgemeines

Ein Cross-Compiler wird immer dann benötigt, wenn man Programme oder generell Code für eine andere Architektur als die eigene entwickeln und in den entsprechenden Maschinencode übersetzen will. Aber auch, wenn das Host-Betriebssystem bzw. die für dieses System verfügbaren Compiler nativ bestimmte Dateiformate nicht unterstützen, muss ein Cross-Compiler genutzt werden.

Typische Fälle, in denen man einen Cross-Compiler benötigt:

- Man hat einen 32-Bit-Prozessor und möchte Code für einen 64-Bit-Prozessor übersetzen (und vice versa)
- Man hat einen x86-Prozessor und möchte Code für die ARM- oder PPC-Architektur entwickeln
- Man nutzt MS Windows und möchte [ELF](https://github.com/lowlevel-eu/wiki/wiki/Executable-and-Linking-Format "ELF")-Binaries erstellen

In diesen Fällen muss man einen Cross-Compiler erstellen bzw. verwenden.

## Target Triplets

Target Triplets beschreiben eine Maschine. Man kann sie mithilfe von

    gcc -dumpmachine

für die derzeitige Maschine anzeigen lassen.

Ein Target Triplet besteht aus vier teilen, bei denen die mittleren beiden weggelassen werden können.

     architektur-hersteller-betriebsystem-abi (/Binärformat)

Ein beispiel von einem Raspberry Pi 2:

     armv7l-unknown-linux-gnueabihf

Das sagt aus, dass die Maschine einen [Little-Endian](https://github.com/lowlevel-eu/wiki/wiki/Bytereihenfolge "Little-Endian") ARMv7 Prozessor hat, unter Linux läuft und die GNU-embedded-ABI mit Hardfloat verwendet. Hersteller "unknown" kann weggelassen werden, das Betriebsystem kann auch weggelassen werden und wird als "none" angenommen. Weitere Beispiele:

     arm-none-eabi (ARM ohne spezielles Betriebsystem und ein embedded ABI)
     i686-elf (i686 ohne spezielles Betriebsystem und ELF als Binärformat)
     armeb-eabi (Big-Endian ARM mit embedded ABI)
     x86_64-elf (x86_64 mit ELF als Binärformat)

## Bau eines Cross-Compilers

Der Bau eines Cross-Compilers gestaltet sich recht einfach. Meistens gilt es, sich die aktuellen binutils und den gcc herunterzuladen. Die Befehle zum Übersetzen gleichen sich unter Linux und Windows (Cygwin, MinGW). Man sollte beachten, dass man eine recht aktuelle Version von GCC auf dem System installiert haben sollte (z.B. GCC \>= 4.9). Man benötigt außerdem g++, welches in den meisten Distributionen zusammen mit GCC installiert wird

### Linux

Unter Linux kann es passieren, dass spätestens beim Konfigurieren vom gcc selbiges mit der Fehlermeldung abbricht, dass drei Libraries nicht installiert seien: GMP, MPFR und MPC. Diese sind dann aus der Paketverwaltung der Distribution zu beziehen oder können hier, hier und hier heruntergeladen werden. Diese können entpackt und mit dem in Linux bekannten Dreisatz *./configure, make, make install* gebaut und installiert werden. Die nachfolgende Anleitung benötigt aber die Installation dieser 3 Libraries nicht.

### MS Windows

Unter MS Windows gibt es zwei Möglichkeiten zum Bau eines Cross-Compilers:

#### Cygwin

Cygwin kann als „emulierte Linux-Umgebung“ unter MS Windows angesehen werden. Cygwin lässt sich leicht installieren: [diese](http://www.cygwin.com/setup.exe) Setup-Datei reicht, den Rest erledigt der Installer. Es können dann alle benötigten Pakete heruntergeladen und ebenfalls installiert werden. Besonders wichtig sind folgende Pakete:

- Devel → gcc5
- Devel → make
- Web → wget

optional:

- Devel → [nasm](https://github.com/lowlevel-eu/wiki/wiki/Netwide-Assembler "Netwide Assembler")
- Libs → libgmp-devel
- Libs → libmpfr-devel
- Libs → libmpc-devel

Ist Cygwin erfolgreich eingerichtet, können die binutils sowie der gcc entsprechend der Vorgehensweise unter Ablauf gebaut werden.

#### MinGW

MinGW ist ein auf MS Windows portierter GCC. Die neueste Version des Installers für MinGW kann man auf der Projektseite unter [Installer / mingw-get-inst](http://sourceforge.net/projects/mingw/files/Installer/mingw-get-inst/) herunterladen. Bei der Installation sollte man das MSYS Base System noch auswählen. Um GCC zu kompilieren, kann man außerdem GMP, MPFR und MPC nachinstallieren, indem man nach der Installation mingw-get in der MinGW Shell aufruft:

    mingw-get install gmp mpfr mpc

Für den GCC selbst ist es nötig, die folgenden Schritte von der "MinGW Shell" (zu finden im Startmenü) auszuführen. Versucht man es von der Windows-CMD, tritt ein Fehler auf. Die Installationsdateien müssen, damit man sie von der MinGW-Shell aus erreichbar sind, im MinGW-Installationspfad unter msys/home/\<username\>/ liegen.

### Ablauf

Der Ablauf ist immer der gleiche. Folgende Pakete müssen heruntergeladen werden: [Binutils](http://ftp.gnu.org/gnu/binutils/binutils-2.26.tar.bz2), [gcc](http://ftp.gnu.org/gnu/gcc/gcc-5.3.0/gcc-5.3.0.tar.bz2), den oben genannten Links für MPC, MPFR und GMP und anschließend mittels

    $ tar -xf binutils-2.26.tar.bz2
    $ tar -xf gcc-5.3.0.tar.bz2
    $ cd gcc-5.3.0
    $ tar -xf ../mpc-1.0.3.tar.gz
    $ mv mpc-1.0.3 mpc
    $ tar -xf ../mpfr-3.1.3.tar.xz
    $ mv mpfr-3.1.3 mpfr
    $ tar -xf ../gmp-6.1.0.tar.xz
    $ mv gmp-6.1.0 gmp
    $ cd ..

entpackt werden.

    $ export TARGET=ziel-plattform
    $ export PREFIX=wo-die-crossutils-landen-sollen
    $ export PATH=$PREFIX/bin:$PATH

Dann reicht es, beim configure --target=\$TARGET und --prefix=\$PREFIX anzugeben. Auch ist es sinnvoll, die binutils und den gcc außerhalb ihrer entpackten Verzeichnisse zu bauen, also immer separate Verzeichnisse zu erstellen (gcc-ARCHITEKTUR und binutils-ARCHITEKTUR eignen sich beispielsweise hierfür). Jetzt konfigurieren wir die Pakete mit folgenden Befehlen (jeweils im entsprechenden separaten Verzeichnis (gcc-ARCHITEKTUR und binutils-ARCHITEKTUR) ausführen):

binutils:

    $ Pfad/zum/Code/configure  --prefix=$PREFIX --with-sysroot=$PREFIX --target=$TARGET --disable-nls --disable-werror

gcc:

    $ Pfad/zum/Code/configure --prefix=$PREFIX --target=$TARGET --disable-nls --enable-languages=c,c++ --disable-shared --without-headers

Nachdem die Pakete nun konfiguriert wurden, müssen die **binutils** mit

    $ make
    $ make install

bzw. der **gcc** mit

    $ make all-gcc
    $ make target-libgcc
    $ make install-gcc
    $ make install-target-libgcc

gebaut und installiert werden.

## Siehe auch

- [Cross-Compiler für Windows (erzeugt ELF-Dateien)](https://github.com/lowlevel-eu/wiki/wiki/Crosscompiler-f%C3%BCr-Windows "Crosscompiler für Windows")

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/11370/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1628/index.html)

<!-- MediaWiki page 1628; revision 11370; parent 11343; 2016-09-06T09:31:43Z -->
