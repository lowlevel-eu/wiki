# Syscall

Ein **Syscall** wird verwendet, um Programmen Zugriff auf Funktionen im [Kernel](Kernel "Kernel") zu gewähren. Da Programme in separaten Adressräumen untergebracht sind und nicht im Kernelmodus (d.h. im Ring 0 im Protected/Long-Mode) ausgeführt werden, ist es für das Programm unmöglich, bestimmte Aktionen wie zum Beispiel [Interprozesskommunikation](Interprozesskommunikation "IPC") selbstständig auszuführen.

## Parameterübergabe

Der aufrufende Prozess füllt entweder die Syscall-Parameter in Prozessorregister oder legt sie auf den Stack. Meistens wird der Syscall, den der Prozess aufrufen will, über eine Nummer als Parameter, z.B. über das Register eax, übergeben.

Anschließend löst der Prozess einen Syscall aus.

## Auslösen des Syscalls

Meistens werden Syscalls mithilfe eines Software-[Interrupts](Interrupt "Interrupt") realisiert. Der auszulösende Softwareinterrupt hat normalerweise eine fest kodierte Nummer. Linux verwendet beispielsweise den Interrupt 0x80. In manchen Prozessoren sind spezielle Instruktionen für ein performanteres Auslösen von Syscalls vorgesehen. Beispielsweise unterstützen neuere AMD-Prozessoren die *[syscall](Syscall-sysret "Syscall/sysret")*-Instruktion und neuere Intel-Prozessoren die *[sysenter](Sysenter "Sysenter")*-Instruktion. [ARM](ARM "ARM")-CPUs haben dafür die svc-Instruktion.

Anschließend befindet sich der Prozessor im Kernelmodus, und der Kernel übernimmt.

## Behandlung des Syscalls

Im Kernel wird dann ein Syscallhandler verwendet, um mit Hilfe der übergebenen Nummer die Funktion aufzurufen und die Parameter zu übergeben. Die von diesem Handler selektierte Funktion führt die vom Programm gewünschte Aktion aus, falls das Programm die benötigten Rechte dazu hat. Anschließend kehrt die Funktion zurück zu dem Programm und gibt möglicherweise einen oder mehrere Rückgabewerte über Prozessorregister oder Stack zurück. Alternativ kann das Programm auch geblockt werden, falls beispielsweise die Anfrage nach Daten von der Festplatte nicht sofort (über Caches) beantwortet werden kann, oder das Programm wird terminiert.

## siehe auch

- [Interrupt](Interrupt "Interrupt")

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/11125/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1629/index.html)

<!-- MediaWiki page 1629; revision 11125; parent 10014; 2013-07-24T15:07:55Z -->
