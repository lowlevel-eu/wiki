# Control Register

Die Control Register sind spezielle Register der [IA-32](https://github.com/lowlevel-eu/wiki/wiki/X86 "IA-32") und [AMD64](https://github.com/lowlevel-eu/wiki/wiki/X86-64 "AMD64") Architekturen, die den Betriebsmodus und einige Eigenschaften der CPU festlegen. In der AMD64-Architektur haben sie eine Breite von 64 Bit, wobei die unteren 32 Bit, den der IA-32 Architektur entsprechen. Der Zugriff auf diese Register ist wie bei den Segment Registern auch nur mit einem Umweg über Allzweckregister möglich.

## CR0

**63-32**

*Reserviert*

| 31 | 30 | 29 | 28-19 | 18 | 17 | 16 | 15-6 | 5 | 4 | 3 | 2 | 1 | 0 |
| ----- | ----- | ----- | -------------- | ----- | ----- | ----- | -------------- | ----- | ----- | ----- | ----- | ----- | ----- |
| PG | CD | NW | *Reserviert* | AW |  | WP | *Reserviert* | NE | ET | TS | EM | MP | PE |

- PE - *Protection Enbale* Flag schaltet den [Protected Mode](https://github.com/lowlevel-eu/wiki/wiki/Protected-Mode "Protected Mode") ein bzw. aus (Genaueres siehe [hier](https://github.com/lowlevel-eu/wiki/wiki/Umschalten-in-Protected-Mode "Umschalten in Protected Mode"))
- MP - Mit dem *Monitor Coprocessor* Flag kann festgelegt werden ob bei Gesetztem TS-Flag der Aufruf von WAIT/FWAIT einen Exception auslösen oder nicht (bei gesetztem MP-Flag wird die Exception ausgelöst).
- EM - Bei gesetztem *Emulation* Flag löst die CPU für jede [FPU](https://github.com/lowlevel-eu/wiki/wiki/Mathematischer-Koprozessor "FPU")-Instruktion eine [\#NM-Exception](https://github.com/lowlevel-eu/wiki/wiki/Exception "Exception") aus. Für Multimedia-Instruktionen wird eine [\#UD-Exception](https://github.com/lowlevel-eu/wiki/wiki/Exception "Exception") ausgelöst. Damit wird es dem Betriebssystem ermöglicht eine FPU zu emulieren. (WAIT/FWAIT lösen keine Exception aus)
- TS - Das *Task Switched* Flag wird bei einem [Hardware-Taskswitch](https://github.com/lowlevel-eu/wiki/wiki/Multitasking "Multitasking") von der CPU gesetzt und kann für Software Multitasking auch von Hand gesetzt werden. Wenn bei gesetztem TS-Flage versucht wird eine FPU- oder Multimedia-Instruktion auszuführen, dann löst die CPU eine \#NM-Exception aus. Dadurch können die FPU- bzw. Multimedia-Register, die bei normalen Taskswitchs nicht beachtet werden, entsprechend gesichert und geladen werden bevor sie verwendet werden.
- ET - *Extension Type*
- NE - *Numeric Error*
- WP - *Write Protect*
- AM - *Alignment Mask*
- NW - *Not Write-throgh*
- CD - *Cache Disable*
- PG - *Paging* schaltet den Paging-Meschanismus Ein/Aus

## CR2

Bevor die CPU eine [Page-Falut Exception](https://github.com/lowlevel-eu/wiki/wiki/Exception "Exception") auslöst, lädt sie die virtuelle Adresse, die den Fehler verursacht hat, in das CR2 Register.

## CR3

Das CR3-Register enthält primär die Adresse des Page Directories, sowie 2 Flags, die das interne Caching innerhalb der CPU (nicht im TLB) steuern. Wenn [Physical Address Extension](https://github.com/lowlevel-eu/wiki/wiki/Physical-Address-Extension "Physical Address Extension") (PAE) aktiviert ist, wird die Adresse des Page Directories ersetzt durch die um 7 Bits größere Adresse zur Page-Directory Pointer Table.

| Bit | Funktion | Funktion mit aktivierter [PAE](https://github.com/lowlevel-eu/wiki/wiki/Physical-Address-Extension "PAE") |
| ----------- | ----------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| Bit 0-2 | *Reserviert* |  |
| Bit 3 | **PWT** *Page-level Writes Transparant* |  |
| Bit 4 | **PCD** *Page-level Cache Disable* |  |
| Bit 5-11 | *Reserviert* | **Page-Directory-Pointer-Table Base** Basis-Adresse der PDPT<br> |
| Bit 12-31 | **Page-Directory Base** Basis Adresse des Page-Directorys | **Page-Directory-Pointer-Table Base** Basis-Adresse der PDPT<br> |

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

## CR1, CR5-CR7 und CR9-CR15

Die Register CR1, CR5-CR7 und CR9-CR15 sind reserviert. Versucht Software dennoch darauf zuzugreifen löst die CPU eine [\#UD-Exception](https://github.com/lowlevel-eu/wiki/wiki/Exception "Exception") aus.

## Weblinks

- [Intel® 64 and IA-32 Architectures Software Developer's Manual Volume 3A: System Programming Guide](http://www.intel.com/products/processor/manuals/index.htm) (Kapitel 2.5)
- [AMD64 Architecture Programmer's Manual Volume 2: System Programming](http://developer.amd.com/documentation/guides/Pages/default.aspx#Manuals)(Kapitel 3.1)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/4515/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1610/index.html)

<!-- MediaWiki page 1610; revision 4515; parent 4513; 2009-06-29T17:13:39Z -->
