# Virtual 8086 Mode

VM86 ist der Kompatibilitätsmodus von x86-Prozessoren, um 16bit-RealMode-Code auszuführen. Er ist vor allem praktisch, um Realmode-Interrupts wie den int 0x10 (VGA/VESA) aufzurufen.

# Einrichtung

Der VM86-Modus wird aktiviert, indem für den entsprechenden Task in EFLAGS das VM-Bit (0x20000) gesetzt wird. Zusätzlich werden während einem iret aus dem Kernel in den Task vier Realmode-Segmentregister geladen, die vorher auf den Kernel-Stack gepusht werden müssen. Da für den Task Realmode-Addressierung benutzt wird, müssen auch cs:ip und ss:sp so gesetzt werden, dass sie im Realmode auf die entsprechende Addresse zeigen. VM86-Tasks laufen grundsätzlich im Ring 3. Der große Vorteil des VM86 ist, dass Paging unterstützt wird, so können die entsprechenden physikalischen Addressen von Kernel belegt werden und sogar mehrere VM86-Tasks gleichzeitig laufen, indem Speicher aus anderen Bereichen in das erste Megabyte gemappt wird. Hier kann es allerdings Probleme geben, wenn der Kernel in diesem Bereich Speicher benutzt, bei einem entsprechend niedrig geladenen Kernel muss man halt entsprechend aufpassen.

# Beispiel

Aufbau eines Stacks direkt vor dem iret zu einem VM86-Task:

(Alle Werte, auch die 16-Bit-Register, sind auf dem Stack 32 bit groß, alle Segment-Register sind mit Realmode-Werten gefüllt)

**Wert**

gs fs es ds ss sp eflags cs ip

Darunter kommen je nach OS noch andere Werte, unter anderem die General Purpose Register des Tasks.

# VM86-Monitor

Da bestimmte Befehle im VM86-Task das restliche Betriebssystem blockieren oder sonstiges Unheil anrichten können, werden sie vom Prozessor blockiert und lösen einen GPF aus. Die Aufgabe des Betriebssystems ist jetzt, diese Befehle im Exceptionhandler abzufangen und zu emulieren. Befehle, die emuliert werden müssen, sind: pushf/popf cli/sti int/iret in/out (falls der Task die nötigen Berechtigungen nicht hat) Ich persönlich benutze den VM86-Mode nur, um Interrupts aufzurufen und missbrauche so das iret zusätzlich dazu, um herauszufinden, ob der Interrupt beendet wurde.

# Links

- [Sehr gutes Tutorial von Tim Robinson (englisch)](http://osdev.berlios.de/v86.html)
- [Code aus LOST für VM86-Tasks (nur für RM-Interrupts)](http://svn.tyndur.org/filedetails.php?repname=Lost&path=%2Ftrunk%2Fsrc%2Fkernel%2Fsrc%2Fvm86.c)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/3175/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1546/index.html)

<!-- MediaWiki page 1546; revision 3175; parent 3144; 2008-08-15T11:18:34Z -->
