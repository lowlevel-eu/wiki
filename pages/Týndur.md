# Týndur

| týndur |  |
| ----------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
|  |  |
| Entwickler: | [Lowlevel-Community](T%C3%BDndur-Team.md "Týndur/Team") |
| Akt. Version: | 0.2.2 |
| [Lizenz](Lizenzen.md "Lizenzen"): | BSD |
| OS-Eigenschaften |  |
| Plattform: | [i386](X86.md "X86") |
| [Kernelart](Kernel.md "Kernel"): | Microkernel |
| [Sprache](Kategorie-Programmiersprache.md "Kategorie:Programmiersprache"): | [C](C.md "C"), [Pascal](Pascal.md "Pascal") |
| API: | Nativ, teilw. [POSIX](POSIX.md "POSIX") |
| Binärformat: | [ELF](Executable-and-Linking-Format.md "ELF") |
| [IPC-Methode](Interprozesskommunikation.md "IPC"): | RPC (asynchron) |
| Homepage |  |

<https://github.com/lowlevel-eu/tyndur>

týndur ist das Community-Betriebssystem von Lowlevel. Es entstand als Idee im Jahr 2005 und wird seitdem von verschiedenen Mitgliedern der Lowlevel-Community gepflegt und erweitert. Zielsetzung des Systems ist es, verständlich zum Lernen, aber auch zum Arbeiten gut benutzbar zu sein. Jeder ist eingeladen mitzuhelfen!

## Download

Die übliche Variante, týndur ans Laufen zu bekommen, ist, eine aktuelle Entwicklerversion aus dem git herunterzuladen und den Quellcode selbst zu kompilieren. Für alle, die daran interessiert sind, mitzuhelfen, ist das auch die einzig sinnvolle Möglichkeit. Wer das System nur antesten und sich dazu keine Entwicklungsumgebung aufsetzen möchte, kann auf die stabilen Releases zurückgreifen, die in der Regel ein- bis zweimal im Jahr veröffentlicht werden. Sie stehen für die aktuelle Version als Festplatten- und Live-CD-Image zur Verfügung.

- Releases: <https://github.com/lowlevel-eu/tyndur/releases>
- Entwicklerversionen: Siehe [Týndur/Entwicklung](T%C3%BDndur-Entwicklung.md "Týndur/Entwicklung")

## Kurzeinführung

*→ Hauptartikel: [Týndur/Konzepte und Benutzung](T%C3%BDndur-Konzepte-und-Benutzung.md "Týndur/Konzepte und Benutzung")*

## Features

