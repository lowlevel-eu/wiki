# Syscall

**Syscalls** werden verwendet um Programmen Zugriff auf Funktionen im [Kernel](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel") zu gewähren.

## Parameterübergabe

Der aufrufende Prozess füllt entweder die Syscall-Parameter in Prozessorregister oder legt sie auf den Stack. Meistens wird der Syscall, den der Prozess aufrufen will über eine Nummer als Parameter übergeben.

Anschließend [löst der Prozess einen Syscall aus](https://github.com/lowlevel-eu/wiki/wiki/Syscall#ausl%C3%B6sen-des-syscalls "Syscall").

## Auslösen des Syscalls

Meistens werden Syscalls mithilfe eines Software-[Interrupts](https://github.com/lowlevel-eu/wiki/wiki/Interrupt "Interrupt") realisiert. Der auszulösende Softwareinterrupt hat normalerweise eine fest kodierte Nummer. Linux verwendet beispielsweise den Interrupt 0x80. In manchen Prozessoren sind spezielle Instruktionen für ein performanteres Auslösen von Syscalls vorgesehen. Beispielsweise unterstützen neuere x86 AMD Prozessoren die *syscall* Instruktion. Im Unterschied dazu unterstützen neuere Intel Prozessoren die *sysenter* Instruktion.

Anschließend befindet sich der Prozessor im Kernelmodus (d.h. auf x86 Ring 0) und der Kernel übernimmt [die Behandlung des Syscalls](https://github.com/lowlevel-eu/wiki/wiki/Syscall#behandlung-des-syscalls "Syscall").

## Behandlung des Syscalls

Im Kernel wird dann ein Syscallhandler verwendet um die Funktion aufzulösen und die Parameter zu übergeben. Diese Funktion führt dann die vom Programm gewünschte Aktion aus (falls das Programm die benötigten Rechte dazu hat). Anschließend kehrt die Funktion zurück zu dem Programm (und gibt möglicherweise einen oder mehrere Rückgabewerte über Prozessorregister oder Stack zurück. Alternativ dazu kann das Programm auch geblockt werden, falls beispielsweise die Anfrage nach Daten von der Festplatte nicht sofort (über Caches) beantwortet werden kann, oder das Programm wird terminiert.

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/2617/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1629/index.html)

<!-- MediaWiki page 1629; revision 2617; parent 2587; 2008-03-08T14:40:29Z -->
