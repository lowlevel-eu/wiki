# WinSysOS

## Autor

Moin ihr alle, ich bin Ronny Barthmann ( WindowSystemCompany )

### Lebenslauf

Als ich 8 war, hatte ich schon ein Rechner mit Win98, aber ich war damals so in dieser Texteingabe verschossen, dass ich die BATCH-Sprache auswendig lernte. Als ich 9 war, konnte ich schon alle BATCH befehle auswendig und erstellte selber Scripte und benutzerdefinierte Bootdisketten mit MicrosoftDOS, die eine ganze Menüsteuerung ( mit CHOICE ) hatten. Als ich 12 war, lernte ich PureBasic kennen, weil ich durch BATCH den drang verspürte richtige Programme zu erstellen. Durch fehlende Strukturkenntnis und Unwissenheit in der WinAPI, erstellte ich nur kleine Tools. Als ich 15 war ( also vor 2 Jahren ), lernte ich dann mein Baby kennen ( FlatAssembler ). Jedoch wusste ich immer noch nichts über die WinAPI und konnte deshalb keine Programme in FASM erstellen, aber ich war von der maschinennahen Sprache so überzeugt ( und süchtig ), dass ich sie nicht aufgeben wollte.

### Weg zum ersten Vorläufer vom OS

Schon in PureBasic versuchte ich eigene Desktops zu Programmieren, jedoch scheiterte ich immer an der Integration in das OS.

#### Menuet und KolibriOS

