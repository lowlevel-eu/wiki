# Control Register

Die Control Register sind spezielle Register der Intel Architektur (x86 und x86-64), die den Betriebsmodus und einige Eigenschaften der CPU festlegen.

## CR0

| Bit | Funktion |
| ----------- | -------------------------------------------------------------------- |
| Bit 0 | **PE** *Protection Enable* Schaltet den Protected-Mode Ein/Aus<br> |
| Bit 1 | **MP** *Monitor Coprocessor* |
| Bit 2 | **EM** *Emulation* |
| Bit 3 | **TS** *Task Switched* |
| Bit 4 | **ET** *Extension Type* |
| Bit 5 | **NE** *Numeric Error* |
| Bit 6-15 | *Reserviert* |
| Bit 16 | **WP** *Write Protect* |
| Bit 17 | *Reserviert* |
| Bit 18 | **AM** *Alignment Mask* |
| Bit 19-28 | *Reserviert* |
| Bit 29 | **NW** *Not Write-throgh* |
| Bit 30 | **CD** *Cache Disable* |
| Bit 31 | **PG** *Paging* Schaltet den Paging-Meschanismus Ein/Aus<br> |

## CR1

*Reserviert*

## CR2

Enthält noch einem Page-Fault die lineare Adresse, die den Fehler verursacht hat.

## CR3

Das CR3-Register enthält primär die Adresse des Page Directorys, sowie 2 Flags, die das interne Caching innerhalb der CPU (nicht im TLB) steuern. Wenn [Physical Address Extension](https://github.com/lowlevel-eu/wiki/wiki/Physical-Address-Extension "Physical Address Extension") (PAE) aktiviert ist, wird die Adresse des Page Directorys ersetzt durch die um 7 Bits größere Adresse zur Page-Directory Pointer Table.

| Bit | Funktion | Funktion mit aktivierter [PAE](https://github.com/lowlevel-eu/wiki/wiki/Physical-Address-Extension "PAE") |
| ----------- | --------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| Bit 0-2 | *Reserviert* |  |
| Bit 3 | **PWT** *Page-level Writes Transparant* |  |
| Bit 4 | **PCD** *Page-level Cache Disable* |  |
| Bit 5-11 | *Reserviert* | **Page-Directory-Pointer-Table Base** Basis-Adresse der PDPT<br> |
| Bit 12-31 | **Page-Directory Base** Basis Adresse des Page-Directorys<br> | **Page-Directory-Pointer-Table Base** Basis-Adresse der PDPT<br> |

## CR4

| Bit | Funktion |
| ----------- | ----------------------------------------------------------------------- |
| Bit 0 | **VME** *Virtual 8086 Mode Extension* |
| Bit 1 | **PVI** *Protected Mode Virtual Interrupt* |
| Bit 2 | **TSD** *Time Stamp Disable* |
| Bit 3 | **DE** *Debugging Extension* |
| Bit 4 | **PSE** *Page Size Extension* |
| Bit 5 | **PAE** *Physical Address Extension* |
| Bit 6 | **MCE** *Machine Check Enable* |
| Bit 7 | **PGE** *Page Global Enable* |
| Bit 8 | **PCE** *Performance Monitoring Counter Enable* |
| Bit 9 | **OSFXSR** *Operating System Support for FXSAVE and FXSTOR* |
| Bit 10 | **OSXMMEXCPT** *Operating System Support for Unmasked SIMD Exception* |
| Bit 11-31 | *Reserviert* |

## CR8

| Bit | Funktion |
| ---------- | ------------------------------- |
| Bit 0-3 | **TPL** *Task Priority Level* |
| Bit 3-31 | *n/a* |

## Weblinks

- [Intel® 64 and IA-32 Architectures Software Developer's Manual Volume 3A: System Programming Guide](http://www.intel.com/products/processor/manuals/index.htm) (Kapitel 2.5)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/4469/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1610/index.html)

<!-- MediaWiki page 1610; revision 4469; parent 4345; 2009-06-21T22:29:45Z -->
