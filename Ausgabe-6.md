# Ausgabe 6

|  |  |
| ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| © | Dieser Artikel ist urheberrechtlich geschützt.<br>Bitte beachte, dass die üblichen [Lizenzbestimmungen](https://lowlevel-eu.github.io/wiki/pages/1637/index.html "Lowlevel:Urheberrecht") des Wikis für diesen Artikel nicht gelten. |

  

|  |  |  |
| ------------------------------------------------------------------------------- | ---------------- | ------------------------------------------------------------------------------- |
| « [Ausgabe 5](Ausgabe-5 "Ausgabe 5") | **Navigation** | [Ausgabe 7](Ausgabe-7 "Ausgabe 7") » |

## Vorwort

Nach relativ langer Zeit gibt es nun doch endlich die neue, sechste, Ausgabe des LowLevel Magazins. Und das unter einen neuen Leitung, denn Mastermesh, der hochverehrte Schöpfer dieses Magazins und natürlich auch des dazugehörigen Forums, kann/will nicht mehr. Also bin ich (Roshl) ab sofort an allem Schuld was hier so steht oder nicht steht. Also schlagt mich in Zukunft wenn hier irgendwelcher Blödsinn steht.

Damit ihr auch wisst wer ich bin werde ich mich kurz vorstellen. Ich bins also der/die/das Roshl, hin und wieder auch Roschü oder ähnliche Namensverhunzungen. Ich bin 18 Jahre alt und geh auf ein Gymnasium in die 13 Klasse, also demnächst steht mein Abitur ins Haus (na klasse). Wie ich zum Programmieren gekommen wüsste ich selbst mal ganz gern. Angefangen hab ich dann mit C/C++. Zum Lowlevel kam ich eigentlich dadurch, dass ich wissen wollte wie Betriebsysteme eigentlich funzeln. Auf der Suche danach bin ich irgendwann hier gelandet. Hab mich etwas mit Assembly beschäftigt und wurde ein paar Tage später zum Guru aller Programmierer, naja oder so ähnlich...

Viel Spass mit der 6. Ausgabe

## Partitionstabellen

Da vor einiger Zeit im Forum die Frage auftauchte wie Partitionstabellen aufgebaut sind, hab ich mal beschlossen das nochmal hier zusammenzufassen, da es ziemlich nützlich sein kann. Also etwas gleich vorweg, Partitionstabellen sind nicht wirklich festgelegt, das heist keiner ist gezwungen diese auch so anzulegen wie ich es gleich beschreiben werde. Das kann zu Problemen führen wenn ein OS versucht die Tabelle zu lesen die aber in einem anderen Format steht, vielleicht bringt Microsoft sowas irgendwann mal fertig, zu zutrauen wäre es allemal.

Ok was ist nun der Sinn von Partitionstabellen? Partitionstabellen dienen dazu festzulegen welche Partitionen auf dem Datenträger vorhanden sind. Es werden Dinge gespeichert wie der Anfangspunkt, Endpunkt, die Länge, oder der Typ der Partition. Ein OS liest diese Informationen ein und weiss dann, dass es entweder nicht weiss wie es die Partition behandeln soll, weil das Dateisystem unbekannt ist, oder weiss dann wo es nachschauen muss um an weitere Informationen zu kommen, wie zum Beispiel der Lage der FAT oder anderen Dingen. Gut der Sinn ist jetzt klar aber wo ist diese ominöse Tabelle und wie ist sie aufgebaut? Im Allgemeinen liegt die Partitiontabelle im ersten Sektor des jeweiligen Datenträgers. Sinnvollerweise weil der am einfachsten zu finden ist. Und innerhalb dieses Sektor haben wir: 446 Byte die wir für den Bootloader oder sonstwas verwenden können, 64 Byte für die Partitionstabelle und 2 Byte für die Bootkennung. Die 64 Byte der Tabelle zerlegen wir in 4 gleich grosse Teile, so dass wir 4 Partitionen da reinpacken können. Die 4 Einträge sind jeweils gleich aufgebaut, ich werde also nur einen erklären;-) Ein Einträg ist 16 Byte lang. Fangen wir am besten beim ersten Byte an. Ganz am Anfang steht das Active Partition Flag, dieses sagt uns ob die Partition aktiv ist. Ist sie das, dann muss dort 80h hin, wenn nicht dann sollte 0 dort stehen. Darauf folgen 3 Byte im Zusammenhang. Diese Beschreiben den Anfang der Partition im CHS Format, also so wie es im INT 13h auch verwenden wird, ein Byte für den Kopf, einen für den Sektor und einen für den Track/Cylinder. Dann folgt ein Byte das für die Typkennung zuständig ist, damit wir auch wissen um was für ein Dateisystem es sich handelt, zum Beispiel, 01h wenn es ein DOS 12-BIT FAT System ist. Dann wieder 3 Byte im CHS Format, diesmal allerdings für den Endpunkt der Partition. Danach haben wir 4 Byte in denen steht wieviele Sektoren vor der Partition stehen, also im LBA Format. Dann 4 Byte die die Anzahl an Sektoren angibt welche in der Partition liegen. Das Ganze noch als kleine Tabelle:

