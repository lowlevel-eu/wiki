# Enter / Leave

Das Befehlspaar *enter* und *leave* adjustiert den [Stack](Stack "Stack") für die Verwendung von lokalen Variablen.

  

## Funktionsweise

Das Befehlspaar *enter*/*leave* war nicht zwingend notwendig, da man sie durch mehrere Befehle ersetzen kann. Da aber diese Befehlsfolge von vielen Hochsprachen häufig verwendet wurde, hat man dieses spezielle Befehlspaar eingeführt.

### enter

*enter* hat folgende Syntax:

``` asm
enter operand1, operand2
```

Sie lässt sich ersetzen durch:

``` asm
push ebp
mov ebp, esp
sub esp, operand1
```

*operand1* gibt also an, wieviel Speicherplatz auf dem Stack für lokale Variablen freigehalten werden soll. *operand2* steht für die Verschachtelungstiefe und kann auf 0 gesetzt werden.

Wird der zweite Operand verwende (sprich \<\> 0) wird die Struktur komplizierter. In dieser Kombination wird der Befehl kann dieser Befehl dazu genutzt werden, eine Verschachtelte Funktion. Dabei entspricht:

``` asm
enter operand1, operand2
```

Folgender Darstellung in einer Art Pseudocode (wobei "framePtr" ein internes Hilfregister ist):

``` asm
push ebp
mov framePtr, esp
if (operand2 > 0) then
    repeat (operand2 - 1) times
        add ebp, 4
        push ebp
    end repeat
    push framePtr
end if
mov ebp, framePtr
sub esp, operand1
```

Die Funktion schiebt also nach zwischen dem Framepointer (der Position auf die ebp nachher zeigt.) und dem Speicherplatz für lokale Variablen noch einen Block der die Framepointer von operant2 darüber liegenden Funktionen abschießend mit sich selbst.

### leave

*leave* macht die Änderungen von *enter* rückgängig, damit der Aufrufstack wiederhergestellt wird und die Funktion zum Aufrufer zurückkehren kann:

``` asm
leave
```

Sie lässt sich ersetzen durch:

``` asm
mov esp, ebp
pop ebp
```

## Umsetzung in verschiedenen Compilern

### gcc

[gcc](GNU-Compiler-Collection "Gcc") verwendet nur den *leave*-Befehl, anstatt *enter* aber die obige Ersatzform.

## siehe auch

- [Stack](Stack "Stack")

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/11531/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2186/index.html)

<!-- MediaWiki page 2186; revision 11531; parent 10232; 2024-05-14T16:36:51Z -->
