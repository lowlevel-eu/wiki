# Long Mode

Der **Long Mode** ist ein CPU-Modus neuerer CPUs, in dem erstmals [64-Bit-Allzweckregister](Register "Register") zur Verfügung stehen. Wie auch beim [Protected Mode](Protected-Mode "Protected Mode") starten Prozessoren, die diesen Modus unterstützen, aus Kompatibilitätsgründen zunächst im [Real Mode](Real-Mode "Real Mode") mit deaktiviertem [A20-Gate](A20-Gate "A20-Gate").

## Eigenschaften

- Address-/Registerbreite beträgt 64 Bit
- Viele neue Register (z.B. R8-R15, CR8-CR15, ...)
- ...

## Überprüfung der Unterstützung

CPUs, die den Long Mode unterstützen, setzen bei einem Aufruf der [CPUID Funktion 0x80000001](CPUID#funktion-0x8000_0001 "CPUID") das [Long-Mode-Capable-Bit (Bit 29)](CPUID#edx---erweiterte-featureflags "CPUID") im EDX-Register auf 1. Sicherheitshalber sollte man auch noch überprüfen, ob [Physical Address Extensions](Physical-Address-Extension "Physical Address Extension") unterstützt werden.

``` asm
mov eax, 0x80000001
cpuid                 ; CPUID Funktion 0x8000_0001 aufrufen
and edx, 0x20000000   ; LM-Bit isolieren
test edx, edx         ; Wenn EDX jetzt 0 ist, war das LM-Bit nicht gesetzt
jz long_unsupported   ; Long Mode nicht unterstützt!

mov eax, 0x00000001
cpuid                 ; CPUID Funktion 0x0000_0001 aufrufen
and edx, 0x00000040   ; PAE-Bit isolieren
test edx, edx         ; Wenn EDX jetzt 0 ist, war das PAE-Bit nicht gesetzt
jz long_unsupported   ; Long Mode nicht unterstützt!
jmp long_supported    ; Long Mode unterstützt!
```

## Aktivierung des Long Mode

Um in den Long Mode umschalten zu können, muss erst einmal der [Protected Mode](Protected-Mode "Protected Mode") aktiviert werden. Eine weitere Voraussetzung ist, dass das **[Physical Address Extension](Physical-Address-Extension "Physical Address Extension")**-Bit (Bit 5) im [CR4](Control-Register#cr4 "Control Register") Register gesetzt und **[Paging](Paging "Paging")** aktiviert ist. Jetzt kann der Long Mode mit dem Setzen des LME-Bits (Bit 8) im **MSR 0xC0000080** aktiviert werden. Im eigentlichen Long Mode befindet man sich aber erst, wenn man in ein 64-Bit-Code-Segment wechselt, das im Vergleich zu den 32-Bit-Code-Segmenten in seinem Descriptor das L-Bit (Bit 21) im 2. DWord gesetzt hat. Die entsprechenden Einträge in der [GDT](Global-Descriptor-Table "Global Descriptor Table") sind natürlich vorher vorzunehmen.

**Achtung!**

Das Paging funktioniert im Long Mode ein wenig anders als im Protected Mode.

Dieser Beispielcode zeigt beispielhaft, wie man denn Long Mode aktiviert. Die hier verwendeten Pagingstrukturen sind nur provisorisch angedacht und sollten möglichst durch eigene ersetzt werden, sonst wird das Ganze ganz schnell nicht mehr ganz so schön.

``` asm
mov eax, cr4            ; CR4 einlesen
or eax, 0x20            ; Physical Address Extension-Bit setzen
mov cr4, eax            ; CR4 beschreiben

mov edi, 0x300000       ; Pagingstrukturen liegen bei 0x300000

mov eax, 0x30100F       ; Eintrag für die Page Directory Pointer Table
stosd
mov ecx, 0x03FF
xor eax, eax
rep stosd               ; Rest mit Nullen auffüllen

mov eax, 0x30200F       ; Eintrag für die Page Directory Table
stosd
mov ecx, 0x03FF
xor eax, eax
rep stosd               ; Rest mit Nullen auffüllen

mov ecx, 0x0200
mov esi, 0x008B         ; Die Attribute für die Einträge im Page Directory

map.loop:               ; Hier werden die ersten 512 MiB Identity-Mapped
mov eax, esi            ; Page eintragen
stosd
xor eax, eax            ; Jeder Eintrag besteht aus 8 Byte, also die oberen 4 auffüllen
stosd
add esi, 0x200000       ; Wir benutzen hier 2 MiB Pages
sub ecx, 1
jnz map.loop

mov eax, 0x300000       ; Die Adresse des Page Map Level 4 hier eintragen
mov cr3, eax

mov ecx, 0xC0000080     ; Wir brauchen Zugriff aus das MSR-Register 0xC0000080
rdmsr                   ; MSR-Register einlesen
or eax, 0x00000100  ; Long Mode einschalten
wrmsr                   ; MSR-Register beschreiben

mov eax, cr0            ; CR0 einlesen
or eax, 0x80000000      ; Das Paging-Bit setzen
mov cr0, eax            ; CR0 beschreiben, ab jetzt sind wir im Long Mode

jmp 0x30:kernel.longmode; Far Jmp in 64-Bit Code Segment


[bits 64]
kernel.longmode:    ; Jetzt führen wir auch endlich 64-Bit Code aus
jmp $                   ; Endlosschleife xD
```

## Links

- <http://www.sandpile.org/aa64/index.htm>

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/11382/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1666/index.html)

<!-- MediaWiki page 1666; revision 11382; parent 9850; 2018-07-29T19:35:37Z -->
