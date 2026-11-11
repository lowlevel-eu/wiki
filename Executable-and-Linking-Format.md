# Executable and Linking Format

Das Executable and Linking Format (kurz ELF) ist ein Dateiformat für ausführbare Dateien. Es gibt 3 verschiedene Arten von ELF-Dateien:

- executable
- relocatable
- shared object

## Aufbau

### ELF-Header

Der ELF-Header ist wie folgt aufgebaut.

| Name | Offset | Größe | Beschreibung |
| ----------------------------- | -------- | ------- | ------------------------------------------------------------------- |
| [e_ident](#e_ident) | 0x00 | 16 | Enthält Daten zur Identifikation |
| [e_type](#e_type) | 0x10 | 2 | Enthält den ELF-Typ |
| [e_machine](#e_machine) | 0x12 | 2 | Beschreibt die benötigte Architektur |
| [e_version](#e_version) | 0x14 | 4 | Version |
| [e_entry](#e_entry) | 0x18 | 4 | Entrypoint |
| [e_phoff](#e_phoff) | 0x1C | 4 | Das Offset des Programm-Headers |
| [e_shoff](#e_shoff) | 0x20 | 4 | Das Offset des Section-Headers |
| [e_flags](#e_flags) | 0x24 | 4 | Verschiedene Flags |
| [e_ehsize](#e_ehsize) | 0x28 | 2 | Größe des ELF-Headers |
| [e_phentsize](#e_phentsize) | 0x2A | 2 | Größe eines Eintrags im Programm-Header |
| [e_phnum](#e_phnum) | 0x2C | 2 | Anzahl an Einträgen im Programm-Header |
| [e_shentsize](#e_shentsize) | 0x2E | 2 | Größe eines Eintrags im Section-Header |
| [e_shnum](#e_shnum) | 0x30 | 2 | Anzahl an Einträgen im Section-Header |
| [e_shstrndex](#e_shstrndx) | 0x32 | 2 | Assoziiert einen Eintrag im Section-Header mit der String-Tabelle |

#### e_ident

Das Feld e_ident ist 16 Byte groß und enthält Werte zur Identifikation der ELF-Datei. Dies sind die Indizes:

| Name | Wert | Beschreibung |
| --------------------------------- | ------ | ------------------------------------- |
| [EI_MAG0](#ei_mag0-bis-ei_mag3) | 0 | Datei-Identifikation |
| [EI_MAG1](#ei_mag0-bis-ei_mag3) | 1 | Datei-Identifikation |
| [EI_MAG2](#ei_mag0-bis-ei_mag3) | 2 | Datei-Identifikation |
| [EI_MAG3](#ei_mag0-bis-ei_mag3) | 3 | Datei-Identifikation |
| [EI_CLASS](#ei_class) | 4 | Datei-Klasse |
| [EI_DATA](#ei_data) | 5 | Prozessorspezifische Datenkodierung |
| [EI_VERSION](#ei_version) | 6 | Datei-Version |
| [EI_PAD](#ei_pad) | 7 | Letztes genutztes Byte in e_ident |
| EI_NIDENT | 16 | Anzahl an Bytes in e_ident |

##### EI_MAG0 bis EI_MAG3

Diese Bytes werden zur Datei-Identifikation benutzt.

| Name | Wert | Position |
| --------- | ------ | -------------------- |
| ELFMAG0 | 0x7f | e_ident\[EI_MAG0\] |
| ELFMAG1 | 'E' | e_ident\[EI_MAG1\] |
| ELFMAG2 | 'L' | e_ident\[EI_MAG2\] |
| ELFMAG3 | 'F' | e_ident\[EI_MAG3\] |

##### EI_CLASS

Die Klasse gibt unter anderen an, wie viel Bits zur Adressierung verwendet werden. Also eine 32-Bit-Maschine sollte überprüfen, ob der Code auch wirklich auf 32-Bit-Maschinen geht.

| Name | Wert | Beschreibung |
| -------------- | ------ | ------------------ |
| ELFCLASSNONE | 0 | Ungültige Klasse |
| ELFCLASS32 | 1 | 32-Bit-Objekte |
| ELFCLASS64 | 2 | 64-Bit-Objekte |

##### EI_DATA

Das Byte e_ident\[EI_DATA\] gibt an, in welchen Format Daten gespeichert werden, Little-Endian oder Big-Endian.

| Name | Wert | Beschreibung |
| ------------- | ------ | --------------- |
| ELFDATANONE | 0 | Ungültig |
| ELFDATA2LSB | 1 | Little-Endian |
| ELFDATA2MSB | 2 | Big-Endian |

##### EI_VERSION

Hier sollte das gleiche wie in e_version drinstehen, also EV_CURRENT.

##### EI_PAD

Alle Bytes in e_ident ab EI_PAD (inklusive) werden nicht benutzt und sollten auf Null gesetzt sein.

##### Architektur-Identifikation

Für einen [x86](X86 "X86")-Prozessor sollten folgende Felder folgende Werte haben:

| Feld | Wert |
| --------------------- | ------------- |
| e_ident\[EI_CLASS\] | ELFCLASS32 |
| e_ident\[EI_DATA\] | ELFDATA2LSB |
| e_machine | EM_386 |

#### e_type

Dieses Feld beschreibt, welches ELF-Format benutzt wird:

| Name | Wert | Beschreibung |
| ----------- | -------- | --------------------- |
| ET_NONE | 0 | Kein Typ |
| ET_REL | 1 | Relocatable Datei |
| ET_EXEC | 2 | Ausführbare Datei |
| ET_DYN | 3 | Shared-Object-Datei |
| ET_CORE | 4 | Kerndatei |
| ET_LOPROC | 0xff00 | Prozessorspezifisch |
| ET_HIPROC | 0xffff | Prozessorspezifisch |

Für eine ausführbare ELF-Datei müsste hier ET_EXEC stehen.

#### e_machine

Wie oben bereits erwähnt, enthält dieses Element den Prozessor-Typ.

| Name | Wert | Beschreibung |
| ----------- | ------ | ---------------- |
| EM_NONE | 0 | Kein Typ |
| EM_M32 | 1 | AT&T WE 32100 |
| EM_SPARC | 2 | SPARC |
| EM_386 | 3 | Intel 80386 |
| EM_68K | 4 | Motorola 68000 |
| EM_88K | 5 | Motorola 88000 |
| EM_860 | 7 | Intel 80860 |
| EM_MIPS | 8 | MIPS RS3000 |
| EM_X86_64 | 62 | AMD64 |

#### e_version

Beschreibt die ELF-Version der Datei.

| Name | Wert | Beschreibung |
| ------------ | ------ | ------------------- |
| EV_NONE | 0 | Ungültige Version |
| EV_CURRENT | 1 | Aktuelle Version |

#### e_entry

Virtuelle Adresse des Entrypoints

#### e_phoff

Offset in der Datei, an dem die Programm-Header steht. Wenn die Datei keinen Programm-Header enthält, steht hier 0.

#### e_shoff

Offset in der Datei, an dem der Section-Header steht. Wenn die Datei keinen Section-Header enthält, steht hier 0.

#### e_flags

Dieses Feld enthält prozessorspezifische Flags.

#### e_ehsize

Größe des ELF-Headers.

#### e_phentsize

Dieses Feld gibt an, wie groß ein Eintrag im Programm-Header ist.

#### e_phnum

Gibt an, wie viele Einträge im Programm-Header enthalten sind. Das Produkt von e_phentsize und e_phnum ergibt die insgesamte Größe des Programm-Headers. Wenn die Datei keinen Programm-Header hat, steht hier 0.

#### e_shentsize

Dieses Feld gibt an, wie groß ein Eintrag im Section-Header ist.

#### e_shnum

Gibt an, wie viele Einträge im Section-Header enthalten sind. Das Produkt von e_shentsize und e_shnum ergibt die insgesamte Größe des Section-Headers. Wenn die Datei keinen Section-Header hat, steht hier 0.

#### e_shstrndx

Gibt an, welcher Eintrag im Section-Header mit der String-Tabelle verknüpft wird.

### Programm-Header

Der Programm-Header besteht aus e_phnum Einträgen, wobei jeder e_phentsize groß ist. Der Programm-Header ist also insgesamt e_phnum\*e_phentsize Bytes groß. Im Programm-Header stehen z. B. der Text- oder Daten-Teil eines Programms. Ein Eintrag im Programm-Header ist wie folgt aufgebaut:

| Name | Offset | Größe | Beschreibung |
| ----------------------- | -------- | ------- | ----------------------------------------------------------- |
| [p_type](#p_type) | 0x00 | 4 | Typ des Segments |
| [p_offset](#p_offset) | 0x04 | 4 | Dateioffset, an dem das Segment steht |
| [p_vaddr](#p_vaddr) | 0x08 | 4 | Virtuelle Adresse, an die das Segment kopiert werden soll |
| [p_paddr](#p_paddr) | 0x0C | 4 | Physische Adresse (meist irrelevant) |
| [p_filesz](#p_filesz) | 0x10 | 4 | Größe des Segments in der Datei |
| [p_memsz](#p_memsz) | 0x14 | 4 | Größe des Segments, das es im Speicher haben soll |
| [p_flags](#p_flags) | 0x18 | 4 | Flags |
| [p_align](#p_align) | 0x1C | 4 | Alignment |

#### p_type

Dieses Feld gibt den Typ des Segments an, für eine ausführbare ELF-Datei ist vor allem PT_LOAD relevant. Die folgenden Beschreibungen sind auf PT_LOAD bezogen (es kann sein, dass sie auch auf andere Typen zutreffen).

| Name | Wert | Beschreibung |
| ------------ | -------------- | -------------------------------------------------------------------- |
| PT_NULL | 0 | Ungültiges Segment |
| PT_LOAD | 1 | Ladbares Segment |
| PT_DYNAMIC | 2 | Dynamisches Segment |
| PT_INTERP | 3 | Position eines 0-terminierten Strings, der den Interpreter angibt. |
| PT_NOTE | 4 | Universelles Segment |
| PT_SHLIB | 5 | Shared Lib |
| PT_PHDIR | 6 | Gibt Position und Größe des Programm-Headers an. |
| PT_TLS | 7 | Thread-Local Storage |
| PT_LOOS | `0x60000000` | Reserviert für betriebssystemspezifische Erweiterungen |
| PT_HIOS | `0x6fffffff` | Reserviert für betriebssystemspezifische Erweiterungen |
| PT_LOPROC | `0x70000000` | Reserviert für prozessorspezifische Erweiterungen |
| PT_HIPROC | `0x7fffffff` | Reserviert für prozessorspezifische Erweiterungen |

Außerdem habe ich noch diese (betriebssystemspezifischen) Werte in Linux-Header-Dateien (<http://www.cs.fsu.edu/~baker/devices/lxr/http/source/linux/include/linux/elf.h#L35>) gefunden.

| Name | Wert |
| ----------------- | --------------------- |
| PT_GNU_EH_FRAME | PT_LOOS+`0x474e550` |
| PT_GNU_STACK | PT_LOOS+`0x474e551` |

#### p_offset

Offset in der Datei, an dem das Segment beginnt.

#### p_vaddr

Virtuelle Adresse, an die das Segment kopiert werden soll.

#### p_paddr

Gibt die physische Zieladresse für Systeme an, für welche dies relevant ist.

#### p_filesz

Enthält die Größe des Segments in der Datei. Kann eventuell auch 0 sein, z. B. für die BSS-Sektion.

#### p_memsz

Gibt die Größe des Segments im RAM an. Kann 0 sein.

#### p_flags

Beschreibt Flags, z. B. Zugriffsrechte.

| Name | Wert | Beschreibung |
| ------ | ------ | ------------------------ |
| PF_X | 1 | Ausführbares Segment |
| PF_W | 2 | Beschreibbares Segment |
| PF_R | 4 | Lesbares Segment |

Damit kann man den Wert berechnen: \<c\>

    flags = (read?PF_R:0)|(write?PF_W:0)|(exe?PF_X:0);

\</c\>

#### p_align

Alignment des Segmentes. Wenn 0 oder 1 angegeben wird, ist kein Alignment erforderlich. Ansonsten muss es eine 2er-Potenz sein (2, 4, 8, 16, ...).

## Überprüfen

Überprüfen kann man die ELF-Datei mit den folgenden Schritten:

- MAGIC-String überprüfen
- Architektur überpüfen
- Klasse (32bit/64bit) überprüfen
- Daten-Format (Little-/Big-Endian) überprüfen
- Version überprüfen

## Siehe auch

[ELF-Tutorial](ELF-Tutorial "ELF-Tutorial")

## Links

- [ELF für x86](http://www.acm.uiuc.edu/sigops/rsrc/pfmt11.pdf)
- [Wikipedia: ELF](http://en.wikipedia.org/wiki/Executable_and_Linkable_Format) (sehr gute Sammlung von Links)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/11160/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1528/index.html)

<!-- MediaWiki page 1528; revision 11160; parent 10626; 2013-11-15T21:55:28Z -->
