# Kategorie:Týndur

| týndur |  |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------- |
|  |  |
| Entwickler: | [Lowlevel-Community](T%C3%BDndur-Team "Týndur/Team") |
| Akt. Version: | 0.2.0 |
| [Lizenz](Lizenzen "Lizenzen"): | BSD |
| OS-Eigenschaften |  |
| Plattform: | i386 |
| [Kernelart](Kernel "Kernel"): | Microkernel |
| [Sprache](Kategorie-Programmiersprache "Kategorie:Programmiersprache"): | [C](C "C"), [Pascal](Pascal "Pascal") |
| API: | Nativ, teilw. [POSIX](POSIX "POSIX") |
| Binärformat: | [ELF](Executable-and-Linking-Format "ELF") |
| [IPC-Methode](Interprozesskommunikation "IPC"): | RPC (asynchron) |
| Homepage |  |

<http://www.tyndur.org/>

  
týndur ist das Community-Betriebssystem von Lowlevel. Es entstand als Idee im Jahr 2005 und wird seitdem von verschiedenen Mitgliedern der Lowlevel-Community gepflegt und erweitert. Zielsetzung des Systems ist es, verständlich zum Lernen, aber auch zum Arbeiten gut benutzbar zu sein. Jeder ist eingeladen mitzuhelfen!

## Geschichte

Erste Planungen für ein Community-OS, welches als Idee vorher bereits mehrmals abgelehnt worden war, starteten am 31. März 2005. Allgemeine Zustimmung fand hierbei ein Team-Ansatz: Wer wollte konnte sich für ein Thema melden, sobald alles erledigt war wovon man abhing konnte man seine Arbeit starten. Allerdings entstand im Endeffekt kaum brauchbarer Code, viele die mitarbeiten wollten verschwanden, taten nichts, oder konnten mangels eines richtigen Anfangs nicht mitarbeiten. Zwischenzeitlich wechselte die Projektführung von mastermesh (dem Gründer des Lowlevel-Magazins) und Roshl (einem sehr aktiven und langjährigem Mitglied der Community) zu T0ast3r. In dieser Zeit entstand auch erster Kernelcode in der Form in der er in aktuellen Versionen noch verwendet wird. Aufgrund von Unzufriedenheit und einiger persönlicher Differenzen kam es zum nächsten Führungswechsel, in welchem T0ast3r seine Position am 13. Juni 2006 an den aktuellen Projektleiter taljeth abgab.

In den folgenden Monaten nahm die Arbeit am Kernel an Fahrt auf. Ein wichtiger Meilenstein hierbei ist der Anfang von Multitasking, welches am 9. Oktober 2006 Einzug in die Entwicklerversion hielt. Die Hauptarbeit bis dahin wurde von taljeth und Jidder geleistet, weiterer Code wurde von Damian/seeker und [stultus](https://lowlevel-eu.github.io/wiki/pages/1534/index.html "Benutzer:Stultus") beigesteuert. Der nächste Meilenstein war die Entwicklung eines RPC-Mechanismus und des koordinierenden Init-Dienstes, welche so seit Ende Februar 2007 funktionieren. Seitdem sind taljeth und [FreakyPenguin](https://lowlevel-eu.github.io/wiki/pages/1460/index.html "Benutzer:FreakyPenguin") unangefochten die Hauptprogrammierer, auf die der größte Teil des Codes zurückgeht.

Mit Einführung von RPC zwischen Prozessen begann die Implementierung von LostIO, einer Abstraktionsschicht für Virtuelle Dateisysteme, mit welcher jeder Prozess der sich bei init registriert hat ein Dateisystem anbieten kann. Hierdurch wurde die Grundlage für jede Treiberentwicklung gelegt (jeder Treiber stellt seine Dienste über LostIO bereit, die direkte Verwendung von RPC ist sehr selten). Infolge hiervon ist eine Anzahl verschiedener Treiber und Anwendungen von verschiedenen Entwicklern (siehe [týndur/Team](T%C3%BDndur-Team "Týndur/Team")) entstanden.

Weitere Meilensteine der Entwicklung sind die Veröffentlichung der Versionen 0.1 am 3. Mai 2007, 0.1.1 an Weihnachten 2007, sowie der aktuellen Version 0.2 an Weihnachten 2008. Mit der Version 0.2 erfolgte auch die Umbenennung des Projektes von LOST (Lowlevel Operating System T) zu týndur (der isländischen Übersetzung des alten Namens). Gründe für die Umbenennung waren der Mangel an gescheiten Domains, schlechter Trefferchancen in Suchmaschinen sowie einer generellen Verwechslunggefahr mit der TV-Serie.

Seit dem 27. Mai 2007 ist ein neuer Kernel (kernel2 genannt) in Arbeit, welcher eine neue Version der [VFS](Virtuelles-Dateisystem "VFS")-Schnittstelle [LostIO](T%C3%BDndur-LostIO "LostIO") implementieren soll. Weitere geplante oder bereits implementierte Features sind Unterstützung für andere Architekturen (in erster Linie [x86-64](X86-64 "X86-64")), Mehrprozessorsysteme nach [SMP](Symmetrisches-Multiprozessorsystem "SMP")-Standard, sowie Threading. Aktuell werden die Arbeiten an kernel2 intensiviert, da dieser mit Version 0.3 zum Standardkernel werden soll.

## Versionen

**0.1.0, Codename Morgoth**  
Die erste Version des Community-OS. Der Feature-Freeze für die Version war am 09.04.2007, das Release erfolgte am 03.05.2007. Features waren:

- Speicher&Prozessverwaltung
- einfache Interprozesskommunikation
- Treiber für [DMA](Direct-Memory-Access "DMA"), [Diskettenlaufwerke](Floppy-Disk-Controller "FDC") und [Tastaturen](Keyboard-Controller "KBC")
- Einfache Textkonsolen
- Unterstützung für das FAT12-Dateisystem ([LostIO](T%C3%BDndur-LostIO "LostIO")-Treiber)
- eine einfache Shell

  
**0.1.1**  
Diese Version enthält Überarbeitungen und Bugfixes für Features der 0.1.0-Version. Neuerungen:

- optimierte RPC-Funktionen
- Puffer in LostIO
- Kernelseitige Kontrolle der IO-Ports

  
**0.2.0, Codename Gothmog**  
Das Release im Jahr 2008, und außerdem erste Version unter dem neuen Namen týndur. Offizielle Features:

- Treiber für ata und ext2
- Paketverwaltung lpt
- Pakete wie binutils, fpc (FreePascal), gcc und nano
- Netzwerkunterstützung mit Treiber für rtl8139 und sis900
- Tab-Completion und andere neue Möglichkeiten zum editieren der Kommandozeile in der Shell
- Editor kedit verbessert; neu ist unter anderem das Syntax-Highlighting für C (einschalten mit F8)
- Virtuelle Terminals (umschaltbar via Alt+Fx, Standardmäßig gibt es 4 Terminals)

Außerdem hat sich unter der Haube viel getan, die meisten Treiber basieren jetzt auf der Betriebssystemunabhängigen Schnittstelle [CDI](Common-Driver-Interface "CDI").

## Links

- [Die Webseite von týndur](http://www.tyndur.org/)
- [Builds von jeder Revision](http://nightlies.tyndur.org/)
- [WebSVN](http://svn.tyndur.org/)
- [Mailingliste](http://list.tyndur.org/mailman/listinfo) ([Archiv](http://list.tyndur.org/pipermail/tyndur-devel/))

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/3790/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1795/index.html)

<!-- MediaWiki page 1795; revision 3790; parent 3780; 2009-01-01T19:59:06Z -->
