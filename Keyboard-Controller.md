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
        │││││││└─ Status des Ausgabepuffers (KBC -> CPU) :  0=leer;  1=voll (es kann von Port 0x60 gelesen werden)
        ││││││└── Status des Eingabepuffers (KBC <- CPU) :  0=leer (Schreiben auf 0x60 oder 0x64 möglich);  1=voll
        │││││└─── Systemstatus? :  0=Reset/Selbsttest wird gerade ausgeführt;  1=Selbsttest OK
        ││││└──── zuletzt benutztes Port : 0=0x60;  1=0x61 oder 0x64?
        │││└───── Tastatursperre : 0=Tastatur gesperrt; 1=Tastatur nicht gesperrt
        ││└────── PSAUX?
        │└─────── Timeout : 1=Tastatur oder PSAUX-Gerät ragiert nicht?
        └──────── Paritätsfehler : 1=Beim letzten Senden/Empfangen trat ein Paritätsfehler auf

  

Inputport (Lesen über KBC-Befehl 0xC0)

    Bit 76543210
        │││││││└─ Keyboard data in pin?
        ││││││└── PS/2 mouse in pin?
        │││││└─── Reserviert
        ││││└──── Reserviert
        │││└───── Reserviert
        ││└────── Reserviert
        │└─────── Wether you have a color or mono screen?
        └──────── Tastatursperre : 0=Tastatur gesperrt;  1=Tastatur nicht gesperrt

  

Outputport (Lesen über KBC-Befehl 0xD0, schreiben über KBC-Befehl 0xD1)

    Bit 76543210
        │││││││└─ 1=CPU-Reset
        ││││││└── 1=A20-Gate eingeschaltet
        │││││└─── ? PS/2 mouse data out
        ││││└──── ? PS/2 mouse clock signal
        │││└───── ? 1: Output buffer full
        ││└────── ? 1: Output buffer PS/2 mouse full
        │└─────── ? Keyboard clock signal
        └──────── ? Keyboard data out

  

  
Port 0x61 (lesen und schreiben)

    Bit 76543210
        │││││││└─ PPI \
        ││││││└── PPI  \
        │││││└─── PPI   |Dieser Teil ist vom Programmable Peripheral Interface
        ││││└──── PPI   |nicht überschreiben!
        │││└───── PPI  /
        ││└────── PPI /
        │└─────── Setzt die "clock"-Leitung auf low, so dass die Tastatur keine Daten an den PC senden kann
        └──────── 0=Tastatur eingeschaltet;  1=Tastatur ausgeschaltet

  

KBC-Befehle (schreiben auf Port 0x64)  
Bevor man auf Port 0x64 schreibt, müssen Port\[0x60\].Bit\[1\]==0 und Port\[0x60\].Bit\[2\]==1 sein!

    0xAA   Tastatur-Selbsttest. Sollte 0x55 auf Port 0x60 zurückgeben.

    0xAB   Testen des Tastaturanschlusses. Auf Port 0x60 wird ein Byte zurückgegeben:

             00h: No error
             01h: Clock low
             02h: Clock high
             03h: Data low
             04h: Data high
             ffh: Total Error

    0xAD   Deaktivieren der Tastatur

    0xAE   Aktivieren der Tastatur

    0xC0   Lesen des Inputports. Gibt den Inhalt vom Inputport auf Port 0x60 aus. (Siehe: Inputport)

    0xD0   Lesen des Outputports. Gibt den Inhalt vom Outputport auf Port 0x60 aus. (Siehe: Outputport)

    0xD1   Schreiben des Outputports. Den neuen Wert für das Outputport auf Port 0x60 schreiben. (Siehe: Outputport)

    0xD2   ?
    0xD3   ?
    0xD4   ?

    0xE0   ?

    0xFx   ?

  

Tastatur-Befehle (schreiben auf Port 0x60)  
Bevor man auf Port 0x60 schreibt, müssen Port\[0x60\].Bit\[1\]==0 und Port\[0x60\].Bit\[2\]==1 sein!

    0xED   Setzen der LEDs auf der Tastatur. Ein zweites Byte wird über Port 0x60 gesendet:

           Bit 76543210
               │││││││└─ Scroll Lock : 0=aus 1=an
               ││││││└── Num Lock    : 0=aus 1=an
               │││││└─── Caps Lock   : 0=aus 1=an
               └┴┴┴┴──── 0

    0xEE   Dieser Befehl ist zum testen der Tastatur. Die Tastatur sollte mit 0xEE antworten.

    0xF0   Auswählen des Scancodes. Als Parameter den Scancode 1, 2(standard) oder 3 auf Port 0x60 senden.
           (Anmerkung: Kann man mit dem Wert 0 als Parameter den aktuellen Scancode auslesen?)

    0xF2   Diesen Befhel sendet man zum identifiziren der Tastatur. Es gibt folgende Rückgabewerte:

           XT Tastatur    :  Timeout (Port[0x64].Bit[6]=1)
           AT Tastatur    :  Rückgabewert 0xFA
           MF II Tastatur :  Rückgabewert 0xFA 0xAB 0x41

    0xF3   Setzen der Wiederholrate für gedrückte Tasten. Ein zweites Byte wird über Port 0x60 gesendet:

           Bit 76543210
               │││└┴┴┴┴─ Wiederholrate der Taste nach der Wartezeit
               │││       Wert  : Wiederholungen pro Sekunde
               │││       00000 : 30
               │││       00001 : 26,7
               │││       00010 : 24
               │││       00100 : 20
               │││       01000 : 15
               │││       01010 : 10
               │││       01101 :  9
               │││       10000 :  7,5
               │││       10100 :  5
               │││       11111 :  2
               │││
               │└┴────── Wartezeit bevor eine gehaltene Taste wiederholt wird.
               │         00 :  250 ms
               │         01 :  500 ms
               │         10 :  750 ms
               │         11 : 1000 ms
               │
               └──────── 0

    0xF4   ?
    0xF5   ?
    0xF6   ?

    0xFE   ?

    0xFF   ?

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/1769/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1468/index.html)

<!-- MediaWiki page 1468; revision 1769; parent 1768; 2007-01-21T13:46:34Z -->
