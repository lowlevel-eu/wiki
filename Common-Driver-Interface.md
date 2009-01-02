# Common Driver Interface

Common Driver Interface (oder kurz CDI) ist ein Standard, der es ermöglichen soll betriebssystemunabhängige Treiber zu schreiben. Dies funktioniert mithilfe einer Bibliothek, die einmal für ein Betriebssystem implementiert werden muss. Dann können CDI-komforme Treiber einfach mit dieser Bibliothek kompiliert werden. Der CDI-Standard gibt lediglich vor, wie die Funktionsprototypen aussehen müssen, aber nicht wie diese implementiert werden, denn das ist ja von Betriebssystem zu Betriebssystem unterschiedlich.

Ein Link zur Dokumentation der Funktionsprototypen, Strukturen, Enumerationen, usw. ist in dem [Absatz Weblinks](#weblinks) zu finden.

## Module

CDI definiert in seinen Modulen Schnittstellen für unterschiedliche Geräteklassen. Derzeit existieren die folgenden Module:

- **core**: Kernfunktionalität von CDI
- **net**: Netzwerk (vorhandene Treiber: rtl8139, sis900, pcnet, e1000)
- **fs**: Dateisysteme (vorhandene Treiber: ext2, ramdisk)
- **storage**: Massenspeicher (vorhandene Treiber: floppy, ata)

Ein Betriebssystem muss dabei nicht zwingend die Schnittstellen aller Module implementieren. Alle Treiber benutzen Funktionen aus *core*, aber es ist ohne weiteres möglich, z.B. neben *core* nur die Schnittstelle für Netzwerktreiber zu implementieren.

## Aufbau eines typischen Treibers

Zunächst eine Vorbemerkung: CDI wurde erstmals in tyndur implementiert, das nach wie vor das Referenzsystem für CDI darstellt. tyndur ist ein Mikrokernelsystem und aus diesem Grund liegt gelegentlich in Erklärungen die Annahme vor, dass ein Treiber ein eigenständiges Programm ist. CDI funktioniert aber auch mit einem monolithischen Kernel, aus der main-Funktion wird dann eine gewöhnliche Funktion, die zur Initialisierung des Treibers aufgerufen wird.

Sobald diese Funktion aufgerufen wird, registriert sie Datenstrukturen zur Beschreibung des Treibers bei CDI und führt die Initialisierung des Treibers durch. Im Allgemeinen werden dabei Geräte erkannt (z.B. auf dem PCI-Bus) und wiederum bei CDI registriert. Anschließend wird als letzte Aktion im Hauptprogramm die Funktion *cdi_run_drivers* aufgerufen, die bei einem Mikrokernelkonzept die Kontrolle an CDI übergibt und bei einem Monolithen im Allgemeinen leer ist und damit zum Kernel zurückkehrt, der die Treiberinitialisierung aufgerufen hat.

Der Treiber kommt ab diesem Zeitpunkt nur noch über Callbacks ins Spiel. Die Datenstrukturen zur Registrierung des Treibers enthalten Funktionspointer, die von CDI aufgerufen, wenn vom Treiber eine Aktion nötig ist. Das kann beispielsweise sein, wenn ein Interrupt für den Treiber eingetroffen ist oder wenn der Netzwerktreiber ein Ethernet-Paket versenden soll.

## Betriebssysteme welche CDI benutzen

- [meinOS](https://github.com/lowlevel-eu/wiki/wiki/MeinOS "MeinOS")
- [planlOS](https://github.com/lowlevel-eu/wiki/wiki/PlanlOS "PlanlOS")
- [tyndur](https://github.com/lowlevel-eu/wiki/wiki/T%C3%BDndur "Tyndur")

## Weblinks

- [Aktuell-gehaltene Dokumentation der CDI-Header-Files von tyndur](http://lpt.tyndur.org/cdi)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/3806/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1622/index.html)

<!-- MediaWiki page 1622; revision 3806; parent 3805; 2009-01-02T16:57:32Z -->
