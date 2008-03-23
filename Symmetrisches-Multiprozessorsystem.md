# Symmetrisches Multiprozessorsystem

Ein **Symmetrisches Multiprozessorsystem** (=**SMP**) ist ein System mit einem oder mehreren identischen Prozessoren. Im Gegensatz zu [NUMA](https://github.com/lowlevel-eu/wiki/wiki/Non-Uniform-Memory-Architecture "NUMA")-Systemen sind alle Prozessoren auf gleiche Art & Weise mit dem Hauptspeicher verbunden, d.h. es gibt für keinen Prozessor einen von der Geschwindigkeit her bevorzugten/benachteiligten Speicherbereich im Hauptspeicher.

## Intel Multiprocessor Specification

Die *Intel Multiprocessor Specification* ist ein Standard für [x86](https://github.com/lowlevel-eu/wiki/wiki/X86 "X86")- und [x86-64](https://github.com/lowlevel-eu/wiki/wiki/X86-64 "X86-64")-basierte, symmetrische Multiprozessorsysteme und ist abwärtskompatibel mit existierenden [x86](https://github.com/lowlevel-eu/wiki/wiki/X86 "X86")- und [x86-64](https://github.com/lowlevel-eu/wiki/wiki/X86-64 "X86-64")-Uniprozessorsystemen. Die Spezifikation beschreibt einerseits die Anforderungen an die Hardware und das [BIOS](https://github.com/lowlevel-eu/wiki/wiki/Basic-Input-Output-System "BIOS") und andererseits die Schritte die notwendig sind, um mit einem [Betriebssystem](https://github.com/lowlevel-eu/wiki/wiki/Betriebssystem "Betriebssystem") den Geschwindigkeitsvorteil mehrerer Prozessoren nutzbar zu machen.

### Floating Pointer Structure

Der erste Schritt dahingehend ist das Auffinden der *Floating Pointer Structure*. Diese Struktur wird vom BIOS erstellt und falls sie existiert ist dieses System zur *Intel Multiprocessor Specification* kompatibel.

#### Aufbau

Die *Floating Pointer Structure* liegt an einer 16-Byte Grenze im Speicher und sieht folgendermaßen aus:

  

![SMPFloatingPointer.png](http://lowlevel.brainsware.org/wiki/images/SMPFloatingPointer.png) *Floating Pointer Structure*

  

| Feld | Beschreibung |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| *Signatur* | Die Signatur enthält die nicht nullterminierte ASCII-Zeichenkette "\_MP\_" |
| *physikalische Adresse* | Enthält die physikalische Adresse der [Configuration Table](https://github.com/lowlevel-eu/wiki/wiki/Symmetrisches-Multiprozessorsystem#configuration-table "SMP") oder 0x00000000, falls dieses System einer der [Default Configurations](https://github.com/lowlevel-eu/wiki/wiki/Symmetrisches-Multiprozessorsystem#default-configuration "SMP") entspricht. |
| *Länge* | Die Größe der Struktur in 16-Byte großen Abschnitten. |
| *Revision* | Die Revision der Intel Multiprocessor Specification. Der Wert 0x01 steht für die Version 1.1 und 0x04 für Version 1.4. |
| *Checksum* | siehe [Auffinden der Struktur](https://github.com/lowlevel-eu/wiki/wiki/Symmetrisches-Multiprozessorsystem#auffinden-der-struktur "SMP") |
| *Featurebyte 0* | Der Wert 0x00 gibt an, dass eine [Configuration Table](https://github.com/lowlevel-eu/wiki/wiki/Symmetrisches-Multiprozessorsystem#configuration-table "SMP") vorhanden ist. Jeder andere Wert steht für eine der [Default Configurations](https://github.com/lowlevel-eu/wiki/wiki/Symmetrisches-Multiprozessorsystem#default-configuration "SMP"). |
| *Featurebyte 1* | Bit 0-6: reserviert<br>Bit 7 (IMCRP): Falls dieses Bit gesetzt ist, ist das *IMCR* präsent und der *PIC Mode* implementiert. Andernfalls ist der *Virtual Wire Mode* implementiert. |
| *Featurebyte 2-4* | reserviert |

#### Auffinden der Struktur

Die *Floating Pointer Structure* wird anhand der 4 Signaturbytes und der Checksumme identifiziert. Die Prüfsumme wird berechnet indem man alle Bytes (inklusive des Feldes *Checksum*) der Struktur aufaddiert. Das Ergebnis dieser Berechnung muss 0x00 sein. Die Struktur befindet sich in mindestens einem der folgenden Speicherbereiche:

- In dem ersten Kilobyte der [Extended BIOS Data Area](https://github.com/lowlevel-eu/wiki/wiki/Extended-BIOS-Data-Area "Extended BIOS Data Area")
- In dem letzten Kilobyte des Hauptspeichers unterhalb der 1MB Marke (Die Größe des Basisspeichers steht an Offset 0x13 in der [BIOS Data Area](https://github.com/lowlevel-eu/wiki/wiki/BIOS-Data-Area "BIOS Data Area"))
- Im Adressraum des BIOS ROM (0xF0000 - 0xFFFFF)

Die Speicherbereiche sind in exakt dieser Reihenfolge zu durchsuchen.

### Configuration Table

### Default Configuration

## siehe auch

- [APIC](https://github.com/lowlevel-eu/wiki/wiki/Advanced-Programmable-Interrupt-Controller "APIC")
- [I/O APIC](https://github.com/lowlevel-eu/wiki/wiki/I-O-Advanced-Programmable-Interrupt-Controller "I/O APIC")
- [Local APIC](https://github.com/lowlevel-eu/wiki/wiki/Local-Advanced-Programmable-Interrupt-Controller "Local APIC")

## Weblinks

- [Intel Multiprocessor Specification](http://www.intel.com/design/pentium/datashts/242016.htm)
- Kapitel 7 von [Intel® 64 and IA-32 Architectures Software Developer’s Manual](http://www.intel.com/design/processor/manuals/253668.pdf)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/2781/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1490/index.html)

<!-- MediaWiki page 1490; revision 2781; parent 2743; 2008-03-23T01:21:35Z -->