|  |  |  |
| ----------------------- | --------- | ------------------------------------------ |
| Name | Länge | Bedeutung |
| Active Partition Flag | 1 Byte | Gibt an ob die Partition aktiv ist |
| CHS Start | 3 Byte | Anfangspunkt der Partition im CHS-Format |
| Typ | 1 Byte | Kennzeichnet den Partitionstyp |
| CHS Ende | 3 Byte | Endpunkt der Partition im CHS-Format |
| LBA Start | 1 DWord | Anzahl an Sektoren VOR(!) der Partition |
| LBA Länge | 1 DWord | Anzahl an Sektoren IN der Partition |

Das wars dann auch schon, ich hoffe ihr konnten mir folgen und seid nicht eingeschlafen.

**Roshl**

## Interview mit Mike Hibbet

**First of all, please introduce yourself (where do you live, Age, job, family, hobbies, ...)**

I live in the south-east of England with my partner and our two young children. I\`m 39, and currently working as an embedded software engineer for a telecommunications equipment manufacturer. With a young family at home my spare time is limited, and most of it goes into Menuet. Rock climbing sometimes occurs when I can find the time!

**When and how did you start to code?**

I started coding at the age of 14 when I bought my first computer, an Acorn System 1 (<http://www.cary.demon.co.uk/acorn/> ). I still own it. It was programmed in assembly, and the challenges and fun I had getting the thing to do anything useful remains with me to this day, and are the reasons why I still enjoy the challenge of programming at the low level.

**Which languages do you know and why did you learn them, and which one do you like best and why?**

6502 Assembly was the first language I learnt for programming the Acorn system 1. I then moved onto Cobol, simply because that was the only book on programming in the Library. I started to use BASIC on the TRS80, but I didn\`t like it; To abstract from the hardware, and too slow. That feeling still dominates my view of BASIC and I have never really done any serious coding in it. My first real experience of a high level language was Pascal which I learnt at university along with Fortran. I never really liked either, even though I programmed in Pascal for several years during the 80\`s. But then I found \`C\`, and never looked back. I view C as a decent assembler rather than a high level language. It gave me the opportunity to visualise my designs more quickly than with assembly, but still allowed me direct access to the underlying hardware, and an easy interface to assembly when I wanted it. Even so, I often find myself looking at the assembly output of a compiler to check it isn\`t making mistakes! I think I have to say that assembly and C are my joint favorites; I need both. I love expressing design concepts in \`C\`, but I love the challenge of assembly.

**How did you learned about OS developing and, beside of MenuetOS, have you ever created or contributed to any other OS?**

Menuet is in fact the first \`proper\` OS I have ever coded on; Up until last year (and that is over 25 years of coding,) I have relied on a basic \`main loop\` and interrupt processing to get the job done. And that is in a wide range of products; Telephones, pagers, robots, electricity meters and telecoms equipment.

**How and when did you find MenuetOS?**

I forget now how I first came across it. It was about 3 years ago, and I suspect what may have attracted me was that it had no TCP/IP support. I\`d just written a TCP/IP stack in \`C\` and had always been interested in networking, so I thought I would give it a go. And it\`s small size attracted me. Even though I played with Linux back in 1993 I still found Linux too large to get to grips with. I like to fully understand the enviroment that I am working in.

**What made you decide to code stuff for MenuetOS, and what one have you already coded?**

I guess I have already answered that; It was Menuets lack of networking that pushed me to create a simple stack. I started off with IP, UDP and SLIP, then moved on to TCP, Ethernet, and a host of network applications. My favorite network application is an IRC client written by Ville, and it\`s only 8KB of code.

**After four successful years MenuetOS got a new leader/operator: You. Why did Ville Turjanmaa (the founder) choose you?**

I dont really know, I never asked him. Ville and I have always worked well together, I understand what his views are for Menuet, and I respect them. And I think realises that; Perhaps he trusts me to keep to the original ideals for Menuet; A small, assembly language OS. When he asked me to take over I was both delighted and sad; Delighted that I would be able to contribute more to the direction of Menuet, but sad because I have enjoyed working with Ville, sharing his ideals.

**The main aim of MenuetOS seems to be fitting on one 1"44 Disk. In future, if the whole applications and sources are to big for one disk, what will you do?**

I dont believe fitting on a floppy is an aim of Menuet, it certainly isn\`t one of my aims. But it is a question of size; Menuet is a small OS, and it isn\`t going to outgrow the size of a floppy soon! We already have many megabytes of applications, and Jarek Pelczar has done some great work on C libraries that increase that significantly! I am keen to keep the main distribution small since that fits in with the general philosophy of the project, but at the same time I want to encourage people to build on top of Menuet as they see fit. The OS is after all just a part of a complete working system. I hope to improve on the harddisk installation procedures soon. This will mean a second \`official\` distribution along side the main floppy version, but the \`floppy\` version will always be the primary release.

**What is the target group of MenuetOS, who uses it?**

The target group is clear from the banner on the web site: "The Assembly Language Programmers OS" And there do seem to be quite a hardcore group of highly technical programmers, mainly in Europe. Recent media coverage in the USA has increased our user base, and we now seem to have a number of different interest groups. We are moving into the phase of "users verses developers" which is quite an interesting juggling act.

**What is more important for you: Bigger target group (more user-friendly) or more technically applications?**

Neither. What is important to me is moving Menuet forward to the stage where it is a real contender for my desktop. I\`m currently writing this article at home under Windows; I\`d rather be using Menuet. It\`s going to be an interesting journey, and it\`s one that I hope the Menuet community can make together without fragmenting, or loosing interest. Part of that journey will involve more user-friendliness, part of it technical improvements such as font support, web browser, etc.

**Now let\`s talk about Menuet\`s future: What will be (do you hope) in near future (let\`s say: 6 month - 2 years)?**

Near term, getting harddisk boot support, font handling and a web browser. All of these are in progress, but progress is slow. There are smaller goals along the road, but those are the things I think of before falling asleep at night!

**And what do you think about the far-away future (5-10 years)?**

Ah, the vision thing. I never look more than 5 years hence, it\`s just too far. But in 5 years I hope that Menuet will be my main OS at home; What that means in terms of development is hard to say, ask me again in one year!

**Which advise would you give new OS developers? How to start? Which tutorials to read?**

The best tutorial I have found is Andy Tanenbaums book on OS design (Operating Systems: Design and Implementation.) Although the book describes a micro kernel (which I dont like,) I loved the principles, and it is a great read. The problem with good books though is that they can stop you from engaging in the best activity for learning how to code an OS: Coding. And the reason? Because coding is hard, and sometimes you have to throw away months of work. What worked for me was finding a project with a vital part missing, and setting down to provide that part. Thats how I got involved; I loved networking, and Menuet was without a network stack. I have learned much more about OS\`s and TCP/IP than I would from just reading books. Of course the web is a great source for tutorials these days, and there are plenty of individuals and institutions who have published well documented examples on the web.

**Thanks a lot for the interview! I hope the questions weren\`t too stupid :)!**

They weren\`t stupid, they made me step back and think, and it\`s important to do that from time to time! Thanks for the interest.

Regards, Mike.

Der Dank für dieses Interview gebührt SPTH, der die Fragen gestellt und dann freundlicherweise zur Verfügung gestellt hat. Also big thx to Mike for giving this Interview, just in case he ever reads this!

## MenuetOS - Der Weg zum Erfolg mit Assembler

### Einleitung

MeunetOS ist ein 32bit Betriebssystem, das ausschließlich in x86 Assembler geschrieben wurde. Es ist total Open Source, gratis und passt auf eine 1.44MB Diskette. MenuetOS hat eine GUI (Graphical User Interface - Grafische Benutzeroberfläche), jede Menge nützliche Netzwerktools wie einen eMail-Client, einen IRC-Client, einen Web-Browser, einen Netzwerk-Schach-Client, einige Spiele wie Get4 (4 Gewinnt), einen JPG- und BMP-Viewer, einen integrierten Compiler, einige Demo-Programme und vieles, vieles mehr. MenuetOS hat keine Windows oder Unix Wurzeln, und arbeitet mit Multi-Tasking. Das Projekt wurde 2000 von Ville Mikael Turjanmaa gestartet, und seit Sommer 2004 von Mike Hibbett geleitet. Die offizielle Seite von MenuetOS ist www.menuetos.org. Derzeit, Sebtember 2004, ist es in version 0.77 bzw. 0.78 pre3 erhältlich. Als ich dieses Betriebssystem fand, war ich sofort bezaubert von der Idee, und musste mehr darüber herausfinden. In diesem Artikel möchte ich dieses Betriebssystem näher erklären, sowie erklären, wie man selbst Programme dafür schreibt.

### Der Einstieg - Generelle Informationen

Nachdem man sich MenuetOS gratis heruntergeladen hat, und auf eine Diskette installiert hat, kann man von der Diskette booten. Wenn man das macht, erscheinen zuerst 4 Fragen, welche zum Beispiel die Einstellung der Bildschirmauflösung und des Boot-Typs festlegen. Hat man diese Fragen beantwortet, läd der Kernel das OS in den Speicher, erstellt den Interrupt-Table, läd Maus und Tastatur, und schließtlich, nach einem ESC-Druck, wird der Launcher geladen, der den Desktop, die Taskleiste sowie die Icons generiert. MenuetOS wird in den RAM geladen, wie bereits erwähnt wurde. Die Daten im RAM sind mit dem Adresspfad \`/RAMDISK/1/\*\` erreichbar. Die Daten der primäre Festplatte kann man mit dem Pfad \`/HARDDISK/1/\*\` erreichen.

### Programmaufbau

Menuets ausführbare haben keine Dateiendung wie zum Beispiel DOS (\*.com), Windows (\*.exe) oder Linux (\*.elf) Dateien. MenuetOS benuetzt zwar Dateiendungen, aber nur für Bilder, Homepage-Dateien oder Textdateien. Eine ausführbare Datei besteht aus 2 Teilen, dem Head und dem Code:

       Header
       Executable Code

Viele Programme Speichern nach dem Header ihre Daten, um sie im Code nicht überspringen zu müssen. Das Program wird im Speicher an die Adresse 0x0 (org 0x0) geladen, im Gegensatz zu DOS, welches Dateien aud der Adresse 0x100 läd.

### Der Header

Der Header der ausführbaren Menuet-Dateien beinhaltet wichtige Informationen, welche das OS zum Laden der Datei braucht. Hier ist der Aufbau des Headers:

|  |  |  |
| -------- | --------- | ---------------------- |
| Offset | Länge | Name |
| 00h | 8 Bytes | Datei ID |
| 08h | 4 Bytes | benötigte OS-Version |
| 0Ch | 4 Bytes | Entry Point |
| 10h | 4 Bytes | Dateilänge |
| 14h | 4 Bytes | Benötigter Speicher |
| 18h | 4 Bytes | Extra Header/Stack |
| 1Ch | 4 Bytes | Parameters |
| 20h | 4 Bytes | Icon Information |

**Datei ID** Die ID gibt an, dass es sich um eine ausführbare Menuet Datei handelt. Es gibt hier entweder den Wert \`MENUET00\` oder \`MENUET01\`. Ich habe keinerlei Unterschied zwischen diesen zwei Werten gefunden.

**Benötigte OS-Version** Da Menuet immer weiterentwickelt wird, werden auch immer wieder neue System Calls (mehr dazu später) hinzugefügt. Wenn ein Programm einen System Call von zB Menuet 0.77 benützt, ist dieser Wert \`77\`, und eine mögliche ältere Version führt das Programm nicht aus, um Fehler zu vermeiden. Am besten ist hier der Wert des neusten OS, da normalerweise jeder die neuste Version verwendet.

**Entry Point** Der Entry Point ist die Adresse des Codeanfangs. Wenn kein Extra Head verwendet wird, und keine Daten nach dem Code gespeichert sind, ist dieser Wert \[0x1C\]. Am einfachsten sollte hier ein Label vor dem Code benutzt werden, und der Compiler rechnet sich die Adresse selbst aus.

**Dateilänge** Dieser Wert ist Header+Code+Daten. Einfach ein Label nach dem gesamten Code verwenden, und der Compiler rechnet die Länge selbst aus.

**Benötigter Speicher** Hier reservieren Anwendungen den benötigten Speicher. Da Menuet mindestens 128MB RAM benutzt, ist der Wert hier meistens sehr hoch (viel höher als wirklich benützt). In den meisten Anwendungen ist dieser Wert \[0x100000\]. Extra Header / Stack: Dieser Teil des Headers enthält einen von zwei Werten: Entweder die Adresse des Stacks, wenn ein Extra Header verwendet wird. Der Stack befindet sich auf Adresse \[0x7FFF0\]. Anderenfalls, wenn kein Extra Header verwendet wird, ist dieser Wert \[0x0\]. Parameters / Icon Information: In den meisten Fällen sind beide werde \[0x0\]. Diese Werte sind Extra Parameter für das Programm sowie die Information für das zu verwendende Icon.

### Ein typisches Programm

Die allermeisten Programme für MenuetOS benützen das gleiche, ganz einfache Schema. Die folgende Grafik, erstellt von Ville Mikael Turjanmaa, zeigt diesen Aufbau:

       Header Data
       Start:
       call draw_window
       Wait until event
       Read event type
       -> redraw -> call draw_window ->
       -> key -> read keypress -> process ->
       -> button -> read buttonpress -> process ->
       draw_window:
       Draw static window parts
       ret
       Data area
       Static data

Man kann genau erkennen, wie das Programm funktioniert. Zuerst wird das Fenster erstellt, dann wird auf eine Aktion (Tastendruck, Mausklick auf Button, Fenster Veränderung) gewartet. Wenn ein Tastendruck oder ein Klick auf einen Button erfolgt, wird ein bestimmter Teil des Codes aufgerufen.

### System Calls

Mit System Calls ruft man in MenuetOS APIs auf, das heißt, Funktionen wie \`WAIT FOR EVENT\` oder \`SYSTEM TREE ACCESS\`. In DOS ruft man Funktionen meistens mit INT 0x21 auf, und in Windows direkt mit CALL. In Menuet funktioniert das folgendermaßen: \<asm\>

       mov eax, FUNKTIONSNUMMER
       ebx, ecx, edx, esi, edi, ebp = Parameters
       INT 0x40 - SYSTEM CALL

\</asm\>

Die Funktionen, die bis jetzt 68 an der Zahl sind, findet man in der Datei SYSFUNCS.TXT. Ein Beispiel - SYSFUNCS.TXT enthält folgende Informationen:

       05 = DELAY X/100 SECS
       
           ebx delay in 1/100 secs
           ret: nothing changed

Wenn wir jetzt in unserem Programm eine 0.5 Sekunden lange Wartezeit wollen, müssen wir es folgendermaßen benützen: \<asm\>

       mov  eax, 5             ; Function number: DELAY X/100 SECS
       mov  ebx, 50          ; 50/100 sek = 0.5 Sekunden
       int  0x40             ; System call

\</asm\>

Wir setzen die Funktionsnummer (die hier 5 ist) in eax, setzten ebx die gewünschten ?\*0.01 Sekunden und rufen die Funktion auf - ganz einfach.

### Hello World

Es ist schon zur Tradition geworden, im ersten Programm ein \`Hello World\` ausgeben zu lassen, darum das auch hier: Unser Ziel: Ein Programm, das \`Hello World\` ausgibt, und hier ist der Code, und jede Zeile wird genau erklärt. \<asm\>

       use32                        ; Sagt FASM (unserem Assembler), 
                                    ; dass wir 32bit Code generieren wollen
       
       org 0x0                      ; Die Anwendung wird auf diese Adresse geladen
       db 'MENUET01'                ; Datei ID
       dd 0x01                      ; benötigte OS-Version
       dd START                     ; Entry Point
       dd I_END                     ; Dateilänge
       dd 0x100000                  ; Benötigter Speicher 
                                    ; (natürlich sehr übertrieben, 
                                    ; aber wen stört `s?)
       dd 0x0                       ; Kein Extra Header
       
       START:                       ; Unser Entry-Point: Hier fängt der Code an
       call draw_window             ; Ruft die interne Funktion draw_window` auf
                                    ; draw_windows ist ganz am
                                    ; Ende des Codes zu finden.
       
       still:                       ; Hier ist unser Main-Loop-Start-Label. 
                                    ; Wenn kein Aktion passiert, dann
                                    ; wird das Programm immer und immer 
                                    ; wieder hier ausgeführt.
       
       mov eax, 10                  ; System Call 10 = WAIT FOR EVENT
                                    ; Der zurückgegebene Wert befindet sich,
                                    ; nach INT 0x40, in eax
       int 0x40                     ; SYSTEM CALL ausführen
       cmp eax, 1                   ; eax enthält jetzt den zurückgegebenen Wert
                                    ; von `WAIT FOR EVENT`.
       je red                       ; Wenn eax=1 (das Fenster wurde
                                    ; verschoben/seine Größe wurde verändert)
                                    ; dann springt das Programm zum Label `red`.
       
       cmp eax, 2                   ; eax wird mit 2 Verglichen
       je key                       ; Wenn eax=2 (eine Taste wurde gedrückt), 
                                    ; dann springt das Programm zum
                                    ; Label `key`.
       
       cmp eax, 3                   ; eax wird mit 3 verglichen
       je button                    ; Wenn eax=3 (ein Button wurde mit 
                                    ; der Maus gedrückt), dann springt das
                                    ; Programm zum Label `button`.
       
       jmp still                    ; Wenn nichts passiert ist, 
                                    ; dann wird der Haupt-Loop wiederholt.
       
       red:                         ; Label, falls das Fenster wurde
                                    ; verschoben/seine Größe wurde verändert
       call draw_window             ; Das Fenster wird neu generiert,
                                    ; um es an die neue Größe oder den neuen
                                    ; Ort anzupassen.
       jmp still                    ; Danach wird im Haupt-Loop wieder fortgefahren.
       
       key:                         ; Label, falls eine Taste gedrückt wurde
       mov eax, 2                   ; System Call 2: Get Key
                                    ; Zurückgegebene Werte:
                                    ; al=0: Erfolgreich | al=1: Kein Tastendruck
                                    ; gespeichert. ah=Wert der Taste (zB: RETURN=13)
       int 0x40                     ; SYSTEM CALL ausführen
       jmp still                    ; Danach wird im Haupt-Loop wieder fortgefahren.
       
       button:                      ; Label, falls ein Button mit 
                                    ; der Maus gedrückt wurde
       mov eax, 17                  ; System Call 17: GET PRESSED BUTTON ID
                                    ; Jeder Button, der generiert wird,
                                    ; bekommt eine ID.
                                    ; Die ID-Nummer wird bei dieser 
                                    ; Funktion in ah zurückgegeben.
       int 0x40                     ; SYSTEM CALL ausführen
       
       cmp ah, 1                    ; ah (Button ID) wird mit 1 verglichen
       
       jne noclose                  ; Wenn Button ID!=1 (der EXIT Button, 
                                    ; der bei `draw_window` generiert
                                    ; wird), springt das Programm zu `no_close`.
       
       mov eax, -1                  ; System Call -1: END APPLICATION
                                    ; Beendet das Programm, 
                                    ; keine Weiteren Informationen werden benötigt
                                    ; oder zurückgegeben.
       int 0x40                     ; SYSTEM CALL ausführen
       
       noclose:                     ; Label, Button ID!=1
       
       jmp  still                   ; Danach wird im Haupt-Loop wieder fortgefahren.
       
       
             ;   *********************************************
             ;   *******       FENSTER GENERIEREN     ********
             ;   *********************************************
       
       draw_window:                        ; Label für das Generieren vom Fenster
       mov eax, 12                         ; System Call 12: WINDOW REDRAW STATUS
                                           ; Teilt dem OS mit,
                                           ; dass jetzt ein Fenstergeneriert wird
       mov ebx, 1                          ; ebx=1: Start des Fenster Generierens
       int 0x40                            ; SYSTEM CALL ausführen
       
       mov eax, 0                          ; System Call 0: DEFINE AND DRAW WINDOW
                                           ; Hier wird das Fenster generiert
       mov ebx, 100*65536+300              ; [x start] *65536 + [x size]
       mov ecx, 100*65536+120              ; [y start] *65536 + [y size]
       mov edx, 0x02ffffff                 ; Hauptfarbe
       mov esi, 0x805080d0                 ; Nebenfarbe
       mov edi, 0x005080d0                 ; Framefarbe
       int 0x40                            ; SYSTEM CALL ausführen
       
       
       mov eax, 4                          ; System Call 4: WRITE TEXT TO WINDOW
                                           ; Hier wird der Kopf 
                                           ; des Fensters beschrieben
       mov ebx, 8*65536+8                  ; [x start] *65536 + [y start]
       mov ecx, 0x10ddeeff                 ; Farbe
       mov edx, labelt                     ; Adresse des Textes
       mov esi, labellen-labelt            ; Textlänge
       int 0x40                            ; SYSTEM CALL ausführen
       
       
       mov eax, 8                          ; System Call 8: DEFINE BUTTON
                                           ; Hier wird der Button 
                                           ; zum Schließen des Programms erstellt
       mov ebx, (300-19)*65536+12          ; [x start] *65536 + [x size]
       mov ecx, 5*65536+12                 ; [y start] *65536 + [y size]
       mov edx, 1                          ; Button ID
       mov esi, 0x6688dd                   ; Button Farbe
       int 0x40                            ; SYSTEM CALL ausführen
       
       mov eax, 4                          ; System Call 4: WRITE TEXT TO WINDOW
                                           ; Wir schreiben jetzt unser 
                                           ; 'Hello World!'
       mov ebx, 20*65536+35                ; [x start] *65536 + [y start]
       mov ecx, 0x224466                   ; Farbe
       mov edx, text                       ; Adresse des Textes
       mov esi, labelt-text                ; Textlänge
       int 0x40                            ; SYSTEM CALL ausführen
       
       mov eax, 12                         ; System Call 12: WINDOW REDRAW STATUS
       mov ebx, 2                          ; ebx=2: Wir sagen dem OS, 
                                           ; dass wir fertig gezeichnet haben
       int 0x40                            ; SYSTEM CALL ausführen
       
       ret                                 ; Zurück, woher wir auch immer 
                                           ; gekommen sind
       
                               ; DATEN
       
       text db 'Hello World!'              ; Unser Hello World
       
       labelt:
       db 'Mein erstes MenuetOS Programm'  ; Die Information 
                                           ; im Kopf des Fensters
       labellen:
       I_END:                              ; Das ENDE-Label

\</asm\>

### Nachwort / Quellenangabe

Dieser Artikel ist eine Informationssammlung über MenuetOS, einem sehr interessanten Betriebssystem. Ich danke jedem Leser, dass er sich Zeit genommen hat, um diesen Text zu lesen, und für das Interesse an MenuetOS oder an der Assembler-Sprache. Ich hoffe, ich habe niemanden gelangweilt. :) Jetzt wünsche ich noch jedem viel Spaß mit MenuetOS!

Quellenangabe:

- Turjanmaa, Ville: MENUET 0.78 Pre1 SYSTEM CALLS FOR APPLICATIONS. Helsinki, 2004.
- Turjanmaa, Ville: MenuetOS (0.75). Kernel and process management. Helsinki, 2003.
- Turjanmaa, Ville: EXAMPLE APPLICATION. Helsinki, 2003.

**SPTH**

## Programmerfish\`s Kolumne

Ich gehe momentan in die 8. Klasse auf eine staatliche Realschule und gehöre zu einer Gruppe von "Versuchskaninchen" die das Glück hatten als erste die R6, die 6-Stufige Realschule zu besuchen. Bei der R6 kommt man schon nach der 4. Klasse auf die Realschule, statt sonst erst nach der Sechsten. Das hat durchaus gewisse Vorteile, zum Beispiel kriegen wir jedes Jahr neue Bücher, weil der Lehrplan ganz anders ist, was aber auch Nachteile mit sich bringt, die neuen Bücher müssen natürlich auch eingebunden werden. Aber jetzt zurück zum eigentlichen Thema: Irgend so ein Bleistiftspitzer aus dem Kultusministerium Bayern hat beschlossen die Fächer Textverarbeitung, Informatik und TZ (Technisch Zeichnen) zu einen Fach, IT (Informationstechnologie) zusammenzulegen. Das Ergebnis dieses Beschlusses ist, das wir nun eine "ausgebildete IT-Fachlehrkraft" in Form einer älteren Dame die trotz ihrer fachlichen Ausbildung nicht zu wissen scheint das man MS-Word Dokumente auch als Vorlagen abspeichern kann ("Und jetzt dürft Ihr nicht auf Symbol Diskette gehen, sonst macht Ihr eure Maske kaputt!"), obendrein langsamer tippt als ich ("Man kann den Computer so einstellen das er 'Mfg' automatisch durch 'Mit freundlichen Grüßen' ersetzt, aber wenn man so schnell schreiben kann wie ich braucht man das nicht.") und scheinbar nicht weiß dass es neben Windows auch noch andere Betriebssysteme gibt. In der 7. Klasse haben wir dafür das krasse Gegenteil dieser älteren Dame gehabt: Eine Lehrerin, die was von ihrem Job versteht. Im Grunde haben wir zwar nur schreiben gelernt und am Schluss des Schuljahres noch die Bedienung des Internet Explorers gelernt (Was 29 von 30 Schülern eh schon können). Letzteres war also praktisch umsonst. Zurück zur 8. Klasse: Wie bereits erwähnt besteht IT aus Textverarbeitung, Informatik und TZ. TZ haben wir dieses Jahr noch als eigenes Fach, nächstes Jahr brauchen wir also einen Lehrer der diese drei Fächer unterrichten kann. Der einzige der das kann ist unser momentaner TZ-Lehrer der zum Glück genauso wie unsere Ex-IT-Lehrerin was von seinem Job versteht, es kann also nur noch besser werden. Ein weiterer Nachteil dieser Kombination: Auf der R4 konnte man sich nach der 8. aussuchen ob man Informatik oder TZ weitermacht. Und bei IT wird beides weiter gemacht. Ergebnis davon ist also das man von beidem etwas, aber von keinem wirklich genug lernt. (Da man ja auch weniger Unterrichtszeit hat.). Ein Freund von mir, der auf die letzte R4 Jahrgansstufe (Momentan 9. Klasse Informatik) geht hat in der 8. Klasse Programmieren mit VB (Nicht das ich das nötig hätte), Flussdiagramme und andere Sachen dieser Sorte gelernt. Und das fällt bei uns komplett flach. Dafür dürfen wir Texte in verschiedenen Schriftgrößen und -farben formatieren, da die ausgebildete Fachlehrkraft nicht glaubt das wir das schon können.

Nachtrag: Alles wird gut! Mittlerweile bin ich doch schon in der neunten Klasse und hab neben dem alten TZ-Lehrer noch einen neuen IT-Lehrer die sich den Stoff teilen. Und es wird besser! Flussdiagramme und Theorie zur Programmierung, ein Projekt (Eine Homepage. Mit Mozilla Composer), Netzwerke und noch ein recht großer Teil TZ. Letzteres und Netzwerke übernimmt dann der alte TZ Lehrer. Die erste Stunde haben also 15 IT beim neuen Lehrer während die anderen 14 (Wir sind 29) IT beim alten TZ-Lehrer haben. In der 2. Stunde wird getauscht.

**The Programmerfish**

## Nachwort

So alles in allem ist die Ausgabe leider nicht die Umfangreichste geworden, aber ich hoffe dennoch, dass es zur Zufriedenheit der Mehrheit ist. Ich bin Hoffnungsvoll, dass mich für die nächste Ausgabe mehr Material erreichen wird, bzw das ich selbst etwas mehr schreiben kann.

Leider ist so gut wie nichts an Programmierpraktischen Beispielen in der Ausgabe dabei, dafür ist ein regelrechtes MenuetOS Spezial daraus geworden (aktuellste Version davon derzeit ist die 0.78 pre3). Das konnte vielleicht ein paar Designanregungen für das eigene Projekt geben.

Dies war sie also, die erste Ausgabe unter neuer Leitung. Anregungen, Beschwerden, Loblieder, Morddrohungen, neue Artikel zur nächsten Ausgabe und ähnliches bitte an mich -\> Roshl.

**Roshl**

|  |  |  |
| ------------------------------------------------------------------------------- | ---------------- | ------------------------------------------------------------------------------- |
| « [Ausgabe 5](Ausgabe-5 "Ausgabe 5") | **Navigation** | [Ausgabe 7](Ausgabe-7 "Ausgabe 7") » |

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/6645/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1471/index.html)

<!-- MediaWiki page 1471; revision 6645; parent 6301; 2009-12-28T01:22:37Z -->
