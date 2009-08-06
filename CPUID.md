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

Bevor man munter versucht, mit dem CPUID-Befehl Informationen auszulesen, sollte man ersteinmal prüfen, ob die CPU den Befehl überhaupt unterstützt. Dazu testet man, ob das ID-Flag gesetzt und gelöscht werden kann.

Aussehen kann das zum Beispiel so: \<asm\> pushfd  ; Sichere Flags pushfd  ; Sichere Flags pop ecx  ; Lade Flags in ECX mov eax, ecx  ; Schiebe Flags in EAX xor eax, 0x200000  ; Vertausche das ID-Flag push eax  ; Sichere neue Flags popfd  ; Lade neue Flags in EFLAGS

                          ; Wenn CPUID unterstützt wird, wird das geänderte ID-Flag übernommen
                          ; Ansonsten wird bleibt das alte ID-Flag bestehen

pushfd  ; Sichere Flags pop eax  ; Lade Flags in EAX xor eax, ecx  ; Vergleiche EAX und ECX popfd  ; Stelle Original Flags wieder her je cpuid_unsupported  ; EAX und ECX sind gleich, CPUID wird nicht unterstützt! jmp cpu_supported  ; EAX und ECX sind verschieden, CPUID wird unterstützt! \</asm\>

Um den CPUID-Befehl auszuführen, verwendet man einfach den Assemblerbefehl **CPUID**. Die Funktionsnummer der CPUID-Funktion wird dabei im **EAX**-Register übergeben. Die Rückgabewerte werden in den Registern **EAX**, **EBX**, **EDX** und **ECX** abgelegt.

Um zum Beispiel den Vendor-ID-String, also den Herstellernamen, auszulesen, ruft man CPUID mit der Funktionsnummer 0x00000000 auf. \<asm\> mov eax, 0x00000000  ; xor eax, eax bewirkt das selbe und ist schneller cpuid  ; Der Vendor-ID-String befindet sich nun in (in dieser Reihenfolge), EBX, EDX, ECX \</asm\> Ein **AMD**-Prozessor hätte jetzt folgende Registerwerte: **EBX**="**Auth**", **EDX**="**enti**", **ECX**="**cAMD**"  
Ein **Intel**-Prozessor hätte jetzt folgende Registerwerte: **EBX**="**Genu**", **EDX**="**ineI**", **ECX**="**ntel**"

# Standardfunktionen

Die Standardfunktionsnummern beginnen bei 0. Die größtmögliche Funktionsnummer, die von der jeweiligen CPU unterstützt wird, befindet sich nach dem Aufruf von Funktion 0 im *EAX*-Register. Die Standardfunktionen sind nicht herstellerspezifisch, sondern sollen für alle CPUs gleich sein.

## Funktion 0x0000_0000

