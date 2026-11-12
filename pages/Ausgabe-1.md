# Ausgabe 1

|  |  |
| ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| © | Dieser Artikel ist urheberrechtlich geschützt.<br>Bitte beachte, dass die üblichen [Lizenzbestimmungen](https://lowlevel-eu.github.io/wiki/pages/1637/index.html "Lowlevel:Urheberrecht") des Wikis für diesen Artikel nicht gelten. |

  

|  |  |  |
| ----- | ---------------- | ------------------------------------------------------------------------------- |
|  | **Navigation** | [Ausgabe 2](Ausgabe-2.md "Ausgabe 2") » |

## Vorwort

Das ist sie, die erste Ausgabe von Lowlevel, dem ersten deutschen Magazin für Betriebssystem-Entwicklung – oder auf Englisch: Operating System Development (OS Dev). Ich bin Mastermesh, der Redakteur dieser Ausgabe und ich würde gerne etwas über mich selbst erzählen.

Ich war schon immer von Computern fasziniert. Schon mit fünf Jahren saß ich gespannt vor dem Monitor und habe zugeschaut, wie mein Bruder auf einem 386er mit Turbo Pascal programmiert hat. Mit etwa 9 Jahren habe ich BASIC gelernt, mit 12 Visual Basic, mit 14 C und mit 15 Assembler - was ich mich aber immer gefragt habe, war: wie schreibt man ein Betriebssystem?

Nach langer Suche im Internet habe ich tatsächlich einige Dokumente gefunden und habe begonnen, YaOS, mein eigenes Betriebssystem zu schreiben. YaOS wurde nie ein großes Projekt, doch es half mir, meinen PC etwas besser kennen zu lernen, und Lowlevel-Grundlagen zu begreifen. Dann beschloss ich, ein Online-Magazin heraus zu geben, ein Magazin über die Entwicklung eines Betriebssystems...

Dies ist die allererste Ausgabe von Lowlevel, ihr könnt euch gar nicht denken, wie ich aufgeregt bin... auf jeden Fall bin ich stolz auf diese Ausgabe und wünsche dem Leser viel Vergnügen!

## News

- Gareth Owen hat die Arbeit an seinem GazOS aufgegeben. Das Projekt wird nun von Kurt Maxwell Weber weitergeführt. Übrigens ist die Gaztek-Seite nur noch über <http://gaztek.sourceforge.net> erreichbar.

<!-- -->

- Das LittleOS-Projekt wurde, aus welchen Gründen auch immer, gestoppt.

<!-- -->

- Version 2.02 des beliebten Emulators bochs ist herausgekommen. [\[1\]](http://bochs.sourceforge.net)

<!-- -->

- Das V2_OS-Projekt scheint tot zu sein – hat jemand Infos weitere Infos darüber?

## Leserbriefe

Dies ist die erste Ausgabe von Lowlevel, dementsprechend gibt es auch keine Leserbriefe.

Lob? Kritik? Anregungen? Fehler im Code? Beiträge? Egal was – Mailt mir! Je mehr Mails ich kriege, desto mehr sehe ich, dass mein Magazin gelesen wird, und umso mehr kann ich auch schreiben... bitte, es ist wichtig, dass ich Feedback kriege, ansonsten weiß ich ja gar nicht, für wen ich das ganze hier eigentlich schreibe!

## OS Dev-Tutorial, Teil 1

### Was man zur Betriebssystementwicklung braucht...

Als ich beschloss, etwas über Betriebssysteme zu lernen, um vielleicht eines Tages eins zu programmieren, fragte ich mich als erstes:

Wie und mit welchen Tools kompiliere ich meinen Kernel?

Am besten hat es in diesem Fall der Linux-Anwender: Im Internet gibt es die besten Compiler für Linux kostenlos - wenn sie nicht sowieso im System enthalten sind... da wäre der GNU Compiler gcc für die C und C++ Teile eures Systems, NASM, der Netwide Assembler oder ld, der GNU Linker. Da jedoch die Mehrheit der Leute, die dieses Magazin lesen, Windows benutzt, werde ich mich auf die Entwicklung unter Windows konzentrieren.

Wir werden unseren Kernel (und unseren Bootsektor) in Assembler schreiben. Ganz einfach aus dem Grund, dass man mit Assembler die größte Kontrolle über den PC hat und weil man damit viel über den Aufbau eines PCs lernt.

Also. Wir brauchen:

- NASM [\[2\]](http://nasm.sourceforge.net)
- Rawwrite [\[3\]](http://www.chrysocome.net/rawwrite) oder ein anderes Diskettenimageschreibeprogramm.
- Grundkenntnisse in Assembler
- 1 Diskette

### Etwas Systemtheorie

Wenn wir unseren PC einschalten, sind alle Register des Prozessors leer. Der Wert 0xFFFF wird in CS (Codesegment) geladen, das bedeutet, die Anweisungen an dieser Adresse werden ausgeführt.

Nun stellt sich die Frage: was befindet sich in 0xFFFF? Ganz einfach. Dort ist das BIOS (Basic Input Output System). Das BIOS wird einige System-Checks durchführen und anschließend nach einem Betriebssystem suchen. Wir können einstellen, wo das BIOS schauen soll: auf der Festplatte, auf einer Floppy-Disk etc.

Wenn das BIOS also etwas gefunden hat, lädt es den Bootsektor vom Anfang einer Diskette oder Festplatte in den Arbeitsspeicher (Adresse: 0x07C00). Ein Bootsektor muss in Assembler geschrieben sein und zu einer rohen Binärdatei kompiliert werden.

Der Bootsektor hat nun die Aufgabe, den Kernel aufzurufen. Der Kernel ist der Hauptteil des Betriebssystems. Er führt die Interrupts aus, die Hardware und Software an ihn schicken, koordiniert den Zugriff auf die Hardware und teilt (bei Multitasking-Systemen) den einzelnen Programmen die Rechenzeit zu, die sie benötigen. Außerdem führt er die Befehle aus, die Shell oder GUI an ihn senden. Heutzutage sind die meisten Kernels in C/C++ geschrieben. Früher war Assembler die typische Sprache für das Betriebssystem.

Um all seine Aufgaben erfüllen zu können, benutzt der Kernel BIOS, Gerätetreiber und Hardware. Damit der Benutzer mit dem System kommunizieren kann, hat jedes Betriebssystem eine Shell (Befehlszeilenverarbeitung wie DOS) oder eine GUI (Grafische Oberfläche wie Windows). Beide Programme haben die Aufgabe, Anwendungen zu starten, Fehler auszugeben und Befehle auszuführen. Dazu bedienen sie sich des Kernels, des BIOS, Gerätetreibern, Systemsoftware oder direkt der Hardware.

Gerätetreiber unterstützen all das, indem sie den anderen Programmen den Zugriff auf speziellere Hardware erleichtern. Bei manchen Systemen sind die Treiber direkt in den Kernel integriert.

Wenn all dies so funktioniert, wie es sollte, dann kann die Anwendungssoftware ganz bequem mit fertig kompilierten Bibliotheken arbeiten. Der Entwickler braucht sich nicht mehr zu sorgen, wie all das funktioniert.

### Unser Bootloader

**Warnung**

Die meisten aktiven Forenmitglieder raten davon ab einen eigenen Bootloader zu schreiben, da es relativ sinnlos und extrem fehleranfällig ist. Vor allem Neulinge sollten stattdessen lieber zu [GRUB](Grand-Unified-Bootloader.md "GRUB") (relevante Artikel: [C-Kernel mit GRUB](C-Kernel-mit-GRUB.md "C-Kernel mit GRUB"), [GRUB-Image erstellen](GRUB-Image-erstellen.md "GRUB-Image erstellen"), [Ausgabe 5](Ausgabe-5.md#programmierung-eines-grub-kompatiblen-kernels "Ausgabe 5"), [Multiboot](Multiboot.md "Multiboot")) greifen.

  

**Warnung**

Teilweise scheint der Reset des Diskettenlaufwerks nicht zu funktionieren, siehe auch die [Diskussionsseite](https://lowlevel-eu.github.io/wiki/pages/1840/index.html "Diskussion:Ausgabe 1")

Zuerst einmal sucht das BIOS auf dem ersten Sektor von Diskette und Festplatte nach einer Binärdatei, die genau 512 Bytes (1 Sektor) lang ist und am Ende das Wort 0x0AA55 enthält. Jetzt lädt das BIOS unseren Bootloader, wenn es ihn denn gefunden hat, an die Adresse 0x7C00. Damit alles so läuft, wie wir es uns gedacht haben, enthält die erste Zeile unseres Assemblercodes also den Code:

\<asm\>

       ORG 0x7C00

\</asm\>

Diese Zeile regelt, dass all unsere Adressierungen richtig sind usw. Jetzt basteln wir einen Stack. Er sitzt im Segment 0x9000. Den Stackpointer setzen wir auf null. Während wir das alles tun, sind übrigens keine Interrupts zugelassen. Nun schreiben wir die Information über das Bootlaufwerk aus DL in eine Variable, rufen die Funktion "load" auf und springen zum geladenen Programm, unserem Kernel rüber (das seht ihr im vollständigen Code weiter unten).

Zum Schluss des Codes seht ihr noch folgende Zeilen:

\<asm\>

       times 512-($-$$)-2 db 0
       dw 0x0AA55

\</asm\>

Sie sind für die Länge von 512 Bytes und das Wort 0x0AA55 am Ende zuständig.

Hmmm... Das war jetzt noch nicht schwer - aber damit es funktioniert, brauchen wir noch diese Ladefunktion. Sie benutzt den BIOS-Interrupt 0x13, um auf das Laufwerk zuzugreifen und wenn das gelang, unser Binary vom 2. Sektor zu lesen. Dann gibt sie noch eine Meldung aus, damit wir im Fall eines Fehlers (bei einem späteren Kernel) wissen, ob das Laden wenigstens geklappt hat.

Der Code am Stück

\<asm\>

       org 0x7C00 ; Unsere Startadresse
       
       ; -----------------------------------------
       ; Unser Bootloader
       ; -----------------------------------------
       
       jmp 0x0000:start
       start:
                       ; Erst brauchen wir einen Stack.
       cli             ; Keine Interrupts!
       mov ax, 0x9000  ; Stackadresse
       mov ss, ax      ; SS = 0x9000 (unser Stack)
       mov sp, 0       ; SP = 0x0000  (der Stackpointer)
       sti             ; Interrupts zulassen
       
       ; Segmentregister initialisieren (für Zugriff auf bootdrv notwendig)
       mov ax, 0x0000
       mov es, ax
       mov ds, ax
       
       ; Bootlaufwerk aus DL speichern
       mov [bootdrv], dl
       
       ;Lade unseren Kernel
       call load
       
       ;Springe zu diesem Kernel
       mov ax, 0x1000 ; Die Adresse des Programms
       mov es, ax     ; Segmentregister updaten
       mov ds, ax
       jmp 0x1000:0x0000
       
       ; ----------------------------------------------
       ; Funktionen und Variablen
       ; ----------------------------------------------
       
       bootdrv db 0 ;Das Bootlaufwerk
       loadmsg db "Laden...",13,10,0
       
       ; Einen String ausgeben:
       putstr:
       lodsb             ; Byte laden
       or al,al
       jz short putstrd  ; 0-Byte? -> Ende!
       
       mov ah,0x0E       ; Funktion 0x0E
       mov bx,0x0007     ; Attribut-Byte (wird nicht benötigt)
       int 0x10          ; schreiben
       jmp putstr        ; Nächstes Byte
       putstrd:
       retn
       
       ; Lade den Kernel vom Bootlaufwerk
       load:
       ; Diskdrive reset (Interrupt 13h, 0)
       mov ax, 0          ; Die gewünschte Funktion (reset)
       mov dl, [bootdrv]  ; Dieses Laufwerk ist gewünscht
       int 13h            ; Den Interrupt ausführen
       jc load            ; Geht nicht? -> Noch mal!
       
       load1:
       mov ax,0x1000      ; ES:BX = 0x10000
       mov es,ax
       mov bx, 0
       
       ; Sektoren lesen (Interrupt 13h, 2)
       mov ah, 2         ; Funktion 2 (Lesen)
       mov al, 5         ; Lese 5 Sektoren
       mov cx, 2         ; Cylinder=0, Sector=2
       mov dh, 0         ; Head=0
       mov dl, [bootdrv] ; Laufwerk aus Vorgabe
       int 13h           ; ES:BX =  Daten vom Laufwerk
       jc load1          ; Fehler? Noch mal!
       mov si,loadmsg
       call putstr       ; Meldung ausgeben
       retn
       
       times 512-($-$$)-2 db 0   ; Dateilänge: 512 Bytes
       dw 0AA55h                 ; Bootsignatur

\</asm\>

Ein kleiner Kernel zum Testen...

Nun kneten wir uns einen kleinen Kernel, damit unser Bootloader auch was zu laden hat.

\<asm\>

       ; ---------------------------------------------------
       ; Unser Kernel
       ; ---------------------------------------------------
       
       mov ax, 0x1000 ; Segmentregister updaten
       mov ds, ax
       mov es, ax
       
       start:
       mov si, msg
       call putstr   ; Schicke Bootmessage :)
       
       mov si,msg_boot
       call putstr   ; Noch eine Message :D
       
       call getkey   ; Warte auf einen Tastendruck
       jmp reboot    ; Reboot
       
       ; -------------------------------------------------
       ; Funktionen und Variablen
       ; -------------------------------------------------
       
       msg db "Herzlich Willkommen zu StupidOS 0.1",13,10,0
       msg_boot db "Beliebige Taste druecken...",10,0
       
       ; Stringausgabe
       putstr:
       lodsb            ; Byte laden
       or al,al
       jz short putstrd ; 0-Byte? -> Ende!
       mov ah,0x0E      ; Funktion 0x0E
       mov bx,0x0007    ; Atrribut-Byte
       int 0x10         ; schreiben
       jmp putstr       ; nächstes Byte
       putstrd:
       retn
       
       ; Warte auf einen Tastendruck
       getkey:
       mov ah, 0 ; Funktion 0
       int 0x16  ; Ausführen
       ret
       
       ; Rebooten.
       reboot:
       jmp 0xffff:0x0000

\</asm\>

Kompilieren und Testen

So! Gleich ist es soweit! Wir müssen nur noch unsere Dateien assemblieren:

       C:\StupidOS>nasm -f bin -o boot.bin boot.asm
       C:\StupidOS>nasm -f bin -o kernel.bin kernel.asm

Dann legen wir ein Diskimage an, indem wir die Dateien zusammenkopieren:

       C:\StupidOS>copy /b boot.bin + kernel.bin myOS.img

Und zum Schluss schreiben wir das Image mit Rawrite auf die Diskette:

       C:StupidOS> rawwritewin
       (den Anweisungen folgen, myOS.img auf "a" schreiben)

Jetzt rebootet ihr ganz einfach euren Rechner mit unserer neuen bootfähigen Diskette im Laufwerk... TÄDÄÄÄÄÄÄÄH!!!

**Anmerkung:** Wer sein OS mit [QEMU](QEMU.md "QEMU") testen will, sollte dafür sorgen, dass auch die Größes des Kernels durch 512 teilbar ist, da QEMU nur ganze Sektoren lädt.

## Lowlevel-Grundlagen, Teil 1

### Prozessoraufbau

Der kleinste gemeinsame Nenner bei Prozessoren der x86-Familie ist der 8086. Hierbei handelt es sich bereits um einen 16-Bit-Prozessor, d.h. über den Datenbus können 16 Bit auf einmal in den Prozessor geladen werden. Kurz nach Erscheinen dieses Prozessors gab Intel noch eine Variante für den schmaleren Geldbeutel heraus, der 8088. Dieser verfügte nur über einen 8 Bit breiten Datenbus, d. h. um 16 Bit zu laden, musste dieser Prozessor halt zwei Speicherzugriffe durchführen, statt nur einem beim 8086. Aber das wusste der Prozessor selbst. Aus programmiertechnischer Sicht können der 8086 und der 8088 gleich behandelt werden. Alles, was sich im 8086 findet, wurde in den nachfolgenden Prozessoren nicht entfernt, deshalb gelten die folgenden Ausführungen für alle Prozessoren (der x86-Familie).

Der Prozessor enthält so genannte Register, die man sich als kleine Speicherstellen vorstellen kann. Der Programmierer kann diese Register über einen Namen ansprechen, die tatsächliche physische Realisierung ist damit für den Programmierer ohne Belang, er muss sich also keine Adressen merken. Ursprünglich hatte jedes Register eine genau zugeteilte Aufgabe, aber in den späteren Prozessoren verschwand diese strikte Unterteilung immer mehr.

Bis zum 80286 waren die Register maximal 16 Bit breit, d. h. es passten Werte mit einer maximalen Größe von 16 Bit in diese Register. Ab dem 80386 wurden einige Register auf 32 Bit erweitert und seit dem Pentium gibt es auch 64-Bit-Register.

Die Register können grob in allgemeine Register, Segmentregister, Pointer- bzw. Indexregister und sonstige Register unterteilt werden.

#### Allgemeine Register

Die allgemeinen Register sind 16 Bit breit, können aber jeweils in zwei 8 Bit breite Register aufgeteilt werden. Das niederwertige Register wird mit dem Buchstaben L, das höherwertige Register mit dem Buchstaben H gekennzeichnet. In Verbindung mit dem Buchstaben A, B, C oder D ergibt sich ein vollständiger Registername. Zum Beispiel wird aus AX (16 Bit breit) das Register AL (8 Bit) und das Register AH (8 Bit). Änderungen an AL oder AH schlagen sich immer auch auf AX nieder.

Und hier die einzelnen Register:

|  |  |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| AX | Akkumulator. Wird häufig für arithmetische Operationen (Division, Multiplikation) verwendet. Der höherwertige Teil AH nimmt häufig die Funktionsnummer bei interruptbasierten Operationen auf. |
| BX | Basis. Wird meist bei der Adressierung von Werten im Speicher verwendet. |
| CX | Counter. Vielfach in Schleifenstrukturen als "Laufvariable" eingesetzt. |
| DX | Daten. Wird ebenfalls für die Adressierung eingesetzt. |

Einige Befehle oder Routinen arbeiten mit bestimmten Registern. In diesen Fällen ist die Benutzung der Register genau an den Befehl gebunden. Abgesehen von diesen speziellen Aufgaben können diese Register jederzeit verwendet werden, zum Beispiel, um Werte im Prozessor statt im Speicher zwischenzulagern.

  

#### Segmentregister

Um diese Register zu erklären, muss etwas weiter ausgeholt werden.

Wie bereits gesagt wurde, verfügt der 8086 über einen 16 Bit breiten Datenbus. Zusätzlich enthält er auch noch einen Adressbus, den man sich als ein Bündel von Adressleitungen vorstellen kann. Dieses Bündel umfasst 20 Leitungen. Adressierbar sind damit also 2^20 Bytes (entspricht 1048576 Bytes oder einem Megabyte).

Sie haben sicherlich schon gehört, dass MS-DOS nur ein Megabyte Speicher ansprechen kann. Das ist allerdings weniger ein Problem von DOS, sondern liegt eher in der verzahnten Entstehung von DOS und dem 8086. Aus Kompatibilitätsgründen wurde aus dieser Begrenzung später auch kein richtiger Ausweg gesucht.

Um auf eine Adresse im Speicher zugreifen zu können, muss sie in einem Register hinterlegt sein. Die Register des 8086 waren aber nur maximal 16 Bit breit. Mit 16 Bit lassen sich aber nur 2^16=65536 Bytes (64 KB) ansprechen.

Um diesem Dilemma aus dem Weg zu gehen, entschloss man sich, zwei Register für die Adressierung zu verwenden. Damit ließen sich dann immerhin 2^32 Bytes adressieren. Da der Adressraum des 8086 aber nur ein Megabyte (2^20) umfasste, blieben von den 32 Bit (4 GB) 12 Bit unbenutzt (32-20=12). Aus diesem Grunde verfiel man bei Intel auf die Idee der Segmentierung.

Als Voraussetzung für die folgenden Überlegungen gehen wir davon aus, dass ein Segment eine bestimmte Anzahl Bytes enthalten kann und im Prozessor ein Register existiert, das eine Segmentnummer enthalten kann. Dieses Register ist 16 Bit breit.

An welchen Adressen beginnen nun Segmente? Dividieren wir die maximale Größe des Adressraumes durch die maximal mögliche Anzahl an Segmenten, so erhalten wir 2^20 / 2^16 = 2^4 = 16. Ein Segment ist also ein Block mit einer Größe von 16 Bytes. Ein Segment kann demzufolge an jeder Adresse beginnen, die ohne Rest durch 16 teilbar ist. In das Segmentregister muss dann die Nummer des Segmentes eingetragen werden. Dessen Adresse errechnet sich dann so:

       Segmentnummer * 16 Bytes

Bis jetzt können wir nur auf Segmente oder besser Segmentgrenzen zugreifen. Um den Zugriff auf einzelne Bytes innerhalb der Segmente zu ermöglichen, wird ein zweites Register verwendet. Dieses enthält einen Zeiger auf ein bestimmtes Byte, letzlich auch nur eine Zahl. Um also das 4. Byte im 6. Segment ansprechen zu können, muss ins Segmentregister der Wert 6 und in das zweite Register der Wert 4 eingetragen werden. Eine vollständige Adresse errechnet sich folgendermaßen:

       Segmentnummer * 16 + Offset (Abstand zum Segmentanfang)

Die logische Darstellung von Segment und Offset sieht so aus:

       Segment:Offset

Also zum Beispiel 00006:00004 (üblicherweise erfolgt die Darstellung in hexadezimaler Schreibweise).

Mit einem 16-Bit-Register kann man wesentlich mehr als nur die 16 Bytes bis zur nächsten Segmentgrenze adressieren. Dies bedeutet, dass man mit diesem Zeigerregister über mehrere Segmentgrenzen hinweg operieren kann. Im Umkehrschluss bedeutet das auch, dass eine lineare Speicheradresse mit verschiedenen logischen Adressen ansprechbar ist. So ist die logische Adresse 00006:00004 gleichbedeutend mit der logischen Adresse 00005:00020 (Sie können es nachrechnen - es ergibt sich die physikalische Adresse 100).

Und weil mit einem Zeigerregister 64 KB adressierbar sind, ist es tatsächlich möglich, mit einer Segment:Offset-Kombination mehr als ein Megabyte anzusprechen. Dies ergibt sich aus folgender Rechnung:

|  |  |
| --------------------------- | ---------------------------------------- |
| max. Anzahl Segmente | 65536 |
| Größe eines Segments | 16 Bytes |
| max. Größe des Offsets | 65536 Bytes |
| physikalische Adresse | Segmentnummer \* Segmentgröße + Offset |
| max. ansprechbare Adresse | 65536 \* 16 + 65536 = 1114112 |

Der Überhang über ein MB wird unter DOS als High Memory Area (HMA) bezeichnet.

Ein Segmentregister ist immer 16 Bit breit und lässt sich im Gegensatz zu den allgemeinen Register nicht in einen nieder- und einen höherwertigen Teil zergliedern.

|  |  |  |
| ----- | ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| CS | Codesegment | Enthält die Nummer des Segmentes, das den aktuellen Code enthält - siehe Informationen zum Register IP. |
| DS | Datensegment | Enthält die Nummer des Segmentes, das die Daten enthält. Der Offset kann in verschiedenen Registern stehen oder als Konstante übergeben werden. |
| ES | Extrasegment | Findet vor allem bei den Stringoperationen Verwendung, in diesen Fällen steht der Offset im Register DI. |
| SS | Stacksegment | Enthält die Nummer des Segmentes, das den Stack enthält. Offsets stehen in den Register BP oder SP. Die Bedeutung des Stack wird später geklärt. |
| FS | Erst ab dem 80386 | Dient vor allem als Zusatzsegmentregister, wird hauptsächlich im Protected Mode verwendet. |
| GS | Erst ab dem 80386 | Dient vor allem als Zusatzsegmentregister, wird hauptsächlich im Protected Mode verwendet. |

#### Indexregister

Im Befehlssatz des 8086 gibt es die so genannten Stringbefehle. Den Begriff String darf man an dieser Stelle aber nicht mit gleichlautenden Datenstrukturen aus Hochsprachen verwechseln.

Wichtig! Ein String ist für den Prozessor eine Aneinanderreihung von Daten eines bestimmten Typs (Byte, Word). Dazu sei gesagt, dass der Prozessor Zeichen (Char) als Bytes behandelt. Der Prozessor sieht lediglich den ASCII-Code (oder eine andere numerische Codierung), die Interpretation als Zeichen muss der Programmierer vornehmen. Aufgrund der prozessorseitigen Interpretation als Zahl ist es sehr einfach, mit Buchstaben zu rechnen.

Die Stringbefehle umfassen das Kopieren aus und Schreiben in einen String, kopieren eines ganzen Strings oder Teile davon, den Stringvergleich und das Suchen in Strings. Die Indexregister übernehmen zusammen mit einem vom jeweiligen Stringbefehl abhängigen Segmentregister die Aufgabe, auf die nächste zu bearbeitende Adresse im String zu zeigen. Wie die Segmentregister sind die Indexregister 16 Bit breit und nicht teilbar.

|  |  |  |
| ----- | ------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| DI | Destination Index | Kann im Grunde frei verwendet werden, dient aber bei den Stringbefehlen in Verbindung mit dem Register ES als genaue Adressangabe. |
| SI | Source Index | Kann im Grunde frei verwendet werden, dient aber bei den Stringbefehlen in Verbindung mit dem Register DS als genaue Adressangabe. |

#### Der Stack und die Pointerregister

Da diese Register in engem Zusammenhang zum so genannten Stack stehen, wird hier zuerst geklärt, was ein Stack denn überhaupt ist.

Stack bedeutet übersetzt soviel wie Stapel und übertragen auf einen Stapel Teller handelt es sich um einen so genannten LIFO-Speicher. LIFO steht für Last In First Out. Dessen Gegenteil ist der FIFO-Speicher (First In First Out). In der Praxis bedeutet LIFO, dass das letzte Element, das auf den Stapel gelegt wird, auch als erstes wieder vom Stapel entfernt wird. Genau wie der Tellerstapel: der letzte Teller, der oben aufgelegt wird, ist auch der erste Teller, der wieder entnommen wird.

Im Umfeld eines Prozessors dient der Stack hauptsächlich als Zwischenspeicher für Adressen, wenn es um Unterprogramme geht, dient er auch als Medium, um Parameter zu halten.

Wozu benötigt man den Stack jetzt konkret? Ganz einfach. Wenn der Prozessor ein Unterprogramm anspringt, dann muss er sich irgendwo merken, an welcher Adresse im Codesegment dieses Unterprogramm aufgerufen wurde, da nach Beendigung des Unterprogramms das aufrufende Programm hinter dieser Stelle fortfahren muss. Folgender Pseudocode soll zur Erklärung beitragen:

- Anweisung1
- Anweisung2
- Anweisung3
- Unterprogrammaufruf
- Anweisung5
- .
- .
- .
- AnweisungN

Der Prozessor muss sich also die Rücksprungadresse merken, damit er ordnungsgemäß mit Anweisung 5 fortfahren kann. Der Hinterlegungsort für diese Adresse ist der Stack, dem Intel gleich ein eigenes Segment spendiert hat. Dessen Adresse steht im Register SS.

Als zweites Hauptanwendungsgebiet werden im Stack Parameter für Unterprogramme untergebracht.

Und wenn gerade mal kein Prozessorregister mehr frei ist um einen Wert zu speichern und man die Einrichtung einer eigenen Variablen vermeiden will, dann ist der Stack einfach nur ein Zwischenspeicher.

Üblicherweise sollte jedes Programm über einen Stack verfügen. Sollte dies nicht zutreffen und es wird Platz auf dem Stack benötigt, dann bedient sich der Prozessor beim aufrufenden Programm, auch wenn es sich dabei um das Betriebssystem handelt. In aller Regel sehen Programme (und Betriebssysteme erst recht) nicht vor, dass andere Programme als sie selbst den Stack verwenden. Aus diesem Grunde kann es ganz schnell zum sogenannten Stack Overflow kommen, der vielleicht noch abgefangen wird, oft genug aber den ganzen Rechner abstürzen lässt.

Als Besonderheit des Stacks ist zu beachten, dass die Adresse der aktuellen Stackspitze von oben nach unten wächst, d. h. je mehr Elemente auf den Stack gelegt werden, desto niedriger ist die Adresse der Stackspitze.

Wo der Stack dann letztlich liegt, wird erst beim Start des Programms festgelegt. Die benötigte Größe des Stacks ist im Voraus oft nur schlecht bestimmbar. Wenn man mit rekursiven Unterprogrammen arbeitet, also Prozeduren, die sich selbst aufrufen, die Anzahl der Aufrufe aber größer ist als es der Stack zulässt, dann kann im schlimmsten Fall der gesamte Rechner abstürzen, weil wichtige Daten überschrieben werden. Besonders bei COM-Dateien, die ja nur maximal eine Größe von 64 KB erreichen können und alles im gleichen Segment liegen muss, kann es sein, dass der nach unten wachsende Stack Teile des Codes überschreibt.

Bezüglich Größe und Teilbarkeit gilt das gleiche wie bei den Indexregistern.

|  |  |  |
| ----- | --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SP | Stack Pointer | Dieses Register zeigt auf die aktuelle Stackspitze |
| BP | Base Pointer | Dieses Register zeigt auf die für den aktuellen Kontext gültige Stackbasis. Meist verwenden Unterprogramme einen eigenen sogenannten Stackrahmen und mit Einbeziehung dieses Registers lassen sich Adressen von übergebenen Parametern errechnen. |

#### Das Flagregister

Dieses Register wird auch Prozessorzustandsregister genannt. Es ist 16 Bit breit und jedes einzelne Bit spiegelt einen bestimmten Zustand nach einer Operation des Prozessors wider.

Meistens sollen abhängig von diesem Zustand bestimmte Aktionen durchgeführt werden. Eine Verzweigung in einem Assemblerprogramm ist nur über Sprünge realisierbar. Im Befehlssatz des 8086 befinden sich die so genannten bedingten Sprungbefehle, die die Flags auswerten und entsprechend zu anderen Programmstellen verzweigen.

Beim 8086 sieht es folgendermaßen aus ("\_" bedeutet: reserviertes oder noch nicht belegtes Bit):

| 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| ----- | ----- | ----- | ----- | ---------- | ----------- | ------------------ | -------------------- | ------ | ------ | ----- | ----------- | ----- | -------- | ----- | ------- |
| \- | \- | \- | \- | Overflow | Direction | Interrupt Enable | Trap / Single Step | Sign | Zero | \- | Auxiliary | \- | Parity | \- | Carry |

#### IP - Instruction Pointer

Dies ist eines der wichtigsten Register des Prozessors. Es enthält einen Zeiger auf die Adresse im Codesegment, an der der nächste auszuführende Befehl steht (CS:IP).

Der Programmierer kann dieses Register nicht direkt beeinflussen. Eine Einflussnahme ist nur über die Sprungbefehle oder den Aufruf eines Unterprogramms oder einem Rücksprung aus einem solchen möglich.

### Spätere Prozessorgenerationen

Die Entwicklung ist selbstverständlich nicht beim 8086 stehen geblieben. Intel brachte noch eine Reihe weiterer Prozessoren heraus, die natürlich um Befehle, Register und Fähigkeiten erweitert wurden, trotzdem aber Kompatibilität zum jeweiligen Vorgänger wahrten.  

- 80186/80188
- 80286
- 80386 DX/SX
- 80486 DX/SX
- Pentium (und Pentium MMX)
- Pentium Pro
- Celeron
- Pentium II/III (und XEON-Varianten)
- Pentium 4

Im folgenden ein kurzer Abriss dessen, was den neuen Prozessoren alles spendiert wurde.

#### 80186/80188

Intel brachte zu diesem Prozessor wieder eine 8-Bit-Variante heraus (80188). Als wichtige neue Befehle treten BOUND, ENTER und LEAVE auf die Bildfläche. BOUND kann prüfen, ob Arraygrenzen über/unterschritten wurden. Unter DOS sind für diesen Befehl aber Vorarbeiten nötig, weil er einen Bildschirmausdruck (Hardcopy) verursachen kann, wenn die Arraygrenzen über/unterschritten wurden.

Die Befehle ENTER und LEAVE vereinfachen die Verwendung von Unterprogrammen. Den 8018x findet man eher in Maschinensteuerungsanlagen als in PCs.

#### 80286

Mit diesem Prozessor war es möglich, die vom 8086 rührende Speicherbegrenzung (ein MB) zu knacken.

Intel erhöhte die Zahl der Adressleitungen von 20 auf 24 und führte den so genannten Protected Mode (PM) ein, durch den dieser Prozessor immerhin 16 MB linearen Speicher ansprechen konnte. Im Protected Mode dienen die Inhalte der Segmentregister als Selektoren auf Deskriptorentabellen. Ein Deskriptor ist eine Datenstruktur die ein Segment im Protected Mode beschreibt.

Des Weiteren wurden die Unterstützung für den Umgang mit virtuellem Speicher und verschiedene Schutzmechanismen (die zum PM gehören) eingebaut. Diese Schutzmechanismen bestehen aus Segmentgrenzenprüfung, Schreib/Lese/Ausführungsbeschränkungen für Segmente und maximal vier Privilegstufen. Die Privilegstufen und das durch den Prozessor unterstützte Task Switching sowie lokale Deskriptortabellen ermöglichen den Schutz von Programmen voreinander und den Schutz des Betriebssystemcodes vor den Anwendungen. Leider vergaßen die Intel-Entwickler, dem Prozessor einen Befehl zum Rücksprung aus dem PM mitzugeben. Zum Rücksprung wäre ein kompletter Prozessor-Reset nötig gewesen, was einem Neustart gleichkommt. Fakt ist jedenfalls, dass der PM beim 80286 kaum verwendet wurde, wenngleich Sie vielleicht eine der Borland-Entwicklungsumgebungen in Verwendung haben, die Kompilate für den 80286-PM erzeugen können.

#### 80386 DX/SX

Die allgemeinen Register, die Index- und Pointerregister, das Flagregister und IP wurden auf 32 Bit erweitert. Ansprechbar werden die vollen 32 Bit durch Voranstellen eines "E" vor den ursprünglichen Registernamen, also z.B. EAX, ESI, EBP. Die niederwertigen 16 Bit entsprechen dem ursprünglichen 16-Bit-Register. Auf die oberen 16 Bit kann man nur über einen Umweg zugreifen. Ebenso wurden die meisten Befehle so erweitert, dass sie mit 32-Bit-Operanden arbeiten können.

Die SX-Variante wurde gegenüber der DX-Variante in ihren Kontaktmöglichkeiten mit der Außenwelt eingeschränkt. Statt 32 Datenleitungen (DX) erhielt sie nur 24, d.h. auch hier waren mehr Zugriffe nötig, was aber für den Programmierer ohne Belang ist.

Durch die 32-Bit-Register und die Erweiterung des Adressbusses auf 32 Bit konnten 4 GB linearen Speichers adressiert werden. Es kann sowohl mit segmentiertem Speicher als auch mit dem sog. Flat Memory Model gearbeitet werden. Im Flat Model stehen dem Anwendungsentwickler die vollen 4 GB zur Verfügung. Das Programm kann also so tun, als wäre es allein im Speicher. Die moderneren Windows-Version ab Windows 95 stellen dem Entwickler dieses Speichermodell zur Verfügung, was die Programmentwicklung deutlich einfacher macht.

Intel erkannte die beim 80286 gemachten Fehler und legte diesmal eine Rücksprungmöglichkeit aus dem PM bei. Gleichzeitig wurden noch diverse Control- und Debugregister eingeführt, die hauptsächlich im PM Verwendung finden. Der sogenannte V86-Modus ermöglichte ein Betreiben des Prozessors im Protected Mode, erlaubte aber die Ausführung von normalen Nicht-PM-Programmen.

Mit dem 80386 wurde das Paging eingeführt. Jede Page hat eine Größe von 4 KB. Paging ist Bestandteil des Managements des Virtuellen Speichers und völlig transparent für den Anwendungsentwickler (wird durch das Betriebssystem gesteuert).

Dieser Prozessor war der erste in der Reihe, der einen Ansatz von Parallelverarbeitung bot. Dabei waren 6 Stufen parallel geschaltet, die aus der Buseinheit, der Code Prefetch-Einheit, der Befehlsdecodierungseinheit, der Ausführungseinheit, der Segmenteinheit und der Paging-Einheit bestehen. Der 80386 war der Grundstein damit heute so populäre Betriebssysteme wie Windows, Unix und Linux auf dieser Prozessorfamilie ihre Leistung ausspielen können.

#### 80486 DX/SX

Die Möglichkeit der parallelen Befehlsverarbeitung wurde verbessert indem die Befehlsdecodierungseinheit und die Ausführungseinheit zu 5 in einer Pipeline angeordneten Stufen erweitert wurden. Zusätzlich wurde noch ein 8 KB First-Level-Cache auf dem Prozessor untergebracht der vor allem den Zugriff auf Speicheroperanden drastisch erhöhte wenn sie sich bereits im Cache befanden. Beim 486 DX gelang Intel endlich die Vereinigung des normalen Prozessors mit einem numerischen Coprozessor. Unterstützung für Second Level Cache und Multiprozessorsysteme wurde ebenfalls eingebaut.

#### Pentium

Intel entschied sich für eine Abkehr von der normalen Nummerierung (8086, 80186 .. 80486), da sich Zahlen in den USA nicht als Warenzeichen schützen lassen und diverse andere Hersteller Clones von Intels Prozessoren unter der gleichen Bezeichnung herstellten.

Bislang war es für einen Programmierer recht schwer, herauszufinden, mit was für einem Prozessor er es zu tun hat. Beim Programmieren selbst weiß er das sicherlich selbst, aber wenn das Produkt beim Kunden ist, dann soll vielleicht abhängig vom Prozessor eine bestimmte Aktion ausgeführt werden, beispielsweise eine Meldung, dass der vorgefundene Prozessor zu alt für das Programm ist, da 80386-Befehle verwendet werden, der Prozessor aber ein 80286 ist.

Beim Pentium endlich legte Intel einen Befehl bei, der nicht nur einen herstellerspezifischen String zurückgab (GenuineIntel, AuthenticAMD bei AMD-Prozessoren), sondern auch Informationen über verschiedene Prozessorfähigkeiten zu liefern vermochte. Das sind natürlich Fähigkeiten, die sich viele Programmierer schon viel früher gewünscht hätten, die jetzt aber umso mehr genutzt werden.

Der Pentium enthielt eine zweite Ausführungseinheit was die Ausführung von theoretisch zwei Befehlen je Takt ermöglichte. Der First-Level-Cache wurde auf 16 KB erweitert (je 8 KB für Code und Daten). Beim Paging konnte die Größe einer Page auf 4 MB erhöht werden. Sprungvorhersage konnte die Performance in Schleifenkonstrukten steigern. Neben neuen Befehlen erhielt der Pentium einen weiteren Betriebsmodus (SMM).

Mit einer späteren Version des Pentium führte Intel die MMX-Technologie ein. Dabei kommt das SIMD-Modell (Single Instruction, Multiple Data) zur parallelen Berechnung von Werten in den MMX-Registern. MMX sollte vor allem der Leistungssteigerung im Multimediabereich (Bild/Film-und Tonbearbeitung) dienen. Tatsächlich handelt es sich bei den MMX-Registern nicht um neue Register. Stattdessen werden die Register der FPU verwendet. Deswegen ist bei der Arbeit mit der FPU zu beachten, dass nicht auch gleichzeitig MMX-Befehle abgearbeitet werden (und umgekehrt).

#### Pentium Pro

Mit dem Pentium Pro führte Intel die sogenannte P6-Familie ein. Diese Prozessoren verwenden eine neue superskalare Mikro-Architektur. Da noch immer der gleiche Fertigungsprozess verwendet wurde waren Leistungssteigerungen nur durch Fortschritte in der Mikro-Architektur möglich. Hier handelt es sich um einen vollwertigen 32-Bit-Prozessor mit RISC-Kern, der allerdings bei 16-Bit-Programmen nicht nur starke Leistungseinbußen zeigt sondern teilweise langsamer als ein normaler Pentium oder 486 wurde.

Der Adressbus wurde auf 36 Bit erweitert, wodurch 64 GB physikalischer Speicher adressierbar wurden.

#### Celeron

Die Celeron-Prozessoren sind speziell auf den typischen Heim-PC oder den einfachen Büroarbeitsplatz zugeschnitten. Bei gleicher Taktrate bieten sie weniger Leistung als ein gleich getakteter Pentium (was aber beim anvisierten Verwendungszweck keine weiteren Probleme darstellt).

#### Pentium II/III

Hier hat sich vor allem der physikalische Aufbau verändert. Durch weitergehende Miniaturisierung wurden Leistungssteigerungen erreicht. Mit dem Pentium II hielt MMX in der P6-Familie Einzug. Der First-Level-Cache für Daten und Code wurde auf je 16 KB erhöht, ein Second-Level-Cache von bis zu 1 MB wurde möglich. Das Power Management wurde verbessert.

Die XEON-Varianten vereinten eine Reihe von Eigenschaften und erweiterten sie um eine bessere Unterstützung der Anforderungen an hochperformante Server zu bieten.

Der Pentium III besaß als erster die Streaming SIMD Extensions (SSE), die vor allem neue, 128 Bit breite Register und neue Berechnungsmodi für Gleitkommazahlen boten. Die acht neuen 128 Bit breiten Register für die SSE-Operanden erhielten den leicht verwechselbaren Namen XMM-Register.

#### Pentium 4

Der P4 enthält eine ganze Reihe von Neuerungen. Zum einen basiert er auf der Intel NetBurst Mikro-Architektur, zum anderen bietet er SSE2, die MMX und SSE um 144 neue Befehle erweitern (Berechnungen mit 128-Bit-Operanden, Cache- und Speichermanagement) und Multimediaanwendungen weiter beschleunigen.

Des Weiteren arbeitet er mit dem neuen 400 MHz Intel NetBurst Bus und ist dabei immer noch kompatibel zu allen Anwendungen die für die 32-Bit-Intel Prozessoren geschrieben wurden.

  

### Prozessormodi

#### Real Mode

In diesem Modus befindet sich der Prozessor nach Einschalten des Rechners oder nach einem Reset. Die Daten werden über normale 16:16 Segment - Offset - Kombinationen angesprochen und maximal 1 MB Speicher ist adressierbar.

Nach dem Willen von Intel sollte dieser Modus seit dem 80286 nur noch als Sprungbrett für den Protected Mode dienen. Auch wenn ein Pentium III im Real Mode betrieben wird, ist er eigentlich nicht anderes als ein um zusätzliche Register und Befehle erweiterter, dafür aber sehr schneller 8086. Beibehalten wurde dieser Modus also hauptsächlich aus Kompatibilitätsgründen.

**Hinweis:**

Weitere Informationen gibt es im Artikel [Real Mode](Real-Mode.md "Real Mode")

  

#### Protected Mode

Der Protected Mode (PM) wurde mit dem 80286 eingeführt und mit dem 80386 das Fundament heutiger moderner Betriebssysteme wie Windows 9x/NT, OS/2 und Linux geschaffen. Erst im PM kann der Prozessor Multitasking, Multihreading, Speicherschutz, Privilegebenen und vieles weitere ermöglichen.

Im Gegensatz zum Real Mode sind für die Adressierung völlig andere Speicherstrukturen notwendig, die so klangvolle Namen wie Descriptor und Selektor tragen, in lokalen und globalen Tabellen abgelegt werden und kurzerhand dafür sorgen, dass man alles, was man über die Adressierung im Real Mode jemals wusste getrost vergessen kann.

An den bisher eingeführten Befehlen ändert sich nichts, dafür sind jede Menge Register und weitere Befehle hinzugekommen, die teilweise nur im PM funktionieren, teilweise nur den Wechsel von Real Mode zu PM vorbereiten.

**Hinweis:**

Weitere Informationen gibt es im Artikel [Protected Mode](Protected-Mode.md "Protected Mode")

#### V86-Mode

Der V86-Mode ist eine Sonderform des Protected Mode. Hier wird der vorhandene Speicher so eingeteilt, dass dem darin laufenden Programm vorgegaukelt wird, es befände sich auf einem 8086, d. h. das Programm kann maximal 1 MB Speicher ansprechen. Tatsächlich können in diesem Modus aber auch Befehle von Prozessoren \> 8086/88 verwendet werden.

Ein gutes Beispiel ist der Treiber EMM386.EXE. Sobald dieser geladen ist, versetzt er den Prozessor in den V86-Mode, mit der Konsequenz, dass das in diesem einen MB laufende Programm DOS selbst ist. Anders wäre die Speicherkontrolle unter Wahrung der Kompatibilität zu älteren Prozessoren nicht zu erreichen. Im Gegensatz zum reinen PM können in diesem Modus also normale Real Mode-Programme laufen.

**Hinweis:**

Weitere Informationen gibt es im Artikel [Virtual 8086 Mode](Virtual-8086-Mode.md "Virtual 8086 Mode")

#### SMM - System Management Mode

Dieser Stromsparmodus wurde mit dem Pentium eingeführt. In ihn wird gewechselt, wenn der Prozessor ein bestimmtes Signal über eine seiner vielen Leitungen erhält, es gibt also keinen direkten Befehl für die Umschaltung. Dafür hält der Pentium-Befehlsvorrat einen Befehl bereit, der den Prozessor aus seinem Schlafmodus erweckt.

**Hinweis:**

Weitere Informationen gibt es im Artikel [System Management Mode](System-Management-Mode.md "System Management Mode")

  

## Code Corner

### CPU \>= 386

\<asm\>

       ; determine CPU type. Code from Freedows 98 ldr_asm.asm
       ; Copyright (C) 1997 Joachim Breitsprecher 
       cpu_check:
           cli
           pushf
           pushf
           pop ax
           mov bx,ax      ; ax=bx=flags
           and ax,0x0FFF  ; ax=flags AND 0x0FFF
           or bx,0x7000   ; bx=flags | 0x7000
           push ax        ; try clearing b15:b12 of flags
           popf
           pushf
           pop ax         ; ax=result
           push bx        ; try setting b14:b12 of flags
           popf
           pushf
           pop bx         ; bx=result
           popf
           and ax,0xF000
           cmp ax,0xF000
           je not_386     ; 80(1)86/88 sets b15:b12
           test bx,0x7000 ; 80286 clears b14:b12
           jne is_386plus
           
           not_386:

\</asm\>

## OS-Showcase: MenuetOS

**Hinweis:**

Es existiert ein Wikiartikel zu [MenuetOS](MenuetOS.md "MenuetOS").

![menuet1.gif](http://lowlevel.brainsware.org/wiki/images/menuet1.gif) ![menuet2.gif](http://lowlevel.brainsware.org/wiki/images/menuet2.gif) ![menuet3.gif](http://lowlevel.brainsware.org/wiki/images/menuet3.gif)

  

### OS Design

Ein wenig seltsam, aber gut durchdacht. Die meisten OSes basieren auf einer Shell und die GUI ist schmückendes Beiwerk. Bei MenuetOS ist es genau anders herum: die tolle GUI steht im Vordergrund, die Shell ist ein wenig mager geraten. Obwohl man eine richtige Shell vermisst, kann man sich sehr schnell in die GUI reinarbeiten.

### Funktionalität

Umfangreich. Hier ein Auszug aus der Features-Liste:

- pre-emptive multitasking, multithreading, ipc
- graphical UI with 16 M colours up to 1280x1024
- ide: editor/compiler for applications and kernel
- ethernet: tcp/udp/icmp/ip
- http/mp3 servers, 3D maze
- free-form, skinnable application windows
- hard real-time data fetch

Vorbildlich: zu jedem Feature gibt es gleich das passende Beispielprogramm.

### Stabilität / Kompatibilität

Sehr gut. Kein einziges Kompatibilitätsproblem und während dem Test nur ein einziger Absturz (selbst dieser wahrscheinlich wegen unsachgemäßer Bedienung).

### Dokumentation

Gut. Zwar nicht sehr ausführlich, aber die meisten Themen werden behandelt.

### Fazit

MenuetOS ist ein Betriebssystem, bei dem man auf mehr hoffen kann. Die Entwickler haben bereits jetzt ein sehr solides OS gemacht, und mit ein wenig Arbeit wird MenuetOS ein tolles Hobby-OS!

## Nächste Ausgabe

Für die [nächste Ausgabe](Ausgabe-2.md "Ausgabe 2") sind folgende Themen geplant:

- Design von Kernels
- Lowlevel Teil 2: Interrupts, IO-Ports, Speicheradressen
- Real Mode vs. Protected Mode

## Nachwort

Das wars auch schon wieder mit der ersten Ausgabe von Lowlevel. Ich hoffe, dass dieses Magazin ein wenig Licht in die dunkle Ecke von OS Development bringt... in den nächsten paar Wochen wird das Internet wohl mit Selfmade-OSes überschwemmt sein ^\_^

Eine Bitte noch: Mailt mir, wie es euch gefallen hat! Das ist für mich ganz wichtig!

**Mastermesh**

|  |  |  |
| ----- | ---------------- | ------------------------------------------------------------------------------- |
|  | **Navigation** | [Ausgabe 2](Ausgabe-2.md "Ausgabe 2") » |

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/7484/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1412/index.html)

<!-- MediaWiki page 1412; revision 7484; parent 7470; 2010-04-01T10:35:19Z -->
