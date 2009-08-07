# Long Mode

**Achtung!**

Der Artikel wird zur Zeit bearbeitet. Bitte bearbeite diesen Artikel nicht! Es kann zu Darstellungsproblemen während des Betrachtens des Artikels kommen. [SHyx0rmZ](https://lowlevel-eu.github.io/wiki/pages/1785/index.html "Benutzer:SHyx0rmZ") 12:14, 7. Aug. 2009 (CEST)

Der **Long Mode** ist ein CPU-Modus neuerer CPUs, in dem erstmals 64-Bit-Allzweckregister zur Verfügung stehen. Wie auch beim [Protected Mode](https://github.com/lowlevel-eu/wiki/wiki/Protected-Mode "Protected Mode") starten Prozessoren, die diesen Modus unterstützen, aus Kompatibilitätsgründen zunächst im [Real Mode](https://github.com/lowlevel-eu/wiki/wiki/Real-Mode "Real Mode") mit deaktiviertem [A20-Gate](https://github.com/lowlevel-eu/wiki/wiki/A20-Gate "A20-Gate").

## Eigenschaften

- Address-/Registerbreite beträgt 64 Bit
- Viele neue Register (z.B. R8-R15, CR8-CR15, ...)
- ...

## Wie überprüfe ich, ob die CPU den Long Mode unterstützt?

CPUs, die den Long Mode unterstützen, setzen bei einem Aufruf der [CPUID Funktion 0x80000001](https://github.com/lowlevel-eu/wiki/wiki/CPUID#funktion-0x8000_0001 "CPUID") das [Long-Mode-Capable-Bit (Bit 29)](https://github.com/lowlevel-eu/wiki/wiki/CPUID#edx---erweiterte-featureflags "CPUID") im EDX-Register auf 1. Sicherheitshalber sollte man auch noch überprüfen, [Physical Address Extensions](https://github.com/lowlevel-eu/wiki/wiki/Physical-Address-Extension "Physical Address Extension") unterstützt werden.

\<asm\> mov eax, 0x80000001 cpuid  ; CPUID Funktion 0x8000_0001 aufrufen and edx, 0x20000000  ; LM-Bit isolieren test edx, edx  ; Wenn EDX jetzt 0 ist, war das LM-Bit nicht gesetzt jz long_unsupported  ; Long Mode nicht unterstützt!

mov eax, 0x00000001 cpuid  ; CPUID Funktion 0x0000_0001 aufrufen and edx, 0x00000040  ; PAE-Bit isolieren test edx, edx  ; Wenn EDX jetzt 0 ist, war das PAE-Bit nicht gesetzt jz long_unsupported  ; Long Mode nicht unterstützt! jmp long_supported  ; Long Mode unterstützt! \</asm\>

## Wie schalte ich den Long Mode um?

Um in den Long Mode umschalten zu können, muss erst einmal der [Protected Mode](https://github.com/lowlevel-eu/wiki/wiki/Protected-Mode "Protected Mode") aktiviert werden ([Es geht auch anders](https://github.com/lowlevel-eu/wiki/wiki/Long-Mode "Long Mode")). Eine weitere Voraussetzung ist, dass das **[Physical Address Extension](https://github.com/lowlevel-eu/wiki/wiki/Physical-Address-Extension "Physical Address Extension")**-Bit (Bit 5) im [CR4](https://github.com/lowlevel-eu/wiki/wiki/Control-Register#cr4 "Control Register") Register gesetzt und **[Paging](https://github.com/lowlevel-eu/wiki/wiki/Paging "Paging")** aktiviert ist. Jetzt kann der Long Mode mit dem Setzen des LME-Bits (Bit 8) im **MSR 0xC00000080** aktiviert werden. Im eigentlichen Long Mode befindet man sich aber erst, wenn man in ein 64-Bit-Code-Segment wechselt, das im Vergleich zu den 32-Bit-Code-Segmenten in seinem Descriptor das L-Bit (Bit 21) im 2. DWord gesetzt hat.

**Achtung!**

Das Paging funktioniert im Long Mode ein wenig anders als im Protected Mode.

## Links

- <http://www.osdev.org/wiki/X86-64>
- <http://www.sandpile.org/aa64/index.htm>

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/5432/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1666/index.html)

<!-- MediaWiki page 1666; revision 5432; parent 5429; 2009-08-07T10:51:31Z -->
