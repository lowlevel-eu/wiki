# CPUID

Der CPUID Befehl wird benutzt, um Informationen über die Fähigkeiten eines Prozessors zu erhalten. (Wie zum Beispiel den Herstellernamen, Modelnummer, die Größe des Cache ...)

## Wie man CPUID benutzt

Um den CPUID-Befehl auszuführen, schreibt man einfach den ASM-Befehl CPUID in den Code. Die Parameter werden dabei im Register EAX angegeben. Um z.B. den Vendor-ID-String (Herstellername) zu bekommen, ruft man CPUID mit dem Parameter 0x0 in EAX auf.

    mov eax, 0x0
    cpuid

Natürlich gibt der CPUID-Befehl auch ein Ergebnis zurück. In diesem Fall gibt er einen String zurück, dessen ASCII-Werte in EBX, EDX und ECX liegen. Wenn man den Inhalt dieser drei Register (in dieser Reihenfolge!) hintereinander in den Speicher schreibt, erhält man einen String, die Vendor-ID. Jeder Hersteller hat eigene Vendor-ID. **Achtung: Der String ist nicht nullterminiert !**

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

Wenn im EAX statt Null eine Eins vorkommt, dann wird bei Intelprozessoren in EAX folgendes ausgegeben:

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

Hier soll ein Bytearray sein, aber es wird nicht empfohlen, was daraus zu lesen. Dieses Feld ist ein kommendes Feature. Zudem ist es reserviert.

##### EDX

Dies sind Featureflags. Wenn das Bit eins, wird das Feature unterstüzt.

| Bit | Funktion |
| --------- | ----------------------------------------------------------------------------------------------------------------------- |
| 31 - 30 | Reserviert |
| 29 | Wenn eins, dann wird das Thermal Monitor unterstützt. |
| 28 | Der Prozessor könnte Hyper-Threading. Wenn in EBX ein Wert größer als 1 ist, dann wird Hyper-Threading unterstützt. |
| 27 | Der Prozessor unterstützt Self-Snoop. |
| 26 | Der Prozessor kann SSE2. |
| 25 | Der Prozessor kann SSE. |
| 24 | Der Prozessor unterstützt FXSAVE und FXSTOR, womit er einen Floatzusammenhang(?) speichern und wiederherstellen kann. |
| 23 | Der Prozessor kann MMX. |
| 22 | Der Prozessor kann die Temperatur und den Prozessortakt durch eine Software verändert und überwacht werden. |
| 21 | Der Prozessor hat die Fähigkeit, die Entwicklung eines Ablegers in eine Adresse zu schreiben. |
| 20 | Reserviert |
| 19 | Der Prozessor kann CSFLUSH. |
| 18 | Der 12-Byte ProzessorID ist aktiviert und vorhanden |
| 17 | Der Prozessor kann im Protected Mode mehr als 4 GByte adressieren. (Fachbegriff bitte ergänzen) |
| 16 | Der Prozessor unterstützt die Page Atribut Table |
| 15 | Der Prozessor untersützt CMOVcc, und wenn Bit 0 gesetzt ist, dann kann er FCMOVCC und FCOMI. |
| 14 | Der Prozessor unterstützt die Machine Check Archikture und MCG_CAP Register |
| 13 | Der Prozessor unterstützt die Page Entry Table, die Page Directonery Table und das TLB muss nicht erneuert werden. |

WIrd noch erweiter

## Hinweise

Es gibt Befehle, die nur für Intel bzw. AMD Prozessoren verfügbar sind. Solche Befehle sollte man nicht ausführen, wenn man nicht weiß von welchem Hersteller die CPU ist! Z.B. sollten CPUID-Befehle, die nur für Intel-CPU´s gelten, nicht auf einer AMD-CPU ausgeführt werden.

## Siehe auch

[Englischer Artikel über den CPUID-Befehl](http://wiki.osdev.org/CPUID)

[Englische Doku von CPUID; mit AMD/INTEL und anderen Prozessoren](http://sandpile.org/ia32/cpuid.htm)

[Intels CPUID-Spezifikation](http://bochs.sourceforge.net/techspec/24161821.pdf)

[AMDs CPUID-Spezifikation](http://www.amd.com/us-en/assets/content_type/white_papers_and_tech_docs/25481.pdf)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/3620/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1739/index.html)

<!-- MediaWiki page 1739; revision 3620; parent 3618; 2008-12-08T19:06:19Z -->
