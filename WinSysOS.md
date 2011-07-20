# WinSysOS

## Autor

Moin ihr alle ich bin Ronny Barthmann ( WindowSystemCompany )

### Lebenslauf

Als ich 8 war hate ich schon ein Rechner mit Win98 aber ich war damals so in dieser Texteingabe verschossen das ich die BATCH-Sprache auswendich lehrnte Als ich 9 war konnte ich schon alle BATCH befehle auswendig und erstellte selber Scripte und Benutzerdefinierte Bootdisketten mit MicrosoftDOS die eine ganze menusteuerung ( mit CHOICE ) hatte Als ich 12 War lernte ich PureBasic kennen weiel ich durch BATCH den drang verspürte richtige Programme zu erstellen Durch fehlender strukturkentnis und unwissenheit in der WinAPI erstellte ich nur kleine Tools Als ich 15 war ( also vor 2 Jahren ) lehrnte ich dan mein Baby kennen ( FlatAssembler ) Jedoch wusste ich immernochnichts über die WinAPI und konnte deshalb keine Programme in FASM erstellen Aber ich war von der Machinennahen Sprache so überzeugt ( und süchtig ) das ich sie nicht aufgeben wollte

### Weg zum ersten vorläufer vom OS

Schon in PureBasic versuchte ich eigene Dektops zu Programmieren, jedoch scheiterte ich immer an der Intigrierung in das OS

#### Menuet und KolibriOS

Im Internet sah ich irgendwahn MenuetOS ... ich fragte mich wie man ein Grafich ausgereiftes OS auf EINE DISKETTE kriegte ... IREE dann fand ich bei recherschen KolibriOS ... bo ej das war der reinste Hammer EXTREM AUSGEREIFTE GRAFIG , VIELE PROGRAMME und das beste war das war auch nur auf EINER DISKETTE ich fragte mich wie das geht und forschte nochweiter nach und fand heraus das die beiden OSe in ( juhu ) FLATASSEMBLER geprogt wurden

#### FDOS

dan fand ich FDOS das war auch in Assembler geprogt zwar in NASM aber ich stellte fest das NASM und FASM sich sehr ähnlich sind also schaute ich ein bischen in der Quelltext und fand heraus das es garnicht so schwer ist ein OS zu schreiben

## WinSysOS

WinSysOS ( Eigentglichername ist WindowSystemOS ) ist ein von [Mir](https://lowlevel-eu.github.io/wiki/pages/2456/index.html) erstelltes Betriebssystem was das ziel verfolgt

### Inspieration

als ich mich in FDOS ( siehe WinSysOS\Lebenslauf\FDOS\\ ) vertiefte merkte ich das es garnicht so schwer ist ein OS zu schreiben und da ich ja auch schon damals vergeblichst versucht hate ein Desktop ( in PureBasic ) zu schreiben machte ich einen Neuen versuch Und wolla war ich darauf regelrecht SÜCHTIG nochmal zu versuchen ein Betriebssystem zu progen

### Ziele

Mein Ziel war ein Betriebssystem zu erstellen das es Grafich ( selbst im Textmodus ) in sich hatte und das habe ich erreicht :

## Versionen ( Diereckt von Befehl "changes" kopiert )

    Žnderungen von WindowSystemOS :

    * = Ge„ndert / Repariert
    ! = Hinweis / Info
    + = Hinzugefgt
    - = Entfehrnt 

### 0.0.1 Beta

     [!] Erste Version
     [+] "RESET" zum zurksetzen
     [+] "EXIT" zum runterfahren
     [+] "VER" zum herausfinden der OS-Version
     [+] "HELP" als kleine Hilfe
     [+] "INFO" ein paar Worte vom Programmierer
     [+] "CLS" um den Bildschirm zu l”schen
     [+] Color untersttzung
     [+] Back untersttzung bei Befehleingabe 

### 0.0.2 Beta

     [*] "INFO" zeigt jetzt wirklich Text
     [*] Komplett neues Style / Farbgebung
     [+] "CHANGES" zum verfolgen der Žnderungen
     [+] Pause funktion
     [+] Commander Prefix "CMD>"      

### 0.0.3 Beta

     [+] Diskettenzugriffs-Funktionen
     [+] String2Value zur Zahleingabe ( HEX und DEC )
     [+] Value2String zur Zahlausgabe ( nur HEX )
     [+] "Read" zum Lesen von Sektoren
     [+] "Write" zum Schreiben von Sektoren
     [+] "RawRead" zum Lesen von Sektoren ( rohformat )
     [+] Benutzerverwaltung mit Passwortschutz
     [+] "Registry" zum „ndern der Benutzerdaten
     [+] Einstellungen werden gespeichert   

### 0.0.4 Beta

     [+] Value2String zur Zahlausgabe ( DEC )
     [+] Tastatur hat jetzt deutsches Layout
     [+] "Copy" um Sektoren kopieren zu k”nen
     [+] "Move" um Sektoren verschieben zu k”nen
     [+] "Del" um Sektoren l”schen zu k”nen
     [+] "Run" um Sektoren ausfhren zu k”nnen   

### 0.0.5 Beta

     [*] "Registry" passwort sicherung fuktioniert
     [*] Farbfehler in "HELP"
     [*] Farbfehler in "INFO"
     [*] "RUN" funktioniert jetzt
     [*] "UE" "OE" "AE" mit "š" "™" "Ž" ausgetauscht
     [*] Back untersttzung repariert
     [+] Beispielprogramm "run 2879" ( im Sektor 2879 )
     [+] "FullRead" zum Lesen von Sektoren ( 512 Byte )
     [+] Passwort verschlsselung
     [+] "Type" zum Seitenweisse anzeigen eines Sektors  

### 0.0.6 Beta

     [*] "Reset" in "Help" eingefgt
     [*] Texteingabe repariert
     [*] Ge„nderte Speicherbereiche
     [*] Neues Style / Farbgebung
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
     [+] "Welcome" um zum Startbildschirm zu w„chseln
     [+] "Save" um die Benutzereinstellungenn zu speichern
     [+] "Load" um die Benutzereinstellungen zu laden     

## Zukunft

Die zukunft von WinSysOS stell ich mir folgender maßen for:

### Grafig

Ab Version 0.0.8 ( jetzt ) werde ich versuchen in der Grafig modus zu wächseln und eine richtige GUI anzubieten

### Sprachen

Mein os wird ausschlieslich in Deutsch sein auser irgend etwas "bringt mich von rechten weg ab" dann wird es in Englisch und Deutsch erheltlich sein

### Treiber

Überlegt habe ich Treiber für Maus Bildschirm Festplatten USB-Massenspeicher und Laufwerke zu erstellen

### Netzwerk & internet

Ich hasse Internet daher wird Internet und Netzwerk mein letztes Projekt sein===

### Dateisystem

#### Bis jetzt unterstützt

Sektor adressierung

#### In zukunft

FAT12 FAT32 CDFS NTFS ( in GANZ fehrner zukunft )

## Internetlinks

[Mein Projekt bei SourceForge](https://sourceforge.net/projects/winsysos/files/) [Meine Diskusieonsseite](http://www.coding-board.de/board/showthread.php?t=30903) [FlatAssembler Downloadseite ( Englich)](http://flatassembler.net/download.php) [PureBasic Downloadseite ( Deutsch )](http://www.purebasic.com/german/download.php) [PureBasic Downloadseite ( Englich )](http://www.purebasic.com/download.php)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/9955/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2457/index.html)

<!-- MediaWiki page 2457; revision 9955; parent 0; 2011-07-20T13:20:09Z -->
