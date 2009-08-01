# Common Driver Interface

**Common Driver Interface** (oder kurz **CDI**) ist ein Standard, der vom Týndur-Team entwickelt wird, und der es ermöglichen soll, betriebssystemunabhängige Treiber zu schreiben. Dies funktioniert mithilfe einer Bibliothek, die einmal für ein Betriebssystem implementiert werden muss. Dann können CDI-komforme Treiber einfach mit dieser Bibliothek kompiliert werden. Der CDI-Standard gibt lediglich vor, wie die Funktionsprototypen aussehen müssen, aber nicht wie diese implementiert werden, denn das ist ja von Betriebssystem zu Betriebssystem unterschiedlich.

Ein Link zur Dokumentation der Funktionsprototypen, Strukturen, Enumerationen, usw. ist in dem [Absatz Weblinks](#weblinks) zu finden.

## Module

CDI definiert in seinen Modulen Schnittstellen für unterschiedliche Geräteklassen. Derzeit existieren die folgenden Module:

- **core**: Kernfunktionalität von CDI
- **net**: Netzwerk (vorhandene Treiber: rtl8139, sis900, pcnet, e1000)
- **fs**: Dateisysteme (vorhandene Treiber: ext2, ramdisk)
- **storage**: Massenspeicher (vorhandene Treiber: floppy, ata)

Ein Betriebssystem muss dabei nicht zwingend die Schnittstellen aller Module implementieren. Alle Treiber benutzen Funktionen aus *core*, aber es ist ohne weiteres möglich, z.B. neben *core* nur die Schnittstelle für Netzwerktreiber zu implementieren.

### Core

Die Kernfunktionalität umfasst die folgenden Punkte:

- Verwaltung der Treiber und Geräte
- Zugriff auf I/O-Ports
- Zugriff auf Physischen Speicher
- PCI
- Verkettete Listen

### Net

Ein Neztwerktreiber muss nur eine Funktion bereitstellen um Pakete über eine Karte zu versenden:

- **send_packet**(device, buffer, size)

Die Implementierung stellt dem Treiber eine Funktion zur Verfügung um empfangene Pakete abzuliefern.

### FS

Das Interface für Dateisystemtreiber ist komplexer als bei den anderen Treibern. Hier müssen Funktionen für alle möglichen Dateioperationen zur Verfügung gestellt werden.

Um möglichst alle Dateisysteme unterstützen zu können, verfolgt CDI/FS ein etwas ungewöhnliches Konzept. Im Zentrum stehen dabei so genannte Ressourcen. Diese **Ressourcen können** Datei, Verzeichnis, Symlink, Spezialdatei oder alles gleichzeitig sein. Umgesetzt wird das mit den so genannten **Klassen**. Eine Ressource gehört zu mindestens einer Klasse (andernfalls ist sie nicht persistent). Diese Klassen beschreiben dann jeweils die verfügbaren Operationen. Es existieren momentan 4 verschiedene Klassen:

- **file**: Reguläre Datei
- **dir**: Verzeichnis
- **link**: Symbolische Verknüpfung (symlink)
- **special**: Spezialdateien

Ein Treiber kann jeweils mehrere Klassen des selben Typs anbieten, in denen unterschiedliche Funktionen eingetragen sind.

### Storage

Die Schnittstelle für Massenspeicher-Treiber ist äusserst einfach definiert. Der Treiber muss die folgenden Funktionen bereitstellen:

- **read_blocks**(device, start_block, block_count, buffer)
- **write_blocks**(device, start_block, block_count, buffer)

Diese beiden Funktionen werden von der Implementierung dazu Benutzt Sektoren zu lesen oder zu schreiben. Wieviele Sektoren ein Gerät hat, und wie gross diese sind, wird in der Device-Struktur festgelegt. Die Implementierung muss garantieren, dass die Funktion nur mit, für dieses Gerät sinnvollen, Parametern aufgerufen wird.

## Aufbau eines typischen Treibers

Zunächst eine Vorbemerkung: CDI wurde erstmals in týndur implementiert, das nach wie vor das Referenzsystem für CDI darstellt. týndur ist ein Mikrokernelsystem und aus diesem Grund liegt gelegentlich in Erklärungen die Annahme vor, dass ein Treiber ein eigenständiges Programm ist. CDI funktioniert aber auch mit einem monolithischen Kernel, aus der main-Funktion wird dann eine gewöhnliche Funktion, die zur Initialisierung des Treibers aufgerufen wird.

Sobald diese Funktion aufgerufen wird, registriert sie Datenstrukturen zur Beschreibung des Treibers bei CDI und führt die Initialisierung des Treibers durch. Im Allgemeinen werden dabei Geräte erkannt (z.B. auf dem PCI-Bus) und wiederum bei CDI registriert. Anschließend wird als letzte Aktion im Hauptprogramm die Funktion *cdi_run_drivers* aufgerufen, die bei einem Mikrokernelkonzept die Kontrolle an CDI übergibt und bei einem Monolithen im Allgemeinen leer ist und damit zum Kernel zurückkehrt, der die Treiberinitialisierung aufgerufen hat.

Der Treiber kommt ab diesem Zeitpunkt nur noch über Callbacks ins Spiel. Die Datenstrukturen zur Registrierung des Treibers enthalten Funktionspointer, die von CDI aufgerufen, wenn vom Treiber eine Aktion nötig ist. Das kann beispielsweise sein, wenn ein Interrupt für den Treiber eingetroffen ist oder wenn der Netzwerktreiber ein Ethernet-Paket versenden soll.

## Betriebssysteme welche CDI benutzen

- [meinOS](https://github.com/lowlevel-eu/wiki/wiki/MeinOS "MeinOS")
- [MyXomycota](https://github.com/lowlevel-eu/wiki/wiki/MyXomycota "MyXomycota")
- [planlOS](https://github.com/lowlevel-eu/wiki/wiki/PlanlOS "PlanlOS")
- [týndur](https://github.com/lowlevel-eu/wiki/wiki/T%C3%BDndur "Týndur")

## Weblinks

- [Aktuell-gehaltene Dokumentation der CDI-Header-Files von týndur](http://lpt.tyndur.org/cdi)
- [CDI-Treiber von týndur](http://git.tyndur.org/?p=tyndur.git;a=tree;f=src/modules/cdi)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/5009/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1622/index.html)

<!-- MediaWiki page 1622; revision 5009; parent 5001; 2009-08-01T18:26:48Z -->
