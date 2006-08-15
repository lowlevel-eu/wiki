# Ausgabe 9

## 1. Einleitung

Hi, wie ihr sicher auch schon gemerkt habt, ist das Weiterführen vom Magazin nicht immer unproblematisch. Deshalb haben N00B und ich vor, einige Änderungen durchzuführen. Im Wesentlichen betrifft das das Kategoriesystem. Es wird keine 10 Kategorien mehr geben, die in allen Ausgaben vorhanden sind. Stattdessen hat jede Ausgabe einen Thmenschwepunkt. Das könnten z.B. Protected Mode Features sein, mit Tutorials über Paging, Hardware MT, usw. Natürlich gibt es trotzdem noch einige Standard Kategorien, nämlich die News, das OS-Showcase, usw. In dieser Ausgabe wird der Schwerpunkt bei Speichergeräten liegen, wir haben dazu eine IDE-Übersicht, ein ext2-Tutorial, und noch einiges mehr.  
Dies wird außerdem die erste Ausgabe sein, die nicht nur als PDF File sondern auch im Wiki erscheint. Das hat natürlich den Vorteil, dass Fehler schnell verbessert werden können.  
Wir wünschen euch viel Spaß mit der neuen Ausgabe!

## 2. News

Viel neues ist passiert seit der letzten Ausgabe - auch nicht weiter verwunderlich, wenn man bedenkt wieviel Zeit ins Land gegangen ist ;) . Vor wenigen Wochen, am 22.7 ist QEMU 0.8.2 herausgekommen. Als einer der wenigen Emulatoren verfügt er über ein Kernelmodul um die Ausführung der ganzen VM erheblich zu beschleunigen - mir fällt sonst nur VMWare ein, dass diese Möglichkeit nutzt. Neu in der aktuellen Version sind u.a. ACPI Support und einige Verbesserungen der USB-Fähigkeiten.  
  
Auch beim längst totgeglaubten Community-OS LOST gibt es Fortschritte. Seitdem taljeth die Projektleitung übernommen hat, sind einige Fortschritte zu beobachten. Mittlerweile funktioniert sogar eine erste Form des Multitasking, welche Jidder/PorkChicken zusammen mit dem Phys. Speichermanagment entwickelt hat. Es fehlt also nicht mehr viel bis die ersten Treiberprogramme (FÜr die die es nicht wissen, LOST ist ein Microkernel) geschrieben werden können.

## 3. Ein OS auf einer CD-ROM

### Index

- Einleitung
- Praxis: Ahead Nero
- Theorie: Das ISO El-Torito Format
- Nachwort

### Einleitung

Irgendwie ist es halb drei Uhr in der Früh und ich kann nicht mehr schlafen, darum will ich jetzt mal was sinnvolles machen und anderen versuchen zu erklären, wie man ein Betriebssystem auf eine CD-ROM bekommt, und wie das BIOS dieses ISO El-Torito Format ließt. Nun gut, auf gehts...

### Praxis: Ahead Nero

Wenn wir unser Betriebssystem geschrieben haben und in einer .IMG Datei compiliert haben, schreiben wir es normalerweise mit RaWrite (oder einem ähnlichen Programm) 1 zu 1 auf eine Diskette. Da aber in unserer 'modernen' Welt selbst PCs existieren, die keine Diskettenlaufwerke mehr haben (tja, scheisse :D) haben wir Pech gehabt. Oder? Anstatt das Betriebssystem auf einer Diskette anzubieten, können wir es auch auf eine CD-ROM schreiben (ein CD-ROM Laufwerk hat beinahe jeder PC/Laptop), und wir sind dieses Problem los. Wie schreibt man nun ein Betriebssystem auf eine CD-ROM. Ich werde das nun versuchen Schritt für Schritt zu erklären:  
  

1.  Man compiliert sein Betriebssystem ganz normal, und erstellt eine .IMG

Datei - wie es auch für Disketten-Betriebssysteme gemacht wird.

1.  Man öffnet 'Ahead Nero Burning ROM' (btw: ich finde den Namen sehr

gelungen :D).

1.  Neue Zusammenstellung -\> 'CD-ROM (Boot)'
2.  Das Options-Feld 'Image-Datei' anklicken und den Pfad zum Image des

Betriebssystems eingeben. 'Neu' klicken.

1.  Dann, schlussendlich, das Dialogfeld 'CD Brennen' klicken und die

CD-ROM brennen.  
  
Wenn wir nun den Computer neu starten, und im BIOS die Option "von CD-ROM Booten" auswählen, startet unser Betriebssystem als wäre es eine Diskette. OK, wir wissen nun, wie es gemacht wird, aber nicht, warum es das macht.

### Theorie: Das ISO El-Torito Format

