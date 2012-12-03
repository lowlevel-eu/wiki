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

## Nachteile

Da UEFI noch nicht besonders weit verbreitet ist, konnten noch nicht allzu viele Nachteile gefunden werden. Eine potenzielle Gefahr wurde aber bereits festgestellt: Das UEFI besitzt Netzwerk-Funktionen. Dadurch könnten Viren schon vor dem Start des [Betriebssystems](https://github.com/lowlevel-eu/wiki/wiki/Betriebssystem "Betriebssystem") auf den PC gelangen, da auf dem UEFI keine Schadsoftware läuft.

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/10958/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2612/index.html)

<!-- MediaWiki page 2612; revision 10958; parent 10937; 2012-12-03T09:50:59Z -->
