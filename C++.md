# C\+\+

Da C++ eine Weiterentwicklung von C ist, sollte man sich auch den Wikiartikel zu [C](https://github.com/lowlevel-eu/wiki/wiki/C "C") zu Gemüte führen. Die meisten C++ Features sind ohne zusätzlichen Aufwand sofort verfügbar. Nur für die folgenden Features werden Hilffunktionen benötigt, welche der C++ Compiler von Haus aus nicht zur Verfügung stellt:

- Startup-Code
- rein virtuelle Funktionen
- globale/statische Objekte
- new/delete
- RTTI (= Runtime type information)
- Exceptions

Da jeder Compilerhersteller eine eigene ABI (= Application Binary Interface) zur Verfügung stellt sind auch die Namen und der Funktionsumfang von Compiler zu Compiler verschieden.

# Startup-Code

Dieser Code wird ausgeführt bevor die main-Funktion des Programmes/Kernels aufgerufen wird und muss zumindest die Kommandozeilenargumente, mit denen das Programm aufgerufen wurde, an die main-Funktion weiterreichen.

# rein virtuelle Funktionen

Wenn eine Klasse eine rein virtuelle Funktion nicht implementiert hat und diese Funktion aufgerufen wird, wird zur Fehlerbehandlung eine Hilfsfunktion aufgerufen, welche im Normalfall das Programm beendet.

## g++

    extern "C" void __cxa_pure_virtual()
    {
        // Fehlermeldung anzeigen
        // Programm/Kernel beenden
    }

# globale/statische Objekte

Da diese vor dem Eintritt in die main-Funktion initialisiert sein sollen, müssen auch Konstruktoren und Destruktoren aufgerufen werden.

## g++

Die Konstruktion der globalen/statischen Objekte ist unter g++ immer gleich. Nur die Destruktion der selben hängt von der Verwendung des configure-flags --enable-\_\_cxa_atexit und vom Kommandozeilenparameter -fuse-cxa-atexit ab.

### Konstruktoren

G++ erstellt eine "ctors\*" Sektion, welche ein Array aus Funktionszeigern ist. Diese Funktionszeiger zeigen jeweils auf einen Konstruktor. Man muss nun nur dieses Array durchgehen und alle Funktionen aufrufen und schon hat man alle globalen/statischen Objekte initialisiert.

### Destruktoren (ohne --enable-\_\_cxa_atexit und ohne -fuse-cxa-atexit)

G++ erstellt eine "dtors\*" Sektion, analog zur "ctors\*" Sektion und speicher dort wiederum ein Array aus Funktionszeigern. Diesmal zeigen diese Funktionszeiger aber auf Destruktoren.

### Destruktoren (mit --enable-\_\_cxa_atexit oder mit -fuse-cxa-atexit)

Im Konstruktor eines globalen/statischen Objekts wird die folgende Funktion aufgerufen:

    int __cxa_atexit(void (* f)(void *), void *p, void *d);

f ist ein Funktionszeiger zu einem Destruktor, p der Parameter, der dem Destruktor übergeben werden soll und d ist das sog. "home DSO" (DSO = dynamic shared object). Diese Funktion sollte alle drei Parameter speichern und bei Erfolg 0, andernfalls nicht 0 zurückgeben. Wenn der Kernel/das Programm dann beendet wird, sollte man die Funktion

    void __cxa_finalize(void *d);

mit d = 0 aufrufen, um alle mit \_\_cxa_atexit registrierten Funktionen mit passenden Paramtern aufzurufen. Die registrierten Funktionen müssen in umgekehrter Reihenfolge aufgerugen werden. Außerdem muss man ein Symbol namens \_\_dso_handle bereitstellen. Es wird allerdings nur die Adresse des Symbols verwendet um ein DSO zu identifizieren und um \_\_cxa_atexit aufzurufen.

    extern "C"
            {
            int __cxa_atexit(void (*f)(void *), void *p, void *d);
            void __cxa_finalize(void *d);
            };

    void *__dso_handle;

    struct object
    {
            void (*f)(void*);
            void *p;
            void *d;
    } object[32] = {0};
    unsigned int iObject = 0;

    int __cxa_atexit(void (*f)(void *), void *p, void *d)
    {
            if (iObject >= 32) return -1;
            object[iObject].f = f;
            object[iObject].p = p;
            object[iObject].d = d;
            ++iObject;
            return 0;
    }

    /* Zerstört momentan unabhängig von d alle Objekte */
    void __cxa_finalize(void *d)
    {
            unsigned int i = iObject;
            for (; i > 0; --i)
            {
                    --iObject;
                    object[iObject].f(object[iObject].p);
            }
    }

# new/delete

# RTTI

# Exceptions

# Links

- [g++ ABI](http://www.codesourcery.com/cxx-abi/abi.html) (Nicht nur die ABI für Itanium, sondern auch für x86 und x86-64)
- [g++ ABI: Exception Handling](http://www.codesourcery.com/cxx-abi/abi-eh.html) (Nicht nur die ABI für Itanium, sondern auch für x86 und x86-64)
- [OSDev.org wiki](http://www.osdev.org/wiki/C_PlusPlus)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/1897/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1486/index.html)

<!-- MediaWiki page 1486; revision 1897; parent 1794; 2007-03-27T18:50:42Z -->
