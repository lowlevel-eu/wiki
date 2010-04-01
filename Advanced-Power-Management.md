# Advanced Power Management

Diese Seite oder Abschnitt ist zwar komplett, es wird aber folgende Verbesserungen gewünscht:  

*Tutorial fertigschreiben*

Hilf Lowlevel, den Artikel zu verbessern.

  

## Allgemeines

Als erstes ein paar Informationen zu APM (Advanced Power Management) und diesem Tutorial.

### Vorwort

Da dies mein erstes Tutorial ist bitte ich euch bei Fehlern nachsichtig zu sein. Ich hoffe, dass ich alles gut erkläre.

### Worum geht es in diesem Artikel?

Da ich mich selbst eine Zeit lang mit APM beschäftigt habe möchte ich euch zeigen wie man mit diesem Standard umgeht.

### Was muss mein OS können, damit ich diesem Tutorial folgen kann?

Im Real-Mode: Für den Real-Mode brauchst du eigentlich nur ein lauffähiges Real-Mode-OS.

Im Protected-Mode: Für den Protected-Mode brauchst du ein OS, dass eine variable [GDT](https://github.com/lowlevel-eu/wiki/wiki/Global-Descriptor-Table "GDT") unterstützt.

### Was ist APM?

APM ist ein Standard für Power-Management, der von Intel und Microsoft entwickelt wurde.

  

## APM Einstieg

Der APM-Standard definiert 3 Schnittstellen, mit denen das Betriebssystem arbeiten kann.

Diese Schnittstellen sind:

1.  Das Real Mode Interface
2.  Das 16Bit Protected Mode Interface
3.  Das 32Bit Protected Mode Interface.

Nur eine dieser Schnittstellen kann gleichzeitig genutzt werden.  
Bevor eine dieser Schnittstellen genutzt werden kann muss das Betriebssystem kontrollieren, ob APM vorhanden ist, denn einige neue Computer unterstützen APM nicht mehr.  
Wenn APM unterstützt wird muss das Betriebssystem sich als nächstes mit einer Schnittstelle verbinden. Es ist eine gute Idee das Trennkommando zu senden bevor man sich mit einer Schnittstelle verbindet.

  

## Real-Mode

### Initialisation

#### Versions-Kontrolle

Diese Funktion kontrolliert ob APM unterstützt wird:

    <asm>mov ah,53h            ;Das APM-Komando     

mov al,00h  ;Versions-Anzeige Komando xor bx,bx  ;Geräte id (0 = APM BIOS) int 15h  ;Die BIOS-Funktion über Interrupt 15h aufrufen jc APM_error  ;Wenn das Carry-Flag gesetzt wurde gab es einen Fehler (APM_error eigenes Label)

                         ;Die Funktion war erfolgreich
                         ;AX = APM Versionsnummer
                             ;AH = Major revision number (im BCD Format)
                             ;AL = Minor revision number (auch BCD Format)
                         ;BX = ASCII Zeichen "P" (in BH) und "M" (in BL)
                         ;CX = APM Flags (Weiteres in der offiziellen Dokumentation)

\</asm\>

#### Schnittstellen

##### Verbinden

Diese Funktion verbindet sich zu einer der Schnittstellen, basierend auf der Variable *interface_number*, die folgende Werte haben kann:

    01h = Real Mode Interface
    02h = 16bit Protected Mode Interface
    03h = 32bit Protected Mode Interface

    <asm>;Verbinden zu einer APM-Schnittstelle

mov ah,53h  ;Dies ist das APM Komando mov al,\[interface_number\];Siehe oben xor bx,bx  ;Geräte id (0 = APM BIOS) int 15h  ; jc APM_error  ;Wenn das Carry-Flag gesetzt wurde gab es einen Fehler (APM_error eigenes Label)

                            ;Die Funktion war erfolgreich
                            ;Die Rückgabewerte sind unterschiedlich für jede Schnittstelle
                            ;Die Real Mode Schnittstelle gibt nichts zurück.
                            

interface_number db 01h  ;Siehe oben \</asm\>

##### Trennen

Diese Funktion trennt alle Schnittstellen, die verbunden sind.

    <asm>;Jede Schnittstelle trennen

mov ah,53h  ;dies ist das APM KOmando mov al,04h  ;Trennkomando xor bx,bx  ;Geräte id (0 = APM BIOS) int 15h  ;Die BIOS-Funktion über Interrupt 15h aufrufen jc .disconnect_error  ;Wenn das Carry-Flag gesetzt wird kontrollieren was für ein Fehler auftrat jmp .no_error

.disconnect_error:  ;Der Fehlercode ist in ah. cmp ah,03h  ;Wenn der Fehlercode nicht 03h ist gab es einen Fehler jne APM_error  ;Der Fehlercode 03h bedeutet, dass keine Schnittstelle vebunden war. (APM_error eigenes Label)

.no_error:

                            ;Die Funktion war erfolkreich
                            ;Nichts wurde zurückgegeben

\</asm\>

### Geräte kontrollieren

Nachdem das Betriebssystem sich mit einer Schnittstelle verbunden hat kann es anfangen Geräte zu kontrollieren, aber als erstes muss es das Power Management aktivieren.

#### Power Management aktivieren

Diese Funktion aktiviert das Power Management für alle Geräte. Das ist schneller als es für jedes einzeln zu aktivieren

    <asm>;Power Management für alle Geräte aktivieren

mov ah,53h  ;Dies ist das APM KOmando mov al,08h  ;Den Status von Power Managemen wechseln... mov bx,0001h  ;...bei allen Geräten zu... mov cx,0001h  ;...Power Management an. int 15h  ;Die BIOS-Funktion über Interrupt 15h aufrufen jc APM_error  ;Wenn das Carry-Flag gesetzt wurde gab es einen Fehler (APM_error eigenes Label)

                           ;Keine Rückgabe

\</asm\> Um das Power Management nur für ein bestimmtes Gerät zu aktivieren muss du die Geräte id in der Dokumentation nachschlagen und statt 0001h in bx eintragen.

#### Gerätezustand setzen

Diese Funktion setzt alle Geräte auf den Zustand auf den Wert der Variable *power_state* Korrekte Werte für *power_state* sind:

    01h = Standby
    02h = Suspend
    03h = Off
       
    20h...7Fh = OEM-defined power states

Um nur den Status eines bestimmten Gerätes zu ändern musst du die Geräte id in der Dokumentation nachschlagen und statt 0001h in bx eintragen.

    <asm>mov ah,53h              ;Dies ist das APM Komando

mov al,07h  ;Setze den Status... mov bx,0001h  ;...aller Geräte... mov cx,\[power_state\]  ;...zu Siehe oben int 15h  ;Die BIOS-Funktion über Interrupt 15h aufrufen jc APM_error  ;Wenn das Carry-Flag gesetzt wurde gab es einen Fehler (APM_error eigenes Label)

                           ;Keine Rückgabe

power_state db 03h  ;Siehe oben \</asm\>

### Alles zusammen

So zum Abschluss des Real Mode Teils noch eine Funktion zum Herrunterfahren des Computers:

    <asm>shutdown: 

pusha mov ah,53h  ;Das APM-Komando mov al,00h  ;Versions-Anzeige Komando xor bx,bx  ;Geräte id (0 = APM BIOS) int 15h  ;Die BIOS-Funktion über Interrupt 15h aufrufen jc APM_error  ;Wenn das Carry-Flag gesetzt wurde gab es einen Fehler (APM_error eigenes Label)

mov ah,53h  ;dies ist das APM KOmando mov al,04h  ;Trennkomando xor bx,bx  ;Geräte id (0 = APM BIOS) int 15h  ;Die BIOS-Funktion über Interrupt 15h aufrufen jc .disconnect_error  ;Wenn das Carry-Flag gesetzt wird kontrollieren was für ein Fehler auftrat jmp .no_error

.disconnect_error:  ;Der Fehlercode ist in ah. cmp ah,03h  ;Wenn der Fehlercode nicht 03h ist gab es einen Fehler jne APM_error  ;Der Fehlercode 03h bedeutet, dass keine Schnittstelle vebunden war. (APM_error eigenes Label)

.no_error:

Verbinden zu einer APM-Schnittstelle

mov ah,53h  ;Dies ist das APM Komando mov al,\[interface_number\];Siehe oben xor bx,bx  ;Geräte id (0 = APM BIOS) int 15h  ; jc APM_error  ;Wenn das Carry-Flag gesetzt wurde gab es einen Fehler (APM_error eigenes Label)

Power Management für alle Geräte aktivieren

mov ah,53h  ;Dies ist das APM KOmando mov al,08h  ;Den Status von Power Managemen wechseln... mov bx,0001h  ;...bei allen Geräten zu... mov cx,0001h  ;...Power Management an. int 15h  ;Die BIOS-Funktion über Interrupt 15h aufrufen jc APM_error  ;Wenn das Carry-Flag gesetzt wurde gab es einen Fehler (APM_error eigenes Label)

mov ah,53h  ;Dies ist das APM Komando mov al,07h  ;Setze den Status... mov bx,0001h  ;...aller Geräte... mov cx,\[power_state\]  ;...zu Siehe oben int 15h  ;Die BIOS-Funktion über Interrupt 15h aufrufen jc APM_error  ;Wenn das Carry-Flag gesetzt wurde gab es einen Fehler (APM_error eigenes Label)

                           ;Keine Rückgabe

APM_error: popa ret

interface_number db 01h ;Real Mode Schnittstelle power_state db 03h  ;Power off \</asm\>

## Protected Mode

TODO: ergänzen

  

## Nachwort

Ich hoffe, dass euch das Tutorial Spass gemacht hat und euch APM etwas näher gebracht hat.

## Siehe auch

- [ACPI](https://github.com/lowlevel-eu/wiki/wiki/Advanced-Configuration-and-Power-Interface "ACPI")

## Weblinks

- [Offizielle Spezifikation von Microsoft und Intel zu Version 1.2 von APM](http://www.microsoft.com/whdc/archive/amp_12.mspx)
- [APM bei OSDev.org](http://wiki.osdev.org/APM)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/7493/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2221/index.html)

<!-- MediaWiki page 2221; revision 7493; parent 7489; 2010-04-01T11:05:55Z -->
