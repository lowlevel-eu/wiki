# C\+\+

| Allgemeines |  |
| -------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| Name: | C++ |
| Inlineassembler: | Ja |
| Compiler: | [g++](https://github.com/lowlevel-eu/wiki/wiki/GNU-Compiler-Collection "GNU Compiler Collection"), icc |
| Spracheneigenschaften |  |
| Plattformen: | Alle |
| Beispielkernel in der Sprache: | [C++-Kernel mit GRUB](https://github.com/lowlevel-eu/wiki/wiki/C%2B%2B-Kernel-mit-GRUB "C++-Kernel mit GRUB") |
| Homepage |  |

[The C++ Standards Committee](http://www.open-std.org/jtc1/sc22/wg21/)

**C++** wurde 1983 von Bjarne Stroustrup veröffentlicht, um C mit Sprachmitteln der objektorientierten Programmierung zu erweitern. Da C++ somit eine Weiterentwicklung von [C](https://github.com/lowlevel-eu/wiki/wiki/C "C") ist, sollte man sich auch den Wikiartikel über [C](https://github.com/lowlevel-eu/wiki/wiki/C "C") zu Gemüte führen.

## Überblick

Die meisten C++ Features sind ohne zusätzlichen Aufwand sofort verfügbar. Nur für die folgenden Features werden Hilfsfunktionen benötigt, welche der C++ Compiler von Haus aus nicht zur Verfügung stellt:

- [Startup-Code](https://github.com/lowlevel-eu/wiki/wiki/C%2B%2B#startup-code "C++")
- [Rein virtuelle Funktionen](https://github.com/lowlevel-eu/wiki/wiki/C%2B%2B#rein-virtuelle-funktionen "C++")
- [globale/statische Objekte](https://github.com/lowlevel-eu/wiki/wiki/C%2B%2B#globalestatische-objekte "C++")
- [new/delete](https://github.com/lowlevel-eu/wiki/wiki/C%2B%2B#newdelete "C++")
- [RTTI (= Runtime type information)](https://github.com/lowlevel-eu/wiki/wiki/C%2B%2B#rtti "C++")
- [Exceptions](https://github.com/lowlevel-eu/wiki/wiki/C%2B%2B#exceptions "C++")

Da jeder Compilerhersteller eine eigene ABI (= Application Binary Interface) zur Verfügung stellt, sind auch die Funktionsnamen sowie auch der Funktionsumfang, von Compiler zu Compiler verschieden.

## Startup-Code

Dieser Code wird ausgeführt, bevor die main-Funktion des Programmes/Kernels aufgerufen wird und muss zumindest die Kommandozeilenargumente, mit denen das Programm aufgerufen wurde, an die main-Funktion weiterreichen.

## rein virtuelle Funktionen

Wenn eine Klasse eine rein virtuelle Funktion nicht implementiert hat und diese Funktion aufgerufen wird, wird zur Fehlerbehandlung eine Hilfsfunktion aufgerufen, welche im Normalfall das Programm beendet.

### g++

\<cpp\> // Lizenz: public domain

extern "C" void \_\_cxa_pure_virtual() {

     // Fehlermeldung anzeigen
     // Programm/Kernel beenden

} \</cpp\>

## globale/statische Objekte

Da diese vor dem Eintritt in die main-Funktion initialisiert sein sollen, müssen auch Konstruktoren und Destruktoren aufgerufen werden.

### g++

Die Konstruktion der globalen/statischen Objekte ist unter g++ immer gleich. Nur die Destruktion der Selben hängt von der Verwendung des configure-flags --enable-\_\_cxa_atexit und vom Kommandozeilenparameter -fuse-cxa-atexit / -fno-use-cxa-atexit ab.

#### Konstruktoren

G++ erstellt eine "ctors\*" Sektion, welche ein Array aus Funktionszeigern ist. Diese Funktionszeiger zeigen jeweils auf einen Konstruktor. Man muss nun nur dieses Array durchgehen und alle Funktionen aufrufen und schon hat man alle globalen/statischen Objekte initialisiert.

In neueren Version von GCC wurde die Sektion .ctors\* in .init_array umbenannt und muss im gegebenenfalls im Linkerscript geändert werden.

\<cpp\> // Lizenz: public domain

typedef void (\*constructor)();

// Im Linkerskript definiert extern "C" constructor start_ctors; extern "C" constructor end_ctors;

extern "C" void initialiseConstructors();

// Ruft die Konstruktoren für globale/statische Objekte auf void initialiseConstructors() {

     for (constructor* i = &start_ctors;i != &end_ctors;++i)
       (*i)();

} \</cpp\>

Diese Funktion muss explizit aufgerufen werden bevor globale/statische Objekte verwendet werden. Dies kann beispielsweise im [Startup-Code](https://github.com/lowlevel-eu/wiki/wiki/C%2B%2B#startup-code "C++") geschehen.

#### Destruktoren (ohne --enable-\_\_cxa_atexit und ohne -fuse-cxa-atexit)

G++ erstellt eine "dtors\*" Sektion, analog zur "ctors\*" Sektion und speicher dort wiederum ein Array aus Funktionszeigern. Diesmal zeigen diese Funktionszeiger aber auf Destruktoren.

In neueren Version von GCC wurde die Sektion .dtors\* in .fini_array umbenannt und muss im gegebenenfalls im Linkerscript geändert werden.

#### Destruktoren (mit --enable-\_\_cxa_atexit oder mit -fuse-cxa-atexit)

Im Konstruktor eines globalen/statischen Objekts wird die folgende Funktion aufgerufen:

\<cpp\>

    int __cxa_atexit(void (* f)(void *), void *p, void *d);

\</cpp\>

f ist ein Funktionszeiger zu einem Destruktor, p der Parameter, der dem Destruktor übergeben werden soll und d ist das sog. "home DSO" (DSO = dynamic shared object). Diese Funktion sollte alle drei Parameter speichern und bei Erfolg 0, andernfalls nicht 0 zurückgeben. Wenn der Kernel/das Programm dann beendet wird, sollte man die Funktion

\<cpp\>

    void __cxa_finalize(void *d);

\</cpp\>

mit d = 0 aufrufen, um alle mit \_\_cxa_atexit registrierten Funktionen mit passenden Paramtern aufzurufen. Die registrierten Funktionen müssen in umgekehrter Reihenfolge aufgerugen werden. Außerdem muss man ein Symbol namens \_\_dso_handle bereitstellen. Es wird allerdings nur die Adresse des Symbols verwendet um ein DSO zu identifizieren und um \_\_cxa_atexit aufzurufen.

\<cpp\> // Lizenz: public domain

extern "C" {

     int __cxa_atexit(void (*f)(void *), void *p, void *d);
     void __cxa_finalize(void *d);

};

void \*\_\_dso_handle;

struct object {

     void (*f)(void*);
     void *p;
     void *d;

} object\[32\] = {0}; unsigned int iObject = 0;

int \_\_cxa_atexit(void (\*f)(void \*), void \*p, void \*d) {

     if (iObject >= 32) return -1;
     object[iObject].f = f;
     object[iObject].p = p;
     object[iObject].d = d;
     ++iObject;
     return 0;

}

/\* NOTE: Zerstört momentan unabhängig von d alle Objekte \*/ void \_\_cxa_finalize(void \*d) {

     unsigned int i = iObject;
     for (; i > 0; --i)
     {
       --iObject;
       object[iObject].f(object[iObject].p);
     }

} \</cpp\>

## new/delete

Um dynamisch Objekte mit new erstellen bzw. mit delete zerstören zu können muss man die vier Operatoren

- new
- new\[\]
- delete
- delete\[\]

implementieren.

Eine einfache Implementation ist z.B.: \<cpp\> void \*operator new( size_t size ) {

     return kcalloc( size );

}

void \*operator new\[\]( size_t size ) {

     return kcalloc( size );

}

void operator delete( void \*obj ) {

     kfree( obj );

}

void operator delete\[\]( void \*obj ) {

     kfree( obj );

} \</cpp\>

## RTTI

RTTI (Runtime Type Information) wird am besten innerhalb des Kernels komplett deaktiviert. Mit g++ geschieht dies mittels des Kommandozeilenparameter *-fno-rtti*. Ohne RTTI muss man aber auch auf *dynamic_cast* und *typeid* verzichten.

## Exceptions

Exceptions sollten auch am besten innerhalb des Kernels deaktiviert werden. Mit g++ können Exceptions über den Kommandozeilenparameter *-fno-exceptions* deaktiviert werden.

## sonstige Probleme

### C++-Funktionen aus C/Assembler nutzen

Um C++-Funktionen von Sourcecode, der in C oder Assembler geschrieben ist, aufrufen zu können, muss das *name mangling* – dabei werden die Funktionsnamen nicht direkt als Symbolnamen genommen, sondern Parameter- und Rückgabetypen und Informationen zum Namespace mit in den Symbolnamen eingebaut – für diese Funktionen deaktiviert werden. Dies geschieht dadurch, dass die betreffende Funktion innerhalb des C++-Sourcecodes *extern "C"* deklariert wird, wie in folgendem Beispiel: \<cpp\>extern "C" void foobar(int i, char\* s);\</cpp\> Anschließend kann die Funktion in C++ ganz normal definiert werden und schließlich aus dem C/Assembler-Sourcecode heraus wie sonst üblich aufgerufen werden.

Eine Einschränkung gibt es aber doch: man kann diese Funktion nicht mehr überladen, das würde beim Linken zu ernsten Problemen führen. Folgendes Beispiel funktioniert also nicht: \<cpp\>extern "C" void foobar(int i, char\* s); extern "C" void foobar(int i, double\* d);\</cpp\> Der Linker würde 2 Funktionen mit dem Namen 'foobar' finden und könnte das ganze nicht mehr linken und auch nicht feststellen, welche Funktion die Aufrufer jeweils meinen.

## Siehe auch

[C++-Kernel mit GRUB](https://github.com/lowlevel-eu/wiki/wiki/C%2B%2B-Kernel-mit-GRUB "C++-Kernel mit GRUB")

## Links

- [Draft des C++ Standards](http://www.open-std.org/JTC1/SC22/WG21/docs/papers/2006/n2135.pdf)
- [Draft des TR1 (=Technical Report 1)](http://www.open-std.org/JTC1/SC22/WG21/docs/papers/2005/n1836.pdf)
- [g++ ABI](http://www.codesourcery.com/cxx-abi/abi.html) (Nicht nur die ABI für Itanium, sondern auch für x86 und x86-64)
- [g++ ABI: Exception Handling](http://www.codesourcery.com/cxx-abi/abi-eh.html) (Nicht nur die ABI für Itanium, sondern auch für x86 und x86-64)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/11306/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1486/index.html)

<!-- MediaWiki page 1486; revision 11306; parent 9588; 2015-10-14T18:36:18Z -->
