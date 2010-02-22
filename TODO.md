# TODO

## Überarbeiten

- Das Wiki braucht dringend einen neuen Kategorienbaum. Manche Artikel kann man im Moment wirklich nicht vernünftig kategorisieren. Alles nur nach [Kategorie:Glossar](https://lowlevel-eu.github.io/wiki/pages/1461/index.html "Kategorie:Glossar") zu stopfen kann es auch nicht sein. (siehe auch [Lowlevel:Kategoriebaum](https://lowlevel-eu.github.io/wiki/pages/2148/index.html "Lowlevel:Kategoriebaum"))
- [System Management Mode](https://github.com/lowlevel-eu/wiki/wiki/System-Management-Mode "System Management Mode")
- [GRUB Installation auf einem USB-Stick](https://github.com/lowlevel-eu/wiki/wiki/GRUB-Installation-auf-einem-USB-Stick "GRUB Installation auf einem USB-Stick")
- [Kernel](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel")
  - [Exokernel](https://github.com/lowlevel-eu/wiki/wiki/Kernel#exokernel "Exokernel") einarbeiten und dann redirecten
- [ISA](https://github.com/lowlevel-eu/wiki/wiki/Industry-Standard-Architecture "ISA")

## Magazin ausschlachten

- [Ausgabe 1: Lowlevel-Grundlagen](https://github.com/lowlevel-eu/wiki/wiki/Ausgabe-1#lowlevel-grundlagen-teil-1 "Ausgabe 1")
- [Ausgabe 2: Lowlevel-Grundlagen](https://github.com/lowlevel-eu/wiki/wiki/Ausgabe-2#lowlevel-grundlagen-teil-2 "Ausgabe 2")
- [Ausgabe 1: Etwas Systemtheorie](https://github.com/lowlevel-eu/wiki/wiki/Ausgabe-1#etwas-systemtheorie "Ausgabe 1") -\> [Bootprozess](https://github.com/lowlevel-eu/wiki/wiki/Bootprozess-auf-x86 "Bootprozess") oder so

## Erweitern

- [Mathematischer Koprozessor](https://github.com/lowlevel-eu/wiki/wiki/Mathematischer-Koprozessor "Mathematischer Koprozessor") - Programmierung, Einsatz im OS-Dev
- [Treiber](https://github.com/lowlevel-eu/wiki/wiki/Treiber "Treiber")
- [Linux Artikel erweitern](https://github.com/lowlevel-eu/wiki/wiki/Linux "Linux")
- [IPC](https://github.com/lowlevel-eu/wiki/wiki/Interprozesskommunikation "IPC"): Ideen für RPC aus dem Thread im Forum
- [FAT](https://github.com/lowlevel-eu/wiki/wiki/File-Allocation-Table "FAT"): Was sind Cluster? Wie liest man Dateien?
- das [PE](https://github.com/lowlevel-eu/wiki/wiki/Microsoft-Portable-Executable-and-Common-Object-File-Format "PE")-Dateiformat erklären
- [Long Mode](https://github.com/lowlevel-eu/wiki/wiki/Long-Mode "Long Mode")
- Dateisysteme wie FAT, extfs, reiser, UDF, iso9660 usw.
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
  - Liste der Hardware die sonst noch zu einem x86-System gehört
- [x86-64](https://github.com/lowlevel-eu/wiki/wiki/X86-64 "X86-64"): SSE und FPU Register in [FPU (x86)](https://github.com/lowlevel-eu/wiki/wiki/FPU-%28x86%29 "FPU (x86)") und [SSE](https://github.com/lowlevel-eu/wiki/wiki/Streaming-SIMD-Extensions "SSE") oder so verschieben
- [AMD PCnet](https://github.com/lowlevel-eu/wiki/wiki/AMD-PCnet "AMD PCnet") Netzwerkkarte
- [Floppy Disk Controller](https://github.com/lowlevel-eu/wiki/wiki/Floppy-Disk-Controller "Floppy Disk Controller")
- [Kategorie:Versionsverwaltung](https://lowlevel-eu.github.io/wiki/pages/1887/index.html "Kategorie:Versionsverwaltung")
- OSDev dür Einsteiger Serie: auf irgendwas zum Umwandeln zwischen verschiedenen Zahlensystemen verweisen
- [VFS](https://github.com/lowlevel-eu/wiki/wiki/Virtuelles-Dateisystem "VFS")

## Kleinigkeiten

- [I/O APIC](https://github.com/lowlevel-eu/wiki/wiki/I-O-Advanced-Programmable-Interrupt-Controller "I/O APIC"): Beschreibung des INIT Delivery Modes

## Neu erstellen

- irgendwas zu QEMU und GDB, primär wie man beides zusammen verwendet
  - Macht das im OS Dev überhaupt Sinn? Kann man mit GDB einen Kernel debuggen?!
    - Ob es Sinn macht, weiß ich nicht, aber ergeben tut es welchen (tut-tuuut): Ja, man kann einen Kernel debuggen. Mit qemu eben.
      - Ok. PS: Der Lok ergibt es Spaß zu pfeifen...

<!-- -->

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

- Aritkel zu Datenstrukturen:
  - Stack
  - Heap
  - Ausbau des Artikels [Speicherverwaltung](https://github.com/lowlevel-eu/wiki/wiki/Speicherverwaltung "Speicherverwaltung")
  - evtl noch kurz Datenstrukturen wie den "Binärbaum" (=binary tree) oder "Verlinkte Liste" (=linked list) erläutern?
- Artikel über [Unix](https://github.com/lowlevel-eu/wiki/wiki/Unix "Unix"). Wir sollten uns echt schämen, dass wir als OS-Entwicklungs Wiki nichts darüber haben!
  - Mit welchem Inhalt denn? --[Bluecode](https://lowlevel-eu.github.io/wiki/pages/1489/index.html "Benutzer:Bluecode") 18:27, 21. Feb. 2010 (CET)
  - Ein wenig zur Geschichte, aber hauptsächlich Internes wie zB. das VFS, das ja doch recht revolutionär war. --[Bjork](https://lowlevel-eu.github.io/wiki/pages/2155/index.html "Benutzer:Bjork") 19:44, 21. Feb. 2010 (CET)
  - Geschichte halte ich nicht für relevant. Das kann wikipedia (besser). Und VFS kommt in einen Artikel zum VFS und in keinen zu Unix.--[Bluecode](https://lowlevel-eu.github.io/wiki/pages/1489/index.html "Benutzer:Bluecode") 22:04, 21. Feb. 2010 (CET)
  - Zur Geschichte reichen ja drei, vier Zeilen. Aber ein wenig das Design von Unix sollte man dennoch beschreiben (Monolith, VFS, Syscall, viel mehr ist das ja auch nicht), da vor allem Anfäger bei der Wahl ihres Designs für ihr Betriebssystem bei den "Großen" abschauen. --[Bjork](https://lowlevel-eu.github.io/wiki/pages/2155/index.html "Benutzer:Bjork") 15:11, 22. Feb. 2010 (CET)

<!-- -->

- Hier kommt dein Wunsch hin ;)

## Diskussionen, die sich noch nicht erledigt haben

- Diskussion:Ausgabe 2
- weitere: siehe [Liste der Diskussionsseiten](http://lowlevel.brainsware.org/wiki/index.php?title=Spezial%3APr%C3%A4fixindex&from=&namespace=1)

Siehe auch: Gewünschte Seiten \| Gewünschte Kategorieseiten

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/7151/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1518/index.html)

<!-- MediaWiki page 1518; revision 7151; parent 7150; 2010-02-22T14:11:33Z -->
