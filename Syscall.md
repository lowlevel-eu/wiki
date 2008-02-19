# Syscall

Syscalls werden verwendet um Programmen Zugriff auf Funktionen im [Kernel](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel") zu gewährleisten.

Meistens werden Syscalls mithilfe eines Software-[Interrupts](https://github.com/lowlevel-eu/wiki/wiki/Interrupt "Interrupt") realisiert. Der aufrufende Prozess füllt entweder die Syscall-Parameter in Arbeitsregister oder legt sie auf den Stack. Meistens wird der Syscall, den der Prozess aufrufen will über eine Nummer als Parameter übergeben. Dann ruft der Prozess einen Software-[Interrupt](https://github.com/lowlevel-eu/wiki/wiki/Interrupt "Interrupt") auf, dieser hat normalerweise eine festgelegte Nummer, bei [Linux](https://github.com/lowlevel-eu/wiki/wiki/Linux "Linux") ist das der [Interrupt](https://github.com/lowlevel-eu/wiki/wiki/Interrupt "Interrupt") 0x80. Auf neueren CPUs besteht auch die Möglichkeit die Instruktion *sysenter* zu verwenden, so wie das bei [Windows](https://github.com/lowlevel-eu/wiki/wiki/Windows "Windows") der Fall ist.

Im Kernel wird dann ein Syscallhandler verwendet um die Funktion aufzulösen und die Parameter zu übergeben.

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/2587/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1629/index.html)

<!-- MediaWiki page 1629; revision 2587; parent 0; 2008-02-19T12:06:14Z -->
