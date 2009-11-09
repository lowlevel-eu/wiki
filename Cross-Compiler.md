# Cross-Compiler

Ein Cross-Compiler ist ein [Compiler](https://lowlevel-eu.github.io/wiki/pages/1923/index.html "Kategorie:Compiler"), der Objektdateien für eine andere Plattform (Zielplattform oder target) als die Verwendete (Hostsystem, kurz host) erzeugt. Die Zielplattform kann sich dabei sowohl beim [Betriebssystem](https://github.com/lowlevel-eu/wiki/wiki/Betriebssystem "Betriebssystem"), als auch beim verwendeten Prozessor unterscheiden.

  

## Allgemeines

Ein Cross-Compiler wird immer dann benötigt, wenn man Programme oder generell Code für eine andere Architektur als die eigene entwickeln (und auch in den entsprechenden Maschinencode) übersetzen will. Aber auch, wenn das Host-Betriebssystem bzw. die für dieses System verfügbaren Compiler nativ bestimmte Dateiformate nicht unterstützen muss ein Cross-Compiler genutzt werden.

Typische Fälle, in denen man einen Cross-Compiler braucht sind also:

- Man hat einen 32-Bit-Prozessor und möchte Code für einen 64-Bit-Prozessor übersetzen (und vice versa)
- Man hat einen x86-Prozessor und möchte Code für die ARM- oder PPC-Architektur entwickeln
- Man nutzt Windows und möchte [ELF](https://github.com/lowlevel-eu/wiki/wiki/Executable-and-Linking-Format "ELF")-Binaries erstellen

In diesen Fällen muss man sich einen Cross-Compiler erstellen.

  

## Bau eines Cross-Compilers

Der Bau eines Cross-Compilers gestaltet sich als recht einfach. Meistens gilt es, sich die aktuellen binutils und den gcc herunterzuladen. Die Befehle zum Übersetzen gleichen sich unter Linux sowie unter Windows/Cygwin.

### Linux

Unter Linux braucht man dazu [dieses](http://ftp.gnu.org/gnu/binutils/binutils-2.20.tar.gz) Paket mit den binutils und [dieses](http://ftp.gnu.org/gnu/gcc/gcc-4.4.2/gcc-core-4.4.2.tar.bz2) Paket mit dem gcc. Will man Unterstützung für mehr Sprachen als C müssen weitere Pakete [hier](http://ftp.gnu.org/gnu/gcc) heruntergeladen werden. Die einzelnen Sprachen müssen dann später beim Konfigurieren angegeben werden, aber dazu später mehr.

Unter Linux kann es passieren, dass spätestens beim Konfigurieren vom gcc selbiges mit einem Fehler abbricht, dass zwei Libraries nicht installiert seien: GMP und MPFR. Diese sind dann aus der Paketverwaltung der Distribution zu beziehen oder können hier und [hier](http://www.mpfr.org/mpfr-current/mpfr-2.4.1.tar.bz2) heruntergeladen werden. Diese müssen nur entpackt und mit dem bekannten Dreisatz *./configure, make, make install* gebaut und installiert werden.

  

### Windows

Unter Windows gibt es zwei Möglichkeiten zum Bau eines Cross-Compilers:

#### Cygwin

Cygwin kann als "emulierte Linux-Umgebung" unter Windows angesehen werden. Cygwin lässt sich leicht installieren: [diese](http://www.cygwin.com/setup.exe) Setup-Datei reicht, der Rest erledigt der Installer. Es können dann alle benötigten Pakete heruntergeladen und mit installiert werden. Besonders wichtig sind folgende Pakete:

- Devel -\> gcc4
- Devel -\> make
- Libs -\> libgmp-devel
- Libs -\> libmpfr-devel
- Web -\> wget

optional:

- Devel -\> [nasm](https://github.com/lowlevel-eu/wiki/wiki/Netwide-Assembler "Netwide Assembler")

Ist Cygwin erfolgreich eingerichtet können die binutils sowie der gcc wie unter Linux konfiguriert und kompilliert werden. Hierfür müssen ebenfalls die [binutils](http://ftp.gnu.org/gnu/binutils/binutils-2.20.tar.gz) und der [gcc](http://ftp.gnu.org/gnu/gcc/gcc-4.4.2/gcc-core-4.4.2.tar.bz2) heruntergeladen werden.

#### minGW

MinGW ist ein auf Windows portierter GCC. Für mehr Informationen siehe [Cross-Compiler für Windows](https://github.com/lowlevel-eu/wiki/wiki/Crosscompiler-f%C3%BCr-Windows "Crosscompiler für Windows")

  

### Ablauf

Der Ablauf ist fast immer der gleiche: Die Pakete müssen ausgepackt und mit speziellen Parametern konfiguriert werden. Der Einfachheit halber sollte man dabei folgendes setzen:

    $ export TARGET=ziel-plattform
    $ export PREFIX=wo-die-crossutils-landen-sollen

Dann reicht es, beim configure --target=\$TARGET und --prefix=\$PREFIX anzugeben. Auch ist es sinnvoll, die binutils und den gcc außerhalb ihrer entpackten Verzeichnisse zu bauen, also immer seperate Verzeichnisse zu erstellen (gcc-ARCHITEKTUR und binutils-ARCHITEKTUR eigenen sich dafür z.B.).

Beide Pakete (eventuell noch weitere, je nachdem ob weitere Sprachen gewünscht werden) werden dann per

    $ tar -xjf paket.tar.endung

entpackt, wobei paket mit dem Namen des Pakets und endung mit der entsprechenden Endung zu ersetzen ist.

  

## Targets

### x86-64

Wer einen 32-Bit-Prozessor (oder ein 32-Bit-Betriebssystem) hat und Code für 64-Bit-Prozessoren und Betriebssysteme schreiben will, muss sich wie folgt seine Umgebung aufsetzen:

    $ export TARGET=x86_64-elf
    $ export TARGET=wo-die-crossutils-landen-sollen

Die binutils müssen dann entsprechend konfiguriert werden.

    $ ../binutils-2.20.0/configure --target=$TARGET --prefix=$PREFIX

Nach erfolgreichem Konfigurieren können die binutils dann per

    $ make
    # make install

gebaut werden. Mit dem gcc wird analog verfahren: Er wird wir folgt konfiguriert.

    $ ../gcc-4.4.2/configure --target=$TARGET --prefix=$PREFIX --enable-languages=c

Falls, wie im [Linux-Abschnitt](https://github.com/lowlevel-eu/wiki/wiki/Cross-Compiler#linux "Cross-Compiler") erwähnt, das Konfigurieren mit einer Fehlermeldung abgebrochen wird, müssen die entsprechenden Libraries heruntergeladen und gebaut sowie installiert werden.

Nach erfolgreichem Konfigurieren reicht dann ein

    $ make all-gcc
    # make install-gcc

Zum Installieren des gcc. Weitere Informationen zum Bau eines x86-64-Cross-Compilers findet man [hier](https://github.com/lowlevel-eu/wiki/wiki/X86-64-Cross-Compiler "X86-64 Cross-Compiler").

  

### ARM

Wer einen x86-Prozessor hat und gerne Code für die ARM-Architektur entwickeln möchte muss sich seine Umgebung verfährt analog. einzig das Target muss geändert werden:

    $ export TARGET=arm-unknown-linux-gnu

Dann ist genau so zu verfahren wie beim Bau eines x86-64-Cross-Compilers. Einen ausführlicheren Aritkel dazu und mehr Informationen finden sich [hier](https://github.com/lowlevel-eu/wiki/wiki/ARM-Cross-Compiler "ARM Cross-Compiler").

  

### ELF

Windows unterstützt nativ leider kein [ELF](https://github.com/lowlevel-eu/wiki/wiki/Executable-and-Linking-Format "ELF")-Format. Hier kann man sich schnell Abhilfe schaffen, in dem man den eigens von Jidder erstellten Cross-Compiler herunterlädt und sich seine Umgebung dementsprechend konfiguriert. Mehr Informationen dazu [hier](https://github.com/lowlevel-eu/wiki/wiki/Crosscompiler-f%C3%BCr-Windows "Crosscompiler für Windows").

  

## Siehe auch

- [Cross-Compiler für x86-64-Systeme](https://github.com/lowlevel-eu/wiki/wiki/X86-64-Cross-Compiler "X86-64 Cross-Compiler")
- [Cross-Compiler für ARM-Systeme](https://github.com/lowlevel-eu/wiki/wiki/ARM-Cross-Compiler "ARM Cross-Compiler")
- [Cross-Compiler für Windows (erzeugt ELF-Dateien)](https://github.com/lowlevel-eu/wiki/wiki/Crosscompiler-f%C3%BCr-Windows "Crosscompiler für Windows")

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/6233/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1628/index.html)

<!-- MediaWiki page 1628; revision 6233; parent 6206; 2009-11-09T16:08:47Z -->
