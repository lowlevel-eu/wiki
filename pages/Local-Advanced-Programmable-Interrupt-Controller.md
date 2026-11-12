# Local Advanced Programmable Interrupt Controller

Der **LAPIC** oder **Local APIC** (= **Local Advanced Programmable Interrupt Controller**) nimmt [Interrupts](Interrupt.md "Interrupt") vom [I/O APIC](I-O-Advanced-Programmable-Interrupt-Controller.md "I/O APIC") (oder auch vom [PIC](Programmable-Interrupt-Controller.md "PIC")) und anderen prozessorinternen Einheiten an und leitet diese an den Prozessorkern zum Abarbeiten weiter. Außerdem ist es nur über den LAPIC möglich [IPIs](Interprocessor-Interrupt.md "IPI") zu senden und zu empfangen.

## Register

### Aufbau

Die Register des *Local APIC* sind in den physischen Speicher eingeblendet. Jedes der Register beginnt an einer 16 Byte Grenze, erstreckt sich aber nur über die ersten 32 Bit. Falls das Register größer als 32 Bit ist, befinden sich die nächst höheren 32 Bit an der nächst höheren 16 Byte Grenze. Der *Local APIC* stellt folgende Register zur Programmierung bereit:

  

| Offset | r/w | Größe (Bit) | Abkürzung | Name des Registers |
| ------------------ | ----- | ------------- | ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0x0020 | r/w | 32 |  | [Local APIC ID Register](Local-Advanced-Programmable-Interrupt-Controller.md#local-apic-id-register "LAPIC") |
| 0x0030 | r | 32 |  | [Local APIC Version Register](Local-Advanced-Programmable-Interrupt-Controller.md#local-apic-version-register "LAPIC") |
| 0x0080 | r/w | 32 | TPR | Task Priority Register |
| 0x0090 | r | 32 | APR | Arbitration Priority Register ¹ |
| 0x00A0 | r | 32 | PPR | Processor Priority Register |
| 0x00B0 | w | 32 |  | EOI Register |
| 0x00D0 | r/w | 32 |  | Logical Destination Register |
| 0x00E0 | r/w | 32 |  | Destination Format Register |
| 0x00F0 | r/w | 32 |  | Spurious Interrupt Vector Register |
| 0x0100<br>0x0170 | r | 256 | ISR | In-Service Register |
| 0x0180<br>0x01F0 | r | 256 | TMR | Trigger Mode Register |
| 0x0200<br>0x0270 | r | 256 | IRR | Interrupt Request Register |
| 0x0280 | r | 32 |  | Error Status Register |
| 0x0300<br>0x0310 | r/w | 64 | ICR | [Interrupt Command Register](Local-Advanced-Programmable-Interrupt-Controller.md "LAPIC") |
| 0x0320 | r/w | 32 |  | LVT Timer Register |
| 0x0330 | r/w | 32 |  | LVT Thermal Sensor Register ² |
| 0x0340 | r/w | 32 |  | LVT Performance Monitoring Counters Register ³ |
| 0x0350 | r/w | 32 |  | LVT LINT0 Register |
| 0x0360 | r/w | 32 |  | LVT LINT1 Register |
| 0x0370 | r/w | 32 |  | LVT Error Register |
| 0x0380 | r/w | 32 |  | Initial Count Register |
| 0x0390 | r | 32 |  | Current Count Register |
| 0x03E0 | r/w | 32 |  | Divide Configuration Register |

  
¹ Nicht unterstützt in Pentium 4 und Intel Xeon Prozessoren  
² Eingeführt mit dem Pentium 4 und Intel Xeon Prozessoren. Dieses Register ist implementationsabhängig und muss in Zukunft nicht mehr vorhanden sein.  
³ Eingeführt mit dem Pentium Pro Prozessor. Dieses Register ist implementationsabhängig und muss in Zukunft nicht mehr vorhanden sein.  

### Local APIC ID Register

P6-Prozessorfamilie und Pentium-Prozessoren:

| 31-28 | 27-24 | 23-0 |
| ------------ | --------------- | ------------ |
| Reserviert | Local APIC ID | Reserviert |

Pentium4, IntelXeon und spätere Prozessoren:

| 31-24 | 23-0 |
| --------------- | ------------ |
| Local APIC ID | Reserviert |

  

### Local APIC Version Register

| 31-24 | 23-16 | 15-8 | 7-0 |
| ------------ | ------------------- | ------------ | --------- |
| Reserviert | Max. LVT-Einträge | Reserviert | Version |

Wenn beim Version-Byte das HighNibble 1 ist, ist es ein Local APIC. Andernfalls ein externer APIC. Bei Pentium 4 und Intel Xeon wird als LocalApic 0x14 zurückgegeben. Bei einem externen APIC entspricht das LowNibble X dem Chip 82489DX.

Das Feld "Max. LVT-Einträge" gibt die Anzahl an maximalen LVT-Einträgen minus 1 an. Das Feld muss bei Pentium 4 und Intel Xeon also auf 5 gesetzt sein, da es maximal 6 LVT-Einträge gibt. Bei der P6-Familie gibt es maximal 5 LVT-Einträge. Pentium-Prozessoren haben nur 4 LVT-Einträge.  

### Interrupt Command Register (ICR)

Das Interrupt Command Register wird verwendet um IPIs zu versenden.

| Bits | Beschreibung |
| ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 63-56 | Destination Field |
| 55-20 | Reserviert |
| 19-18 | Destination Shorthand<br>00b = No shorthand<br>01b = Self<br>10b = All Including Self<br>11b = All excluding Self |
| 17-16 | Reserviert |
| 15 | Trigger Mode<br>0b = Edge<br>1b = Level |
| 14 | Level<br>0b = De-Assert<br>1b = Assert |
| 13 | Reserviert |
| 12 | Delivery Status<br>0b = Idle<br>1b = Send Pending |
| 11 | Destination Mode<br>0b = Physical<br>1b = Logical |
| 10-8 | Delivery Mode<br>000b = Fixed<br>001b = Lowest Priority<br>010b = SMI<br>011b = Reserviert<br>100b = NMI<br>101b = INIT<br>110b = Startup<br>111b = Reserviert |
| 7-0 | Vector |

## Programmierung

### physische Adresse

Die physische Adresse der Register kann entweder aus der [Configuration Table](Symmetrisches-Multiprozessorsystem.md#configuration-table "SMP") der *Intel Multiprocessor Specification* oder über das [MSR](Machine-Specific-Register.md "MSR") 0x001B ausgelesen werden.

### Initialisierung

Zuerstmal muss man den *Local APIC* über das *Spurious Interrupt Vector Register* aktivieren (und natürlich den Spurious Interrupt Vector setzten). Anschließend sind noch folgende Register zu initialisieren:

- *Task Priority Register*
- *LVT Timer Register*
- *LVT Thermal Sensor Register*
- *LVT Performance Counter Register*
- *LVT LINT0 Register*
- *LVT LINT1 Register*
- *LVT Error Register*

### Bug beim Beschreiben der Register

Bei Pentium Prozessoren mit einer Geschwindigkeit über 75 MHz aus der Prozessor-Familie 5 mit der Modellnummer 2 und der Revisionsnummer (Stepping) 1,2,3,4 oder 11 wird jegliches einfache Schreiben in LAPIC Register ignoriert. Um dies zu verhindern, muss vor einem Schreibzugriff auf den APIC zuerst etwas daraus ausgelesen werden.

### End of Interrupt

Ein *End of Interrupt* (EOI) wird dem *Local APIC* signalisiert, in dem man in das *EOI Register* den Wert 0 schreibt.

## Timer

Der *Local APIC* besitzt einen sehr genauen Timer, welcher eigentlich allen anderen Timern wie dem [PIT](Programmable-Interval-Timer.md "PIT") oder der Real-time Clock vorgezogen werden sollte. Wenn das System mit mehreren Prozessoren (siehe auch [SMP](Symmetrisches-Multiprozessorsystem.md "SMP")) oder mit dem [I/O APIC](I-O-Advanced-Programmable-Interrupt-Controller.md "I/O APIC") (Symmetric Mode) läuft, dann ist er eigentlich die einzige Wahl, denn der PIT ist meistens nur mit dem PIC verbunden und damit nur an den [BSP](Symmetrisches-Multiprozessorsystem.md#unterteilung-der-prozessoren "Symmetrisches Multiprozessorsystem") angeschlossen. Er kann somit nicht effizient für SMP verwendet werden.

### Register

Der Timer des APIC wird über das LVT Timer Register (0x320), das Initial Count Register (0x380), das Current Count Register (0x390 - nur Lesezugriff) sowie das Divide Configuration Register (0x3E0) angesprochen.

#### Das LVT Timer Register:

| 31-18 | 17 | 16 | 15-13 | 12 | 11-8 | 7-0 |
| ------------ | ------------- | ------------ | ------------ | ------------ | ------------ | -------- |
| Reserviert | Timer Modus | Maskierung | Reserviert | Zustellung | Reserviert | Vektor |

- Wenn das Timer Modus Bit gesetzt ist, arbeitet der Timer periodisch. Ansonsten wird der Interrupt nur ein einzige Mal aufgerufen.
- Das Maskierungsbit ist standardmäßig gesetzt und verhindert somit das Erzeugen eines Interrupts.
- Auf das Zustellungsbit kann nur lesend zugegriffen werden. Wenn es gesetzt ist, wird gerade ein Interrupt gesendet, ansonsten wird nicht gearbeitet.
- Der Vektor beinhaltet die Interruptnummer, mit welcher der Timer-Interrupt zur CPU gesendet werden soll. Dort wird der Interrupt dann zu einer ISR geleitet, welche durch diesen Vektor in der IDT ausgewählt wird.

#### Das Divide Configuration Register:

| 31-4 | 3 | 2 | 1-0 |
| ------------ | ------------------------------- | ----- | ---------------------------------- |
| Reserviert | höchstes Bit des Divide Value | 0 | niedrige 2 Bits des Divide Value |

Wenn man zum Divide Value eine Eins addiert, erhält man den Exponenten der Zweierpotenz, welche dann den Divisor bildet. Ausnahme: Sind alle 3 Bits gesetzt ist der Divisor 1. Da die Funktion dieser Division nicht spezifiziert ist, sollte man sie auch nicht verwenden und einfach durch 1 dividieren. Das gäbe demnach eine Wertzuweisung von 0xb in das Divide Configuration Register (Man beachte die Teilung des Divide Value im Register).

#### Initial und Current Count Regsiter:

Der Wert im Current Count Regsiter wird in der Frequenz des Timers immer um Eins dekrementiert. Sobald der Wert Null erreicht, wird ein Interrupt ausgelöst, das Current Count Register wird, sofern mehr als ein Interrupt generiert werden soll, wieder mit dem Wert des Initial Count Register gefüllt und beginnt somit wieder mit dem stufenweisen dekrementieren.

### Aktivierung

Der Timer wird durch setzen des Divide Configuration Regsisters, des LVT-Timer Registers und des Initial Count Registers aktiviert. Das muss genau in dieser Reihenfolge geschehen. Auch wenn der Timer schon aktiviert ist und der Wert eines der Register geändert werden soll, sollte man immer alle 3 Register in der richtigen Reihenfolge beschreiben, wenn man will, dass die Änderungen wirksam werden.

### Frequenz

Der Timer des LAPIC läuft jedoch nicht auf allen Systemen mit der selben Frequenz, da diese abhängig vom CPU Bus ist. Deshalb muss man die Frequenz des Timers mit Hilfe der anderen Timer bestimmen. Je mehr man davon verwendet, desto besser kann man die Frequenz des LAPIC Timer bestimmen und hat einen extrem genauen Timer. Am einfachsten ist es jedoch ohne zuerst die Frequenz und damit dann wieder einen Initial Count Value auszurechnen nur durch Auslesen des Current Count Value einen passenden Initial Count Value zu bestimmen. Das heisst, man kann den APIC Timer zusammen mit dem PIT laufen lassen. Sobald dann der PIT den nächsten Interrupt produziert, kann man nur noch den Current Count Value des APIC Timers auslesen und weiss dann, wie man den Initial Count Value einstellen muss.

#### Codebeispiel:

Dieser Code gehört in den anderen Init-Code für den APIC / Symmetric Mode. Er stellt den PIT auf den gewünschten Wert für den APIC Timer ein (hier 10ms), lässt die ISR des PITs den nötigen Wert für den Initial Count Value des APIC Timers berechnen und stellt diesen dann zugleich ein. Er setzt voraus, dass in der Variable \[apicregs\] die Adresse der APIC Register gespeichert ist. \<asm\> xor ebp,ebp  ;EBP nullen, damit nachher in PIT-ISR erkenbar, wie oft der Timer-Interrupt aufgerufen wurde

       mov al,00110110b        ;den PIT auf den gewünschten Wert (hier 10ms) einstellen
       out 43h,al
       
       mov ax,11931
       out 40h,al
       mov al,ah
       out 40h,al

       sti                ;IRQs freigeben

timerschleife:  ;Solange Warten, bis das Einschalten und Messen des APIC Timers sicher fertig ist

       cmp ebp,0x3            ;Die Zählvariable hat dann den Wert 3
       jne timerschleife
       cli

       mov eax,[apicregs]        ;Den zuvor ermittelten Platz der APIC Register laden                            
       mov ecx,DWORD[apiczähler]    ;Den Gemessenen Wert für den Initial Count des APIC Timers nach ECX laden

       mov ebp,[eax+0x3e0]        ;Alle Register des APIC Timers neu schreiben, um den neuen Initial Count einzustellen
       mov DWORD[eax+0x3e0],0xb

       mov ebp,[eax+0x320]        ;Zuerst irgendein Register lesen, wegen Bug in manchem APICS
       mov DWORD[eax+0x320],0x20031

       mov ebp,[eax+0x380]        ;Nach Lesen eines Wertes, den neuen Wert des Zählers aus ECX ins Initial Count Register schreiben
       mov [eax+0x380],ecx</asm>

  
Dieser Code muss als ISR des PITs eingetragen sein. Er kümmert sich zuerst um das Starten des APIC Timers und in einem zweiten Durchgang das Ablesen des heruntergezählten Wertes im Current Count Register. Er setzt voraus, dass in der Variable \[apicregs\] die Adresse der APIC Register gespeichert ist. \<asm\>APICkalibrieren:

       inc ebp                ;Variable um zwischen Einschalten und Messen (des Current Count) des APIC Timers zu unterscheiden 
       mov eax,[apicregs]        ;Den zuvor ermittelten Platz der APIC Register laden    

       cmp ebp,0x1
       jne ApicSchonGestartet

  

       mov edx,[eax+0x3e0]        ;Zuerst irgendein Wert auslesen, dannach Divide Configuration Register auf Divide Value = 1 setzen
       mov DWORD[eax+0x3e0],0xb

       mov edx,[eax+0x320]        ;Zuerst Wert auslesen, dannach LVT-Timer Register setzen (peridischer Timer auf Vektor 31)
       mov DWORD[eax+0x320],0x20031

       mov edx,[eax+0x380]        ;Initial Count Register auf das Maximum setzen --> möglichst viel Werte zum Kalibrieren möglich
       mov DWORD[eax+0x380],0xFFFFFFFF
       
       jmp schlussKalib

  
ApicSchonGestartet:

       cmp ebp,0x3            ;Wenn der Timer schon zum 3. Mal ausgelöst, muss nichts mehr getan werden
       je schlussKalib

                       ;Wenn Timer schon gestartet wurde, dann wird jetzt das Current Count Register gemessen
       mov ecx,0xFFFFFFFF        ;Unterschied des Current Count in der Zeit des PITs ausrechnen
       sub ecx,[eax+0x390]
       mov DWORD[apiczähler],ecx
       

schlussKalib:

       mov al,20h            ;EOI senden an den PIC, da dieser verwendet wurde zum Kalibrieren
              out 20h,al
       
       iret</asm>

## Weblinks

- [Intel® 64 and IA-32 Architectures Software Developer's Manual Volume 3A: System Programming Guide](http://www.intel.com/products/processor/manuals/index.htm) (Kapitel 8)
- [AMD64 Architecture Programmer's Manual Volume 2: System Programming](http://www.amd.com/us-en/Processors/DevelopWithAMD/0,,30_2252_739_7044,00.html) (Kapitel 16)
- [Advanced Programmable Interrupt Controller](http://osdev.berlios.de/pic.html) (Tutorial von Mike Rieker)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/11142/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1581/index.html)

<!-- MediaWiki page 1581; revision 11142; parent 10375; 2013-09-08T23:59:30Z -->
