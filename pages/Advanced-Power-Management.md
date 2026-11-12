# Advanced Power Management

Diese Seite oder Abschnitt ist zwar komplett, es wird aber folgende Verbesserungen gewünscht:  

*Tutorial fertigschreiben*

Hilf Lowlevel, den Artikel zu verbessern.

  
**Advanced Power Management** (**APM**) ist ein Standard für Power-Management, der von Intel und Microsoft entwickelt wurde. Um die [Real-Mode Schnittstelle](Advanced-Power-Management.md "Advanced Power Management") zu nutzen, sollte bereits ein [Real Mode](Real-Mode.md "Real Mode")-Betriebssystem oder ein Betriebssystem, das den [Virtual 8086 Mode](Virtual-8086-Mode.md "Virtual 8086 Mode") unterstützt, vorhanden sein. Für die [Protected-Mode Schnittstelle](Advanced-Power-Management.md#protected-mode-schnittstelle "Advanced Power Management") sollte ein lauffähiges [Protected Mode](Protected-Mode.md "Protected Mode")-Betriebssystem, das zumindest Funktionen zum Verändern der [GDT](Global-Descriptor-Table.md "GDT") bereitstellt, vorhanden sein.

  

## Allgemeines

Der APM-Standard definiert drei Schnittstellen, mit denen das Betriebssystem arbeiten kann.

Diese Schnittstellen sind:

1.  Das Real-Mode-Interface
2.  Das 16-Bit-Protected-Mode-Interface
3.  Das 32-Bit-Protected-Mode-Interface.

Nur eine dieser Schnittstellen kann gleichzeitig genutzt werden.  
Bevor eine dieser Schnittstellen genutzt werden kann, muss das Betriebssystem kontrollieren, ob APM vorhanden ist, denn einige neue Computer unterstützen APM nicht mehr.  
Wenn APM unterstützt wird, muss das Betriebssystem sich als nächstes mit einer Schnittstelle verbinden. Es ist eine gute Idee das Trennkommando zu senden, bevor man sich mit einer Schnittstelle verbindet.

  

## Real-Mode-Schnittstelle

### Initialisierung

#### Versionskontrolle

Diese Funktion kontrolliert, ob APM unterstützt wird:

    <asm>mov ah,53h            ;Das APM-Kommando     

mov al,00h  ;Versionsanzeigebefehl xor bx,bx  ;Geräte-ID (0 = APM BIOS) int 15h  ;Die BIOS-Funktion über Interrupt 15h aufrufen jc APM_error  ;Wenn das Carry-Flag gesetzt wurde, gab es einen Fehler (APM_error ist eigenes Label)

                         ;Die Funktion war erfolgreich
                         ;AX = APM-Versionsnummer
                             ;AH = Major revision number (im BCD-Format)
                             ;AL = Minor revision number (auch BCD-Format)
                         ;BX = ASCII-Zeichen „P“ (in BH) und „M“ (in BL)
                         ;CX = APM-Flags (Weiteres in der offiziellen Dokumentation)

\</asm\>

#### Schnittstellen

##### Verbinden

Diese Funktion verbindet sich zu einer der Schnittstellen, basierend auf der Variable *interface_number*, die folgende Werte haben kann:

    01h = Real-Mode-Interface
    02h = 16-Bit-Protected-Mode-Interface
    03h = 32-Bit-Protected-Mode-Interface

    <asm>;Verbinden zu einer APM-Schnittstelle

mov ah,53h  ;Dies ist das APM-Kommando mov al,\[interface_number\];Siehe oben xor bx,bx  ;Geräte-ID (0 = APM BIOS) int 15h  ; jc APM_error  ;Wenn das Carry-Flag gesetzt wurde, gab es einen Fehler (APM_error ist eigenes Label)

                            ;Die Funktion war erfolgreich
                            ;Die Rückgabewerte sind unterschiedlich für jede Schnittstelle
                            ;Die Real-Mode-Schnittstelle gibt nichts zurück.
                            

interface_number db 01h  ;Siehe oben \</asm\>

##### Trennen

Diese Funktion trennt alle Schnittstellen, die verbunden sind.

    <asm>;Jede Schnittstelle trennen

mov ah,53h  ;dies ist das APM-Kommando mov al,04h  ;Trennbefehl xor bx,bx  ;Geräte-ID (0 = APM BIOS) int 15h  ;Die BIOS-Funktion über Interrupt 15h aufrufen jc .disconnect_error  ;Wenn das Carry-Flag gesetzt wird, kontrollieren, was für ein Fehler auftrat jmp .no_error

.disconnect_error:  ;Der Fehlercode ist in AH. cmp ah,03h  ;Wenn der Fehlercode nicht 03h ist, gab es einen Fehler jne APM_error  ;Der Fehlercode 03h bedeutet, dass keine Schnittstelle vebunden war. (APM_error ist eigenes Label)

.no_error:

                            ;Die Funktion war erfolgreich
                            ;Nichts wurde zurückgegeben

\</asm\>

### Geräte kontrollieren

Nachdem das Betriebssystem sich mit einer Schnittstelle verbunden hat, kann es anfangen Geräte zu kontrollieren, aber als erstes muss es das Power Management aktivieren.

#### Power Management aktivieren

Diese Funktion aktiviert das Power Management für alle Geräte. Das ist schneller, als es für jedes einzeln zu aktivieren.

    <asm>;Power Management für alle Geräte aktivieren

mov ah,53h  ;Dies ist das APM-Kommando mov al,08h  ;Den Status des Power Managements wechseln... mov bx,0001h  ;...bei allen Geräten zu... mov cx,0001h  ;...Power Management an. int 15h  ;Die BIOS-Funktion über Interrupt 15h aufrufen jc APM_error  ;Wenn das Carry-Flag gesetzt wurde, gab es einen Fehler (APM_error ist eigenes Label)

                           ;Keine Rückgabe

\</asm\> Um das Power Management nur für ein bestimmtes Gerät zu aktivieren, muss die Geräte-ID in der Dokumentation nachgeschlagen und statt 0001h in BX eingetragen werden.

#### Gerätezustand setzen

Diese Funktion setzt alle Geräte auf den Zustand, den die Variable *power_state* angibt. Gültige Werte für *power_state* sind:

    01h = Standby
    02h = Suspend
    03h = Off
       
    20h...7Fh = OEM-defined power states

Um nur den Status eines bestimmten Gerätes zu ändern, muss die Geräte-ID in der Dokumentation nachgeschlagen und statt 0001h in BX eingetragen werden.

    <asm>mov ah,53h              ;Dies ist das APM-Kommando

mov al,07h  ;Setze den Status... mov bx,0001h  ;...aller Geräte... mov cx,\[power_state\]  ;...zu (siehe oben) int 15h  ;Die BIOS-Funktion über Interrupt 15h aufrufen jc APM_error  ;Wenn das Carry-Flag gesetzt wurde, gab es einen Fehler (APM_error ist eigenes Label)

                           ;Keine Rückgabe

power_state db 03h  ;Siehe oben \</asm\>

### Alles zusammen

Zum Abschluss des Real-Mode-Teils noch eine Funktion zum Herunterfahren des Computers:

    <asm>shutdown: 

pusha mov ah,53h  ;Das APM-Komando mov al,00h  ;Versionsanzeigebefehl xor bx,bx  ;Geräte-ID (0 = APM BIOS) int 15h  ;Die BIOS-Funktion über Interrupt 15h aufrufen jc APM_error  ;Wenn das Carry-Flag gesetzt wurde, gab es einen Fehler (APM_error ist eigenes Label)

mov ah,53h  ;dies ist das APM-Kommando mov al,04h  ;Trennbefehl xor bx,bx  ;Geräte-ID (0 = APM BIOS) int 15h  ;Die BIOS-Funktion über Interrupt 15h aufrufen jc .disconnect_error  ;Wenn das Carry-Flag gesetzt wird, kontrollieren, was für ein Fehler auftrat jmp .no_error

.disconnect_error:  ;Der Fehlercode ist in AH. cmp ah,03h  ;Wenn der Fehlercode nicht 03h ist, gab es einen Fehler jne APM_error  ;Der Fehlercode 03h bedeutet, dass keine Schnittstelle vebunden war. (APM_error ist eigenes Label)

.no_error:

Verbinden zu einer APM-Schnittstelle

mov ah,53h  ;Dies ist das APM-Kommando mov al,\[interface_number\];Siehe oben xor bx,bx  ;Geräte-ID (0 = APM BIOS) int 15h  ; jc APM_error  ;Wenn das Carry-Flag gesetzt wurde, gab es einen Fehler

Power Management für alle Geräte aktivieren

mov ah,53h  ;Dies ist das APM-Kommando mov al,08h  ;Den Status des Power Managements wechseln... mov bx,0001h  ;...bei allen Geräten zu... mov cx,0001h  ;...Power Management an. int 15h  ;Die BIOS-Funktion über Interrupt 15h aufrufen jc APM_error  ;Wenn das Carry-Flag gesetzt wurde, gab es einen Fehler

mov ah,53h  ;Dies ist das APM-Kommando mov al,07h  ;Setze den Status... mov bx,0001h  ;...aller Geräte... mov cx,\[power_state\]  ;...zu (siehe oben) int 15h  ;Die BIOS-Funktion über Interrupt 15h aufrufen jc APM_error  ;Wenn das Carry-Flag gesetzt wurde gab es einen Fehler

                           ;Keine Rückgabe

APM_error: popa ret

interface_number db 01h ;Real-Mode-Schnittstelle power_state db 03h  ;Power off \</asm\>

## Protected-Mode Schnittstelle

TODO: ergänzen

## Siehe auch

- [ACPI](Advanced-Configuration-and-Power-Interface.md "ACPI"): Ein neuerer Standard für Power Management (unter anderem)

## Weblinks

- [Offizielle Spezifikation von Microsoft und Intel zu Version 1.2 von APM](http://www.microsoft.com/whdc/archive/amp_12.mspx)
- [APM bei OSDev.org](http://wiki.osdev.org/APM)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/9451/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2221/index.html)

<!-- MediaWiki page 2221; revision 9451; parent 7639; 2011-02-05T14:16:29Z -->
