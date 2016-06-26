# Unified Extensible Firmware Interface

**Unified Extensible Firmware Interface** (oder kurz **UEFI**) ist der Nachfolger des [BIOS](https://github.com/lowlevel-eu/wiki/wiki/Basic-Input-Output-System "BIOS"), welches nach drei Jahrzehnten leicht veraltet war. So kann man mit dem typischen BIOS keine Festplatten mit sehr großer Speicherkapazität von über 2 TB addressieren, was mit dem UEFI möglich wird.

Das UEFI ist der direkte Nachfolger von EFI (*Extensible Firmware Interface*). Seit 2005 existiert das Unified EFI Forum, in dem zahlreiche Unternehmen aus der IT-Branche vertreten sind. So wird der Standard nicht mehr ausschließlich von Intel festgelegt.

## Vorteile gegenüber dem BIOS

### Höhere Geschwindigkeit

Das System bootet schneller. Das liegt daran, dass die verschiedenen Bestandteile des Computers nun parallel geprüft werden. Außerdem besitzt das UEFI einen eigenen Bootloader. So muss nicht erst der Bootloader selbst gesucht und geladen werden; man kann direkt mit dem Laden des [Betriebssystems](https://github.com/lowlevel-eu/wiki/wiki/Betriebssystem "Betriebssystem") beginnen.

### Mehr Speicher verfügbar

Wie oben bereits angedeutet, ist es dem BIOS nicht möglich, auf Festplatten mit mehr als 2 Terabytes (2.000.000.000.000 Bytes) auf den kompletten Speicher zuzugreifen. Das UEFI dagegen ist in der Lage, auf bis zu 8 Zettabytes, also 8 Milliarden Terabytes, zuzugreifen. Arbeitsspeicher ist ebenfalls vermehrt verfügbar; es stehen nun theoretisch bis zu 16 Exabyte zur Verfügung (16 Mio. TB). Das liegt an der 64-Bit-Architektur, die von UEFI zwingend erfordert wird.

### Benutzerfreundlichkeit

Die gute, alte BIOS- [Oberfläche](https://github.com/lowlevel-eu/wiki/wiki/Graphical-User-Interface "GUI") hat ausgedient: Kein [Textmodus](https://github.com/lowlevel-eu/wiki/wiki/Textausgabe "Textausgabe") mehr, sondern eine [grafische Oberfläche](https://github.com/lowlevel-eu/wiki/wiki/Graphical-User-Interface "GUI"). Das erleichtert nicht ganz so erfahrenen Benutzern die Bedienung deutlich. Das BIOS-Flair geht dadurch aber leider verloren.

### Modular

Das UEFI ist sehr modular aufgebaut. Beim Bootvorgang können UEFI-Programme in einer bestimmten Reihenfolge ausgeführt werden. Jedes Programm kann dabei sogenannte Protokolle registrieren, die von später gestarteten Programmen verwendet werden können. Beispielsweise installiert der UEFI-Bootloader "shim" ein Protokoll über das die nachgelagerten Programme (meistens ein richtiger Bootloader wie z.B. Grub) die Signatur einer EFI-Binary prüfen können. So wird Secure-Boot im Linux-Umfeld umgesetzt.

Die UEFI-Programme liegen dabei alle auf einer EFI System Partition (ESP), die FAT32 formatiert ist. Eigene Programme können da problemlos hinzugefügt werden, zumindest sofern sie signiert sind oder Secure Boot abgeschaltet ist.

## Nachteile

Da UEFI noch nicht besonders weit verbreitet ist, konnten noch nicht allzu viele Nachteile gefunden werden. Eine potenzielle Gefahr wurde aber bereits festgestellt: Das UEFI besitzt Netzwerk-Funktionen. Dadurch könnten Viren schon vor dem Start des [Betriebssystems](https://github.com/lowlevel-eu/wiki/wiki/Betriebssystem "Betriebssystem") auf den PC gelangen, da auf dem UEFI keine Schutzsoftware läuft.

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/11348/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2612/index.html)

<!-- MediaWiki page 2612; revision 11348; parent 10978; 2016-06-26T14:00:35Z -->
