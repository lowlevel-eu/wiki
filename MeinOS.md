# MeinOS

meinOS ist ein [Microkernel](https://github.com/lowlevel-eu/wiki/wiki/Ausgabe-2#der-microkernel "Ausgabe 2")-Betriebssystem für x86-Systeme. Außerdem unterstützt meinOS Mehrprozessor-Systeme. Es wird von [jgraef](https://lowlevel-eu.github.io/wiki/pages/1550/index.html "Benutzer:Jgraef") entwickelt.

## Entwicklung

Im Moment werden einige Kernel-Funktionen noch vollendet und es müssen noch viele Treiber geschrieben werden. Außerdem muss noch sehr viel getestet werden, da bis jetzt z.B noch keine Möglichkeit besteht Server oder Bibliotheken auf Logik-Fehler zu überprüfen.

### Komplett (oder noch in Arbeit)

- Kernel
  - Memorymanagement
  - Multiprocessor-Kompatibilität (noch nicht vollständig)
  - Taskmanagement (Taskwechsel-Algorithmus fehlt noch)
  - IPC (Message Passing)
  - (Kernel-)Timer (100Hz) - zeitversetztes Aufrufen von Funktionen (z.B für Beep)
  - [Multiboot](https://github.com/lowlevel-eu/wiki/wiki/Multiboot "Multiboot")-Kompatibilität

<!-- -->

- Server
  - Keyboard-Server
  - Console-Server
  - COM-Server
  - Floppy-Server (noch in Arbeit)
  - Filesystem-Server (noch in Arbeit)

<!-- -->

- Bibliotheken
  - ScreenIO-Bibliothek
  - System-Bibliothek (wird bestimmt noch größer)
  - IPC-Bibliothek
  - DevFS-Bibliothek

(Server und Bibliotheken sind noch nicht vollständig getestet, da Programme noch nicht richtig geladen werden.)

### Planung

- Init-Task (Initialisierung aller Treiber und des Login-Programms)
- Shell (eventuell Portierung einer vorhandenen Shell)
- devfs (FS-Treiber für /dev)
- Floppy-Treiber
- Ext2-Treiber
- eventuell pipefs (Für Named Pipes ohne "richtiges" FS, dass Named Pipes unterstützt)
- Einige kleine Programme (cp, mv, rm, mkfile, cat, echo, usw.)

Wie man sieht, ist noch eine Menge zu tun.

## Download

- Unoffizielles Release vom 19.11.07:
  - Floppy-Image: [floppy.img.gz](http://wonsheimlan.wo.funpic.de/meinos/floppy.img.gz) (76,5kB)
  - Sourcecode: [meinos.tar.gz](http://wonsheimlan.wo.funpic.de/meinos/meinos.tar.gz) (218,6kB)

## Screenshot (Unoffizielles Release vom 19.11.07)

![screen.gif](http://wonsheimlan.wo.funpic.de/meinos/screen.gif)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/2342/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1551/index.html)

<!-- MediaWiki page 1551; revision 2342; parent 2276; 2007-12-03T15:18:33Z -->
