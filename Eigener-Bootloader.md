# Eigener Bootloader

## Vorwort

Der Weg zum eigenen Betriebsystem ist lang und steinig. Viele versuchen als erstes einen eigenen [Boot Record](https://github.com/lowlevel-eu/wiki/wiki/Bootsektor "Boot Record"), auch Bootsektor genannt, zu entwickeln. Einem Programm das man in einem bestimmten Sektor einer Diskette oder Partition liegt, und vom PC direkt nach der Ausführung des BIOS geladen und ausgeführt wird.

In diesem Tutorial wollen wir so ein Programm entwickeln und testen. Dieses Programm wird nicht viel können, außer etwas Text auszugeben, auf eine Tastatureingabe zu warten und anschliessend das System neu zu starten.

Grundkenntisse in Assembler sind für dieses Tutorial von Vorteil, aber nicht zwingend notwendig.

## Tools

Was brauchen wir um unser erstes Programm zu realisieren. Einen Editor , einen Assembler ein paar Konsolentools und eine Testumgebung.

### Der Editor

Fürs erste reicht jeder beliebige Text Editor. Unter Windows z.B. Notepad. Von Vorteil ist es, wenn der Editor Syntaxhighlighting für Assembler Dateien unterstützt wie z.B. Notepad 2, Ultraedit, Proton ... Für LINUX gilt das gleiche hier gibt es auch jede menge brauchbarer Editoren die unseren Ansprüchen genügen.

### Der Assembler

Der Assembler ist das Tool, mit dem wir unseren Quelltext in eine dem PC verständliche Sprache übersetzen. Der Assemblerquelltext ist für viele Menschen zwar auch nicht gerade verständlich. Der PC kann damit aber auch noch nichts anfangen. Daher übersetzt der Assembler unser geschriebenes in einen von Maschinen ausführbaren Programmcode.

Als Assembler verwenden wir den Netwide Assembler kurz NASM. Er ist für dass was wir vorhaben eine gute Wahl. Außerdem existiert er sowohl für Windows als auch für Linux und steht unter der LGPL. NASM ist ein Sourceforge Projekt und kann unter der untenstehenden URL bezogen werden.

<http://sourceforge.net/projects/nasm>

### Die Testumgebung

Zum Testen unseres Images werden wir Bochs verwenden. Bochs ist ein PC–Emulator. Er emuliert einen vollständigen PC inklusive Prozessor. Nicht wie z.B. VM-Ware oder Virtual PC; diese Programme simulieren auch einen PC. Hier wird jedoch das Programm auf dem Hostprozessor ausgeführt, um mehr Geschwindigkeit heraus zu holen. Bochs hingegen hat für uns den Vorteil, das er einen integrierten Debugger besitzt. Er wird uns noch viele nützliche Informationen über unser Programm und dessen Fehler liefern.

Auch Bochs unterliegt der LGPL, und ist auf Sourceforge.net erhältlich. Nachstehend die URL zu dem Projekt.

<http://bochs.sourceforge.net>

## Hello World

Wie bereits erwähnt, unser ersters Programm wird nicht viel anderes machen, als einen Text auszugeben, danach auf eine beliebige Taste zu warten, um dann das System neu zu Starten.

Bevor wir anfangen sind noch ein paar Informatioen wichtig. Unser Programm wird im [Boot Record](https://github.com/lowlevel-eu/wiki/wiki/Bootsektor "Boot Record") liegen. Daher muss unser Programm im ersten Sektor einer Parition oder Diskette liegen. Weiter braucht unser Programm eine besondere Kennzeichnung, die Magicnumber (0xAA55). diese muss am Ende des Sektors stehen. Ein Sektor ist übrigens nur 512 Byte gross. Abzüglich der Magicnumber bleiben uns noch 510 Byte für unser Programm. Das ist nich wirklich viel. Und auch mit einer der Gründe wieso wir das Programm in Assembler schreiben und nicht in einer Hochsprache wie z.B. C. Der nächste wichtige Punkt ist, dass das BIOS unseren Sektor an die Absolute Addresse 0x07C00 kopiert und ausführt. Je nach BIOS-Hersteller, kann die Zusammensetzung der Absoluten Addresse aber unterschiedlich aussehen.

### Assembler Direktiven

So nun zu unserem Programm. Das Programm beginnt mit folgenden Zeilen.

\<asm\>

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

\</asm\>

Die ersten Zeilen beginnen mit einem Semikolon, und sind somit Kommentarzeilen. Alles was nach einem Semikolon steht wird vom Assembler nachher beim Übersetzen (assemblieren) nicht berücksichtigt.

Die darauffolgenden beiden Zeilen enthalten Anweisungen an den Assembler selber (Assembler Direktiven). Die Zeile \[BITS 16\] gibt an, das es sich bei diesem Programm um eine 16 Bit Programm handelt. Dadurch wird die Addressierung für den Realmode festgelegt. Die Zeile \[ORG 0x0000\] ist für die Speicherorganisation zuständig. Im Realmode lässt sich damit der Offset festlegen, ab dem die Addressierung beginnen soll. In unseremfalle 0.

### Start Code

\<asm\>

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

\</asm\>

Die Erste Zeile enthlält ein Label. Die Befehle die nach dem Label START folgen, sind für die Initialisierung des Stacks, der Segmentregister und des Instruktion Pointers. Wie bereits erwähnt, ist die absolute Addresse an die unser Programm vom BIOS kopiert wird zwar gleich, kann aber von BIOS Hersteller zu Hersteller unterschiedlich realisiert werden. Daher bringen wir sie erst einmal in einen definierten Zustand, mit dem wir weiterarbeiten können.

Data Segment, Extra Segment Code Segment und Stack Segment werden alle auf das gleiche Segment gelegt. Hört sich jetzt erst einmal gefährlich an, Code- und Stack Segment in den gleichen Speicher zu legen. Da der Stack aber von oben nach unten wächst, und unser Programm um unteren Ende des Segements liegt ist da genug Platz dazwischen.

Da Segmentregister nicht direkt mit absoluten Werten gesetzt werden können, machen wir den Umweg über AX. Mit dem ersten MOV Befehl wird AX mit der Segmentadresse 0x07C0 Initallisiert, die anschliessend mit den nächsten 3 MOV Befehlen den einzelnen Segmentregistern DS, ES und SS zugewiesen wird. Der Stackpointer wird anschliessend mit dem letzten MOV auf den höchst möglichen Wert gesetzt, damit dieser von oben nach unten wachsen kann. Der letzte Befehl ist ein Absoluter Sprung (JMP für jump), mit dem DS und IP neu gesetzt werden. DS wird dabei auf 0x07C0 gesetzt, IP auf die Addresse die dem Label Main vom Assembler zugewiesen wird. Wir kennen den absoluten Wert nicht, nur den Platzhalter dafür. Aber das ist nicht schlimm, der Assembler ersetzt beim assemblieren die Platzhalter durch die zugehörigen Addressen.

### Hauptprogramm

\<asm\>

       MAIN:
          mov     si, msgText             ; set SourceIndex to msgText
          call    DisplayMessage          ; Display the message

          mov     ah, 0x00                ; 
          int     0x16                    ; await keypress
          int     0x19                    ; reboot computer

\</asm\>

Nach dem Label MAIN folgt das Hauptprogramm. Es besteht im ganzen aus nur 5 Anweisungen. 2 mov Befehlen, einem call und 2 Interrupt Aufrufen. Die ersten beiden kümmern sich um die Textausgabe. Die Darauffolgenden beiden um das Warten auf die Tastatur. Der Letzte um den Reset. Aber erst mal der Reihe nach.

Als erstes wird dem Register SI ein Wert zugewiesen. Das geschieht mit einem mov. Danach folgt ein CALL DisplayMessage. DisplayMessage ist eine Prozedur, die einen Text auf dem Monitor ausgibt. Die Prozedur erwartet, das die Addresse des auszugebenden Textes durch DS:SI angegeben wird. Da DS bereits im START - Bereich gesetzt wurde, müssen wir nur noch SI entsprechend setzen. Da wir den genauen Wert nicht kennen, verwenden wir auch hier einen Platzhalter bzw ein Label. Das Label wird weiter unten noch definiert.

Danach folgt ein mov, mit dem das Register AH auf 0x00 gesetzt wird. Anschliessend ein INT 0x16. Diese beiden Zeilen starten ein Funktion die uns das BIOS zur Verfügung stellt. Diese Funktion wartet auf einen Tastendruck und liest diesen aus. Die ISR für den Interrupt 0x16 wertet einige Register aus, bevor die entsprechende Funktion ausgeführt wird. Die meisten der ISR des BIOS verwenden Register zur Parameterübergabe an Software Interrupts.

Als letztes folgt ein INT 0x19. Diese ISR startet das BIOS neu und generiert somit einen Neustart des Rechners.

### Procedure DisplayMessage

\<asm\>

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

\</asm\>

DisplayMessage ist eine Prozedur die den Text der durch DS:SI angegeben ist auf dem Monitor ausgibt. Die Textausgabe erfolgt Zeichenweise mit der Funktion 14 des BIOS Interupts 0x10. Wir benötigen daher eine Schleife die die BIOS Funktion für jedes einzelne Zeichen aufruft. Die Schleife wird verlassen, wenn das darzustellende Zeichen den Wert 0 aufweist. Wir geben mit dieser Prozedur somit einen Nullterminierten String aus, so wie er z.B. in C verwendet wird.

Die Prozedur benötigt intern einige Register für Zähler und Funktionsparameter. Daher sind wir gezwungen diese Register zu sichern, bevor wir sie verwenden. Danach müssen wir logischerweise das Gesicherte wieder zurücksichern. Würden wir das nicht tun, müssten wir überall dort, wo wir unsere Prozedur aufrufen erst eimal all diejenigen Register sichern die die Prozedur verwendet, und nach dem Aufruf rücksichern. Also machen wir das gleich in der Prozedur und wir müssen uns beim Aufruf nicht mehr drum kümmern.

Die Sicherung der Register auf dem Stack erfolgt mit dem Befehl pusha. Danach wird AH auf 0x0E und BX auf 0x0007 gesetzt. AH enthält die Funktionsnummer für den BIOS Interrupt 0x10. BX enthält Parameter für die Entsprechende Funktion 14. In diesem Fall Vorder-/Hintergrundfarbe und die Nummer des DisplayPuffers.

Danachfolgt die Schleife. Das Label .DisplayLoop kennzeichnet den Anfang der Schleife. Es wird solange angesprungen bis der komplette Text ausgegeben wurde.

Der Befehl lodsb lädt das durch DS:SI angegebene Byte in AL und erhöht dabei gleichzeitig SI um eins. Danach zeigt DS:SI auf das nächste Zeichen, das ausgegeben werden soll. Mit dem nächsten beiden Befehlen wird überprüft, ob das Zeichen das Textende kennzeichnet oder nicht. Der Befehl test führt einen „Test“ durch, der einige Flags im Statusreigster setzt. Wurde das Zero flag (ZF) gesetzt, sprich in AL befindet sich 0x00, dann wird mit dem Befehl JZ (Jump if Zero) die Schleife verlassen und an das Label .DONE gesprungen, wenn nicht, werden die nachfolgenden Befehle ausgeführt. Handelte es sich um ein druckbares Zeichen, das Zero Flag wurde somit beim test nicht gesetzt, wird int 0x10 aufgerufen. Dieser BIOS Interrupt mit den vorher gesetzten Funktionsnummer in AH gibt das Zeichen auf dem Monitor aus. Das Zeichen muss sich in AL befinden, die Farbangaben in BX. Anschliessend wird mit JMP wieder zum Anfang der Schleife gesprungen.

Wird das Label .DONE angesprungen, werden mit dem Befehl POPA die Register wieder in den Ursprungszustand gebracht. Danach wird mit dem Befehl RET die Prozedur verlassen.

### Datenbereich

\<asm\>

       ; Data area
       msgText  db 0x0D, 0x0A, "HELLO World!", 
                db 0x0D, 0x0A, "This is no OS. Press any key to reboot.", 
                db 0x0D, 0x0A, 0x00

                TIMES 510-($-$$) db 0x00           ; 
                dw 0xAA55                          ; Magic Number

       %ifdef IMAGE                                ;
                TIMES 1474048 DB 0x00              ; Empty Disk Image 1.44MB
       %endif                                      ;

\</asm\>

Nach der Prozedur folgt der Datenteil unseres Programmes. Hier befindet sich unser Text, den wir ausgeben wollen. Das Label msgText Kennzeichnet die Addresse, an der sich unser Text befindet. Wir erinnern uns, im Hauptprogramm haben wir es bei der Textausgabe verwendet. Nach dem Label folgt ein db, es kennzeichnet eine Datenbereich der aus Bytes besteht. Danach folgt entweder durch Kommas getrennt die einzelnen Zeichen als Hexzahl, oder in Hochkommas ganz normaler Text. 0x0D, 0x0A sind Steuerzeichen, die dafür sorgen, das unser Text in einer neuen Zeile ausgegeben wird.

Die darauffolgende Zeile enthält wieder eine Besonderheit von NASM. Hiermit werden soviele 0x00 DatenBytes in den Programmcode eingefügt, das unser Programm mit der Magic Number genau 512 Byte gross ist.

Die nächste Zeille enthält die Magic Number. Das dw kenzeichnet einen Datenbereich mit 16 Bit Werten.

In den letzten 3 Zeilen werden die bisher 512 Byte auf Disketten Image Größe von 1.44 MB aufgefüllt. Diese Erweiterung lässt sich über ein Parameter beim Aufruf von NASM ein bzw. ausschalten.

### Assemblierung und Image Erzeugung

Ich gehe davon aus, das wir unser Programm mittlerweile in einer Datei mit dem Namen HelloWorld.asm gespeichert haben. Wenn nicht, unter **TODO** lässt sich der Quelltext herunterladen.

#### Windows

Um den Boot Record zu übersetzen genügt nun folgender Aufruf:

    F:\BootRecord>nasmw src\HelloWorld.asm -o bin\HelloWorld.bin -l bin\HelloWorld.lst

Danach sollte im Verzeichnis bin eine 512 Byte grosse Datei entstanden sein sowie eine HelloWorld.lst. Aus dieser Datei lassen sich Addressen und enstandener Maschinencode ablesen. Die .bin Datei kann jetzt in den ersten Sektor jeder beliebigen Diskette kopiert werden.

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

Wir aber wollen ja zum Test ein Diskettenimage, das wir Testen können. Dafür rufen wir NASM mit der Option "-dIMAGE" auf. Mit -d wird das Define IMAGE gesetzt. Mit hilfe dieses Defines und dem %ifdef %endif in unsere HelloWorld.asm erzeugt NASM jetzt eine 1.44 MB grosse Datei.

    F:\BootRecord>nasmw src\HelloWorld.asm -o img\HelloWorld.img -dIMAGE

Zur Kontrolle ob unser Image auch erzeugt wurde:

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

#### Der Test

Jetzt können wir das erstellte Image mit Bochs testen. Ich gehe einmal davon aus dass ihr es schon installiert habt. Hier mal eine kleine bochsrc.txt:

    # small bochsrc.txt
    # by muuh

    ### Hier den Pfad anpassen für dein disk-image
    floppya: 1_44=C:\NASM\HelloWorld.img, status=inserted
    ####
    romimage: file=$BXSHARE/BIOS-bochs-latest, address=0xf0000
    cpu: count=1, ips=10000000, reset_on_triple_fault=1
    megs: 32
    vgaromimage: file=$BXSHARE/VGABIOS-lgpl-latest
    vga: extension=vbe
    boot: floppy
    floppy_bootsig_check: disabled=0
    log: bochsout.txt
    panic: action=ask
    error: action=report
    info: action=report
    debug: action=ignore
    debugger_log: -
    parport1: enabled=1, file="parport.out"
    vga_update_interval: 300000
    keyboard_serial_delay: 250
    keyboard_paste_delay: 100000
    private_colormap: enabled=0
    keyboard_mapping: enabled=0, map=
    i440fxsupport: enabled=1

Einfach die Datei bochsrc.txt im Installationsordner von Bochs anlegen, Pfad zum erstellten Image anpassen, bochs.exe starten und in dem Menü die Option 6 (Simulation) wählen.

## Nachwort

Wenn alles gutgegangen ist haben wir jetzt ein Diskettenimage mit unserem HelloWorld Programm. Im nachfolgenden Teil 2 wollen wir diesen BootRecord so weit umbauen, und erweitern, dass wir damit auch andere Programme von einem Datenträger laden und ausführen können.

  
Termite 18:11, 16. Sep 2006 (CEST)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/2931/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1427/index.html)

<!-- MediaWiki page 1427; revision 2931; parent 2696; 2008-05-08T11:55:13Z -->
