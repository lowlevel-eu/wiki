# CPUID

Der CPUID-Befehl wird benutzt, um Informationen über die Fähigkeiten eines Prozessors zu erhalten, wie zum Beispiel den Herstellernamen, die Modellnummer, die Größe des Caches, usw.

## Wie man CPUID benutzt

Um den CPUID-Befehl auszuführen, verwendet man einfach den Assembler-Befehl "CPUID". Die nötigen Parameter werden dabei im Register EAX angegeben. Um zum Beispiel den Vendor-ID-String, also den Herstellernamen, zu bekommen, ruft man CPUID mit dem Parameter 0x0 in EAX auf.

    mov eax, 0x0
    cpuid

Natürlich gibt der CPUID-Befehl auch ein Ergebnis zurück. In diesem Fall gibt er einen String zurück, dessen ASCII-Werte in EBX, EDX und ECX liegen. Wenn man den Inhalt dieser drei Register (in dieser Reihenfolge!) hintereinander in den Speicher schreibt, erhält man einen String, die Vendor-ID. Jeder Hersteller hat eigene Vendor-ID. **Achtung: Der String ist nicht nullterminiert!**

### Vendor-ID der einzelnen Hersteller

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

## Spezifische CPUID-Befehle

### Intelbefehle

#### EAX-Inhalt ist eins

Wenn im EAX statt Null eine Eins steht, dann wird bei Intelprozessoren stattdessen folgendes ausgegeben:

##### EAX

| Byte | Funktion |
| --------- | ------------------------------------ |
| 31 - 28 | Reserviert |
| 27 - 20 | Erweiterte Familie |
| 19 - 16 | Erweitertes Modell |
| 15 - 14 | Reserviert |
| 13 - 12 | Prozessortyp |
| 11 - 8 | Familienkennzeichen / Familiencode |
| 7 - 4 | Model |
| 4 - 0 | Stepping |

##### EBX

| Byte | Funktion |
| --------- | -------------------------------------------------------------------------------------------------------------------- |
| 31 - 24 | [APIC](https://github.com/lowlevel-eu/wiki/wiki/Advanced-Programmable-Interrupt-Controller "APIC") ID (Reserviert) |
| 23 - 16 | Zähler(?) (Reserviert) |
| 15 - 8 | Stücke/Einheiten(?) (Reserviert) |
| 7 - 0 | Brand ID (Reserviert) |

##### ECX

Hier soll ein Bytearray sein, es wird aber nicht empfohlen, daraus zu lesen. Dieses Feld ist ein kommendes Feature. Es zählt also zu den reservierten Feldern.

##### EDX

Dies sind die Featureflags. Wenn ein Bit eins, wird das entsprechende Feature unterstüzt.

| Bit | Funktion |
| --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 31 - 30 | Reserviert |
| 29 | Wenn eins, dann wird das Thermal Monitor unterstützt |
| 28 | Der Prozessor könnte Hyper-Threading. Wenn in EBX ein Wert größer als 1 ist, dann wird Hyper-Threading unterstützt |
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
| 17 | Der Prozessor kann im Protected Mode mehr als 4 GByte adressieren. (PAE?) |
| 16 | Der Prozessor unterstützt die Page Attribute Table |
| 15 | Der Prozessor untersützt CMOVcc, und wenn Bit 0 gesetzt ist, dann kann er FCMOVCC und FCOMI |
| 14 | Der Prozessor unterstützt die Machine Check Architecture und MCG_CAP Register |
| 13 | Der Prozessor unterstützt die Page Entry Table, die Page Directory Table und das TLB muss nicht erneuert werden |
| 12 | Der Prozessor unterstützt die Memory Type Range Register, speziell das MTRR_CAP Register |
| 11 | Der Prozessor unterstützt die Fast System Call Befehle, den SYSENTER Befehl und SYSEXIT Befehl |
| 10 | Reserviert |
| 9 | Der Prozessor beinhaltet ein per Softwareansprechbaren [Local APIC](https://github.com/lowlevel-eu/wiki/wiki/Local-Advanced-Programmable-Interrupt-Controller "Local APIC") |
| 8 | Der Prozessor unterstützt das Vergleichen und Verändern von 8-Byte-Befehlen |
| 7 | Der Prozessor unterstützt die Machine Check Exception |
| 6 | Der Prozessor unterstützt Physical Adress Extension |
| 5 | Der Prozessor unterstützt die Model Specific Register, den RDMSR Befehl und den WRMSR Befehl |
| 4 | Der Prozessor unterstützt den RDTSC Befehl, zudem den CR4.TSD-Bit für Rechtekontrolle |
| 3 | Der Prozessor unterstützt 4-Byte-Pages |
| 2 | Der Prozessor unterstützt I/O-Breakpoints, das CR4.DE Bit und die DR4 und DR5 Register |
| 1 | Der Prozessor unterstützt Erweiterungen für den Virtual-8086-Modus |
| 0 | Der Prozessor unterstützt die Intel857-Gleitkommeoperationen |

#### Wenn EAX 2 ist

Wenn in EAX statt Null Zwei steht, dann werden bei Intelprozessoren Informationen über den Cache und die TLB-Deskriptoren ausgegeben.

#### Wenn EAX 3 ist

Wenn in EAX statt Null Drei steht, wird bei Intelprozessoren stattdessen folgendes ausgegeben:

##### EAX

Reserviert

##### EBX

Reserviert

##### ECX

Die Bytes 31 bis 0 der Prozessor-ID sind darin hinterlegt. **Funktioniert nur bei Intelprozessoren, wo das im Featureflag steht. (Tabelle siehe oben)**

##### EDX

Die Bytes 63 bis 32 der Prozessor-ID sind darin hinterlegt. **Funktioniert nur bei Intelprozessoren, wo das im Featureflag steht. (Tabelle siehe oben)**

## Hinweise

Es gibt Befehle, die nur für Intel bzw. AMD Prozessoren verfügbar sind. Solche Befehle sollte man nicht ausführen, wenn man nicht weiß von welchem Hersteller die CPU ist! Zum Beispiel sollten CPUID-Befehle, die nur für Intel-CPUs gelten, nicht auf einer AMD-CPU ausgeführt werden.

## Siehe auch

[Englischer Artikel über den CPUID-Befehl](http://wiki.osdev.org/CPUID)

[Englische Doku von CPUID; mit AMD/INTEL und anderen Prozessoren](http://sandpile.org/ia32/cpuid.htm)

[Intels CPUID-Spezifikation](http://bochs.sourceforge.net/techspec/24161821.pdf)

[AMDs CPUID-Spezifikation](http://www.amd.com/us-en/assets/content_type/white_papers_and_tech_docs/25481.pdf)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/3650/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1739/index.html)

<!-- MediaWiki page 1739; revision 3650; parent 3636; 2008-12-09T17:55:50Z -->
