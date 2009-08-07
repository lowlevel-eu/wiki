# Long Mode

**Achtung!**

Der Artikel wird zur Zeit bearbeitet. Bitte bearbeite diesen Artikel nicht! Es kann zu Darstellungsproblemen während des Betrachtens des Artikels kommen. [SHyx0rmZ](https://lowlevel-eu.github.io/wiki/pages/1785/index.html "Benutzer:SHyx0rmZ") 12:14, 7. Aug. 2009 (CEST)

Der **Long Mode** ist ein CPU-Modus neuerer CPUs, in dem erstmals 64-Bit-Allzweckregister zur Verfügung stehen. Wie auch beim [Protected Mode](https://github.com/lowlevel-eu/wiki/wiki/Protected-Mode "Protected Mode") starten Prozessoren, die diesen Modus unterstützen, aus Kompatibilitätsgründen zunächst im [Real Mode](https://github.com/lowlevel-eu/wiki/wiki/Real-Mode "Real Mode") mit deaktiviertem [A20-Gate](https://github.com/lowlevel-eu/wiki/wiki/A20-Gate "A20-Gate").

## Eigenschaften

- Address-/Registerbreite beträgt 64 Bit
- Viele neue Register (z.B. R8-R15, CR8-CR15, ...)
- ...

## Wie überprüfe ich, ob die CPU den Long Mode unterstützt?

CPUs, die den Long Mode unterstützen, setzen bei einem Aufruf der [CPUID](https://github.com/lowlevel-eu/wiki/wiki/CPUID "CPUID")-Operation mit EAX=0x80000001 das Long-Mode-Capable-Bit (Bit 29) im EDX-Register auf 1.

## Wie schalte ich den Long Mode um?

Um in den Long Mode umschalten zu können, muss erst einmal der [Protected Mode](https://github.com/lowlevel-eu/wiki/wiki/Protected-Mode "Protected Mode") aktiviert werden. Eine weitere Voraussetzung ist es, dass das *Physical Address Extension*-Bit (Bit 5) im CR4 gesetzt und Paging deaktiviert ist. Jetzt kann der Long Mode mit dem Setzen des LME-Bits (Bit 8) im MSR 0xC00000080 aktiviert werden. Im eigentlichen Long Mode befindet man sich aber erst, wenn man in ein 64-Bit-Code-Segment wechselt, das im Vergleich zu den 32-Bit-Code-Segmenten in seinem Descriptor das L-Bit (Bit 21) im 2. DWord gesetzt hat.

  

## Links

- <http://www.osdev.org/wiki/X86-64>
- <http://www.sandpile.org/aa64/index.htm>

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/5424/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1666/index.html)

<!-- MediaWiki page 1666; revision 5424; parent 4880; 2009-08-07T10:14:32Z -->
