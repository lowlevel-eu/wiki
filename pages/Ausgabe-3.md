# Ausgabe 3

|  |  |
| ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| © | Dieser Artikel ist urheberrechtlich geschützt.<br>Bitte beachte, dass die üblichen [Lizenzbestimmungen](https://lowlevel-eu.github.io/wiki/pages/1637/index.html "Lowlevel:Urheberrecht") des Wikis für diesen Artikel nicht gelten. |

  

|  |  |  |
| ------------------------------------------------------------------------------- | ---------------- | ------------------------------------------------------------------------------- |
| « [Ausgabe 2](Ausgabe-2 "Ausgabe 2") | **Navigation** | [Ausgabe 4](Ausgabe-4 "Ausgabe 4") » |

## Vorwort

Nun, das ist also die dritte Ausgabe von Lowlevel. In den letzten Wochen habt ihr wenig von mir gehört, ganz einfach aus dem Grund, dass ich im Urlaub war und deshalb keine Zeit hatte, an Lowlevel zu arbeiten.

Aber egal, jetzt bin ich wieder da, mit neuen Ideen und neuem Material für Lowlevel. Allerdings fürchte ich, dass die nächsten Ausgaben nicht ganz so umfangreich sein werden, wie die ersten zwei. Ich werde in den nächsten Monaten viel zu tun haben, und außerdem arbeite ich noch an einem Spieleprojekt...

Na ja, auf jeden Fall wünsche ich viel Spaß mit Ausgabe 3.

## News

PiranhOS wird von Grund auf neu gecodet. Grund: "messy code" (Originalzitat)

Das interne Betatesting zu EngesnOS ist fertig. In den nächsten Tagen können wir mit einer Public Beta rechnen

Ende August soll die nächste Beta des Windows NT-Clones [ReactOS](ReactOS "ReactOS") erscheinen.

In Frankreich kann man nun bei Dell PCs bestellen, auf denen [FreeDOS](FreeDOS "FreeDOS") installiert ist. Toll, oder?

## Leserbriefe

**Hi, eine tolle Idee, ein Deutsches Online Magazin für Betriebssystem- Entwicklung. Die ersten beiden Ausgaben sind sehr interessant, ich bin schon gespannt auf die folgenden!** **So, jetzt zu meiner Kritik: überall gibt es Webseiten, die zeigen, wie man Kernel in Assembler schreibt ... mich würde C mehr interessieren.**

**Jetzt noch ein paar Anregungen für die nächste oder übernächste Ausgabe ;-) Ich würde gerne mehr über die Technischen Details der Diskette erfahren und besonders über den Aufbau und wie man dort ein Betriebssystem unterbringt.**

**Hey, wie wäre es, wenn die Webseite mehr ausgebaut wird? Zum Beispiel Links, und sowas? Naja, alles hier nur Anregungen ... weitermachen!**

Vielen Dank fürs Lob. Wegen C... hier in der 3. Ausgabe habe ich einen Aufruf gemacht. Die Leute sollen mir sagen, ob ich mich eher auf C oder auf Assembler konzentrieren soll.

Diskette... schon gemacht, siehe "Lowlevel Grundlagen".

Das mit der Website - da hab ich schon was vor. Zusätzlich zu den Ausgaben wird dort es dort ein "Resource Center" geben, wo alle Infos und Sources gesammelt werden. Und natürlich auch mit Links und so.

## OS Dev-Tutorial, Teil 3

### Designüberlegungen

Nachdem wir also letztes Mal gelernt haben, wie Interrupts funktionieren, werden wir uns dieses Mal anschauen, wie man einen eigene ISR (Interrupt Service Routine) schreibt. Wir werden also eine rudimentäre API schreiben, die verschiedene Funktionen bereitstellt. Sowohl dem Kernel - als auch den User-Programmen.

Als erstes müssen wir uns einige Sachen überlegen.

1.  Welchen Interrupt benutzen wir?
2.  Wie viele Funktionen werden wir pro Interrupt haben?
3.  Welches Register wird für die Funktionsnummer benutzt?
4.  Was werden die Funktionen machen?

Ich schlage vor, wir benutzen Interrupt 0x21. DOS benutzt für die meisten Calls 0x21 und auch wir werden es so machen. Zur Übergabe der Funktionsnummer benutzen wir AL (anders als in DOS). Da ein 8 Bit-Register bekanntlich Zahlen von 0 bis 255 enthalten kann, können wir theorethisch 255 Funktionen pro Interrupt haben.

