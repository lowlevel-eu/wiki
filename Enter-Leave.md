# Enter / Leave

Die Befehle *enter* und *leave* adjustieren den [Stack](https://github.com/lowlevel-eu/wiki/wiki/Stack "Stack") für die Verwendung von lokalen Variablen.

  

## Funktionsweise

Das Befehlspaar enter/leve war nicht zwingend notwendig, da man sie durch mehrere Befehle ersetzen kann. Da aber diese Befehlsfolge von vielen Hochsprachen häufig verwendet wurde, hat man dieses spezielle Befehlspaar eingeführt.

### enter

Enter hat folgende Syntax: \<asm\> enter operand1, operand2 \</asm\> Sie lässt sich ersetzen durch: \<asm\> push ebp mov ebp, esp sub esp, operand1 \</asm\> *operand1* gibt also an, wieviel Speicherplatz auf dem Stack freigehalten werden soll für lokale Variablen. *operand2* steht für die Verschachtlungstiefe und kann auf 0 gesetzt werden.

## leave

Leave macht die Änderungen von Enter rückgängig, damit der Aufrufstack wiederhergestellt wird und die Funktion zum Aufrufer zurückkehren kann: \<asm\> leave \</asm\> Sie lässt sich ersetzen durch: \<asm\> mov esp, ebp pop ebp \</asm\>

## Umsetzung in verschiedenen Compilern

### gcc

[gcc](https://github.com/lowlevel-eu/wiki/wiki/GNU-Compiler-Collection "Gcc") verwendet nur den *leave*-Befehl, anstatt *enter* aber die obige Ersatzform.

## siehe auch

- [Stack](https://github.com/lowlevel-eu/wiki/wiki/Stack "Stack")
- lokale Variablen

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/7087/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2186/index.html)

<!-- MediaWiki page 2186; revision 7087; parent 0; 2010-02-17T14:34:14Z -->
