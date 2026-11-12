# Sysenter

Die meisten Betriebssysteme verwenden wohl ein [Interrupt](Interrupt.md "Interrupt") als [Syscall](Syscall.md "Syscall"). Dies hat jedoch einen großen Nachteil: Der Prozessor muss dafür zunächst jede Menge Privilegüberprüfungen machen und viele Informationen speichern, die für einen einfachen Syscall unnötig sind. Dadurch geht viel Zeit verloren.  
Um diese Probleme zu umgehen, wurden die Befehle *sysenter* und *sysexit* eingeführt, die speziell für Syscalls entwickelt wurden. Sie funktionieren im [Protected Mode](Protected-Mode.md "Protected Mode") und bei Intelprozessoren auch im [Long Mode](Long-Mode.md "Long Mode"), im LM von AMD-Prozessoren löst ihre Verwendung hingegen eine Invalid-Opcode-Exception aus.

## Funktionsweise

Wenn *sysenter* ausgeführt wird, dann lädt der Prozessor einige Werte aus bestimmten [MSRs](Machine-Specific-Register.md "MSR") in die entsprechenden Register. So wird der Wert aus dem MSR 0x174 (IA32_SYSENTER_CS) in CS geladen, außerdem wird zu diesem Wert noch 8 addiert und das Ergebnis in SS geladen. Bei beiden Werten wird die Privilegstufe auf 0 gesetzt. Der Wert aus dem MSR 0x175 (IA32_SYSENTER_ESP) kommt nach ESP und aus 0x176 (IA32_SYSENTER_EIP) nach EIP.  
Weiterhin werden das VM- und das Interruptflag im EFLAGS-Register gelöscht.

Wird *sysexit* ausgeführt, so wird zuerst 16 zum Wert aus IA32_SYSENTER_CS addiert und das Ergebnis in CS geladen. Weiterhin wird zum gleichen Wert (IA32_SYSENTER_CS) nochmals 8 (also insgesamt 24) addiert und dieses Ergebnis nach SS kopiert. Die Privilegstufen beider Selektoren werden auf 3 gesetzt. EIP wird auf den Wert aus EDX gesetzt und ECX wird nach ESP kopiert. **Wichtig: EDX und ECX müssen vor sysexit vom Betriebssystem gesetzt werden, sysenter speichert keine Informationen über Rücksprungadresse und "ehemaliges" ESP!**

### Erforderlicher Aufbau der GDT

Offensichtlich stellen beide Befehle spezielle Anforderungen an die [GDT](Global-Descriptor-Table.md "GDT"). Sie muss also an irgendeiner Stelle die folgenden Deskriptoren in dieser Reihenfolge besitzen:

| Typ | Ring | Flags | Bedeutung |
| -------------- | ------ | ---------------------------------------------------------------------------------------------------- | --------------------------------------- |
| Codesegment | 0 | Readable, Executable, Present, Non-Conforming, 32 Bit, Basis: 0, Limit: 0xFFFFF, Granularity: 4 kB | Codesegment für den Syscallhandler |
| Datensegment | 0 | Readable, Writeable, Present, 32 Bit, Basis: 0, Limit: 0xFFFFF, Granularity: 4 kB | Stacksegment für den Syscallhandler |
| Codesegment | 3 | Readable, Executable, Present, Non-Conforming, 32 Bit, Basis: 0, Limit: 0xFFFFF, Granularity: 4 kB | Codesegment für das Usermodeprogramm |
| Datensegment | 3 | Readable, Writeable, Present, 32 Bit, Basis: 0, Limit: 0xFFFFF, Granularity: 4 kB | Stacksegment für das Usermodeprogramm |

In IA32_SYSENTER_CS muss dann der Selektor für das erste Ring-0-Codesegment eingetragen werden. Sind dies zum Beispiel die ersten vier Deskriptoren nach dem Nulldeskriptor, so müsste man dort 0x0008 eintragen.

## Vorhandensein

Um zu überprüfen, ob die *sysenter* und *sysexit* überhaupt unterstützt werden, muss man den *[cpuid](CPUID.md "CPUID")*-Befehl mit eax = 0x00000001 ausführen. Ist nach dem Befehl Bit 11 in EDX (SEP) gesetzt, sollte die Benutzung der Befehle in keiner Exception enden. Um ganz sicher zu gehen, sollte man aber auch Family, Model und Stepping überprüfen. Ist Family = 6, Model \< 3 und Stepping \< 3, dann werden beide Befehle trotzdem nicht unterstützt. Dies ist beim Pentium Pro der Fall, dessen CPUID zwar SEP gesetzt zurückgibt, aber der diese Befehle dennoch nicht unterstützt.

## Beispiel

Mit dem Code aus dem [MSR](Machine-Specific-Register.md "MSR")-Artikel und einer GDT, bei der die oben beschriebenen vier Deskriptoren bei 0x0008 beginnen, sähe das Einrichten eines Handlers folgendermaßen aus: \<c\>int set_sysenter_handler() {

      int eax, edx, family, model, stepping;

      //Zuerst mal überprüfen, ob es überhaupt geht
      __asm__ __volatile__ ("cpuid":"=a"(eax),"=d"(edx):"a"(0x00000001));
      if (!(edx & 0x800))
         return 0; //SEP nicht gesetzt
      family   = (eax & 0x00000F00) >> 8;
      model    = (eax & 0x000000F0) >> 4;
      stepping =  eax & 0x0000000F;
      if ((family == 6) && (model < 3) && (stepping < 3))
         return 0;

      wrmsr(0x174, 0x0008);
      wrmsr(0x175, /*Entsprechender ESP*/);
      wrmsr(0x176, &sysenter_handler);

      return 1;

}

void sysenter_handler() {

      //Auszuführender Code...

      __asm__ __volatile__ ("sysexit"::"c"(/*ESP vor dem sysenter-Befehl*/),"d"(/*EIP nach dem sysenter-Befehl*/));

}\</c\>

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/6041/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2083/index.html)

<!-- MediaWiki page 2083; revision 6041; parent 6022; 2009-10-14T20:47:42Z -->
