# Machine-Specific Register

Diese Seite ist ein Artikel, welcher **mehr** haben könnte..  

Wenn du mehr darüber weißt oder recherchieren willst, bist **du** aufgerufen, dies zu tun. Wenn du dir in einer Sache nicht sicher bist, dann stell es auf die Diskussionsseite.

Die **Machine-Specific Register**s bzw. **Model-Specific Register**s (**MSR**) sind Prozessorregister. Sie können im Gegensatz zu anderen Registern nur mit den Instruktionen *rdmsr* und *wrmsr* ([x86](https://github.com/lowlevel-eu/wiki/wiki/X86 "X86") und [x86-64](https://github.com/lowlevel-eu/wiki/wiki/X86-64 "X86-64")) angesprochen werden. Außerdem sind diese Register spezifisch für eine bestimmte Prozessorfamilie/-generation, d.h. sie müssen von folgenden Prozessoren nicht bzw. nicht genauso implementiert werden.

Ob eine bestimmte CPU MSRs besitzt und somit die Befehle *rdmsr* und *wrmsr* ohne Exception ausführt, kann per [CPUID](https://github.com/lowlevel-eu/wiki/wiki/CPUID "CPUID") herausgefunden werden. Ist nach einem *cpuid*-Befehl mit EAX = 0x00000001 in EDX Bit 5 gestzt, dann werden diese Instruktionen unterstützt (s. auch [EDX - Featureflags](https://github.com/lowlevel-eu/wiki/wiki/CPUID#edx---featureflags "CPUID") im CPUID-Artikel).

## WRMSR/RDMSR

Mit folgendem Code kann man auf die MSRs zugreifen: \<c\>uint64_t rdmsr(uint32_t msr) {

       uint32_t low, high;

       __asm__ __volatile__ ("rdmsr" :
                             "=a" (low), "=d" (high) :
                             "c" (msr));

       return ((uint64_t)high << 32) | low;

}

void wrmsr(uint32_t msr,

              uint64_t value)

{

       uint32_t low = value & 0xFFFFFFFF;
       uint32_t high = value >> 32;

       __asm__ __volatile__ ("wrmsr" ::
                             "a"(low), "c"(msr), "d"(high));

}\</c\>

## Auswahl einiger MSRs

| Nummer | Name | Inhalt |
| ------------ | -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0x1B | IA32_APIC_BASE_MSR | Basisadresse des [Local-APIC](https://github.com/lowlevel-eu/wiki/wiki/Local-Advanced-Programmable-Interrupt-Controller "Local APIC") |
| 0x174 | IA32_SYSENTER_CS | **CS** für **[SYSENTER](https://github.com/lowlevel-eu/wiki/wiki/Sysenter "Sysenter")** |
| 0x175 | IA32_SYSENTER_ESP | **ESP** für **SYSENTER** |
| 0x176 | IA32_SYSENTER_EIP | **EIP** für **SYSENTER** |
| 0xC0000080 | IA32_EFER | Erweiterte Features. Beispiele: Bit 0 - Aktiviert syscall/sysret im 64-Bit-Modus; Bit 8 - Schaltet den [Long Mode](https://github.com/lowlevel-eu/wiki/wiki/Long-Mode "Long Mode") ein |
| 0xC0000081 | STAR | **EIP** für **SYSCALL** im Protected Mode |
| 0xC0000082 | LSTAR | **RIP** für **SYSCALL** im Long Mode |
| 0xC0000083 | CSTAR | **RIP** für **SYSCALL** im Compability Mode |

## Weblinks

- <http://www.intel.com/Assets/PDF/manual/253669.pdf> - "Intel Architectures Software Developer's Manual Volume 3B: System Programming Guide" - Anhang B

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/11254/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1607/index.html)

<!-- MediaWiki page 1607; revision 11254; parent 6741; 2015-01-14T17:05:25Z -->