CPUID-Funktion Nr. 0x00 gibt die höchste vom Prozessor unterstützte Funktionsnummer im **EAX**-Register und die [Vendor-ID](https://github.com/lowlevel-eu/wiki/wiki/CPUID#vendor-id-strings "CPUID") in den Registern **EBX**, **EDX** und **ECX**(in dieser Reihenfolge) zurück.

**Achtung!**

Der String ist nicht nullterminiert!

#### EAX - Höchste Standardfunktion

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
<td colspan="32">Höchste unterstützte Standardfunktion
</td></tr></tbody></table>

#### EBX - Vendor

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

#### ECX - Vendor

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

#### EDX - Vendor

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

Eine Liste der möglichen Vendor-ID-Strings

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

#### EAX - Prozessor

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

#### EBX - Sonstiges

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
<td colspan="8">CLFLUSH-Size
</td>
<td colspan="8">Brand ID
</td></tr></tbody></table>

**Achtung!**

**APIC ID** ist nur gültig wenn das **[APIC-Flag](#edx---featureflags)** gesetzt ist.  
Die Anzahl der logischen Prozessoren ist nur bei gesetztem **[Hyper-Threading-Flag](#edx---featureflags)** gültig.  
**CLFLUSH-Size** gibt die Größe einer Cache line in 8-Byte-Blöcken an. Das Feld ist nur gültig in Verbindung mit einem gesetzten **[CFLUSH-Flag](#edx---featureflags)**.

#### ECX - Featureflags

Dies sind die Featureflags. Wenn ein Bit gesetzt (=1) ist, dann wird das entsprechende Feature unterstützt.

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
<td colspan="1">VMX
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
</td></tr></tbody></table> <table>
<tbody><tr>
<th>Bit
</th>
<th>Funktion
</th></tr>
<tr>
<th colspan="1">31
</th>
<td rowspan="4">
</td></tr>
<tr>
<th colspan="1">30
</th></tr>
<tr>
<th colspan="1">29
</th></tr>
<tr>
<th colspan="1">28
</th></tr>
<tr>
<th colspan="1">27
</th>
<td colspan="1">Zeigt an, dass das <a href="https://github.com/lowlevel-eu/wiki/wiki/Betriebssystem" title="Betriebssystem">Betriebssystem</a> die Befehle <b>XSETBV</b> und <b>XGETBV</b> aktiviert hat, um auf das <b>XFEATURE_ENABLE_MASK</b> Register (<b>XCR0</b>) zuzugreifen und die erweiterten Zustandsfeatures <b>XSAVE</b> und <b>XRSTOR</b> zu nutzen
</td></tr>
<tr>
<th colspan="1">26
</th>
<td colspan="1">Unterstützt die erweiterten Zustandsfeatures <b>XSAVE</b> und <b>XRSTOR</b>, die Befehle <b>XSETBV</b> und <b>XGETBV</b> und implementiert das <b>XFEATURE_ENABLE_MASK</b> Register (<b>XCR0</b>)
</td></tr>
<tr>
<th colspan="1">25
</th>
<td rowspan="2">
</td></tr>
<tr>
<th colspan="1">24
</th></tr>
<tr>
<th colspan="1">23
</th>
<td colspan="1">Unterstützt den <b>POPCNT</b> Befehl
</td></tr>
<tr>
<th colspan="1">22
</th>
<td colspan="1">Unterstützt den <b>MOVBE</b> Befehl
</td></tr>
<tr>
<th colspan="1">21
</th>
<td colspan="1">Unterstützt x2APIC-Features
</td></tr>
<tr>
<th colspan="1">20
</th>
<td colspan="1">Unterstützt SSE4.2
</td></tr>
<tr>
<th colspan="1">19
</th>
<td colspan="1">Unterstützt SSE4.1
</td></tr>
<tr>
<th colspan="1">18
</th>
<td colspan="1">Unterstützt das prefetchen von Daten von einem in den Speicher gemappten Gerät
</td></tr>
<tr>
<th colspan="1">17
</th>
<td rowspan="2">
</td></tr>
<tr>
<th colspan="1">16
</th></tr>
<tr>
<th colspan="1">15
</th>
<td colspan="1">Unterstützt das Performance Capabilities MSR (<b>IA32_PERF_CAPABILITIES</b>, MSR 0x345)
</td></tr>
<tr>
<th colspan="1">14
</th>
<td colspan="1">Unterstützt die Möglichkeit, das Senden von Task Priority Messages abzuschalten, indem Bit 23 im <b>IA32_MISC_ENABLE</b> MSR gesetzt wird
</td></tr>
<tr>
<th colspan="1">13
</th>
<td colspan="1">Unterstützt den <b>CMPXCHG16B</b> Befehl
</td></tr>
<tr>
<th colspan="1">12
</th>
<td rowspan="2">
</td></tr>
<tr>
<th colspan="1">11
</th></tr>
<tr>
<th colspan="1">10
</th>
<td colspan="{{{1}}}">Der L1-Cachemodus kann vom Bios entweder auf <b>adaptive</b> oder auf <b>shared</b> gesetzt werden
</td></tr>
<tr>
<th colspan="1">9
</th>
<td colspan="1">Unterstützt SSSE3
</td></tr>
<tr>
<th colspan="1">8
</th>
<td colspan="1">Implementiert den "Thermal Monitor 2 thermal control circuit" (TCC)
</td></tr>
<tr>
<th colspan="1">7
</th>
<td colspan="1">Unterstützt Enhanced Intel SpeedStep und implementiert das <b>IA32_PERF_STS</b>-Register und das <b>IA32_PERF_CTL</b>-Register
</td></tr>
<tr>
<th colspan="1">6
</th>
<td colspan="1">Unterstützt Intel Trusted Execution
</td></tr>
<tr>
<th colspan="1">5
</th>
<td colspan="1">Unterstützt <a title="Virtualisierung (Seite nicht vorhanden)">VMX</a>
</td></tr>
<tr>
<th colspan="1">4
</th>
<td colspan="1">Unterstützt die Erweiterungen des Debug-Speicher-Features um durch CPL qualifizierten Branch-Message-Speicher zu nutzen
</td></tr>
<tr>
<th colspan="1">3
</th>
<td colspan="1">Unterstützt den <b>MONITOR</b> Befehl und den <b>MWAIT</b> Befehl
</td></tr>
<tr>
<th colspan="1">2
</th>
<td colspan="1">Kann den Verlauf der 64-Bit-Branch in/von Adressen in einen Buffer schreiben
</td></tr>
<tr>
<th colspan="1">1
</th>
<td colspan="1">
</td></tr>
<tr>
<th colspan="1">0
</th>
<td colspan="1">Unterstützt SSE3
</td></tr></tbody></table>

#### EDX - Featureflags

Dies sind die Featureflags. Wenn ein Bit gesetzt (=1) ist, dann wird das entsprechende Feature unterstützt.

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

| Bit | Funktion |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 31 | Unterstützt die Benutzung des FERR#-Pins und des PBE#-Pins um dem Prozessor im Stop Clock State (STPCLK#) zu signalisieren, dass er einen wartenden Interrupt bearbeiten und dann zur normalen Ausführung zurückkehren soll. |
| 30 | Gehört zur Intel Intanium Familie und läuft gerade im IA32-Emulationsmodus |
| 29 | Implementiert den "Thermal Monitor aumatic thermal control circuitry" (TCC) |
| 28 | Kann mehr als einen logischen Prozessor verwalten |
| 27 | Unterstützt die Verwaltung von miteinander in Konflikt stehenden Speichertypen |
| 26 | Unterstützt SSE2 |
| 25 | Unterstütz [SSE](https://github.com/lowlevel-eu/wiki/wiki/Streaming-SIMD-Extensions "SSE") |
| 24 | Unterstützt die **FXSAVE** und **FXRSTOR** Befehle, mit denen die [Floatingpointregister](https://github.com/lowlevel-eu/wiki/wiki/Register "Register") schnell gesichert werden können |
| 23 | Unterstützt [MMX](https://github.com/lowlevel-eu/wiki/wiki/MultiMedia-Extension "MMX") |
| 22 | Unterstützt Überwachung der Prozessortemperatur und Änderung des Prozessortaktes |
| 21 | Kann Debuginformationen in im Hauptspeicher vorhandene Buffer schreiben |
| 20 |  |
| 19 | Unterstützt den **CLFLUSH**-Befehl |
| 18 | Besitzt eine 96-Bit Prozessor-Seriennummer (Nur verfügbar auf Prozessoren, die neuer als Pentium 4 sind) |
| 17 | Unterstützt [36-Bit Page Size Extensions](https://github.com/lowlevel-eu/wiki/wiki/Page-Size-Extension "Page Size Extension") (4-MiB [Pages](https://github.com/lowlevel-eu/wiki/wiki/Paging "Paging")) |
| 16 | Unterstützt das [PAT-Bit](https://github.com/lowlevel-eu/wiki/wiki/Paging "Paging") |
| 15 | Unterstützt den **CMOVcc** Befehl, mit dem bedingte Verschiebungen vorgenommen werden können |
| 14 | Unterstützt die Machine-Check-Architektur (Besonders das **MTRR_CAP**-Register) |
| 13 | Unterstützt das [Page-Global-Bit](https://github.com/lowlevel-eu/wiki/wiki/Paging "Paging") |
| 12 | Unterstützt MTRR-Register (Besonders das **MTRR_CAP**-Register) |
| 11 | Unterstützt schnelle [Syscalls](https://github.com/lowlevel-eu/wiki/wiki/Syscall "Syscall") durch die Befehle **SYSENTER** und **SYSEXIT** |
| 10 |  |
| 9 | Besitzt einen lokalen [APIC](https://github.com/lowlevel-eu/wiki/wiki/Advanced-Programmable-Interrupt-Controller "APIC") |
| 8 | Unterstützt den **CMPXCHG8B** Befehl |
| 7 | Unterstützt Machine-Check-[Exceptions](https://github.com/lowlevel-eu/wiki/wiki/Exception "Exception") |
| 6 | Unterstützt physische Adressen, die größer als 32-Bit sind |
| 5 | Implementiert Modellspezifische Register über die Befehle **RDMSR** und **WRMSR** |
| 4 | Unterstützt den **RDTSC** Befehl und CR4.TSD-Bit |
| 3 | Unterstützt 4-MiB [Pages](https://github.com/lowlevel-eu/wiki/wiki/Paging "Paging") |
| 2 | Unterstützt I/O-Breakpoints, das CR4.DE-Bit und die DR4- und DR5-Register |
| 1 | Unterstützt den [Virtual 8086 Mode](https://github.com/lowlevel-eu/wiki/wiki/Virtual-8086-Mode "Virtual 8086 Mode") |
| 0 | Besitzt eine [FPU](https://github.com/lowlevel-eu/wiki/wiki/Mathematischer-Koprozessor "FPU"), die den x87-Befehlssatz implementiert |

## EAX = 0x00000002

Wenn in EAX statt null zwei steht, dann werden bei Intelprozessoren Informationen über den Cache und die TLB-Deskriptoren ausgegeben.

## EAX = 0x00000003

Wenn in EAX statt null drei steht, wird bei Intelprozessoren stattdessen folgendes ausgegeben:

#### EAX

Reserviert

#### EBX

Reserviert

#### ECX

Die Bits 31 bis 0 der Prozessor-ID sind darin hinterlegt. **Funktioniert nur bei Prozessoren, bei denen das entsprechende *[Featureflag(Bit 18)](#edx---featureflags)* gesetzt ist.**

#### EDX

Die Bits 63 bis 32 der Prozessor-ID sind darin hinterlegt. *(siehe oben)*

# Erweiterte Funktionen

Es gibt Funktionen, die herstellerspezifisch sind, d.h. sie gelten nur nur für Intel- bzw. nur für AMD-Prozessoren. Solche Befehle sollte man nicht ausführen, wenn man nicht weiß, von welchem Hersteller die CPU ist! Zum Beispiel sollten CPUID-Befehle, die nur für Intel-CPUs gelten, nicht auf einer AMD-CPU ausgeführt werden. Diese Funktionen beginnen bei 0x80000000.

Erweiterte Funktionen von Intel:

## EAX = 0x80000000

#### EAX

Enthält maximale erweiterte Funktionsnummer.

#### EBX

Reserviert

#### ECX

Reserviert

#### EDX

Reserviert

## EAX = 0x80000001

#### EAX

Reserviert

#### EBX

Reserviert

#### ECX

Reserviert

#### EDX

Wenn Bit 29 gesetzt, dann ist Intel64-Technologie verfügbar

## EAX = 0x80000002

#### EAX

Eingebrannter String

#### EBX

Eingebrannter String (Fortsetzung)

#### ECX

Eingebrannter String (Fortsetzung)

#### EDX

Eingebrannter String (Fortsetzung)

## EAX = 0x80000003

#### EAX

Eingebrannter String (Fortsetzung)

#### EBX

Eingebrannter String (Fortsetzung)

#### ECX

Eingebrannter String (Fortsetzung)

#### EDX

Eingebrannter String (Fortsetzung)

## EAX = 0x80000004

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

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/5252/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1739/index.html)

<!-- MediaWiki page 1739; revision 5252; parent 5244; 2009-08-06T15:10:43Z -->
