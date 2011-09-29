# Virtual 8086 Mode

**VM86** ist der Kompatibilitätsmodus von x86-Prozessoren, um 16bit- [Real-Mode](https://github.com/lowlevel-eu/wiki/wiki/Real-Mode "Real Mode")-Code auszuführen. Er ist vor allem praktisch, um Realmode-Interrupts wie den int 0x10 ([VGA](https://github.com/lowlevel-eu/wiki/wiki/Video-Graphics-Array "Video Graphics Array")/VESA) aufzurufen.

## Einrichtung

Der VM86-Modus wird aktiviert, indem für den entsprechenden Task in [EFLAGS](https://github.com/lowlevel-eu/wiki/wiki/EFLAGS "EFLAGS") das VM-Bit (0x20000) gesetzt wird. *Achtung:* Dieses Setzen funktioniert *nicht* per popfd oder einem ähnlichen Befehl! Das VM-Bit kann nur durch einen Sprung verändert werden, z. B. also durch einen Sprung in einen anderen Hardwaretask, dessen EFLAGS-Feld im [TSS](https://github.com/lowlevel-eu/wiki/wiki/Task-State-Segment "TSS") ein gesetztes VM-Bit enthält oder durch ein iret mit einem Stack, wie er unten beschrieben wird.

Während eines solchen iret aus dem Kernel in den Task werden automatisch vier Realmode-Segmentregister geladen (wenn die CPU im neuen EFLAGS das VM-Bit als gesetzt erkannt hat), die vorher auf den Kernel-Stack gepusht werden müssen. Da für den Task Realmode-Addressierung benutzt wird, müssen auch cs:ip und ss:sp so gesetzt werden, dass sie im Realmode auf die entsprechende Addresse zeigen. VM86-Tasks laufen grundsätzlich im Ring 3. Der große Vorteil des VM86 ist, dass [Paging](https://github.com/lowlevel-eu/wiki/wiki/Paging "Paging") unterstützt wird, so können die entsprechenden physikalischen Addressen von Kernel belegt werden und sogar mehrere VM86-Tasks gleichzeitig laufen, indem Speicher aus anderen Bereichen in das erste Megabyte gemappt wird. Hier kann es allerdings Probleme geben, wenn der Kernel in diesem virtuellen Bereich Speicher benutzt, bei einem entsprechend niedrig geladenen Kernel muss man halt entsprechend aufpassen.

## Beispiel

Aufbau eines Stacks direkt vor dem iret zu einem VM86-Task:

(Alle Werte, auch die 16-Bit-Register, sind auf dem Stack 32 bit groß, alle Segment-Register sind mit Realmode-Werten gefüllt. Man beachte auch die nicht-alphabetische Reihenfolge von ds und es.)

**Wert**

gs fs ds es ss sp eflags cs ip

Darunter kommen je nach OS noch andere Werte, unter anderem die [General Purpose Register](https://github.com/lowlevel-eu/wiki/wiki/Register "Register") des Tasks.

## VM86-Monitor

Da bestimmte Befehle im VM86-Task das restliche Betriebssystem blockieren oder sonstiges Unheil anrichten können, werden sie vom Prozessor blockiert und lösen einen GPF aus. Die Aufgabe des Betriebssystems ist jetzt, diese Befehle im Exceptionhandler abzufangen und zu emulieren. Befehle, die emuliert werden müssen, sind:

- pushf/popf
- cli/sti
- int/iret
- in/out (falls der Task die nötigen Berechtigungen nicht hat)

Ich persönlich benutze den VM86-Mode nur, um Interrupts aufzurufen und missbrauche so das iret zusätzlich dazu, um herauszufinden, ob der Interrupt beendet wurde.

## Links

- [Sehr gutes Tutorial von Tim Robinson (englisch)](http://osdev.berlios.de/v86.html)
- [Code aus LOST für VM86-Tasks (nur für RM-Interrupts)](http://git.tyndur.org/?p=tyndur.git;a=blob;f=src/kernel2/src/arch/i386/vm86.c;hb=HEAD)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/10160/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1546/index.html)

<!-- MediaWiki page 1546; revision 10160; parent 9442; 2011-09-29T19:24:57Z -->
