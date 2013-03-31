# Symmetrisches Multiprozessorsystem

Diese Seite oder Abschnitt ist zwar komplett, es wird aber folgende Verbesserungen gewünscht:  

*Dieser Artikel soll erweitert werden*

Hilf Lowlevel, den Artikel zu verbessern.

Ein **Symmetrisches Multiprozessorsystem** (**SMP**) ist ein System mit einem oder mehreren identischen Prozessoren. Im Gegensatz zu [NUMA](https://github.com/lowlevel-eu/wiki/wiki/Non-Uniform-Memory-Architecture "NUMA")-Systemen sind alle Prozessoren auf gleiche Art und Weise mit dem Hauptspeicher verbunden, d.h. es gibt für keinen Prozessor einen von der Geschwindigkeit her bevorzugten/benachteiligten Speicherbereich im Hauptspeicher.

## Intel Multiprocessor Specification

Die *Intel Multiprocessor Specification* ist ein Standard für [x86](https://github.com/lowlevel-eu/wiki/wiki/X86 "X86")- und [x86-64](https://github.com/lowlevel-eu/wiki/wiki/Long-Mode "Long Mode")-basierte, symmetrische Multiprozessorsysteme und ist abwärtskompatibel mit existierenden [x86](https://github.com/lowlevel-eu/wiki/wiki/X86 "X86")- und [x86-64](https://github.com/lowlevel-eu/wiki/wiki/X86-64 "X86-64")-Uniprozessorsystemen. Die Spezifikation beschreibt einerseits die Anforderungen an die Hardware und das [BIOS](https://github.com/lowlevel-eu/wiki/wiki/Basic-Input-Output-System "BIOS"), und andererseits die Schritte, die notwendig sind, um mit einem [Betriebssystem](https://github.com/lowlevel-eu/wiki/wiki/Betriebssystem "Betriebssystem") den Geschwindigkeitsvorteil mehrerer Prozessoren nutzbar zu machen.

### Unterteilung der Prozessoren

Beim Start eines Intel-basierten Rechners ist ein Prozessor dafür zuständig, alle Initialisierungen vorzunehmen und schließlich ein Betriebssystem zu booten, wie es auch auf Intel-Uniprozessorsystemen der Fall ist. Dieser Prozessor wird *Bootstrap Processor* (BSP) genannt, alle anderen Prozessoren heißen *Application Processors* (AP). Die letzteren werden erst aktiviert, wenn das Betriebssystem startet. Das bedeutet, dass die Unterstützung für SMP im Betriebssystem programmiert sein muss, weil die APs sonst im Ruhezustand bleiben und der Rechner somit nur wie ein Uniprozessor-System genutzt werden kann.

### Floating Pointer Structure

Der erste Schritt dahingehend ist das Auffinden der *Floating Pointer Structure*. Diese Struktur wird vom BIOS erstellt und falls sie existiert ist dieses System zur *Intel Multiprocessor Specification* kompatibel.

#### Aufbau

Die *Floating Pointer Structure* liegt an einer 16-Byte Grenze im Speicher und sieht folgendermaßen aus:

  

![SMPFloatingPointer.png](http://lowlevel.brainsware.org/wiki/images/SMPFloatingPointer.png) *Floating Pointer Structure*

  

| Feld | Beschreibung |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| *Signatur* | Die Signatur enthält die nicht nullterminierte ASCII-Zeichenkette "\_MP\_" |
| *physische Adresse* | Enthält die physische Adresse der [Configuration Table](https://github.com/lowlevel-eu/wiki/wiki/Symmetrisches-Multiprozessorsystem#configuration-table "SMP") oder 0x00000000, falls dieses System einer der [Default Configurations](https://github.com/lowlevel-eu/wiki/wiki/Symmetrisches-Multiprozessorsystem#default-configuration "SMP") entspricht. |
| *Länge* | Die Größe der Struktur in 16-Byte großen Abschnitten. |
| *Revision* | Die Revision der Intel Multiprocessor Specification. Der Wert 0x01 steht für die Version 1.1 und 0x04 für Version 1.4. |
| *Checksum* | siehe [Auffinden der Struktur](https://github.com/lowlevel-eu/wiki/wiki/Symmetrisches-Multiprozessorsystem#auffinden-der-struktur "SMP") |
| *Featurebyte 0* | Der Wert 0x00 gibt an, dass eine [Configuration Table](https://github.com/lowlevel-eu/wiki/wiki/Symmetrisches-Multiprozessorsystem#configuration-table "SMP") vorhanden ist. Jeder andere Wert steht für eine der [Default Configurations](https://github.com/lowlevel-eu/wiki/wiki/Symmetrisches-Multiprozessorsystem#default-configuration "SMP"). |
| *Featurebyte 1* | Bit 0-6: reserviert<br>Bit 7 (IMCRP): Falls dieses Bit gesetzt ist, ist das *IMCR* präsent und der *PIC Mode* implementiert. Andernfalls ist der *Virtual Wire Mode* implementiert. |
| *Featurebyte 2-4* | reserviert |

#### Auffinden der Struktur

Die *Floating Pointer Structure* wird anhand der 4 Signaturbytes und der Checksumme identifiziert. Die Prüfsumme wird berechnet, indem man alle Bytes (inklusive des Feldes *Checksum*) der Struktur aufaddiert. Das Ergebnis dieser Berechnung muss 0x00 sein. Die Struktur befindet sich in mindestens einem der folgenden Speicherbereiche:

- In dem ersten Kilobyte der [Extended BIOS Data Area](https://github.com/lowlevel-eu/wiki/wiki/Extended-BIOS-Data-Area "Extended BIOS Data Area")
- In dem letzten Kilobyte des Hauptspeichers unterhalb der 1MiB Marke (Die Größe des Basisspeichers steht an Offset 0x13 in der [BIOS Data Area](https://github.com/lowlevel-eu/wiki/wiki/BIOS-Data-Area "BIOS Data Area")), wenn die Adresse der Extended BIOS Data Area nicht definiert ist.
- Im Adressraum des BIOS ROM (0xE0000 - 0xFFFFF)

Die Speicherbereiche sind in exakt dieser Reihenfolge zu durchsuchen.

### Configuration Table

### Default Configuration

Default Configurations sind vordefinierte Multiprozessorkonfigurationen für Systeme mit genau zwei Prozessoren.

  

| Featurebyte 0 | Bus | APIC-Typ | Sonstiges |
| --------------- | ------------ | ------------ | ----------------------------------------------- |
| 1 | ISA | 82489DX |  |
| 2 | EISA | 82489DX | IRQ0-Timer und *DMA-Chaining* nicht verfügbar |
| 3 | EISA | 82489DX |  |
| 4 | MCA | 82489DX |  |
| 5 | ISA + PCI | Integrated |  |
| 6 | EISA + PCI | Integrated |  |
| 7 | MCA + PCI | Integrated |  |
| 8-255 | Reserviert |  |  |

## Besonderheiten bei der Programmierung

### Multiprozessorsynchronisation (TSL-Instruktion)

Um auf Uniprozessorsystemen effizient wechselseitigen Ausschluss (Mutex) zu implementieren, wird üblicherweise die *xchg*-Instruktion verwendet (oder passende API-Funktionen wie [InterlockedExchange](http://msdn.microsoft.com/en-us/library/ms683590(VS.85).aspx) unter Windows). Architekturübergreifend wird diese Instruktion als *TSL* (Test and Set Lock) oder auch *TSTS* (Test and Set) bzw. *TAS* (Test and Set) bezeichnet. Dabei liest man mit der Instruktion den alten Wert z.B. in ein Register und schreibt den neuen Wert in den Speicher (z.B. 0 = Mutex verfügbar, 1 = Mutex gelockt). Die Instruktion ist atomar, d.h. kann nicht unterbrochen werden (CPU führt immer ganze Instruktionen aus!). Da Instruktionen *echt* gleichzeitig ausgeführt werden können (anstatt hintereinander bei Uniprozessorsystemen), muss diese Instruktion auf Multiprozessorsystemen ebenfalls atomar sein.

Eine fehlerhafte Mutex-Implementierung mit nicht-atomaren Operationen könnte z.B. so aussehen:

- Der Mutex sei freigegeben (= 0), es kann also ein Prozess in den kritischen Abschnitt eintreten, wenn er den Mutex lockt (d.h. auf 1 setzt)
- Nun wollen zwei Threads/Prozesse, die auf verschiedenen CPUs ausgeführt werden, etwa gleichzeitig den Mutex für sich locken
- Thread \#1 auf CPU \#1 liest die Speicherstelle = 0
- Thread \#2 auf CPU \#2 liest ebenfalls die Speicherstelle = 0
- Thread \#1 auf CPU \#1 überschreibt den Speicher mit 1 und gibt als alten Wert die gelesene 0 zurück
- Thread \#2 auf CPU \#2 überschreibt den Speicher nochmals mit 1 und gibt als alten Wert die gelesene 0 zurück

Nun ist eine [Race Condition](https://github.com/lowlevel-eu/wiki/wiki/Race-Condition "Race Condition") aufgetreten: Beide Threads/Prozesse denken nun, dass der Mutex vorher nicht gelockt war und sie nun als einziger Thread/Prozess im kritischen Bereich arbeiten werden. Ganz offensichtlich arbeiten aber in diesem Beispiel nun beide in dem kritischen Abschnitt.

Aus diesem Grund wird zur Implementierung die TSL-Instruktion verwendet. Sie ist auch auf SMP-Systemen atomar (vgl. [Intel Spezifikation](http://www.intel.com/design/intarch/manuals/243191.htm), S. 3-714), d.h. der sogenannte *lock*-Präfix wird implizit angenommen, wenn bei der *xchg*-Instruktion eine Speicherstelle verwendet wird. Der Präfix kann auch explizit angegeben werden - er bewirkt, dass der Speicherbus während der nächsten Instruktion gesperrt wird.

Ein Beispiel für eine simple 32-Bit-TSL-Funktion: \<asm\>; uint32_t tsl(uint32_t \*ptr, uint32_t newValue) \_tsl:

       push ebx
       mov eax, [esp+12]
       mov ebx, [esp+8]
       xchg eax, [ebx]
       pop ebx
       ret</asm>

## siehe auch

- [APIC](https://github.com/lowlevel-eu/wiki/wiki/Advanced-Programmable-Interrupt-Controller "APIC")
- [I/O APIC](https://github.com/lowlevel-eu/wiki/wiki/I-O-Advanced-Programmable-Interrupt-Controller "I/O APIC")
- [Local APIC](https://github.com/lowlevel-eu/wiki/wiki/Local-Advanced-Programmable-Interrupt-Controller "Local APIC")

## Weblinks

- [Intel Multiprocessor Specification](http://www.intel.com/design/pentium/datashts/242016.htm)
- Kapitel 7 von [Intel® 64 and IA-32 Architectures Software Developer’s Manual](http://www.intel.com/design/processor/manuals/253668.pdf)
- [Bona-Fide-Tutorial "Multiprocessing Support for Hobby OSes Explained"](http://www.osdever.net/tutorials/view/multiprocessing-support-for-hobby-oses-explained)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/11092/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1490/index.html)

<!-- MediaWiki page 1490; revision 11092; parent 11051; 2013-03-31T14:24:24Z -->
