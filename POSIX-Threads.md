# POSIX Threads

Diese Seite ist ein Artikel, welcher **mehr** haben könnte..  

Wenn du mehr darüber weißt oder recherchieren willst, bist **du** aufgerufen, dies zu tun. Wenn du dir in einer Sache nicht sicher bist, dann stell es auf die Diskussionsseite.

POSIX Threads (auch pthreads genannt) sind eine der beiden relevanten Betriebssystem-APIs für Multithreading (die andere ist die [Win32 API](https://github.com/lowlevel-eu/wiki/wiki/Windows "Windows")). Dabei werden in der Basisversion Mutexe, Condvars und [Threads](https://github.com/lowlevel-eu/wiki/wiki/Prozess#threads "Thread") unterstützt, jeweils mit einigen Attributen. Der Standard wurde mehrfach erweitert und ist inzwischen wesentlich komplexer, aber die Basisversion ist für die meisten Hobby-OS vermutlich schon ein sehr guter Stand.

Es gibt keine Bibliothek "pthreads" die einfach nur portiert werden muss, es ist nur eine Beschreibung der API. Die ganzen Funktionen müssen für den eigenen Kernel selber implementiert werden. Bestenfalls entsteht dabei eine eigene `libpthread.a`, da viele Buildsysteme davon ausgehen dass es eine eigene lib ist.

## Weblinks

- [The Single UNIX ® Specification, Version 2, pthread.h](https://pubs.opengroup.org/onlinepubs/007908799/xsh/pthread.h.html)
- [LF OS Branch für pthread (und bisschen mehr weil Chaos)](https://praios.lf-net.org/littlefox/lf-os_amd64/-/tree/pthread)

\[Kategorie:Glossar\] \[Kategorie:Multitasking\]

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/11496/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2675/index.html)

<!-- MediaWiki page 2675; revision 11496; parent 11494; 2020-08-20T13:04:44Z -->
