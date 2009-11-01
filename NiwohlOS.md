# NiwohlOS

| niwohlOS<br>*"In God we trust – Da hilft nur noch beten"* |  |
| ----------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|  |  |
| Entwickler: | [DerHartmut](https://lowlevel-eu.github.io/wiki/pages/1865/index.html "Benutzer:Hartmut")<br>[DickHuuhn](https://lowlevel-eu.github.io/wiki/pages/1871/index.html "Benutzer:DickHuuhn")<br>[SHyx0rmZ](https://lowlevel-eu.github.io/wiki/pages/1785/index.html "Benutzer:SHyx0rmZ")<br>[XanClic](https://lowlevel-eu.github.io/wiki/pages/1860/index.html "Benutzer:XanClic") |
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

  
**niwohlOS** ist ein hochmodernes Betriebssystem für die x86-Architektur. Es wird von bekannten hochprofessionellen Entwicklern aus dem [IRC](https://github.com/lowlevel-eu/wiki/wiki/IRC "IRC")-Channel \#niwohlos im euIRC entwickelt.

## Inside niwohlOS

### Loader

Als Bootloader wird der hochprofessionelle Bootloader [GRUB](https://github.com/lowlevel-eu/wiki/wiki/Grand-Unified-Bootloader "GRUB") verwendet. Dieser wird von zahlreichen professionellen Firmen und Betriebssystemen seit Jahren mit Erfolg eingesetzt und verspricht eine optimale Grundlage für ein jedes Betriebssystem. Um dem User unnötige und komplexe Konfiguration abzunehmen wird nach dem eigentlich Bootloader ein Zwischenloader, der niwohunloader, geladen. Dieser entscheidet anhand komplexer und hochperformanter Algorithmen, welche Systemarchitektur der entsprechende Computer besitzt und lädt daraufhin alle passenden Komponenten nach. Hierdurch ist ein voll-automatisierter Ablauf des Ladeprozesses bei optimaler Perfomance und höchster Stabilität garantiert.

### Kernel

Der Kernel ist ein micromonolithischer Modularhybrid. Im Klartext bedeutet das: niwohlOS hat einen monolithischen Kernel, der zur Laufzeit Module einbinden kann. Diese laufen dann mit speziellen Privilegien im Usermode. Dadurch kann das Grundsystem beliebig erweitert werden und auf die individuellen Bedürfnisse jedes einzelnen Users ausgerichtet werden. Gleichzeitig wird aber auch die hohe Performance und die extreme Stabilität gewährleistet. Der monolithische Teil wird so klein wie möglich gehalten, um die vorausgesetzte optimale Performance zu garantieren.

Da der Kernel emmmh (ein micromonlithischer Modularhybrid) ist, wird er auch als "Stoiber" bezeichnet. Hierin soll auch das Ziel KISS (Keep it simple, stupid) zum Ausdruck kommen (in Anerkennung der Leistungen Edmund Stoibers beim Bürokratieabbau in Europa).

tl;dr: Wie Linux, nur geiler.

### Treiber

Es gibt zwei Sorten von Treibern in niwohlOS: Ring-0-Treiber und Ring-3-Treiber (oder auch Kernel- und Usertreiber). Kerneltreiber werden direkt in den Kernel miteingelinkt und laufen mit der gleichen Privilegsstufe wie der Kernel, Usertreiber können zur Laufzeit nachgeladen werden und laufen im Ring-3, also mit Privilegien, die jedes normale Programm auch besitzt. Durch eine ausgeklügelte und hochmoderne HAL, der niwohlosenHAL, können Usertreiber die gleiche Funktionalität wie Kerneltreiber nutzen, ohne jedoch bei Instabilität die Ausführung des Systems zu behindern. Durch den perfekten Mix aus extrem stabilen Kerneltreibern und hochoptimierten Usertreibern kann ein sicheres, stabiles und gleichzeitig hochperformantes System garantiert werden.

  

## Die Entwickler

Das Entwicklerteam besteht aus auf dem Gebiet der Betriebssystementwicklung hocherfahrenen Informatikern mit jahrelanger Programmiererfahrung, welche sicherlich zu den zukünftigen Leistungsträgern gehören, und DickHuuhn. Die Entwickler genießen zur Zeit eine Ausbildung bei der Elite der Betriebssystementwicklung im IRC-Channel \#lost im euIRC. Durch monatelange Arbeit an dem hochkomplexen Betriebssystem [týndur](https://github.com/lowlevel-eu/wiki/wiki/T%C3%BDndur "Týndur") wissen sie, wie ein hochperfomantes und extrem stabiles System aufgebaut sein muss.

### XanClic alias Crazy-OS-names

[XanClic](https://lowlevel-eu.github.io/wiki/pages/1860/index.html "Benutzer:XanClic") (hochkomplexes Hybridakrobackronym) ist einer der Top-Entwickler von niwohlOS. Er besitzt auf dem Gebiet der Betriebssystementwicklung höchste Kompetenzen, entwickelte er doch schon mehrere Betriebssysteme im Alleingang ([MyXomycota](https://github.com/lowlevel-eu/wiki/wiki/MyXomycota "MyXomycota"), [Paloxena](https://github.com/lowlevel-eu/wiki/wiki/Paloxena "Paloxena")) und reichte schon zahlreiche Patches für [týndur](https://github.com/lowlevel-eu/wiki/wiki/T%C3%BDndur "Týndur") ein, wie einen AC97-Treiber, USB-Treiber und die hochkomplexe libmaumau, die es den Anwendern ermöglicht, Mau-Mau zu spielen. XanClic ist für den soliden Aufbau, das Grundgerüst in niwohlOS zuständig.

### DerHartmut alias PageFaultHartmut

[DerHartmut](https://lowlevel-eu.github.io/wiki/pages/1865/index.html "Benutzer:Hartmut") (kein hochkomplexes Hybridakrobackronym) ist ebenfalls einer der Top-Entwickler von niwohlOS. Er besitzt jahrelange Erfahrung auf dem Gebiet der Betriebssystementwicklung und daher beste Reputationen auf diesem Gebiet. Er entwickelte ebenfalls sein eigenes Betriebssystem im Alleingang (qultics und arbeitet an einem neuen, hochoptimierten Betriebssystem, quasi als "Hobby" neben niwohlOS. Er reichte bisher wenige, aber dafür umso wichtigere Patches bei [týndur](https://github.com/lowlevel-eu/wiki/wiki/T%C3%BDndur "Týndur") ein, darunter zwei hochperformante Interpreter für die wohl wichtigsten Sprachen im industriellen Umfeld, Malbolge und h9q+, er halb-portierte den extrem komplexen Mailclient mutt und implementierte einer der wichtigsten Features unter týndur: lpt moo. Er ist bei niwohlOS für alle ~~kaputten~~ hochoptimierten Stellen zuständig.

### SHyx0rmZ alias HardcoreProgger

[SHyx0rmZ](https://lowlevel-eu.github.io/wiki/pages/1785/index.html "Benutzer:SHyx0rmZ") (hochoptimierter Buchstabenkomplex) ist auch einer der Top-Entwickler von niwohlOS. Er programmiert seit sage und schreibe 11 Jahren und weist in diesem Feld höchste Kompetenzen auf. er wird oft als "Hardcore-Informatiker" bezeichnet, denn er schafft, was andere nicht schaffen: Er hat sein hochperformantes und hochoptimiertes Betriebssystem [Nuke](https://github.com/lowlevel-eu/wiki/wiki/Nuke "Nuke") mit gleich **drei** Kerneln ausgestattet, um aus jedem erdenklichen System die höchste Maß an Leistung herauszukitzeln. Des Weiteren schrieb er an Vortex, einem Loader, der unter anderem in qultics eingesetzt wird und womöglich von Microsoft patentiert wird. Er ist bei niwohlOS für die ganz komplexen Sachen zuständig.

### DickHuuhn alias DickHuuhn

[DickHuuhn](https://lowlevel-eu.github.io/wiki/pages/1871/index.html "Benutzer:DickHuuhn") (kein hochkomplexes Hybridakrobackronym und auch kein hochoptimierter Buchstabenkomplex) ist ein Chiken.

  

## Frequently Asked Questions (FAQ)

Da niwohlOS so avantgardistisch ist, ist es natürlich ganz klar, dass beim durchschnittlichen Betrachter direkt einige Fragen auftauchen. Dafür muss man sich nicht schämen. Also, eigentlich doch. Aber nur ein bisschen. Für diese Leute haben wir ein praktisches FAQ aufgesetzt.

### Mal ehrlich, seid ihr eigentlich 4chan oder so?

Nein, die meisten Entwickler haben immer wesentlich mehr als vier IRC-Channels offen.

### Was ist V.O.M.I.T.?

V.O.M.I.T. steht für "Verbose object-oriented machine-readable information transfer". Unsere besten Designer verbrachten Monate damit, ein ansprechendes und elegeantes Design für diese neue Art der Interprozesskommunikation zu entwerfen.

Dann haben wir aber doch XML-RPC genommen, weil das auch auf die Beschreibung passt.

### Ist niwohlOS in safe language geschrieben?

niwohlOS wird natürlich in C und Assembler geschrieben. Außerdem wird es einen PHP-Intepreter geben, damit wir unseren IPC-Code von Wordpress klauen können. Also kann man beruhigt sein: niwohlOS ist fast so sicher wie die Rente!

  

## Kritik

Zahlreiche professionelle Entwickler haben eine Kritik zu niwohlOS abgegeben:

- [Hochprofessioneller, neutraler, unvoreingenommener Entwickler \#1](https://lowlevel-eu.github.io/wiki/pages/1871/index.html "Benutzer:DickHuuhn"): *"Jo"*
- [Hochprofessioneller, neutraler, unvoreingenommener Entwickler \#2](https://lowlevel-eu.github.io/wiki/pages/1860/index.html "Benutzer:XanClic"): *"Super \*Applaus\*"*
- [Hochprofessioneller, neutraler, unvoreingenommener Entwickler \#3](https://lowlevel-eu.github.io/wiki/pages/1865/index.html "Benutzer:Hartmut"): *"Astrein."*
- Zufriedener Benutzer: *"Wer sind Sie, und wie sind Sie in mein Haus gekommen?"*
- Zufriedener Black Hat: *"Oh EXPLOITABLE!"*

  

## Fertig implementiert

Folgende Teile sind fertig implementiert:

- Repository erfolgreich angelegt
- Ausgeklügelte Verzeichnisstruktur des Quelltextes
- State-of-the-art Makefile

  

## To-Do

Folgende Teile müssen noch implementiert werden:

- Professionelle Homepage (verzögert sich leider aufgrund der Schließung von Geocities)
- niwohunloader
- Kernel
- libc
- Signifanten
- Unicode-Support (für ẞ und です)
- Programme
- Einfach alles

  

------------------------------------------------------------------------

Disclaimer: Dieses OS ist ein **echtes** Projekt und wird von uns aktiv entwickelt. Die genauen Beschreibungen zur Performance und Stabilität im Artikel könnten allerdings von der Wirklichkeit abweichen. Theoretisch. Natürlich stehlen wir auch keinen GPL-Code von Wordpress: Bei der Herstellung dieses OS wurden keine GNUs gequält.

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/6148/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2095/index.html)

<!-- MediaWiki page 2095; revision 6148; parent 6140; 2009-11-01T10:08:44Z -->
