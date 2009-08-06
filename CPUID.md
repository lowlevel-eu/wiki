# CPUID

**Achtung!**

Dieser Artikel wird gerade generalüberholt. Bitte nimm keine Änderungen an diesem Artikel vor! (Der Artikel könnte zwischenzeitlich ein wenig komisch anmuten ;-) ~[SHyx0rmZ](https://lowlevel-eu.github.io/wiki/pages/1785/index.html "Benutzer:SHyx0rmZ") 10:55, 6. Aug. 2009 (CEST)

Vorlage:Hinweiss

So sehen die herstellerspezifischen Tabellenzellen aus:

| Farbe | Bedeutung |
| ------- | --------------------------------------------------------------------------------------------------------------------------- |
| Blau | Dieser Eintrag gilt **ausschließlich** für **Intel**-Prozessoren. Auf AMD-Prozessoren ist dieser Eintrag **reserviert**!. |
| Grün | Dieser Eintrag gilt **ausschließlich** für **AMD**-Prozessoren. Auf Intel-Prozessoren ist dieser Eintrag **reserviert**!. |

Vorlage:Hinweiss

Der **CPUID**-Befehl liefert, sofern er denn von der CPU unterstützt wird, Informationen zu zahlreichen Fähigkeiten der CPU, wie zum Beispiel den Herstellernamen, die Modellnummer oder die Größe des Caches.

## Wie man CPUID benutzt

Bevor man munter versucht, mit dem CPUID Befehl Informationen auszulesen, sollte man ersteinmal prüfen, ob die CPU den Befehl überhaupt unterstützt. Dazu testet man, ob das ID-Flag gesetzt und gelöscht werden kann.

Aussehen kann das zum Beispiel so: \<asm\> pushfd  ; Sichere Flags pushfd  ; Sichere Flags pop ecx  ; Lade Flags in EXC mov eax, ecx  ; Schiebe Flags in EAX xor eax, 0x200000  ; Vertausche das ID-Flag push eax  ; Sichere neue Flags popfd  ; Lade neue Flags in EFLAGS

                          ; Wenn CPUID unterstützt wird, wird das geänderte ID-Flag übernommen
                          ; Ansonsten wird bleibt das alte ID-Flag bestehen

pushfd  ; Sichere Flags pop eax  ; Lade Flags in EAX xor eax, ecx  ; Vergleiche EAX und ECX popfd  ; Stelle Original Flags wieder her je cpuid_unsupported  ; EAX und ECX sind gleich, CPUID wird nicht unterstütz! jmp cpu_supported  ; EAX und ECX sind verschieden, CPUID wird unterstützt! \</asm\>

Um den CPUID-Befehl auszuführen, verwendet man einfach den Assembler-Befehl **cpuid**. Die Funktionsnummer der CPUID-Funktion wird dabei im **EAX**-Register übergeben. Die Rückgabewerte werden in den Registern **EAX**, **EBX**, **EDX** und **ECX** abgelegt.

Um zum Beispiel den Vendor-ID-String, also den Herstellernamen, auszulesen, ruft man CPUID mit der Funktionsnummer 0x00000000 auf. \<asm\> mov eax, 0x00000000  ; xor eax, eax bewirkt das selbe und ist schneller cpuid  ; Der Vendor-ID-String befindet sich nun in (in dieser Reihenfolge), EBX, EDX, ECX \</asm\> Ein **AMD**-Prozessor hätte jetzt folgende Register Werte: **EBX**="**Auth**", **EDX**="**enti**", **ECX**="**cAMD**"  
Ein **Intel**-Prozessor hätte jetzt folgende Register Werte: **EBX**="**Genu**", **EDX**="**ineI**", **ECX**="**ntel**"

# Standard Funktionen

Die Standard Funktionsnummern beginnen bei 0. Der größtmögliche Funktionsnummer, die von der jeweiligen CPU unterstützt wird befindet sich nach dem Aufruf von Funktion 0 im *EAX*-Register. Die Standard Funktionen sind nicht Hersteller spezifisch, sondern sollen für alle CPUs gleich sein.

## Funktion 0x0000_0000

CPUID-Funktion Nr. 0x00 gibt höchste vom Prozessor unterstützte Funktionsnummer im **EAX**-Register und die [Vendor-ID](https://github.com/lowlevel-eu/wiki/wiki/CPUID#vendor-id-strings "CPUID") in den Registern **EBX**, **EDX** und **ECX**(in dieser Reihenfolge) an.

**Achtung!**

Der String ist nicht nullterminiert!

#### EAX

<table>
<tbody><tr>
<th colspan="32">Bit
</th></tr>
<tr>
<th>31
</th>
<th>30
</th>
<th>29
</th>
<th>28
</th>
<th>27
</th>
<th>26
</th>
<th>25
</th>
<th>24
</th>
<th>23
</th>
<th>22
</th>
<th>21
</th>
<th>20
</th>
<th>19
</th>
<th>18
</th>
<th>17
</th>
<th>16
</th>
<th>15
</th>
<th>14
</th>
<th>13
</th>
<th>12
</th>
<th>11
</th>
<th>10
</th>
<th>9
</th>
<th>8
</th>
<th>7
</th>
<th>6
</th>
<th>5
</th>
<th>4
</th>
<th>3
</th>
<th>2
</th>
<th>1
</th>
<th>0
</th></tr>
<tr>
<td colspan="32">Höchste, unterstützte Standard-Funktion
</td></tr></tbody></table>

#### EBX

<table>
<tbody><tr>
<th colspan="32">Bit
</th></tr>
<tr>
<th>31
</th>
<th>30
</th>
<th>29
</th>
<th>28
</th>
<th>27
</th>
<th>26
</th>
<th>25
</th>
<th>24
</th>
<th>23
</th>
<th>22
</th>
<th>21
</th>
<th>20
</th>
<th>19
</th>
<th>18
</th>
<th>17
</th>
<th>16
</th>
<th>15
</th>
<th>14
</th>
<th>13
</th>
<th>12
</th>
<th>11
</th>
<th>10
</th>
<th>9
</th>
<th>8
</th>
<th>7
</th>
<th>6
</th>
<th>5
</th>
<th>4
</th>
<th>3
</th>
<th>2
</th>
<th>1
</th>
<th>0
</th></tr>
<tr>
<td colspan="32">Bytes 0 - 3 des Vendor-ID-Strings
</td></tr></tbody></table>

#### ECX

<table>
<tbody><tr>
<th colspan="32">Bit
</th></tr>
<tr>
<th>31
</th>
<th>30
</th>
<th>29
</th>
<th>28
</th>
<th>27
</th>
<th>26
</th>
<th>25
</th>
<th>24
</th>
<th>23
</th>
<th>22
</th>
<th>21
</th>
<th>20
</th>
<th>19
</th>
<th>18
</th>
<th>17
</th>
<th>16
</th>
<th>15
</th>
<th>14
</th>
<th>13
</th>
<th>12
</th>
<th>11
</th>
<th>10
</th>
<th>9
</th>
<th>8
</th>
<th>7
</th>
<th>6
</th>
<th>5
</th>
<th>4
</th>
<th>3
</th>
<th>2
</th>
<th>1
</th>
<th>0
</th></tr>
<tr>
<td colspan="32">Bytes 8 - 11 des Vendor-ID-Strings
</td></tr></tbody></table>

#### EDX

<table>
<tbody><tr>
<th colspan="32">Bit
</th></tr>
<tr>
<th>31
</th>
<th>30
</th>
<th>29
</th>
<th>28
</th>
<th>27
</th>
<th>26
</th>
<th>25
</th>
<th>24
</th>
<th>23
</th>
<th>22
</th>
<th>21
</th>
<th>20
</th>
<th>19
</th>
<th>18
</th>
<th>17
</th>
<th>16
</th>
<th>15
</th>
<th>14
</th>
<th>13
</th>
<th>12
</th>
<th>11
</th>
<th>10
</th>
<th>9
</th>
<th>8
</th>
<th>7
</th>
<th>6
</th>
<th>5
</th>
<th>4
</th>
<th>3
</th>
<th>2
</th>
<th>1
</th>
<th>0
</th></tr>
<tr>
<td colspan="32">Bytes 4 - 7 des Vendor ID-Strings
</td></tr></tbody></table>

#### Vendor-ID-Strings

| Vendor-ID-String | Hersteller |
| ------------------ | ------------------------ |
| `"AuthenticAMD"` | AMD |
| `"CentaurHauls"` | Centaur |
| `"CyrixInstead"` | Cyrix |
| `"GenuineIntel"` | Intel |
| `"NexGenDriven"` | NexGen |
| `"Geode by NSC"` | National Semiconductor |
| `"RiseRiseRise"` | Rise |
| `"SiS SiS SiS "` | SiS |
| `"GenuineTMx86"` | Transmeta |
| `"UMC UMC UMC "` | UMC |
| `"VIA VIA VIA "` | VIA |

## Funktion 0x0000_0001

#### EAX

<table>
<tbody><tr>
<th colspan="32">Bit
</th></tr>
<tr>
<th>31
</th>
<th>30
</th>
<th>29
</th>
<th>28
</th>
<th>27
</th>
<th>26
</th>
<th>25
</th>
<th>24
</th>
<th>23
</th>
<th>22
</th>
<th>21
</th>
<th>20
</th>
<th>19
</th>
<th>18
</th>
<th>17
</th>
<th>16
</th>
<th>15
</th>
<th>14
</th>
<th>13
</th>
<th>12
</th>
<th>11
</th>
<th>10
</th>
<th>9
</th>
<th>8
</th>
<th>7
</th>
<th>6
</th>
<th>5
</th>
<th>4
</th>
<th>3
</th>
<th>2
</th>
<th>1
</th>
<th>0
</th></tr>
<tr>
<td colspan="4">
</td>
<td colspan="8">Erweiterte Familie
</td>
<td colspan="4">Erweitertes Modell
</td>
<td colspan="2">
</td>
<td colspan="2">Typ
</td>
<td colspan="4">Familie
</td>
<td colspan="4">Modell
</td>
<td colspan="4">Stepping
</td></tr></tbody></table>

#### EBX

<table>
<tbody><tr>
<th colspan="32">Bit
</th></tr>
<tr>
<th>31
</th>
<th>30
</th>
<th>29
</th>
<th>28
</th>
<th>27
</th>
<th>26
</th>
<th>25
</th>
<th>24
</th>
<th>23
</th>
<th>22
</th>
<th>21
</th>
<th>20
</th>
<th>19
</th>
<th>18
</th>
<th>17
</th>
<th>16
</th>
<th>15
</th>
<th>14
</th>
<th>13
</th>
<th>12
</th>
<th>11
</th>
<th>10
</th>
<th>9
</th>
<th>8
</th>
<th>7
</th>
<th>6
</th>
<th>5
</th>
<th>4
</th>
<th>3
</th>
<th>2
</th>
<th>1
</th>
<th>0
</th></tr>
<tr>
<td colspan="8"><a href="https://github.com/lowlevel-eu/wiki/wiki/Advanced-Programmable-Interrupt-Controller" title="APIC">APIC ID</a>
</td>
<td colspan="8">Anzahl logischer Prozessoren
</td>
<td colspan="8">CLFLUSH Size
</td>
<td colspan="8">Brand ID
</td></tr></tbody></table>

**Achtung!**

**APIC ID** ist nur gültig wenn das **[APIC-Flag](#)** gesetzt ist.  
Die Anzahl der logischen Prozessoren ist nur bei gesetztem **[Hyper-Threading-Flag](#)** gültig.  
**CLFLUSH Size** gibt die Größe einer Cache line in 8 Byte Blöcken an. Das Feld ist nur gültig in Verbindung mit einem gesetzten **[CFLUSH-Flag](#)**.

#### ECX

<table>
<tbody><tr>
<th colspan="32">Bit
</th></tr>
<tr>
<th>31
</th>
<th>30
</th>
<th>29
</th>
<th>28
</th>
<th>27
</th>
<th>26
</th>
<th>25
</th>
<th>24
</th>
<th>23
</th>
<th>22
</th>
<th>21
</th>
<th>20
</th>
<th>19
</th>
<th>18
</th>
<th>17
</th>
<th>16
</th>
<th>15
</th>
<th>14
</th>
<th>13
</th>
<th>12
</th>
<th>11
</th>
<th>10
</th>
<th>9
</th>
<th>8
</th>
<th>7
</th>
<th>6
</th>
<th>5
</th>
<th>4
</th>
<th>3
</th>
<th>2
</th>
<th>1
</th>
<th>0
</th></tr>
<tr>
<td colspan="1">RAZ
</td>
<td colspan="3">
</td>
<td colspan="1">OSXSAVE
</td>
<td colspan="1">XSAVE
</td>
<td colspan="2">
</td>
<td colspan="1">POPCNT
</td>
<td colspan="1">MOVBE
</td>
<td colspan="1">x2APIC
</td>
<td colspan="1">SSE4.2
</td>
<td colspan="1">SSE4.1
</td>
<td colspan="1">DCA
</td>
<td colspan="2">
</td>
<td colspan="1">PDCM
</td>
<td colspan="1">xTPR
</td>
<td colspan="1">CX16
</td>
<td colspan="2">
</td>
<td colspan="{{{1}}}">CNXT-ID
</td>
<td colspan="1">SSSE3
</td>
<td colspan="1">TM2
</td>
<td colspan="1">EST
</td>
<td colspan="1">SMX
</td>
<td colspan="1">DS-CPL
</td>
<td colspan="1">MONITOR
</td>
<td colspan="1">DTES64
</td>
<td colspan="1">
</td>
<td colspan="1">SSE3
</td></tr></tbody></table>

Dieses Register gibt erweiterte Informationen über den Prozessor:

| Bits | Funktion |
| ------ | ---------------------------------------------------- |
| 9 | Verfügbarkeit von SSSE3 |
| 5 | Verfügbarkeit von Virtual Machine Extensions (VMX) |
| 3 | Die Befehle MONITOR und MWAIT sind verfügbar |
| 0 | Verfügbarkeit von SSE3 |

#### EDX

<table>
<tbody><tr>
<th colspan="32">Bit
</th></tr>
<tr>
<th>31
</th>
<th>30
</th>
<th>29
</th>
<th>28
</th>
<th>27
</th>
<th>26
</th>
<th>25
</th>
<th>24
</th>
<th>23
</th>
<th>22
</th>
<th>21
</th>
<th>20
</th>
<th>19
</th>
<th>18
</th>
<th>17
</th>
<th>16
</th>
<th>15
</th>
<th>14
</th>
<th>13
</th>
<th>12
</th>
<th>11
</th>
<th>10
</th>
<th>9
</th>
<th>8
</th>
<th>7
</th>
<th>6
</th>
<th>5
</th>
<th>4
</th>
<th>3
</th>
<th>2
</th>
<th>1
</th>
<th>0
</th></tr>
<tr>
<td colspan="1">PBE
</td>
<td colspan="1">IA64
</td>
<td colspan="1">TM
</td>
<td colspan="1">HTT
</td>
<td colspan="1">SS
</td>
<td colspan="1">SSE2
</td>
<td colspan="1">SSE
</td>
<td colspan="1">FXSR
</td>
<td colspan="1">MMX
</td>
<td colspan="1">ACPI
</td>
<td colspan="1">DS
</td>
<td colspan="1">
</td>
<td colspan="1">CLFLSH
</td>
<td colspan="1">PSN
</td>
<td colspan="1">PSE-36
</td>
<td colspan="1">PAT
</td>
<td colspan="1">CMOV
</td>
<td colspan="1">MCA
</td>
<td colspan="1">PGE
</td>
<td colspan="1">MTRR
</td>
<td colspan="1">SEP
</td>
<td colspan="1">
</td>
<td colspan="1">APIC
</td>
<td colspan="1">CX8
</td>
<td colspan="1">MCE
</td>
<td colspan="1">PAE
</td>
<td colspan="1">MSR
</td>
<td colspan="1">TSC
</td>
<td colspan="1">PSE
</td>
<td colspan="1">DE
</td>
<td colspan="1">VME
</td>
<td colspan="1">FPU
</td></tr></tbody></table>

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
| 22 | Die Temperatur und der Prozessortakt kann durch eine Software verändert und überwacht werden |
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

Die Bits 31 bis 0 der Prozessor-ID sind darin hinterlegt. **Funktioniert nur bei Prozessoren, bei denen das entsprechende *[Featureflag(Bit 18)](#)* gesetzt ist.**

#### EDX

Die Bits 63 bis 32 der Prozessor-ID sind darin hinterlegt. *(siehe oben)*

## Erweiterte Funktionen

Es gibt Funktionen, die Hersteller spezifisch sind, d.h. sieh gelten nur nur für Intel- bzw. nur für AMD Prozessoren. Solche Befehle sollte man nicht ausführen, wenn man nicht weiß von welchem Hersteller die CPU ist! Zum Beispiel sollten CPUID-Befehle, die nur für Intel-CPUs gelten, nicht auf einer AMD-CPU ausgeführt werden. Diese Funktionen beginnen bei 0x80000000.

Erweiterte Funktionen von Intel:

### EAX = 0x80000000

#### EAX

Enthält maximale erweiterte Funktionsnummer.

#### EBX

Reserviert

#### ECX

Reserviert

#### EDX

Reserviert

### EAX = 0x80000001

#### EAX

Reserviert

#### EBX

Reserviert

#### ECX

Reserviert

#### EDX

Wenn Bit 29 gesetzt, dann ist Intel64-Technologie verfügbar

### EAX = 0x80000002

#### EAX

Eingebrannter String

#### EBX

Eingebrannter String (Fortsetzung)

#### ECX

Eingebrannter String (Fortsetzung)

#### EDX

Eingebrannter String (Fortsetzung)

### EAX = 0x80000003

#### EAX

Eingebrannter String (Fortsetzung)

#### EBX

Eingebrannter String (Fortsetzung)

#### ECX

Eingebrannter String (Fortsetzung)

#### EDX

Eingebrannter String (Fortsetzung)

### EAX = 0x80000004

#### EAX

Eingebrannter String (Fortsetzung)

#### EBX

Eingebrannter String (Fortsetzung)

#### ECX

Eingebrannter String (Fortsetzung)

#### EDX

Eingebrannter String (Fortsetzung)

  

## Siehe auch

- [Englischer Artikel über den CPUID-Befehl](http://wiki.osdev.org/CPUID)
- [Englische Doku von CPUID; mit AMD/INTEL und anderen Prozessoren](http://sandpile.org/ia32/cpuid.htm)
- [Intels CPUID-Spezifikation](http://support.intel.com/Assets/PDF/appnote/241618.pdf)
- [AMDs CPUID-Spezifikation](http://www.amd.com/us-en/assets/content_type/white_papers_and_tech_docs/25481.pdf)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/5203/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1739/index.html)

<!-- MediaWiki page 1739; revision 5203; parent 5144; 2009-08-06T11:57:19Z -->
