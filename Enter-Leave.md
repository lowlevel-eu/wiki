# Enter / Leave

Das Befehlspaar *enter* und *leave* adjustiert den [Stack](https://github.com/lowlevel-eu/wiki/wiki/Stack "Stack") für die Verwendung von lokalen Variablen.

  

## Funktionsweise

Das Befehlspaar *enter*/*leave* war nicht zwingend notwendig, da man sie durch mehrere Befehle ersetzen kann. Da aber diese Befehlsfolge von vielen Hochsprachen häufig verwendet wurde, hat man dieses spezielle Befehlspaar eingeführt.

### enter

*enter* hat folgende Syntax: \<asm\>enter operand1, operand2\</asm\> Sie lässt sich ersetzen durch: \<asm\>push ebp mov ebp, esp sub esp, operand1\</asm\> *operand1* gibt also an, wieviel Speicherplatz auf dem Stack für lokale Variablen freigehalten werden soll. *operand2* steht für die Verschachtelungstiefe und kann auf 0 gesetzt werden.

Wird der zweite Operand verwende (sprich \<\> 0) wird die Struktur komplizierter. In dieser Kombination wird der Befehl kann dieser Befehl dazu genutzt werden, eine Verschachtelte Funktion. Dabei entspricht:

\<asm\>enter operand1, operand2\</asm\> Folgender Darstellung in einer Art Pseudocode (wobei "framePtr" ein internes Hilfregister ist): \<asm\> push ebp mov framePtr, esp if (operant2 \> 0) then

       repeat (operant2 - 1) times
           add ebp, 4
           push ebp
       end repeat
       push framePtr

end if mov ebp, framePtr sub esp, operant1 \</asm\>

Die Funktion schiebt also nach zwischen dem Framepointer (der Position auf die ebp nachher zeigt.) und dem Speicherplatz für lokale Variablen noch einen Block der die Framepointer von operant2 darüber liegenden Funktionen abschießend mit sich selbst.

### leave

*leave* macht die Änderungen von *enter* rückgängig, damit der Aufrufstack wiederhergestellt wird und die Funktion zum Aufrufer zurückkehren kann: \<asm\>leave\</asm\> Sie lässt sich ersetzen durch: \<asm\>mov esp, ebp pop ebp\</asm\>

## Umsetzung in verschiedenen Compilern

### gcc

[gcc](https://github.com/lowlevel-eu/wiki/wiki/GNU-Compiler-Collection "Gcc") verwendet nur den *leave*-Befehl, anstatt *enter* aber die obige Ersatzform.

## siehe auch

- [Stack](https://github.com/lowlevel-eu/wiki/wiki/Stack "Stack")

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/10232/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2186/index.html)

<!-- MediaWiki page 2186; revision 10232; parent 7090; 2011-11-13T15:00:38Z -->
