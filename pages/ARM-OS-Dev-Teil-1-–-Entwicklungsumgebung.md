# ARM-OS-Dev Teil 1 – Entwicklungsumgebung

|  |  |  |
| ------------------------------------------------------------------------------------------------------------------------------------ | ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| « [ARM-OS-Dev für Einsteiger](ARM-OS-Dev-f%C3%BCr-Einsteiger.md "ARM-OS-Dev für Einsteiger") | **Navigation** | [ARM-OS-Dev Teil 2 – Assembler 101](ARM-OS-Dev-Teil-2-%E2%80%93-Assembler-101.md "ARM-OS-Dev Teil 2 – Assembler 101") » |

## Ziel, Computer, Betriebssystem, Editor, Versionsverwaltung

Hier gelten die gleichen Regeln wie in „[Teil 1 - Entwicklungsumgebung](Teil-1-Entwicklungsumgebung.md "Teil 1 - Entwicklungsumgebung")“ der x86-Reihe.

## Compiler

Wenn man nicht gerade auf einem ARM-Linux entwickelt, benötigt man einen Crosscompiler, um ARM-Programme und damit auch ein ARM-Betriebssystem erstellen zu können. Zusätzlich sind auch Cross-Binutils nötig. Letztere bekommt man relativ häufig von der Distribution als vorkompiliertes Paket (mit Namen wie „cross-arm-binutils“), ersteres eher selten. Der Artikel [ARM Cross-Compiler](ARM-Cross-Compiler.md "ARM Cross-Compiler") beschreibt, wie man einen Cross-GCC und Cross-Binutils unter Linux erstellt (unter Windows könnte dies etwas schwieriger werden, sollte aber ähnlich ablaufen).

## Emulator

Als Emulator für Integrator/CP-Boards ist mir nur QEMU bekannt. Die aktuelle Version kann unter <http://www.qemu.org/> geladen werden, gebaut wird mittels:

    ./configure --target-list=arm-softmmu
    make
    make install

Um QEMU zu starten, wird dann qemu-system-arm verwendet. Um explizit das Integrator/CP-Board als Plattform zu verwenden (welches aber Standard ist), wird der Parameter „-M integratorcp“ benötigt.

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/9759/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2418/index.html)

<!-- MediaWiki page 2418; revision 9759; parent 0; 2011-05-11T13:48:56Z -->
