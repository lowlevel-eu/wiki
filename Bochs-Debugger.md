# Bochs Debugger

Der [bochsinterne](https://github.com/lowlevel-eu/wiki/wiki/Bochs "Bochs") Debugger stellt eine nützliche Hilfe beim [Debuggen](https://github.com/lowlevel-eu/wiki/wiki/Debugging "Debugging") eines Betriebssystems dar, weil er unter anderem Registerinhalte, Speicherinhalte oder auch disassemblierte Codestellen ausgeben kann.

## Speicherinhalte ausgeben und manipulieren

Um sich den Speicherinhalt an einer bestimmten Adresse ausgeben zu lassen, verwendet man einen der folgenden Befehle:

    x /nuf virtuelle_Adresse
    xp /nuf physikalische_Adresse

n, u und f bestimmen dabei die Ausgabe genauer:

- n steht für die Anzahl der auszugebenen Einheiten
- u für die Größe einer Einheit (b=1, h=2, w=4 und g=8 Bytes)
- f legt das Ausgabeformat fest (d=dezimal, x=hexadezimal und t=binär)

Wenn [Paging](https://github.com/lowlevel-eu/wiki/wiki/Paging "Paging") deaktiviert ist, dann bewirken beide Befehle dasselbe.

Möchte man geziehlt bestimmte Werte im Arbeitsspeicher verändern, nutzt man:

    setpmem  physikalische_Adresse  Länge  Wert

Dadurch wird der Arbeitsspeicher von der physikalischen Adressen an soweit mit dem Wert gefüllt, wie die Länge angibt.

Zudem kann auch der Inhalt des [Stacks](https://github.com/lowlevel-eu/wiki/wiki/Stack "Stack") ausgegeben werden mit:

    print-stack [Anzahl_Elemente]

Im [Real Mode](https://github.com/lowlevel-eu/wiki/wiki/Real-Mode "Real Mode") werden dabei Words, im [Protected Mode](https://github.com/lowlevel-eu/wiki/wiki/Protected-Mode "Protected Mode") Dwords ausgegeben.

  

## Register ausgeben und manipulieren

| Befehl | auszugebene Register |
| ------------- | -------------------------------------------------------------------------------------------------- |
| reg | Alle [Register](https://github.com/lowlevel-eu/wiki/wiki/Register "Register") |
| sreg | Segment-Register |
| dreg | [Debug-Register](https://github.com/lowlevel-eu/wiki/wiki/Debug-Register "Debug Register") |
| creg | [Control-Register](https://github.com/lowlevel-eu/wiki/wiki/Control-Register "Control Register") |
| info eflags | [EFLAGS](https://github.com/lowlevel-eu/wiki/wiki/EFLAGS "EFLAGS") |
| fpu | [FPU](https://github.com/lowlevel-eu/wiki/wiki/Mathematischer-Koprozessor "FPU")-Register |

Außerdem gibt es die Möglichkeit die allgemeinen Register zu verändern mit dem Befehl:

    set Register = Wert

## Code ausführen und ausgeben

Die Codeausführung kann man jederzeit mit Strg+C anhalten oder auch gezielt Breakpoints setzen:

    vbreak segment:offset
    lbreak lineare_adresse

Auch gibt es die Möglichkeit Watchpoints an bestimmte Arbeitsspeicherstellen zu setzen. Wenn an diesen Stellen dann auf die Daten zugegriffen wird, wird die Codeausführung unterbrochen:

    watch r/w physikalische_Adresse

Mit r (lesen) und w (schreiben) wird bestimmt, bei welcher Art von Zugriff unterbrochen wird.

  
Wird die Ausführung angehalten, dann gibt Bochs die aktuelle Codestelle automatisch disassembliert aus. Möchte man den Code dann weiterlaufen lassen, kann man entweder mit

    cont

normal fortfahren oder mit

    step [Anzahl_Schritte]

Einzelschritte ausführen lassen.

## Sonstiges

- Mit „quit“ wird der Debugger beendet.
- Mit „help“ kann man sich die Liste der verfügbaren Befehle ausgeben.
- Mit „show int“ werden Interruptaufrufe ausgegeben.

## Weblinks

- <http://bochs.sourceforge.net/doc/docbook/user/internal-debugger.html> Liste aller verfügbaren Befehle (Englisch)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/11439/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2163/index.html)

<!-- MediaWiki page 2163; revision 11439; parent 10580; 2020-08-02T21:53:17Z -->
