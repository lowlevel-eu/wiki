# EFLAGS

Das EFLAGS (Programmstatus und Kontrollregister) Register ist 32 Bit groß, wobei jedes Bit ein Flag repräsentiert. Es beinhaltet Status-Informationen über das laufende Programm und erlaubt anwendungsbasierte Prozessorkontrolle. Das Register kann nicht komplett verändert werden, es können nur die einzelnen Flags gesetzt oder gelöscht werden, meistens auch nur indirekt, in der Form das ein aufgerufener Befehl ein Flag als nebeneffekt ändert.

## Aufbau des EFLAGS-Registers

Im folgenden steht (X) für Systemflag, (S) für Statusflag und (C) für Controlflag

| Bit | Beschreibung |
| --------- | ------------------------------------------------- |
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
| 11 | OF - **O**verflow **F**lag (S) |
| 10 | DF - **D**irection **F**lag (C) |
| 9 | IF - **I**nterrupt **E**nable Flag (X) |
| 8 | TF - **T**rap **F**lag (X) |
| 7 | SF - **S**ign **F**lag (S) |
| 6 | ZF - **Z**ero **F**lag (S) |
| 5 | Reserviert, nicht ändern |
| 4 | AF - **A**uxiliary Carry **F**lag (S) |
| 3 | Reserviert, nicht ändern |
| 2 | PF - **P**arity **F**lag (S) |
| 1 | Reserviert, nicht ändern |
| 0 | CF - **C**arry **F**lag (S) |

### Statusflags

### Controlflags

### Systemflags

## Befehle zum direkten Verändern

- PUSHF
- PUSHFD
- POPF
- POPFD
- LAHF
- SAHF

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/3455/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1751/index.html)

<!-- MediaWiki page 1751; revision 3455; parent 3454; 2008-11-02T12:54:58Z -->
