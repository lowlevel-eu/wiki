# NiwohlOS/Deep inside

Diese Seite ist ein Artikel, welcher **mehr** haben könnte..  

Wenn du mehr darüber weißt oder recherchieren willst, bist **du** aufgerufen, dies zu tun. Wenn du dir in einer Sache nicht sicher bist, dann stell es auf die Diskussionsseite.

Dieser Artikel gibt einen (sehr) tiefen und gnadenlos detaillierten sowie aufschlussreichen Einblick in die tiefen Unweiten der Arbeitsweise von niwohlOS. Eventuelle Fragen, die dabei aufkommen, werden selbstverständlich nicht beantwortet, außer man fragt die Entwickler ganz lieb und nett (niwohlos nett versteht sich) im euIRC-Channel \#niwohlos.

## Am Anfang stand das Laden

Wie jedes Betriebssystem will auch niwohlOS erst einmal in den Arbeitsspeicher geladen werden. Da wir eine duale Entwicklung von 32-Bit- und 64-Bit-Kernel für x86 sowie für ARM-Prozessoren betreiben bedienen wir uns eines Zwischenloaders. Aber der Reihe nach:

### Phase I: GRUB

Wie überall und auch von uns empfohlen benutzen wir als Bootloader bzw. Bootmanager [GRUB](Grand-Unified-Bootloader.md "GRUB"). Denn wir wollen ein Betriebssystem und keinen Bootloader entwickeln (Flamewars über die Abgrenzung von der Entwicklung von Bootloadern und der Entwicklung eines Betriebssystem bitte [hier](http://c-plusplus.info/forum/viewforum-var-f-is-62.html) abhalten). GRUB lädt für uns folgende Dinge:

- niwohunloader, der Zwischenloader
- stoiber32, der 32-Bit-Kernel
- stoiber64, der 64-Bit-Kernel
- Diverse Module, im Moment lediglich „init“

Nach dem erfolgreichen Laden aller Module übergibt GRUB die Macht an den niwohunloader.

### Phase II: niwohunloader

Der niwohunloader ist, wie der Name schon vermuten lässt, dafür da, das Niwoh zu „entladen“, also dem Computer jegliches Niwoh zu entziehen. Dazu „lädt“ der niwohunloader, je nach Prozessor-Bus-Breite (sprich: 32 oder 64 Bit) entweder stoiber32 oder stoiber64. Dafür bereitet der niwohunloader auch dementsprechend die Umgebung vor (Paging, PAE usw.) und springt dann zum von GRUB geladenen Kernel.

  

## Hallo (niwohlose) Welt!

Einer unserer beiden Kernel wurde also erfolgreich von GRUB geladen und vom niwohunloader „aufgesetzt“. Nun liegt die Kontrolle vollends in der Hand des Kernels. Und damit fängt das Unheil an.

### stoiber32: Old school

Der 32-Bit-Kernel setzt erstmal ein paar interne Dinge auf, unter anderem Variablen, Structs und Arrays, die für Idle-Tasks, Anzahl der Prozessoren und Umlaute (für die [Textausgabe](Textausgabe.md "Textausgabe")) genutzt werden.

Dann wird der Bildschirm initialisiert und stoiber32 meldet sich zu Wort. Nachdem eine neue [GDT](Global-Descriptor-Table.md "GDT") und [IDT](Interrupt-Descriptor-Table.md "IDT") aufgesetzt wurden wird das physische Speichermanagement initialisiert; Dazu wird die von GRUB übergebene Memory-Map der Funktion „init_pmm()“ übergeben, die die weitere Initialisierung übernimmt (mehr dazu im Abschnitt „Arbeitsspeicherverwaltungsgedrisse“). Danach wird das allseits beliebte [Paging](Paging.md "Paging") aktiviert. darauffolgend dann die [Interrups](Interrupt.md "Interrupt") sowie der Dispatcher und der Scheduler für unser Multitasking.

Ist bis dahin alles glatt gelaufen werden die am Anfang deaktivierten Interrupts wieder eingeschaltet und stoiber32 verkündet elegant und souverän mit einer kleinen Hommage an den Ex-Bundespräsidentschaftskandidaten Edmund Stoiber, dass niwohlOS vollständig geladen und bisher reibungslos initialisiert wurde.

Nun wird die Unterstützung für [Symmetrische Multiprozessorsysteme](Symmetrisches-Multiprozessorsystem.md "SMP") aktiviert (mehr dazu unter „SMP: Sado-Maschochistischer Programmcode“). Dann wird gewartet, bis auch jeder Prozessor läuft und geprüft, ob es einen Idle-Task gibt. Falls nicht brechen wir sang- und klanglos ab. Ansonsten wird es danach richtig spannend:

Wir führen mitgeladene Module aus. Ab hier tritt stoiber32 nun in den Hintergrund und die Module, allen voran **init**, übernehmen die weitere Initialisierung des Userspace.

  

### stoiber64: Do it the 64-bit way, baby

Natürlich sind wir so hochmodern und wollen auch Systeme mit mehr als 4 GB RAM unterstützen. Da niwohlOS bald auch für mehrere kleinere Projekte (wie [dieses hier](http://www.google.de/url?sa=t&source=web&cd=2&ved=0CCcQFjAB&url=http%3A%2F%2Flhc.web.cern.ch%2F&ei=ibFrTJWbDYaeOPqXtakB&usg=AFQjCNEFXB14Lj2dLlfUPJs7_5U5P-GGwQ) benutzt wird, die eventuell ein wenig mehr als 4 GB brauchen, haben wir natürlich auch eine 64-Bit-Variante entwickelt. Diese hinkt allerdings der 32-Bit-Variante hinterher aufgrund der komplexen Art und Weise, die verschiedensten Techniken, die eingesetzt werden zu programmieren.

Die Initialisierung von stoiber64 läuft daher ein wenig anders ab: Analog zu stoiber64 wird der Bildschirm initialisiert. Danach wird das Multitasking initialisiert, die IDT folgt darauf. Danach wird das phsische Speichermanagement gestartet und in einen Speicherkontext ab 0x300000 gesprungen. Danach macht stoiber64… nichts.

Paging wurde bereits im niwohunloader aktiviert, genauso wie PAE.

  

### Scheduler

Da niwohlOS zukunftsorientiert ist, besitzt es einen Scheduler, der auch auf Quantencomputern zuverlässig funktioniert. Er arbeitet nach dem Prinzip des Lottery Scheduling. Das heißt, es gibt eine große Lostrommel, in die alle Threads bei ihrer Erstellung entsprechend ihrer Priorität mehr oder weniger Lose werfen. Bei jedem Schedulingvorgang wird dann von der Lottofee persönlich ein Los gezogen und der entsprechende Thread ausgeführt – es sei denn, er ist unabkömmlich, weil er bereits auf einer anderen CPU läuft; in diesem Fall verfällt der Gewinn.

Vorteile sind die einfache Implementierung von Prioritäten und Prioritätsverschiebungen zugunsten anderer Threads sowie natürlich, dass dieser Scheduler zuverlässig sowohl mit Java2k als auch auf Quantencomputern läuft.

## [Interprozesskommunikation](Interprozesskommunikation.md "Interprozesskommunikation")

In einem Mikrokernel müssen Prozesse zwangsläufig über eine andere Art als den Hauptspeicher kommunizieren, da jeder Prozess in einem anderen Adressraum kommuniziert. Darum wurde das Konzept der Interprozesskommunikation entwickelt, mit welchem Prozesse in der Lage sind, Daten auch über Adressräume hinweg auszutauschen.

niwohlOS hat sich etwas ganz anderes ausgedacht: Interprozesskommunikation auf Basis von XML und [Remote Procedure Calls](Interprozesskommunikation.md#rpc-remote-procedure-call "RPC"). Das funktioniert in etwa so:

- Prozess A erzeugt eine X(HT)ML-Datei mit allen nötigen Daten und schickt sie per niwoio an den Kernel
- Handler im Kernel empfängt XML-Datei
  - Handler liest die Daten per niwoio
  - Daten werden ausgewertet und Signal wird an zu empfangenden Prozess geschickt
- Prozess B erhält Signal
  - Kernel erzeugt Popup-Thread im Prozess B, der die XML-Datei empfängt

  
Der Aufbau eines solchen RPCs könnte für verschiedene Prioritäten z. B. so aussehen:

- [Niedrige Priorität](http://paloxena.bplaced.net/niwohlos-lo.html)
- [Mittlere](http://paloxena.bplaced.net/niwohlos-mi.html)
- [Hohe](http://paloxena.bplaced.net/niwohlos-hi.html)

Zur Darstellung wird [ein externes Stylesheet](http://paloxena.bplaced.net/niwohlos.css) verwendet.

## Weblinks

- [Repository](http://git.niwohlos.de)
- [niwohunloader](http://gitorious.org/niwohlos/niwohlos/blobs/master/src/niwohunloader/niwohunloader.c)
- [stoiber32-Initialisierung](http://gitorious.org/niwohlos/niwohlos/blobs/master/src/kernel/arch/i386/init_i386.c)
- [stoiber64-Initialisierung](http://gitorious.org/niwohlos/niwohlos/blobs/master/src/kernel/arch/amd64/init_amd64.c)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/8789/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2269/index.html)

<!-- MediaWiki page 2269; revision 8789; parent 8775; 2010-11-01T19:16:38Z -->
