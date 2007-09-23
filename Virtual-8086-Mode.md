# Virtual 8086 Mode

VM86 ist der Kompatibilitätsmodus vonx86-Prozessoren, um 16bit-RealMode-Code auszuführen. Er ist vor allem praktisch, um Realmode-Interrupts wie den int 0x10 (VGA/VESA) aufzurufen.

# Einrichtung

Der VM86-Modus wird aktiviert, indem für den entsprechenden Task das VM-Bit (0x20000) gesetzt wird. Zusätzlich werden während einem iret aus dem Kernel in den Task vier Realmode-Segmentregister geladen, die vorher auf den Kernel-Stack gepusht werden müssen. Da für den Task Realmode-Addressierung benutzt wird, müssen auch cs:ip und ss:sp so gesetzt werden, dass sie im Realmode auf die entsprechende Addresse zeigen. VM86-Tasks laufen grundsätzlich im Ring 3. Der große Vorteil des VM86 ist, dass Paging unterstützt wird, so können die entsprechenden physikalischen Addressen von Kernel belegt werden und sogar mehrere VM86-Tasks gleichzeitig laufen, indem Speicher aus anderen Bereichen in das erste Megabyte gemappt wird. Hier kann es allerdings Probleme geben, wenn der Kernel in diesem Bereich Speicher benutzt, HigherHalf-Kernel sind so praktischer, aber nicht notwendig, wenn man gut genug aufpasst.

# VM86-Monitor

Da bestimmte Befehle im VM86-Task das restliche Betriebssystem blockieren oder sonstiges Unheil anrichten können, werden sie vom Prozessor blockiert und lösen einen GPF aus. Die Aufgabe des Betriebssystems ist jetzt, diese Befehle im Exceptionhandler abzufangen und zu emulieren. Befehle, die emuliert werden müssen, sind: pushf/popf cli/sti int/iret in/out (falls der Task die nötigen Berechtigungen nicht hat) Ich persönlich benutze den VM86-Mode nur, um Interrupts aufzurufen und missbrauche so das iret zusätzlich dazu, um herauszufinden, ob der Interrupt beendet wurde.

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/2105/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1546/index.html)

<!-- MediaWiki page 1546; revision 2105; parent 0; 2007-09-23T13:01:50Z -->
