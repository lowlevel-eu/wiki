# NiwohlOS

| niwohlOS |  |
| ----------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|  |  |
| Entwickler: | [DerHartmut](https://lowlevel-eu.github.io/wiki/pages/1865/index.html "Benutzer:Hartmut")<br>[DickHuuhn](https://lowlevel-eu.github.io/wiki/pages/1871/index.html "Benutzer:DickHuuhn")<br>[SHyx0rmZ](https://lowlevel-eu.github.io/wiki/pages/1785/index.html "Benutzer:SHyx0rmZ")<br>[XanClic](https://lowlevel-eu.github.io/wiki/pages/1860/index.html "Benutzer:XanClic") |
| Akt. Version: | 0.1.0 |
| [Lizenz](https://github.com/lowlevel-eu/wiki/wiki/Lizenzen "Lizenzen"): | MIT/X11 |
| OS-Eigenschaften |  |
| Plattform: | [i386](https://github.com/lowlevel-eu/wiki/wiki/X86 "X86")/[x86-64](https://github.com/lowlevel-eu/wiki/wiki/X86-64 "X64") |
| [Kernelart](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel"): | [Micro](https://github.com/lowlevel-eu/wiki/wiki/Kernel#mikrokernel "Microkernel")[monolithischer](https://github.com/lowlevel-eu/wiki/wiki/Kernel#monolithischer-kernel "Monolithischer Kernel") Modularhybrid |
| [Sprache](https://lowlevel-eu.github.io/wiki/pages/1648/index.html "Kategorie:Programmiersprache"): | C, Assembler (Intel und AT&T) |
| API: | POSIX |
| Binärformat: | [ELF](https://github.com/lowlevel-eu/wiki/wiki/Executable-and-Linking-Format "ELF") |
| [IPC-Methode](https://github.com/lowlevel-eu/wiki/wiki/Interprozesskommunikation "IPC"): | \- |
| Homepage |  |

<http://gitroious.org/niwohlos>

**niwohlOS** ist ein hochmodernes Betriebssystem für die x86-Architektur. Es wird von bekannten hochprofessionellen Entwicklern aus dem [IRC](https://github.com/lowlevel-eu/wiki/wiki/IRC "IRC")-Channel \#niwohlos im euIRC entwickelt.

  

## Inside niwohlOS

### Loader

Als Bootloader wird der hochprofessionelle Bootloader [GRUB](https://github.com/lowlevel-eu/wiki/wiki/Grand-Unified-Bootloader "GRUB") verwendet. Dieser wird von zahlreichen professionellen Firmen und Betriebssystemen seit Jahren mit Erfolg eingesetzt und verspricht eine optimale Grundlage für ein jedes Betriebssystem. Um dem User unnötige und komplexe Konfiguration abzunehmen wird nach dem eigentlich Bootloader ein Zwischenloader, der niwohloseloader, geladen. Dieser entscheidet anhand komplexer und hochperformanter Algorithmen, welches Systemarchitektur Ihr Computer besitzt und lädt daraufhin alle passenden Komponenten nach. Damit ist ein voll-automatisierter Ablauf des Ladeprozesses bei optimaler Perfomance und höchstes Stabilität garantiert.

### Kernel

Der Kernel ist ein micromonolithischer Modularhybrid. Im Klartext bedeutet das: niwohlOS hat einen monolithischen Kernel, der zur Laufzeit Module einbinden kann. Diese laufen dann mit speziellen Privilegien im Usermode. Dadurch kann das Grundsystem beliebig erweitert werden und auf die individuellen Bedürfnisse jedes einzelnen Users ausgerichtet werden. Gleichzeitig wird aber auch die hohe Performance und die extreme Stabilität gewährleistet. Der monolithische Teil wird so klein wie möglich gehalten, um die vorausgesetzte optimale Performance zu garantieren.

### Treiber

Es gibt zwei Sorten von Treibern in niwohlOS: Ring-0-Treiber und Ring-3-Treiber (oder auch Kernel- und Usertreiber). Kerneltreiber werden direkt in den Kernel miteingelinkt und laufen mit der gleichen Privilegsstufe wie der Kernel, Usertreiber können zur Laufzeit nachgeladen werden und laufen im Ring-3, also mit Privilegien, die jedes normale Programm auch hat. Durch eine ausgeklügelte und hochmoderne HAL, der niwohlosenHAL, können Usertreiber die gleiche Funktionalität wie Kerneltreiber nutzen, ohne jedoch bei Instabilität das System mit instabil zu machen. Durch den perfekten Mix aus extrem stabilen Kerneltreibern und hochoptimierten Usertreibern kann ein sichere, stabiles und gleichzeitig hochperformantes System garantiert werden.

  

## Die Entwickler

Die Entwickler sind allesamt hocherfahrene Informatiker mit jahrelanger Erfahrung. Sie genießen zur Zeit eine Ausbildung bei der Elite der Betriebssystementwicklung im IRC-Channel \#lost im euIRC. Allesamt sind auf dem Gebiet der Betriebssystementwicklung hocherfahren und zählen zur Elite von Morgen. Durch monatelange Arbeit an dem hochkomplexen Betriebssystem [týndur](https://github.com/lowlevel-eu/wiki/wiki/T%C3%BDndur "Týndur") wissen sie, wie ein hochperfomantes und extrem stabiles System aufgebaut sein muss.

  

## Fertig implementiert

Folgende Teile sind fertig implementiert:

- Makefile
- Verzeichnisstruktur
- Repository

## To-Do

Folgende Teile müssen noch implementiert werden:

- niwohloserloader
- Kernel
- libc
- Programme
- Einfach alles

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/6118/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2095/index.html)

<!-- MediaWiki page 2095; revision 6118; parent 0; 2009-10-30T21:20:13Z -->
