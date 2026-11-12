# Real Time Clock

Diese Seite ist ein Artikel, welcher **mehr** haben könnte..  

Wenn du mehr darüber weißt oder recherchieren willst, bist **du** aufgerufen, dies zu tun. Wenn du dir in einer Sache nicht sicher bist, dann stell es auf die Diskussionsseite.

Die **Real Time Clock** (= **RTC**) bzw. **Echtzeituhr** eines [x86](X86 "X86")- bzw. [x86-64](X86-64 "X86-64")-Computers gehört zum [CMOS](CMOS "CMOS") und aktualisiert die darin gespeicherte Uhrzeit und das Datum.

## Programmierung

Die RTC wird über die Statusregister im CMOS programmiert. Wenn Bit 6 im [Statusregister B](CMOS "CMOS") gesetzt ist, kann die RTC periodisch den [IRQ](Programmable-Interrupt-Controller#irq-tabelle "IRQ") 8 auslösen. Die Frequenz lässt sich mit dem [Statusregister A](CMOS "CMOS") einstellen. \<c\>void rtc_init() { cmos_write(0x0B, cmos_read(0x0B) \| 0x40); // IRQ aktivieren cmos_write(0x0A, (cmos_read(0x0A) & 0xF0) \| 0x0F); // Interrupt alle 500ms }\</c\>

Im IRQ-Handler muss dann das [Statusregister C](CMOS "CMOS") ausgelesen werden, sonst löst der RTC keine Interrupts mehr aus. Das Statusregister enthält Informationen über die Ursache des Interrupts, allerdings man kann den Wert nach dem Lesen auch einfach ignorieren.

## Siehe auch

- [CMOS](CMOS "CMOS")

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/9951/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1715/index.html)

<!-- MediaWiki page 1715; revision 9951; parent 4721; 2011-07-18T11:27:45Z -->
