# TODO

## Überarbeiten

- [A20 Gate](https://github.com/lowlevel-eu/wiki/wiki/A20-Gate "A20-Gate")
- [C](https://github.com/lowlevel-eu/wiki/wiki/C "C")
- [Debugging](https://github.com/lowlevel-eu/wiki/wiki/Debugging "Debugging"): Wie kann man Debuggen? Printf/cout? bochs? qemu? vmware? Disassemblieren? Stack traces? Was tun, bevor ich im Forum/Chat frage?
- [System Management Mode](https://github.com/lowlevel-eu/wiki/wiki/System-Management-Mode "System Management Mode")
- TeeJays Tutorial (Link siehe [Diskussion:Programmable Interrupt Controller](https://lowlevel-eu.github.io/wiki/pages/1713/index.html "Diskussion:Programmable Interrupt Controller")) in den Artikel [Programmable Interrupt Controller](https://github.com/lowlevel-eu/wiki/wiki/Programmable-Interrupt-Controller "Programmable Interrupt Controller") einarbeiten
- [GRUB Installation auf einem USB-Stick](https://github.com/lowlevel-eu/wiki/wiki/GRUB-Installation-auf-einem-USB-Stick "GRUB Installation auf einem USB-Stick")

## Magazin ausschlachten

- [Ausgabe 1: Lowlevel-Grundlagen](https://github.com/lowlevel-eu/wiki/wiki/Ausgabe-1#lowlevel-grundlagen-teil-1 "Ausgabe 1")
- [Ausgabe 2: OS-Dev-Tutorial](https://github.com/lowlevel-eu/wiki/wiki/Ausgabe-2#os-dev-tutorial-teil-2 "Ausgabe 2") in [Kernel](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel") einarbeiten
- [Ausgabe 2: Lowlevel-Grundlagen](https://github.com/lowlevel-eu/wiki/wiki/Ausgabe-2#lowlevel-grundlagen-teil-2 "Ausgabe 2")
- [Ausgabe 1: Etwas Systemtheorie](https://github.com/lowlevel-eu/wiki/wiki/Ausgabe-1#etwas-systemtheorie "Ausgabe 1") -\> [Bootprozess](https://github.com/lowlevel-eu/wiki/wiki/Bootprozess-auf-x86 "Bootprozess") oder so

## Erweitern

- Screenshots von V2_OS für Ausgabe 2? siehe Diskussionsseite zu Ausgabe 2
- [Textausgabe](https://github.com/lowlevel-eu/wiki/wiki/Textausgabe "Textausgabe"): bitte-blinken-Bit bei den Attributen fehlt, iirc kann man sogar zwischen ich-will-blink-bit und normaler Farbpalette wechseln?
- [BDA](https://github.com/lowlevel-eu/wiki/wiki/BIOS-Data-Area "BDA"): Die einzelnen Felder erklären
- [Linux Artikel erweitern](https://github.com/lowlevel-eu/wiki/wiki/Linux "Linux")
- [IPC](https://github.com/lowlevel-eu/wiki/wiki/Interprozesskommunikation "IPC"): Ideen für RPC aus dem Thread im Forum
- [FAT](https://github.com/lowlevel-eu/wiki/wiki/File-Allocation-Table "FAT"): Was sind Cluster? Wie liest man Dateien?
- das [PE](https://github.com/lowlevel-eu/wiki/wiki/Microsoft-Portable-Executable-and-Common-Object-File-Format "PE")-Dateiformat erklären
- [Long Mode](https://github.com/lowlevel-eu/wiki/wiki/Long-Mode "Long Mode")
- Dateisysteme wie FAT, extfs, reiser, UDF, iso9660 usw.
- [PIC](https://github.com/lowlevel-eu/wiki/wiki/Programmable-Interrupt-Controller "PIC"): Programmierung, etc...
- Unter [physische Speicherverwaltung](https://github.com/lowlevel-eu/wiki/wiki/Speicherverwaltung#physische-speicherverwaltung "Speicherverwaltung") weitere mögliche Datenstruktur hinzufügen. (Liste)
- [SMP](https://github.com/lowlevel-eu/wiki/wiki/Symmetrisches-Multiprozessorsystem "SMP")
- [APIC](https://github.com/lowlevel-eu/wiki/wiki/Advanced-Programmable-Interrupt-Controller "APIC")
- [Local APIC](https://github.com/lowlevel-eu/wiki/wiki/Local-Advanced-Programmable-Interrupt-Controller "Local APIC")
- [I/O APIC](https://github.com/lowlevel-eu/wiki/wiki/I-O-Advanced-Programmable-Interrupt-Controller "I/O APIC")
- [DMA](https://github.com/lowlevel-eu/wiki/wiki/Direct-Memory-Access "DMA")
- [x86](https://github.com/lowlevel-eu/wiki/wiki/X86 "X86"): ~~Gescheites Diagramm zur Registerarchitektur,~~ Ergänzungen zur Handhabung von Interrupts, Eingehen auf verschiedene Befehlssätze, Verweis auf [CPUID](https://github.com/lowlevel-eu/wiki/wiki/CPUID "CPUID") zur Identifizierung.
  - Register sind größtenteils erledigt, siehe [Register](https://github.com/lowlevel-eu/wiki/wiki/Register "Register")
- ~~[CPUID](https://github.com/lowlevel-eu/wiki/wiki/CPUID "CPUID"): Die wichtigsten Kommandos (0x0 - 0x2, evtl, auch die Erweiterten von AMD) erläutern.~~
  - Größtenteils erledigt, muss man vielleicht noch vervollständigen
- [OS-Dev für Einsteiger](https://github.com/lowlevel-eu/wiki/wiki/OS-Dev-f%C3%BCr-Einsteiger "OS-Dev für Einsteiger"): Gründe für OS-Dev auflisten (Einleitung), mehr auf genaue Schritte eingehen / Leitfaden bieten, Erfahrungen einbringen, auf Userspace eingehen.
- [Register](https://github.com/lowlevel-eu/wiki/wiki/Register "Register")
- [CDI](https://github.com/lowlevel-eu/wiki/wiki/Common-Driver-Interface "CDI") Könnte bei den Funktionslisten noch eine Sortierung nach Headern vertragen, so sieht das nach so abschreckend viel aus.

## Neu erstellen

- irgendwas zu QEMU und GDB, primär wie man beides zusammen verwendet
- ~~Informationen zur [AMD PCnet](https://github.com/lowlevel-eu/wiki/wiki/AMD-PCnet "AMD PCnet") Netzwerkkarte~~

<!-- -->

- *Von [XanClic](https://lowlevel-eu.github.io/wiki/pages/1860/index.html "Benutzer:XanClic") begonnen, muss nur noch ausgebaut/korrigiert werden*

<!-- -->

- Lowlevel Optimierungsmöglichkeiten (bsp *mov eax, 0* mit *xor eax,eax* ersetzen)
- Entwicklungsumgebungen - Woraus sollte sie bestehen, welche Programme gibt es für einen Verwendungszweck - gesonderte Programmvorstellungen, vllt. Empfehlungen wären gut! Die unterschiedlichen Entwicklungsplattformen (Linux, Windows, ...) sollten schon aufgeführt sein.
  - Teilweise erledigt: [Editoren](https://github.com/lowlevel-eu/wiki/wiki/Editor "Editor") sind schon abgedeckt.
- ~~Versionsverwaltung - Pro&Kontra, welche Systeme gibt es...~~

<!-- -->

- *Muss nur noch ausgebaut werden, siehe [Kategorie:Versionsverwaltung](https://lowlevel-eu.github.io/wiki/pages/1887/index.html "Kategorie:Versionsverwaltung")*

<!-- -->

- ~~Interne Darstellung der Zahlen, Darstellungsmöglichkeiten negativer Zahlen, Aufbau von Gleitkommazahlen (IEEE)~~

<!-- -->

- *Muss noch ausgebaut werden, siehe [Binäre Datentypen](https://github.com/lowlevel-eu/wiki/wiki/Bin%C3%A4re-Datentypen "Binäre Datentypen")*

<!-- -->

- Wie funktionert eine CPU, ein Befehl, ein Maschinenzyklus, ein Interrupt? Alles, was an den Universitäten im Laufe von 2-4 Semestern gelehrt wird, in 5 Absätzen mit einer prise Humor und garniert mit bunten Struktogrammen.
- Datenblätter lesen und verstehen! Was tun, wenn das Internet kaputt gegangen ist, und man keine Codebeispiele zum Abtippen hat? (Zum Anfang vielleicht die Datenblätter von [PIC](https://github.com/lowlevel-eu/wiki/wiki/Programmable-Interrupt-Controller "PIC"), [PIT](https://github.com/lowlevel-eu/wiki/wiki/Programmable-Interval-Timer "PIT") und die Intel Manuals. Dann knackigere Sachen wie Netzwerkkarten, Soundkarten, ATA, ... was weiß ich.)
- Hier kommt dein Wunsch hin ;)

  
Siehe auch: Gewünschte Seiten \| Gewünschte Kategorieseiten

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/5819/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1518/index.html)

<!-- MediaWiki page 1518; revision 5819; parent 5703; 2009-08-31T18:47:20Z -->
