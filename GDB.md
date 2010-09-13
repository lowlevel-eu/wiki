# GDB

Der GDB (GNU Debugger) ist ein sehr nützliches Werkzeug um Programme zu debuggen. Auch wenn GDB ein sehr mächtiges Programm ist, so ist es doch relativ einfach mit ihm auch den eigenen Kernel zu debuggen.

Um GDB dazu zu bringen den Kernel über die RS232 zu debuggen sind folgende Dinge nötig:

- 2 Computer die über eine RS232-Schnittstelle verfügen
- Ein Lauffähiges Betriebssystem auf dem GDB installiert ist
- und der eigene Kernel mit [RS232-Treibern](https://github.com/lowlevel-eu/wiki/wiki/Serielle-Schnittstelle "Rs232")

Damit der eigene Kernel allerdings in der Lage ist sich mit GDB zu verbinden muss man die Datei *i386-stub.c* zu dem Kernel linken. Diese Datei findet man in den GDB-Source-Files.

Damit dieser Code erfolgreich kompiliert und gelinkt wird müssen folgende Funktionen bereitgestellt werden: \<c\>int getDebugChar(); // Liest Daten (Bytes) von der Seriellen Schnittstelle void putDebugChar(int chr); // Schickt Daten (Bytes) über die serielle Schnittstelle void exceptionHandler(int exception_number, void \*exception_address); // wird benötigt um exception-handler einzurichten\</c\>

Zusätzlich wird die ANSI-C-Funktion: *strcpy* benötigt. An einigen Stellen im Code noch wird die Funktion *fprintf* aufgerufen. Diese sollten auskommentiert oder besser durch Kernel-eigene Äquivalente ersetzt werden.

Nun muss nur noch eine Verbindung aufgebaut werden. Dazu muss im Kernel die Funktion *set_debug_traps* aus der i386-stub.c aufgerufen werden und ein breakpoint gesetzt werden damit der Kernel auf den User, bzw GBD wartet. \<c\>set_debug_traps(); // i386-stub initialisieren

asm volatile ("int \$3"); // warten bis GDB auf den anderen System gestartet wurde\</c\>

Auf der kernel-seite ist nun alles Fertig. Jetzt kann man sich ganz einfach mit GDB zu dem Kernel verbinden und ihn debuggen: ` $ gdb (gdb) target remote /dev/ttyS0 `

  

## Weblinks

- [GDB download und Dokumentation](http://sourceware.org/gdb/)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/8226/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2283/index.html)

<!-- MediaWiki page 2283; revision 8226; parent 0; 2010-09-13T13:57:13Z -->
