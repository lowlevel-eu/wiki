# Keyboard Controller

Der **Keyboard-Controller** oder auch **KBC** ist ein Baustein auf dem Mainboard und dient (unter anderem) der Tastaturansteuerung. Von IBM ursprünglich entwickelt, wurde der Keyboard-Controller in seiner Funktion stark erweitert, wodurch sich heutzutage viele Aufgaben über seligem erledigen lassen.

  
Der KBC wurde mit dem AT System (286) eingeführt. In dem Vorgängersystem XT wurde für vergleichbare Aufgaben das Programmable Peripheral Interface (PPI) genutzt.

## Funktionen des KBC

- Ansteuerung eines oder zweier Auxiliary Port(s) (Tastatur, Maus)

<!-- -->

- ein-/ausschalten der 21-Adressleitung ([A20-Gate](https://github.com/lowlevel-eu/wiki/wiki/A20-Gate "A20-Gate"); Sollte aus Performance-Gründen in aktuellen Systemen direkt über die CPU aktiviert werden.)

<!-- -->

- CPU-Reset auslösen, also neustarten des Systems

<!-- -->

- Zusammen mit dem [PIT](https://github.com/lowlevel-eu/wiki/wiki/Programmable-Interval-Timer "Programmable Interval Timer") den [Systemlautsprecher](https://github.com/lowlevel-eu/wiki/wiki/Systemlautsprecher "Systemlautsprecher") ansteuern.

<!-- -->

- Information ob das System eine Monochrom- oder Farbgrafikkarte benutzt (Irrelevant: Farbgrafik wurde mit XT Systemen als Standard eingeführt!)

  

## Kommunikationswege

  
![kbclogic20071105bt5.png](http://img441.imageshack.us/img441/636/kbclogic20071105bt5.png)  
  

Normalerweise wird der erste Auxiliary Port (PSAUX0\*) für eine Tastatur verwendet und an den zweiten (PSAUX1\*) ein Maus oder ein anderes Zeigegerät angeschlossen. Technisch unterscheiden sich die beiden Ports nicht. Daher kann man dort beliebige Gerätekombinationen anschließen, solange das BIOS nicht mit einer Fehlermeldung stoppt, weil es bestimmte Geräte an bestimmten Ports erwartet. Beliebige Gerätekombinationen werden z.B. von Linux unterstützt, nicht jedoch von Windows.  

(\*Anmerkung zu PSAUX0 und PSAUX1: Diese Begriffe habe ich mir "ausgedacht", da ich keine vernünftige offizielle Bezeichnung kenne. Man wird diese Begriffe also in keiner anderen Referenz finden. Außer es wurde hier abgeschrieben.)  

## USB Legacy Support

Diese von vielen Mainboards bereitgestellte Funktion simuliert angeschlossene USB-Geräte wie Maus und Tastatur als PS/2 Geräte.  
  
Dies hat für Programmierer Vor- und Nachteile. Einerseits muss man für die Unterstützung solcher Eingabegeräte keine eigenen USB Treiber programmieren. Andererseits ergeben sich damit einige der hier aufgelisteten Probleme:  

- Auf manchen Systemen Läuft IMMER eine Abstraktionsschicht mit, auch wenn keine USB Geräte angeschlossen sind. Dies kann zur folge haben, dass die Intellimaus-Extension nicht funktioniert. Oder dass man nicht, wie weiter oben beschrieben, beliebige Geräte an ein PSAUX Port anschließen kann. (wird nicht erkannt)
- Das [SMM BIOS](https://github.com/lowlevel-eu/wiki/wiki/System-Management-Mode "SMM"), über welches die USB zu PS/2 Abstraktion stattfindet, unterstützen nicht immer den Betrieb über 32Bit [Protected Mode](https://github.com/lowlevel-eu/wiki/wiki/Protected-Mode "Protected Mode"). Die Benutzung erweiterter Speichertechniken oder des [Long Mode](https://github.com/lowlevel-eu/wiki/wiki/Long-Mode "Long Mode") kann das System daher zum Abstürzen bringen!

  
Diese Probleme sind nicht mehr vorhanden wenn der Legacy-Modus ausgeschaltet wurde.  
  
Nach meinen Informationen wird der Legacy-Modus ausgeschaltet sobald der USB-Chip initialisiert wird. Also die Hardware weiß, dass die Software die USB Geräte direkt ansteuern kann. (Ist diese Information korrekt?)

## Programmieren des KBC

Programmiert wird der KBC über die 2 Ports 0x60 und 0x64. Dabei werden auf den Ports nur Bytes gesendet und empfangen.  
  
Über den Port 0x64 kann man das Statusregister auslesen und KBC-Befehle senden.  
  
Der Port 0x60 dient als Ein-/Ausgabe Puffer. Parameter oder Rückgabewerte für einen Befehl werden über diesen Port geschrieben bzw. gelesen. Wenn keine Befehlsparameter erwartet werden und man auf den Port 0x60 schreibt, wird direkt an PSAUX0 weitergeleitet.  

- Vor dem Schreiben auf Port 0x60 oder 0x64 muss der Eingabepuffer leer sein. (Port\[0x64\].Bit\[1\] == 0)
- Vor dem Lesen von Port 0x60 muss der Ausgabepuffer voll sein (Port\[0x64\].Bit\[0\] == 1)

### Statusregister

lesen von Port 0x64

    Bit 76543210
        │││││││└─ Status des Ausgabepuffers (KBC -> CPU) :  0=leer;  1=voll (es kann von Port 0x60 gelesen werden)
        ││││││└── Status des Eingabepuffers (KBC <- CPU) :  0=leer (Schreiben auf 0x60 oder 0x64 möglich);  1=voll
        │││││└─── 1=Erfolgreicher Selbsttest (Wie Controller_Command_Byte.Bit[3]; sollte immer 1 sein)
        ││││└──── zuletzt benutzter Port : 0=0x60;  1=0x61 oder 0x64?
        │││└───── Tastatursperre : 0=Tastatur gesperrt; 1=Tastatur nicht gesperrt
        ││└────── PSAUX?
        │└─────── Timeout : 1=Tastatur oder PSAUX-Gerät ragiert nicht?
        └──────── Paritätsfehler : 1=Beim letzten Byte Senden/Empfangen trat ein Paritätsfehler auf

  

### Input Port P1

Nur aus Vollständigkeitsgründen hier aufgeführt!!! Wie man mit einem kurzen Blick erkennen kann heute nicht mehr relevant! Lesen über KBC-Befehl 0xC0

    Bit 76543210
        │││││││└─ Keyboard data in pin?
        ││││││└── PS/2 mouse in pin?
        │││││└─── Unused in ISA, EISA, PS/2 systems, Can be configured for clock switching
        ││││└──── Unused in ISA, EISA, PS/2 systems, Can be configured for clock switching
        │││└───── Speicher auf dem Mainboard:  0= 512 KB, 1= 256 KB
        │││       
        ││└────── Manufacturing jumper 0= installed, 1= not installed
        ││        with jumper the BIOS runs an infinite diagnostic loop
        │└─────── Grafikkarte: 0=Color Graphics Adapter (CGA), 1=Monochrome Display Adapter (MDA)
        │         Kleiner Tip: CGA wurde mit den XT System eingeführt. ;)
        └──────── Tastatursperre : 0=Tastatur gesperrt;  1=Tastatur nicht gesperrt

  

### Outputport

Lesen über KBC-Befehl 0xD0  
schreiben über KBC-Befehl 0xD1

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

Lesen über KBC-Befehl 0x20  
Schreiben über KBC-Befehl 0x60

    Bit 76543210
        │││││││└─ 1=Erzeuge einen IRQ1 wenn PSAUX0 daten auf Port 0x60 ausgibt
        ││││││└── 1=Erzeuge einen IRQ12 wenn PSAUX1 daten auf Port 0x60 ausgibt
        │││││└─── 1=Erfolgreicher Selbsttest (Wie Statusregister.Bit[3]; sollte immer 1 sein)
        ││││└──── AT  : 1=Tastatursperre Ignorieren (Statusregister Bit4 immer 1)
        ││││      PS/2: 0 (unbenutzt)
        │││└───── 1 = Die Taktleitung zu PSAUX0 auf low halten und damit das Senden/Empfangen unterbinden
        ││└────── EISA, PS/2 : 1 = Die Taktleitung zu PSAUX1 auf low halten und damit das Senden/Empfangen unterbinden
        ││        ISA : 0 = Benutze 11 Bit Übertragung, Paritätsüberprüfung und konvertiere PSAUX0 Bytes*
        ││              1 = Benutze 8086 Übertragung, keine Paritätsüberprüfung oder Konvertierung 
        │└─────── ? 1=Der KBC übersetzt von PSAUX eingehenden Bytes*
        └──────── 0 (reserviert)

  

- KBC Scancode-Übersetzung: <http://www.win.tue.nl/~aeb/linux/kbd/scancodes-10.html#translationtable>

  

### KBC-Befehle

schreiben auf Port 0x64 (Bevor man auf Port 0x64 schreibt, muss der Ausgabepuffer leer sein (Port\[0x64\].Bit\[1\]==0) und die Tastatur darf sich nicht mehr im Resetmodus befinden (Port\[0x64\].Bit\[2\]==1))

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

schreiben auf Port 0x60 (Bevor man auf Port 0x60 schreibt, muss der Ausgabepuffer leer sein (Port\[0x64\].Bit\[1\]==0) und die Tastatur darf sich nicht mehr im Resetmodus befinden (Port\[0x64\].Bit\[2\]==1))

    0xED   Setzen der LEDs auf der Tastatur. Ein zweites Byte wird über Port 0x60 gesendet:

           Bit 76543210
               │││││││└─ Scroll Lock : 0=aus 1=an
               ││││││└── Num Lock    : 0=aus 1=an
               │││││└─── Caps Lock   : 0=aus 1=an
               └┴┴┴┴──── 0

    0xEE   Dieser Befehl ist zum testen der Tastatur. Die Tastatur sollte mit 0xEE antworten.

    0xF0   Auswählen des Scancodes. Als Parameter den Scancode 1, 2(standard) oder 3 auf Port 0x60 senden.
           Mit dem Wert 0 als Parameter kann man den aktuellen Scancode auslesen

    0xF2   Diesen Befehl sendet man zum identifizieren der Tastatur. Es gibt folgende Rückgabewerte:

           XT Tastatur    :  Timeout (leider NICHT Port[0x64].Bit[6]=1, sondern selbst zu messender Zweitwert)
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

    0xF4   Aktivieren der Tastatur. Wenn ein Übertragungsfehler aufgetreten ist, muss           
           die Tastatur mit diesem Kommando neu aktiviert werden, der interne Puffer
           wird dabei gelöscht.

    0xF5   Tastatur deaktivieren und Standardwerte setzen. Der Puffer wird gelöscht, 
           die LEDs werden abgeschaltet, Wiederholrate und Wartezeit werden auf 
           Standardwerte zurückgesetz und die Tastatur wird deaktiviert (es werden 
           keine Tastenanschläge mehr übertragen)

    0xF6   Standardwerte setzen

    0xFE   Wird nur intern vom Keyboardcontroller an die Tastatur gesendet. Ist nicht
           für die Nutzung mit der CPU gedacht.

    0xFF   Tastatur-Reset und Selbst-test. Rückgabe 0xAA wenn Test erfolgreich, sonst 
           0xFC

## Beispiele zur Benutzung der KBC Funktionen

### Ein einfacher Tastatur Handler in Form eines Bootsektors

Dieses Beispiel zeigt, wie man die Tastatur im Realmode benutzen kann. Dabei wird bei jedem Tastendruck oder loslassen einer Taste der Scancode ausgegeben. Der Quellcode kann mit NASM oder FASM assembliert werden. Die erzeugte Datei auf den Bootsektor einer Diskette kopieren oder direkt mit einem Emulator benutzen.

\<asm\> use16 org 0x7C00

cli

xor ax, ax push ax pop ds

Standardmäßig ist der IRQ1 im Realmode auf dem Interrupt 9 gemapt

mov word\[ds:(9\*4) \], keyboard_handler  ;Offset mov word\[ds:(9\*4)+2\], 0  ;Segment

sti

jmp \$

  
keyboard_handler:

     pusha

     ;scancode lesen
     in  al, 0x60

     ;Hier kann man mit dem Scancode machen was man will :)
     call write_byte_as_hex
     mov  al, '|'
     call bios.write_char

     ;dem PIC1 sagen, dass wir den IRQ verarbeitet haben
     mov al, 0x20
     out 0x20, al

     popa

iret

  

Input  
al = char

bios.write_char:

     pusha
     mov  ah, 0x0E
     int  0x10
     popa

ret

hex_chars: db '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F'

Input  
al = byte

write_byte_as_hex:

     pusha
     and  ax, 0xFF
     push ax
     mov  bx, ax
     shr  bx, 4
     mov  al, [hex_chars+bx]
     call bios.write_char
     pop  bx
     and  bx, 0xF
     mov  al, [hex_chars+bx]
     call bios.write_char
     popa

ret

times 510-(\$-\$\$) db 0 dw 0xAA55 \</asm\>

### CPU-reset

Der CPU-Reset wird ausgelöst indem der Wert 0xFE in das Outputport geschrieben wird. \<asm\>

Warten bis der Eingabepuffer leer ist

wait1: in al, 0x64 test al, 00000010b jne wait1

Befehl 0xD1 zum schreiben des Inputports an den KBC senden

mov al, 0xD1 out 0x64, al

Wieder warten bis der Eingabepuffer leer ist

wait2: in al, 0x64 test al, 00000010b jne wait2

Den neuen Wert für den Inputport über Port 0x60 senden

mov al, 0xFE out 0x60, al \</asm\>

# Links

- <http://www.win.tue.nl/~aeb/linux/kbd/scancodes-1.html>

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/5323/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1468/index.html)

<!-- MediaWiki page 1468; revision 5323; parent 4959; 2009-08-06T15:57:10Z -->
