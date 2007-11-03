# Keyboard Controller

Der Keyboard Controller (KBC) sitzt auf dem Mainboard und dient, wie der Name vermuten lässt, unter anderem der Tastaturansteuerung. Da IBM ihn nach seiner Einführung stark erweitert hat, kann man ihn in heutigen Systemen eher als Kontroller "für alles mögliche" ansehen.

Der KBC wurde mit dem AT System (286) eingeführt. In dem Vorgängersystem XT wurde für vergleichbare Aufgaben das Programmable Peripheral Interface (PPI) genutzt.

## Funktionen des KBC

- Ansteuerung eines oder zweier Auxiliary Port(s) (Tastatur, Maus)

<!-- -->

- ein-/ausschalten der 21-Adressleitung ([A20-Gate](https://github.com/lowlevel-eu/wiki/wiki/A20-Gate "A20-Gate"); Sollte aus Performance-Gründen in aktuellen Systemen direkt über die CPU aktiviert werden.)

<!-- -->

- CPU-Reset auslösen, also neustarten des Systems

<!-- -->

- Zusammen mit dem [PIT](https://github.com/lowlevel-eu/wiki/wiki/Programmable-Interval-Timer "Programmable Interval Timer") den [Systemlautsprecher](https://github.com/lowlevel-eu/wiki/wiki/Systemlautsprecher "Systemlautsprecher") steuern.

<!-- -->

- Information ob das System eine Monochrom- oder Farbgrafikkarte benutzt

  

## Kommunikationswege

  
![kbclogic20071103ev6.png](http://img229.imageshack.us/img229/3005/kbclogic20071103ev6.png)  
  
Programmiert wird der KBC über die 3 Ports 0x60, 0x61 und 0x64.  

Normalerweise wird das erste Auxiliary Port (PSAUX0\*) für eine Tastatur verwendet und an das zweite (PSAUX1\*) ein Maus oder ein anderes Zeigegerät angeschlossen. Technisch unterscheiden sich die beiden Ports nicht. Daher kann man dort beliebige Gerätekombinationen anschließen, solange das BIOS nicht mit einer Fehlermeldung stoppt, weil es bestimmte Geräte an bestimmten Ports erwartet. Beliebige Gerätekombinationen werden z.B. von Linux unterstützt, nicht jedoch von Windows.  

(\*Anmerkung zu PSAUX0 und PSAUX1: Diese Begriffe habe ich mir "ausgedacht", da ich keine vernünftige offizielle Bezeichnung kenne. Man wird diese Begriffe also in keiner anderen Referenz finden. Außer es wurde hier abgeschrieben.)  

## Programmieren des KBC

### Statusregister

lesen von Port 0x64

    Bit 76543210
        │││││││└─ Status des Ausgabepuffers (KBC -> CPU) :  0=leer;  1=voll (es kann von Port 0x60 gelesen werden)
        ││││││└── Status des Eingabepuffers (KBC <- CPU) :  0=leer (Schreiben auf 0x60 oder 0x64 möglich);  1=voll
        │││││└─── Systemstatus? :  0=Reset/Selbsttest wird gerade ausgeführt;  1=Selbsttest OK
        ││││└──── zuletzt benutztes Port : 0=0x60;  1=0x61 oder 0x64?
        │││└───── Tastatursperre : 0=Tastatur gesperrt; 1=Tastatur nicht gesperrt
        ││└────── PSAUX?
        │└─────── Timeout : 1=Tastatur oder PSAUX-Gerät ragiert nicht?
        └──────── Paritätsfehler : 1=Beim letzten Senden/Empfangen trat ein Paritätsfehler auf

  

### Inputport

Lesen über KBC-Befehl 0xC0

    Bit 76543210
        │││││││└─ Keyboard data in pin?
        ││││││└── PS/2 mouse in pin?
        │││││└─── Reserviert
        ││││└──── Reserviert
        │││└───── Reserviert
        ││└────── Reserviert
        │└─────── Wether you have a color or mono screen?
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

  

  

### Port 0x61

lesen und schreiben

    Bit 76543210
        │││││││└─ PPI \
        ││││││└── PPI  \
        │││││└─── PPI   |Dieser Teil ist vom Programmable Peripheral Interface
        ││││└──── PPI   |nicht überschreiben!
        │││└───── PPI  /
        ││└────── PPI /
        │└─────── Setzt die "clock"-Leitung auf low, so dass die Tastatur keine Daten an den PC senden kann
        └──────── 0=Tastatur eingeschaltet;  1=Tastatur ausgeschaltet

  

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
           (Anmerkung: Kann man mit dem Wert 0 als Parameter den aktuellen Scancode auslesen?)

    0xF2   Diesen Befehl sendet man zum identifiziren der Tastatur. Es gibt folgende Rückgabewerte:

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

    0xF4   ?
    0xF5   ?
    0xF6   ?

    0xFE   ?

    0xFF   ?

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

wait: in al, x064 test al, 00000010b jne wait

Befehl 0xD1 zum schreiben des Inputports an den KBC senden

mov al, 0xD1 out 0x64, al

Wieder warten bis der Eingabepuffer leer ist

wait2: in al, x064 test al, 00000010b jne wait2

Den neuen Wert für das Inputport über Port 0x60 senden

mov al, 0xFE out 0x60, al \</asm\>

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/2216/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1468/index.html)

<!-- MediaWiki page 1468; revision 2216; parent 2215; 2007-11-03T14:53:33Z -->
