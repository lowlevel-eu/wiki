# NiwohlOS

| niwohlOS<br>*"In God we trust – Da hilft nur noch beten"* |  |
| ----------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|  |  |
| Entwickler: | Cjreek<br>cra1n<br>[DerHartmut](https://lowlevel-eu.github.io/wiki/pages/1865/index.html "Benutzer:Hartmut")<br>[DickHuuhn](https://lowlevel-eu.github.io/wiki/pages/1871/index.html "Benutzer:DickHuuhn")<br>Paddy<br>[pocky](https://lowlevel-eu.github.io/wiki/pages/2097/index.html "Benutzer:Pocky")<br>[SHyx0rmZ](https://lowlevel-eu.github.io/wiki/pages/1785/index.html "Benutzer:SHyx0rmZ")<br>[XanClic](https://lowlevel-eu.github.io/wiki/pages/1860/index.html "Benutzer:XanClic") |
| Akt. Version: | 0.1.0 |
| [Lizenz](https://github.com/lowlevel-eu/wiki/wiki/Lizenzen "Lizenzen"): | MIT/X11 |
| OS-Eigenschaften |  |
| Plattform: | [i386](https://github.com/lowlevel-eu/wiki/wiki/X86 "X86")/[x86-64](https://github.com/lowlevel-eu/wiki/wiki/X86-64 "X64") |
| [Kernelart](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel"): | [Micro](https://github.com/lowlevel-eu/wiki/wiki/Kernel#mikrokernel "Microkernel")[monolithischer](https://github.com/lowlevel-eu/wiki/wiki/Kernel#monolithischer-kernel "Monolithischer Kernel") Modularhybrid |
| [Sprache](https://lowlevel-eu.github.io/wiki/pages/1648/index.html "Kategorie:Programmiersprache"): | C, Assembler (Syntax: Intel und Falschrum) |
| API: | POSIX (nur besser, weil noch kaputter) |
| Binärformat: | [ZWÖLF](https://github.com/lowlevel-eu/wiki/wiki/Executable-and-Linking-Format "ELF") |
| [IPC-Methode](https://github.com/lowlevel-eu/wiki/wiki/Interprozesskommunikation "IPC"): | V.O.M.I.T. (**V**erbose **O**bject-oriented **M**achine-readable **I**nformation **T**ransfer) |
| Homepage |  |

<http://gitorious.org/niwohlos>

*"Ich verstehe Ihre Frage so, dass es Benutzer gibt, die wünschen, dass wir die Entwickler von niwohlOS dazu mobilisieren, um einen Paketfilter zu implementieren. Mir ist nicht bekannt, dass eine solche Absicht besteht. Die Entwickler kooperieren zur Sicherung von niwohlOS eifrig mit dem BSI, und ihre Arbeitskraft wird dafür voll eingesetzt. Niemand hat die Absicht, eine Firewall zu errichten!"*  

-- [Linus Torvalds](https://github.com/lowlevel-eu/wiki/wiki/Linux "Linux"), der alte [Kommunist](https://github.com/lowlevel-eu/wiki/wiki/Lizenzen#gnu-general-public-license "Lizenzen"), äußert sich zu niwohlOS.

  
**niwohlOS** (Hochprofessionellisch für: Niveau-L-OS) ist ein hochmodernes Betriebssystem für die x86-Architektur. Es wird von bekannten hochprofessionellen Entwicklern aus dem [IRC](https://github.com/lowlevel-eu/wiki/wiki/IRC "IRC")-Channel \#niwohlos im euIRC entwickelt.

## Inside niwohlOS

### Bootvorgang

#### Phase Ia: GRUB

Als Bootloader wird der hochprofessionelle Bootloader [GRUB](https://github.com/lowlevel-eu/wiki/wiki/Grand-Unified-Bootloader "GRUB") verwendet. Dieser wird von zahlreichen professionellen Firmen und Betriebssystemen seit Jahren mit Erfolg eingesetzt und verspricht eine optimale Grundlage für ein jedes Betriebssystem. GRUB richtet eine standardisierte und standartisierte Umgebung ein und übergibt der zweiten Phase, dem niwohunloader alle nötigen Daten, die es brauch. Auch lädt GRUB dank hochperformanter Lademechnismen unsere beiden Kernel stoiber32 und stoiber64 in den Speicher.

#### Phase Ib: NILO

Alternativ zu GRUB kann der NIwohLOader, kurz NILO eingesetzt werden. Dieser ist ein hochperformanter und hochkomplexer multiboot-kompatibler Bootloader, mit dessen Hilfe der niwohunloader geladen wird.

#### Phase II: niwohunloader

Um dem User unnötige und komplexe Konfiguration abzunehmen wird nach dem eigentlich Bootloader ein Zwischenloader, der niwohunloader, geladen. Dieser entscheidet anhand komplexer und hochperformanter Algorithmen, welche Systemarchitektur der entsprechende Computer besitzt und lädt daraufhin alle passenden Komponenten nach. Hierdurch ist ein voll-automatisierter Ablauf des Ladeprozesses bei optimaler Perfomance und höchster Stabilität garantiert.

### Kernel

#### Allgemeines Konzept

Die Kernel sind micromonolithische Modularhybride. Im Klartext bedeutet das: niwohlOS hat monolithische Kernel, die zur Laufzeit Module einbinden können. Diese laufen dann mit speziellen Privilegien im Usermode. Dadurch kann das Grundsystem beliebig erweitert werden und auf die individuellen Bedürfnisse jedes einzelnen Users ausgerichtet werden. Gleichzeitig wird aber auch die hohe Performance und die extreme Stabilität gewährleistet. Der monolithische Teil wird so klein wie möglich gehalten, um die vorausgesetzte optimale Performance zu garantieren.

#### 32-Bit: stoiber32

Für alle Computer mit bewährten und dennoch hochperformanten 32-Bit-Prozessoren dient der 32-Bit-Kernel stoiber32. Dieser zeichnet sich durch eine hochperformante Speicherverwaltung und ein hochperformantes Multitasking aus, welches bis zu zwei Prozesse mit unglaublicher Geschwindigkeit nahezu parallel ausführen kann. Stoiber32 verfügt über ein Linux-Subsystem, mit dessen Hilfe es möglich ist, Linux-Module in den Kernel einzubinden.

#### 64-Bit: stoiber64

Hochmoderne Computer mit hochperformanten und hochkomplexen 64-Bit-Prozessoren stehen dank stoiber64 neue Möglichkeiten zur Verfügung. Der 64-Bit-Kernel verfügt über ebenfalls über eine hochperformante und auf 64-Bit-Systeme mit mehr als 4 Petabyte Arbeitsspeicher ausgelegte Speicherverwaltung, welche garantiert, dass ein Programm nie zu wenig Speicher hat, auch wenn zu wenig Speicher vorhanden ist. Win-Win-Situation wird dieses Verfahren im professionellem Umfeld genannt. Auch stoiber64 verfügt über hochperformantes Multitasking, welches ebenfalls bis zu zwei Programme nahezu gleichzeitig und in einer atemberaubenden Geschwindkeit ausführen kann.

#### Namensherkunft

Da der Kernel emmmh (ein micromonolithischer Modularhybrid) ist, wird er auch als "Stoiber" bezeichnet. Hierin soll auch das Ziel KISS (Keep it simple, stupid) zum Ausdruck kommen (in Anerkennung der Leistungen Edmund Stoibers beim Bürokratieabbau in Europa).

tl;dr: Wie Linux, nur geiler.

### Treiber

Es gibt zwei Sorten von Treibern in niwohlOS: Ring-0-Treiber und Ring-3-Treiber (oder auch Kernel- und Usertreiber). Kerneltreiber werden direkt in den Kernel miteingelinkt und laufen mit der gleichen Privilegsstufe wie der Kernel, Usertreiber können zur Laufzeit nachgeladen werden und laufen im Ring-3, also mit Privilegien, die jedes normale Programm auch besitzt. Durch eine ausgeklügelte und hochmoderne HAL, der niwohlosenHAL, können Usertreiber die gleiche Funktionalität wie Kerneltreiber nutzen, ohne jedoch bei Instabilität die Ausführung des Systems zu behindern. Durch den perfekten Mix aus extrem stabilen Kerneltreibern und hochoptimierten Usertreibern kann ein sicheres, stabiles und gleichzeitig hochperformantes System garantiert werden.

#### [Interprozesskommunikation](https://github.com/lowlevel-eu/wiki/wiki/Interprozesskommunikation "Interprozesskommunikation")

Wie es sich für jedes anständige micromonolithische Modulahybridsystem gehört, implementiert natürlich auch niwohlOS einen Mechanismus der Interprozesskommunikation. Dabei wird, inspiriert von [týndur](https://github.com/lowlevel-eu/wiki/wiki/T%C3%BDndur "Týndur"), eine abgewandelte Form des [Remote Procedure Calls](https://github.com/lowlevel-eu/wiki/wiki/Interprozesskommunikation#rpc-remote-procedure-call "Remote Procedure Call") eingesetzt: In die Kernel wird eine Untermenge eines generischen XML-Parsers implementiert, welcher XML-RPCs, welche durch Sockets übertragen werden, parst und dementsprechend an ein Eventsystem weiterleitet, welches von da aus alles weitere koordiniert.

### GUI

Wie für alle größenwahnsinnigen Systeme wird natürlich auch in der relativ jungen Entwicklungsgeschichte von niwohlOS über eine grafische Benutzeroberfläche nachgedacht. Hier soll nicht allzuviel verraten werden, nur dass wir ein System namens D.U.M.M., inspiriert von Windows-Usern, entwickeln werden.

## Die Entwickler

Das Entwicklerteam besteht aus auf dem Gebiet der Betriebssystementwicklung hocherfahrenen Informatikern mit jahrelanger Programmiererfahrung, welche sicherlich zu den zukünftigen Leistungsträgern gehören, und DickHuuhn. Die Entwickler genießen zur Zeit eine Ausbildung bei der Elite der Betriebssystementwicklung im IRC-Channel \#lost im euIRC. Durch monatelange Arbeit an dem hochkomplexen Betriebssystem [týndur](https://github.com/lowlevel-eu/wiki/wiki/T%C3%BDndur "Týndur") wissen sie, wie ein hochperfomantes und extrem stabiles System aufgebaut sein muss.

### niwohlose-developers

Die "niwohlose-developers" sind das Entwicklerteam rund um niwohlOS sowie anderen Projekten. Es besteht aus vier hochoptimierten, äh hochintelligenten Programmierern und Softwareentwicklern.

#### XanClic alias Crazy-OS-names

[XanClic](https://lowlevel-eu.github.io/wiki/pages/1860/index.html "Benutzer:XanClic") (hochkomplexes Hybridakrobackronym) ist einer der Top-Entwickler von niwohlOS. Er besitzt auf dem Gebiet der Betriebssystementwicklung höchste Kompetenzen, entwickelte er doch schon mehrere Betriebssysteme im Alleingang ([MyXomycota](https://github.com/lowlevel-eu/wiki/wiki/MyXomycota "MyXomycota"), [Paloxena](https://github.com/lowlevel-eu/wiki/wiki/Paloxena "Paloxena")) und reichte schon zahlreiche Patches für [týndur](https://github.com/lowlevel-eu/wiki/wiki/T%C3%BDndur "Týndur") ein, wie einen AC97-Treiber, USB-Treiber und die hochkomplexe libmaumau, die es den Anwendern ermöglicht, Mau-Mau zu spielen. XanClic ist für den ~~fragilen~~ soliden Aufbau, das Grundgerüst in niwohlOS zuständig.

#### DerHartmut alias TheHartmutYouHaveCalledIsTemporarilyNotAvailable

[DerHartmut](https://lowlevel-eu.github.io/wiki/pages/1865/index.html "Benutzer:Hartmut") (kein hochkomplexes Hybridakrobackronym) ist ebenfalls einer der Top-Entwickler von niwohlOS. Er besitzt jahrelange Erfahrung auf dem Gebiet der Betriebssystementwicklung und daher beste Reputationen auf diesem Gebiet. Er entwickelte ebenfalls sein eigenes Betriebssystem im Alleingang (qultics) und arbeitet an einem neuen, hochoptimierten Betriebssystem, quasi als "Hobby" neben niwohlOS. Er reichte bisher wenige, aber dafür umso wichtigere Patches bei [týndur](https://github.com/lowlevel-eu/wiki/wiki/T%C3%BDndur "Týndur") ein, darunter zwei hochperformante Interpreter für die wohl wichtigsten Sprachen im industriellen Umfeld, Malbolge und hq9+, er halb-portierte den extrem komplexen Mailclient mutt und implementierte einer der wichtigsten Features unter týndur: lpt moo. Er ist bei niwohlOS für alle ~~kaputten~~ hochoptimierten Stellen zuständig. Seine mannigfaltigen Pflichten in vielfältigen anderen Gebieten zwingen ihn allerdings bisweilen, die entsprechende Arbeit ~~monatelang~~ zeitweilig zu suspendieren.

#### SHyx0rmZ alias HardcoreProgger

[SHyx0rmZ](https://lowlevel-eu.github.io/wiki/pages/1785/index.html "Benutzer:SHyx0rmZ") (hochoptimierter Buchstabenkomplex) ist auch einer der Top-Entwickler von niwohlOS. Er programmiert seit sage und schreibe 11 Jahren und weist in diesem Feld höchste Kompetenzen auf. er wird oft als "Hardcore-Informatiker" bezeichnet, denn er schafft, was andere nicht schaffen: Er hat sein hochperformantes und hochoptimiertes Betriebssystem [Nuke](https://github.com/lowlevel-eu/wiki/wiki/Nuke "Nuke") mit gleich **drei** Kerneln ausgestattet, um aus jedem erdenklichen System die höchste Maß an Leistung herauszukitzeln. Des Weiteren schrieb er an Vortex, einem Loader, der unter anderem in qultics eingesetzt wird und womöglich von Microsoft patentiert wird. Er ist bei niwohlOS für die ganz komplexen Sachen zuständig.

#### DickHuuhn alias DickHuuhn

[DickHuuhn](https://lowlevel-eu.github.io/wiki/pages/1871/index.html "Benutzer:DickHuuhn") (kein hochkomplexes Hybridakrobackronym und auch kein hochoptimierter Buchstabenkomplex) ist ein Chiken.

  

### Die Committer

Neben dem Entwicklerteam gibt es zahlreiche hochproffessionelle Commiter, die wertvollen Code und wertvolle Ideen tagtäglich committen.

#### pocky alias 1337h4x0r

[pocky](https://lowlevel-eu.github.io/wiki/pages/2097/index.html "Benutzer:Pocky") (kein hochkomplexes Hybridakrobackronym und kein hochoptimierter Buchstabenkomplex, dafür aber der Wahrheit) ist vor allem für die noch nicht vorhandene, noch nicht geplante und wahrscheinlich auch gar nicht realsiert-werdende GUI zuständig. So ganz nebenbei ist er auch für die mooraalische Unterstützung zu gebrauchen. Er betreut also sozusagen die GUI und die Mooraale. Und die GUI.

#### Cjreek alias Sado-Masochist aka Windows-User

Cjreek (kein Mensch weiß, was das heißen soll) ist ebenfalls ein hochprofessionelle Entwickler, der zur Zeit bei einem Tierversuch teilnimmt, bei welchem getestet wird, wie sich die dauerhafte ernsthafte Nutzung von dem sogenannten "Betriebssystem" "Windows" auf Mensch und Maschine auswirkt. Er hat ebenfalls weitreichende Erfahrungen in der Betriebssystementwicklung und entwickelt den multiboot-kompatiblen Bootloader NILO, der irgendwann als Ersatz für den hochprofessionellen GRUB dienen soll.

#### Paddy alias Paddynator

Paddy (kein Mensch weiß, wer das ist) ist ein geheminisvoller Entwickler, der sich zu unserem Projekt gesellt hat. Auf einmal war er da, wie aus dem Nichts tauchte er in \#lost und \#niwohlos auf. Keiner weiß wer er ist, keiner weiß, ob er was kann. Man weiß nur, dass er was gegen kwolf zu haben scheint...

#### cra1n alias Ich-kenn-ihn-erst-zwei-Minuten-und-mach-ihn-direkt-zum-Committer

cra1n (auch hier weiß keiner, wer das ist) ist Schüler mit Informatik als Leistungskurs. Mehr weiß ich auch nicht.

  

## Frequently Asked Questions (FAQ)

Da niwohlOS so avantgardistisch ist, ist es natürlich ganz klar, dass beim durchschnittlichen Betrachter direkt einige Fragen auftauchen. Dafür muss man sich nicht schämen. Also, eigentlich doch. Aber nur ein bisschen. Für diese Leute haben wir ein praktisches FAQ aufgesetzt.

### Mal ehrlich, seid ihr eigentlich 4chan oder so?

Nein, die meisten Entwickler haben immer wesentlich mehr als vier IRC-Channels offen.

### Wie werde ich eigentlich Entwickler bei niwohlOS?

Grundsätzlich darf jeder, der genug Freizeit hat und die gewissen Portion an Wahnsinn besitzt für niwohlOS entwickeln. Man schreibt dazu einen Patch und gesellt sich in den Channel niwohlOS. Der Patch wird dann mit Sicherheit nicht angenommen und niemals commited, außer es ist ein Super-Mööögaaa-Pätsch (Diese Aussage ist Copyright © 2009 by XanClic). Ansonsten kann man sich als Committer bewerben.

### Wie bewirbt man sich als Committer?

Sag ich nicht. Könnt' ja jeder kommen. Nene.

### Was ist V.O.M.I.T.?

V.O.M.I.T. steht für "Verbose object-oriented machine-readable information transfer". Unsere besten Designer verbrachten Monate damit, ein ansprechendes und elegeantes Design für diese neue Art der Interprozesskommunikation zu entwerfen.

Dann haben wir aber doch XML-RPC genommen, weil das auch auf die Beschreibung passt.

### Ist niwohlOS in safe language geschrieben?

niwohlOS wird natürlich in C und Assembler geschrieben. Außerdem wird es einen PHP-Intepreter geben, damit wir unseren IPC-Code von Wordpress klauen können. Also kann man beruhigt sein: niwohlOS ist fast so sicher wie die Rente!

### Habt ihr eigentlich Angst vor der Konkurrenz?

Es gibt Konkurrenz?

Okay, um ehrlich zu sein: Ja, es gibt ein System. Das System heißt [PrettyOS](https://github.com/lowlevel-eu/wiki/wiki/PrettyOS "PrettyOS") (Personally retarded ethymology table-tennis, yeah, operating system (das es so heißt ist allerdings nur eine Vermutung!)) und ist ein hochoptimiertes Betriebssystem mit einigen vollkommenen Neuerungen und Innovationen. Welche wissen wir auch nicht. Achja, und dann gibt es noch diesen "týndur", aber der stellt ja eher keine Gefahr dar bei genauerer Betrachtung (und nachdem man die rosa-rote Naivitätsbrille abgenommen hat).

### Was war an der GUI nochmal so besonders?

Das Konzept der GUI ist recht simpel, denn es ist einfach nur D.U.M.M.. Da viele User bereits Erfahrung im Umganng mit D.U.M.M.-heit besitzen, haben wir uns für dieses tolle Konzept entschieden. Falls du dumm bist und darum nicht genug Erfahrung mit D.U.M.M.-heit hast, hier die Auflösung: D.U.M.M. steht für "Deutsches Userinterface mit Mauszeiger".

### Was für Tabletten nehmt ihr eigentlich? Und warum nehmt ihr nicht genug davon?

Natürlich nur \$NAMEEINESWIRKSTOFFS von \$FIRMENNAMEDERDIESENWIRKSTOFFINFORMVONTABLETTENHERSTELLT. \$WERBESPRUCH.

## Kritik

Zahlreiche professionelle Entwickler haben eine Kritik zu niwohlOS abgegeben:

- [Hochprofessioneller, neutraler, unvoreingenommener Entwickler \#1](https://lowlevel-eu.github.io/wiki/pages/1871/index.html "Benutzer:DickHuuhn"): *"Jo"*
- [Hochprofessioneller, neutraler, unvoreingenommener Entwickler \#2](https://lowlevel-eu.github.io/wiki/pages/1860/index.html "Benutzer:XanClic"): *"Super \*Applaus\*"*
- [Hochprofessioneller, neutraler, unvoreingenommener Entwickler \#3](https://lowlevel-eu.github.io/wiki/pages/1865/index.html "Benutzer:Hartmut"): *"Astrein."*
- Zufriedener Benutzer: *"Wer sind Sie, und wie sind Sie in mein Haus gekommen?"*
- Zufriedener Black Hat: *"Oh EXPLOITABLE!"*
- [ehenkes](https://lowlevel-eu.github.io/wiki/pages/2274/index.html "Benutzer:Ehenkes"): *"niwohlOS \<-- Name finde ich gut, ein Os, das sich nie Wohl fühlt..."niw" rückwärts erinnert allerdings an "win""*

  

## Fertig implementiert

Folgende Teile sind fertig implementiert:

- Repository erfolgreich angelegt
- Ausgeklügelte Verzeichnisstruktur des Quelltextes
- State-of-the-art Makefile

  

## Teilweise implementiert

Folgende Teile sind in Arbeit und schon teilweise implementiert:

- niwohunloader: Kann beide Kernel laden
- stoiber32: Kann schon Exceptions und lernt gerade [physische Speicherverwaltung](https://github.com/lowlevel-eu/wiki/wiki/Physische-Speicherverwaltung "Physische Speicherverwaltung")
- stoiber64: Kann auch schon Exceptions und lernt gerade physische Speicherverwaltung (Man könnte auch sagen: Wie stoiber32 nur [x64iger](https://github.com/lowlevel-eu/wiki/wiki/X86-64 "X64"))
- SMP: APs werden niwohlosisiert und stellen nach Anzeige einer entsprechenden Nachricht (selbstverständlich mit ẞ) blinkende ß dar (in Ermangelung eines ẞ in [Codepage 437](https://github.com/lowlevel-eu/wiki/wiki/Codepage-437 "Codepage 437")).

## To-Do

Folgende Teile müssen noch implementiert werden (einige durchgestrichene müssen noch in den master-Branch gemerget werden):

- printf gut machen
- kprintf gut machen
- vsprintf gut machen
- ~~printf mit Zahlen~~
- ~~Eine Funktion zum Ausgeben von Zahlen~~ Hexzahlen ausgeben
- ~~puts mit Zahlen~~ (nennt sich printf)
- ~~Zahlenausgabefunktion~~ Hex ausgeben
- ~~%i~~
- Professionelle Homepage (verzögert sich leider aufgrund der Schließung von Geocities)
- Geeignetes Logo ~~von 4chan klauen~~ erstellen
- Kernel
- libc.hiken
- Signifanten
- Unicode-Support (für ẞ und です)
- Programme
- Einfach alles
- SMP (in Arbeit)

  

------------------------------------------------------------------------

Disclaimer: Dieses OS ist ein **echtes** Projekt und wird von uns aktiv entwickelt. Die genauen Beschreibungen zur Performance und Stabilität im Artikel könnten allerdings von der Wirklichkeit abweichen. Theoretisch. Natürlich stehlen wir auch keinen GPL-Code von Wordpress: Bei der Herstellung dieses OS wurden keine GNUs gequält.

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/6980/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2095/index.html)

<!-- MediaWiki page 2095; revision 6980; parent 6979; 2010-01-25T20:58:07Z -->
