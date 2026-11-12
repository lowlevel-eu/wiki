# ARM-OS-Dev für Einsteiger

|  |  |  |
| ----- | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|  | **Navigation** | [ARM-OS-Dev Teil 1 – Entwicklungsumgebung](ARM-OS-Dev-Teil-1-%E2%80%93-Entwicklungsumgebung.md "ARM-OS-Dev Teil 1 – Entwicklungsumgebung") » |

Diese Reihe soll eine Adaption der [OS-Dev-für-Einsteiger-Reihe](OS-Dev-f%C3%BCr-Einsteiger.md "OS-Dev für Einsteiger") für ARM-Systeme sein. Viele der dort gesagten Dinge gelten unabhängig von der Architektur, dies gilt insbesondere für den Einführungsartikel. Bei Gemeinsamkeiten wird auf die x86-Reihe verwiesen, Unterschiede werden hier verdeutlicht und erklärt.

## Vor dem Start

Alles in der x86-Reihe gesagte gilt auch hier, mit dem Unterschied, dass sich die Wahl der Plattform erübrigt. Verwendet wird in dieser Tutorialreihe das sogenannte Integrator/CP-Board, welches die Standardumgebung des ARM-QEMU darstellt. Echte Integrator/CP-Boards sind recht teuer und schwer zu bekommen, sodass die Ausführung des hier gezeigten Codes wohl auf QEMU beschränkt bleiben wird. Die Übertragung des Tutorials auf andere Plattformen sollte jedoch nicht allzu schwer fallen, wenn die dort vorhandene Hardware bekannt ist.

Als eine zusätzliche Voraussetzung wäre in dieser Tutorialreihe die Kenntnis der x86-Architektur bzw. von grundlegenden Abläufen wie Interruptbehandlung und ähnlichem zu nennen. Sehr sinnvoll ist es auch, den [ARM](ARM.md "ARM")-Artikel gelesen zu haben.

## Wo anfangen?

### Booten

Dies ist eine interessantere Frage als auf x86, denn im Unterschied zu PCs existiert bei ARM keine einheitliche Bootumgebung. Der Prozessor beginnt seine Ausführung an der Speicheradresse 0x00000000, dort kann jedoch je nach Plattform entweder ein BIOS (z. B. Game Boy Advance), ein in den RAM eingeblendeter Flashspeicher (z. B. Integrator/CP-Board) oder etwas ganz anderes sein. Im ersten Fall wird das BIOS eine erste Umgebung aufsetzen und anschließend einen spezifizischen Einsprungspunkt aufrufen (ähnlich dem PC-BIOS), im zweiten muss am Beginn des Flashspeichers der Bootcode stehen. Aufgrund dieser Unterschiede wird im Folgenden nur noch auf die Umgebung eingegangen, die das Integrator/CP-Board (im weiteren Verlauf „I/CP“ genannt) bietet.

### Hello World und weiter

Leider gibt es auch hier keine einheitliche Umgebung. Beim I/CP gibt es keinen schönen Textgrafikmodus wie bei der PC-Grafikausgabe, sodass man die Wahl hat, entweder einen VGA-Grafikmodus zu initialisieren und dann alle Zeichen des „Hello, World“ selbst zu zeichnen oder die Zeichen per serieller Schnittstelle auszugeben. Ersteres ist auf echter Hardware besser, letzteres dafür wesentlich einfacher zu implementieren. Da ich davon ausgehe, dass sowieso niemand ein echtes I/CP hat und QEMU zur Ausführung des Codes verwendet, wird in diesem Tutorial die serielle Schnittstelle verwendet, die mit QEMU genauso (im Zweifelsfalle besser) gut wie eine grafische VGA-Ausgabe ist.

### Tabellen

Bei ARM gibt es keine Descriptortabellen wie bei x86. Eine Segmentierung des Speichers findet nicht statt. Interrupts und Exceptions werden behandelt, indem an feste Stellen im Speicher gesprungen wird. Die Verwaltung des virtuellen Speichers geschieht im Allgemeinen über Paging (all dies wird in der Tutorialreihe behandelt).

## Der eigentliche Kernel

Hier gelten wieder die gleichen Prinzipien wie in der x86-Reihe. Unterschiede sind, dass die Privilegien nicht durch die Ringe 0 bis 3, sondern durch Prozessormodi vergeben werden. Es gibt sechs privilegierte Modi und einen Usermodus, in dem alle Programme laufen. Kernelcode wird immer in einem der privilegierten Modi ausgeführt (IRQ/FIQ für Interrupts, SVC für Syscalls, ABT/UND für Exceptions; SYS könnte für Programme verwendet werden, die im Kernelmodus laufen sollen).

Als kleine Anmerkung wäre noch zu nennen, dass das Multitasking auf ARM natürlich ohne x86-TSS geschieht. Dazu mehr im entsprechenden Teil der Reihe.

### Treiber

An sich gelten hier die gleichen Regeln wie für x86-Treiber. Zu beachten ist jedoch, dass es selten so schöne Tutorials wie für x86-Geräte gibt und man sich daher im Allgemeinen selbst durch die Spezifikationen quälen muss. Bei I/CP ist dies jedoch durch ein entsprechendes Manual, das eine Zusammenfassung des Interfaces für jedes vorhandene Gerät bietet, recht einfach. [CDI](Common-Driver-Interface.md "CDI") kann man theoretisch auch auf ARM implementieren, praktisch ist dies wenig sinnvoll, da bisher kaum Treiber für Geräte von ARM-Plattformen existieren (wobei es auf einigen ARM-Plattformen auch PCI gibt, wodurch man die Treiber für PCI-Geräte durchaus nutzen kann, soweit diese kein x86-Port-I/O verwenden).

## Weblinks

- [Integrator/CP-Manual](http://infocenter.arm.com/help/topic/com.arm.doc.dui0138e/DUI0138E_CMxx6_UserGuide.pdf) – Vor allem Informationen zur Speichermap, Interrupts, etc.
- [Integrator/CP-Manual](http://infocenter.arm.com/help/topic/com.arm.doc.dui0159b/DUI0159B_integratorcp_1_0_ug.pdf) – Eher Informationen zur Peripherie (VGA-Ausgabe, PS/2-Eingabe, Timer, etc.)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/9764/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2417/index.html)

<!-- MediaWiki page 2417; revision 9764; parent 9758; 2011-05-11T17:21:11Z -->