Im Internet sah ich irgendwann [MenuetOS](MenuetOS.md "MenuetOS") ... ich fragte mich wie man ein grafisch ausgereiftes [OS](Betriebssystem.md "Betriebssystem") auf eine Diskette kriegte ... Irre dann fand ich bei Recherchen [KolibriOS](KolibriOS.md "KolibriOS") ... das war der reinste Hammer: Extrem ausgereifte Grafik, viele Programme und das beste war, dass war auch nur auf einer Diskette ich fragte mich wie das geht, forschte noch weiter nach und fand heraus das die beiden OS in ( juhu ) \[\[FASM \| Flatassembler\] programmiert wurden.

#### FDOS

Dann fand ich FDOS, das war auch in [Assembler](Assembler.md "Assembler") programmiert worden, zwar in [NASM](Netwide-Assembler.md "NASM"), aber ich stellte fest, dass [NASM](Netwide-Assembler.md "NASM") und [FASM](Flat-Assembler.md "FASM") sich sehr ähnlich sind, also schaute ich ein bisschen in der Quelltext und fand heraus, dass es gar nicht so schwer ist ein OS zu schreiben.

## WinSysOS

WinSysOS ( Eigentlicher Name ist WindowSystemOS ) ist ein von [mir](https://lowlevel-eu.github.io/wiki/pages/2456/index.html) erstelltes Betriebssystem, das das Ziel eines [grafischen](Graphical-User-Interface.md "GUI") [Betriebssystems](Betriebssystem.md "Betriebssystem") verfolgt.

### Inspiration

als ich mich in FDOS ( siehe WinSysOS\Lebenslauf\FDOS\\ ) vertiefte merkte ich das es gar nicht so schwer ist ein OS zu schreiben und da ich ja auch schon damals vergeblichst versucht hatte ein Desktop ( in PureBasic ) zu schreiben machte ich einen Neuen versuch. Wolla, war ich regelrecht süchtig geworden, nochmal zu versuchen ein [Betriebssystem](Betriebssystem.md "Betriebssystem") zu programmieren.

### Ziele

Mein Ziel war ein Betriebssystem zu erstellen das es grafisch ( selbst im Textmodus ) in sich hat. Das habe ich erreicht :

## Versionen

    Änderungen von WindowSystemOS :

    * = Geändert / Repariert
    ! = Hinweis / Info
    + = Hinzugefügt
    - = Entfernt 

### 0.0.1 Beta

     [!] Erste Version
     [+] "RESET" zum zurücksetzen
     [+] "EXIT" zum herunterfahren
     [+] "VER" zum herausfinden der OS-Version
     [+] "HELP" als kleine Hilfe
     [+] "INFO" ein paar Worte vom Programmierer
     [+] "CLS" um den Bildschirm zu löschen
     [+] Farbunterstützung
     [+] Backunterstützung bei Befehlseingabe

### 0.0.2 Beta

     [*] "INFO" zeigt jetzt wirklich Text
     [*] Komplett neuer Style / Farbgebung
     [+] "CHANGES" zum verfolgen der Änderungen
     [+] Pause Funktion
     [+] Command Präfix "CMD>"   
      

### 0.0.3 Beta

     [+] Diskettenzugriffs-Funktionen
     [+] String2Value zur Zahleingabe ( HEX und DEC )
     [+] Value2String zur Zahlausgabe ( nur HEX )
     [+] "Read" zum Lesen von Sektoren
     [+] "Write" zum Schreiben von Sektoren
     [+] "RawRead" zum Lesen von Sektoren ( rohformat )
     [+] Benutzerverwaltung mit Passwortschutz
     [+] "Registry" zum ändern der Benutzerdaten
     [+] Einstellungen werden gespeichert 
     

### 0.0.4 Beta

     [+] Value2String zur Zahlausgabe ( DEC )
     [+] Tastatur hat jetzt deutsches Layout
     [+] "Copy" um Sektoren kopieren zu können
     [+] "Move" um Sektoren verschieben zu können
     [+] "Del" um Sektoren löschen zu können
     [+] "Run" um Sektoren ausführen zu können   

### 0.0.5 Beta

     [*] "Registry" Passwort Sicherung funktioniert
     [*] Farbfehler in "HELP"
     [*] Farbfehler in "INFO"
     [*] "RUN" funktioniert jetzt
     [*] "UE" "OE" "AE" mit "Ü" "Ö" "Ä" ausgetauscht
     [*] Backunterstützung repariert
     [+] Beispielprogramm "run 2879" ( im Sektor 2879 )
     [+] "FullRead" zum Lesen von Sektoren ( 512 Byte )
     [+] Passwort Verschlüsselung
     [+] "Type" zum Seitenweisen anzeigen eines Sektors  

### 0.0.6 Beta

     [*] "Reset" in "Help" eingefügt
     [*] Texteingabe repariert
     [*] Geänderte Speicherbereiche
     [*] Neuer Style / Farbgebung
     [*] Beispielprogramm von 2879 nach 2000 verschoben
     [*] Befehl "Reset" in "Restart" umbenannt
     [!] Sektoren    0- 999 = System
     [!] Sektoren 1000-1999 = Benutzer
     [!] Sektoren 2000-2879 = Programme
     [+] Indexsektor "type 1000" ( im Sektor 1000 )
     [+] Beispielprogramm "run 2001" ( im Sektor 2001 )
     [+] ASmallOS "run 2002" ( im Sektor 2002 )
     [+] "Reset" zum zurksetzen ( ohne Einstellungen zu speichern )

### 0.0.7 Beta

     [*] Beispielprogramm 2001 optimiert
     [*] Befehl "Exit" in "ShutDown" umbenannt
     [*] Schreibfehler bei "Changes" "Version 0.0.2"
     [*] Schreibfehler bei "Changes" "Version 0.0.6"
     [*] Texteingabe repariert
     [+] "Exit" zum herunterfahren ( ohne Einstellungen zu speichern )
     [+] "Welcome" um zum Startbildschirm zu wechseln
     [+] "Save" um die Benutzereinstellungen zu speichern
     [+] "Load" um die Benutzereinstellungen zu laden     

## Zukunft

Die Zukunft von WinSysOS stell ich mir folgender maßen vor:

### Grafik

Ab Version 0.0.8 ( jetzt ) werde ich versuchen in der Grafikmodus zu wechseln und eine richtige GUI anzubieten.

### Sprachen

Mein OS wird ausschließlich in Deutsch sein, es sei denn irgendetwas "bringt mich von rechten Weg ab", dann wird es in Englisch und Deutsch erhältlich sein.

### Treiber

Überlegt habe ich Treiber für Maus, Bildschirm, Festplatten, USB-Massenspeicher und Laufwerke zu erstellen.

### Netzwerk & Internet

Ich hasse Internet, daher wird Internet und Netzwerk mein letztes Projekt sein.

### Dateisystem

#### Bis jetzt unterstützt

Sektor Adressierung

#### In Zukunft

FAT12 FAT32 CDFS NTFS ( in ganz ferner Zukunft )

## Internetlinks

[Mein Projekt bei SourceForge](https://sourceforge.net/projects/winsysos/files/) [Meine Diskussionsseite](http://www.coding-board.de/board/showthread.php?t=30903) [FlatAssembler Download Seite ( Englisch)](http://flatassembler.net/download.php) [PureBasic Download Seite ( Deutsch )](http://www.purebasic.com/german/download.php) [PureBasic Download Seite ( Englisch )](http://www.purebasic.com/download.php) [FDOS](http://fdos.de/fdos/download/) [MenuetOS](http://menuetos.de/downloads/) [KolibriOS](http://www.kolibrios.org/)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/11438/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2457/index.html)

<!-- MediaWiki page 2457; revision 11438; parent 10842; 2020-08-02T21:51:07Z -->
