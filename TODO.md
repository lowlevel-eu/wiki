# TODO

## Überarbeiten

- Das Wiki braucht dringend einen neuen Kategorienbaum. Manche Artikel kann man im Moment wirklich nicht vernünftig kategorisieren. Alles nur nach [Kategorie:Glossar](https://lowlevel-eu.github.io/wiki/pages/1461/index.html "Kategorie:Glossar") zu stopfen kann es auch nicht sein. (siehe auch [Lowlevel:Kategoriebaum](https://lowlevel-eu.github.io/wiki/pages/2148/index.html "Lowlevel:Kategoriebaum"))
- [System Management Mode](https://github.com/lowlevel-eu/wiki/wiki/System-Management-Mode "System Management Mode")
- [GRUB Installation auf einem USB-Stick](https://github.com/lowlevel-eu/wiki/wiki/GRUB-Installation-auf-einem-USB-Stick "GRUB Installation auf einem USB-Stick")
- [ISA](https://github.com/lowlevel-eu/wiki/wiki/Industry-Standard-Architecture "ISA")
- [Textausgabe](https://github.com/lowlevel-eu/wiki/wiki/Textausgabe "Textausgabe") bedarf wahrscheinlich der Überarbeitung (stilistisch)
- [Bluecode](https://lowlevel-eu.github.io/wiki/pages/1489/index.html "Benutzer:Bluecode") denkt, dass man [GRUB-Image erstellen](https://github.com/lowlevel-eu/wiki/wiki/GRUB-Image-erstellen "GRUB-Image erstellen"), GRUB-Image erstellen (Windows) und GRUB auf CD in den Artikel [GRUB](https://github.com/lowlevel-eu/wiki/wiki/Grand-Unified-Bootloader "GRUB") einarbeiten könnte

## Magazin ausschlachten

- [Ausgabe 1: Lowlevel-Grundlagen](https://github.com/lowlevel-eu/wiki/wiki/Ausgabe-1#lowlevel-grundlagen-teil-1 "Ausgabe 1")
- [Ausgabe 2: Lowlevel-Grundlagen](https://github.com/lowlevel-eu/wiki/wiki/Ausgabe-2#lowlevel-grundlagen-teil-2 "Ausgabe 2")
- ~~[Ausgabe 1: Etwas Systemtheorie](https://github.com/lowlevel-eu/wiki/wiki/Ausgabe-1#etwas-systemtheorie "Ausgabe 1") -\> [Bootprozess](https://github.com/lowlevel-eu/wiki/wiki/Bootprozess-auf-x86 "Bootprozess") oder so~~
  - [Bootprozess](https://github.com/lowlevel-eu/wiki/wiki/Bootprozess-auf-x86 "Bootprozess") enthält doch schon alle Informationen aus [Ausgabe 1: Etwas Systemtheorie](https://github.com/lowlevel-eu/wiki/wiki/Ausgabe-1#etwas-systemtheorie "Ausgabe 1"), oder übersehe ich da was?

## Erweitern

- [Heapverwaltung](https://github.com/lowlevel-eu/wiki/wiki/Heapverwaltung "Heapverwaltung"): Buddy?
- [Troubleshooting](https://github.com/lowlevel-eu/wiki/wiki/Erste-Hilfe "Troubleshooting")
  - du wolltest eine IDT/GDT laden und es gibt Exceptions? Registerdump des Emulators IDTR und GDTR (Adresse und Größe) überprüfen
  - bitte Liste erweitern
    - Mich würde viel mehr interessieren, wo man die Grenze setzt zwischen Kinderkram und interessantem/nützlichem Troubleshooting?
- [Cross-Compiler](https://github.com/lowlevel-eu/wiki/wiki/Cross-Compiler "Cross-Compiler"): aus irgendeinem Grund ist hier der i\*86 Teil weggefallen
- [Mathematischer Koprozessor](https://github.com/lowlevel-eu/wiki/wiki/Mathematischer-Koprozessor "Mathematischer Koprozessor") - Programmierung, Einsatz im OS-Dev
- [Linux Artikel erweitern](https://github.com/lowlevel-eu/wiki/wiki/Linux "Linux")
  - Was wäre denn speziell gewünscht? Über Linux könnte man halt Bücher füllen.
- [IPC](https://github.com/lowlevel-eu/wiki/wiki/Interprozesskommunikation "IPC"): Ideen für RPC aus dem Thread im Forum
  - Welcher Thread? Der hier: [http://forum.lowlevel.eu/index.php?topic=1787.0](https://lowlevel-eu.github.io/forum/topics/1787/index.html) Steht im Artikel unter Links.
    - Ja. Wobei bei den 4 Möglichkeiten von bluecode noch eine fehlt: der Thread der einen/mehrere Service(s) anbieten will wartet (blockierend per Syscall) einfach auf ankommende Anfragen, so ähnlich wie bei TCP-Server-Sockets. Die Anfrage könnte dann entweder im Thread selber bearbeitet werden (womit dann keine weiteren Anfragen parallel bearbeitet werden können) oder es wird ein Worker-Thread erstellt/aktiviert (wobei dann die Variante mit den OS-gemanagten-PopUp-Threads wieder interessanter klingt weil damit im Service eine Ebene weg fällt).
- [FAT](https://github.com/lowlevel-eu/wiki/wiki/File-Allocation-Table "FAT"): Wie liest man Dateien?
- [Long Mode](https://github.com/lowlevel-eu/wiki/wiki/Long-Mode "Long Mode")
- Dateisysteme
  - [ReiserFS](https://github.com/lowlevel-eu/wiki/wiki/ReiserFS "ReiserFS")
  - UDF
- [SMP](https://github.com/lowlevel-eu/wiki/wiki/Symmetrisches-Multiprozessorsystem "SMP")
- [APIC](https://github.com/lowlevel-eu/wiki/wiki/Advanced-Programmable-Interrupt-Controller "APIC")
  - logischer Adressierungsmodus
  - [Benutzer:Bluecode](https://lowlevel-eu.github.io/wiki/pages/1489/index.html "Benutzer:Bluecode") glaubt, dass in der SMP-Spec irgendwas dazu steht wie die PIC mit dem Zeuch verbunden ist bzw. verbunden sein kann
- irgendwo edge- vs. level-triggered Interrupts besprechen
- [x86](https://github.com/lowlevel-eu/wiki/wiki/X86 "X86")
  - Ergänzungen zur Handhabung von Interrupts
    - Was genau? Denke das gehört eher dann in [Real Mode](https://github.com/lowlevel-eu/wiki/wiki/Real-Mode "Real Mode"), [Protected Mode](https://github.com/lowlevel-eu/wiki/wiki/Protected-Mode "Protected Mode") und/oder [Long Mode](https://github.com/lowlevel-eu/wiki/wiki/Long-Mode "Long Mode")
  - Eingehen auf verschiedene Befehlssätze
    - [bluecode](https://lowlevel-eu.github.io/wiki/pages/1489/index.html "Benutzer:Bluecode") würde Vorschlagen nur auf [FPU (x86)](https://github.com/lowlevel-eu/wiki/wiki/FPU-%28x86%29 "FPU (x86)"), [MMX](https://github.com/lowlevel-eu/wiki/wiki/MultiMedia-Extension "MMX") und [SSE](https://github.com/lowlevel-eu/wiki/wiki/Streaming-SIMD-Extensions "SSE") zu verweisen
      - Das Wichtigste für uns OS-Frickler ist vielleicht, wie man die mit Multitasking kombiniert. Also wie man unnötiges Sichern/Wiederherstellen der Register vermeidet. 3DNow! wäre wohl auch noch ein Kandidat in der Liste.
        - 3DNow! ist eher bedeutungslos, von SSE überholt und wird hoffentlich nicht mehr eingesetzt, da es nur unter AMD CPUs läuft
  - Liste der Hardware die sonst noch zu einem x86-System gehört
- [x86-64](https://github.com/lowlevel-eu/wiki/wiki/X86-64 "X86-64"): SSE und FPU Register in [FPU (x86)](https://github.com/lowlevel-eu/wiki/wiki/FPU-%28x86%29 "FPU (x86)") und [SSE](https://github.com/lowlevel-eu/wiki/wiki/Streaming-SIMD-Extensions "SSE") oder so verschieben
- [AMD PCnet](https://github.com/lowlevel-eu/wiki/wiki/AMD-PCnet "AMD PCnet") Netzwerkkarte
- [Floppy Disk Controller](https://github.com/lowlevel-eu/wiki/wiki/Floppy-Disk-Controller "Floppy Disk Controller")
- [VFS](https://github.com/lowlevel-eu/wiki/wiki/Virtuelles-Dateisystem "VFS")

## Kleinigkeiten

- [I/O APIC](https://github.com/lowlevel-eu/wiki/wiki/I-O-Advanced-Programmable-Interrupt-Controller "I/O APIC"): Beschreibung des INIT Delivery Modes

## Neu erstellen

- irgendwas zu QEMU und GDB, primär wie man beides zusammen verwendet
- Entwicklungsumgebungen - Woraus sollte sie bestehen, welche Programme gibt es für einen Verwendungszweck - gesonderte Programmvorstellungen, vllt. Empfehlungen wären gut! Die unterschiedlichen Entwicklungsplattformen (Linux, Windows, ...) sollten schon aufgeführt sein.
  - Teilweise erledigt: [Editoren](https://github.com/lowlevel-eu/wiki/wiki/Editor "Editor") sind schon abgedeckt.
- ~~Interne Darstellung der Zahlen, Darstellungsmöglichkeiten negativer Zahlen, Aufbau von Gleitkommazahlen (IEEE)~~

<!-- -->

- *Muss noch ausgebaut werden, siehe [Binäre Datentypen](https://github.com/lowlevel-eu/wiki/wiki/Bin%C3%A4re-Datentypen "Binäre Datentypen")*

<!-- -->

- Wie funktionert eine CPU, ein Befehl, ein Maschinenzyklus, ein Interrupt? Alles, was an den Universitäten im Laufe von 2-4 Semestern gelehrt wird, in 5 Absätzen mit einer prise Humor und garniert mit bunten Struktogrammen.
- Datenblätter lesen und verstehen! Was tun, wenn das Internet kaputt gegangen ist, und man keine Codebeispiele zum Abtippen hat? (Zum Anfang vielleicht die Datenblätter von [PIC](https://github.com/lowlevel-eu/wiki/wiki/Programmable-Interrupt-Controller "PIC"), [PIT](https://github.com/lowlevel-eu/wiki/wiki/Programmable-Interval-Timer "PIT") und die Intel Manuals. Dann knackigere Sachen wie Netzwerkkarten, Soundkarten, ATA, ... was weiß ich.)

Was meinst du damit? Soll das eine Anleitung werden, wie man Datenblätter ließt oder Primär eine Liste mit allen Datenblättern als Links? Programm Noob 14:53, 7. Jan. 2010 (CET)

Eine Anleitung, Links zu Datenblättern sind bei den Artikeln weit besser aufgehoben

- ~~[USB](https://github.com/lowlevel-eu/wiki/wiki/Universal-Serial-Bus "USB")~~ und alles drumherum (~~[UHCI](https://github.com/lowlevel-eu/wiki/wiki/Universal-Host-Controller-Interface "UHCI")~~, [OHCI](https://github.com/lowlevel-eu/wiki/wiki/Open-Host-Controller-Interface "OHCI"), [EHCI](https://github.com/lowlevel-eu/wiki/wiki/Enhanced-Host-Controller-Interface "EHCI"), vielleicht ja auch [xHCI](https://github.com/lowlevel-eu/wiki/wiki/Extensible-Host-Controller-Interface "XHCI"))
  - Selbst eingetragen, nun löffel ich die Suppe auch selbst aus. Wer helfen kann und will, ist natürlich herzlich eingeladen! ;-) --[XanClic](https://lowlevel-eu.github.io/wiki/pages/1860/index.html "Benutzer:XanClic") 01:21, 6. Mär. 2010 (CET)
- APM, und vielleicht als Beispiel wie man damit einen PC herunterfährt
  - Wäre ACPI nicht besser? Dazu gibt es im OS-Dev-Forum immerhin ein Beispiel (dazu könnte man ja einfach einen Link im ACPI-Artikel setzen): [\[1\]](http://forum.osdev.org/viewtopic.php?f=1&t=16990&p=151565) --[XanClic](https://lowlevel-eu.github.io/wiki/pages/1860/index.html "Benutzer:XanClic") 14:47, 24. Feb. 2010 (CET)
  - Im Real Mode erledigt fehlt nur noch im Protected Mode --Thylôn 12:32, 1. Apr. 2010 (CEST)
- Mich würde mal interessieren, wie man ein Programm für das eigenen OS portiert. Also mit einer Anleitung, wie man das dan compilern muss usw. --user94 21:14, 8. Mär. 2010 (CET)
  - Wie sowas funktioniert dürfte sehr stark von Deinem OS abhängen. Allgemeine Anleitungen sind da IMHO unmöglich. --[Erik.vikinger](https://lowlevel-eu.github.io/wiki/pages/2196/index.html "Benutzer:Erik.vikinger") 17:16, 9. Mär. 2010 (CET)

Ich mein, man hat ja eine libc oder so was ähnliches. Und wie kann man damit dann z.B. [FASM](https://github.com/lowlevel-eu/wiki/wiki/Flat-Assembler "FASM") compilern? Weil da steht ja, dass man nicht viel dazu braucht.--user94 19:20, 9. Mär. 2010 (CET)

Na ja, bei FASM linkt man halt einfach die [libc-Objektdatei](http://flatassembler.net/fasm-1.69.12.tar.gz) gegen die eigene libc.a. Bei anderen Sachen ist es aber eben um einiges komplizierter und weil es bei FASM so einfach ist, denke ich nicht, dass sich da eine Seite lohnt (wogegen es bei anderen Sachen eben, wie von Erik beschrieben, zu betriebssystemspezifisch ist). --[XanClic](https://lowlevel-eu.github.io/wiki/pages/1860/index.html "Benutzer:XanClic") 20:30, 9. Mär. 2010 (CET)

- Möglicherweise lohnt es sich in jeweils einem Artikel zu beschreiben, wie man häufig verwendete Komponenten portiert. Zum Beispiel Compiler, Shells, oder Standard-Bibliotheken. lbuild ist sicherlich auch ein guter Ansatzpunkt. Weil da vermutlich keine Copy&Paste-Anleitung entstehen kann, könnte man das ganze als mehr oder weniger allgemein gehaltene Erfahrungsberichte halten, wie es sie teilweise auch auf osdev.org gibt. --Jidder 01:22, 28. Mär. 2010 (CET)

Zu Programmen die configure/make verwenden und sich an POSIX halten könnte man sicherlich ein bisschen was sagen. Aber sobald man die Anwendung wirklich ändern muss zum portieren wird es sehr schwierig.--[Bluecode](https://lowlevel-eu.github.io/wiki/pages/1489/index.html "Benutzer:Bluecode") 19:21, 1. Apr. 2010 (CEST)

- RaWrite: evtl. mit Commands usw.
- Variable Sektor-Größen bei Massenspeichern (Block-Devices). Dafür dürfte sich wohl kein eigener Artikel lohnen aber es sollte in einigen Artikeln berücksichtigt werden, z.B. könnten sich einige Dateisystem-Strukturen ändern wenn sie auf größere Sektoren "skaliert" werden (zumindest bei den komplexeren Dateisystemen, also nicht bei FAT). Auch müsste ein OS mit verschiedenen Sektorgrößen von verschiedenen Massenspeichern gleichzeitig umgehen können. "Variabel" deshalb weil ich nicht glaube, das wenn die HDD-Hersteller erst mal damit angefangen haben an der Sektorgröße zu drehen, das dann bei 4k wieder Schluss ist. --[Erik.vikinger](https://lowlevel-eu.github.io/wiki/pages/2196/index.html "Benutzer:Erik.vikinger") 18:40, 16. Apr. 2010 (CEST)
- Das neue/moderne [GUID-Partitionierungsschema](http://de.wikipedia.org/wiki/GUID_Partition_Table) könnte mal hier im Wiki berücksichtigt werden. --[Erik.vikinger](https://lowlevel-eu.github.io/wiki/pages/2196/index.html "Benutzer:Erik.vikinger") 18:40, 16. Apr. 2010 (CEST)
  - Da GUID nur eine Untermenge von EFI ist, das am besten auch. --[Dem epOS sein Linus](https://lowlevel-eu.github.io/wiki/pages/1770/index.html "Benutzer:Dem epOS sein Linus") 15:49, 19. Sep. 2010 (CEST)
- Hier kommt dein Wunsch hin ;)

## Diskussionen, die sich noch nicht erledigt haben

- Diskussion:Ausgabe 2
- weitere: siehe Liste der Diskussionsseiten

Siehe auch: Gewünschte Seiten \| Gewünschte Kategorieseiten \| Seiten, die die TODO-Vorlage verwenden \| [Stubs](https://lowlevel-eu.github.io/wiki/pages/1618/index.html "Kategorie:Stub")

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/8307/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1518/index.html)

<!-- MediaWiki page 1518; revision 8307; parent 8302; 2010-09-19T16:14:32Z -->
