# Unified Extensible Firmware Interface

Diese Seite oder Abschnitt ist zwar komplett, es wird aber folgende Verbesserungen gewünscht:  

*nützliche Protokolle, gnu-efi und co erwähnen. Beispielcode (gerne mich mal wieder anhauen [Littlefox](https://lowlevel-eu.github.io/wiki/pages/2674/index.html "Benutzerin:Littlefox") (Diskussion))*

Hilf Lowlevel, den Artikel zu verbessern.

  
**Unified Extensible Firmware Interface** (oder kurz **UEFI**) ist der Nachfolger des [BIOS](Basic-Input-Output-System.md "BIOS"), welches nach drei Jahrzehnten leicht veraltet war. So kann man mit dem typischen BIOS keine Festplatten mit sehr großer Speicherkapazität von über 2 TB addressieren, was mit dem UEFI möglich wird.

Das UEFI ist der direkte Nachfolger von EFI (*Extensible Firmware Interface*). Seit 2005 existiert das Unified EFI Forum, in dem zahlreiche Unternehmen aus der IT-Branche vertreten sind. So wird der Standard nicht mehr ausschließlich von Intel festgelegt.

Die UEFI-Spezifikation ist absichtlich Plattformneutral gehalten, es gibt UEFI-Implementierungen für x86, x86_64, ARMv7 (32Bit), ARMv8 (64Bit) und IA64. Aus dem IA64-Umfeld kommt das ursprüngliche EFI.

## EFI-Programme

EFI-Programme sind [PE](Microsoft-Portable-Executable-and-Common-Object-File-Format.md "PE")-Dateien mit der Dateiendung EFI. Standardmäßig wird auf x86_64 die Microsoft-ABI verwendet. Kompiliert man mit anderen Compilern (wie gcc), muss man jeden API-Aufruf besonders behandeln.

Es gibt auch die Möglichkeit Programme Plattformunabhängig mit EFI ByteCode zu erstellen, das wird aber nur selten genutzt. Interessant ist das für Hardware die ihren eigenen Treiber mitbringt.

Um selber EFI-Programme zu schreiben kann man entweder das EFI Development Kit II (EDKII) oder gnu-efi verwenden. Gefühlt ist die Doku für beides eher spärlich, die meisten Infos findet man noch im Quellcode.

## Bootvorgang

Im Gegensatz zum BIOS bootet das UEFI Programme. Diese Programme liegen auf einer EFI SystemPartion (ESP) mit der Dateiendung .EFI. Es können mehrere Programme nacheinander ausgeführt werden. Die UEFI-Spezifikation definiert eine API um alle wichtigen Infos des Computers zu kommen, beispielsweise eine Memory-Map oder die eingebauten PCI-Geräte. Sobald ein Programm der Firmware mitteilt den Boot-Prozess zu beenden ist dieses Programm der laufende Betriebssystemkernel, womit nur noch manche Funktionen des UEFI genutzt werden können, das Programm dafür aber die volle Kontrolle über den Computer bekommt.

Auf der ESP gibt es die folgende Ordnerstruktur:

    EFI/
       BOOT/
          BOOTX64.EFI
       debian/
          BOOTX64.EFI

Der Ordner /EFI/BOOT ist der Boot-Pfad für Wechseldatenträger. Das dort drin liegende Programm wird ausgeführt wenn der Nutzer zum Beispiel sagt von CD booten zu wollen. Außerdem kann man unterhalb des EFI-Ordners mehrere Order für verschiedene installierte Betriebssysteme haben. Viele Firmwares bieten eine Möglichkeit beim Start das gewünschte Betriebssystem auszuwählen - man benötigt also nicht mehr zwingend einen Boot-Manager.

## Unterschiede zum BIOS

### Vorteile

#### Höhere Geschwindigkeit

Das System bootet schneller. Das liegt daran, dass die verschiedenen Bestandteile des Computers nun parallel geprüft werden. Außerdem besitzt das UEFI einen eigenen Bootloader. So muss nicht erst der Bootloader selbst gesucht und geladen werden; man kann direkt mit dem Laden des [Betriebssystems](Betriebssystem.md "Betriebssystem") beginnen.

#### Mehr Speicher verfügbar

Wie oben bereits angedeutet, ist es dem BIOS nicht möglich, auf Festplatten mit mehr als 2 Terabytes (2.000.000.000.000 Bytes) auf den kompletten Speicher zuzugreifen. Das UEFI dagegen ist in der Lage, auf bis zu 8 Zettabytes, also 8 Milliarden Terabytes, zuzugreifen. Arbeitsspeicher ist ebenfalls vermehrt verfügbar; es stehen nun theoretisch bis zu 16 Exabyte zur Verfügung (16 Mio. TB). Das liegt an der 64-Bit-Architektur, die auf normalen PCs mit UEFI meistens verwendet wird.

#### Benutzerfreundlichkeit

Die gute, alte BIOS- [Oberfläche](Graphical-User-Interface.md "GUI") hat ausgedient: Kein [Textmodus](Textausgabe.md "Textausgabe") mehr, sondern eine [grafische Oberfläche](Graphical-User-Interface.md "GUI"). Das erleichtert nicht ganz so erfahrenen Benutzern die Bedienung deutlich. Das BIOS-Flair geht dadurch aber leider verloren.

#### Modular

Das UEFI ist sehr modular aufgebaut. Beim Bootvorgang können UEFI-Programme in einer bestimmten Reihenfolge ausgeführt werden. Jedes Programm kann dabei sogenannte Protokolle registrieren, die von später gestarteten Programmen verwendet werden können. Beispielsweise installiert der UEFI-Bootloader "shim" ein Protokoll über das die nachgelagerten Programme (meistens ein richtiger Bootloader wie z.B. Grub) die Signatur einer EFI-Binary prüfen können. So wird Secure-Boot im Linux-Umfeld umgesetzt.

Die UEFI-Programme liegen dabei alle auf einer EFI System Partition (ESP), die FAT32 formatiert ist. Eigene Programme können da problemlos hinzugefügt werden, zumindest sofern sie signiert sind oder Secure Boot abgeschaltet ist.

### Nachteile

#### Komplexität

Da eine UEFI-Firmware sehr komplex ist und viele Features enthält (wie z.B. einen kompletten TCP/IP-Stack) ist es sehr wahrscheinlich dass dort gefährliche Sicherheitslücken vorhanden sind.

#### Secure Boot

Secure-Boot ist eine stark von Microsoft kontrollierte Technik, die es anderen Betriebssystemen erschweren kann auf bestimmten Rechnern zu laufen.

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/11460/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2612/index.html)

<!-- MediaWiki page 2612; revision 11460; parent 11446; 2020-08-02T22:27:52Z -->