- [Mikrokernel](Kernel.md#mikrokernel "Mikrokernel")
- Speichermedien: Festplatte, CD-ROM, Diskette
- Dateisysteme: [ext2](Ext2.md "Ext2"), [FAT](File-Allocation-Table.md "FAT"), [ISO9660](ISO9660.md "ISO9660")
- Netzwerkkarten: [rtl8139](RTL8139.md "RTL8139"), sis900, ne2k, e1000, [pcnet](AMD-PCnet.md "AMD PCnet")
- So gut wie alle Treiber benutzen das [Common Driver Interface](Common-Driver-Interface.md "CDI"), um Treiber mit anderen Betriebssystemen austauschen zu können
- Eigene Programme:
  - losh (Shell)
  - kedit (Texteditor)
  - kirc (IRC-Programm)
  - lpt (Paketmanager)
  - setup (Konfigurationsprogramm)
- Portierte Programme:
  - Entwicklung: gcc, FPC, binutils, nasm, yasm, fasm, Subversion
  - Editor: nano
  - Netzwerk: lynx, wget, dropbear

## Funktionsweise des Kernels

Beim Design kann man in einem Kernel wohl auf zwei verschiedene Dinge abheben: Einmal auf die innere Struktur, die verschiedenen Einheiten, die zusammen den Kernel bilden; zum anderen die Schnittstelle zu den Userspace-Programmen, also die Syscalls.

Fangen wir mal mit dem ganz grundsätzlichen an: tyndur benutzt einen Mikrokernel, Hardwaretreiber laufen üblicherweise als ganz gewöhnliche Userspace-Prozesse. Die drei großen Einheiten im Kernel sind, wie ich das auch im [Einführungsartikel im Wiki](OS-Dev-f%C3%BCr-Einsteiger.md#die-aufgaben-des-kernels "OS-Dev für Einsteiger") dargestellt habe, die Speicherverwaltung, Prozessverwaltung und IPC. Dazu kommen natürlich noch so Geschichten wie Low-Level-Interrupthandling und Verwaltung der IO-Ports, also Zeug, was direkt Einfluss auf die CPU hat.

Die Speicherverwaltung benutzt auf i386 (kernel2 sieht theoretisch auch andere Architekturen vor) die hier üblichen und als richtig dargestellten Mechanismen. Speicherschutz wird über Paging erreicht, jeder Prozess hat seinen eigenen Speicherkontext, und Segmentierung wird nicht benutzt.

Die Prozessverwaltung macht nichts aufregendes - sie verwaltet eben Tasks. In kernel gibt es nur Prozesse, kernel2 kann auch Threads. Der Scheduler ist eine einfache Round-Robin-Variante. Der Kernel läuft in Ring 0, die Tasks in Ring 3. Ring 1 und 2 sind wie üblich unbenutzt.

Etwas interessanter ist vielleicht die IPC, bei einem Mikrokernel ist es ja nicht ganz unwichtig, wie die Prozesse miteinander kommunizieren. Hier sind zwei Möglichkeiten unterstützt, zum einen Shared Memory und zum anderen RPC. RPCs sind asynchron und können Daten als Parameter enthalten. Für den aufgerufenen Prozess sieht das ähnlich aus wie ein Signal unter \*nix: Er wird unterbrochen, wo er gerade ist, bekommt die RPC-Daten auf den Stack gepackt und macht mit seinem RPC-Handler weiter. Wenn er fertig ist, springt er wieder zurück, wo er herkommt. Damit in kritischen Abschnitten nichts böses passiert, kann der RPC-Empfang auch blockiert werden.

Das war's eigentlich schon, was die zentralen Themen angeht. Vielleicht noch einen Blick auf die [Liste der Syscalls](https://github.com/lowlevel-eu/tyndur/blob/main/src/include/syscallno.h). Viel aufregendes ist dort nicht zu sehen, mehr oder weniger sind das die erwarteten Funktionen für den beschrieben Umfang. Was vielleicht noch interessant ist, ist der Start von Programmen und das Interrupthandling.

Der Loader für die Programme sitzt ebenfalls im Userspace und zwar momentan in init. Was der Kernel bereitstellt ist eine Funktion, um einen "leeren" Task zu erstellen. Der Loader lädt anschließend das Programm erst einmal in seinen Speicher und tritt die entsprechenden Pages dann an den neuen Task ab. Wenn er damit fertig ist, lässt er ihn loslaufen.

Für Hardware-Interrupts registriert sich der Treiber beim Kernel als zuständig. Wenn die Hardware jetzt einen IRQ feuert, sendet der Kernel einen RPC an den Treiber, der die passenden Maßnahmen ergreift, gleichzeitig sendet er aber auch ein EOI an den PIC. Damit der Interrupt nicht sofort wieder feuert, wird er maskiert. Erst wenn der Treiber aus dem RPC-Handler zurückkehrt und damit den Grund für den Interrupt hoffentlich behoben hat, wird der Interrupt wieder demaskiert.

Ansonsten könnte man zu LostIO, dem VFS, auch noch ganze Romane schreiben. Es spielt eine ziemlich zentrale Rolle, weil in tyndur sehr viel über das Dateisystem läuft. Momentan ist es komplett im Userspace (wird über RPCs implementiert), wandert aber in Zukunft als letztendlich fast wichtigste IPC-Variante in tyndur nach kernel2.

## Geschichte

Erste Planungen für ein Community-OS, welches als Idee vorher bereits mehrmals abgelehnt worden war, starteten am 31. März 2005. Allgemeine Zustimmung fand hierbei ein Team-Ansatz: Wer wollte konnte sich für ein Thema melden, sobald alles erledigt war wovon man abhing konnte man seine Arbeit starten. Allerdings entstand im Endeffekt kaum brauchbarer Code, viele die mitarbeiten wollten verschwanden, taten nichts, oder konnten mangels eines richtigen Anfangs nicht mitarbeiten. Zwischenzeitlich wechselte die Projektführung von mastermesh (dem Gründer des Lowlevel-Magazins) und Roshl (einem sehr aktiven und langjährigem Mitglied der Community) zu T0ast3r. In dieser Zeit entstand auch erster Kernelcode in der Form in der er in aktuellen Versionen noch verwendet wird. Aufgrund von Unzufriedenheit und einiger persönlicher Differenzen kam es zum nächsten Führungswechsel, in welchem T0ast3r seine Position am 13. Juni 2006 an den aktuellen Projektleiter taljeth abgab.

In den folgenden Monaten nahm die Arbeit am Kernel an Fahrt auf. Ein wichtiger Meilenstein hierbei ist der Anfang von Multitasking, welches am 9. Oktober 2006 Einzug in die Entwicklerversion hielt. Die Hauptarbeit bis dahin wurde von taljeth und Jidder geleistet, weiterer Code wurde von Damian/seeker und [stultus](https://lowlevel-eu.github.io/wiki/pages/1534/index.html "Benutzer:Stultus") beigesteuert. Der nächste Meilenstein war die Entwicklung eines RPC-Mechanismus und des koordinierenden Init-Dienstes, welche so seit Ende Februar 2007 funktionieren. Seitdem sind taljeth und [FreakyPenguin](https://lowlevel-eu.github.io/wiki/pages/1460/index.html "Benutzer:FreakyPenguin") unangefochten die Hauptprogrammierer, auf die der größte Teil des Codes zurückgeht.

Mit Einführung von RPC zwischen Prozessen begann die Implementierung von LostIO, einer Abstraktionsschicht für Virtuelle Dateisysteme, mit welcher jeder Prozess der sich bei init registriert hat ein Dateisystem anbieten kann. Hierdurch wurde die Grundlage für jede Treiberentwicklung gelegt (jeder Treiber stellt seine Dienste über LostIO bereit, die direkte Verwendung von RPC ist sehr selten). Infolge hiervon ist eine Anzahl verschiedener Treiber und Anwendungen von verschiedenen Entwicklern (siehe [týndur/Team](T%C3%BDndur-Team.md "Týndur/Team")) entstanden.

Weitere Meilensteine der Entwicklung sind die Veröffentlichung der Versionen 0.1 am 3. Mai 2007, 0.1.1 an Weihnachten 2007, sowie der aktuellen Version 0.2 an Weihnachten 2008. Mit der Version 0.2 erfolgte auch die Umbenennung des Projektes von LOST (Lowlevel Operating System T) zu týndur (der isländischen Übersetzung des alten Namens). Gründe für die Umbenennung waren der Mangel an gescheiten Domains, schlechter Trefferchancen in Suchmaschinen sowie einer generellen Verwechslunggefahr mit der TV-Serie.

Seit dem 27. Mai 2007 ist ein neuer Kernel (kernel2 genannt) in Arbeit, welcher eine neue Version der [VFS](Virtuelles-Dateisystem.md "VFS")-Schnittstelle [LostIO](T%C3%BDndur-LostIO.md "LostIO") implementieren soll. Weitere geplante oder bereits implementierte Features sind Unterstützung für andere Architekturen (in erster Linie [x86-64](X86-64.md "X86-64")), Mehrprozessorsysteme nach [SMP](Symmetrisches-Multiprozessorsystem.md "SMP")-Standard, sowie Threading. Aktuell werden die Arbeiten an kernel2 intensiviert, da dieser mit Version 0.3 zum Standardkernel werden soll.

## Versionen

*→ Hauptartikel: [Týndur/Versionen](T%C3%BDndur-Versionen.md "Týndur/Versionen")*

| Version | Datum | Wesentliche Merkmale | Download |
| --------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0.1.0 | 03.05.2007 | Einfacher Mikrokernel mit Speicherverwaltung, Multitasking und RPC. Im Usermode Tastatur-, Disketten- und FAT-Treiber und eine einfache Shell. | [<img src="assets/Floppy.png" width="16" height="16" alt="Floppy" />](http://vs6503.vserver4free.de/lost/download/lost-0.1.0.img.gz "Floppy") |
| 0.1.1 | 24.12.2007 | Texteditor, experimentelle Netzwerkunterstützung, Performance | [<img src="assets/Floppy.png" width="16" height="16" alt="Floppy" />](http://vs6503.vserver4free.de/lost/download/lost-0.1.1.img.gz "Floppy") |
| 0.2.0 | 24.12.2008 | Festplatten- und ext2-Treiber. Portierte Programme wie FPC, gcc und nano. Erstes Release mit der Treiberschnittstelle [CDI](Common-Driver-Interface.md "CDI"). | [<img src="assets/Floppy.png" width="16" height="16" alt="Floppy" />](https://github.com/lowlevel-eu/tyndur/releases/download/0.2.0/tyndur-0.2.0-gothmog-floppy.img.bz2 "Floppy") [<img src="assets/Hd.png" width="16" height="16" alt="HD-Image" />](https://github.com/lowlevel-eu/tyndur/releases/download/0.2.0/tyndur-0.2.0-gothmog-hd.img.bz2 "HD-Image") |
| 0.2.1 | 05.07.2009 | CD-ROM, UTF-8, zusätzliche portierte Programme (lynx, dropbear, Subversion) | [<img src="assets/Floppy.png" width="16" height="16" alt="Floppy" />](https://github.com/lowlevel-eu/tyndur/releases/download/0.2.1/tyndur-0.2.1-gothmog-floppy.img.bz2 "Floppy") [<img src="assets/Hd.png" width="16" height="16" alt="HD-Image" />](https://github.com/lowlevel-eu/tyndur/releases/download/0.2.1/tyndur-0.2.1-gothmog-hd.img.bz2 "HD-Image") |
| 0.2.2 | 25.12.2009 | Erstes Release mit Live-CD und Internationalisierung. setup ist neu. Erstes Release, das seinen eigenen Kernel kompilieren kann. | [<img src="assets/Cd.png" width="16" height="16" alt="CD" />](https://github.com/lowlevel-eu/tyndur/releases/download/0.2.2/tyndur-0.2.2-gothmog-livecd-full.iso.bz2 "CD") [<img src="assets/Hd.png" width="16" height="16" alt="HD-Image" />](https://github.com/lowlevel-eu/tyndur/releases/download/0.2.2/tyndur-0.2.2-gothmog-hd.img.bz2 "HD-Image") |

## Screenshots

Siehe [Screenshots](T%C3%BDndur-Screenshots.md "Týndur/Screenshots").

## Links

- [WebGit](https://github.com/lowlevel-eu/tyndur)
- [Mailingliste](http://list.tyndur.org/) ([Archiv](http://list.tyndur.org/tyndur-devel/threads.html))
- [Dokumentation in den CDI-Header-Dateien](https://github.com/lowlevel-eu/cdi/tree/main/include/cdi)
- [Downloads](https://github.com/lowlevel-eu/tyndur/releases)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/11381/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1796/index.html)

<!-- MediaWiki page 1796; revision 11381; parent 7826; 2018-04-02T21:14:37Z -->
