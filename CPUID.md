# CPUID

Der CPUID-Befehl wird benutzt, um Informationen über die Fähigkeiten eines Prozessors zu erhalten, wie zum Beispiel den Herstellernamen, die Modellnummer, die Größe des Caches, usw.

## Wie man CPUID benutzt

Um den CPUID-Befehl auszuführen, verwendet man einfach den Assembler-Befehl "CPUID". Die nötigen Parameter(Funktionsnummer) werden dabei im Register EAX angegeben. Die Rückgabewerte werden in den Registern *EAX*, *EBX*, *EDX* und *ECX* abgelegt.

Um zum Beispiel den Vendor-ID-String, also den Herstellernamen, zu bekommen, ruft man CPUID mit der Funktionsnummer 0x00 auf. \<asm\>

    mov eax, 0x00
    cpuid

\</asm\> Ein AMD-Prozessor hätte jetzt folgende Register Werte: EBX="**Auth**", EDX="**enti**", ECX="**cAMD**"

## Standard Funktionen

Die Standard Funktionsnummern beginnen bei 0. Der größt mögliche Funktionsnummer, die von der jeweiligen CPU unterstützt wird befindet sich nach dem aufrufen von *Function 0* im *EAX*-Register. Die Standard Funktionen sind nicht Hersteller spezifisch, sondern sollen für alle CPUs gleich sein.

### EAX = 0x00000000

CPUID-Funktion Nr. 0x00 gibt wie bereits genannt die größte vom Prozessor unterstützte Funktionsnummer im *EAX*-Register und die Vendor-ID in den Registern *EBX*, *EDX* und *ECX*(in dieser Reihenfolge) an. **Auchtung: Der String ist nicht nullterminiert!**

#### Vendor-ID der einzelnen Hersteller

- AMD: "AuthenticAMD"
- Intel: "GenuineIntel"
- VIA: "CentaurHauls"
- Transmeta: "GenuineTMx86"
- Cyrix: "CyrixInstead"
- Centaur: "CentaurHauls"
- NexGen: "NexGenDriven"
- UMC: "UMC UMC UMC "
- SiS: "SiS SiS SiS "
- NSC: "Geode by NSC"
- Rise: "RiseRiseRise"

## Intelbefehle

### EAX = 0x00000001

Das Ergebnis der diser Funktion ist folgendes:

#### EAX

| Bits | Funktion |
| --------- | ------------------------------------ |
| 31 - 28 | Reserviert |
| 27 - 20 | Erweiterte Familie |
| 19 - 16 | Erweitertes Modell |
| 15 - 14 | Reserviert |
| 13 - 12 | Prozessortyp |
| 11 - 8 | Familienkennzeichen / Familiencode |
| 7 - 4 | Model |
| 4 - 0 | Stepping |

#### EBX