### Unser erster Interrupt

Unsere erste Routine - 0x01 von Interrupt 0x21 - wird ein Ersatz für die putstr-Funktion sein. Unsere Routine wird also den String nehmen, auf den SI zeigt und ihn über BIOS Teletype auf den Bildschirm schreiben (String muss Null-terminiert sein!).

\<asm\> \_int0x21:

        _int0x21_ser0x01:       ; funktion 0x01
        cmp al, 0x01            ; funktion 0x01 angefragt?
        jne _int0x21_end        ; nächste Routine checken
        
        _int0x21_ser0x01_start:
        lodsb                   ; nächstes Byte laden
        or  al, al              ; 0-Byte?
        jz  _int0x21_ser0x01_end
        mov ah, 0x0E            ; BIOS Teletype
        mov bh, 0x00            ; Page 0
        mov bl, 0x07            ; Text-Attribute
        int 0x10                ; BIOS-Call
        jmp _int0x21_ser0x01_start
        _int0x21_ser0x01_end:
        jmp _int0x21_end
        
        _int0x21_end:
        iret</asm>

Jetzt gehen wir den Code Stück für Stück durch. Jede Funktion hat ein Label in der Form "\_int0x21_ser0x01". Der erste Teil ist die Interrupt-Nummer, der Zweite die Funkionsnummer. Zu beginn jeder Funktion wird geprüft, ob in AL die Nummer der Funktion drinsteht. Wenn ja, geht der Code normal weiter und die Routine wird ausgeführt. Wenn nicht, wird zur nächsten Funktion gesprungen. In diesem Beispiel haben wir nur eine Routine, deshalb wäre dann die ISR gleich zu Ende.

Nun haben wir also unseren Interrupt Handler. Dieser ist aber noch nicht in der Interrupt Vector Table registriert. Bevor wir den Interrupt aufrufen, müssen wir also ein paar Pointer umbiegen, damit der PC auch unseren Interrupt Handler benutzt.

\<asm\> push dx

       push es
       xor ax, ax
       mov es, ax
       cli
       mov word [es:0x21*4], _int0x21  ; Pointer auf den Handler
       mov [es:0x21*4+2], cs           ; Pointer auf CS
       sti
       pop es
       pop dx</asm>

Als erstes speichern wir DX und ES. Danach leeren wir das AX-Register und schreiben den Wert von AX in ES rein (keine Panik, das ist die schnellste Möglichkeit!). Als nächstes schalten wir Interrupts aus, da wir ja selbst mit Interrupts arbeiten.

Danach wird die Einsprungadresse von unserem Interrupt nach ES:0x21\*4 geschrieben. Zum Schluss schreiben wir noch den CS-Wert in die nächsten zwei Bytes rein, damit der Prozessor weiß, wo das Segment des Interrupt Handlers liegt.

Manch einer wird sich wundern, warum wir den jetztigen CS-Wert nehmen: der Interrupt-Handler befindet sich ja im Kernel-Bereich (Remember? Monolithischer Kernel?), deshalb kann man auch diesen CS-Wert benutzen.

Wie benutzen wir also unsere schöne neue Funktion zur Textausgabe?

\<asm\> mov si, Message ; der String

       mov al, 0x01    ; wir brauchen Funktion 0x01
       int 0x21        ; unser Interrupt!!!</asm>

So, das wars auch schon. Jeder kann jetzt mit wenig Aufwand neue Funktionen hinzufügen und so seine API Stück für Stück erweitern. War doch einfach, oder?

## Nachtrag von TeeJay

Hier noch ein kleiner Nachtrag zum Thema Interrupts der Ausgabe 3 von LOWLEVEL.

Wenn man den Befehl "int 10h" im Assembler aufruft, dann passiert nichts anderes, als das der Prozessor einen Sprung an eine ganz bestimmte Stelle im Speicher macht, and der eine Routine steht, die dann ausgeführt wird. Meist muss man vor dem Aufruf ja noch gewisse Werte in den Registern speichern. Das sind dann einfach die Variablen, die man an diese Routine übergibt.

So, nun wüßte man wohl auch gerne, wo sich diese Stelle im Speicher befindet, zu der der Prozessor springt und woher er diese weiß.

