# Portieren von Programmen und Bibliotheken

Diese Seite ist ein Artikel, welcher **mehr** haben könnte..  

Wenn du mehr darüber weißt oder recherchieren willst, bist **du** aufgerufen, dies zu tun. Wenn du dir in einer Sache nicht sicher bist, dann stell es auf die Diskussionsseite.

| Portieren von Programmen und Bibliotheken |  |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Schwierigkeit**: [<img src="assets/Stern_gold.gif" width="16" height="16" alt="Stern gold.gif" />](assets/Stern_gold.gif)[<img src="assets/Stern_wei%C3%9F.gif" width="16" height="16" alt="Stern weiß.gif" />](assets/Stern_wei%C3%9F.gif)[<img src="assets/Stern_wei%C3%9F.gif" width="16" height="16" alt="Stern weiß.gif" />](assets/Stern_wei%C3%9F.gif)[<img src="assets/Stern_wei%C3%9F.gif" width="16" height="16" alt="Stern weiß.gif" />](assets/Stern_wei%C3%9F.gif)[<img src="assets/Stern_wei%C3%9F.gif" width="16" height="16" alt="Stern weiß.gif" />](assets/Stern_wei%C3%9F.gif)<br> |  |
| Benötigtes Vorwissen: | *[keins\*](OS-Dev-f%C3%BCr-Einsteiger.md#voraussetzungen "OS-Dev für Einsteiger")* |
| Sprache: | [Assembler](Assembler.md "Assembler"), [C](C.md "C"),[C++](C%2B%2B.md "C++") |

  
In diesem Tutorial geht es um das Portieren von Programmen und Bibliotheken aufs eigene Betriebssystem. Es ist nicht sehr sinnvoll, alle Programme neu zu schreiben, weil es diese schon zu hunderten gibt.

## Vorbereitung

Als erstes solltest du dir einen Crosscompiler für dein OS aufsetzten und ein paar Funktionen in deiner libc implementiert haben.

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

Wenn du alle diese Funktionen in deiner libc implementiert hast, kannst du weiterlesen, ansonsten solltest du dies erstmal tun.

##### Bauen

Du brauchst FASM, LD und deine libc als .a-Datei.

Zuerst assemblierst du FASM mit `fasm fasm.asm fasm.o`. Danach linkst du die `fasm.o` gegen deine `libc.a`.

### Bibliotheken

Hier werde ich einige Bibliotheken auflisten, welche sich recht einfach portieren lassen, und werde zu jedem Programm erklären, welche Schritte notwendig sind.

#### zlib

Ich verwende als Beispiel die Version 1.2.5.

##### Benötigte Funktionen

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/11083/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2256/index.html)

<!-- MediaWiki page 2256; revision 11083; parent 7859; 2013-03-25T08:30:17Z -->
