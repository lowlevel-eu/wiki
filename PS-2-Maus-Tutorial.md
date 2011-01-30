# PS/2-Maus Tutorial

| PS/2-Maus |  |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Schwierigkeit**: [<img src="https://raw.githubusercontent.com/wiki/lowlevel-eu/wiki/assets/f49eb9cc36b09af043f1.gif" width="16" height="16" alt="Stern gold.gif" />](https://raw.githubusercontent.com/wiki/lowlevel-eu/wiki/assets/f49eb9cc36b09af043f1.gif)[<img src="https://raw.githubusercontent.com/wiki/lowlevel-eu/wiki/assets/f49eb9cc36b09af043f1.gif" width="16" height="16" alt="Stern gold.gif" />](https://raw.githubusercontent.com/wiki/lowlevel-eu/wiki/assets/f49eb9cc36b09af043f1.gif)[<img src="https://raw.githubusercontent.com/wiki/lowlevel-eu/wiki/assets/e092c7d3c71af0daba80.gif" width="16" height="16" alt="Stern weiß.gif" />](https://raw.githubusercontent.com/wiki/lowlevel-eu/wiki/assets/e092c7d3c71af0daba80.gif)[<img src="https://raw.githubusercontent.com/wiki/lowlevel-eu/wiki/assets/e092c7d3c71af0daba80.gif" width="16" height="16" alt="Stern weiß.gif" />](https://raw.githubusercontent.com/wiki/lowlevel-eu/wiki/assets/e092c7d3c71af0daba80.gif)[<img src="https://raw.githubusercontent.com/wiki/lowlevel-eu/wiki/assets/e092c7d3c71af0daba80.gif" width="16" height="16" alt="Stern weiß.gif" />](https://raw.githubusercontent.com/wiki/lowlevel-eu/wiki/assets/e092c7d3c71af0daba80.gif)<br> |  |
| Benötigtes Vorwissen: | [IRQ](https://github.com/lowlevel-eu/wiki/wiki/Programmable-Interrupt-Controller#irq-tabelle "IRQ"), [PIC](https://github.com/lowlevel-eu/wiki/wiki/Programmable-Interrupt-Controller "PIC"), [KBC](https://github.com/lowlevel-eu/wiki/wiki/Keyboard-Controller "KBC") |
| Sprache: | C |

  
Die Maus ist neben der Tastatur eines der wichtigsten Eingabemittel. Über den Keyboard Controller kann das Betriebssystem mit ihr kommunizieren, der hierfür vorgeschriebene Ablauf ist im sogenannten PS/2-Protokoll beschrieben.

Dieses Tutorial geht nicht auf alle Aspekte der PS/2-Maus ein, sondern liefert nur einen Leitfaden zur Programmierung. Für Details siehe [PS/2-Maus](https://github.com/lowlevel-eu/wiki/wiki/PS-2-Maus "PS/2-Maus").

## Der Keyboard-Controller

Der Keyboard Controller wurde entwickelt, um zwei Eingabegeräte zu steuern. Das erste ist die Tastatur, das zweite in der Regel die Maus. Die Tastatur sendet einen IRQ1, wenn sie Daten für die CPU hat, also wenn der Benutzer eine Taste gedrückt hat. Die Maus verwendet dafür den IRQ12. Die Maus selbst und das Senden des IRQ12 müssen aber erst durch den Keyboard Controller aktiviert werden. Der Keyboard Controller ist über die Ports 0x60 und 0x64 ansprechbar. Der Port 0x60 dient dabei als Datenpuffer, der Port 0x64 als Status- und Befehlsregister:

- Lesen von 0x60 liefert den Inhalt des Output Puffers.
- Schreiben nach 0x60 schreibt Daten in den Input Puffer.
- Lesen von 0x64 liefert das Statusbyte des Keyboard Controllers.
- Schreiben nach 0x64 sendet einen Befehl an den Keyboard Controller.

## Das Statusregister

Das Statusregister kann jederzeit vom Port 0x64 gelesen werden. Hier sind die ersten beiden Bits wichtig:

| Bit | gelöscht (0) | gesetzt (1) |
| ----- | -------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| 0 | Es befinden sich keine Daten im Output Puffer. | Es befinden sich Daten im Output Puffer, das Lesen vom Port 0x60 ist somit erlaubt. |
| 1 | Der Input Puffer ist leer. Es dürfen Befehle über die Ports 0x60 und 0x64 gesendet werden. | Es befinden sich noch Daten im Input Puffer. Der Keyboard Controller nimmt momentan keine Befehle an. |

Die anderen Bits sind erst einmal irrelevant.

## Verwendung des Daten Puffers

Einige der weiter unten aufgeführten Befehle erwarten zusätzliche Daten. Diese werden über den Input Puffer (Port 0x60) übergeben. Das Schreiben in den Input Puffer ist aber nur erlaubt, wenn Bit 1 im Statusregister gelöscht ist. Die folgende Funktion wartet darauf, dass das Bit 1 gelöscht ist und sendet dann die Daten:

\<c\> VOID kbc_write_inbuf(BYTE data) {

     DWORD to = 255;
     while ( inb(0x64) & 0x02)
     {
       if (! (to--) )
       {
         kprintf(“mouse timeout!”);
         return;
       }
     }
     outb(0x60, data);

} \</c\>

Andere Befehle des Keyboard Controllers liefern Daten zurück. Diese werden dann aus dem Output Puffer (Port 0x60) gelesen. Hier muss darauf gewartet werden, dass das Bit 0 im Statusregister gesetzt ist:

\<c\> BYTE kbc_read_outbuf() {

     DWORD to = 255;
     while ( ! (inb(0x64) & 0x01) )
     {
       if (! (to--) )
       {
         kprintf(“mouse timeout!”);
         return;
       }
     }
     return inb(0x60);

} \</c\>

## Befehle des Keyboard Controllers

Befehle an den Keyboard Controller werden zum Port 0x64 geschrieben. Auch hier muss vor dem Senden darauf gewartet werden, dass das Bit 1 des Statusregisters gelöscht ist:

\<c\> VOID kbc_send_cmd (BYTE cmd) {

     DWORD to = 255;
     BYTE kbc_status = inb(KBC_STATUS);
     while ( inb(0x64) & 0x02)
     {
       if (! (to--) )
       {
          kprintf(“mouse timeout!”);
          return;   
       }
       sleep(10);
     }
     outb (0x64, cmd);

} \</c\>

Der Keyboard Controller kennt einige Befehle. Hier eine Auswahl der Befehle, die man zur Ansteuerung der Maus benötigt:

| Wert | Beschreibung |
| ------ | ------------------------------------------------------------ |
| 0xA8 | Mause aktivieren |
| 0xA7 | Maus deaktivieren |
| 0x20 | Command Byte lesen |
| 0x60 | Command Byte schreiben |
| 0xD4 | sende den nächsten Befehl an die Maus anstatt zur Tastatur |

### Maus aktivieren (0xA8) und deaktiveren (0xA7)

Der Keyboard Controller kann zwei Eingabegeräte steuern. Standardmäßig ist aber nur das erste, nämlich die Tastatur, aktiviert. Mit diesem Befehl wird auch die das zweite Eingabegerät, nämlich die Maus aktiviert. Das kann natürlich auch wieder rückgängig gemacht werden.

### Command Byte lesen (0x20)

Das Command Byte befindet sich im RAM des Keyboard Controllers. Es enthält ein für uns wichtiges Bit, nämlich Bit 1. Ist dieses gesetzt, dann sendet die Maus immer einen IRQ12, wenn es neue Daten für uns hat (also wenn der Benutzer die Maus bewegt hat). Zum Lesen des Command Bytes muss man zuerst den Befehl 0x20 an den Keyboard Controller senden, woraufhin dieser das Byte im Output Puffer (0x60) platziert.

### Command Byte schreiben (0x60)

Zum Schreiben muss man zuerst den Befehl 0x60 an den Keyboard Controller senden und danach das Command Byte im Input Puffer platzieren.

### Befehl an die Maus senden (0xD4)

Der Keyboard Controller steuert wie bereits erwähnt zwei Eingabegeräte. Wenn man Daten im Inputpuffer platziert interpretiert der Keyboard Controller diese als Befehle an die Tastatur und leitet sie entsprechend weiter. Wenn man aber nun Befehle an die Maus senden möchte, dann muss man dieses vorher mit dem Befehl 0xD4 signalisieren:

\<c\> VOID mouse_send_cmd(BYTE cmd) {

     kbc_send_cmd(KBC_CMD_MOUSE);
     kbc_write_inbuf(cmd);

} \</c\>

Auch wenn ein Mausbefehl noch Daten erwartet, dann muss das Senden von Daten vorher mit dem Befehl 0xD4 signalisiert werden. Im PS/2-Protokoll sind u.a. folgende Befehle definiert, die die Maus „kennt“:

| Befehl | Beschreibung |
| -------- | ----------------------------------------------------------------- |
| 0xF4 | Teile der Maus mit, dass sie Daten an die CPU senden soll |
| 0xF5 | Teile der Maus mit, dass sie keine Daten an die CPU senden soll |
| 0xF6 | Setze Mauseinstellungen auf Standarteinstellungen zurück |

Auf all diese Befehle antwortet die Maus, indem sie den Wert 0xFA (ACK – Acknowledge genannt) im Output Puffer platziert:

\<c\> BYTE mouse_read_data() {

     return kbc_read_outbuf();

} \</c\>

## Initialisierung der Maus

Folgende Funktion aktiviert die Maus so, dass sie immer einen IRQ12 auslöst, wenn der Benutzer die Maus bewegt hat:

\<c\>

1.  define ACK 0xFA

VOID mouse_install() {

     BYTE command_byte;

         //leere den Daten Puffer
     while ( inb(0x64) & 0x01)
     {
       inb(0x60);
     }

         //aktiviere die Maus beim Keyboard Controller
     kbc_send_cmd(0xA8);

         //Bit 1 im Command Byte setzen
     kbc_send_cmd(0x20);
     cb = kbc_read_outbuf();
     cb |= 0x02;
     kbc_send_cmd(0x60);
     kbc_write_inbuf(cb);

         //Standards setzen
     mouse_send_cmd(0xF6)
     if ( mouse_read_data() != ACK)
     {
       kprintf(“mouse error!”);
       return;
     }

         //das Senden von Daten aktivieren
     mous_send_cmd(0xF4);
     if ( mouse_read_data() != ACK)
     {
       kprintf(“mouse error!”);
       return;
     }
     return;

} \</c\>

## Der IRQ12

### Datenpakete

Die Maus sendet nun immer mehrere IRQ 12, wenn sie bewegt oder geklickt wurde. Im einfachsten Falle sendet sie drei IRQs, bei denen mit jedem IRQ nacheinander folgende Datenbytes im Output Puffer liegen:

<table>
<tbody><tr>
<th>Byte #</th>
<th>Bit 7</th>
<th>Bit 6</th>
<th>Bit 5</th>
<th>Bit 4</th>
<th>Bit 3</th>
<th>Bit 2</th>
<th>Bit 1</th>
<th>Bit 0
</th></tr>
<tr>
<td>1</td>
<td>Y Overflow</td>
<td>X Overflow</td>
<td>Y Sign</td>
<td>X Sign</td>
<td>Immer 1</td>
<td>Mittlerer Button gedrückt</td>
<td>Rechter Button gedrückt</td>
<td>Linker Button gedrückt
</td></tr>
<tr>
<td>2</td>
<td colspan="8">Bewegung in X Richtung
</td></tr>
<tr>
<td>3</td>
<td colspan="8">Bewegung in Y Richtung
</td></tr></tbody></table>

Beim Drücken der Maustasten sendet die Maus also drei Bytes, bei dem im ersten jeweils Bit 0, Bit 1 und Bit 2 entsprechend den Tasten gesetzt / gelöscht sind. Wenn die Maus dann zusätzlich noch bewegt wird, dann bekommen Byte 2 und Byte 3 sowie die Sign Bits im Byte 1 noch eine Bedeutung:

- Wenn die Maus horizontal nach rechts bewegt wird, dann ist das Sign Bit gelöscht, Byte 2 gibt die Weite der Bewegung an.
- Wenn die Maus horizontal nach links bewegt wird, dann ist das Sign Bit gesetzt, Byte 2 ist das Zweierkomplement der Weite der Bewegung.
- Wenn die Maus vertikal nach oben bewegt wird, dann ist das Sign Bit gelöscht, Byte 3 gibt die Weite der Bewegung an.
- Wenn die Maus horizontal nach unten bewegt wird, dann ist das Sign Bit gesetzt, Byte 3 ist das Zweierkomplement der Weite der Bewegung.

Wenn im Byte 1 das X Overflow und/oder das Y Overflow Bit gesetzt ist, dann sollte das Paket verworfen werden. Das Bit 3 in Byte 1 ist immer gesetzt. Es kann dazu genutzt werden, um sicherzustellen, dass man bei der Reihenfolge der Daten nicht durcheinander kommt.

### IRQ 12 Handler

Der Handler für den IRQ 12 wird dreimal aufgerufen, damit man alle drei Bytes der Maus hat. Im Handler muss man sich natürlich merken, bei welchem der Bytes man gerade ist. Der Handler kann also z.B. so aussehen:

\<c\> BYTE cycle=1; BYTE flags; int x_mov, y_mov;

VOID irq_12_handler() {

     DWORD val;
     switch (cycle)
     {
       case 1:
         flags = mouse_read_data();
         if (! (flags & 0x08) ) //teste, ob Bit 3 wirklich gesetzt ist
         {
           cycle = 1;       //wenn nicht, dann sind wir mit der Reihenfolge der Bytes durcheinander gekommen!
         }
         else
         {
           cycle = 2;
         }
         break;
       case 2:
         val = mouse_read_data();
         val &= (DWORD) 0xFF;       //es dürfen wirklich nur die ersten 8 Bits belegt sein!
         if (flags & 0x10)
           x_mov = (val | 0xFFFFFF00);
         else
           x_mov = val;
         cycle = 3;
         break;
       case 3:
         val = inb(0x60);
         val &= (DWORD) 0xFF;
         if (flags & 0x20)
           y_mov = - (val | 0xFFFFFF00);
         else
           y_mov = - (val);

//auf overflow testen

         if ((flags & 0x40) || (flags & 0x80))
           ;
         else
         {
           update_mouse(flags, x_mov, y_mov);   //oder was auch immer du damit machen möchtest..
         }
         cycle = 1;
         break;
     }

} \</c\>

Die Rechnerei in case 2 und case 3 dient nur dafür, das Zweierkomplement von neun Bits auf 32 zu erweitern. Diese Rechnung funktioniert (ich werde hier nicht erklären wie) aber nur wenn:

- x_mov und y_mov wirklich Integerwerte (32 Bit!) sind
- die linke obere Ecke die kleinsten Koordinaten und die untere rechte die höchsten Koordinaten hat

Vergiss nicht, das EOI Signal an den PIC zu senden!

## Weitere Maus Features

### Scrollrad und ähnliches

//TODO

### Nicht lineare Bewegung

//TODO

## Siehe auch

- [PS/2-Maus](https://github.com/lowlevel-eu/wiki/wiki/PS-2-Maus "PS/2-Maus") - Artikel mit allen Befehlen der Maus
- [Keyboard Controller](https://github.com/lowlevel-eu/wiki/wiki/Keyboard-Controller "Keyboard Controller")

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/9393/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2390/index.html)

<!-- MediaWiki page 2390; revision 9393; parent 0; 2011-01-30T18:57:41Z -->