Das ist ganz einfach. Es gibt eine sogenannte Interrupt Vector Tabelle, die direkt im Speicher an der Adresse 0000:0000 steht. Die Tabelle umfasst 256 Einträge (es gibt daher auch 256 verschiedene Interrupts). Jeder Eintrag dieser Tabelle ist genau 4 Bytes lang. In diesen 4 Bytes stehen der Offset (2 Bytes) und das Segment (2 Bytes), an denen sich Code im Speicher befindet, welcher ausgeführt werden soll, wenn dieser Interrupt aufgerufen wird.

Nun wird auch ersichtlicher was im folgenden Code passiert:

\<asm\> push dx

       push es
       xor ax, ax
       mov es, ax
       cli
       mov word [es:0x21*4], _int0x21  ; Pointer auf den Handler
       mov [es:0x21*4+2], cs           ; Pointer auf CS
       sti
       pop es
       pop dx</asm>

Entscheiden sind hier die Zeilen zwischen "cli" und "sti".

Hier überschreibt man den Eintrag der Interrupt Vector Tabelle so, dass dieser auf den Code zeigt, der ausgeführt werden soll, wenn man Interrupt 21h aufruft. Man sieht nun auch, wie man sich die Adresse jedes Eintrages dieser Tabelle errechnet.

Man multipliziert einfach die Interruptnummer mit 4 (jeder Eintrag ist 4 Bytes lang). Und genau SO findet auch der Prozessor den Code den er ausführen soll, wenn ein Interrupt aufgerufen wird. Er schaut also in der Tabelle nach, zu welcher Stelle er im Code Springen soll um dort die Routine des Interrupts auszurühren.

Als kleine Anmerkung sei noch erwähnt, dass auch der PIC (Programmable Interrupt Controller) in dieser Tabelle nachschaut, um den Code zu finden, den er ausführen soll, wenn zum Beispiel eine Taste auf der Tastatur gedrückt wurde. Man muss also nur nachschauen, welchen Interrupt der PIC aufruft, sobald eine Taste gedrückt wurde und kann dann den entsprechenden Eintrag in der Tabelle so abändern, das eine eigens geschriebene Routine dann ausgführt wird. So kann man seinen eigenen Tastaturtreiber schreiben.

Eine Tabelle der Interrupts, die aufgerufen werden, sobald der PIC ein Signal von der Hardware (Soundkarte, Tastatur usw.) empfängt, kann man in Ausgabe 2 von Lowlevel nachlesen.

PS: Man sollte sich beim Verändern der Einträge in dieser Tabelle die Ursprungswerte irgendwo sichern (Variable), damit man diese evtl. wieder herstellen kann. Auch sollte man nicht willkürlich diese Tabelle abändern, da das BIOS seine eigenen Einträge dort reingeschrieben hat.

So führt der Aufruf von int 10h ebenso "nur" zu einer Routine die das BIOS von Haus aus mitbringt um ein Zeichen auf dem Bildschirm auszugeben. Im Internet gibt es vollständige Auflistungen aller 256 Interrupts und in wie weit diese belegt sind. Gerade im Bereich über 200 sind noch ein paar Einträge unbelegt, die man so für eigene Zwecke gebrauchen kann.

PS2: (Das nun folgende ist von mir zusammengereimt! Ich kann nicht belegen, dass dies so stimmt, aber es klingt einleuchtend). Jetzt wird wohl auch klar, warum das BIOS den Bootsektor erst so weit hinten im Speicher (0x7C00) lädt. Das BIOS lädt nämlich vorher seine eigenen Routinen in den Speicher und ändert die Interrupt-Tabelle so ab, dass diese auf diesen Speicher zeigt.

Man könnte sich also theoretisch den gesammten Speicher von 0x0000 bis 0x7C00 (31744 Bytes) auf Diskette schreiben und dann unter Windows, Linux oder DOS in einem Disassembler anschauen. So kann man evtl. nachvollziehen, wie die Routinen des BIOS aussehen und was sie machen. Das wäre eine kleine, wenn auch eher "lächerliche" Abwandlung des Reverse Engeenering \*g\*.

**Anmerkung von Mastermesh: das ist leider nicht richtig. Der Bereich zwischen 0x0000 bis 0x7C00 beinhaltet vor allem Speicheradressen von Systemports und andere Kleinigkeiten. Das BIOS hat seinen Einsprungscode und damit auch seine ganzen Routinen in 0xFFFF.**

