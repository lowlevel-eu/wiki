# Non Maskable Interrupt

Diese Seite ist ein Artikel, welcher **mehr** haben könnte..  

Wenn du mehr darüber weißt oder recherchieren willst, bist **du** aufgerufen, dies zu tun. Wenn du dir in einer Sache nicht sicher bist, dann stell es auf die Diskussionsseite.

Ein NMI (**N**on-**M**askable **I**nterrupt) ist ein [Hardwareinterrupt](https://github.com/lowlevel-eu/wiki/wiki/Interrupt "Interrupt"), welcher nicht über das Interruptflag gesperrt werden kann. Er kann jedoch über das höchste Bit im [CMOS](https://github.com/lowlevel-eu/wiki/wiki/CMOS "CMOS")-Adressregister ge- bzw. entsperrt werden. Das ist jedoch aus verschiedenen Gründen **nicht** zu empfehlen!

Ein NMI wird ausgelöst, wenn ein so fataler Hardwarefehler auftritt, dass dieser nicht mehr ohne weiteres bis überhaupt nicht mehr zu beheben ist. Er kann jedoch auch vom Benutzer selbst ausgelöst werden, nämlich durch Drücken der Reset-Taste, die bei einigen PCs vorhanden ist.

Eine völlig andere Art der NMIs, sogenannte "Debugging NMIs", werden verwendet, um fehlerhaften Code zu debuggen: Durch den NMI wird ein Interrupthandler aufgerufen, der dann beispielsweise ein Programm zur Speicheranalyse starten könnte, welches kritische Stellen im RAM auf dem Bildschirm zeigt.

Wie oben bereits erwähnt, ist es nicht sinnvoll, NMIs zu deaktivieren, und schon gar nicht über längere Zeiträume hinweg. Wer es trotzdem tun will, hier der nötige Code dazu (der Code stammt von den Kollegen von OSDev.org):

\<c\>

    void NMI_disable()
    {
        outb(0x70, inb(0x70)|0x80);
    }

\</c\>

...und das hier zum reaktivieren:

\<c\>

    void NMI_enable()
    {
        outb(0x70, inb(0x70)&0x7F);
    }

\</c\>

## Weblinks

- [Die Seite auf OSDev.org](http://wiki.osdev.org/Non_Maskable_Interrupt)
- [Artikel auf Wikipedia (leider nur auf Englisch so ausführlich)](http://en.wikipedia.org/wiki/Non-maskable_interrupt)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/10435/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1594/index.html)

<!-- MediaWiki page 1594; revision 10435; parent 9847; 2012-02-14T17:13:16Z -->
