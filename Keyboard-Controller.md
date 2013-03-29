# Keyboard Controller

Der **Keyboard-Controller** oder auch **KBC** ist ein Baustein auf dem Mainboard und dient (unter anderem) der Tastaturansteuerung. Ursprünglich von IBM entwickelt, wurde der Keyboard-Controller in seiner Funktion stark erweitert, wodurch sich heutzutage viele Aufgaben über selbigen erledigen lassen.

  
Der KBC wurde mit dem AT-System (i286) eingeführt. Im Vorgängersystem XT wurde für vergleichbare Aufgaben das Programmable Peripheral Interface (PPI) genutzt.

## Funktionen des KBC

- Ansteuerung eines oder zweier Auxiliary Port(s) (Tastatur, Maus)

<!-- -->

- Ein-/ausschalten der 21. Adressleitung ([A20-Gate](https://github.com/lowlevel-eu/wiki/wiki/A20-Gate "A20-Gate"))

<!-- -->

- CPU-Reset auslösen, also Neustart des Systems

<!-- -->

- Zusammen mit dem [PIT](https://github.com/lowlevel-eu/wiki/wiki/Programmable-Interval-Timer "Programmable Interval Timer") den [Systemlautsprecher](https://github.com/lowlevel-eu/wiki/wiki/Systemlautsprecher "Systemlautsprecher") ansteuern.

<!-- -->

- Information darüber, ob das System eine Monochrom- oder Farbgrafikkarte benutzt (Irrelevant, da Farbgrafik bereits mit XT-Systemen als Standard eingeführt wurde!)

  

## Kommunikationswege

  
[<img src="https://raw.githubusercontent.com/wiki/lowlevel-eu/wiki/assets/a827e7311878670cc162.png" width="569" height="437" alt="Kbc logic.png" />](https://raw.githubusercontent.com/wiki/lowlevel-eu/wiki/assets/a827e7311878670cc162.png)  
  

Normalerweise wird der erste Auxiliary Port (PSAUX0\*) für eine Tastatur verwendet und an den zweiten (PSAUX1\*) eine Maus oder ein anderes Zeigegerät angeschlossen. Technisch unterscheiden sich die beiden Ports nicht. Daher kann man dort beliebige Gerätekombinationen anschließen, solange das BIOS nicht mit einer Fehlermeldung stoppt, weil es bestimmte Geräte an bestimmten Ports erwartet. Beliebige Gerätekombinationen werden z. B. von Linux unterstützt, nicht jedoch von Windows.  

(\*Anmerkung zu PSAUX0 und PSAUX1: Diese Begriffe habe ich mir „ausgedacht“, da ich keine vernünftige offizielle Bezeichnung kenne. Man wird diese Begriffe also in keiner anderen Referenz finden, außer es wurde hier abgeschrieben.)  

## USB Legacy Support

Diese von vielen Mainboards bereitgestellte Funktion simuliert angeschlossene USB-Geräte wie Maus und Tastatur als PS/2-Geräte.  
  
Dies hat für Programmierer Vor- und Nachteile. Einerseits muss man für die Unterstützung solcher Eingabegeräte keine eigenen USB-Treiber programmieren. Andererseits können damit folgende Probleme auftreten:  

- Auf manchen Systemen läuft IMMER eine Abstraktionsschicht mit, auch wenn keine USB-Geräte angeschlossen sind. Dies kann zur Folge haben, dass die Intellimaus-Extension nicht funktioniert. Oder dass man nicht, wie weiter oben beschrieben, beliebige Geräte an einen PSAUX-Port anschließen kann (werden nicht erkannt).
- Das [SMM-BIOS](https://github.com/lowlevel-eu/wiki/wiki/System-Management-Mode "SMM"), über welches die USB-zu-PS/2-Abstraktion stattfindet, unterstützt nicht immer den Betrieb über 32-Bit-[Protected-Mode](https://github.com/lowlevel-eu/wiki/wiki/Protected-Mode "Protected Mode"). Die Benutzung erweiterter Speichertechniken oder des [Long Mode](https://github.com/lowlevel-eu/wiki/wiki/Long-Mode "Long Mode") kann das System daher zum Absturz bringen!

  
Diese Probleme sind nicht mehr vorhanden, wenn der Legacy-Modus ausgeschaltet wurde. Dies geschieht während der Initialisierung des USB-Hostcontrollers.

## Programmieren des KBC

Programmiert wird der KBC über die zwei Ports 0x60 und 0x64. Dabei werden auf den Ports nur Bytes gesendet und empfangen.  
  
Über den Port 0x64 kann man das Statusregister auslesen und KBC-Befehle senden.  
  
Der Port 0x60 dient als Ein-/Ausgabe-Puffer. Parameter oder Rückgabewerte für einen Befehl werden über diesen Port geschrieben bzw. gelesen. Wenn keine Befehlsparameter erwartet werden und man auf den Port 0x60 schreibt, wird direkt an PSAUX0 weitergeleitet.  

- Vor dem Schreiben auf Port 0x60 oder 0x64 muss der Eingabepuffer leer sein. (Port\[0x64\].Bit\[1\] == 0)
- Vor dem Lesen von Port 0x60 muss der Ausgabepuffer voll sein (Port\[0x64\].Bit\[0\] == 1)

### Statusregister

Wird vom Port 0x64 gelesen und ist folgendermaßen aufgebaut:

    Bit 76543210
        │││││││└─ Status des Ausgabepuffers (KBC -> CPU): 0=leer; 1=voll (es kann von Port 0x60 gelesen werden)
        ││││││└── Status des Eingabepuffers (KBC <- CPU): 0=leer (Schreiben auf 0x60 oder 0x64 möglich); 1=voll
        │││││└─── 1=Erfolgreicher Selbsttest (Wie Controller_Command_Byte.Bit[3]; sollte immer 1 sein)
        ││││└──── zuletzt benutzter Port: 0=0x60; 1=0x61 oder 0x64?
        │││└───── Tastatursperre: 0=Tastatur gesperrt; 1=Tastatur nicht gesperrt
        ││└────── PSAUX?
        │└─────── Timeout: 1=Tastatur oder PSAUX-Gerät reagiert nicht?
        └──────── Paritätsfehler: 1=Beim letzten gesendeten/empfangenen Byte trat ein Paritätsfehler auf

  

### Input Port P1

Nur aus Vollständigkeitsgründen hier aufgeführt! Wie man auf einem kurzen Blick erkennen kann, sind diese Werte heute nicht mehr relevant. Gelesen wird er über den KBC-Befehl 0xC0.

    Bit 76543210
        │││││││└─ Keyboard data in pin?
        ││││││└── PS/2 mouse in pin?
        │││││└─── Unused in ISA, EISA, PS/2 systems, Can be configured for clock switching
        ││││└──── Unused in ISA, EISA, PS/2 systems, Can be configured for clock switching
        │││└───── Speicher auf dem Mainboard:  0= 512 KB, 1= 256 KB
        │││       
        ││└────── Manufacturing jumper 0=installed, 1=not installed
        ││        with jumper the BIOS runs an infinite diagnostic loop
        │└─────── Grafikkarte: 0=Color Graphics Adapter (CGA), 1=Monochrome Display Adapter (MDA)
        │         Kleiner Tipp: CGA wurde mit den XT-System eingeführt. ;)
        └──────── Tastatursperre: 0=Tastatur gesperrt; 1=Tastatur nicht gesperrt

  

### Outputport

Wird mit dem KBC-Befehl 0xD0 ausgelesen und per 0xD1 geschrieben:

    Bit 76543210
        │││││││└─ 1=CPU-Reset
        ││││││└── 1=A20-Gate eingeschaltet
        │││││└─── ? PS/2 mouse data out
        ││││└──── ? PS/2 mouse clock signal
        │││└───── ? 1: Output buffer full
        ││└────── ? 1: Output buffer PS/2 mouse full
        │└─────── ? Keyboard clock signal
        └──────── ? Keyboard data out

  

### Controller Command Byte

Wird mit dem KBC-Befehl 0x20 ausgelesen und per 0x60 geschrieben:

    Bit 76543210
        │││││││└─ 1=Erzeuge einen IRQ 1, wenn PSAUX0 Daten auf Port 0x60 ausgibt
        ││││││└── 1=Erzeuge einen IRQ 12, wenn PSAUX1 Daten auf Port 0x60 ausgibt
        │││││└─── 1=Erfolgreicher Selbsttest (Wie Statusregister.Bit[3]; sollte immer 1 sein)
        ││││└──── AT  : 1=Tastatursperre Ignorieren (Statusregister Bit4 immer 1)
        ││││      PS/2: 0 (unbenutzt)
        │││└───── 1 = Die Taktleitung zu PSAUX0 auf low halten und damit das Senden/Empfangen unterbinden
        ││└────── EISA, PS/2 : 1 = Die Taktleitung zu PSAUX1 auf low halten und damit das Senden/Empfangen unterbinden
        ││        ISA : 0 = Benutze 11 Bit Übertragung, Paritätsüberprüfung und konvertiere PSAUX0 Bytes*
        ││              1 = Benutze 8086 Übertragung, keine Paritätsüberprüfung oder Konvertierung 
        │└─────── ? 1=Der KBC übersetzt von PSAUX eingehenden Bytes*
        └──────── 0 (reserviert)

  

- [KBC-Scancode-Übersetzung](http://www.win.tue.nl/~aeb/linux/kbd/scancodes-10.html#translationtable)

### KBC-Befehle

Müssen auf Port 0x64 ausgegeben werden (bevor man auf Port 0x64 schreibt, muss der Ausgabepuffer leer sein (Port\[0x64\].Bit\[1\]==0) und die Tastatur darf sich nicht mehr im Resetmodus befinden (Port\[0x64\].Bit\[2\]==1))

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

  

### Tastatur-Befehle

Werden auf Port 0x60 ausgegeben (bevor man auf Port 0x60 schreibt, muss der Ausgabepuffer leer sein (Port\[0x64\].Bit\[1\]==0) und die Tastatur darf sich nicht mehr im Resetmodus befinden (Port\[0x64\].Bit\[2\]==1))

    0xED   Setzen der LEDs auf der Tastatur. Ein zweites Byte wird über Port 0x60 gesendet:

           Bit 76543210
               │││││││└─ Scroll Lock : 0=aus 1=an
               ││││││└── Num Lock    : 0=aus 1=an
               │││││└─── Caps Lock   : 0=aus 1=an
               └┴┴┴┴──── 0

    0xEE   Dieser Befehl ist zum Testen der Tastatur. Die Tastatur sollte mit 0xEE antworten.

    0xF0   Auswählen des Scancodes. Als Parameter den Scancode 1, 2 (Standard) oder 3 an Port 0x60 senden.
           Mit dem Wert 0 als Parameter kann man den aktuellen Scancode von Port 0x60 auslesen

    0xF2   Diesen Befehl sendet man zum Identifizieren der Tastatur. Es gibt folgende Rückgabewerte:

           XT-Tastatur    :  Timeout (leider NICHT Port[0x64].Bit[6]=1, sondern selbst zu messender Zweitwert)
           AT-Tastatur    :  Rückgabewert 0xFA
           MF-II-Tastatur :  Rückgabewert 0xFA 0xAB 0x41

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
               │└┴────── Wartezeit, bevor eine gehaltene Taste wiederholt wird.
               │         00 :  250 ms
               │         01 :  500 ms
               │         10 :  750 ms
               │         11 : 1000 ms
               │
               └──────── 0

    0xF4   Aktivieren der Tastatur. Wenn ein Übertragungsfehler aufgetreten ist, muss           
           die Tastatur mit diesem Kommando neu aktiviert werden, der interne Puffer
           wird dabei gelöscht.

    0xF5   Tastatur deaktivieren und Standardwerte setzen. Der Puffer wird gelöscht, 
           die LEDs werden abgeschaltet, Wiederholrate und Wartezeit werden auf 
           Standardwerte zurückgesetzt und die Tastatur wird deaktiviert (es werden 
           keine Tastenanschläge mehr übertragen)

    0xF6   Standardwerte setzen

    0xFE   Wird nur intern vom Keyboardcontroller an die Tastatur gesendet. Ist nicht
           für die Nutzung mit der CPU gedacht.

    0xFF   Tastatur-Reset und Selbsttest. Rückgabe 0xAA, wenn Test erfolgreich, sonst 
           0xFC

## Tastaturtreiber

Im Folgenden soll genauer auf die Ansteuerung der Tastatur als ganzes eingegangen werden, also das Auslesen und Verarbeiten der vom Benutzer gedrückten Tasten. Dabei wird nur die manuelle Ansteuerung ohne BIOS-Funktionen behandelt, wie sie benötigt wird, wenn die Tastatur im Protected Mode angesteuert werden soll. Es wird davon ausgegangen, dass die entsprechenden Grundlagen für den Treiber gegeben sind (IRQ-Behandlung, Port-Funktionen).

### Initialisierung

Bevor man die Tastatur benutzt, ist es ratsam, sie erst einmal in einen bekannten, sauberen Zustand zu bringen. Im [Tastaturtreiber von týndur](http://git.tyndur.org/?p=tyndur.git;a=blob;f=src/modules/kbc/keyboard.c) hat sich nach einigem Herumexperimentieren mit verschiedenen Emulatoren die folgende einfache Initialisierung bewährt:

- Solange das Bit 0 im Statusregister (Puffer voll) gesetzt ist, Bytes aus dem Datenregister lesen. Das hilft, wenn schon vor der Initialisierung des Treibers irgendwelche Tasten betätigt wurde, da der KBC dann keine weiteren Zeichen sendet, bis der Puffer geleert (ausgelesen wurde). Das tritt zum Beispiel im Zusammenhang mit GRUB oft auf, wenn der Benutzer die Taste zu lange gedrückt hält.
- Tastatur mit Befehl 0xF4 aktivieren. Andere Kombinationen wurden auch getestet, haben aber Probleme bereitet, unter anderem war Zeitweise ein Reset der Tastatur drin, was dazu geführt hat, dass diese unter gewissen Emulatoren überhaupt nicht mehr funktionierte.

Dieser Code könnte beispielsweise folgendermaßen aussehen: \<c\> static void send_command(uint8_t command); void init_keyboard(void) {

       // IRQ-Handler fuer Tastatur-IRQ(1) registrieren
       register_intr_handler(IRQ_BASE + 1, &irq_handler);

       // Tastaturpuffer leeren
       while (inb(0x64) & 0x1) {
           inb(0x60);
       }   

       // Tastatur aktivieren
       send_command(0xF4);

}

/\*\* Befehl an die Tastatur senden \*/ static void send_command(uint8_t command) {

       // Warten bis die Tastatur bereit ist, und der Befehlspuffer leer ist
       while ((inb(0x64) & 0x2)) {}
       outb(0x60, command);

} \</c\>

In einem vernünftigen Betriebssystem möchte man die Tastatur wahrscheinlich mit IRQs nutzen, damit man jeweils benachrichtigt wird, wenn eine Taste gedrückt wird, und nicht darauf warten muss. Dabei ist es wichtig, dass die Routine zur Behandlung der Tastatur-IRQs vor der oben angegebenen Initialisierung erfolgt, da sich sonst möglicherweise üble [Race-Conditions](https://github.com/lowlevel-eu/wiki/wiki/Race-Condition "Race Condition") ergeben, also konkret, wenn der Puffer bereits geleert wurde und noch vor dem Registrieren der IRQ-Routine eine Taste gedrückt wird, dann ist der Puffer der Tastatur voll, und sie schickt somit auch keine IRQs mehr, bis er geleert wird, was aber dann nicht mehr passiert, und die Tastatur hängt somit.

### IRQ-Handler

Nun sind wir also bereit, Tastendrücke von der Tastatur einzulesen. Im Folgenden wird genauer darauf eingegangen, wie wir die Tastendrücke, die wir vom Controller über einen IRQ signalisiert erhalten, verarbeiten können.

Der erste und wichtigste Schritt in unserer IRQ-Behandlungsroutine ist es, das vom Tastaturkontroller bereitgestellte Byte aus dem Puffer zu lesen. In einem weiteren Schritt müssen wir jetzt entscheiden, womit wir es bei diesem Byte nun genau zu tun haben. Eine erste Unterscheidung, die wir machen müssen, ist die Unterteilung in gedrückte und gelöste Tasten, was uns durch das oberste Bit im eingelesenen Byte signalisiert wird.

Der Rest des Bytes ist ein Scancode, der uns angibt um welche Taste es sich handelt. Dieser Scancode hat überhaupt nichts mit irgendwelchen Zeichen zu tun, er gibt uns nur, an welche Taste gedrückt oder gelöst wurde und muss von uns manuell mit einer Scancode-Tabelle in die korrespondierenden Zeichen umgewandelt werden. Dabei muss man sich bewusst sein, dass für die Tastatur eine Steuertaste, wie zum Beispiel die Umschalttaste oder Capslock, genau das selbe ist wie beispielsweise ein „a“. Wird beispielsweise \[Umschalt\]+\[a\] gedrückt, um ein großes „a“ zu erhalten, schickt uns der Tastaturcontroller 2 Bytes, eines Umschalttaste gedrückt und ein anderes „a“ gedrückt. Es ist also Aufgabe des Treibers, diese Tasten entsprechend zu interpretieren.

Um das Ganze noch komplizierter zu machen, gibt es noch so genannte *Extented* Scancodes*, davon gibt es zwei verschiedene Sorten. Diese werden mit E0 und E1* bezeichnet, und bestehen aus zwei respektive drei Bytes. Das erste Byte eines E0-Scancodes hat überraschenderweise den Wert 0xE0, während das zweite Byte beinhaltet, um welchen e0-Scancode es sich genau handelt. E1-Scancodes bestehen aus 3 Bytes, das erste hat den Wert 0xE1, während die folgenden zwei Bytes zu einem Scancode-Wert kombiniert werden. Dabei muss beachtet werden, dass bei den Extended-Scancodes das Bit 8 des zweiten und dritten Bytes darüber Aufschluss gibt, ob es sich um eine gedrückte oder eine gelöste Taste handelt. Die einzelnen Bytes der E0-Scancodes werden mit unterschiedlichen IRQs gesendet, man muss sich den aktuellen Zustand im Code also irgendwie merken. Bei Extended Scancodes gibt es noch eine weitere Stolperfalle und zwar sind das die so genannten *„fake* shifts“ *[vgl.](http://www.win.tue.nl/~aeb/linux/kbd/scancodes-1.html#ss1.6)*

So, nun wissen wir also, mit welchem Scancode wir es zu tun haben. Als nächstes müssen wir den seltsamen Scancode jetzt in etwas sinnvolles umwandeln. Hier gibt es jetzt zwei Möglichkeiten, entweder wir wandeln sie direkt in ASCII-Zeichen (oder welche Kodierung auch immer) um oder wir wandeln sie in ein internes Format um (meist Keycodes genannt), welches wir dann weitergeben.

Auch hier wieder ein kleiner Codeabschnitt, der zeigt wie man den IRQ-Handler umsetzen könnte (aus týndur übernommen, BSD-Lizenz): \<c\> /\*\*

    * Scancode in einen Keycode uebersetzen
    * @return Keycode oder 0 falls der Scancode nicht bekannt ist
    */

uint8_t translate_scancode(int set, uint16_t scancode);

void irq_handler(uint8_t irq) {

       uint8_t scancode;
       uint8_t keycode = 0;
       int break_code = 1;

       // Status-Variablen fuer das Behandeln von e0- und e1-Scancodes
       static int     e0_code = 0;
       // Wird auf 1 gesetzt, sobald e1 gelesen wurde, und auf 2, sobald das erste
       // Datenbyte gelesen wurde
       static int      e1_code = 0;
       static uint16_t  e1_prev = 0;

       scancode = inb(0x60);

       // Um einen Breakcode handelt es sich, wenn das oberste Bit gesetzt ist und
       // es kein e0 oder e1 fuer einen Extended-scancode ist
       if ((scancode & 0x80) &&
           (e1_code || (scancode != 0xE1)) &&
           (e0_code || (scancode != 0xE0)))
       {
           break_code = 0;
           scancode &= ~0x80;
       }

       if (e0_code) {
           // Fake shift abfangen und ignorieren
           if ((scancode == 0x2A) || (scancode == 0x36)) {
               e0_code = 0;
               return;
           }

           keycode = translate_scancode(1, scancode);
           e0_code = 0;
       } else if (e1_code == 2) {
           // Fertiger e1-Scancode
           // Zweiten Scancode in hoeherwertiges Byte packen
           e1_prev |= ((uint16_t) scancode << 8);
           keycode = translate_scancode(2, e1_prev);
           e1_code = 0;
       } else if (e1_code == 1) {
           // Erstes Byte fuer e1-Scancode
           e1_prev = scancode;
           e1_code++;
       } else if (scancode == 0xE0) {
           // Anfang eines e0-Codes
           e0_code = 1;
       } else if (scancode == 0xE1) {
           // Anfang eines e1-Codes
           e1_code = 1;
       } else {
           // Normaler Scancode
           keycode = translate_scancode(0, scancode);
       }
           // Zum Testen sollte folgendes verwendet werden:

kprintf("%c", keycode);

           //Nach erfolgreichen Tests, könnte eine send_key_event Funtkion wie bei Týndur verwendet werden

} \</c\>

Dieses Codestück unternimmt genau die oben beschriebenen Schritte. Die Funktion „translate_scancode“ übersetzt, wie oben im Kommentar angegeben, die Scancodes in interne Keycodes der Code dazu findet sich ebenfalls im [tyndur-Repository](http://git.tyndur.org/?p=tyndur.git;a=blob;f=src/modules/kbc/sc2kc.c). Es handelt sich dabei aber nur um eine mögliche Umsetzung und keineswegs um die einzig mögliche, hier muss man sich selbst überlegen wie das für den konkreten Anwendungsfall am komfortabelsten ist.

## Beispiele zur Benutzung der KBC Funktionen

### CPU-Reset

Der CPU-Reset wird ausgelöst, indem der Wert 0xFE in den Outputport geschrieben wird. \<asm\>

Warten, bis der Eingabepuffer leer ist

wait1: in al, 0x64 test al, 00000010b jne wait1

Befehl 0xD1 zum Schreiben des Inputports an den KBC senden

mov al, 0xD1 out 0x64, al

Wieder warten, bis der Eingabepuffer leer ist

wait2: in al, 0x64 test al, 00000010b jne wait2

Den neuen Wert für den Inputport über Port 0x60 senden

mov al, 0xFE out 0x60, al \</asm\>

# Links

- <http://www.win.tue.nl/~aeb/linux/kbd/scancodes-1.html>
- [SMS "8042" Datenblatt](http://www.diakom.ru/el/elfirms/datashts/Smsc/42w11.pdf)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/11088/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1468/index.html)

<!-- MediaWiki page 1468; revision 11088; parent 10545; 2013-03-29T20:45:23Z -->
