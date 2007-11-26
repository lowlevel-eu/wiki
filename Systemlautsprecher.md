# Systemlautsprecher

Der Systemlautsprecher kann für ein Betriebssystem ganz nützlich sein, z.B um auf Fehler aufmerksam zumachen oder einfach das Zeichen *\a* ausgeben zu können. Der Systemlautsprecher wird manchmal auch als "BIOS-Beeper" oder einfach nur als "Beeper" bezeichnet, da er ein monotones Piepen erzeugt. Man kann nur die Frequenz anpassen und nicht etwa die Form der Schwingungskurve. Der Systemlautspecher kann nur Rechteckkurven erzeugen, aber das reicht auch oft schon aus.

## Ansteuerung

Zur Steuerung der Frequenz wird der 3. Kanal des [PIT](https://github.com/lowlevel-eu/wiki/wiki/Programmable-Interval-Timer "PIT") verwendet, man muss also vorher in das Latchregister des 3. Kanals des [PIT](https://github.com/lowlevel-eu/wiki/wiki/Programmable-Interval-Timer "PIT") den richtigen Wert hineinschreiben. Um den richtigen Wert zu ermitteln kann man diese Formel benutzen: *teiler = 1193180/frequenz*.

Man muss aber noch dem Lautsprecher mitteilen, wie er den Ton erzeugen soll. Dafür eignet es sich *10110110b* in das Kommanndoregister zu laden, damit wird:

- Kanal 3 des [PIT](https://github.com/lowlevel-eu/wiki/wiki/Programmable-Interval-Timer "PIT") verwendet (üblich für Lautsprecher)
- erst das Low-Byte und dann das High-Byte des Latch-Registers verwendet
- eine symetrische Pulsfolge erzeugt
- das Kommandobyte binär interpretiert und nicht als BCD

Ob man zuerst den Timer einstellt oder das Kommandoregister ist eigentlich egal, auf jeden Fall muss man dann den Ton anschalten und wieder ausschalten. Die Zeit dazwischen muss irgendwie überbrückt werden. Ich benutze dafür meinen Kernel-Timer, mitdem ich eine Callback-Funktion nach einer bestimmten Zeit aufrufen lassen kann.

## Beispiel

Die Funktionen *inb()* und *outb()* sollten vorhanden sein, außerdem noch sowas ähnliches wie *add_timeout()* um eine Funktion zeitversetzt aufzurufen (*sleep* würde auch reichen).

\<c\>

    void sound_on() {
      // 1. und 2. Bit setzen um Lautsprecher anzuschalten
      outb(0x61,inb(0x61)|3);
    }
    void sound_off() {
      // 1. und 2. Bit zurücksetzen um Lautsprecher auszuschalten
      outb(0x61,inb(0x61)&~3);
    }
    void sound(u32 frequenz,u32 dauer) {
      u32 teiler;
      teiler = 1193180/frequenz;
      outb(0x43,0xB6);
      outb(0x42,teiler&0xFF);
      outb(0x42,teiler>>8);
      sound_on()
      add_timeout(dauer,sound_off());
    }

\</c\>

## Weblinks

- <http://de.wikipedia.org/wiki/Systemlautsprecher>

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/2282/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1570/index.html)

<!-- MediaWiki page 1570; revision 2282; parent 2281; 2007-11-26T14:57:48Z -->