| Bits | Funktion |
| --------- | ------------------------------------------------------------------------------------------------------- |
| 31 - 24 | [APIC ID](https://github.com/lowlevel-eu/wiki/wiki/Advanced-Programmable-Interrupt-Controller "APIC") |
| 23 - 16 | Count |
| 15 - 8 | Chunks |
| 7 - 0 | Brand ID |

- *APIC ID* ist nur gültig wenn das *[APIC-Flag](#edx---featureflags)* gesetzt ist.
- *Count* ist die Anzahl der logischen Prozessoren und ist nur mit gesetztem *[Hyper-Threading-Flag](#edx---featureflags)* gültig.
- *Chunks* gibt die Größe einer Cache line in 8 Byte Blocken an. Das Feld ist ebenfalls nur gültig in Verbindung mit einem gesetzten *[CFLUSH-Flag](#edx---featureflags)*.

#### ECX

Hier soll ein Bytearray sein, es wird aber nicht empfohlen, daraus zu lesen. Dieses Feld ist ein kommendes Feature. Es zählt also zu den reservierten Feldern.

#### EDX - Featureflags

Dies sind die Featureflags. Wenn ein Bit gesetzt(=1) ist, dann wird das entsprechende Feature unterstützt.

| Bit | Funktion |
| --------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| 31 - 30 | Reserviert |
| 29 | Wenn eins, dann wird das Thermal Monitor unterstützt |
| 28 | Der Prozessor unterstützt Hyper-Threading. |
| 27 | Der Prozessor unterstützt Self-Snoop |
| 26 | Der Prozessor kann SSE2 |
| 25 | Der Prozessor kann SSE |
| 24 | Der Prozessor unterstützt FXSAVE und FXSTOR, womit er einen Floatzusammenhang(?) speichern und wiederherstellen kann |
| 23 | Der Prozessor kann MMX |
| 22 | Der Prozessor kann die Temperatur und den Prozessortakt durch eine Software verändert und überwacht werden |
| 21 | Der Prozessor hat die Fähigkeit, die Entwicklung eines Ablegers in eine Adresse zu schreiben |
| 20 | Reserviert |
| 19 | Der Prozessor kann CSFLUSH |
| 18 | Der 12-Byte ProzessorID ist aktiviert und vorhanden |
| 17 | Der Prozessor kann im Protected Mode mehr als 4 GByte adressieren. (PSE) |
| 16 | Der Prozessor unterstützt die Page Attribute Table |
| 15 | Der Prozessor untersützt CMOVcc, und wenn Bit 0 gesetzt ist, dann kann er FCMOVCC und FCOMI |
| 14 | Der Prozessor unterstützt die Machine Check Architecture und MCG_CAP Register |
| 13 | Der Prozessor unterstützt die Page Entry Table, die Page Directory Table und das TLB muss nicht erneuert werden |
| 12 | Der Prozessor unterstützt die Memory Type Range Register, speziell das MTRR_CAP Register |
| 11 | Der Prozessor unterstützt die Fast System Call Befehle, den SYSENTER Befehl und SYSEXIT Befehl |
| 10 | Reserviert |
| 9 | Der Prozessor beinhaltet ein [Local APIC](https://github.com/lowlevel-eu/wiki/wiki/Local-Advanced-Programmable-Interrupt-Controller "Local APIC") |
| 8 | Der Prozessor unterstützt den CMPXCHG8 Befehl |
| 7 | Der Prozessor unterstützt die Machine Check Exception |
| 6 | Der Prozessor unterstützt Physical Adress Extension |
| 5 | Der Prozessor unterstützt die Model Specific Register, den RDMSR Befehl und den WRMSR Befehl |
| 4 | Der Prozessor unterstützt den RDTSC Befehl, zudem den CR4.TSD-Bit für Rechtekontrolle |
| 3 | Der Prozessor unterstützt 4-MByte-Pages |
| 2 | Der Prozessor unterstützt I/O-Breakpoints, das CR4.DE Bit und die DR4 und DR5 Register |
| 1 | Der Prozessor unterstützt Erweiterungen für den Virtual-8086-Modus |
| 0 | Der Prozessor unterstützt die Intel857-Gleitkommeoperationen |

### EAX = 0x00000002

Wenn in EAX statt Null Zwei steht, dann werden bei Intelprozessoren Informationen über den Cache und die TLB-Deskriptoren ausgegeben.

### EAX = 0x00000003

Wenn in EAX statt Null Drei steht, wird bei Intelprozessoren stattdessen folgendes ausgegeben:

#### EAX

Reserviert

#### EBX

Reserviert

#### ECX

Die Bits 31 bis 0 der Prozessor-ID sind darin hinterlegt. **Funktioniert nur bei Prozessoren, bei denen das entsprechende *[Featureflag(Bit 18)](#edx---featureflags)* gesetzt ist.**

#### EDX

Die Bytes 63 bis 32 der Prozessor-ID sind darin hinterlegt. *(siehe oben)*

## Erweiterte Funktionen

Es gibt Funktionen, die Hersteller spezifisch sind, d.h. sieh gelten nur nur für Intel- bzw. nur für AMD Prozessoren. Solche Befehle sollte man nicht ausführen, wenn man nicht weiß von welchem Hersteller die CPU ist! Zum Beispiel sollten CPUID-Befehle, die nur für Intel-CPUs gelten, nicht auf einer AMD-CPU ausgeführt werden. Diese Funktionen beginnen bei 0x80000000.

## Siehe auch

[Englischer Artikel über den CPUID-Befehl](http://wiki.osdev.org/CPUID)

[Englische Doku von CPUID; mit AMD/INTEL und anderen Prozessoren](http://sandpile.org/ia32/cpuid.htm)

[Intels CPUID-Spezifikation](http://support.intel.com/Assets/PDF/appnote/241618.pdf)

[AMDs CPUID-Spezifikation](http://www.amd.com/us-en/assets/content_type/white_papers_and_tech_docs/25481.pdf)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/3945/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1739/index.html)

<!-- MediaWiki page 1739; revision 3945; parent 3919; 2009-01-21T01:01:15Z -->