Eine bootfähige CD-ROM hat in den meisten Fällen ein Dateisystem namens "ISO El-Torito". Das ist der gängige Standart für bootfähige CD-ROMs, die fast alle BIOS-Systeme erkennen.  
  
Zuerst ist wichtig: Ein Sektor auf einem ISO-Datenträger ist 0x800 Byte groß (im Gegensatz zu Sektoren auf FAT Systemen, die grundsätzlic 0x200 Byte groß sind).  
  
Bei El-Torito CD-ROM wird im Grunde nichts anderes gemacht als eine Diskette emuliert, die das bootfähige Image beinhaltet. Das ISO-El-Torito Format ist grundsätzlich so aufgebaut:  
  

                   +-------------------------+
        Sector 0:  |          SYSTEM         |
                   |         (UNUSED)        |
                   |-------------------------|
        Sector 16: |      Primary Volume     |
                   |-------------------------|
        Sector 17: |    Boot Record Volume   |-------+
                   |-------------------------|       |
                   |                         |       |
                   |-------------------------|       |
                   |                         |       |
                   |-------------------------|       |
                   |                         |       |
                   |-------------------------|       |
                   | Set Termination Volume  |       |
                   |-------------------------|       |
                   |     Boot Catalog        | <-----+ 
                   |                         |-------+
                   |-------------------------|       |
                   |  Bootable Disk Image    | <-----+
                   |-------------------------|
                   |      CD-ROM Image       |
                   +-------------------------+

  
  
Das bedeutet im Sektor 17 (an der Adresse 17 \* 0x800) ist das Boot-Record Volume. Dieses hat einen Zeiger auf den Boot-Catalog, und sieht folgendermaßen aus:  
  

        Offset * Type  * Description
        ****************************
        0      * Byte  * Boot Record Indicator
        1-5    * Byte  * ISO-9660 Identifier, must be 'CD001'
        6      * Byte  * Version of the descriptor, must be 1
        7-26   * Byte  * Boot System Identifier, must be 'EL TORITO SPECIFICATION" 
                         padded with 0's.
        27-46  * Byte  * Unused, must be 0.
        47-4A  * DWord * Absolute pointer to first sector of Boot Catalog.
        4A-7FF * Byte  * Unused, must be 0.

  
  
Wie wir hier deutlich erkennen können, ist an der Adresse 0x47-0x4A im 17. CD-ROM Sektor der Pointer zum Boot-Catalog. Wir folgen nun diesem Pointer und sehen uns den Boot Catalog an:  
  

        Offset * Type  * Description
        ****************************
        0      * Byte  * Header ID, must be 01.
        1      * Byte  * Platform ID.
        2-3    * Word  * Reserved, must be 0.
        4-1B   * Char  * ID-String.
        1C-1D  * Int   * Checksum Word.
        1E     * Byte  * Key Byte, must be 55.
        1F     * Byte  * Key Byte, must be AA.

  
  
Hier sehen wir zuerst einige Standart-Strings und Zeichen ("0x55, 0xAA" sollten wir schon kennen). 0x20 Byte weiter (also 32 Bytes weiter) im selben Sektor befindet sich dann der "Initial/Default Entry", der auch den Pointer zu unserem Boot-Image beinhaltet:  
  

        Offset * Type  * Description
        ****************************
        0      * Byte  * Boot Indicator (88=bootable | 00=not bootable)
        1      * Byte  * Boot media Type
        2-3    * Word  * Load segment (standart is 0x7C0)
        4      * Byte  * System Type.
        5      * Byte  * Unused, must be 0.
        6-7    * Word  * Sector count.
        8-0B   * DWord * Load RBA. This is the start address of the virtual disk.
        0C-1F  * Byte  * Unused, must be 0.

  
  
An der Adresse 0x08-0x0B befindet sich schließlich der Pointer zum Image unseres Betriebssystems. Hier befindet sich also das Image - und wir wissen nun auch ein bisschen, wie unser Betriebssystem auf einer CD-ROM gespeichert ist.  
  
Wer mehr wissen möchte, sollte folgende Dokumente lesen:

- FAT: Gerneral Overview of On-Disk Formation by Microsoft Corporation
- Volume and File Structure of CDROM for Information Interchange
- "El Torito" Bootable CD-ROM Format Specification

### Nachwort

Das wars auch schon wieder - ich hoffe man konnte einige nützliche Informationen im Artikel finden. Falls nicht, mir egal - ich bin endlich müde und kann vielleicht weiterschlafen ;). Also, schön weiterprogrammieren, lernen, Ideen entwickeln und so weiter. Und: Von nichts und niemandem vom Kurs abbringen lassen ;)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/1422/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1409/index.html)

<!-- MediaWiki page 1409; revision 1422; parent 1419; 2006-08-15T15:44:56Z -->
