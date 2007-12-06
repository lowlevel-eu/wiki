# Symmetrisches Multiprozessorsystem

Ein **Symmetrisches Multiprozessorsystem** (=**SMP**) ist ein System mit einem oder mehreren identischen Prozessoren. Im Gegensatz zu [NUMA](https://github.com/lowlevel-eu/wiki/wiki/Non-Uniform-Memory-Architecture "NUMA")-Systemen sind alle Prozessoren auf gleiche Art & Weise mit dem Hauptspeicher verbunden, d.h. es gibt für keinen Prozessor einen von der Geschwindigkeit her bevorzugten/benachteiligten Speicherbereich im Hauptspeicher.

## Intel Multiprocessor Specification

Die *Intel Multiprocessor Specification* ist ein Standard für [x86](https://github.com/lowlevel-eu/wiki/wiki/X86 "X86")- und [x86-64](https://github.com/lowlevel-eu/wiki/wiki/X86-64 "X86-64")-basierte, symmetrische Multiprozessorsysteme und ist abwärtskompatibel mit existierenden [x86](https://github.com/lowlevel-eu/wiki/wiki/X86 "X86")- und [x86-64](https://github.com/lowlevel-eu/wiki/wiki/X86-64 "X86-64")-Uniprozessorsystemen. Die Spezifikation beschreibt einerseits die Anforderungen an die Hardware und das [BIOS](https://github.com/lowlevel-eu/wiki/wiki/Basic-Input-Output-System "BIOS") und andererseits die Schritte die notwendig sind, um mit einem [Betriebssystem](https://github.com/lowlevel-eu/wiki/wiki/Betriebssystem "Betriebssystem") den Geschwindigkeitsvorteil mehrerer Prozessoren nutzbar zu machen.

### Floating Pointer Structure

Der erste Schritt dahingehend ist das Auffinden der *Floating Pointer Structure*. Diese Struktur wird vom BIOS erstellt und falls sie existiert ist dieses System zur *Intel Multiprocessor Specification* kompatibel. Diese Struktur sieht wie folgt aus:

![SMPFloatingPointer.png](http://lowlevel.brainsware.org/wiki/images/SMPFloatingPointer.png) *Floating Pointer Structure*

- *Signatur*: Die Signatur enthält die nicht nullterminierte ASCII-Zeichenkette "\_MP\_"
- *physikalische Adresse*: Die physikalische Adresse der [Configuration Table](https://github.com/lowlevel-eu/wiki/wiki/Symmetrisches-Multiprozessorsystem#configuration-table "SMP")
- *Länge*: Die Größe der Struktur in 16-Byte großen Abschnitten.
- *Revision*: Die Revision der Intel Multiprocessor Specification. Der Wert 0x01 steht für die Version 1.1 und 0x04 für Version 1.4.

#### Auffinden der Struktur

Die *Floating Pointer Structure* wird anhand der 4 Signaturbytes und der Checksumme identifiziert. Die Checksumme wird berechnet indem man alle Bytes der Struktur aufaddiert. Das Ergebnis dieser Berechnung muss 0x00 sein. Die Struktur befindet sich in mindestens einem der folgenden Speicherbereiche:

- In dem ersten Kilobyte der [Extended BIOS Data Area](https://github.com/lowlevel-eu/wiki/wiki/Extended-BIOS-Data-Area "Extended BIOS Data Area")
- In dem letzten Kilobyte des Hauptspeichers unterhalb der 1MB Marke
- Im Adressraum des BIOS ROM (0xF0000 - 0xFFFFF)

Die Speicherbereiche sind in exakt dieser Reihenfolge zu durchsuchen. Zu beachten ist außerdem, dass die Struktur an einer 16-byte Grenze beginnen muss.

### Configuration Table

## siehe auch

- [APIC](https://github.com/lowlevel-eu/wiki/wiki/Advanced-Programmable-Interrupt-Controller "APIC")
- [I/O APIC](https://github.com/lowlevel-eu/wiki/wiki/I-O-Advanced-Programmable-Interrupt-Controller "I/O APIC")
- [Local APIC](https://github.com/lowlevel-eu/wiki/wiki/Local-Advanced-Programmable-Interrupt-Controller "Local APIC")

## Weblinks

- [Intel Multiprocessor Specification](http://www.intel.com/design/pentium/datashts/242016.htm)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/2347/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1490/index.html)

<!-- MediaWiki page 1490; revision 2347; parent 2346; 2007-12-06T20:57:29Z -->
