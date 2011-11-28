# TODO

Das Wiki braucht dringend einen neuen Kategorienbaum. Manche Artikel kann man im Moment wirklich nicht vernünftig kategorisieren. Alles nur nach [Kategorie:Glossar](https://lowlevel-eu.github.io/wiki/pages/1461/index.html "Kategorie:Glossar") zu stopfen kann es auch nicht sein. (siehe auch [Lowlevel:Kategoriebaum](https://lowlevel-eu.github.io/wiki/pages/2148/index.html "Lowlevel:Kategoriebaum"))

**Wichtig**: Wenn ihr einen Punkt kommentieren wollt signiert euren Kommentar bitte via --\~\~\~~. Dadurch kann ein Kommentar auch einem User zugeordnet werden und eventuell via Forum oder im IRC darüber diskutiert werden. Trotzdem ist diese Seite keine vollwertige Diskussions-Seite, richtige/umfangreiche Diskussionen Bitte nach nebenan auslagern: [Diskussion:TODO](https://lowlevel-eu.github.io/wiki/pages/2185/index.html "Diskussion:TODO"). Die Punkte hier müssen auch nicht nummeriert werden da eine Verlinkung zu der zugehörigen Diskussion direkt möglich ist.

## Überarbeiten/Fehler beheben

- [GRUB#GRUB 2](https://github.com/lowlevel-eu/wiki/wiki/Grand-Unified-Bootloader#grub-2 "GRUB"): Sowohl Diskettenimage als auch CD-Image scheint nicht wirklich zu tun
- [Floppy Disk Controller](https://github.com/lowlevel-eu/wiki/wiki/Floppy-Disk-Controller "Floppy Disk Controller")

## Magazin ausschlachten

- [Ausgabe 1: Lowlevel-Grundlagen](https://github.com/lowlevel-eu/wiki/wiki/Ausgabe-1#lowlevel-grundlagen-teil-1 "Ausgabe 1")
- [Ausgabe 2: Lowlevel-Grundlagen](https://github.com/lowlevel-eu/wiki/wiki/Ausgabe-2#lowlevel-grundlagen-teil-2 "Ausgabe 2")
  - Wirklich noch notwendig? --[DerHartmut](https://lowlevel-eu.github.io/wiki/pages/1865/index.html "Benutzer:Hartmut") 09:11, 12. Mai 2011 (CEST)

## Erweitern

- ~~[ISA](https://github.com/lowlevel-eu/wiki/wiki/Industry-Standard-Architecture "ISA") Der vollständigkeit halber PnP beschreiben.~~
  - Wieso werden meine Fragen einfach entfernt? Nichtsdestotrotz: Wer braucht das wirklich, sodass es auf dieser Liste stehen muss? (Kategorie:TODO per Vorlage:TODO reicht ja) —[Clici McXan](https://lowlevel-eu.github.io/wiki/pages/1860/index.html "Benutzer:XanClic") 18:52, 3. Okt. 2010 (CEST)
  - Hab ich auf der Diskussionsseite zu ISA nicht klar erklärt warum es in heutigen PCs (der letzten \>10 Jahre) kein ISA-PnP mehr gibt? --[Erik.vikinger](https://lowlevel-eu.github.io/wiki/pages/2196/index.html "Benutzer:Erik.vikinger") 09:43, 4. Okt. 2010 (CEST)
- [Long Mode](https://github.com/lowlevel-eu/wiki/wiki/Long-Mode "Long Mode")
- [Linux](https://github.com/lowlevel-eu/wiki/wiki/Linux "Linux") - Mache ich, Themen: Wie der Kernel funktioniert etc. --[DerHartmut](https://lowlevel-eu.github.io/wiki/pages/1865/index.html "Benutzer:Hartmut") 18:03, 3. Okt. 2010 (CEST)
- [Windows](https://github.com/lowlevel-eu/wiki/wiki/Windows "Windows") - Mache ich, Themen: Wie der Kernel funktioniert etc. --[DerHartmut](https://lowlevel-eu.github.io/wiki/pages/1865/index.html "Benutzer:Hartmut") 18:03, 3. Okt. 2010 (CEST)
  - Finde ich vom Inhalt her ausreichend --[DesL](https://lowlevel-eu.github.io/wiki/pages/1770/index.html "Benutzer:Dem epOS sein Linus") 04:10, 13. Okt. 2010 (CEST)
- [SMP](https://github.com/lowlevel-eu/wiki/wiki/Symmetrisches-Multiprozessorsystem "SMP")
- [APM](https://github.com/lowlevel-eu/wiki/wiki/Advanced-Power-Management "APM")
- [APIC](https://github.com/lowlevel-eu/wiki/wiki/Advanced-Programmable-Interrupt-Controller "APIC")
- [Cross-Compiler](https://github.com/lowlevel-eu/wiki/wiki/Cross-Compiler "Cross-Compiler"): aus irgendeinem Grund ist hier der i\*86 Teil weggefallen
- [Mathematischer Koprozessor](https://github.com/lowlevel-eu/wiki/wiki/Mathematischer-Koprozessor "Mathematischer Koprozessor") - Programmierung, Einsatz im OS-Dev
  - FPU wird bei OS-Dev eher weniger als bei anderer Programmierung eingesetzt, oder? Korrekter wäre vielleicht, wie man math.h-Funktionen implementiert, aber das sollte man imho auch per Intelmanual rausfinden können… —[Clici McXan](https://lowlevel-eu.github.io/wiki/pages/1860/index.html "Benutzer:XanClic") 18:32, 3. Okt. 2010 (CEST)
    - Aber der Kernel muss den Zustand von FPU (und auch SSE/AVX/...) manuell sichern, da aber nicht jeder Prozess überhaupt Zugriff auf die FPU benötigt gibt es da ja einige Beschleunigungstricks wo der Kernel von der CPU drauf hingewiesen wird dann jetzt doch mal zu sichern. Ich denke das es nicht schaden würde dazu mal ein paar Sätze zu erklären, das dahinter stehende Konzept ergibt sich nämlich nicht so einfach aus den Intel-Manuals. --[Erik.vikinger](https://lowlevel-eu.github.io/wiki/pages/2196/index.html "Benutzer:Erik.vikinger") 10:43, 21. Nov. 2011 (CET)
- [Troubleshooting](https://github.com/lowlevel-eu/wiki/wiki/Erste-Hilfe "Troubleshooting") Themen siehe [Diskussion:Erste_Hilfe](https://lowlevel-eu.github.io/wiki/pages/2264/index.html "Diskussion:Erste Hilfe")
- [IPC](https://github.com/lowlevel-eu/wiki/wiki/Interprozesskommunikation "IPC"): Ideen für RPC aus dem Thread im Forum
  - Welcher Thread? Der hier: [http://forum.lowlevel.eu/index.php?topic=1787.0](https://lowlevel-eu.github.io/forum/topics/1787/index.html) Steht im Artikel unter Links.
    - Ja. Wobei bei den 4 Möglichkeiten von bluecode noch eine fehlt: der Thread der einen/mehrere Service(s) anbieten will wartet (blockierend per Syscall) einfach auf ankommende Anfragen, so ähnlich wie bei TCP-Server-Sockets. Die Anfrage könnte dann entweder im Thread selber bearbeitet werden (womit dann keine weiteren Anfragen parallel bearbeitet werden können) oder es wird ein Worker-Thread erstellt/aktiviert (wobei dann die Variante mit den OS-gemanagten-PopUp-Threads wieder interessanter klingt weil damit im Service eine Ebene weg fällt).
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
- [x86-64](https://github.com/lowlevel-eu/wiki/wiki/X86-64 "X86-64"): SSE und FPU Register in [FPU (x86)](https://github.com/lowlevel-eu/wiki/wiki/FPU-%28x86%29 "FPU (x86)") und [SSE](https://github.com/lowlevel-eu/wiki/wiki/Streaming-SIMD-Extensions "SSE") oder so verschieben
- [AMD PCnet](https://github.com/lowlevel-eu/wiki/wiki/AMD-PCnet "AMD PCnet")
- ~~Interne Darstellung der Zahlen, Darstellungsmöglichkeiten negativer Zahlen, Aufbau von Gleitkommazahlen (IEEE)~~

<!-- -->

- *Muss noch ausgebaut werden, siehe [Binäre Datentypen](https://github.com/lowlevel-eu/wiki/wiki/Bin%C3%A4re-Datentypen "Binäre Datentypen")*

<!-- -->

- - Little/Big Endian
- [VFS](https://github.com/lowlevel-eu/wiki/wiki/Virtuelles-Dateisystem "VFS") - Mach ich demnächst. --[DesL](https://lowlevel-eu.github.io/wiki/pages/1770/index.html "Benutzer:Dem epOS sein Linus") 04:10, 13. Okt. 2010 (CEST)
  - Habe die Baum-Implementation eingebaut, wer was anderes sehen will soll es einbauen. --[DesL](https://lowlevel-eu.github.io/wiki/pages/1770/index.html "Benutzer:Dem epOS sein Linus") 15:00, 13. Okt. 2010 (CEST)
- [ISO9660](https://github.com/lowlevel-eu/wiki/wiki/ISO9660 "ISO9660") - Scheint ganz unten etwas zu fehlen.
- [Ext2](https://github.com/lowlevel-eu/wiki/wiki/Ext2 "Ext2"): Zu einem richtigen Artikel ausbauen und anschließend den Interwiki-Link von osdev.org zu uns setzen
- [ELF](https://github.com/lowlevel-eu/wiki/wiki/Executable-and-Linking-Format "ELF") ist eine ziemliche Tabellenwüste. Ich würde mir eine Erklärung wünschen, wofür jeder der drei Typen gut ist, und wie man grob vorgeht, um ein Programm (ggf. mit Shared Libs) zu starten oder ein Kernelmodul zu laden.
- [Debugging](https://github.com/lowlevel-eu/wiki/wiki/Debugging "Debugging"):
  - Stacktrace erwähnen/erklären, vllt. mit Beispielcode
  - Tricks und Kniffe von [\[1\]](http://wiki.osdev.org/Troubleshooting) übernehmen - vorallem sowas wie \_\_LINE\_\_, \_\_FILE\_\_ für Debugausgaben wären da wichtig.
- [L4](https://github.com/lowlevel-eu/wiki/wiki/L4 "L4") - [L4](http://de.wikipedia.org/wiki/L4_%28Microkernel%29) eine moderne zukunftsträchtige Mikrokernelspezifikation.

Könnt ich immerhin machen. L4 ist schließlich mein Lieblingskernel. --[Sannaj](https://lowlevel-eu.github.io/wiki/pages/2479/index.html "Benutzer:Sannaj") 20:47, 21. Nov. 2011 (CET)

## Kleinigkeiten

- Interwiki links zu *OSDev.org*: Seiten ohne Links zu anderen Sprachen
- [I/O APIC](https://github.com/lowlevel-eu/wiki/wiki/I-O-Advanced-Programmable-Interrupt-Controller "I/O APIC"): Beschreibung des INIT Delivery Modes
- [Parallele Schnittstelle](https://github.com/lowlevel-eu/wiki/wiki/Parallele-Schnittstelle "Parallele Schnittstelle"): Erklären, wie man damit Daten Sendet.
- [Crosscompiler für Windows](https://github.com/lowlevel-eu/wiki/wiki/Crosscompiler-f%C3%BCr-Windows "Crosscompiler für Windows") verschieben nach \[\[Cross-Compiler-Download mit gewätziger Anleitung\]\] oder so

## Neu erstellen

- [GUID-Partitionierungsschema](http://de.wikipedia.org/wiki/GUID_Partition_Table)
- [EFI](http://de.wikipedia.org/wiki/Extensible_Firmware_Interface)
- [ReiserFS](https://github.com/lowlevel-eu/wiki/wiki/ReiserFS "ReiserFS")

siehe [Diskussion:TODO#ReiserFS](https://lowlevel-eu.github.io/wiki/pages/2185/index.html#ReiserFS "Diskussion:TODO")

- btrfs
- Ext
- UDF
- [EHCI](https://github.com/lowlevel-eu/wiki/wiki/Enhanced-Host-Controller-Interface "EHCI")
- [xHCI](https://github.com/lowlevel-eu/wiki/wiki/Extensible-Host-Controller-Interface "XHCI")
- [ACPI](https://github.com/lowlevel-eu/wiki/wiki/Advanced-Configuration-and-Power-Interface "ACPI")
- Entwicklungsumgebungen - Woraus sollte sie bestehen, welche Programme gibt es für einen Verwendungszweck - gesonderte Programmvorstellungen, vllt. Empfehlungen wären gut! Die unterschiedlichen Entwicklungsplattformen (Linux, Windows, ...) sollten schon aufgeführt sein.
  - Teilweise erledigt: [Editoren](https://github.com/lowlevel-eu/wiki/wiki/Editor "Editor") sind schon abgedeckt.
- Wie funktionert eine CPU, ein Befehl, ein Maschinenzyklus, ein Interrupt? Alles, was an den Universitäten im Laufe von 2-4 Semestern gelehrt wird, in 5 Absätzen mit einer prise Humor und garniert mit bunten Struktogrammen.
- Datenblätter lesen und verstehen! Was tun, wenn das Internet kaputt gegangen ist, und man keine Codebeispiele zum Abtippen hat? (Zum Anfang vielleicht die Datenblätter von [PIC](https://github.com/lowlevel-eu/wiki/wiki/Programmable-Interrupt-Controller "PIC"), [PIT](https://github.com/lowlevel-eu/wiki/wiki/Programmable-Interval-Timer "PIT") und die Intel Manuals. Dann knackigere Sachen wie Netzwerkkarten, Soundkarten, ATA, ... was weiß ich.)

Was meinst du damit? Soll das eine Anleitung werden, wie man Datenblätter ließt oder Primär eine Liste mit allen Datenblättern als Links? Programm Noob 14:53, 7. Jan. 2010 (CET)

Eine Anleitung, Links zu Datenblättern sind bei den Artikeln weit besser aufgehoben

- Variable Sektor-Größen bei Massenspeichern (Block-Devices). Dafür dürfte sich wohl kein eigener Artikel lohnen aber es sollte in einigen Artikeln berücksichtigt werden, z.B. könnten sich einige Dateisystem-Strukturen ändern wenn sie auf größere Sektoren "skaliert" werden (zumindest bei den komplexeren Dateisystemen, also nicht bei FAT). Auch müsste ein OS mit verschiedenen Sektorgrößen von verschiedenen Massenspeichern gleichzeitig umgehen können. "Variabel" deshalb weil ich nicht glaube, das wenn die HDD-Hersteller erst mal damit angefangen haben an der Sektorgröße zu drehen, das dann bei 4k wieder Schluss ist. --[Erik.vikinger](https://lowlevel-eu.github.io/wiki/pages/2196/index.html "Benutzer:Erik.vikinger") 18:40, 16. Apr. 2010 (CEST)
- Java, z.B wie der Bytecode aussieht oder eine VM funktioniert --[Bjork](https://lowlevel-eu.github.io/wiki/pages/2155/index.html "Benutzer:Bjork") 21:30, 8. Jan. 2011 (CET)

Was ich wohl demnächst eh machen wollte, ist ein kleiner Kernel in Java (nativ Kompiliert) incl Wiki-Artikel. Ich kann da wohl wenns passt deinen Vorschlag mit einbauen. --[DesL](https://lowlevel-eu.github.io/wiki/pages/1770/index.html "Benutzer:Dem epOS sein Linus") 12:24, 30. Mär. 2011 (CEST)

Ein Kernel in Java? Interessante Sache, wäre echt nett, wenn du dazu ein wenig schreiben könntest.--[Bjork](https://lowlevel-eu.github.io/wiki/pages/2155/index.html "Benutzer:Bjork") 21:27, 31. Mär. 2011 (CEST)

Würd mich auch mal interessieren. --[Sfan](https://lowlevel-eu.github.io/wiki/pages/2378/index.html "Benutzer:Sfan") 08:27, 3. Apr. 2011 (CEST)

- Andere Prozessorachitekturen (Man braucht ja nicht gleich einen Kernel dazu schreiben.) --[Sannaj](https://lowlevel-eu.github.io/wiki/pages/2479/index.html "Benutzer:Sannaj") 20:34, 23. Nov. 2011 (CET)

siehe [Diskussion:TODO#Andere Architekturen](https://lowlevel-eu.github.io/wiki/pages/2185/index.html#Andere_Architekturen "Diskussion:TODO")

- Hier kommt dein Wunsch hin ;)

## Diskussionen, die sich noch nicht erledigt haben

- siehe Liste der Diskussionsseiten

Siehe auch: Gewünschte Seiten \| Gewünschte Kategorieseiten \| Seiten, die die TODO-Vorlage verwenden \| [Stubs](https://lowlevel-eu.github.io/wiki/pages/1618/index.html "Kategorie:Stub")

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/10338/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1518/index.html)

<!-- MediaWiki page 1518; revision 10338; parent 10336; 2011-11-28T17:03:23Z -->