PS3: Einige werden sich nun vielleicht ärgern, das sie erst jetzt, wo die guten alten DOS-Zeiten vorbei sind, mit Assembler angefangen haben. Alleine mit dem hier beschriebenen hätte man doch soooo schöne Viren programmieren können \*G\*.

Unter Windows funktioniert das nicht mehr, weil hier der Protected Mode läuft und diesen Speicherbereich vor unerlaubtem Zugriff sperrt. Daher kann man mit Assembler auch nicht mehr so einfach direkt auf die Hardware zugreifen. Zumindest nicht, ohne die API von Windows zu benutzen.

Für Fragen, Berichtigungen oder sonstigem: masta_ace_inc@gmx.de

**mfg TeeJay**

## Lowlevel-Grundlagen, Teil 3

### Aufbau von Disketten

Disketten (Englisch: floppy disk) gibt es schon fast so lange wie es Computer (im heutigen Sinn) gibt. Aufgrund ihrer geringen Speicherkapazität verlieren Sie jedoch immer mehr an Bedeutung, was dazu führt, dass viele neue PCs kein Diskettenlaufwerk (englisch: floppy disk drive, kurz: FDD) mehr besitzen.

### Physikalischer Aufbau

Disketten sind recht einfach aufgebaut: Jede Diskette besitzt zunächst zwei Seiten, denen jeweils ein Schreib-Lese-Kopf (englisch: head) des Diskettenlaufwerks zugeordnet ist. Die Seiten bzw. Köpfe werden mit den Nummern 0 und 1 bezeichnet. Zum Speichern der Kopfnummer reicht also 1 Bit aus. Jede Seite der Diskette ist in Spuren (englisch: track), auch Zylinder (englisch: cylinder) genannt, eingeteilt.

Die Anzahl der Spuren pro Seite ist abhängig vom Diskettentyp. Die äußerste Spur bekommt die Nummer 0, die zweite von außen die Nummer 1 und so weiter. Jede dieser Spuren ist wiederum in Sektoren (englisch: sector) eingeteilt, deren Anzahl auch vom Diskettentyp abhängig ist. Ein Sektor bildet die kleinste les- bzw. schreibbare Einheit einer Diskette. Das heißt: Will man nur 1 Byte der Diskette lesen, muss man den gesamten Sektor, in dem sich das Byte befindet, in den Speicher einlesen. Ein Sektor ist bei jedem Diskettentyp 512 Byte groß. Der erste Sektor einer Spur wird mit der Nummer 1 bezeichnet.

Wie schon erwähnt, gibt es verschiedene Diskettentypen, die im Laufe der Zeit auseinander hervorgegangen sind. Man unterscheidet sie in zweierlei Hinsicht: Das primäre Unterscheidungsmerkmal sind die äußeren Abmessungen. Es gibt 5,25-Zoll- und 3,5-Zoll-Disketten. Das zweite Merkmal ist die Dichte, mit der Daten auf einer Diskette gespeichert werden können. Man unterscheidet "Double Density" (kurz: DD), "High Density" (kurz: HD) und "Extra High Density" (kurz: EHD). In der folgenden Tabelle sind die Merkmale der bekanntesten Diskettentypen zusammengefasst:

|  |  |  |  |  |
| ------------------- | ----------- | ------------------ | ------------------- | ------------------- |
| Maße, Bezeichnung | Kapazität | Spuren pro Seite | Sektoren pro Spur | Sektoren (gesamt) |
| 5,25 Zoll, DD | 360 kB | 40 | 9 | 720 |
| 5,25 Zoll, HD | 1200 kB | 80 | 15 | 2400 |
| 3,5 Zoll, DD | 720 kB | 80 | 9 | 1440 |
| 3,5 Zoll, HD | 1440 kB | 80 | 18 | 2880 |
| 3,5 Zoll, EHD | 2880 kB | 80 | 36 | 5760 |

