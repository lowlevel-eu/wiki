# Control Register

Die Control Register sind spezielle Register der [IA-32](X86.md "IA-32") und [AMD64](X86-64.md "AMD64") Architekturen, die den Betriebsmodus und einige Eigenschaften der CPU festlegen. In der AMD64-Architektur haben sie eine Breite von 64 Bit, wobei die unteren 32 Bit, den der IA-32 Architektur entsprechen. Der Zugriff auf diese Register ist wie bei den Segmentregistern auch nur mit einem Umweg über Allzweckregister möglich.

## CR0

**63-32**

*Reserviert*

| 31 | 30 | 29 | 28-19 | 18 | 17 | 16 | 15-6 | 5 | 4 | 3 | 2 | 1 | 0 |
| ----- | ----- | ----- | -------------- | ----- | ----- | ----- | -------------- | ----- | ----- | ----- | ----- | ----- | ----- |
| PG | CD | NW | *Reserviert* | AM |  | WP | *Reserviert* | NE | ET | TS | EM | MP | PE |

- PE - *Protection Enbale* Flag schaltet den [Protected Mode](Protected-Mode.md "Protected Mode") ein bzw. aus (Genaueres siehe [hier](Umschalten-in-Protected-Mode.md "Umschalten in Protected Mode"))
- MP - Mit dem *Monitor Coprocessor* Flag kann festgelegt werden, ob bei gesetztem TS-Flag der Aufruf von WAIT/FWAIT eine Exception auslöst oder nicht (bei gesetztem MP-Flag wird die Exception ausgelöst).
- EM - Bei gesetztem *Emulation* Flag löst die CPU für jede [FPU](Mathematischer-Koprozessor.md "FPU")-Instruktion eine [\#NM-Exception](Exception.md "Exception") aus. Für Multimedia-Instruktionen wird eine [\#UD-Exception](Exception.md "Exception") ausgelöst. Damit wird es dem Betriebssystem ermöglicht eine FPU zu emulieren. (WAIT/FWAIT lösen keine Exception aus)
- TS - Das *Task Switched* Flag wird bei einem [Hardware-Taskswitch](Multitasking.md "Multitasking") von der CPU gesetzt und kann für Software Multitasking auch von Hand gesetzt werden. Wenn bei gesetztem TS-Flage versucht wird eine FPU- oder Multimedia-Instruktion auszuführen, dann löst die CPU eine \#NM-Exception aus. Dadurch können die FPU- bzw. Multimedia-Register, die bei normalen Taskswitchs nicht beachtet werden, entsprechend gesichert und geladen werden bevor sie verwendet werden.
- ET - *Extension Type*
- NE - *Numeric Error* aktiviert die interne Signalisierung von FPU-Ausnahmen als [\#MF-Exception](Exception.md "Exception"). Andernfalls werden die Ausnahmen über den [PIC](Programmable-Interrupt-Controller.md "Programmable Interrupt Controller") als IRQ 13 signalisiert (inkompatibel mit [I/O-APIC](I-O-Advanced-Programmable-Interrupt-Controller.md "I/O APIC") und birgt die Gefahr von Race-Conditions). Dies ist ab dem 80486 möglich.
- WP - Mittels *Write Protect* Flag kann festgelegt werden ob schreibgeschützte Pages auch vor dem Kernel (Ring0) geschützt sind (bei gesetztem WP-Flag sind die Pages auch vor dem Kernel sicher).
- AM - *Alignment Mask*
- NW - Im Long Mode löst das Setzen des *Not Write-throgh Disable* eine [\#GP-Exception](Exception.md "Exception") aus (außer wenn Caching mittels CD-Flag ganz abgeschaltet ist). Im Legacy Mode wird mit gesetztem Flag Writethroug-Caching erzwungen, unabhängig vom PWT-Flag in den Paging Strukturen.
- CD - Das *Cache Disable* Flag steuert das Caching der CPU. Mit dem Setzten dieses Flags wird das Caching der CPU abgeschaltet und die den Cache betreffenden Flags in möglichen Paging-Strukturen werden ignoriert.
- PG - Mit dem *Paging* Flag kann der [Paging-Mechanismus](Paging.md "Paging") ein- bzw. ausgeschaltet werden.

## CR2

Bevor die CPU eine [Page-Fault-Exception](Exception.md "Exception") auslöst, lädt sie die virtuelle Adresse, die den Fehler verursacht hat, in das CR2 Register.

## CR3

Das CR3-Register enthält primär die Adresse des Page Directories, sowie 2 Flags, die das interne Caching innerhalb der CPU (nicht im TLB) steuern. Wenn [Physical Address Extension](Physical-Address-Extension.md "Physical Address Extension") (PAE) aktiviert ist, wird die Adresse des Page Directories ersetzt durch die um 7 Bits größere Adresse zur Page-Directory Pointer Table.

| Bit | Funktion | Funktion mit aktivierter [PAE](Physical-Address-Extension.md "PAE") |
| ----------- | ----------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| Bit 0-2 | *Reserviert* |  |
| Bit 3 | **PWT** *Page-level Writes Transparant* |  |
| Bit 4 | **PCD** *Page-level Cache Disable* |  |
| Bit 5-11 | *Reserviert* | **Page-Directory-Pointer-Table Base** Basis-Adresse der PDPT<br> |
| Bit 12-31 | **Page-Directory Base** Basis Adresse des Page-Directorys | **Page-Directory-Pointer-Table Base** Basis-Adresse der PDPT<br> |

## CR4

**63-32**

*Reserviert*

| 31-11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| -------------- | ------------ | -------- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| *Reserviert* | OSXMMEXCPT | OSFXSR | PCE | PGE | MCE | PAE | PSE | DE | TSD | PVI | VME |

- VME - *Virtual-8086 Mode Extension*
- PVI - *Protected-Mode Virtual Interrupts*
- TSD - *Time-Stamp Disable*
- DE - *Debugging Extension*
- PSE - *Page-Size Extension* (Wird im Long Mode ignoriert)
- PAE - Das Flag schaltet *Physical-Address Extension* ein bzw. aus. (Genaueres siehe [hier](Physical-Address-Extension.md "Physical Address Extension")) (MUSS im Long Mode gesetzt sein)
- MCE - *Machine-Check Enable*
- PGE - Mit dem *Page-Global Enable* Flag kann die Unterstützung des Global-Flags in den [Paging](Paging.md "Paging") Strukturen ein bzw. aus geschaltet werden.
- PCE - Ein gesetztes *Performance-Monitoring Counter Enable* Flag erlaubt die Verwendung der RDPMC-Instruktion auch aus Ring 3-1. Ist das Flag 0, ist die Verwendung nur aus Ring 0 gestattet.
- OSFXSR - Mit dem Setzen des *FXSAVE/FXRSTORE Support* Flags versichert das Betriebssystem, dass es (mittels FXSAVE/FXRSTOR) zum Beispiel bei Taskswitches den Prozessorstatus für FPU- und Multimedia-Instruktionen sichert und wiederherstellt. Ohne diese „Versicherung“ ist die Unterstützung dieser Befehle von seiten der CPU deaktiviert, d.h. die CPU löst für jede dieser Instruktionen (mit Ausnahme der FXSAVE bzw. FXRSTORE Instruktionen) eine [\#UD-Exception](Exception.md "Exception") aus.
- OSXMMEXCPT - Das *Unmasked Exception Support* Flag muss vom Betriebssystem gesetzt werden, wenn es einen Handler für [\#XF-Exceptions](Exception.md "Exception") bereit stellt. Ist das nicht der Fall wird beim auftreten einer *«unmasked SIMD floating-point exception»* statt dessen eine \#UD-Exception ausgelöst.

## CR8

| Bit | Funktion |
| ---------- | ------------------------------- |
| Bit 0-3 | **TPL** *Task Priority Level* |
| Bit 3-31 | *n/a* |

## CR1, CR5-CR7 und CR9-CR15

Die Register CR1, CR5-CR7 und CR9-CR15 sind reserviert. Versucht Software dennoch darauf zuzugreifen löst die CPU eine [\#UD-Exception](Exception.md "Exception") aus.

## Weblinks

- [Intel® 64 and IA-32 Architectures Software Developer's Manual Volume 3A: System Programming Guide](http://www.intel.com/products/processor/manuals/index.htm) (Kapitel 2.5)
- [AMD64 Architecture Programmer's Manual Volume 2: System Programming](http://developer.amd.com/documentation/guides/Pages/default.aspx#Manuals)(Kapitel 3.1)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/11355/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1610/index.html)

<!-- MediaWiki page 1610; revision 11355; parent 10029; 2016-08-02T11:30:09Z -->
