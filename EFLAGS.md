# EFLAGS

Das EFLAGS (Programmstatus und Kontrollregister) Register ist 32 Bit groß, wobei jedes Bit ein Flag repräsentiert. Es beinhaltet Status-Informationen über das laufende Programm und erlaubt anwendungsbasierte Prozessorkontrolle. Das Register kann nicht komplett verändert werden, es können nur die einzelnen Flags gesetzt oder gelöscht werden, meistens auch nur indirekt, in der Form das ein aufgerufener Befehl ein Flag als nebeneffekt ändert.

## Aufbau des EFLAGS-Registers

Im folgenden steht (X) für Systemflag, (S) für Statusflag und (C) für Controlflag

| Bit | Beschreibung |
| --------- | -------------------------------------------------------------------- |
| 22-31 | Reserviert, nicht verändern |
| 21 | ID - ID Flag (X) |
| 20 | VIP - **V**irtual **I**nterrupt **P**ending (X) |
| 19 | VIF - **V**irtual **I**nterrupt **F**lag (X) |
| 18 | AC - **A**lignment **C**heck (X) |
| 17 | VM - **V**irtual 8086 **M**ode (X) |
| 16 | RF - **R**esume **F**lag (X) |
| 15 | Reserviert, nicht ändern |
| 14 | NT - **N**ested **T**ask Flag (X) |
| 13 - 12 | IOPL - **I**/**O** **P**rivilege **L**evel (X) |
| 11 | [OF - **O**verflow **F**lag](#of---overflow-flag-bit-11) (S) |
| 10 | \[\[#DF - Direction Flag (Bit 10)\|DF - **D**irection **F**lag (C) |
| 9 | IF - **I**nterrupt **E**nable Flag (X) |
| 8 | TF - **T**rap **F**lag (X) |
| 7 | [SF - **S**ign **F**lag](#sf---sign-flag-bit-7) (S) |
| 6 | [ZF - **Z**ero **F**lag](#zf---zero-flag-bit-6) (S) |
| 5 | Reserviert, nicht ändern |
| 4 | [AF - **A**uxiliary Carry **F**lag](#af---adjust-flag-bit-4) (S) |
| 3 | Reserviert, nicht ändern |
| 2 | [PF - **P**arity **F**lag](#pf---parity-flag-bit-2) (S) |
| 1 | Reserviert, nicht ändern |
| 0 | [CF - **C**arry **F**lag](#cf---carry-flag-bit-0) (S) |

  

### Statusflags

Die Statusflags (Bits 0,2,4,6,7,11) geben das Ergebnis einer Arithmetischen Operation an (z. B.: ADD, SUB, MUL, DIV). Verwendet werden sie normalerweise in Verbindung mit bedingten Sprüngen, sets, movs, und loops (Jcc, SETcc, MOVcc, LOOPcc; cc = conditional code).

#### CF - Carry Flag (Bit 0)

Zeigt einen Overflow bei unsigned-Arithmetik an

#### PF - Parity Flag (Bit 2)

Gesetzt wenn das niederwertige Byte des Ergebnisses eine gerade Anzahl an 1er Bits enthält.

#### AF - Adjust Flag (Bit 4)

Gesetzt wenn ein Übertrag von Bit 3 stattgefunden hat.  
Wird hauptsächlich für [BCD](https://github.com/lowlevel-eu/wiki/wiki/Binary-Coded-Decimal "BCD") Berechnungen verwendet.

#### ZF - Zero Flag (Bit 6)

Gesetzt wenn das Ergebnis 0 ist.

#### SF - Sign Flag (Bit 7)

Entspricht dem höherwertigsten Bit des Ergebnisses, also dem Vorzeichenbit bei signed-Berechnungen.  
0 steht für einen positiven Wert und 1 für einen negativen.

#### OF - Overflow Flag (Bit 11)

Gesetzt wenn ein Overflow bei einer signed-Zahl stattgefunden hat.

  

### Controlflags

#### DF - Direction Flag (Bit 10)

Gibt die Richtung bei Stringoperationen an.  
Wenn 0 wird der Zeiger inkrementiert, bei 1 dekrementiert.  

### Systemflags

  

## Befehle zum direkten Verändern

- PUSHF
- PUSHFD
- POPF
- POPFD
- LAHF
- SAHF

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/3461/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1751/index.html)

<!-- MediaWiki page 1751; revision 3461; parent 3460; 2008-11-02T18:51:12Z -->
