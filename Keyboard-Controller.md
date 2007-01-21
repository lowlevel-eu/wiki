# Keyboard Controller

Der Keyboard Controller (KBC) sitzt auf dem Mainboard und dient, wie der Name vermuten lässt, unter anderem der Tastaturansteuerung. Er hat jedoch noch viele weitere Funktionen.

Funktionen des KBC:

- Ansteuerung der Tastatur
- Ansteuerung des PSAUX-Ports (z.B. PS/2-Maus)
- ein-/ausschalten der 21-Adressleitung (a20-Gate)
- CPU-Reset auslösen
- ein-/ausschalten des Systemlautsprechers
- Information ob das System eine Monochrom- oder Farbgrafikkarte benutzt

Zur Komunikation mit dem KBC werden die Ports 0x60, 0x61 und 0x64 verwendet.  

![kbcnr6.png](http://img241.imageshack.us/img241/5692/kbcnr6.png)  
Statusregister  

  

    Statusregister (lesen von Port 0x64)

    Bit 76543210
        ║║║║║║║╚═ Status des Ausgabepuffers (KBC -> CPU) :  0=leer;  1=voll (es kann von Port 0x60 gelesen werden)
        ║║║║║║╚══ Status des Eingabepuffers (KBC <- CPU) :  0=leer (Schreiben auf 0x60 oder 0x64 möglich);  1=voll
        ║║║║║╚═══ Systemstatus? :  0=Reset/Selbsttest wird gerade ausgeführt;  1=Selbsttest OK
        ║║║║╚════ zuletzt benutztes Port : 0=0x60;  1=0x61 oder 0x64?
        ║║║╚═════ Tastatursperre : 0=Tastatur gesperrt; 1=Tastatur nicht gesperrt
        ║║╚══════ PSAUX?
        ║╚═══════ Timeout : 1=Tastatur oder PSAUX-Gerät ragiert nicht?
        ╚════════ Paritätsfehler : 1=Beim letzten Senden/Empfangen trat ein Paritätsfehler auf


    Inputport

    Bit 76543210
        ║║║║║║║╚═ Keyboard data in pin?
        ║║║║║║╚══ PS/2 mouse in pin?
        ║║║║║╚═══ Reserviert
        ║║║║╚════ Reserviert
        ║║║╚═════ Reserviert
        ║║╚══════ Reserviert
        ║╚═══════ Wether you have a color or mono screen?
        ╚════════ Tastatursperre : 0=Tastatur gesperrt;  1=Tastatur nicht gesperrt

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/1768/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1468/index.html)

<!-- MediaWiki page 1468; revision 1768; parent 1764; 2007-01-21T10:54:48Z -->
