# FPU (x86)

Diese Seite ist ein Artikel, welcher **mehr** haben könnte..  

Wenn du mehr darüber weißt oder recherchieren willst, bist **du** aufgerufen, dies zu tun. Wenn du dir in einer Sache nicht sicher bist, dann stell es auf die Diskussionsseite.

Die [FPU](https://github.com/lowlevel-eu/wiki/wiki/Mathematischer-Koprozessor "FPU") des [x86](https://github.com/lowlevel-eu/wiki/wiki/X86 "X86") - Prozessors nennt sich x87 und ist heute fest im Prozessor eingebaut. In den Anfangsjahren des x86ers war die FPU noch ein externer Chip, der auf dem Mainboard aufgelötet wurde, und nicht jeder x86 - Nutzer konnte eine FPU sein Eigen nennen.

Heute ist die FPU, wie bereits erwähnt, fest im Prozessor eingebaut, weshalb man sich auch darauf verlassen kann, dass die entsprechenden FPU - Befehle auch wirklich unterstützt werden.

Neben den mathematischen Befehlen, die den ursprünglichen Zweck der FPU darstellen, kann man auf der x87 - FPU auch sog. [MultiMedia Extensions](https://github.com/lowlevel-eu/wiki/wiki/MultiMedia-Extension "MMX") ausführen (die Register MM0 bis MM7 entsprechen den 80 Bit breiten FPU - Registern, wobei 16 Bits reserviert sind (man hat also nur 64 - Bit - Register zur Verfügung)). Allerdings sollte man sich vorher überlegen, ab welchem Prozessor man sein OS unterstützen will, denn Intel empfiehlt heute, anstatt der langsameren [MMX](https://github.com/lowlevel-eu/wiki/wiki/MultiMedia-Extension "MMX") - Befehle die performanteren [SSE](https://github.com/lowlevel-eu/wiki/wiki/Streaming-SIMD-Extensions "SSE") - Befehle zu verwenden, die direkt vom Hauptprozessor abgearbeitet werden.

  

## Aufbau

Der mathematische Koprozessor des [x86](https://github.com/lowlevel-eu/wiki/wiki/X86 "X86") - Prozessors verfügt über acht 80 - Bit - [Register](https://github.com/lowlevel-eu/wiki/wiki/Register "Register"), die von ST(0) bis ST(7) angesprochen werden können. Sie werden allerdings, anders als etwa die [Allzweckregister](https://github.com/lowlevel-eu/wiki/wiki/X86#allzweckregister "X86"), wie ein Stack organisiert, d. h. ein gepushter Wert gelangt ins Register ST(0) und alle bisherigen Werte rutschen eins nach oben, also ST(1) nach ST(2), ST(2) nach ST(3) usw. et vice versa. Viele Befehle verarbeiten ST(0) und ST(1) und geben den Rückgabewert dann in ST(0) zurück.

Die ersten 64 Bits in einem ST(x) - Register stellen dabei die Mantisse, also die Basis, dar, während der Rest den Exponenten darstellt, der übrigens sowohl positiv als auch negativ sein kann. Der tatsächliche Wert wird dann mit "Mantisse mal zwei hoch Exponent" berechnet.

  
Abgesehen davon gibt es noch einige weitere Register:

- Control - Word - Register
- Status - Word - Register
- Instruction - und Data - Pointer
- Opcode - Register
- Tag - Word - Register

Die Register (außer Tag - Word) haben vor allem zwei Bedeutungen:

- Exception Handling, wenn auf der FPU ein Fehler aufgetreten ist
- Sie stellen eine Art Flags dar mit Einstellungsmöglichkeiten z. B. zur Genauigkeit oder zur Rundungsmethode

Das Tag - Word - Register stellt Informationen zu den einzelnen ST(x) - Registern bereit. Es ist 16 Bits lang und bietet somit 2 Bits pro Register (die ersten zwei für ST(0) etc.):

- 0b00: Der Wert im Register ist irgend ein gültiger Wert außer Null.
- 0b01: Der Wert im Register ist gültig und gleich Null.
- 0b10: Der Wert im Register ist ein spezieller Wert, z. B. unendlich.
- 0b11: Es ist kein Wert im Register vorhanden; Das Register ist leer. Dieser Fall tritt beispielsweise auf, wenn man vor der Benutzung irgendwelcher FPU - Befehle, die auf den Stack zugreifen, ein ST(x) - Register betrachtet. Der Wert ist nicht definiert.

  

## Befehle

Hier werden nur die mathematischen Befehle erläutert. Für die MMX - Befehle, die die FPU - Register nutzen, gibt es [hier](https://github.com/lowlevel-eu/wiki/wiki/MultiMedia-Extension "MMX") einen eigenen Artikel.

Die Befehle werden hier in Intel - Assembler - Syntax angegeben.

### Schiebeoperationen

#### fild

Der Befehl fild lädt die angegebene Ganzzahl auf den Stack (ST(0)).

\<asm\> fild eax ;Lädt das eax - Register in ST(0). Der ursprüngliche Wert wird nach ST(1) verschoben etc. \</asm\>

#### fld

Wie fild, allerdings mit reellen Zahlen.

\<asm\> zahl dd 3.1415926536 fld zahl ;Pi ist jetzt in ST(0). \</asm\>

### Rechenoperationen

#### fadd

Führt eine Addition durch. Folgende Muster werden unterstützt: \<asm\>

Ohne Operandangabe  

fadd ;ST(0) + ST(1), Ergebnis in ST(0)

1 Operand angegeben  

fadd memvar ;memvar + ST(0), Ergebnis in ST(0)

2 Operanden angegeben (beide Operanden sind FPU - Register, eins davon muss ST(0) sein)

fadd ST(5), ST(0) ;ST(5) + ST(0), Ergebnis in ST(0) \</asm\>

#### fmul

Führt eine Multiplikation durch. Die möglichen Muster entsprechen denen bei fadd.

#### fsub

Führt eine Subtraktion durch. Die möglichen Muster entsprechen denen bei fadd und fmul. Hier ist zu beachten, dass

- bei keinem angegebenen Operanden ST(1) von ST(0) subtrahiert wird (und nicht umgekehrt).
- bei einem angegebenen Operanden der Operand von ST(0) subtrahiert wird.
- bei zwei angegebenen Operanden der zweite Operand vom ersten subtrahiert wird. Dieser kann sowohl ST(0) als auch ein anderes ST(x) - Register sein (Aufrufkonvention bei fadd beachten!).

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/10717/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2587/index.html)

<!-- MediaWiki page 2587; revision 10717; parent 10716; 2012-08-20T14:02:08Z -->
