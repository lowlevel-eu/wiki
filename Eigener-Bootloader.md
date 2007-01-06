# Eigener Bootloader

## Vorwort

Der weg zum eigenen Betriebsystem ist lang und steing. Viele versuchen als erstes einen eigenen [Boot Record](https://github.com/lowlevel-eu/wiki/wiki/Bootsektor "Boot Record"), auch Bootsektor genannt, zu entwickeln. Einem Programm das man in einem bestimmten Sektor einer Diskette oder Partition liegt, und vom PC direckt nach der Ausführung des BIOS geladen und ausgeführt wird.

In diesem Tutorial wollen wir so ein Programm entwickeln und testen. Dieses Programm wird nicht viel können, auser etwas Text auszugeben, auf eine Tastatureingabe zu warten und anschliessend das System neu zu starten.

Grundkenntisse in Assembler sind für dieses Tutorial von Vorteil, aber nicht zwingend notwendig.

## Tools

Was brauchen wir um unser erstes Programm zu realisieren. Einen Editor , einen Assembler ein paar Konsolentools und eine Testumgebung.

### Der Editor

Fürs erste reicht jeder beliebige Text Editor. Unter Windows z.B. Notepad. Von Vorteil ist es, wenn der Editor Syntaxhilitning für Assembler Dateien unterstützt wie z.B. Notepad 2, Ultraedit, Proton ... Für LINUX gilt das gleiche hier gibt es auch jede menge brauchbarer Editoren die unseren ansprüchen genügen.

### Der Assembler

Der Assembler ist das Tool, mit dem wir unseren Quelltext in eine dem PC verständliche Sprache übersetzen. Der Assemblerquelltext ist für viele Menschen zwar auch nicht gerade verständlich. Der PC kann damit aber auch noch nichts anfangen. Daher übersetzt der Assembler unser geschriebenes in ein Maschienen ausfürbaren Programmcode.

Als Assembler verwenden wir den Netwide Assembler kurz NASM. Er ist für das was wir vorhaben eine gute wahl. Auserdem existiert er sowol für Windows als auch für Linux und steht unter der LGPL. NASM ist ein Sorceforge1 Projekt und kann unter der untenstehenden URL bezogen werden.

<http://sourceforge.net/projects/nasm>

### Die Testumgebung

Zum Testen unseres Images werden wir Bochs verwenden. Bochs ist ein PC – Emulator. Er emuliert einen vollständigen PC inclusieve Prozessor. Nicht wie z.B. VM-Ware oder Virtau PC. Diese Programme Simmulieren auch einen PC, hier wird jedoch das Programm auf dem Host Prozessor ausgeführt, um mehr geschwindigkeit heraus zu hohlen. Bochs hingegen hat für uns den Vorteil, das er einen Integrierten Debugger besitzt. Er wird uns noch viele nützliche informationen über unser Programm und dessen Fehler liefern.

Auch Bochs unterligt der LGPL, und ist auf Sourceforge.net erhältlich. Nachstehend die URL zu dem Projekt.

<http://bochs.sourceforge.net>

## Hello World

Wie bereits erwähnt, unser ersters Programm wird nicht viel anderes machen, als einen Text auszugeben, danach auf eine beliebige Taste zu warten, um dann das System neu zu Starten.

Bevor wir anfagen sind noch ein paar Informatioen wichtig. Unser Programm wird im [Boot Record](https://github.com/lowlevel-eu/wiki/wiki/Bootsektor "Boot Record") liegen. Daher muss unser Programm im ersten Sektor einer Parition oder Disketten liegen. Weiter braucht unser Programme eine besondere Kennzeichnung, die Magicnumber (0xAA55). diese muss am Ende des Sektors stehen. Ein Sektor ist übrigens nur 512 Byte gross. Abzüglich der Magicnumber bleiben uns noch 510 Byte für unser Programm. Das ist nich wirklich viel. Und auch mit einer der Gründe wieso wir das Programm in Assembler schreiben und nicht in einer Hochsprache wie z.B. C. Der nächste wichtige Punkt ist, das das BIOS unseren Sektor an die Absolutenaddresse 0x07C00 kopiert und ausführt. Je nach BIOS-Hersteller, kann die zusammensetzung der Absolutenaddresse aber unterschiedlich aussehen.

### Assembler Direktiven

So nun zu unserem Programm. Das Programm beginnt mit folgenden Zeilen.

    ;*************************************************************************
    ; File:  HelloWorld.asm                     Version: 0.1 
    ; Autor: Michael Graf                       Date:    10.09.2006
    ; Description: 
    ;     Print the Hello World message, Wait for a key and reboot the system.
    ; History :
    ;     v0.1    2006.09.10 UTC    Inital version. Start of History
    ;*************************************************************************
    [BITS 16]                             ; 16bit realmode code
    [ORG 0x0000]                          ; start Organisation at position

Die ersten Zeilen beginnen mit einem Semikolon, und sind somit Kommentarzeilen. Alles was nach einem Semikolon steht wird vom Assembler nachher beim Übersetzen (assemblieren) nicht berücksichtigt.

Die darauffolgenden beiden Zeilen enthalten Anweisungen an den Assembler selber (Assembler Direktiven). Die Zeile \[BITS 16\] gibt an, das es sich bei diesem Programm um eine 16 Bit Programm handelt. Dadurch wird die Addressierung für den Realmode festgelegt. Die Zeile \[ORG 0x0000\] ist für die Speicherorganisation zuständig. Im Realmode lässt sich damit der Offset festlegen, ab dem die Addressierung beginnen soll. In unseremfalle 0.

### Start Code

       START:                             ; Initalize segmentregisters and
                                          ; create Stack
                                          ; 
          mov     ax, 0x07C0              ; segmentlocation 0x07C0
          mov     ds, ax                  ; set DataSegment to 0x07C0
          mov     es, ax                  ; set ExtraSegment t0 0x07C0

                                          ; create stack 
          mov     ss, ax                  ; set StackSegment to 0x07C0
          mov     sp, 0xFFFF              ; set StackPointer to 0xFFFF

          jmp     WORD 07C0h:MAIN         ; jump into main to configure 
                                          ; CodeSegment and InstructionPointer

Die Erste Zeile enthlält ein Label. Die Befehle die nach dem Label START folgen, sind für die initallisierung des Stacks, der Segmentregister und des Instruktion Pointers. Wie bereits erwähnt, ist die abbsolute Addresse an die unser Programm vom BIOS kopiert wird zwar gleich. Kann aber von BIOS Hersteller zu Hersteller unterschiedlich realisiert werden. Daher bringen wir sie erst einmal in einen definierten zustand, mit dem wir weiterarbeiten können.

Data Segment, Extra Segment Code Segment und Stack Segment werden alle auf das gleiche Segment gelegt. Hört sich jetzt erst einaml gefährlich an, Code- und Stack Segment in den gleichen Speicher zu legen. Da der Stack aber von oben nach unten wächst, und unser Programm um unteren Ende des Segements liegt ist da genug Platz dazwischen.

Da Segmentregister nicht direkt mit absoluten Werten gesetzt werden können, machen wir den Umweg über AX. Mit dem ersten Mov Befehl wird AX mit der Segmentadresse 0x07C0 Initallisiert, die anschliesend mit den nächsten 3 MOV Befehlen den einzelnen Segmentregistern DS, ES und SS zugewiesen wird. Der Stackpointer wird anschliessend mit dem letzten move auf den höchst möglichen Wert gesetzt, damit dieser von oben nach unten Wachsen kann. Der letzte Befehl ist ein Absoluter Sprung (JMP für jump), mit dem DS und IP neu gesetzt werden. DS wird dabei auf 0x07C0 gesetzt, IP auf die Addresse die dem Label Main vom Assembler zugewiesen wird. Wir kennen den absoluten Wert nicht, nur den Platzhalter dafür. Aber das ist nicht schlim, der Assembler ersetzt beim assemblieren die Platzalter durch die zugehörigen Addressen.

### Hauptprogramm

       MAIN:
          mov     si, msgText             ; set SorceIndex to msgText
          call    DisplayMessage          ; Display the message

          mov     ah, 0x00                ; 
          int     0x16                    ; await keypress
          int     0x19                    ; reboot computer

Nach dem Label MAIN folgt das Hauptprogramm. Es besteht im ganzen aus nur 5 Anweisungen. 2 mov Befehlen, einem call und 2 Interrupt Aufrufen. Die ersten beiden kümmern sich um die Textausgabe. Die Darauffolgenden beiden um das Warten auf die Tastatur. Der Letzte um den Reset. Aber erst mal der reihe nach.

Als erstes wird dem Register SI ein Wert zugewiesen. Das geschieht mit einem mov. Danach folgt ein CALL DisplayMessage. DisplayMessage ist ein Procedure, die einen Text auf dem Monitor ausgibt. Die Procedure erwartet, das die Addresse des auszugebenden Textes durch DS:SI angegeben wird. Da DS bereits im START - Bereich gesetzt wurde, müssen wir nur noch SI entsprechend setzen. Da wir den genauen Wert nicht kennen, verwenden wir auch hier einen Platzhalter bzw ein Label. Das Label wird weiter unten noch definiert.

Danach folgt ein mov, mit dem das Register AH auf 0x00 gesetzt wird. Anschliessend ein INT 0x16. Diese beiden Zeilen starten ein Funktion die uns das BIOS zur verfügung stellt. Diese Funktion wartet auf einen Tastendruck und liest diesen aus. Die ISR für den Interrupt 0x16 wertet einige Register aus, bevor die entsprechende Funktion ausgeführt wird. Die meisten der ISR des BIOS verwenden Register zur Parameterübergabe an Software Interrupte.

Als letztes folgt ein INT 0x19. Diese ISR startet das BIOS neu und generiert somit einen Neustart des Rechners.

### Procedure DisplayMessage

       ;********************************************************************
       ; PROCEDURE DisplayMessage
       ; display ASCII string at ds:si via BIOS INT 10h
       ;
       ; input ds:si   segment:offset message text
       ;
       ;********************************************************************
       DisplayMessage:
          pusha                           ; save all registers to stack       

          mov ah, 0x0E                    ; BIOS teletype                     
          mov bx, 0x0007                  ; display text at page   0x00       
                                          ; text attribute         0x07
        .DisplayLoop
          lodsb                           ; load next character               
          test al, al                     ; test for NULL character           
          jz .DONE                        ; if NULL exit printing message     
          int 0x10                        ; invoke BIOS                       
          jmp .DisplayLoop                ; restart loop                      
        .DONE:
          popa                            ; load all saved registers from stack         
          ret                             ; exit function

DisplayMessage ist eine Procedur die den Text der durch DS:SI angegeben ist auf dem Monitor ausgibt. Die Textausgabe erfolgt Zeichenweise mit der Funktion 14 des BIOS Interupts 0x10. Wir benötigen daher eine Schleife die die BIOS Funktion für jedes einzelne Zeichen aufruft. Die Schleife wird verlassen, wenn das darzustellende Zeichen den Wert 0 aufweist. Wier geben mit dieser Procedure somit einen Nullterminierten String aus, so wie er z.B. in C verwendet wird.

Die Procedure benötigt intern einige Register für Zähler und Funktionsparameter. Daher sind wir gezwungen diese Register zu sichern, bevor wir sie verwenden. Danach müssen wir logischerweise das gesicherte wieder zurücksichern. Würden wir das nicht tun, müssten wir überall dort, wo wir unsere Procedure aufrufen erst eimal all diejenigen Register sichern die die Procedure verwendet, und nach dem Aufruf rücksichern. Also machen wir das gleich in der Procedure und wir müssen uns beim Aufruf nicht mehr drum kümmern.

Die Sicherung der Register auf dem Stack erfolgt mit dem Befehl pusha. Danach wird AH auf 0x0E und BX auf 0x0007 gesetzt. AH enthält die Funktionsnummer für den BIOS Interrupt 0x10. BX enthält Parameter für die Entsprechende Funktion 14. In diesem Fall Vorder-/Hintergrundfarbe und die numer des DisplayPuffers.

Danachfolgt die Schleife. Das Label .DisplayLoop kennzeichnet den Anfang der Schleife. Es wird solange angesprungen bis der komplette Text ausgegeben wurde.

Der Befehl lodsb lädt das durch DS:SI angegebene Byte in AL und erhöt dabei gleichzeitig SI um eins. Danach zeigt DS:SI auf das nächste Zeichen, das ausgegeben werden soll. Mit dem nächsten beiden Befehlen wird überprüft, ob das Zeichen das Textende kennzeichnet oder nicht. Der Befehl test fürt einen „Test“ durch, der einige Flags im Statusreigster setzt. Wurde das Zero flag gesetzt, sprich in AL befindet sich 0x00, dann wird mit dem Befehl JZ (Jump if Zero) die Schleife verlassen und an das Label .DONE gesprungen, wenn nicht, werden die nachfolgenden befehle ausgeführt. Handelte es sich um ein druckbares Zeichen, das Zero Flag wurde somit beim test nicht gesetzt, wird int 0x10 aufgefufen. Dieser BIOS Interrupt mit den vorher gesetzten Funktionsnummer in AH gibt das Zeichen auf dem Monitor aus. Das Zeichen muss sich in AL befinden, die Farbangaben in BX. Anschliesend wird mit JMP wieder zum anfang der Schleife gesprungen.

Wird das Label .DONE angesprungen, werden mit dem Befehl POPA die Register wieder in den urspurngszustand gebracht. Danach wird mit dem Befehl RET die Procedure verlassen.

### Datenbereich

       ; Data area
       msgText  db 0x0D, 0x0A, "HELLO World!", 
                db 0x0D, 0x0A, "This is no OS. Press any key to reboot.", 
                db 0x0D, 0x0A, 0x00

                TIMES 510-($-$$) db 0x00           ; 
                dw 0xAA55                          ; Magic Number

       %ifdef IMAGE                                ;
                TIMES 1474048 DB 0x00              ; Empty Disk Image 1.44MB
       %endif                                      ;

Nach der Procedure folgt der Datenteil unseres Programmes. Hier befindet sich unser Text, den wir ausgeben wollen. Das Label msgText Kennzeichnet die Addresse, an der sich unser Text befindet. Wir erinnern uns, im Hauptprogramm haben wir es bei der Textausgabe verwendet. Nach dem Label folgt ein db, es kennzeichnet eine Datenbereich der aus Bytes besteht. Danach folgt entweder durch kommas getrennt die einzelnen Zeichen als Hexzahl, oder in Hochkommas ganz normaler Text. 0x0D, 0x0A sind Steuerzeichen, die dafür sorgen, das unser Text in einer neuen Zeile ausgegeben wird.

Die daraufvolgende Zeile enthält wieder eine besonderheit von NASM. Hiermit werden soviele 0x00 DatenBytes in den Programmcode eingefügt, das unser Programm mit der Magic Number genau 512 Byte gross ist.

Die nächste Zeille enthält die Magic Number. Das dw kenzeichnet einen Datenbreich mit 16 bit Werten.

In den letzten 3 Zeilen werden die bisher 512 Byte auf Disketten Image grösse von 1.44MB aufgefüllt. Diese Erweiterung lässt sich über ein Parameter beim aufruf von NASM ein bzw. ausschalten.

### Assemblierung und Image erzeugung

Ich gehe davon aus, das wir unser Programm mitlerweile in einer Datei mit dem Namen HelloWorld.asm gespeichert haben. Wenn nicht, unter **TODO** lässt sich der Quelltext herunterladen.

#### Windows

Um den Boot Record zu übersetzen genügt nun vollgender Aufruf.

    F:\BootRecord>nasmw src\HelloWorld.asm -o bin\HelloWorld.bin -l bin\HelloWorld.lst

Danach sollte im Verzeichnis bin eine 512 Byte grosse Datei entstanden sein. Sowie eine HelloWorld.lst. Aus dieser Datei lassen sich Addressen und enstandener Maschienencode ablesen. Die .bin Datei kann jetzt in 1.Sektor jeder beliebigen Diskette copiert werden.

    F:\BootRecord>dir bin
     Datenträger in Laufwerk F: ist 
     Volumeseriennummer: 

     Verzeichnis von F:\BootRecord\bin

    10.09.2006  18:10    <DIR>          .
    10.09.2006  18:10    <DIR>          ..
    10.09.2006  18:10             5.697 HelloWorld.lst
    10.09.2006  18:10               512 HelloWorld.bin
                   2 Datei(en)          6.209 Bytes
                   2 Verzeichnis(se),   Bytes frei

Wir aber wollen ja zum Test ein Diskettenimage, das wir Testen können. Dafür rufen wir NASM mit der Option -dIMAGE auf. Mit -d wird das Define IMAGE gesetzt. Mit hilfe dieses Defines und dem %ifdef %endif in unsere HelloWorld.asm erzugt NASM jetzt eine 1.44MB grosse Datei.

    F:\BootRecord>nasmw src\HelloWorld.asm -o img\HelloWorld.img -dIMAGE

Zur kontrolle ob unser Image auch erzeugt wurde.

    F:\BootRecord>dir img
     Datenträger in Laufwerk F: ist 
     Volumeseriennummer: 

     Verzeichnis von F:\BootRecord\bin

    10.09.2006  18:10    <DIR>          .
    10.09.2006  18:10    <DIR>          ..
    10.09.2006  18:10         1.474.560 HelloWorld.img
                   1 Datei(en)      1.474.560 Bytes
                   2 Verzeichnis(se),   Bytes frei

#### Linux

Unter Linux verwenden wir anstelle von NASMW NASM

    nasm src/HelloWorld.asm -o bin/HelloWorld.bin -l bin/HelloWorld.lst
    nasm src/HelloWorld.asm -o img/HelloWorld.img -dIMAGE

## Nachwort

Wenn alles gutgegangen ist haben wir jetzt ein Diskettenimage mit unserem HelloWorld Programm. Im nachvolgenden Teil 2 wollen wir diesen BootRecord so weit umbauen, und erweitern, das wir damit auch andere Programme von einem Datenträger laden und ausführen können.

  
Termite 18:11, 16. Sep 2006 (CEST)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/1593/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1427/index.html)

<!-- MediaWiki page 1427; revision 1593; parent 1585; 2007-01-06T16:38:37Z -->
