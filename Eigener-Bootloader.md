# Eigener Bootloader

**Hinweis:**

Dieser Artikel wird in mehreren Schritten komplett überarbeitet, da der bisherige Inhalt nur das Programmieren eines Bootsektor beinhaltet, jedoch in keinster Weise auf das Booten des eigenen OS eingeht. -- [ScollPi](https://lowlevel-eu.github.io/wiki/pages/1765/index.html "Benutzer:ScollPi") 18:16, 30. Mär. 2010 (CEST)

  
Der Weg zum eigenem Betriebssystem ist lang und steinig. Manch einer versucht als erstes einen eigenen [Bootloader](https://github.com/lowlevel-eu/wiki/wiki/Bootloader "Bootloader") inklusiv [Bootsektor](https://github.com/lowlevel-eu/wiki/wiki/Bootsektor "Bootsektor") zu entwickeln. Klar kann man sich die Arbeit auch sparen, indem man prompt zu [GRUB](https://github.com/lowlevel-eu/wiki/wiki/Grand-Unified-Bootloader "GRUB") greift. Dennoch, möchte man die Funktionsweise eines Bootloader verstehen können. Dies soll mit diesem Tutorial vermittelt werden.

Dieses Tutorial wird in erster Linie die Vorgehensweise erläutern, die bei vielen [Dateisystemen](https://github.com/lowlevel-eu/wiki/wiki/Dateisystem "Dateisystem") identisch sind. Folglich wird hier auch kein kompletter Source-Code eines Bootloader gelistet. Grundkenntnise in [Assembler](https://github.com/lowlevel-eu/wiki/wiki/Assembler "Assembler") sind für dieses Tutorial allerdings Voraussetzung, so auch der Umgang mit einem Assembler und einem [Linker](https://github.com/lowlevel-eu/wiki/wiki/Linker "Linker").

Auch in Assembler sollte man sauber programmieren und nicht scheuen, Strunkturen und Variablen statt Offset-Konstanten zu verwenden, besonders beim Boot-Parameter-Block.

  

## Allgemeines

Der [Bootprozess](https://github.com/lowlevel-eu/wiki/wiki/Bootprozess-auf-x86 "Bootprozess") wird ja bereits an anderer Stelle beschrieben, jedoch wird dort nicht näher ins Detail gegangen. Dies wird nun an dieser Stelle nun nachgeholt.

Ausgangspunkt ist, dass das [BIOS](https://github.com/lowlevel-eu/wiki/wiki/Basic-Input-Output-System "BIOS") bereits den ersten Sektor von unserem Datenträger geladen hat und nach einer Überprüfung der Signatur die Kontrolle an diesem abgibt. Man beachte, das der erste Sektor bei Festplatten für gewöhnlich der [Master Boot Record](https://github.com/lowlevel-eu/wiki/wiki/Master-Boot-Record "Master Boot Record") ist und auf dem ebenfalls eingegangen wird, bzw. die Vorgehensweise erläutert.

Die Falle in der man tappen wird, wenn man wild drauf los programmiert, dass der Binärcode des Bootsektors die 512-Byte-Grenze überschreiten wird. OK, zugegeben, bei der CD mit ihren 2048 Bytes pro Sektor und deren Dateisystem langt dieser. Auch zukünftige Festplatten mit einer physikalischen Sektorgröße von 4096 Bytes mögen dem entgegen wirken. Unser Ziel ist aber keineswegs für jedes Dateisystem einen eigenen Bootloader (ausschließlich dem Bootsektor) zu entwickeln, sondern viel mehr ein universelles Modell auf die Beine zu stellen, bei dem nur der Bootsektor individuell dem Dateisystem vorliegt und der Bootloader (Binärdatei) für alle unterstützten Dateisystemen gleich bleibt.

  

## Universelles Bootloader-Modell

Damit wir nicht im Chaos bei der Entwicklung unseres Bootloaders versinken, werden wir diesen unterteilen, nicht nur wegen der Übersicht, sondern weil es zum einen auch partitionierte Datenträger gibt und zum anderem der Bootsektor in seiner Größe begrenzt ist.

- Stage 0: Master-Boot-Recort (optional)
- Stage 1: Bootsektor
- Stage 2: Bootloader

Manch einer würde hier jetzt die Frage stellen, ob es wirklich sinnvoll ist, auch den MBR zu entwickeln. Wie schon anfangs erwähnt, wollen wir den Bootloader im Detail verstehen können, also machen wir keine halben Sachen. Dennoch, ganz so verkehrt ist die Frage allerdings nicht, denn meine Disketten haben für gewöhnlich keinen MBR.

  

**Hinweis:**

Der folgende Text enthält noch den ursprünglichen Artikel.

## Tools

Das brauchen wir um unser erstes Programm zu realisieren: Einen Editor, einen Assembler, ein paar Konsolentools und eine Testumgebung.

### Der Editor

*Hauptartikel: [Editor](https://github.com/lowlevel-eu/wiki/wiki/Editor "Editor")*

Fürs erste reicht jeder beliebige Texteditor. Unter Windows z. B. Notepad. Von Vorteil ist es, wenn der Editor Syntaxhighlighting für Assemblerdateien unterstützt wie z. B. Notepad 2, Ultraedit, Proton ... Für Linux gilt das gleiche. Hier gibt es auch jede Menge brauchbarer Editoren, die unseren Ansprüchen genügen.

### Der Assembler

Der Assembler ist das Tool, mit dem wir unseren Quelltext in eine dem PC verständliche Sprache übersetzen. Der Assemblerquelltext ist für viele Menschen zwar auch nicht gerade verständlich, der PC kann damit aber auch noch nichts anfangen. Daher übersetzt der Assembler unseren Quelltext in einen von Maschinen ausführbaren Programmcode.

Als Assembler verwenden wir den [Netwide Assembler](https://github.com/lowlevel-eu/wiki/wiki/Netwide-Assembler "Netwide Assembler") (kurz NASM). Er ist für das, was wir vorhaben, eine gute Wahl. Außerdem existiert er sowohl für Windows als auch für Linux und steht unter der LGPL. NASM ist ein Sourceforge-Projekt und kann unter <http://sourceforge.net/projects/nasm> bezogen werden.

### Die Testumgebung

Zum Testen unseres Images werden wir Bochs verwenden. Bochs ist ein PC–Emulator. Er emuliert einen vollständigen PC inklusive Prozessor, im Gegensatz zu z. B. VM-Ware oder Virtual PC. Diese Programme simulieren auch einen PC, hier wird jedoch das Programm auf dem Hostprozessor ausgeführt, um mehr Geschwindigkeit zu erzielen. Bochs hingegen hat für uns den Vorteil, dass er einen integrierten Debugger besitzt. Er wird uns noch viele nützliche Informationen über unser Programm und dessen Fehler liefern.

Auch Bochs steht unter der LGPL und ist auf Sourceforge.net unter <http://bochs.sourceforge.net> erhältlich.

  

## Hello World

Wie bereits erwähnt wird unser erstes Programm nicht viel anderes machen, als einen Text auszugeben, danach auf eine beliebige Taste zu warten, und dann das System neu zu starten.

Bevor wir anfangen, sind noch ein paar Informationen wichtig. Unser Programm wird im [Boot Record](https://github.com/lowlevel-eu/wiki/wiki/Bootsektor "Boot Record") liegen. Daher muss es im ersten Sektor einer Partition oder Diskette liegen. Weiterhin braucht unser Programm eine besondere Kennzeichnung, die Magic Number (0xAA55). Diese muss am Ende des Sektors stehen. Ein Sektor ist übrigens nur 512 Byte groß. Abzüglich der Magic Number bleiben uns noch 510 Byte für unser Programm. Das ist nicht wirklich viel und unter anderem ein Grund, wieso wir das Programm in Assembler schreiben und nicht in einer Hochsprache wie z. B. C. Der nächste wichtige Punkt ist, dass das BIOS unseren Sektor an die absolute Adresse 0x07C00 kopiert und ausführt. Je nach BIOS-Hersteller kann die Zusammensetzung der absoluten Adresse aber unterschiedlich aussehen.

### Assemblerdirektiven

Nun zu unserem Programm. Das Programm beginnt mit folgenden Zeilen.

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

Die ersten Zeilen beginnen mit einem Semikolon und sind somit Kommentarzeilen. Alles, was nach einem Semikolon steht, wird vom Assembler beim Übersetzen (Assemblieren) nicht berücksichtigt.

Die darauf folgenden beiden Zeilen enthalten Anweisungen an den Assembler selbst (Assemblerdirektiven). Die Zeile \[BITS 16\] gibt an, dass es sich bei diesem Programm um ein 16-Bit-Programm handelt. Dadurch wird die Adressierung für den Real Mode festgelegt. Die Zeile \[ORG 0x0000\] ist für die Speicherorganisation zuständig. Im Realmode lässt sich damit der Offset festlegen, ab dem die Adressierung beginnen soll, in unserem Falle 0.

### Startcode

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

Die erste Zeile enthält ein Label. Die Befehle, die nach dem Label START folgen, initialisieren den Stack, die Segmentregister und den Instruction Pointer. Wie bereits erwähnt, ist die absolute Adresse, an die unser Programm vom BIOS kopiert wird, zwar gleich, kann aber von BIOS-Hersteller zu Hersteller unterschiedlich realisiert werden. Daher bringen wir sie erst einmal in einen definierten Zustand, mit dem wir weiterarbeiten können.

Data Segment, Extra Segment, Code Segment und Stack Segment werden alle auf das gleiche Segment gelegt. Das hört sich jetzt erst einmal gefährlich an, da der Stack aber von oben nach unten wächst, und unser Programm um unteren Ende des Segments liegt ist genug Platz dazwischen.

Da Segmentregister nicht direkt mit absoluten Werten gesetzt werden können, machen wir den Umweg über AX. Mit dem ersten MOV-Befehl wird AX mit der Segmentadresse 0x07C0 initialisiert, die anschließend mit den nächsten 3 MOV-Befehlen den einzelnen Segmentregistern DS, ES und SS zugewiesen wird. Der Stackpointer wird nun mit dem letzten MOV auf den höchstmöglichen Wert gesetzt, damit dieser von oben nach unten wachsen kann. Der letzte Befehl ist ein absoluter Sprung (JMP für jump), mit dem CS und IP neu gesetzt werden. CS wird dabei auf 0x07C0 gesetzt, IP auf die Adresse die dem Label MAIN vom Assembler zugewiesen wird. Wir kennen den absoluten Wert nicht, nur den Platzhalter dafür. Aber das ist nicht schlimm, der Assembler ersetzt beim Assemblieren die Platzhalter durch die zugehörigen Adressen.

### Hauptprogramm

\<asm\>

       MAIN:
          mov     si, msgText             ; set SourceIndex to msgText
          call    DisplayMessage          ; Display the message

          mov     ah, 0x00                ; 
          int     0x16                    ; await keypress
          int     0x19                    ; reboot computer

\</asm\>

Nach dem Label MAIN folgt das Hauptprogramm. Es besteht im ganzen aus nur 5 Anweisungen. 2 MOV-Befehlen, einem CALL und 2 Interruptaufrufen. Die ersten beiden kümmern sich um die Textausgabe, die darauf folgenden beiden um das Warten auf einen Tastendruck, der letzte um den Reset. Aber erst mal der Reihe nach.

Als erstes wird dem Register SI ein Wert zugewiesen. Das geschieht mit einem MOV. Danach folgt ein CALL DisplayMessage, DisplayMessage ist eine Prozedur, die einen Text auf dem Monitor ausgibt. Die Prozedur erwartet, dass die Adresse des auszugebenden Textes durch DS:SI angegeben wird. Da DS bereits im START-Bereich gesetzt wurde, müssen wir nur noch SI entsprechend setzen. Da wir den genauen Wert nicht kennen, verwenden wir auch hier einen Platzhalter bzw. ein Label, welches weiter unten noch definiert wird.

Danach folgt ein MOV, mit dem das Register AH auf 0x00 gesetzt wird, und anschließend ein INT 0x16. Diese beiden Zeilen rufen eine Funktion auf, die uns das BIOS zur Verfügung stellt. Diese wartet auf einen Tastendruck und liest diesen aus. Die ISR für den Interrupt 0x16 wertet einige Register aus, bevor die entsprechende Funktion ausgeführt wird. Die meisten der ISR des BIOS verwenden Register zur Parameterübergabe an Software-Interrupts.

Als letztes folgt ein INT 0x19. Diese ISR startet das BIOS neu und entspricht somit einem Neustart des Rechners.

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

DisplayMessage ist eine Prozedur, die den Text, der durch DS:SI angegeben ist, auf dem Monitor ausgibt. Die Textausgabe erfolgt zeichenweise mit der Funktion 14 des BIOS-Interrupts 0x10. Wir benötigen daher eine Schleife, die die BIOS-Funktion für jedes einzelne Zeichen aufruft. Die Schleife wird verlassen, wenn das darzustellende Zeichen den Wert 0 aufweist. Wir geben mit dieser Prozedur somit einen nullterminierten String aus, so wie er z. B. in C verwendet wird.

Die Prozedur benötigt intern einige Register für Zähler und Funktionsparameter. Daher sind wir gezwungen, diese Register zu sichern, bevor wir sie verwenden. Danach müssen wir logischerweise das Gesicherte wiederherstellen. Würden wir das nicht tun, müssten wir überall dort, wo wir unsere Prozedur aufrufen, erst einmal all diejenigen Register sichern, die die Prozedur verwendet, und nach dem Aufruf wiederherstellen. Also machen wir das gleich in der Prozedur und müssen uns so beim Aufruf nicht mehr darum kümmern.

Die Sicherung der Register auf dem Stack erfolgt mit dem Befehl PUSHA. Danach wird AH auf 0x0E und BX auf 0x0007 gesetzt. AH enthält die Funktionsnummer für den BIOS-Interrupt 0x10, BX enthält Parameter für die entsprechende Funktion 14 – in diesem Fall Vorder-, Hintergrundfarbe und die Nummer des Displaypuffers.

Anschließend folgt die Schleife. Das Label .DisplayLoop kennzeichnet ihren Anfang, es wird solange angesprungen, bis der komplette Text ausgegeben wurde.

Der Befehl LODSB lädt das durch DS:SI angegebene Byte in AL und erhöht dabei gleichzeitig SI um eins. Jetzt zeigt DS:SI auf das nächste Zeichen, das ausgegeben werden soll. Mit dem nächsten beiden Befehlen wird überprüft, ob das Zeichen das Textende kennzeichnet oder nicht. Der Befehl TEST führt einen „Test“ durch, der einige Flags im Statusregister setzt (ein bitweises UND ohne das Ergebnis zu speichern, es werden nur die entsprechenden Flags gesetzt). Wurde das Zero Flag (ZF) gesetzt, sprich in AL befindet sich 0x00, dann wird mit dem Befehl JZ (Jump if Zero) die Schleife verlassen und an das Label .DONE gesprungen, wenn nicht, werden die nachfolgenden Befehle ausgeführt. Handelte es sich um ein auszugebendes Zeichen, das Zero Flag wurde also beim TEST nicht gesetzt, wird INT 0x10 aufgerufen. Dieser BIOS-Interrupt mit der vorher gesetzten Funktionsnummer in AH gibt das Zeichen auf dem Monitor aus. Das Zeichen muss sich in AL befinden, die Farbangaben in BX. Anschließend wird mit JMP wieder zum Anfang der Schleife gesprungen.

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

Nach der Prozedur folgt der Datenteil unseres Programmes. Hier befindet sich unser Text, den wir ausgeben wollen. Das Label msgText kennzeichnet die Adresse, an der sich unser Text befindet. Wir erinnern uns, im Hauptprogramm haben wir es bei der Textausgabe verwendet. Nach dem Label folgt ein DB, es kennzeichnet einen aus Bytes bestehenden Datenbereich. Anschließend folgen entweder durch Kommas getrennt die einzelnen Zeichen als Hexzahl oder in Hochkommas gesetzter ganz normaler Text. 0x0D und 0x0A sind Steuerzeichen, die dafür sorgen, dass unser Text in einer neuen Zeile ausgegeben wird.

Die darauf folgende Zeile enthält wieder eine Besonderheit von NASM: Hiermit werden so viele 0x00-Datenbytes in den Programmcode eingefügt, dass unser Programm zusammen mit der Magic Number genau 512 Byte groß ist.

Die nächste Zeile enthält diese Magic Number. Das DW kennzeichnet einen Datenbereich mit 16-Bit-Werten.

In den letzten 3 Zeilen werden die bisher 512 Byte auf Diskettenimagegröße von 1,44 MB aufgefüllt. Diese Erweiterung lässt sich über einen Parameter beim Aufruf von NASM ein- und ausschalten.

### Assemblierung und Imageerzeugung

Ich gehe davon aus, dass wir unser Programm mittlerweile in einer Datei mit dem Namen HelloWorld.asm gespeichert haben.

#### Windows

Um den Boot Record zu übersetzen genügt nun folgender Aufruf:

    F:\BootRecord>nasmw src\HelloWorld.asm -o bin\HelloWorld.bin -l bin\HelloWorld.lst

Danach sollte im Verzeichnis bin eine 512 Byte große Datei entstanden sein sowie eine HelloWorld.lst. Aus dieser Datei lassen sich Adressen und entstandener Maschinencode ablesen. Die .bin-Datei kann jetzt in den ersten Sektor jeder beliebigen Diskette kopiert werden.

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

Wir aber wollen ja zum Test ein Diskettenimage, das wir testen können. Hierzu rufen wir NASM mit der Option "-dIMAGE" auf. Mit -d wird das Define IMAGE gesetzt. Mit Hilfe dieses Defines und dem %ifdef %endif in unsere HelloWorld.asm erzeugt NASM jetzt eine 1,44 MB große Datei.

    F:\BootRecord>nasmw src\HelloWorld.asm -o img\HelloWorld.img -dIMAGE

Zur Kontrolle, ob unser Image auch erzeugt wurde:

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

Unter Linux verwenden wir anstelle von NASMW NASM.

    nasm src/HelloWorld.asm -o bin/HelloWorld.bin -l bin/HelloWorld.lst
    nasm src/HelloWorld.asm -o img/HelloWorld.img -dIMAGE

#### Der Test

Jetzt können wir das erstellte Image mit Bochs testen. Ich gehe einmal davon aus, dass ihr es schon installiert habt. Hier mal eine kleine bochsrc.txt:

    # small bochsrc.txt
    # by muuh

    ### Hier den Pfad anpassen für dein Diskimage
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

Einfach die Datei bochsrc.txt im Installationsordner von Bochs anlegen, Pfad zum erstellten Image anpassen, bochs.exe starten und im Menü die Option 6 (Simulation) wählen.

## Nachwort

Wenn alles gutgegangen ist, haben wir jetzt ein Diskettenimage mit unserem HelloWorld-Programm. Im nachfolgenden Teil 2 wollen wir diesen BootRecord so weit umbauen und erweitern, dass wir damit auch andere Programme von einem Datenträger laden und ausführen können.

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/7460/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1427/index.html)

<!-- MediaWiki page 1427; revision 7460; parent 7459; 2010-03-30T18:26:20Z -->