Wenn überhaupt, werden heute nur noch 1,44-MB-Disketten (3,5", HD) verwendet. Die anderen Diskettentypen sind fast vollkommen aus der Welt der Computer verschwunden.

Der oben beschriebene Aufbau ist nur die halbe Wahrheit. Diese Informationen reichen allerdings für Programmierer völlig aus. Alles weitere, wie zum Beispiel der Aufbau eines Sektors (Prüfbytes, Synchronisation usw.), würde hier zu weit führen. Wer sich dafür interessiert, findet entsprechende Informationen in einem gutem Hardware-Buch.

### Logischer Aufbau

Da der Zugriff auf eine Diskette durch Angabe von Kopf, Spur und Sektor (siehe oben) sehr umständlich wäre, werden den Sektoren einer Diskette fortlaufende Nummern, welche als logische Sektornummern (kurz: LSN) bezeichnet werden, zugeteilt. Um aus einer logischen Sektornummer die physikalischen Sektordaten zu berechnen sind die folgenden drei Gleichungen nötig:

       Kopf = (LSN / 18) % 2 
       Spur = LSN / 36 
       Sektor = (LSN % 18) + 1 

### Booten von Diskette

Vorwort: ja, ich weiß, dass ich das bereits in der ersten Ausgabe behandelt habe. Da aber viele Nachfragen kamen, kommt hier das ganze noch mal ausführlich.

Nachdem der Computer eingeschalten wurde, führt die Hardware einen kleinen Selbsttest (englisch: power-on self test, kurz: POST) durch. Wurde dieser erfolgreich abgeschlossen, kopiert das BIOS den ersten Sektor der Diskette in Laufwerk A in den Speicher. Ist dies nicht möglich, weil zum Beispiel keine Diskette eingelegt wurde, wird das nächste (usw.) Laufwerk verwendet. Die Reihenfolge, in der die Laufwerke überprüft werden, kann im BIOS-Setup (unter Boot-Sequenz) eingestellt werden. Um das eigene Betriebssystem von einer Diskette zu starten, muss das entsprechende Laufwerk immer als ersten im BIOS-Setup angegeben werden, da sonst eventuell das "normale" System von der Festplatte gestartet wird.

Wenn kein Fehler auftritt, kopiert das BIOS den ersten Sektor (Kopf 0, Spur 0, Sektor 1) der Diskette in den Speicher und speichert die Nummer des entsprechenden Laufwerks (0 für a, 1 für b usw.) im Register DL. Die Adresse des ersten Bytes des Boot-Sektors im Arbeitsspeicher ist 0000h:7C00h. Wenn das BIOS seine Arbeit beendet hat, teilt es dem Prozessor mit, dass der Code an der genannten Adresse ausgeführt werden soll.

Dieser Programmcode (maximal 512 Byte, also ein Sektor) muss nun mit möglichst wenig Aufwand den restlichen Code des Betriebssystems von der Diskette in den Speicher laden und dessen Ausführung veranlassen.

Beim Schreiben des Bootloaders sollte man unbedingt beachten, dass außer in den Registern CS, IP und DL keine gültigen Werte gespeichert sind oder sich diese von BIOS zu BIOS unterscheiden. Man darf nicht vergessen, einen Stack (SS und SP) und ein Datensegment (DS) anzulegen, bevor man zum Beispiel versucht, Text auszugeben. Ein häufiger Fehler ist auch, dass falsche Offsets für Sprünge verwendet werden, da das erste Code-Byte bei 7C00h und nicht bei 0000h liegt. Zum Beheben dieses Problems hilft eine Anweisung wie "ORG 7C00h", die zu allen verwendeten Offsets den Wert 7C00h addiert.

## Code Corner

### APM Powerdown

\<asm\>  ; SYSTEM POWERDOWN

       ; WARNING - DO NOT RUN UNDER WIN! (IT WORKS!)
       ; (C) 1999 BY VINNY  
       
       MOV AX,0x5300
       XOR BX,BX
       INT 0x15 ; APM install check
       MOV AX,0x5304
       XOR BX, BX
       INT 0x15 ; disconnect interface
       MOV AX,0x5301
       XOR BX, BX
       INT 0x15 ; connect real-mode interface
       MOV AX,0x5307
       MOV BX,1
       MOV CX,3
       INT 0x15 ; powerdown system</asm>

## OS Projekte: SkyOS

![skyos1.jpg](http://lowlevel.brainsware.org/wiki/images/skyos1.jpg) ![skyos2.jpg](http://lowlevel.brainsware.org/wiki/images/skyos2.jpg) ![skyos3.jpg](http://lowlevel.brainsware.org/wiki/images/skyos3.jpg)

### OS Design

SkyOS ist ein reines Desktop-OS. Das bedeutet, dass man eine sehr schöne GUI zu sehen kriegt und fast alles mit der Maus bedient. Über Vorzüge und Nachteile von so einem System möchte ich jetzt nicht reden, allerdings muss gesagt werden, dass SkyOS dies sehr gut hinbekommt.

Auch die technischen Details können sich sehen lassen: Multitasking, Multithreading, SMP, Virtual Memory - solche Begriffe lassen vermuten, dass SkyOS in hohem Maße ein objektorientiertes und durchdachtes System ist.

Der Kernel erlaubt das dynamische Laden von Modulen. Das heißt, dass man nur einen kleinen Kernel hat (~70 KB), die ganze Funktionalität wird durch Module geladen.

Eine besonders coole Sache ist das Virtual File System: dies ist eine Art Treiber, der Zugriff auf Dateisysteme, Netzwerke und Geräte gibt. In der Praxis bedeutet das, dass man auf eine CD mit der gleichen Methode zugreift wie auf einen FTP-Server.

### Funktionalität

Extrem umfangreich.

- FAT filesystem (LFN support)
- ImageMounter filesystem. (Makes it possible to mount ISO images)
- Various binary formats like PE, COFF, A.OUT and ELF
- IDE / ATA / ATAPI driver for harddisks, cdrom, cd-writer and DVD
- Serial mouse device driver
- PS/2 device driver
- Soundblaster device driver
- RealTek 8129/8139 Network card device driver
- 3c509 Network card device driver
- VESA2.0, VGA16 and ChipsTechnologies device driver
- COM device driver
- Parallel port device driver
- Real Time clock, PIC(8259) and APIC (82489 and Pentium integrated and compatible)
- USB Driver
- Full network stack with Ethernet, IP, ICMP, ARP, UDP, TCP and berkley socket interface
- Network services like DHCP server/client, FTP, HTTP, TELNET, ....
- Resolution and color depth independent
- Supports all resolution with 4,8,16,24 and 32bpp graphic modes
- Support for TrueType Fonts and various graphic formats like GIF, JPEG, BMP, Animated GIF and Icons
- Support for multiple desktops where each desktop can has its own graphic driver, resolution and color depth.
- Clipboard
- Key Accelerators
- Very easy to use C API
- GNU compiler collection
- GNU binutils
- GNU shell tools,.....
- Debugging features to support local and remote debuggers
- Support for OpenGL
- Various games available. (Quake, QuakeII,...)

### Stabilität / Kompatibilität

Vorbildlich. Kein einziges Problem mit bestimmter Hardware. Extrem stabil.

### Dokumentation

Sehr gut. Eine sehr umfangreiche Dokumentation + eine Art Designdokument sind vorhanden.

### Fazit

SkyOS beeindruckt durch die extreme umfangreiche Funktionalität und die ausgereifte GUI. Ein tolles OS, hoffen wir mal, dass dieses Projekt noch lange weitergeführt wird!

## Inside Makros (by TeeJay)

Für Leute, die hauptsächlich mit Hochsprachen (C / C++) arbeiten, wird Assembler ein wenig gewöhnungsbedürftig sein. Nehmen wir zum Beispiel unseren Interrupt, den wir in dieser Ausgabe geschrieben haben. Um einen String auszugeben, schreiben wir:

\<asm\> mov al, 0x01

       mov si, Meldung
       int 0x21</asm>

Umständlich, oder? Mit einem Makro können wir uns sehr viel Arbeit ersparen!

\<asm\>  %macro PrintText 1

       mov al, 0x01
       mov si, %1 
       int 0x21
       %endmacro</asm>

Jetzt reicht es, wenn wir im Code schreiben:

\<asm\> PrintText Meldung\</asm\>

Das ist die einzige Zeile, die man sich einfach merken muss.

Simpel, oder? Wenn man das Prinzip verstanden hat, kann man sich beliebig viele solcher Makros machen, die einem sehr viel Arbeit abnehmen. Der Vorteil liegt klar auf der Hand: der Code ist viel übersichtlicher und wenn mal was an der API geändert wird, muss man nicht den ganzen Code umändern.

## Phils Kolumne

**Software darf einfach nichts kosten...**

...hört man immer mehr Leute predigen. Dieselben Leute, die ohne mit der Wimper zu zucken, viel Geld ausgeben für z.B. "optical-out to coax converter", weils angeblich besser klingt (reiner Beschiss mit Placebo-Effekt - zu dem ich vielleicht zu einem anderen Zeitpunkt mal ein paar Zeilen schreibe :-)

Ich werde das Gefühl nicht los, hier läuft etwas ganz gehörig schief. Da sitze ich monatelang Tag für Tag, Abend für Abend am Rechner, um ein Programm zu entwickeln und muss mir dann reichlich unverschämte E-Mails durchlesen, mit der Bitte um Erklärung, weshalb ich dafür Geld haben möchte. Ein Einsteckkarte, die genau das Gleiche macht - und u.U. in einem Bruchteil der Zeit entwickelt wurde, verkauft sich dagegen fast von selbst, und keiner fragt mich, weshalb sie etwas kostet. Tja, wenn die Leute es nicht anders wollen, dann fällt mir auch noch ein, wie ich ihren letzten PCI-Slot zumüllen kann. Auch wenn das noch so unnötig ist.

Die einzige Erklärung, die ich für dieses Phänomen habe, ist einfach, dass die Leute glauben, etwas in der Hand haben zu müssen für ihr Geld. Ein Programm, das womöglich noch über das Internet kommt und nicht mal eine Diskette benötigt, ist in den Augen - der vermutlich sogar Mehrheit - der Anwender, schlicht und einfach kein Produkt, für das Geld zu bezahlen gerechtfertigt ist.

Wann das nun aber diese so genannte "Dienstleistungsgesellschaft" ist, in der wir angeblich leben, dann gute Nacht....

Also wieder mal Schelte für diese fiesen Raubkopierer, die uns nicht die Butter aufs Brot gönnen? Jein... Ich sehe das etwas differenzierter. Wer heutzutage z.B. eine Arbeitsstelle sucht, hat reichlich schlechte Karten, wenn er von den großen bekannten Softwarepaketen keine Ahnung hat. Ähnliches gilt inzwischen auch für die Schule: Die, die finanziell in der Lage sind, sich die Software zu kaufen, haben entsprechende Vorteile im Unterricht. Das kanns ja irgendwie auch nicht sein. Ebenso kann es doch keinem verübelt werden, dass er sich das Zeug - was auch immer - einfach mal anschauen möchte.

Ich gehe sogar noch weiter und fordere eine eindeutige Gesetzgebung. Die aktuelle Situation ist die, dass quasi jeder, der einen Computer hat, potentiell kriminell ist. Bei Jedem, der einen Rechner hat, könnte also zu jeder Zeit die Polizei einlaufen und die Bude auf den Kopf stellen. Natürlich suchen die kein raubkopiertes WinZip - diese Raubkopie würde aber im Nachhinein die Durchsuchung rechtfertigen. Vollkommen egal und unabhängig davon, was die tatsächlich gesucht haben! Das Recht auf Unantastbarkeit der Privatsphäre ist damit also so ganz nebenbei wirkungsvoll unterlaufen. Das gibt mir zu Denken. Das sollte uns zu denken geben...

**phil**

## Nachwort

Puuuuuuuh... fertig ^\_^

Jetzt muss ich hier aber noch eine Sache sagen... es haben mich jetzt einige Leute angesprochen und gefragt, ob ich nicht auf Betriebssystemprogrammierung unter C/C++ eingehen kann.

Übrigens kommen wir bei einem Kernel, der in C/C++ geschrieben ist, trotzdem nicht um Assembler rum. Der Bootsektor und der "Startup-Code" müssen in Assembler geschrieben sein. Das geht einfach nicht anders.

Nun die Frage an euch: sollen wir weiterhin mit Assembler programmieren - eben Lowlevel :) - oder soll ich euch zeigen, wie man einen Kernel in C macht?

**Mastermesh**

|  |  |  |
| ------------------------------------------------------------------------------- | ---------------- | ------------------------------------------------------------------------------- |
| « [Ausgabe 2](Ausgabe-2 "Ausgabe 2") | **Navigation** | [Ausgabe 4](Ausgabe-4 "Ausgabe 4") » |

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/7483/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1419/index.html)

<!-- MediaWiki page 1419; revision 7483; parent 7471; 2010-04-01T10:35:14Z -->
