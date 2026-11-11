# Systemlautsprecher

Der **Systemlautsprecher** kann für ein Betriebssystem ganz nützlich sein, um z. B. auf Fehler aufmerksam zu machen oder einfach das Zeichen *\a* ausgeben zu können. Er wird manchmal auch als "BIOS-Beeper" oder einfach nur als "Beeper" bezeichnet, da er ein monotones Piepen erzeugt. Man kann nur die Frequenz anpassen und nicht etwa die Form der Schwingungskurve. Der Systemlautspecher kann nur Rechteckkurven erzeugen, aber das reicht auch oft schon aus.

## Ansteuerung

Zur Steuerung der Frequenz wird der 3. Kanal des [PIT](Programmable-Interval-Timer "PIT") verwendet, man muss also vor dem Einschalten in das Latchregister des 3. Kanals des [PIT](Programmable-Interval-Timer "PIT") den richtigen Wert hineinschreiben. Um diesen Wert zu ermitteln, kann man folgende Formel benutzen: *teiler = 1193180/frequenz*.

Man muss aber noch dem Lautsprecher mitteilen, wie er den Ton erzeugen soll. Dafür eignet es sich, *10110110b* in das Kommandoregister zu laden, damit wird:

- Kanal 3 des [PIT](Programmable-Interval-Timer "PIT") verwendet (üblich für Lautsprecher)
- erst das Low-Byte und dann das High-Byte des Latch-Registers verwendet
- eine symmetrische Pulsfolge erzeugt
- das Kommandobyte binär interpretiert und nicht als [BCD](Binary-Coded-Decimal "BCD")

Ob man zuerst den Timer einstellt oder das Kommandoregister setzt, ist eigentlich egal, auf jeden Fall muss man anschließend den Ton anschalten und wieder ausschalten. Die Zeit dazwischen muss irgendwie überbrückt werden. Ich benutze dafür meinen Kernel-Timer, mit dem ich eine Callback-Funktion nach einer bestimmten Zeit aufrufen lassen kann.

## Beispiel

Die Funktionen *inb()* und *outb()* sollten vorhanden sein, außerdem noch sowas ähnliches wie *add_timeout()* um eine Funktion zeitversetzt aufzurufen (*sleep* würde auch reichen).

\<c\>

    void sound_on() {
      // 1. und 2. Bit setzen um Lautsprecher anzuschalten
      outb(0x61, inb(0x61) | 3);
    }
    void sound_off() {
      // 1. und 2. Bit zurücksetzen um Lautsprecher auszuschalten
      outb(0x61, inb(0x61) & ~3);
    }
    void sound(uint32_t frequenz, uint32_t dauer) {
      uint16_t teiler;
      teiler = 1193180 / frequenz;
      outb(0x43, 0xB6);
      outb(0x42, teiler & 0xFF);
      outb(0x42, teiler >> 8);
      sound_on()
      add_timeout(dauer, sound_off());
    }

\</c\>

## Weblinks

- <http://de.wikipedia.org/wiki/Systemlautsprecher>

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/6003/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1570/index.html)

<!-- MediaWiki page 1570; revision 6003; parent 2469; 2009-10-12T10:25:07Z -->
