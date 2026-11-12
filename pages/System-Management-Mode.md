# System Management Mode

Diese Seite ist ein Artikel, welcher **mehr** haben könnte..  

Wenn du mehr darüber weißt oder recherchieren willst, bist **du** aufgerufen, dies zu tun. Wenn du dir in einer Sache nicht sicher bist, dann stell es auf die Diskussionsseite.

Der **System Management Mode** (**SMM**) ist ein Betriebsmodus der [x86](X86.md "X86")-Prozessoren, der Systemfunktionen wie Teile des Energiemanagement übernimmt. Er wurde mit Versionen der 386er- und 486er-Prozessoren für Laptops (i386SL bzw. i486SL) eingeführt und steht hinsichtlich der Privilegien der Betriebsmodi über dem [Real Mode](Real-Mode.md "Real Mode") und dem [Protected Mode](Protected-Mode.md "Protected Mode").

## Wechsel in den SMM

In den SMM kann nicht auf eine Art und Weise wie in den Protected Mode oder den Long Mode gesprungen werden. Die CPU wechselt in den SMM ausschließlich dann, wenn ein System Management Interrupt (SMI) über den \#SMI-Pin ausgelöst wird. Das bedeutet, dass dies nicht nur für Anwendungen sondern auch für das Betriebssystem transparent geschieht: Beide bekommen davon also nichts mit, ähnlich wie Programme nichts von [Hardware-Interrupts](Interrupt.md "Interrupt") mitbekommen. Wenn ein SMI ausgelöst wird, wird zunächst der Zustand der CPU gespeichert, und dann ein spezieller Interrupt-Handler ausgeführt. Dieser befindet sich in einem Adressraum, der in der Regel außerhalb des Zugriffs der anderen Betriebsmodi liegt. Der Rücksprung aus dem Interrupt-Handler, geschieht über die spezielle Instruktion *RSM*, die analog zu *IRET* funktioniert.

## Zweck

Für das Betriebssystem an sich ist der SMM nutzlos, verwendet wird er vor allem vom BIOS, um Treiber bereitzustellen, die ständige Kontrolle über ihre Geräte benötigen, auch wenn sich das Betriebssystem bereits im Protected Mode befindet und das BIOS daher keine Kontrolle mehr über Interrupts hat. So kann es bei bestimmten IRQs statt normalen Interrupts SMIs auslösen lassen, sodass der BIOS-Treiber im SMM läuft und das Gerät weiterhin steuert, wovon das Protected-Mode-Betriebssystem nichts mitbekommt. Nützlich ist dies vorrangig für Geräte, für die unbedingt ein Treiber notwendig ist, auch wenn das Betriebssystem keinen solchen bereitstellt: [ACPI](Advanced-Configuration-and-Power-Interface.md "ACPI") z. B. (Lüftersteuerung) oder für den [USB-Legacy-Support](Universal-Serial-Bus.md#legacy-support "USB").

## Links

[Intel Manuals, Volume 3B: System Programming Guide – System Management](http://www.intel.com/products/processor/manuals/)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/9637/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1699/index.html)

<!-- MediaWiki page 1699; revision 9637; parent 8512; 2011-03-28T19:53:35Z -->
