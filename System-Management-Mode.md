# System Management Mode

Diese Seite ist ein Artikel, welcher **mehr** haben könnte..  

Wenn du mehr darüber weißt oder recherchieren willst, bist **du** aufgerufen, dies zu tun. Wenn du dir in einer Sache nicht sicher bist, dann stell es auf die Diskussionsseite.

Der System Management Mode (SMM) ist ein Betriebsmodus der [x86](https://github.com/lowlevel-eu/wiki/wiki/X86 "X86")-Prozessoren, der Systemfunktionen wie das Energie Management verwaltet, um zum Beispiel den Computer in einen Ruhezustand zu versetzen. Er wurde mit Versionen der 386er- und 486er-Prozessoren für Laptops (i386SL bzw. i486SL) eingeführt und steht hinsichtlich der Privilegien der Betriebsmodi über dem [Real Mode](https://github.com/lowlevel-eu/wiki/wiki/Real-Mode "Real Mode") und dem [Protected Mode](https://github.com/lowlevel-eu/wiki/wiki/Protected-Mode "Protected Mode").

## Wechsel in den SMM

In den SMM kann nicht auf eine Art und Weise wie in den Protected Mode oder den Long Mode gesprungen werden. Die CPU wechselt in den SMM ausschließlich dann, wenn ein System Management Interrupt (SMI) über den SMI#-Pin ausgelöst wird. Das bedeutet, dass dies nicht nur für Anwendungen sondern auch für das Betriebssystem transparent geschieht; beide bekommen davon also nichts mit, ähnlich wie Programme nichts von [Hardware Interrupts](https://github.com/lowlevel-eu/wiki/wiki/Interrupt "Interrupt") mitbekommen. Wenn ein SMI ausgelöst wird, wird zunächst der Zustand der CPU gespeichert, und dann ein spezieller Interrupt Handler ausgeführt. Dieser befindet sich in einem Adressraum, der in der Regel außerhalb des Zugriffs der anderen Betriebsmodi liegt. Der Rücksprung aus dem Interrupt Handler, geschieht über die spezielle Instruktion RSM, die analog zu IRET funktioniert.

## Links

[Intels Manual, Volume 3B: System Programming Guide - System Management](http://www.intel.com/products/processor/manuals/)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/4596/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1699/index.html)

<!-- MediaWiki page 1699; revision 4596; parent 4434; 2009-07-09T19:45:08Z -->
