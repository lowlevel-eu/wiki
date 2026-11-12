# EFLAGS

Das EFLAGS (Programmstatus und Kontrollregister) Register ist 32 Bit groß, wobei jedes Bit ein Flag repräsentiert. Es beinhaltet Status-Informationen über das laufende Programm und erlaubt anwendungsbasierte Prozessorkontrolle. Das Register kann nicht komplett verändert werden, es können nur die einzelnen Flags gesetzt oder gelöscht werden, meistens auch nur indirekt, in der Form das ein aufgerufener Befehl ein Flag als Nebeneffekt ändert.

**EFLAGS-Register**

| Bit | Beschreibung |
| --------- | ------------------------------------------------------------------------------------------------- |
| 22-31 | Reserviert, nicht verändern |
| 21 | [ID - ID Flag](#id---identification-flag-bit-21) (X) |
| 20 | [VIP - **V**irtual **I**nterrupt **P**ending](#vip---virtual-interrupt-pending-flag-bit-20) (X) |
| 19 | [VIF - **V**irtual **I**nterrupt **F**lag](#vif---virtual-interrupt-flag-bit-19) (X) |
| 18 | [AC - **A**lignment **C**heck](#ac---alignment-check-flag-bit-18) (X) |
| 17 | [VM - **V**irtual 8086 **M**ode](#) (X) |
| 16 | [RF - **R**esume **F**lag](#rf---resume-flag-bit-16) (X) |
| 15 | Reserviert, nicht ändern |
| 14 | [NT - **N**ested **T**ask Flag](#nt---nested-task-flag-bit-14) (X) |
| 13 - 12 | [IOPL - **I**/**O** **P**rivilege **L**evel](#iopl---io-privilege-field-bits-12-und-13) (X) |
| 11 | [OF - **O**verflow **F**lag](#of---overflow-flag-bit-11) (S) |
| 10 | [DF - **D**irection **F**lag](#df---direction-flag-bit-10) (C) |
| 9 | [IF - **I**nterrupt **E**nable Flag](#if---interrupt-enable-flag-bit-9) (X) |
| 8 | [TF - **T**rap **F**lag](#tf---trap-flag-bit-8) (X) |
| 7 | [SF - **S**ign **F**lag](#sf---sign-flag-bit-7) (S) |
| 6 | [ZF - **Z**ero **F**lag](#zf---zero-flag-bit-6) (S) |
| 5 | Reserviert, nicht ändern |
| 4 | [AF - **A**uxiliary Carry **F**lag](#af---auxiliary-carry-flag-bit-4) (S) |
| 3 | Reserviert, nicht ändern |
| 2 | [PF - **P**arity **F**lag](#pf---parity-flag-bit-2) (S) |
| 1 | Reserviert, nicht ändern |
| 0 | [CF - **C**arry **F**lag](#cf---carry-flag-bit-0) (S) |

*(X) Systemflag, (S) Statusflag, (C) Controlflag*

### Statusflags

Die Statusflags (Bits 0, 2, 4, 6, 7, 11) geben das Ergebnis einer arithmetischen Operation an (z. B.: ADD, SUB, MUL, DIV). Verwendet werden sie normalerweise in Verbindung mit bedingten Sprüngen, sets, movs und loops (Jcc, SETcc, MOVcc, LOOPcc; cc = conditional code).

#### CF - Carry Flag (Bit 0)

Zeigt einen Overflow bei vorzeichenlosen Berechnungen an.

#### PF - Parity Flag (Bit 2)

Gesetzt, wenn das niederwertige Byte des Ergebnisses eine gerade Anzahl an gesetzten Bits enthält.

#### AF - Auxiliary Carry Flag (Bit 4)

Gesetzt, wenn ein Übertrag von Bit 3 auf Bit 4 stattgefunden hat.  
Wird hauptsächlich für [BCD](Binary-Coded-Decimal "BCD")-Berechnungen verwendet.

#### ZF - Zero Flag (Bit 6)

Gesetzt, wenn das Ergebnis 0 ist.

#### SF - Sign Flag (Bit 7)

Entspricht dem höchstwertigen Bit des Ergebnisses, also dem Vorzeichenbit bei vorzeichenbehafteten Berechnungen.  
0 steht für einen positiven Wert und 1 für einen negativen.

#### OF - Overflow Flag (Bit 11)

Gesetzt, wenn ein Overflow bei einer signed-Zahl stattgefunden hat.

### Controlflags

#### DF - Direction Flag (Bit 10)

Gibt die Richtung bei Stringoperationen an. Wenn 0 wird der Zeiger inkrementiert, bei 1 dekrementiert.  
Dieses Flag kann mit **CLD** (Clear Direction Flag) und **STD** (Set Direction Flag) verändert werden.

### Systemflags

#### TF - Trap Flag (Bit 8)

Für schrittweises Debuggen.

#### IF - Interrupt Enable Flag (Bit 9)

Wenn es gesetzt ist, dann wird auf Interrupts reagiert, ist es gelöscht, so werden diese ignoriert (Ausnahme: [Non Maskable Interrupt](Non-Maskable-Interrupt "Non Maskable Interrupt")).  
Kann mit **CLI** (Clear Interruptflag) und **STI** (Set Interruptflag) geändert werden.

#### IOPL - I/O Privilege Field (Bits 12 und 13)

Gibt an, ab welcher Privilegstufe alle I/O-Ports (und nicht nur per I/O-Port-Bitmap ausgewählte) benutzt werden dürfen.

#### NT - Nested Task Flag (Bit 14)

Gesetzt, wenn der akuelle Task eine Verbindung zum vorherigen hat.

#### RF - Resume Flag (Bit 16)

Steuert die Reaktion des Prozessors auf eine Debug Exception.

#### VM - Virtual 8086 Mode Flag (Bit 17)

Gesetzt, um im [Virtual 8086 Mode](Virtual-8086-Mode "Virtual 8086 Mode") zu arbeiten.

#### AC - Alignment Check Flag (Bit 18)

Wenn dieses Flag und das AM-Bit im [CR0-Register](Control-Register "Control Register") gesetzt ist, wird auf Speicherausrichtung geprüft.

#### VIF - Virtual Interrupt Flag (Bit 19)

Das Interruptflag für den Virtual 8086 Mode.

#### VIP - Virtual Interrupt Pending Flag (Bit 20)

Gesetzt, um anzuzeigen, dass ein Interrupt abgearbeitet werden muss (Das Betriebssystem setzt und löscht dieses Flag, der Prozessor liest es nur). Genutzt wird es in Verbindung mit dem Virtual Interrupt Flag.

#### ID - Identification Flag (Bit 21)

Wenn dieses Bit von Software verändert werden kann, dann unterstützt der Prozessor den [CPUID](CPUID "CPUID")-Befehl.

## Befehle zum direkten Verändern

- PUSHF
- PUSHFD
- POPF
- POPFD
- LAHF
- SAHF

## RFLAGS

Das RFLAGS Register ist die 64-Bit Variante von EFLAGS. Allerdings hat sich abgesehen von der Tatsache, dass das Register jetzt 64 Bit breit ist, nichts geändert. Die Bits 32-63 sind reserviert und geben immer 0 zurück.

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/7163/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1751/index.html)

<!-- MediaWiki page 1751; revision 7163; parent 6011; 2010-02-23T20:13:23Z -->
