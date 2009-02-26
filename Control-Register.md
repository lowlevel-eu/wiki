# Control Register

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

| Bit | Funktion |
| ----------- | --------------------------------------------------------------- |
| Bit 0-2 | *Reserviert* |
| Bit 3 | **PWT** *Page-level Writes Transparant* |
| Bit 4 | **PCD** *Page-level Cache Disable* |
| Bit 5-11 | *Reserviert* |
| Bit 12-31 | **Page-Directory Base** Basis Adresse des Page-Directorys<br> |

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

## Weblinks

- [Intel® 64 and IA-32 Architectures Software Developer's Manual Volume 3A: System Programming Guide](http://www.intel.com/products/processor/manuals/index.htm) (Kapitel 2.5)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/4061/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1610/index.html)

<!-- MediaWiki page 1610; revision 4061; parent 3833; 2009-02-26T18:51:51Z -->
