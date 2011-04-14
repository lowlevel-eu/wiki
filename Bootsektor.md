# Bootsektor

Als **Bootsektor** oder auch **Boot Record** bezeichnet man den Sektor eines Datenträgers oder Laufwerks, der vom [BIOS](https://github.com/lowlevel-eu/wiki/wiki/Basic-Input-Output-System "BIOS") während des Bootprozesses eingelesen und ausgeführt wird. Aufgabe des Bootsektors ist es das [Betriebssystem](https://github.com/lowlevel-eu/wiki/wiki/Betriebssystem "Betriebssystem") oder einen [Bootloader](https://github.com/lowlevel-eu/wiki/wiki/Bootloader "Bootloader") zu laden.

Der Bootsektor ist in der Regel 512 Byte groß und endet mit der Magic Number **0xAA55**, anhand welcher das [BIOS](https://github.com/lowlevel-eu/wiki/wiki/Basic-Input-Output-System "BIOS") den Sektor als gültigen Bootsektor erkennt. Bei Disketten befindet sich der Bootsektor im ersten Sektor des Datenträgers. Bei Festplatten im ersten Sektor der bootfähigen Partition des Datenträgers. Der erste Sektor einer Festplatte hingegen heißt [Master Boot Record](https://github.com/lowlevel-eu/wiki/wiki/Master-Boot-Record "Master Boot Record").

## siehe auch

- [Eigener Bootloader](https://github.com/lowlevel-eu/wiki/wiki/Eigener-Bootloader "Eigener Bootloader")
- [Ausgabe 1 (4.3 Unser Bootloader)](https://github.com/lowlevel-eu/wiki/wiki/Ausgabe-1#unser-bootloader "Ausgabe 1")

## die Anfängliche Umgebung

Das folgende gilt nur eingeschränkt für Bootfähige CD-ROMs, sondern nur für Datenträger, auf die über int13h zugegriffen werden kann. (USB-Sticks können Emuliert werden)

### Zum Formatierungszeitpunkt

**Ist folgendes bekannt**

(der Bootsektor wird in der Regel von einem Formatierungsprogramm angelegt)

- Arte des Mediums, (Diskette, Fesplatten**partition**,USB-Stick)
- falls Fesplatte, beginn der Partition (wird in der Regel auch vom MBR übergeben (ES:DI), jedoch sicher ist sicher)
- ob CHS- oder LBA- Zugriff nötig sein wird (nur ein Treiber - spart Platz)
- Dateisystem
- Name und Zieladresse der zu Ladenden Datei
- Der Speicher zwischen 500h und 7c00h wird vorhanden und frei sein.
- Laufwerkszugriff über int13h ist warscheinlich möglich
- Konsolenausgabe über int10h funktion 0Eh ist warscheinlich möglich

**folgendes jedoch NICHT, oder nicht verlässlich**

- welches Physische Laufwerk
- exakte Position der zu ladenden Datei
- welcher Prozessor (also keine exotischen Befehle verwenden)
- ob der Arbeitsspeicher zwischen 7e00h und A0000h vollständig vorhanden, und frei sein wird. (könnte theoritisch nur 32k haben (PC),irgendwo MUSS die EBDA sein, Prä-Boottreiben könnten vorhanden sein)
- Art des Festplattenkontorollers (z.b. ATA oder SATA die sich leicht unterscheiden)
- Details des Prozessorcaches (bei selbstmanipulierendem Code zu beachten)
- Ob die zu ladende Datei vorhanden sein wird (könnte geslöscht sein)

### Zum Bootzeitpunkt

**Beim Laden ist bekannt**

- Physisches Laufwerk (steht in DL)

**nach durchsuchen des Dateisystems wird bekannt**

- ob die zu ladende Datei vorhanden ist (ansonsten Fehlermeldung)
- wo sie beginnt

**im Bootsektor immer noch nicht bekannt ist folgendes**

- was für ein Prozessor vorhanden ist (das erfordert aufwändige tests der Flags)
- ob die Grafikarte überhaupt VGA-kompatibel ist (z.b. bei Laptops nicht sicher)-\> also Fehlermeldungen nur über int 10h, aber nicht den Grafikmodus wechseln und nicht direkt in den Bildschirmspeicher schreiben, bis der Bootloader das geprüft hat)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/9667/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1475/index.html)

<!-- MediaWiki page 1475; revision 9667; parent 9039; 2011-04-14T17:39:15Z -->
