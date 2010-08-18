# NiwohlOS/Deep inside

Diese Seite ist ein Artikel, welcher **mehr** haben könnte..  

Wenn du mehr darüber weißt oder recherchieren willst, bist **du** aufgerufen, dies zu tun. Wenn du dir in einer Sache nicht sicher bist, dann stell es auf die Diskussionsseite.

Dieser Artikel gibt einen (sehr) tiefen Einblick und gnadenlos detaillierten sowie aufschlussreichen Einblick in die tiefen Unweiten der Arbeitsweise von niwohlOS. Eventuelle Fragen, die dabei aufkommen, werden selbstverständlich nicht beantwortet, außer man fragt die Entwickler ganz lieb und nett (niwohlos nett versteht sich) im euIRC-Channel \#niwohlos.

  

# Am Anfang stand das Laden

Wie jedes Betriebssystem will auch niwohlOS erst einmal in den Arbeitsspeicher geladen werden. Da wir eine duale Entwicklung von 32-Bit- und 64-Bit-Kernel für x86 sowie für ARM-Prozessoren betreiben bedienen wir uns eines Zwischenloaders. Aber der Reihe nach:

## Phase I: GRUB

Wie überall und auch von uns empfohlen benutzen wir als Bootloader bzw. Bootmanager [GRUB](https://github.com/lowlevel-eu/wiki/wiki/Grand-Unified-Bootloader "GRUB"). Denn wir wollen ein Betriebssystem und keinen Bootloader entwickeln (Flamewars über die Abgrenzung von der Entwicklung von Bootloadern und der Entwicklung eines Betriebssystem bitte [hier](http://w3.c-plusplus.info/forum/viewforum-var-f-is-62.html) abhalten). GRUB lädt für uns folgende Dinge:

- niwohunloader, der Zwischenloader
- stoiber32, der 32-Bit-Kernel
- stoiber64, der 64-Bit-Kernel
- Diverse Module, im Moment lediglich "init"

Nach dem erfolgreichen Laden aller Module übergibt GRUB die Macht an den niwohunloader.

## Phase II: niwohunloader

Der niwohunloader ist, wie der Name schon vermuten lässt, dafür da, das Niwoh zu "entladen", also dem Computer jegliches Niwoh zu entziehen. Dazu "lädt" der niwohunloader, je nach Prozessor-Bus-Breite (sprich: 32 oder 64 Bit) entweder stoiber32 oder stoiber64. Dafür bereitet der niwohunloader auch dementsprechend die Umgebung vor (Paging, PAE usw.) und springt dann zum von GRUB geladenen Kernel.

  

# Hallo (niwohlose) Welt!

Einer unserer beiden Kernel wurde also erfolgreich von GRUB geladen und vom niwohunloader "aufgesetzt". Nun liegt die Kontrolle vollends in der Hand des Kernels. Und damit fängt das Unheil an.

## stoiber32: Old school

Der 32-Bit-Kernel setzt erstmal ein paar interne Dinge auf, unter anderem Variablen, Structs und Arrays, die für Idle-Tasks, Anzahl der Prozessoren und Umlaute (für die [Textausgabe](https://github.com/lowlevel-eu/wiki/wiki/Textausgabe "Textausgabe")) genutzt werden.

Dann wird der Bildschirm initialisiert und stoiber32 meldet sich zu Wort. Nachdem eine neue [GDT](https://github.com/lowlevel-eu/wiki/wiki/Global-Descriptor-Table "GDT") und [IDT](https://github.com/lowlevel-eu/wiki/wiki/Interrupt-Descriptor-Table "IDT") aufgesetzt wurden wird das physische Speichermanagement initialisiert; Dazu wird die von GRUB übergebene Memory-Map der Funktion "init_pmm()" übergeben, die die weitere Initialisierung übernimmt (mehr dazu im Abschnitt "Arbeitsspeicherverwaltungsgedrisse"). Danach wird das allseits beliebte [Paging](https://github.com/lowlevel-eu/wiki/wiki/Paging "Paging") aktiviert. darauffolgend dann die [Interrups](https://github.com/lowlevel-eu/wiki/wiki/Interrupt "Interrupt") sowie der Dispatcher für unser Multitasking.

Ist bis dahin alles glatt gelaufen werden die am Anfang deaktivierten Interrupts wieder eingeschaltet und stoiber32 verkündet elegant und souverän mit einer kleinen Hommage an den Ex-Bunderpräsidentschaftskandidaten Edmund Stoiber, dass niwohlOS vollständig geladen und bisher reibungslos initialisiert wurde.

Nun wird die Unterstützung für [Symmetrische Multiprozessorsysteme](https://github.com/lowlevel-eu/wiki/wiki/Symmetrisches-Multiprozessorsystem "SMP") aktiviert (mehr dazu unter "SMP: Sado-Maschochistischer Programmcode"). Dann wird gewartet, bis auch jeder Prozessor läuft und geprüft, ob es einen Idle-Task gibt. Falls nicht brechen wir sang- und klanglos ab. Ansonsten wird es danach richtig spannend:

Wir führen mitgeladene Module aus. Ab hier tritt stoiber32 nun in den Hintergrund und die Module, allen voran **init**, übernehmen die weitere Initialisierung des Userspace.

  

## stoiber64: Do it the 64-bit way, baby

Natürlich sind wir so hochmodern und wollen auch Systeme mit mehr als 4 GB RAM unterstützen. Da niwohlOS bald auch für mehrere kleienre Projekte (wie [dieses hier](http://www.google.de/url?sa=t&source=web&cd=2&ved=0CCcQFjAB&url=http%3A%2F%2Flhc.web.cern.ch%2F&ei=ibFrTJWbDYaeOPqXtakB&usg=AFQjCNEFXB14Lj2dLlfUPJs7_5U5P-GGwQ) benutzt wird, die eventuell ein wenig mehr als 4 GB brauchen, haben wir natürlich auch eine 64-Bit-Variante entwickelt. Diese hinkt allerdings der 32-Bit-Variante hinterher aufgrund der komplexen Art und Weise, die verschiedensten Techniken, die eingesetzt werden zu programmieren.

Die Initialisierung von stoiber64 läuft daher ein wenig anders ab: Analog zu stoiber64 wird der Bildschirm initialisiert. Danach wird das Multitasking initialisiert, die IDT folgt darauf. Danach wird das phsische Speichermanagement gestartet und in einen Speicherkontext ab 0x300000 gesprungen. Danach macht stoiber64...nichts.

Paging wurde bereits im niwohunloader aktiviert, genauso wie PAE.

  

# Weblinks

- [Repository](http://git.niwohlos.de)
- [niwohunloader](http://gitorious.org/niwohlos/niwohlos/blobs/master/src/niwohunloader/niwohunloader.c)
- [stoiber32-Initialisierung](http://gitorious.org/niwohlos/niwohlos/blobs/master/src/kernel/arch/i386/init_i386.c)
- [stoiber64-Initialisierung](http://gitorious.org/niwohlos/niwohlos/blobs/master/src/kernel/arch/amd64/init_amd64.c)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/8085/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2269/index.html)

<!-- MediaWiki page 2269; revision 8085; parent 0; 2010-08-18T10:20:13Z -->
