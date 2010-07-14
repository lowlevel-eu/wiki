# Portieren von Programmen und Bibliotheken

| Portieren von Programmen und Bibliotheken |  |
| ------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Schwierigkeit**: *nicht angegeben*<br> |  |
| Benötigtes Vorwissen: | *[keins\*](https://github.com/lowlevel-eu/wiki/wiki/OS-Dev-f%C3%BCr-Einsteiger#voraussetzungen "OS-Dev für Einsteiger")* |
| Sprache: | [Assembler](https://github.com/lowlevel-eu/wiki/wiki/Assembler "Assembler"), [C](https://github.com/lowlevel-eu/wiki/wiki/C "C"),[C++](https://github.com/lowlevel-eu/wiki/wiki/C%2B%2B "C++") |

  

## Worum geht es in diesem Tutorial?

In diesem Tutorial geht es um portieren von Programmen und Bibliotheken aufs eigene OS. Es macht wenig Sinn alle Programme neuzuschreiben, weil es diese schon zu hunderten gibt.

## Vorbereitung

Als erstes solltest du dir einen Crosscompiler für dein OS aufsetzten und ein paar Funktionen in deiner LibC implementiert haben.

## Portieren

### Programme

Hier werde ich einige Programme auflisten, welche sich recht einfach portieren lassen und werde zu jedem Programm erklären welche Schritte notwendig sind.

#### FASM

Ich verwende als Beispiel die Version 1.69.14.

##### Benötigte Funktionen

\<sys/time.h\> \<c\> int gettimeofday(struct timeval \*restrict tp, void \*restrict tzp); \</c\>

\<stdlib.h\> \<c\> void \*malloc(size_t size); void free(void \*pointer); void exit ( int status ); char \* getenv ( const char \* name ); \</c\>

\<time.h\> \<c\> time_t time ( time_t \* timer ); \</c\>

\<stdio.h\> \<c\> FILE \*fopen(const char \*filename, const char \*mode); int fclose( FILE \*stream); size_t fread ( void \* ptr, size_t size, size_t count, FILE \* stream ); size_t fwrite ( const void \* ptr, size_t size, size_t count, FILE \* stream ); int fseek ( FILE \* stream, long int offset, int origin ); long int ftell ( FILE \* stream ); \</c\>

\<unistd.h\> \<c\> size_t write(int fd, const void \*buf, size_t count); \</c\>

wenn du alle diese Funktionen in deine rlibc implementiert hast kannst du weiterlesen ansonsten solltest du erstmal alle Funktionen implementieren

##### Bauen

Du brauchst FASM, LD und deine libc als .a Datei.

zuerst assembilierst du Fasm mit FASM fasm.asm fasm.o danach linkst du die fasm.o gegen deine libc.a

### Bibliotheken

Hier werde ich einige Bibliotheken auflisten, welche sich recht einfach portieren lassen und werde zu jedem Programm erklären welche Schritte notwendig sind.

#### zlib

Ich verwende als Beispiel die Version 1.2.5.

##### Benötigte Funktionen

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/7847/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2256/index.html)

<!-- MediaWiki page 2256; revision 7847; parent 7846; 2010-07-14T15:36:48Z -->
